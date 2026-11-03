"""Roteamento conservador: escolhe acervo só quando há sinais claros no enunciado."""
from __future__ import annotations

import re

from acervo.curate import searchable

REGRAS = {
    'sd': (r'\bkarnaugh\b', r'\bportas?\s+(?:logicas?|and|or|xor|nand|nor|not|e|ou)\b',
           r'\bcircuito\b', r'\btabela.?verdade\b|tabela de verdade', r'flip.?flop|\blatch\b',
           r'\bcomplemento de (?:2|dois)\b', r'\bbinari[oa]\b', r'\bboolean[oa]\b',
           r'\b(?:vhdl|hdl|rtl|multiplexador|decodificador|registrador|somador|subtrator)\b',
           r'\b(?:moore|mealy)\b', r'\bsistemas digitais\b'),
    'paa': (r'\b(?:algoritmo|algoritmos|recorrencia|mochila|bfs|dfs|dijkstra)\b',
            r'\b(?:recursao|pilha|fila)\b',
            r'\bteorema mestre\b', r'\bprogramacao dinamica\b', r'\b(?:grafo|grafos)\b',
            r'\bnp.?complet|\bnp.?dific', r'\b(?:fluxo maximo|fluxo residual|capacidade residual)\b',
            r'\b(?:ordenacao|busca binaria|merge sort|quicksort|guloso)\b',
            r'\bcaminho minimo\b', r'\b(?:robo|grade)\b', r'\bt\s*\(\s*n\s*\)',
            r'\b(?:complexidade|assintotic|inducao)\w*\b'),
}


def identificar(pergunta: str, contexto: str = '') -> str | None:
    # O enunciado tem precedência: código/rascunho pode mencionar outra disciplina.
    def avaliar(texto):
        normal = searchable(texto)
        pontos = {d: sum(bool(re.search(r, normal)) for r in regras) for d, regras in REGRAS.items()}
        candidatas = [d for d, n in pontos.items() if n]
        return candidatas[0] if len(candidatas) == 1 else None

    return avaliar(pergunta) or (avaliar(contexto) if not pergunta.strip() or
        not any(re.search(r, searchable(pergunta)) for regras in REGRAS.values() for r in regras) else None)
