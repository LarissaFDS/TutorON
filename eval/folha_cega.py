"""Folha cega para o aluno reavaliar as 3 perguntas originais.

Para cada pergunta original, junta as respostas do modelo forte nos braços genérico,
TutorON atual (atual_rag) e TutorON novo (novo_rag), embaralha e rotula como A, B e C.
O juiz Gemini é só triagem: a nota do aluno é a validação final.

    python eval/folha_cega.py [--papel forte] [--semente 7] [--manter-citacoes]

Saída:
    eval/results/folha_cega.md        para imprimir ou enviar ao aluno (não revela os braços)
    eval/results/folha_cega_mapa.json quem é A/B/C em cada pergunta (NÃO enviar ao aluno)

As citações ([P1], [L2], "(Lista 5, p. 7-8)", "(Livro, p. 48)") são retiradas por padrão:
só as respostas com RAG as têm, e elas entregariam qual resposta usa o material da disciplina.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matriz  # noqa: E402

BRACOS = ("generico", "atual_rag", "novo_rag")
ESCALA = {
    "a": "A ideia da tabela (o que cada posição guarda) e a recorrência, com os casos base, vêm ANTES do código.",
    "b": "O pseudocódigo é claro e dá para seguir à mão, sem depender de uma linguagem específica.",
    "c": "Explica o que cada índice significa e por que aparecem i-1, j-1 (que subproblema cada um é).",
    "d": "A resposta é bem organizada: dá para estudar por ela sem se perder.",
    "e": "As contas, o exemplo e a complexidade estão corretos.",
    "f": "Entregou o formato que foi pedido (esquema, passo a passo…).",
}
CITACAO = re.compile(
    r"\s?\[(?:[PL]\d+(?:\s*,\s*[PL]\d+)*)\]"                       # [P1], [P1, L2]
    r"|\s?\((?:Lista \d+|Livro|Prova|Material da disciplina)[^()]*\)"  # (Lista 5, p. 7-8)
)


def sem_citacoes(texto: str) -> str:
    return CITACAO.sub("", texto)


def montar(respostas: list[dict], papel: str, semente: int | None, manter_citacoes: bool) -> tuple[str, dict]:
    qs = [q for q in matriz.perguntas() if q.get("original_aluno")]
    por_chave = {(r["id"], r["papel"], r["condicao"]): r for r in respostas if r.get("texto")}
    sorteio = random.Random(semente) if semente is not None else random.SystemRandom()
    linhas = ["# Avaliação de respostas de PAA", "",
              "Cada pergunta tem três respostas, A, B e C, em ordem sorteada. Elas vêm de sistemas diferentes, "
              "mas você não sabe qual é qual. Leia as três e dê uma nota de 1 a 5 em cada item "
              "(1 = muito ruim, 3 = aceitável, 5 = excelente). No fim de cada pergunta, escolha a que mais ajuda "
              "a estudar para a prova.", ""]
    mapa = {"gerado_em": datetime.now().isoformat(timespec="seconds"), "papel": papel,
            "citacoes_removidas": not manter_citacoes, "perguntas": {}}
    for numero, q in enumerate(qs, 1):
        disponiveis = [b for b in BRACOS if (q["id"], papel, b) in por_chave]
        if len(disponiveis) < len(BRACOS):
            faltam = sorted(set(BRACOS) - set(disponiveis))
            raise SystemExit(f"{q['id']}: faltam respostas de {papel} em {faltam}. Rode `matriz.py gerar` antes.")
        sorteio.shuffle(disponiveis)
        rotulos = dict(zip("ABC", disponiveis))
        mapa["perguntas"][q["id"]] = {letra: {"condicao": b, "modelo": por_chave[(q["id"], papel, b)]["modelo"]}
                                      for letra, b in rotulos.items()}
        criterios = matriz.criterios(q)
        linhas += ["---", "", f"## Pergunta {numero}", "", q["pergunta"], ""]
        for letra, braco in rotulos.items():
            texto = por_chave[(q["id"], papel, braco)]["texto"]
            linhas += [f"### Resposta {letra}", "", texto if manter_citacoes else sem_citacoes(texto), "",
                       f"**Suas notas para a resposta {letra}** (1 a 5)", "", "| Item | Nota |", "|---|---|"]
            linhas += [f"| {ESCALA[c]} | ___ |" for c in criterios]
            linhas.append("")
        linhas += ["**Qual resposta você prefere?** ( ) A  ( ) B  ( ) C", "",
                   "**O que ajudou ou ficou confuso?** (opcional)", "", "", ""]
    return "\n".join(linhas), mapa


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--papel", default="forte", help="forte ou lite")
    parser.add_argument("--semente", type=int, help="semente do sorteio (para reproduzir a mesma folha)")
    parser.add_argument("--manter-citacoes", action="store_true")
    args = parser.parse_args()
    folha, mapa = montar(matriz.ler_jsonl(matriz.RESULTS / "respostas.jsonl"), args.papel, args.semente,
                         args.manter_citacoes)
    matriz.RESULTS.mkdir(parents=True, exist_ok=True)
    (matriz.RESULTS / "folha_cega.md").write_text(folha, encoding="utf-8")
    (matriz.RESULTS / "folha_cega_mapa.json").write_text(json.dumps(mapa, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Folha: {matriz.RESULTS / 'folha_cega.md'}\nMapa (não enviar ao aluno): {matriz.RESULTS / 'folha_cega_mapa.json'}")


if __name__ == "__main__":
    main()
