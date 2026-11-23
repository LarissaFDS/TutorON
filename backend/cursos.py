"""Curso e período do aluno (IC/UFAL), para dar contexto ao tutor.

O aluno escolhe no site o curso e o período. Isso:
1. diz à IA em que ponto do curso ele está (calibra o nível e as disciplinas de base);
2. ajuda o roteamento automático (backend/disciplina_auto.py) a achar o acervo certo: as
   disciplinas do período com material têm preferência.

Fonte: disciplinas/cursos.json (matrizes obrigatórias dos PPCs do IC/UFAL; sem eletivas).

Nenhuma disciplina com material fica fora da janela: além da ligação pelo nome, o cadastro pode
dizer onde ela fica em cada curso (`"cursos": {"cc": 6}` ou `{"cc": "eletiva"}`), e toda
disciplina disponível que não cair em nenhum período de um curso entra no grupo
"Eletivas, ênfases e outras" desse curso.
"""
from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parents[1] / "disciplinas" / "cursos.json"
CADASTRO = Path(__file__).resolve().parents[1] / "disciplinas" / "disciplinas.json"


def _chave(nome: str) -> str:
    """Nome sem acento, caixa e pontuação: "Computação, Sociedade e Ética" -> "computacao sociedade e etica"."""
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def _acervos_por_nome(cadastro: dict) -> dict[str, str]:
    """Nome normalizado -> id do acervo, para as disciplinas disponíveis (fora de "em validação").

    Vale o `nome` da disciplina e cada nome de `nomes_nos_cursos` (como ela aparece na matriz de
    algum curso, quando o nome é outro). Assim toda disciplina nova liga sozinha às matrizes.
    """
    mapa: dict[str, str] = {}
    for d in cadastro.get("disciplinas", []):
        if d.get("situacao") == "em validação":
            continue
        for nome in [d["nome"], *d.get("nomes_nos_cursos", [])]:
            mapa.setdefault(_chave(nome), d["id"])
    return mapa


GRUPO_ELETIVAS = "Eletivas, ênfases e outras"


def _disponiveis(cadastro: dict) -> list[dict]:
    return [d for d in cadastro.get("disciplinas", []) if d.get("situacao") != "em validação"]


def _ligar_acervos(dados: dict, cadastro: dict) -> dict:
    """Preenche `acervo` nas matrizes e monta o grupo de eletivas de cada curso.

    1. Um `acervo` escrito em cursos.json tem prioridade; senão, liga pelo nome (ou `nomes_nos_cursos`).
    2. O campo `cursos` do cadastro (curso -> período) põe a disciplina naquele período, se ainda não estiver.
    3. Toda disciplina disponível que não ficou em nenhum período do curso vai para `eletivas`.
    """
    por_nome = _acervos_por_nome(cadastro)
    disponiveis = _disponiveis(cadastro)
    ids = {d["id"] for d in cadastro.get("disciplinas", [])}
    for c in dados["cursos"]:
        for p in c["periodos"]:
            for x in p["disciplinas"]:
                if x.get("acervo") in ids:
                    continue
                auto = por_nome.get(_chave(x["nome"]))
                if auto:
                    x["acervo"] = auto
                else:
                    x.pop("acervo", None)
        periodos = {p.get("numero"): p for p in c["periodos"]}
        for d in disponiveis:
            n = (d.get("cursos") or {}).get(c.get("id"))
            if isinstance(n, int) and not isinstance(n, bool) and n in periodos:
                lista = periodos[n]["disciplinas"]
                if not any(x.get("acervo") == d["id"] for x in lista):
                    lista.append({"nome": d["nome"], "codigo": None, "acervo": d["id"], "extra": True})
        na_grade = {x.get("acervo") for p in c["periodos"] for x in p["disciplinas"]}
        c["eletivas"] = [{"nome": d["nome"], "codigo": None, "acervo": d["id"]}
                         for d in sorted(disponiveis, key=lambda d: _chave(d["nome"])) if d["id"] not in na_grade]
    return dados


@lru_cache(maxsize=1)
def _dados() -> dict:
    dados = json.loads(ARQUIVO.read_text(encoding="utf-8"))
    cadastro = json.loads(CADASTRO.read_text(encoding="utf-8"))
    return _ligar_acervos(dados, cadastro)


def publico() -> dict:
    """Lista enxuta para o site: cursos, períodos e as disciplinas de cada período."""
    d = _dados()
    return {"padrao": d["padrao"], "fonte": d["_fonte"], "cursos": [
        {"id": c["id"], "nome": c["nome"], "sigla": c["sigla"], "instituicao": c["instituicao"], "ppc": c["ppc"],
         "periodos": [{"numero": p["numero"], "disciplinas": [
             {"nome": x["nome"], "codigo": x.get("codigo"), "acervo": x.get("acervo")} for x in p["disciplinas"]]}
             for p in c["periodos"]],
         "eletivas": {"nome": GRUPO_ELETIVAS, "disciplinas": c.get("eletivas", [])}}
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
        atuais = [x["nome"] for x in _periodo(c, periodo) if not x.get("extra")]
        linhas.append(f"Período: {periodo}º." + (f" Disciplinas obrigatórias deste período: {', '.join(atuais)}."
                                                 if atuais else " Período só de eletivas, estágio ou TCC."))
        vistas = [x["nome"] for p in c["periodos"] if p["numero"] < periodo for x in p["disciplinas"]
                  if not x.get("extra")]
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
