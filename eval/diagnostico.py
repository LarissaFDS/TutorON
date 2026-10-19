"""Diagnóstico da Fase 1: roteamento de modelos (pelos logs) e recuperação do acervo.

    python eval/diagnostico.py roteamento [--logs dados/perguntas.jsonl ...]
    python eval/diagnostico.py recuperacao
    python eval/diagnostico.py calibrar      # limiar ACERVO_SIMILARIDADE_MINIMA (precisa do bge-m3)

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

    # Campos gravados a partir do PR de observabilidade (retry_delay_s, cota, degradado).
    cotas = defaultdict(list)
    for r in regs:
        for t in r.get("tentativas", []):
            if t["resultado"] == "HTTP 429":
                cotas[t["modelo"]].append((t.get("cota") or "não informada", t.get("retry_delay_s")))
    com_campo = [r for r in regs if "degradado" in r]
    linhas += ["", "## Cota esgotada e respostas degradadas", ""]
    if not com_campo and not any(c != "não informada" for lista in cotas.values() for c, _ in lista):
        linhas.append("Estes logs são anteriores ao registro de cota e de degradação (`cota`, `retry_delay_s`, "
                      "`degradado`). Rode de novo com um log novo.")
    else:
        linhas += [f"Respostas degradadas (lite depois de falha dos melhores): "
                   f"{sum(bool(r['degradado']) for r in com_campo)} de {len(com_campo)}.", "",
                   "| Modelo | 429 por dia | 429 por minuto | sem informação | retryDelay máximo (s) |",
                   "|---|---:|---:|---:|---:|"]
        for m, lista in cotas.items():
            tipos = Counter(c for c, _ in lista)
            esperas = [d for _, d in lista if d is not None]
            linhas.append(f"| {m} | {tipos['por_dia']} | {tipos['por_minuto']} | {tipos['não informada']} | "
                          f"{max(esperas) if esperas else '–'} |")
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


# ---------------------------------------------------------------------- calibração do corte
# Blocos que hoje acertam (ou que foram criados para a pergunta) e não podem sumir com o corte.
# Ids ausentes do índice são ignorados (os e0x só existem depois de reindexar com o PR de curadoria).
ESPERADOS = {
    "A1-mochila-01": ["e01"],
    "A2-subset-sum": ["e02", "1a81ca283132-q8-8"],
    "A3-substring-comum": ["e03", "1a81ca283132-q5-5"],
    "P1-robo-matriz-facil": ["e05", "1a81ca283132-q2-2"],
    "P3-troco-pd": ["e04"],
    "D1-algoritmo-x": ["c01", "c02"],
    "N1-np-reducao": ["c09"],
}
LIMIARES = [round(0.40 + 0.025 * i, 3) for i in range(13)]  # 0,40 a 0,70


def tabela_calibracao(sims: dict, temas: dict, esperados: dict, limiares=LIMIARES, k: int = 4) -> list[dict]:
    """sims: {pergunta: [(id_bloco, assunto, similaridade_ajustada)]}. Para cada limiar, simula o corte
    e o top-k por similaridade (aproximação do RRF, que também usa o BM25)."""
    linhas = []
    for limiar in limiares:
        passam = mesmo = vazias = 0
        perdidos = []
        for qid, blocos in sims.items():
            acima = sorted((b for b in blocos if b[2] >= limiar), key=lambda b: -b[2])
            top = acima[:k]
            passam += len(top)
            mesmo += sum(b[1] in ASSUNTO_POR_TEMA[temas[qid]] for b in top)
            vazias += not top
            presentes = {b[0] for b in blocos}
            ids_acima = {b[0] for b in acima}
            perdidos += [f"{qid}:{e}" for e in esperados.get(qid, []) if e in presentes and e not in ids_acima]
        linhas.append({"limiar": limiar, "blocos": passam, "mesmo_assunto": mesmo, "vazias": vazias,
                       "esperados_perdidos": perdidos})
    return linhas


def recomendar(linhas: list[dict]) -> float | None:
    seguros = [l["limiar"] for l in linhas if not l["esperados_perdidos"]]
    return max(seguros) if seguros else None


def calibrar() -> str:
    from acervo import models
    from acervo.retrieval import cosine

    indice = json.loads((ROOT / "04-rag/indice.json").read_text(encoding="utf-8"))
    if not indice.get("vectors"):
        raise SystemExit("O índice não tem embeddings: rode `python -m acervo indexar --embeddings` antes.")
    try:
        from acervo.retrieval import hub_scores
        hubs, com_hub = hub_scores(indice["vectors"]), True
    except ImportError:  # sem o PR de recuperação: calibra sem a penalidade
        hubs, com_hub = [0.0] * len(indice["vectors"]), False
    qs = json.loads((ROOT / "eval/perguntas.json").read_text(encoding="utf-8"))
    try:
        vetores = [models.embeddings([q["pergunta"]], indice["embedding_model"])[0] for q in qs]
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f"bge-m3 indisponível ({type(exc).__name__}): rode no servidor com o Ollama ligado.")
    sims = {q["id"]: [(c["id"], c["assunto"], cosine(v, w) - h)
                      for c, w, h in zip(indice["chunks"], indice["vectors"], hubs)] for q, v in zip(qs, vetores)}
    temas = {q["id"]: q["tema"] for q in qs}
    linhas = tabela_calibracao(sims, temas, ESPERADOS)
    sugestao = recomendar(linhas)
    texto = ["# Calibração do corte de relevância", "",
             f"{len(qs)} perguntas do conjunto dourado, {len(indice['chunks'])} blocos, "
             f"penalidade de hub {'ligada' if com_hub else 'DESLIGADA (sem o PR de recuperação)'}. "
             "Top 4 por similaridade ajustada (aproximação: a produção também usa o BM25 na ordem).", "",
             "| Limiar | Blocos que entram | Do mesmo assunto | Perguntas sem material | Acertos conhecidos perdidos |",
             "|---:|---:|---:|---:|---|"]
    for l in linhas:
        pct = f"{100 * l['mesmo_assunto'] / l['blocos']:.0f}%" if l["blocos"] else "–"
        texto.append(f"| {l['limiar']:.3f} | {l['blocos']} | {l['mesmo_assunto']} ({pct}) | {l['vazias']} | "
                     f"{', '.join(l['esperados_perdidos']) or '–'} |")
    texto += ["", f"**Sugestão:** ACERVO_SIMILARIDADE_MINIMA={sugestao:.3f} (o maior limiar sem perder acertos conhecidos)."
              if sugestao is not None else "**Sem sugestão:** todo limiar testado perde algum acerto conhecido.",
              "Antes de fixar no .env, confira a coluna de perguntas sem material: uma pergunta de PAA sem nenhum "
              "bloco é aceitável quando o acervo não cobre o assunto, mas não para PD, que agora tem material."]
    return "\n".join(texto) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="etapa", required=True)
    r = sub.add_parser("roteamento")
    r.add_argument("--logs", nargs="+", default=[str(ROOT / "dados/perguntas.jsonl"),
                                                 str(ROOT / "06-avaliacao/resultados-mvp.json")])
    sub.add_parser("recuperacao")
    sub.add_parser("calibrar")
    parser.add_argument("--saida", help="pasta do relatório (padrão: eval/results); vem antes da etapa")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if args.etapa == "roteamento":
        texto = roteamento([Path(c) for c in args.logs if Path(c).exists()])
    elif args.etapa == "calibrar":
        texto = calibrar()
    else:
        texto = recuperacao()
    pasta = Path(args.saida).resolve() if args.saida else RESULTS
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / f"diagnostico-{args.etapa}.md").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
