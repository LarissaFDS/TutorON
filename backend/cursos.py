"""Curso e período do aluno (IC/UFAL), para dar contexto ao tutor.

O aluno escolhe no site o curso e o período. Isso:
1. diz à IA em que ponto do curso ele está (calibra o nível e as disciplinas de base);
2. ajuda o roteamento automático (backend/disciplina_auto.py) a achar o acervo certo: as
   disciplinas do período com material têm preferência.

Fonte: disciplinas/cursos.json (matrizes obrigatórias dos PPCs do IC/UFAL; sem eletivas).
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parents[1] / "disciplinas" / "cursos.json"


@lru_cache(maxsize=1)
def _dados() -> dict:
    return json.loads(ARQUIVO.read_text(encoding="utf-8"))


def publico() -> dict:
    """Lista enxuta para o site: cursos, períodos e as disciplinas de cada período."""
    d = _dados()
    return {"padrao": d["padrao"], "fonte": d["_fonte"], "cursos": [
        {"id": c["id"], "nome": c["nome"], "sigla": c["sigla"], "instituicao": c["instituicao"], "ppc": c["ppc"],
         "periodos": [{"numero": p["numero"], "disciplinas": [
             {"nome": x["nome"], "codigo": x.get("codigo"), "acervo": x.get("acervo")} for x in p["disciplinas"]]}
             for p in c["periodos"]]}
        for c in d["cursos"]]}


def curso(ident: str | None) -> dict | None:
    return next((c for c in _dados()["cursos"] if c["id"] == ident), None)


def valido(curso_id: str | None, periodo: int | None) -> bool:
    c = curso(curso_id)
    return bool(c) and (periodo is None or any(p["numero"] == periodo for p in c["periodos"]))


def _periodo(c: dict, n: int) -> list[dict]:
    return next((p["disciplinas"] for p in c["periodos"] if p["numero"] == n), [])


def preferidas(curso_id: str | None, periodo: int | None) -> tuple[str, ...]:
    """Acervos do período escolhido (preferência no roteamento). Sem período: vazio."""
    c = curso(curso_id)
    if not c or not periodo:
        return ()
    return tuple(dict.fromkeys(x["acervo"] for x in _periodo(c, periodo) if x.get("acervo")))


def perfil(curso_id: str | None, periodo: int | None, disciplina_atual: str | None = None) -> str | None:
    """Trecho de prompt com o perfil acadêmico do aluno (dados, não instruções)."""
    c = curso(curso_id)
    if not c:
        return None
    linhas = [f"Curso: {c['nome']} ({c['instituicao']})."]
    if periodo:
        atuais = [x["nome"] for x in _periodo(c, periodo)]
        linhas.append(f"Período: {periodo}º." + (f" Disciplinas obrigatórias deste período: {', '.join(atuais)}."
                                                 if atuais else " Período só de eletivas, estágio ou TCC."))
        vistas = [x["nome"] for p in c["periodos"] if p["numero"] < periodo for x in p["disciplinas"]]
        if vistas:
            linhas.append("Já cursou (em princípio): " + ", ".join(vistas[-14:]) + ".")
        if disciplina_atual:
            futuras = [p["numero"] for p in c["periodos"] for x in p["disciplinas"]
                       if x.get("acervo") == disciplina_atual and p["numero"] > periodo]
            if futuras:
                linhas.append(f"A disciplina da dúvida costuma ser do {futuras[0]}º período: o aluno pode estar adiantado "
                              "ou revisando; explique os pré-requisitos que ele ainda pode não ter visto.")
    linhas.append("Use isso só para calibrar o nível e os exemplos (relacione com disciplinas que ele já viu). "
                  "Não comente o perfil na resposta.")
    return "\n".join(linhas)
