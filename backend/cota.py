"""Cota diária de tokens por usuário e planos (protótipo; pagamento SIMULADO, sem API de pagamento).

- Cada visitante é identificado por um cookie anônimo `tutoron_id` (modo convidado, sem login).
  Sem cookie (ex.: CLI), vale o IP.
- Plano grátis: `limite` tokens por dia. Com janela de 24 h (padrão), a cota renova à meia-noite
  (horário do servidor); com outra janela (ex.: 5 h), a janela começa no primeiro uso.
- Planos pagos (Estudante, Intensivo) são ativados por um checkout simulado em /planos: nenhum dado
  de cartão é guardado além dos 4 últimos dígitos digitados, e nada é cobrado. Plano ativo = cota
  maior e "modo completo" (Gemini primeiro, com raciocínio; o grátis usa o modelo local primeiro,
  conforme docs/precificacao-tutoron.md).
- Administrador: quem acessa desta máquina ou envia a chave `TUTORON_DEV_CHAVE` (cookie `tutoron_dev`,
  aberto uma vez em /dev?chave=...) não tem limite e sempre usa o modo completo.
- Tokens são ESTIMADOS (caracteres / 4) da pergunta + contexto + resposta.

Estado em dados/cota.json (uso do dia) e dados/planos.json (assinaturas simuladas). Com o banco
configurado (backend/banco.py), o uso do dia, os planos, o histórico e o limite próprio de cada conta
(perfis.limite_tokens, definido no painel /admin) ficam no Supabase; os arquivos viram só cópia local.
"""
from __future__ import annotations

import datetime as dt
import json
import secrets
import threading
import logging
import time
from pathlib import Path

logger = logging.getLogger("tutoron.cota")

PLANOS = [
    {"id": "gratis", "nome": "Grátis", "preco_mes": 0, "tokens_dia": 40_000, "modo": "padrao",
     "descricao": "Cerca de 20 dúvidas por dia, sem cadastro.",
     "recursos": ["Tutor socrático em todas as disciplinas", "Fotos do caderno", "Modelo local (pode ter fila)"]},
    {"id": "estudante", "nome": "Estudante", "preco_mes": 14.90, "tokens_dia": 400_000, "modo": "completo",
     "destaque": True, "descricao": "Para o semestre inteiro: 10x o grátis e o modo completo.",
     "recursos": ["Tudo do Grátis", "Modo completo: IA mais forte primeiro (Gemini)", "Animações e fotos sem fila",
                  "Cerca de 200 dúvidas por dia"]},
    {"id": "intensivo", "nome": "Intensivo", "preco_mes": 29.90, "tokens_dia": 1_500_000, "modo": "completo",
     "descricao": "Para semanas de prova: praticamente sem limite.",
     "recursos": ["Tudo do Estudante", "Cerca de 750 dúvidas por dia", "Prioridade na fila do servidor"]},
    {"id": "instituicao", "nome": "Instituição", "preco_mes": None, "tokens_dia": None, "modo": "completo",
     "descricao": "Licença por turma ou curso (R$ 3 a 6 por aluno/mês).",
     "recursos": ["Painel de uso por turma", "Material do professor no acervo", "Contrato e nota fiscal"]},
]
PAGOS = {p["id"]: p for p in PLANOS if p["preco_mes"]}


def estimar_tokens(*textos: str | None) -> int:
    return sum(len(t) for t in textos if t) // 4 + 1


