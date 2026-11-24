"""Identificação da disciplina pelo vocabulário do acervo (todas as disciplinas cadastradas).

Complementa as regras fixas de `disciplina_auto.py`, que só cobrem algumas disciplinas:
1. Nome citado: "Sistemas de Controle", "Circuitos Digitais" etc. no texto decidem.
2. Vocabulário: cada disciplina vira um vetor TF-IDF (nome, assuntos, títulos e começo dos blocos do
   acervo). A dúvida (com peso maior) e o arquivo/contexto são comparados com todos; só decide
   quando a melhor disciplina se destaca com folga. Sem dependências novas; carrega uma vez.
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from functools import lru_cache

from acervo.curate import searchable
from acervo.disciplinas import REGISTRO, todas

PALAVRA = re.compile(r"\b[a-z][a-z0-9]{3,}\b")
VAZIAS = set("""
para como qual quais esse essa este esta isso isto aqui onde quando porque pois entao assim sobre entre
mais menos muito muita pelo pela pelos pelas uma umas uns sendo seja sera foram fazer feito faca
temos tem tenho voce voces pode podem deve devem cada todo toda todos todas outro outra outros outras
mesmo mesma ainda apenas sempre nunca depois antes agora parte partes caso casos exemplo exemplos
questao questoes resposta respostas resolucao lista listas prova provas pagina paginas aluno alunos
professor material dados valor valores tipo tipos forma formas primeiro segunda segundo terceiro
calcule determine mostre explique encontre considere usando usar utilize seguinte seguintes figura
item itens anotacoes conferida conferidas equipe validada status tutoron pendente revisao
""".split())

MIN_SCORE = 0.08
FOLGA = 1.25


def _tokens(texto: str) -> list[str]:
    return [t for t in PALAVRA.findall(searchable(texto or "")) if t not in VAZIAS]


def _nomes(d, extra: dict) -> list[str]:
    nomes = [d.nome] + list(extra.get(d.id, ()))
    return [searchable(n) for n in nomes if n and len(n) >= 6]


@lru_cache(maxsize=1)
def _modelo() -> tuple[dict[str, dict[str, float]], dict[str, list[str]]]:
    cadastro = json.loads(REGISTRO.read_text(encoding="utf-8"))
    extra = {x["id"]: x.get("nomes_nos_cursos", []) for x in cadastro["disciplinas"]}
    contagens: dict[str, Counter] = {}
    nomes: dict[str, list[str]] = {}
    for d in todas():
        partes = [d.nome, d.nome, " ".join(a.replace("-", " ") for a in d.assuntos)]
        try:
            itens = json.loads(d.itens.read_text(encoding="utf-8"))
            itens = itens if isinstance(itens, list) else itens.get("itens", [])
        except (OSError, ValueError):
            itens = []
        for it in itens:
            partes += [str(it.get("titulo", "")), str(it.get("assunto", "")).replace("-", " "),
                       str(it.get("texto", ""))[:1500]]
        contagens[d.id] = Counter(_tokens("\n".join(partes)))
        nomes[d.id] = _nomes(d, extra)
    n = len(contagens)
    df = Counter(t for c in contagens.values() for t in c)
    idf = {t: math.log((n + 1) / (k + 0.5)) for t, k in df.items()}
    vetores = {}
    for ident, c in contagens.items():
        v = {t: (1 + math.log(k)) * idf[t] for t, k in c.items() if idf[t] > 0.3}
        norma = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vetores[ident] = {t: x / norma for t, x in v.items()}
    return vetores, nomes


def nome_citado(texto: str) -> str | None:
    """Disciplina cujo nome aparece no texto ("Sistemas de controle 1 · UFAL" -> controle)."""
    normal = searchable(texto or "")
    achadas = {i for i, ns in _modelo()[1].items() for nome in ns if re.search(r"\b" + re.escape(nome) + r"\b", normal)}
    if len(achadas) > 1:  # "Sistemas" de Controle e de "Sistemas Digitais": fica o nome mais longo
        maior = max(achadas, key=lambda i: max(len(n) for n in _modelo()[1][i] if n in normal))
        return maior
    return next(iter(achadas), None)


def pontuar(pergunta: str, contexto: str = "") -> list[tuple[str, float]]:
    vetores, _ = _modelo()
    consulta = Counter()
    for t in _tokens(pergunta):
        consulta[t] += 2.0
    for t in _tokens((contexto or "")[:8000]):
        consulta[t] += 1.0
    if not consulta:
        return []
    q = {t: 1 + math.log(k) for t, k in consulta.items()}
    norma = math.sqrt(sum(x * x for x in q.values())) or 1.0
    notas = [(i, sum(q[t] * v.get(t, 0.0) for t in q) / norma) for i, v in vetores.items()]
    return sorted(notas, key=lambda x: x[1], reverse=True)


def identificar_lexico(pergunta: str, contexto: str = "", preferidas=()) -> str | None:
    notas = pontuar(pergunta, contexto)
    if not notas:
        return None
    if preferidas:  # disciplinas do período do aluno ganham um pequeno empurrão
        notas = sorted(((i, s * (1.15 if i in preferidas else 1.0)) for i, s in notas), key=lambda x: x[1], reverse=True)
    (melhor, s1), (_, s2) = notas[0], notas[1] if len(notas) > 1 else ("", 0.0)
    # Nota boa com folga, ou nota baixa (dúvida curta) com folga bem maior.
    if (s1 >= MIN_SCORE and s1 >= FOLGA * max(s2, 1e-9)) or (s1 >= 0.04 and s1 >= 1.7 * max(s2, 1e-9)):
        return melhor
    return None
