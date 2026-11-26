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
    'oac': (r'\brisc.?v\b', r'\bmips\b', r'\bcpi\b', r'\bpipeline\b', r'\bhazards?\b', r'\bcache\b',
            r'\bdatapath\b|caminho de dados', r'\bassembly\b', r'\b(?:lw|sw|addi|beq|bne|jal|blt|bltu)\b',
            r'\barquitetura de computadores\b'),
    'calc3': (r'\bderivadas? parcia', r'\bgradiente\b', r'\bintegra(?:l|is) (?:dupla|tripla|de linha|de superficie)',
              r'\blagrange\b', r'\bcoordenadas polares\b', r'\bcurvatura\b', r'\bteorema de (?:green|stokes|gauss)\b',
              r'\bderivada direcional\b', r'\bcampo vetorial\b', r'\brotacional\b|\bdivergente\b',
              r'\bcalculo (?:3|iii)\b', r'\bcardioide\b'),
    'fis2': (r'\boscila', r'\bpendulo\b', r'\bondas?\b', r'\bfluidos?\b|\bempuxo\b|\bbernoulli\b|\bhidrostatic',
             r'\bgravita', r'\bentropia\b', r'\btermodinamica\b|\bcalor\b', r'\bmola\b|\bmhs\b',
             r'\belasticidade\b|\bmodulo de young\b', r'\bfisica (?:2|ii)\b', r'\bdoppler\b'),
    'ed': (r'\bponteir', r'\bmalloc\b', r'\blista (?:encadeada|ligada|duplamente)', r'\bstruct\b',
           r'\btabela hash\b|\bhash\b', r'\bheap\b', r'\barvore (?:binaria|avl|rubro)', r'\bhuffman\b',
           r'\bestrutura de dados\b'),
    'bd': (r'\bsql\b', r'\bselect\b', r'\bjoin\b|\bjuncao\b', r'\bnormaliza|\bforma normal\b|\b[123]fn\b|\bbcnf\b',
           r'\bmodelo (?:er|entidade)', r'\bchave (?:primaria|estrangeira)\b', r'\balgebra relacional\b',
           r'\bbanco de dados\b', r'\btransac'),
}


def identificar(pergunta: str, contexto: str = '', preferidas: tuple[str, ...] | list[str] = ()) -> str | None:
    """`preferidas`: disciplinas do período que o aluno escolheu (curso + período). Desempatam
    quando a dúvida tem sinais de mais de uma disciplina e, sem sinal nenhum, decidem se o
    período tem uma única disciplina com material."""
    # O enunciado tem precedência: código/rascunho pode mencionar outra disciplina.
    def avaliar(texto):
        normal = searchable(texto)
        pontos = {d: sum(bool(re.search(r, normal)) for r in regras) for d, regras in REGRAS.items()}
        candidatas = [d for d, n in pontos.items() if n]
        if len(candidatas) > 1 and preferidas:
            candidatas = [d for d in candidatas if d in preferidas] or candidatas
        return candidatas[0] if len(candidatas) == 1 else None

    from .disciplina_lexico import identificar_lexico, nome_citado

    # 1. Nome da disciplina citado na dúvida ("em Sistemas de Controle…") decide.
    citada = nome_citado(pergunta)
    if citada:
        return citada
    # 2. Dúvida sem sinal próprio: o nome no arquivo/contexto (ex.: capa do slide) vem antes das regras,
    #    que confundiam palavras soltas do arquivo ("circuito" de um slide de Controle virava SD).
    if not _tem_sinal(pergunta):
        citada = nome_citado(contexto)
        if citada:
            return citada
    escolhida = _identificar(avaliar, pergunta, contexto)
    if escolhida is None and len(preferidas) == 1 and not _tem_sinal(pergunta) and not _tem_sinal(contexto):
        return preferidas[0]
    # 3. As regras só cobrem algumas disciplinas: sem decisão, o vocabulário do acervo de todas.
    if escolhida is None:
        escolhida = identificar_lexico(pergunta, contexto, preferidas)
    return escolhida


def _tem_sinal(texto: str) -> bool:
    normal = searchable(texto or '')
    return any(re.search(r, normal) for regras in REGRAS.values() for r in regras)


def _identificar(avaliar, pergunta: str, contexto: str) -> str | None:
    return avaliar(pergunta) or (avaliar(contexto) if not pergunta.strip() or
        not any(re.search(r, searchable(pergunta)) for regras in REGRAS.values() for r in regras) else None)
