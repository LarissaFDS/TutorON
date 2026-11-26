"""Coleta para o painel /admin: feedbacks, erros reportados, perguntas e respostas e conversas.

Lê do banco (Supabase) quando ele está configurado; sem banco, ou se a leitura falhar, lê os arquivos de
`dados/`. Nada é apagado nem movido: linhas de teste só ganham a marca `teste` e o painel as esconde.

Quem é do IC: e-mail institucional (domínios em TUTORON_DOMINIOS_IC, padrão ic.ufal.br) -> "email";
aluno que marcou "sou do IC" num feedback (pode usar e-mail pessoal) -> "declarado".
"""
from __future__ import annotations

import json
import logging
import re
from typing import Any

logger = logging.getLogger("tutoron.painel")

RESPOSTA_MAX = 4000  # caracteres de cada resposta enviados ao painel (o texto completo fica no banco)


def eh_teste(registro: dict) -> bool:
    texto = json.dumps(registro, ensure_ascii=False).lower()
    return any(m in texto for m in ("teste-carga", "teste_carga", "pytest", "[teste]"))


def _linhas_banco(banco, tabela: str, limite: int, select: str = "id,criado_em,usuario,dados",
                  ordem: str = "criado_em.desc") -> list[dict]:
    return banco.selecionar(tabela, {"select": select, "order": ordem, "limit": str(limite)})


def _linhas_arquivo(registro, nome: str, limite: int) -> list[dict]:
    linhas = registro.ler(nome)[-limite:] if registro else []
    return [{"id": str(r.get("id") or ""), "criado_em": r.get("data"), "usuario": r.get("usuario"), "dados": r}
            for r in reversed(linhas)]


def _ler(banco, registro, tabela: str, arquivo: str, limite: int) -> tuple[list[dict], str]:
    if banco:
        try:
            return _linhas_banco(banco, tabela, limite), "banco"
        except Exception as exc:  # noqa: BLE001 - tabela ausente ou banco fora do ar: cai para os arquivos
            logger.warning("Painel: %s não lida do banco (%s); usando dados/", tabela, exc)
    return _linhas_arquivo(registro, arquivo, limite), "arquivos"


def _ic_do_email(email: str | None, dominios: tuple[str, ...]) -> bool:
    email = (email or "").lower()
    return any(email.endswith("@" + d) or email.endswith("." + d) for d in dominios)


def categoria(d: dict) -> str:
    tipo = d.get("tipo") or "resposta"
    if d.get("erro_matematico"):
        return "erro"
    if tipo == "disciplina":
        return "disciplina"
    if tipo == "leitura":
        return "leitura" if d.get("util") is False else "positivo"
    if tipo == "conversa" or d.get("sugestao") or d.get("ajudou_em"):
        return "escrito"
    if d.get("util") is True:
        return "positivo"
    if d.get("util") is False:
        return "negativo"
    return "escrito"


def coletar(banco, registro, dominios_ic: tuple[str, ...] = ("ic.ufal.br",), limite: int = 400) -> dict[str, Any]:
    perfis: dict[str, dict] = {}
    if banco:
        try:
            perfis = {"u:" + p["id"]: p for p in banco.selecionar("perfis", {"select": "id,email,nome"})}
        except Exception as exc:  # noqa: BLE001
            logger.warning("Painel: perfis não lidos (%s)", exc)

    feedback, fonte = _ler(banco, registro, "feedback", "feedback.jsonl", limite)
    perguntas, _ = _ler(banco, registro, "perguntas", "perguntas.jsonl", limite)
    conversas: list[dict] = []
    if banco:
        try:
            conversas = _linhas_banco(banco, "conversas", min(limite, 200),
                                      "id,usuario,titulo,atualizado_em,dados", "atualizado_em.desc")
        except Exception as exc:  # noqa: BLE001
            logger.warning("Painel: conversas não lidas (%s)", exc)

    declarados = {f.get("usuario") for f in feedback if f.get("usuario") and (f.get("dados") or {}).get("aluno_ic")}

    def pessoa(usuario: str | None) -> dict:
        p = perfis.get(usuario or "", {})
        email = p.get("email")
        ic = "email" if _ic_do_email(email, dominios_ic) else ("declarado" if usuario in declarados else None)
        return {"usuario": usuario, "email": email, "nome": p.get("nome"), "ic": ic}

    por_id = {}
    saida_perguntas = []
    for linha in perguntas:
        d = linha.get("dados") or {}
        item = {"id": linha.get("id") or d.get("id"), "data": linha.get("criado_em") or d.get("data"),
                **pessoa(linha.get("usuario")),
                "disciplina": d.get("disciplina"), "ajuda": d.get("ajuda"), "pergunta": d.get("pergunta") or "",
                "contexto": (d.get("contexto") or "")[:1500], "foto": bool(d.get("leitura_foto")),
                "resposta": (d.get("resposta") or "")[:RESPOSTA_MAX], "erro": d.get("erro"),
                "bloqueio": d.get("bloqueio"), "modelo": d.get("modelo"), "provedor": d.get("provedor"),
                "segundos": d.get("segundos"), "rodada": d.get("rodada"), "travou": d.get("travou"),
                "teste": eh_teste(d)}
        por_id[item["id"]] = item
        saida_perguntas.append(item)

    saida_feedback = []
    for linha in feedback:
        d = linha.get("dados") or {}
        ref = str(d.get("id") or linha.get("id") or "")
        p = por_id.get(ref) or por_id.get(re.sub(r"-(d|f[0-9a-z]+)$", "", ref)) or {}
        if p:
            p.setdefault("votos", []).append(categoria(d))
        saida_feedback.append({
            "id": linha.get("id"), "data": linha.get("criado_em") or d.get("data"), **pessoa(linha.get("usuario")),
            "categoria": categoria(d), "tipo": d.get("tipo") or "resposta", "util": d.get("util"),
            "nota": d.get("nota"), "erro_matematico": bool(d.get("erro_matematico")),
            "comentario": d.get("comentario") or "", "ajudou_em": d.get("ajudou_em") or "",
            "sugestao": d.get("sugestao") or "", "aluno_ic": d.get("aluno_ic"), "rodadas": d.get("rodadas"),
            "disciplina": d.get("disciplina") or p.get("disciplina"),
            "pergunta": d.get("pergunta") or p.get("pergunta") or "", "resposta": p.get("resposta") or "",
            "ajuda": p.get("ajuda"), "teste": eh_teste(d)})

    saida_conversas = []
    for c in conversas:
        dados = c.get("dados") or {}
        saida_conversas.append({"id": c.get("id"), "data": c.get("atualizado_em"), **pessoa(c.get("usuario")),
                                "titulo": c.get("titulo") or "", "trocas": (dados.get("trocas") or [])[-40:]})

    return {"fonte": fonte, "dominios_ic": list(dominios_ic), "feedbacks": saida_feedback,
            "perguntas": saida_perguntas, "conversas": saida_conversas}
