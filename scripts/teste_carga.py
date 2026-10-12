"""Simula alunos usando o site ao mesmo tempo (pelo endereço público ou local).

Cada "aluno" faz uma validação completa (gera A/B, espera, vota) ou uma pergunta no
modo Tutor. Mede o tempo de cada um e falha se qualquer requisição der erro.
Os registros gerados ficam marcados com o curso "teste-carga" para serem removidos.

Uso: python scripts/teste_carga.py URL [--validacoes 4] [--perguntas 4]
"""
from __future__ import annotations

import argparse
import asyncio
import random
import sys
import time

import httpx

PERGUNTAS = [
    "Qual a complexidade do merge sort e por quê?",
    "Como resolver T(n) = 4T(n/2) + n pelo Teorema Mestre?",
    "Explique a recorrência da mochila 0/1.",
    "Por que o problema do caixeiro viajante é NP-difícil?",
    "Quantas comparações faz a busca binária no pior caso?",
    "O que é um invariante de laço? Dê um exemplo com insertion sort.",
    "Como o algoritmo de Kruskal garante a árvore geradora mínima?",
    "Qual a diferença entre programação dinâmica e divisão e conquista?",
    "Como provar por indução que 1+2+...+n = n(n+1)/2?",
    "Por que o quicksort é O(n²) no pior caso?",
]


async def acompanhar(c: httpx.AsyncClient, ident: str, erros: list) -> dict:
    while True:
        r = await c.get(f"/api/tarefas/{ident}")
        if r.status_code != 200:
            erros.append(f"GET tarefa HTTP {r.status_code}: {r.text[:120]}")
            return {"status": "erro"}
        t = r.json()
        if t["status"] in ("pronta", "erro"):
            return t
        await asyncio.sleep(1)


async def validacao(c, n, erros, tempos):
    inicio = time.monotonic()
    r = await c.post("/api/comparar", json={"pergunta": PERGUNTAS[n % len(PERGUNTAS)] + f" (teste {n})"})
    if r.status_code != 200:
        erros.append(f"validação {n}: POST HTTP {r.status_code} {r.text[:120]}")
        return
    t = await acompanhar(c, r.json()["id"], erros)
    if t["status"] != "pronta" or not t.get("A") or not t.get("B"):
        erros.append(f"validação {n}: {t.get('mensagem')}")
        return
    notas = {"clareza": random.randint(1, 5), "confianca": random.randint(1, 5), "utilidade": random.randint(1, 5),
             "erro_matematico": False}
    r = await c.post("/api/avaliar", json={"sessao": t["sessao"], "preferida": random.choice("AB"), "A": notas,
                                           "B": notas, "curso": "teste-carga"})
    if r.status_code != 200:
        erros.append(f"validação {n}: voto HTTP {r.status_code} {r.text[:120]}")
        return
    tempos.append(("validação", time.monotonic() - inicio))


async def pergunta(c, n, erros, tempos):
    inicio = time.monotonic()
    r = await c.post("/api/perguntar", json={"pergunta": PERGUNTAS[(n + 5) % len(PERGUNTAS)]})
    if r.status_code != 200:
        erros.append(f"pergunta {n}: POST HTTP {r.status_code} {r.text[:120]}")
        return
    t = await acompanhar(c, r.json()["id"], erros)
    if t["status"] != "pronta" or len(t.get("texto", "")) < 50:
        erros.append(f"pergunta {n}: {t.get('mensagem')}")
        return
    tempos.append(("tutor", time.monotonic() - inicio))


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--validacoes", type=int, default=4)
    ap.add_argument("--perguntas", type=int, default=4)
    a = ap.parse_args()
    erros, tempos = [], []
    async with httpx.AsyncClient(base_url=a.url.rstrip("/"), timeout=60) as c:
        trabalhos = [validacao(c, i, erros, tempos) for i in range(a.validacoes)]
        trabalhos += [pergunta(c, i, erros, tempos) for i in range(a.perguntas)]
        inicio = time.monotonic()
        await asyncio.gather(*trabalhos)
    for tipo in ("validação", "tutor"):
        ts = sorted(t for k, t in tempos if k == tipo)
        if ts:
            print(f"{tipo}: {len(ts)} ok | mínimo {ts[0]:.0f} s | mediana {ts[len(ts) // 2]:.0f} s | máximo {ts[-1]:.0f} s")
    print(f"total {time.monotonic() - inicio:.0f} s | erros: {len(erros)}")
    for e in erros:
        print("  ERRO", e)
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
