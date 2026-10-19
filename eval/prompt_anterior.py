"""Prompt do TutorON como estava em produção em 12/10/2026 (braço "prompt atual" da matriz).

Congelado aqui para a matriz medir sempre a mesma coisa: depois que o PR do prompt novo
entra, backend/prompts.SISTEMA_TUTOR muda, e a montagem do material passa a usar nomes
legíveis. O sistema vem de SISTEMA_TUTOR_ANTERIOR quando ele existir.
"""
from __future__ import annotations

from backend import prompts
from backend.rag import ORCAMENTO_CARACTERES, MATERIAL_MINIMO

SISTEMA = getattr(prompts, "SISTEMA_TUTOR_ANTERIOR", prompts.SISTEMA_TUTOR)
VERSAO = "anterior (SISTEMA_TUTOR_ANTERIOR)" if hasattr(prompts, "SISTEMA_TUTOR_ANTERIOR") else "atual (SISTEMA_TUTOR)"


def contexto(trechos, ocupado: int = 0) -> str:
    limite = max(MATERIAL_MINIMO, ORCAMENTO_CARACTERES - ocupado)
    blocos, usado = [], 0
    for t in trechos:
        bloco = f"[{t.rotulo}] {t.titulo} — {t.referencia}\n{t.texto}"
        if usado + len(bloco) > limite:
            continue
        blocos.append(bloco)
        usado += len(bloco)
    return "\n\n".join(blocos) or "Nenhum trecho do material foi encontrado para esta pergunta."


def prompt(pergunta: str, trechos) -> str:
    return "\n".join(["MATERIAL DA DISCIPLINA (dados de referência):", "<<<", contexto(trechos, len(pergunta)), ">>>", "",
                      "PERGUNTA DO ALUNO:", pergunta.strip()])