class Cota:
    def __init__(self, arquivo: Path, limite: int, janela_h: float = 24, chave_dev: str = "", banco=None):
        self.arquivo = arquivo
        self.banco = banco
        self._limites: dict[str, int | None] = {}  # limite próprio da conta (None = o do plano)
        self.limite = limite
        self.janela_s = janela_h * 3600
        self.diaria = janela_h == 24
        self.chave_dev = chave_dev
        self._trava = threading.Lock()
        self._uso: dict[str, dict] = self._ler(arquivo)
        self._planos: dict[str, dict] = self._ler(arquivo.with_name("planos.json"))
        if banco:
            try:
                self._planos = {p["quem"]: p for p in banco.selecionar("planos", {"select": "*"})}
            except Exception as exc:  # noqa: BLE001 - banco fora do ar não derruba o servidor
                logger.warning("Planos não carregados do banco: %s", exc)

    @staticmethod
    def _ler(arquivo: Path) -> dict:
        try:
            return json.loads(arquivo.read_text(encoding="utf-8")) if arquivo.exists() else {}
        except (OSError, ValueError):
            return {}

    @property
    def ativa(self) -> bool:
        return self.limite > 0

    def eh_dev(self, chave: str | None) -> bool:
        return bool(self.chave_dev and chave and secrets.compare_digest(chave, self.chave_dev))

    # ------------------------------------------------------------------ janela
    def _inicio_janela(self, agora: float) -> float:
        if self.diaria:
            hoje = dt.datetime.fromtimestamp(agora).replace(hour=0, minute=0, second=0, microsecond=0)
            return hoje.timestamp()
        return agora

    def _expirou(self, r: dict, agora: float) -> bool:
        if self.diaria:
            return r["inicio"] < self._inicio_janela(agora)
        return agora - r["inicio"] >= self.janela_s

    def _renova_em(self, r: dict) -> float:
        if self.diaria:
            return (dt.datetime.fromtimestamp(r["inicio"]) + dt.timedelta(days=1)).replace(
                hour=0, minute=0, second=0, microsecond=0).timestamp()
        return r["inicio"] + self.janela_s

    def _registro(self, quem: str) -> dict:
        agora = time.time()
        r = self._uso.get(quem)
        if not r or self._expirou(r, agora):
            r = {"inicio": self._inicio_janela(agora), "usados": self._usados_no_banco(quem, agora)}
            self._uso[quem] = r
        return r

    def _dia(self, inicio: float) -> str:
        return dt.date.fromtimestamp(inicio).isoformat()

    def _usados_no_banco(self, quem: str, agora: float) -> int:
        """Outro servidor (ou um reinício) pode já ter cobrado hoje: o banco é a fonte de verdade."""
        if not (self.banco and self.diaria):
            return 0
        try:
            linhas = self.banco.selecionar("cota_diaria", {"quem": "eq." + quem,
                                                           "dia": "eq." + self._dia(self._inicio_janela(agora)),
                                                           "select": "usados"})
            return int(linhas[0]["usados"]) if linhas else 0
        except Exception as exc:  # noqa: BLE001
            logger.warning("Uso do dia não lido do banco: %s", exc)
            return 0

    # ------------------------------------------------------------------ limite por conta (admin)
    def limite_proprio(self, quem: str) -> int | None:
        if quem not in self._limites:
            self._limites[quem] = None
            if self.banco and quem.startswith("u:"):
                try:
                    linhas = self.banco.selecionar("perfis", {"id": "eq." + quem[2:], "select": "limite_tokens"})
                    self._limites[quem] = linhas[0].get("limite_tokens") if linhas else None
                except Exception as exc:  # noqa: BLE001
                    logger.warning("Limite da conta não lido do banco: %s", exc)
                    self._limites.pop(quem, None)
                    return None
        return self._limites[quem]

    def definir_limite(self, quem: str, limite: int | None) -> None:
        """Limite diário próprio da conta (None volta ao do plano). Usado no painel /admin."""
        if limite is not None and limite < 0:
            raise ValueError("Limite inválido.")
        self._limites[quem] = limite
        if self.banco and quem.startswith("u:"):
            self.banco.atualizar("perfis", {"id": "eq." + quem[2:]}, {"limite_tokens": limite})

    def zerar(self, quem: str) -> None:
        """Devolve o limite de hoje (para testes da equipe)."""
        with self._trava:
            r = self._registro(quem)
            r["usados"] = 0
            self._salvar()
        self._gravar_dia(quem, r)

    def _gravar_dia(self, quem: str, r: dict) -> None:
        if self.banco and self.diaria:
            self.banco.inserir("cota_diaria", {"quem": quem, "dia": self._dia(r["inicio"]), "usados": r["usados"]},
                               upsert="quem,dia")

    # ------------------------------------------------------------------ planos (simulados)
    def plano(self, quem: str) -> dict:
        p = self._planos.get(quem)
        return PAGOS.get(p["plano"], PLANOS[0]) if p else PLANOS[0]

    def ativar_plano(self, quem: str, plano_id: str, final_cartao: str = "") -> dict:
        if plano_id not in PAGOS:
            raise ValueError("Plano inválido.")
        with self._trava:
            self._planos[quem] = {"plano": plano_id, "desde": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                  "cartao": final_cartao[-4:], "simulado": True}
            self._salvar_planos()
        if self.banco:
            self.banco.inserir("planos", {"quem": quem} | self._planos[quem], upsert="quem")
        self._registrar(quem, 0, False, "plano:" + plano_id)
        return self._planos[quem]

    def cancelar_plano(self, quem: str) -> None:
        with self._trava:
            if self._planos.pop(quem, None) is not None:
                self._salvar_planos()
        if self.banco:
            try:
                self.banco.apagar("planos", {"quem": "eq." + quem})
            except Exception as exc:  # noqa: BLE001
                logger.warning("Plano não cancelado no banco: %s", exc)

    def limite_de(self, quem: str) -> int:
        proprio = self.limite_proprio(quem)
        if proprio is not None:
            return proprio
        p = self.plano(quem)
        return self.limite if p["id"] == "gratis" else int(p["tokens_dia"])

    def modo(self, quem: str, dev: bool = False) -> str:
        """'completo' (Gemini primeiro) para plano pago e administrador; 'padrao' no grátis."""
        return "completo" if dev or self.plano(quem)["modo"] == "completo" else "padrao"

    # ------------------------------------------------------------------ consulta e cobrança
    def situacao(self, quem: str, dev: bool = False) -> dict:
        p = self.plano(quem)
        base = {"plano": p["id"], "plano_nome": p["nome"], "modo": self.modo(quem, dev), "admin": dev,
                "assinatura": self._planos.get(quem)}
        if dev or not self.ativa:
            return base | {"plano": "dev" if dev else p["id"], "ilimitado": True}
        limite = self.limite_de(quem)
        with self._trava:
            r = self._registro(quem)
            return base | {"ilimitado": False, "limite": limite, "usados": r["usados"],
                           "restantes": max(0, limite - r["usados"]), "renova_em": self._renova_em(r),
                           "diaria": self.diaria}

    def pode(self, quem: str, dev: bool = False) -> bool:
        s = self.situacao(quem, dev)
        return s["ilimitado"] or s["restantes"] > 0

    def cobrar(self, quem: str, tokens: int, dev: bool = False, tipo: str = "") -> None:
        if tokens <= 0:
            return
        self._registrar(quem, tokens, dev, tipo)
        if dev or not self.ativa:
            return
        with self._trava:
            r = self._registro(quem)
            r["usados"] += tokens
            self._salvar()
        self._gravar_dia(quem, r)

    def _registrar(self, quem: str, tokens: int, dev: bool, tipo: str) -> None:
        """Histórico permanente no PC (dados/uso.jsonl): uma linha por cobrança, inclusive dev."""
        linha = {"data": time.strftime("%Y-%m-%dT%H:%M:%S"), "quem": quem, "tokens": tokens,
                 "dev": dev, "tipo": tipo, "plano": self.plano(quem)["id"]}
        if self.banco:
            self.banco.inserir("uso_tokens", linha)
        try:
            with self._trava, open(self.arquivo.with_name("uso.jsonl"), "a", encoding="utf-8") as f:
                f.write(json.dumps(linha, ensure_ascii=False) + "\n")
        except OSError:
            pass

    def relatorio(self) -> list[dict]:
        """Uso por aluno (conta, cookie anônimo ou IP), do maior para o menor."""
        if self.banco:
            try:
                por = {r["quem"]: dict(r) for r in self.banco.selecionar("uso_por_usuario", {"select": "*"})}
            except Exception as exc:  # noqa: BLE001
                logger.warning("Relatório não lido do banco: %s", exc)
                por = {}
            for r in por.values():
                s = self.situacao(r["quem"])
                r["plano"] = s["plano"]
                r["limite"] = None if s["ilimitado"] else s["limite"]
                r["restantes_agora"] = None if s["ilimitado"] else s["restantes"]
            return sorted(por.values(), key=lambda r: -r["tokens"])
        por: dict[str, dict] = {}
        caminho = self.arquivo.with_name("uso.jsonl")
        if caminho.exists():
            for texto in caminho.read_text(encoding="utf-8").splitlines():
                try:
                    l = json.loads(texto)
                except ValueError:
                    continue
                r = por.setdefault(l["quem"], {"quem": l["quem"], "tokens": 0, "perguntas": 0,
                                               "fotos": 0, "animacoes": 0, "primeiro": l["data"], "dev": False})
                r["tokens"] += l["tokens"]
                r["ultimo"] = l["data"]
                r["dev"] = r["dev"] or l.get("dev", False)
                t = l.get("tipo")
                if t in ("pergunta", "comparacao"): r["perguntas"] += 1
                elif t == "foto": r["fotos"] += 1
                elif t == "animacao": r["animacoes"] += 1
        for r in por.values():
            s = self.situacao(r["quem"])
            r["plano"] = s["plano"]
            r["restantes_agora"] = None if s["ilimitado"] else s["restantes"]
        return sorted(por.values(), key=lambda r: -r["tokens"])

    def _salvar(self) -> None:
        agora = time.time()
        self._uso = {k: v for k, v in self._uso.items() if not self._expirou(v, agora)}
        self._gravar(self.arquivo, self._uso)

    def _salvar_planos(self) -> None:
        self._gravar(self.arquivo.with_name("planos.json"), self._planos)

    @staticmethod
    def _gravar(arquivo: Path, dados: dict) -> None:
        try:
            arquivo.parent.mkdir(parents=True, exist_ok=True)
            arquivo.write_text(json.dumps(dados, ensure_ascii=False), encoding="utf-8")
        except OSError:
            pass
