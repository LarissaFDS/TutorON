"""Cota de tokens por usuário (protótipo do plano gratuito, como o ChatGPT/Claude fazem).

- Cada visitante é identificado por um cookie anônimo `tutoron_id` (modo convidado, sem login).
  Sem cookie (ex.: CLI), vale o IP.
- Cada um tem `limite` tokens numa janela de `janela_h` horas. A janela começa no primeiro uso;
  quando o saldo acaba, o servidor responde 429 dizendo quando a cota volta.
- Tokens são ESTIMADOS (caracteres / 4) da pergunta + contexto + resposta. O Gemini e o Ollama
  devolvem a contagem exata; trocar a estimativa por ela é o próximo passo (ver docs/hospedagem-e-precos.md).
- Desenvolvedor: quem envia a chave `TUTORON_DEV_CHAVE` (cookie `tutoron_dev`, aberto uma vez em
  /dev?chave=...) ou acessa desta máquina não tem limite.

Estado salvo em dados/cota.json (suficiente para um servidor só; em produção iria para um banco).
"""
from __future__ import annotations

import json
import secrets
import threading
import time
from pathlib import Path

PLANOS = [
    {"id": "gratis", "nome": "Grátis", "preco_mes": 0, "tokens_janela": 40_000, "janela_h": 5,
     "descricao": "Cerca de 15 a 25 dúvidas a cada 5 horas. Sem cadastro."},
    {"id": "estudante", "nome": "Estudante", "preco_mes": 14.90, "tokens_janela": 400_000, "janela_h": 5,
     "descricao": "10x o grátis, fotos e animações sem fila."},
    {"id": "intensivo", "nome": "Intensivo (provas)", "preco_mes": 29.90, "tokens_janela": 1_500_000, "janela_h": 5,
     "descricao": "Para semanas de prova: praticamente sem limite."},
    {"id": "instituicao", "nome": "Instituição", "preco_mes": None, "tokens_janela": None, "janela_h": None,
     "descricao": "Licença por turma/curso, preço sob consulta (R$ 3 a 6 por aluno/mês)."},
]


def estimar_tokens(*textos: str | None) -> int:
    return sum(len(t) for t in textos if t) // 4 + 1


class Cota:
    def __init__(self, arquivo: Path, limite: int, janela_h: float, chave_dev: str = ""):
        self.arquivo = arquivo
        self.limite = limite
        self.janela_s = janela_h * 3600
        self.chave_dev = chave_dev
        self._trava = threading.Lock()
        self._uso: dict[str, dict] = {}
        if arquivo.exists():
            try:
                self._uso = json.loads(arquivo.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                self._uso = {}

    @property
    def ativa(self) -> bool:
        return self.limite > 0

    def eh_dev(self, chave: str | None) -> bool:
        return bool(self.chave_dev and chave and secrets.compare_digest(chave, self.chave_dev))

    def _registro(self, quem: str) -> dict:
        agora = time.time()
        r = self._uso.get(quem)
        if not r or agora - r["inicio"] >= self.janela_s:
            r = {"inicio": agora, "usados": 0}
            self._uso[quem] = r
        return r

    def situacao(self, quem: str, dev: bool = False) -> dict:
        if dev or not self.ativa:
            return {"plano": "dev" if dev else "sem_limite", "ilimitado": True}
        with self._trava:
            r = self._registro(quem)
            return {"plano": "gratis", "ilimitado": False, "limite": self.limite,
                    "usados": r["usados"], "restantes": max(0, self.limite - r["usados"]),
                    "renova_em": r["inicio"] + self.janela_s}

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
            self._registro(quem)["usados"] += tokens
            self._salvar()

    def _registrar(self, quem: str, tokens: int, dev: bool, tipo: str) -> None:
        """Histórico permanente no PC (dados/uso.jsonl): uma linha por cobrança, inclusive dev."""
        linha = {"data": time.strftime("%Y-%m-%dT%H:%M:%S"), "quem": quem, "tokens": tokens,
                 "dev": dev, "tipo": tipo}
        try:
            with self._trava, open(self.arquivo.with_name("uso.jsonl"), "a", encoding="utf-8") as f:
                f.write(json.dumps(linha, ensure_ascii=False) + "\n")
        except OSError:
            pass

    def relatorio(self) -> list[dict]:
        """Uso por aluno (cookie anônimo ou IP), do maior para o menor."""
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
            r["restantes_agora"] = None if s["ilimitado"] else s["restantes"]
        return sorted(por.values(), key=lambda r: -r["tokens"])

    def _salvar(self) -> None:
        agora = time.time()
        self._uso = {k: v for k, v in self._uso.items() if agora - v["inicio"] < self.janela_s}
        try:
            self.arquivo.parent.mkdir(parents=True, exist_ok=True)
            self.arquivo.write_text(json.dumps(self._uso), encoding="utf-8")
        except OSError:
            pass
