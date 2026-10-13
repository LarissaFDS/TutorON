"""Diagnóstico da Fase 1: roteamento de modelos (pelos logs) e recuperação do acervo.

    python eval/diagnostico.py roteamento [--logs dados/perguntas.jsonl ...]
    python eval/diagnostico.py recuperacao

Não chama nenhum modelo de resposta. A recuperação usa o bge-m3 do Ollama se estiver
ligado; sem ele, cai para a busca léxica (como a produção faria) e o relatório diz isso.
Saída em eval/results/diagnostico-*.md.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

RESULTS = ROOT / "eval" / "results"
ASSUNTO_POR_TEMA = {
    "pd": {"b2-04-programacao-dinamica"},
    "dc": {"b1-02-divisao-e-conquista"},
    "guloso": {"b1-03-algoritmos-gulosos"},
    "np": {"b2-06-np-completude", "b2-07-lidando-com-np-completude", "b2-05-transformacao-de-problemas"},
    "recorrencia": {"b1-01-corretude-complexidade", "b1-02-divisao-e-conquista"},
    "lacos": {"b1-01-corretude-complexidade"},
}


def _hora(texto: str) -> datetime:
    return datetime.fromisoformat(texto)


# ---------------------------------------------------------------------- roteamento
def registros_de_log(caminhos: list[Path]) -> list[dict]:
    """Respostas do modo Tutor (dados/perguntas.jsonl) e as do braço tutoron_gemini da avaliação do MVP."""
    regs = []
    for caminho in caminhos:
        if caminho.suffix == ".jsonl":
            for linha in caminho.read_text(encoding="utf-8").splitlines():
                if linha.strip():
                    r = json.loads(linha)
                    regs.append({**r, "fonte_log": caminho.name})
        else:  # 06-avaliacao/resultados-mvp.json
            for r in json.loads(caminho.read_text(encoding="utf-8")):
                if r.get("condicao") == "tutoron_gemini":
                    regs.append({**r, "fonte_log": caminho.name})
    return regs


def roteamento(caminhos: list[Path]) -> str:
    regs = registros_de_log(caminhos)
    linhas = ["# Diagnóstico de roteamento", "",
              "Fontes: " + ", ".join(f"`{c.name}`" for c in caminhos) + f". {len(regs)} respostas.", ""]
    for fonte in sorted({r["fonte_log"] for r in regs}) + ["(todas)"]:
        sub = [r for r in regs if fonte in ("(todas)", r["fonte_log"])]
        usados = Counter(r.get("modelo") or "erro" for r in sub)
        linhas += [f"## Modelo que respondeu: {fonte}", "", "| Modelo | Respostas | % |", "|---|---:|---:|"]
        linhas += [f"| {m} | {n} | {100 * n / len(sub):.0f}% |" for m, n in usados.most_common()]
        linhas.append("")

    # O que aconteceu com cada modelo da cascata antes de alguém responder.
    resultado = defaultdict(Counter)
    for r in regs:
        for t in r.get("tentativas", []):
            motivo = t["resultado"]
            motivo = "cancelado (outro respondeu antes)" if motivo.startswith("cancelado") else motivo
            resultado[t["modelo"]][motivo] += 1
    motivos = sorted({m for c in resultado.values() for m in c})
    linhas += ["## Resultado de cada modelo nas tentativas", "",
               "| Modelo | " + " | ".join(motivos) + " |", "|---|" + "---:|" * len(motivos)]
    linhas += [f"| {m} | " + " | ".join(str(c.get(x, 0)) for x in motivos) + " |" for m, c in resultado.items()]

    # Pausa: do último erro (429/503/tempo) de um modelo até a última vez que ele foi "pulado (em pausa)".
    com_data = sorted((r for r in regs if r.get("data")), key=lambda r: r["data"])
    pausas = defaultdict(list)
    ultimo_erro: dict[str, tuple[datetime, str]] = {}
    for r in com_data:
        quando = _hora(r["data"])
        for t in r.get("tentativas", []):
            if t["resultado"].startswith(("HTTP", "tempo", "sem resposta")):
                ultimo_erro[t["modelo"]] = (quando, t["resultado"])
            elif t["resultado"] == "pulado (em pausa)" and t["modelo"] in ultimo_erro:
                inicio, motivo = ultimo_erro[t["modelo"]]
                pausas[t["modelo"]].append(((quando - inicio).total_seconds() / 60, motivo))
    linhas += ["", "## Tempo em pausa observado (limite inferior)", "",
               "Do último erro de cada modelo até a última pergunta em que ele foi pulado por estar em pausa. "
               "Pelo código (`backend/llm.py`), um 429 pausa por max(60 s, retryDelay do Google), até 1 h; "
               "503 pausa 20 s; tempo esgotado, 30 s.", "",
               "| Modelo | Erro que causou a pausa | Pausa observada (min) |", "|---|---|---:|"]
    for m, lista in pausas.items():
        maior = max(lista)
        linhas.append(f"| {m} | {maior[1]} | ≥ {maior[0]:.0f} |")

    ollama = Counter(t["resultado"] for r in regs for t in r.get("tentativas", []) if t["modelo"].startswith("ollama:"))
    linhas += ["", "## Papel do modelo local na corrida", "",
               f"Tentativas do `ollama:*` nestes logs: {dict(ollama) or 'nenhuma'}. "
               f"Respostas servidas pelo local: {sum(1 for r in regs if r.get('provedor') == 'ollama')}."]
    return "\n".join(linhas) + "\n"


# ---------------------------------------------------------------------- recuperação
def hubness(k: int = 4) -> list[tuple[int, dict]]:
    """Quantas vezes cada bloco aparece entre os k vizinhos mais próximos dos outros blocos (k-ocorrência).
    Um 'hub' do embedding aparece perto de quase tudo, inclusive de perguntas sem relação."""
    from acervo.retrieval import cosine

    indice = json.loads((ROOT / "04-rag/indice.json").read_text(encoding="utf-8"))
    chunks, vetores = indice["chunks"], indice["vectors"]
    contagem = Counter()
    for i, v in enumerate(vetores):
        sims = sorted(((cosine(v, w), j) for j, w in enumerate(vetores) if j != i), reverse=True)[:k]
        contagem.update(j for _, j in sims)
    return [(contagem[j], chunks[j]) for j in sorted(range(len(chunks)), key=lambda j: -contagem[j])]


def _nome(item: dict) -> str:
    fonte = item["fonte_original"].replace("\\", "/").split("/")[-1]
    return fonte.replace("página(s): ", "p. ")


def recuperacao() -> str:
    from acervo import models
    from acervo.retrieval import search

    indice = json.loads((ROOT / "04-rag/indice.json").read_text(encoding="utf-8"))
    try:
        models.embeddings(["teste"], indice.get("embedding_model") or "bge-m3")
        semantica = True
    except Exception:  # noqa: BLE001 - Ollama ou bge-m3 ausentes
        semantica = False
    qs = json.loads((ROOT / "eval/perguntas.json").read_text(encoding="utf-8"))
    linhas = ["# Diagnóstico de recuperação", "",
              f"Índice `04-rag/indice.json`: {len(indice['chunks'])} blocos, modo {indice['modo']}. "
              f"Consulta desta execução: {'híbrida (bge-m3)' if semantica else 'SÓ LÉXICA (bge-m3 indisponível nesta máquina)'}.",
              "", "Relevância por assunto: o bloco é do mesmo assunto da pergunta (b2-04 para PD etc.). "
              "É um critério grosseiro: um bloco do assunto certo ainda pode tratar de outro problema.", ""]
    contagem = Counter()
    relevantes = total = 0
    for q in qs:
        itens = search(q["pergunta"], k=4, semantic=semantica)
        linhas += [f"### {q['id']} ({q['tema']})", "",
                   "| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |", "|---:|---|---|---:|---:|---:|---|"]
        if not itens:
            linhas.append("| – | nenhum bloco passou do filtro | | | | | |")
        for n, it in enumerate(itens, 1):
            ok = it["assunto"] in ASSUNTO_POR_TEMA[q["tema"]]
            relevantes += ok
            total += 1
            contagem[_nome(it)] += 1
            sim = it.get("similaridade")
            linhas.append(f"| {n} | {_nome(it)} — {it['texto'].splitlines()[0][:60]} | {it['assunto']} | "
                          f"{it['score']:.4f} | {it.get('score_lexico', 0):.2f} | {'–' if sim is None else f'{sim:.3f}'} | "
                          f"{'sim' if ok else 'NÃO'} |")
        linhas.append("")
    linhas += ["## Resumo", "", f"- Blocos do mesmo assunto da pergunta: {relevantes}/{total}.",
               "- Blocos que mais aparecem: " + ", ".join(f"{n} ({c}x)" for n, c in contagem.most_common(5)) + "."]
    if indice.get("vectors"):
        linhas += ["", "## Hubness do embedding (sem consulta)", "",
                   "k-ocorrência com k=4: quantas vezes o bloco está entre os 4 vizinhos mais próximos dos outros "
                   f"{len(indice['chunks']) - 1} blocos. Média esperada = 4.", "",
                   "| k-ocorrência | Bloco | Assunto | Tamanho (car.) |", "|---:|---|---|---:|"]
        for c, ch in hubness()[:8]:
            linhas.append(f"| {c} | {_nome(ch)} — {ch['texto'].splitlines()[0][:50]} | {ch['assunto']} | {len(ch['texto'])} |")
    return "\n".join(linhas) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="etapa", required=True)
    r = sub.add_parser("roteamento")
    r.add_argument("--logs", nargs="+", default=[str(ROOT / "dados/perguntas.jsonl"),
                                                 str(ROOT / "06-avaliacao/resultados-mvp.json")])
    sub.add_parser("recuperacao")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if args.etapa == "roteamento":
        texto = roteamento([Path(c) for c in args.logs if Path(c).exists()])
    else:
        texto = recuperacao()
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / f"diagnostico-{args.etapa}.md").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
