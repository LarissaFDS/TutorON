"""Matriz de avaliação do TutorON: {modelo forte, lite} x {sem RAG, RAG atual} x {prompt atual, novo}.

Cada modelo também responde a pergunta crua, sem instruções nem material (braço "genérico"):
o mesmo modelo nos dois lados isola o efeito de RAG e prompt do efeito do modelo.

Etapas (cada uma retoma de onde parou; rodar de novo só faz o que falta):

    python eval/matriz.py gerar      # respostas -> eval/results/respostas.jsonl
    python eval/matriz.py julgar     # notas do juiz -> eval/results/notas.jsonl
    python eval/matriz.py relatorio  # eval/results/relatorio.md e resumo.json

Precisa de GEMINI_API_KEY no .env. Cada pergunta gera 10 respostas (2 modelos x 5 braços) e 10
julgamentos: 300 chamadas para 15 perguntas. Use outra chave, ou rode fora do horário de uso,
para não esgotar a cota do site. Um 429 aqui espera e tenta de novo no MESMO modelo: a matriz
nunca troca de modelo em silêncio.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "eval"))

from backend import prompts  # noqa: E402
from backend.config import load_settings  # noqa: E402
from backend.llm import LLM, AllUnavailable, Model  # noqa: E402
from backend.rag import contexto, recuperar  # noqa: E402
from prompt_candidato import SISTEMA_NOVO, prompt_novo  # noqa: E402

EVAL = ROOT / "eval"
RESULTS = EVAL / "results"
CONDICOES = ("generico", "atual_sem_rag", "atual_rag", "novo_sem_rag", "novo_rag")
CRITERIOS = {
    "a": "Recorrência/definição do subproblema antes do código",
    "b": "Pseudocódigo claro (sem linguagem específica)",
    "c": "Significado dos índices explicado (i-1, j-1…)",
    "d": "Organização e legibilidade",
    "e": "Correção matemática",
    "f": "Obedece pedidos de formato",
}
CRITERIOS_POR_TEMA = {
    "pd": "abcde", "dc": "abcde", "recorrencia": "acde", "lacos": "acde", "guloso": "de", "np": "de",
}


def criterios(q: dict) -> str:
    return CRITERIOS_POR_TEMA[q["tema"]] + ("f" if q.get("pedido_formato") else "")


# ---------------------------------------------------------------------- arquivos
def ler_jsonl(caminho: Path) -> list[dict]:
    if not caminho.exists():
        return []
    return [json.loads(linha) for linha in caminho.read_text(encoding="utf-8").splitlines() if linha.strip()]


def anexar(caminho: Path, registro: dict) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("a", encoding="utf-8") as f:
        f.write(json.dumps(registro, ensure_ascii=False) + "\n")


def perguntas(filtro: str | None = None) -> list[dict]:
    todas = json.loads((EVAL / "perguntas.json").read_text(encoding="utf-8"))
    return [q for q in todas if not filtro or any(f in q["id"] for f in filtro.split(","))]


def modelo(spec: str) -> Model:
    """'gemini-3.8-flash' ou 'ollama:qwen3:8b'."""
    provedor, _, nome = spec.partition(":") if spec.startswith(("gemini:", "ollama:")) else ("gemini", "", spec)
    return Model(provedor, nome)


# ---------------------------------------------------------------------- geração
def planos(q: dict, trechos) -> dict[str, tuple[str | None, str]]:
    texto = q["pergunta"]
    return {
        "generico": (None, prompts.prompt_generico(texto)),
        # Sem RAG = o que a produção envia quando a busca não acha nada.
        "atual_sem_rag": (prompts.SISTEMA_TUTOR, prompts.prompt_tutor(texto, contexto([]))),
        "atual_rag": (prompts.SISTEMA_TUTOR, prompts.prompt_tutor(texto, contexto(trechos, len(texto)))),
        "novo_sem_rag": (SISTEMA_NOVO, prompt_novo(texto, [])),
        "novo_rag": (SISTEMA_NOVO, prompt_novo(texto, trechos)),
    }


async def gerar_uma(llm: LLM, m: Model, sistema: str | None, prompt: str, esperas=(20, 45, 90, 180)) -> dict:
    """Sempre no mesmo modelo. Em 429/503, espera e tenta de novo; nunca cai para outro modelo."""
    tentativas: list[dict] = []
    for n in range(len(esperas) + 1):
        llm.breaker.reset(m)
        try:
            r = await llm.complete(sistema, prompt, models=[m])
            return {"texto": r.text, "segundos": round(r.seconds, 1), "tentativas": tentativas + r.attempts}
        except AllUnavailable as exc:
            tentativas += exc.attempts
            if n < len(esperas):
                print(f"      {m.name} indisponível ({[a.get('resultado') for a in exc.attempts]}); "
                      f"nova tentativa em {esperas[n]} s", flush=True)
                await asyncio.sleep(esperas[n])
    return {"texto": None, "erro": "modelo indisponível após novas tentativas", "tentativas": tentativas}


async def gerar(args) -> None:
    settings = load_settings()
    llm = LLM(settings)
    modelos = {"forte": modelo(args.forte), "lite": modelo(args.lite)}
    if any(m.provider == "gemini" for m in modelos.values()) and not settings.gemini_enabled:
        raise SystemExit("Falta GEMINI_API_KEY no .env (ou no ambiente).")
    busca = "hibrida (bge-m3)" if await llm.embed("teste") else "lexical (bge-m3 indisponível)"
    print(f"Busca do acervo: {busca}")
    saida = RESULTS / "respostas.jsonl"
    feitos = {(r["id"], r["papel"], r["condicao"]) for r in ler_jsonl(saida) if r.get("texto")}
    condicoes = args.condicoes.split(",")
    recuperacao = {r["id"]: r for r in ler_jsonl(RESULTS / "recuperacao.jsonl")}
    for q in perguntas(args.perguntas):
        trechos = await recuperar(q["pergunta"], llm, settings)
        if q["id"] not in recuperacao:
            recuperacao[q["id"]] = {"id": q["id"], "busca": busca, "trechos": [t.publico() for t in trechos]}
            anexar(RESULTS / "recuperacao.jsonl", recuperacao[q["id"]])
        plano = planos(q, trechos)
        for papel, m in modelos.items():
            for condicao in condicoes:
                if (q["id"], papel, condicao) in feitos:
                    continue
                print(f"[{q['id']}] {papel}={m.name} {condicao}…", flush=True)
                sistema, prompt = plano[condicao]
                r = await gerar_uma(llm, m, sistema, prompt)
                anexar(saida, {"id": q["id"], "papel": papel, "modelo": m.key, "condicao": condicao,
                               "busca": busca if condicao.endswith("_rag") and "sem" not in condicao else None,
                               "data": datetime.now().isoformat(timespec="seconds"), **r})
                print(f"    -> {'ok' if r.get('texto') else r.get('erro')} ({r.get('segundos', '-')} s)", flush=True)
                await asyncio.sleep(args.intervalo)
    await llm.client.aclose()


# ---------------------------------------------------------------------- juiz
SISTEMA_JUIZ = """Você é um professor de Projeto e Análise de Algoritmos avaliando UMA resposta dada a um aluno.
Você não sabe que sistema escreveu a resposta. Avalie só o que está escrito, comparando com a referência.
Dê nota de 1 a 5 em cada critério pedido (5 exemplar, 4 bom com deslize pequeno, 3 aceitável mas falta parte relevante,
2 fraco/vago/fora de ordem, 1 ausente ou errado). Seja exigente: 5 é raro.
Critérios:
a. Recorrência antes do código: o subproblema (o que cada posição da tabela/variável guarda) e a recorrência completa, com casos base, aparecem ANTES de qualquer código/pseudocódigo.
b. Pseudocódigo claro: pseudocódigo legível, independente de linguagem (Python/C/Java sem o aluno pedir vale no máximo 3), que dá para seguir à mão.
c. Significado dos índices: diz o que cada índice representa e por que aparecem i-1, j-1, w-w_i etc. (que vizinho/subproblema é cada um).
d. Organização: ordem didática, sem repetições, sem seções vazias ou blocos genéricos que não acrescentam nada.
e. Correção matemática: recorrência, casos base, contas, exemplos e complexidade corretos segundo a referência.
f. Obedece pedido de formato: entregou o formato pedido pelo aluno (esquema/tabela/diagrama, passo a passo, explicação mais fácil).
Responda só com JSON no formato {"a": {"nota": 4, "motivo": "..."}, ...}, apenas com os critérios pedidos; motivo com até 25 palavras."""


def prompt_juiz(q: dict, resposta: str) -> str:
    pedidos = ", ".join(f"{c} ({CRITERIOS[c]})" for c in criterios(q))
    return "\n".join([
        f"PERGUNTA DO ALUNO:\n{q['pergunta']}",
        f"\nPEDIDO DE FORMATO DO ALUNO: {q['pedido_formato']}" if q.get("pedido_formato") else "",
        f"\nREFERÊNCIA (gabarito resumido, para conferir a correção):\n{q['referencia']}",
        f"\nRESPOSTA AVALIADA:\n<<<\n{resposta}\n>>>",
        f"\nAvalie somente estes critérios: {pedidos}.",
    ])


async def chamar_juiz(llm: LLM, nome: str, prompt: str) -> dict:
    import httpx

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{nome}:generateContent"
    corpo = {"systemInstruction": {"parts": [{"text": SISTEMA_JUIZ}]},
             "contents": [{"role": "user", "parts": [{"text": prompt}]}],
             "generationConfig": {"temperature": 0, "responseMimeType": "application/json"}}
    for espera in (20, 45, 90, 180, None):
        try:
            r = await llm.client.post(url, json=corpo, headers={"x-goog-api-key": llm.settings.gemini_api_key},
                                      timeout=120)
            if r.status_code == 200:
                partes = r.json()["candidates"][0]["content"]["parts"]
                return json.loads("".join(p.get("text", "") for p in partes if not p.get("thought")))
            motivo = f"HTTP {r.status_code}"
        except (httpx.HTTPError, KeyError, IndexError, ValueError) as exc:
            motivo = type(exc).__name__
        if espera is None:
            raise RuntimeError(motivo)
        print(f"      juiz indisponível ({motivo}); nova tentativa em {espera} s", flush=True)
        await asyncio.sleep(espera)
    raise RuntimeError("juiz indisponível")


def validar_notas(bruto: dict, q: dict) -> dict:
    notas = {}
    for c in criterios(q):
        item = bruto.get(c) or {}
        nota = item.get("nota") if isinstance(item, dict) else item
        if not isinstance(nota, (int, float)) or not 1 <= nota <= 5:
            raise ValueError(f"nota inválida no critério {c}: {item!r}")
        notas[c] = {"nota": int(round(nota)), "motivo": str(item.get("motivo", ""))[:300] if isinstance(item, dict) else ""}
    return notas


async def julgar(args) -> None:
    settings = load_settings()
    if not settings.gemini_enabled:
        raise SystemExit("Falta GEMINI_API_KEY no .env (ou no ambiente).")
    llm = LLM(settings)
    qs = {q["id"]: q for q in perguntas()}
    saida = RESULTS / "notas.jsonl"
    feitos = {(n["id"], n["papel"], n["condicao"]) for n in ler_jsonl(saida)}
    for r in ler_jsonl(RESULTS / "respostas.jsonl"):
        chave = (r["id"], r["papel"], r["condicao"])
        if not r.get("texto") or chave in feitos or r["id"] not in qs:
            continue
        q = qs[r["id"]]
        print(f"[{r['id']}] julgando {r['papel']} {r['condicao']}…", flush=True)
        try:
            notas = validar_notas(await chamar_juiz(llm, args.juiz, prompt_juiz(q, r["texto"])), q)
        except (RuntimeError, ValueError) as exc:
            print(f"    -> sem nota: {exc}", flush=True)
            continue
        anexar(saida, {"id": r["id"], "papel": r["papel"], "modelo": r["modelo"], "condicao": r["condicao"],
                       "juiz": args.juiz, "notas": notas})
        feitos.add(chave)
        await asyncio.sleep(args.intervalo)
    await llm.client.aclose()


# ---------------------------------------------------------------------- relatório
def media(valores) -> float | None:
    valores = [v for v in valores if v is not None]
    return round(statistics.fmean(valores), 2) if valores else None


def nota_resposta(n: dict) -> float:
    return statistics.fmean(v["nota"] for v in n["notas"].values())


def fmt(x) -> str:
    return "–" if x is None else f"{x:.2f}"


def diferenca_pareada(notas: dict, a: tuple, b: tuple, ids: list[str]) -> dict:
    """Média de (a - b) nas perguntas em que os dois braços têm nota, e quantas vezes a venceu/perdeu."""
    difs = [notas[(i, *a)] - notas[(i, *b)] for i in ids if (i, *a) in notas and (i, *b) in notas]
    return {"dif": media(difs), "n": len(difs), "vence": sum(d > 0 for d in difs), "perde": sum(d < 0 for d in difs)}


def relatorio(args) -> dict:
    qs = {q["id"]: q for q in perguntas()}
    brutas = [n for n in ler_jsonl(RESULTS / "notas.jsonl") if n["id"] in qs]
    notas = {(n["id"], n["papel"], n["condicao"]): nota_resposta(n) for n in brutas}
    por_criterio = {(n["id"], n["papel"], n["condicao"]): {c: v["nota"] for c, v in n["notas"].items()} for n in brutas}
    modelos = {n["papel"]: n["modelo"] for n in brutas}
    papeis = [p for p in ("forte", "lite") if p in modelos]
    ids = list(qs)
    linhas = ["# Matriz de avaliação do TutorON", "",
              f"Gerado em {datetime.now():%d/%m/%Y %H:%M}. {len(brutas)} respostas julgadas, {len(ids)} perguntas. "
              "Nota = média dos critérios aplicáveis (1 a 5). Rubrica em `eval/rubrica.md`.", "",
              "## Média por braço", "", "| Braço | " + " | ".join(f"{p} ({modelos[p]})" for p in papeis) + " |",
              "|---|" + "---:|" * len(papeis)]
    for c in CONDICOES:
        linhas.append(f"| {c} | " + " | ".join(
            f"{fmt(media(notas.get((i, p, c)) for i in ids))} (n={sum((i, p, c) in notas for i in ids)})"
            for p in papeis) + " |")

    efeitos = {}
    for p in papeis:
        for nome, a, b in (("prompt (novo - atual), com RAG", "novo_rag", "atual_rag"),
                           ("prompt (novo - atual), sem RAG", "novo_sem_rag", "atual_sem_rag"),
                           ("RAG (com - sem), prompt atual", "atual_rag", "atual_sem_rag"),
                           ("RAG (com - sem), prompt novo", "novo_rag", "novo_sem_rag"),
                           ("TutorON atual - genérico", "atual_rag", "generico"),
                           ("TutorON novo - genérico", "novo_rag", "generico")):
            efeitos[f"{p}: {nome}"] = diferenca_pareada(notas, (p, a), (p, b), ids)
    if len(papeis) == 2:
        for c in CONDICOES:
            efeitos[f"modelo (forte - lite): {c}"] = diferenca_pareada(notas, ("forte", c), ("lite", c), ids)
    linhas += ["", "## Efeitos (diferença pareada por pergunta)", "",
               "| Comparação | Diferença média | Perguntas | Vence | Perde |", "|---|---:|---:|---:|---:|"]
    linhas += [f"| {k} | {fmt(v['dif'])} | {v['n']} | {v['vence']} | {v['perde']} |" for k, v in efeitos.items()]

    linhas += ["", "## As três perguntas originais do aluno (nota por critério)", ""]
    for i in [i for i in ids if qs[i].get("original_aluno")]:
        cs = criterios(qs[i])
        linhas += [f"**{i}**", "", "| Braço | " + " | ".join(cs) + " | média |", "|---|" + "---:|" * (len(cs) + 1)]
        for p in papeis:
            for c in CONDICOES:
                pc = por_criterio.get((i, p, c))
                if pc:
                    linhas.append(f"| {p} {c} | " + " | ".join(str(pc.get(x, "–")) for x in cs) +
                                  f" | {fmt(notas[(i, p, c)])} |")
        linhas.append("")

    criterio_sucesso = {}
    for p in papeis:
        gen = media(notas.get((i, p, "generico")) for i in ids)
        novo = media(notas.get((i, p, "novo_rag")) for i in ids)
        originais_ok = all(por_criterio.get((i, p, "novo_rag"), {}).get(c, 0) >= 4
                           for i in ids if qs[i].get("original_aluno") for c in "abd")
        criterio_sucesso[p] = {"novo_rag": novo, "generico": gen,
                               "iguala_ou_supera": None if gen is None or novo is None else novo >= gen,
                               "originais_a_b_d_ao_menos_4": originais_ok}
    linhas += ["## Critério de sucesso (braço novo_rag)", ""]
    for p, v in criterio_sucesso.items():
        linhas.append(f"- {p}: novo_rag {fmt(v['novo_rag'])} x genérico {fmt(v['generico'])} -> "
                      f"{'iguala ou supera' if v['iguala_ou_supera'] else 'abaixo'}; "
                      f"perguntas originais com a, b e d >= 4: {'sim' if v['originais_a_b_d_ao_menos_4'] else 'não'}.")
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "relatorio.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    resumo = {"modelos": modelos, "efeitos": efeitos, "criterio_sucesso": criterio_sucesso}
    (RESULTS / "resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n".join(linhas))
    return resumo


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="etapa", required=True)
    g = sub.add_parser("gerar")
    g.add_argument("--forte", default="gemini-3.8-flash")
    g.add_argument("--lite", default="gemini-3.1-flash-lite")
    g.add_argument("--condicoes", default=",".join(CONDICOES))
    g.add_argument("--perguntas", help="filtro por id, separado por vírgula (ex.: A1,A2)")
    g.add_argument("--intervalo", type=float, default=4.0, help="segundos entre chamadas (poupa a cota)")
    j = sub.add_parser("julgar")
    j.add_argument("--juiz", default="gemini-3.8-flash")
    j.add_argument("--intervalo", type=float, default=4.0)
    sub.add_parser("relatorio")
    args = parser.parse_args()
    inicio = time.monotonic()
    if args.etapa == "gerar":
        asyncio.run(gerar(args))
    elif args.etapa == "julgar":
        asyncio.run(julgar(args))
    else:
        relatorio(args)
    print(f"\nConcluído em {time.monotonic() - inicio:.0f} s.")


if __name__ == "__main__":
    main()
