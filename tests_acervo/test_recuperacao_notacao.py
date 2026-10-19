"""Regressão da busca com notação booleana (mintermos, variáveis de uma letra, negação).

Problema original: "Σm(0,1,3,5,7)" virava só as palavras da pergunta, porque a busca
descarta tokens de um caractere; o bloco da Lista AV1 com essa resolução ficava em 5º.
"""
import json

import pytest

from acervo import disciplinas
from acervo.common import ROOT
from acervo.retrieval import estruturais, search, tokens

SD = disciplinas.obter('sd')


def ids_sd(pergunta):
    return [r['id'] for r in search(pergunta, semantic=False, itens=SD.itens, indice=SD.indice)]


@pytest.mark.parametrize('texto, esperado', [
    ('S = Σm(0,1,3,5,7)', ['mintermos:0,1,3,5,7']),
    ('F = ΠM(2, 4, 6)', ['maxtermos:2,4,6']),
    ('F = Πm(2,4)', ['maxtermos:2,4']),
    ('irrelevâncias d(1, 4, 6, 7)', ['irrelevantes:1,4,6,7']),
    ('S(A,B,C)', ['vars:a,b,c']),
    ("S = C + A'B'", ["termo:a'b'"]),
    ("S = (A⊕B)·D + A'BC", ["termo:a'bc"]),
    ('S = A·B + C', []),             # sem negação, letras soltas não viram termo
    ('lucro de 1,40 e 1,60', []),    # decimal com vírgula não é lista de mintermos
    ('d(a,c) + d(b,d) - d(a,b)', []),  # distância entre vértices (PAA) não é função booleana
    ('para i de 1 até n', []),
])
def test_notacao_extraida(texto, esperado):
    assert estruturais(texto) == esperado


def test_palavras_continuam_iguais():
    assert tokens('Como aplico o Teorema Mestre em T(n) = 3T(n/4) + n log n?') == [
        'aplico', 'teorema', 'mestre', '3t', 'log']


@pytest.mark.parametrize('pergunta, primeiro', [
    # A pergunta do teste manual: a resolução da AV1 Q7a tem de vir primeiro.
    ('Como simplifico S(A,B,C) = Σm(0,1,3,5,7) com mapa de Karnaugh?', 'sd-av1-q01-07'),
    ("Por que a resposta da 7a é S = C + A'B'?", 'sd-av1-q01-07'),
    ('Tabela com S = 1 em 000, 011 e 101 e irrelevâncias d(1,4,6,7): como fica no Karnaugh?', 'sd-av1-q01-07'),
    ('Como agrupar F(A,B,C,D) = Σm(0,2,5,7,8,10,13,15) nos cantos do mapa?', 'sd-nota-karnaugh'),
    ("Na FSM da prova 2, por que n1 = s1'·s0'·a'·b' + s1'·s0·a + s1·s0'?", 'sd-prova2-q1-2'),
])
def test_resolucao_especifica_vem_primeiro(pergunta, primeiro):
    assert ids_sd(pergunta)[0] == primeiro


def test_expressao_com_negacao_encontra_a_resolucao():
    assert 'sd-av1-q01-07' in ids_sd("Como chegar em S = (A⊕B)·D + A'BC?")[:2]


def test_numero_de_resultados_nao_mudou():
    assert len(ids_sd('Como simplifico S(A,B,C) = Σm(0,1,3,5,7) com mapa de Karnaugh?')) == 4


def test_maxtermos_nao_confundem_com_mintermos(tmp_path):
    base = 'assunto: a\ntipo: lista\nfonte: f\nautoria: a\nlicenca: l\ncuradoria: aprovado\n'
    (tmp_path / 'm').mkdir()
    (tmp_path / 'm' / 'min.md').write_text(f'---\nid: min\ntitulo: t\n{base}---\nF = Σm(0,2,4) no mapa', encoding='utf-8')
    (tmp_path / 'm' / 'max.md').write_text(f'---\nid: max\ntitulo: t\n{base}---\nF = ΠM(0,2,4) no mapa', encoding='utf-8')
    d = disciplinas.Disciplina('t', 'T', 'T', tmp_path / 'i.json', tmp_path / 'x.json', rigor='', materiais=tmp_path / 'm')
    disciplinas.construir(d, root=tmp_path)
    busca = lambda p: [r['id'] for r in search(p, semantic=False, itens=d.itens, indice=d.indice)]
    assert busca('Simplifique F = ΠM(0,2,4)')[0] == 'max'
    assert busca('Simplifique F = Σm(0,2,4)')[0] == 'min'


def test_ranking_lexico_de_paa_preservado():
    """As 20 perguntas de 06-avaliacao (questoes.json e perguntas-mvp.json) devolvem exatamente
    os mesmos blocos, na mesma ordem, que antes da mudança (instantâneo de e102e22)."""
    antes = json.loads((ROOT / 'tests_acervo/ranking-paa-lexico.json').read_text(encoding='utf-8'))
    assert len(antes) == 20
    agora = {p: [r['id'] for r in search(p, semantic=False)] for p in antes}
    assert agora == antes
