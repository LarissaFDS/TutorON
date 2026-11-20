"""Acervo de Sistemas de Controle e conferência das resoluções.

Cada resultado escrito num bloco é refeito aqui com SymPy (frações parciais, inversas, `solve` de modelos),
numpy (`roots`) ou SciPy (`signal.step`, `lsim`). Os erros encontrados nas anotações do aluno são conferidos
como erros, e a correção como correção.
"""
import json
import math
import re
import shutil
import subprocess

import numpy as np
import pytest
import sympy as sp
from scipy import signal

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

SC = disciplinas.obter('controle')
FONTES = read_json(ROOT / 'disciplinas/controle/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {x['id']: x for x in read_json(SC.itens)}
NA_BUSCA = {c['id'] for c in read_json(SC.indice)['chunks']}
VETORES = json.loads((ROOT / 'eval/relevancia-vetores.json').read_text(encoding='utf-8'))
s = sp.Symbol('s')
tp = sp.Symbol('t', positive=True)


def texto(ident):
    return ITENS[ident]['texto']


def buscar(pergunta, d=SC):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def hibrida(pergunta, d=SC):
    return [r['id'] for r in search(pergunta, k=4, vector=VETORES[pergunta], min_similarity=0.45, hub_penalty=True,
                                    itens=d.itens, indice=d.indice)]


def ilaplace(F):
    return sp.simplify(sp.inverse_laplace_transform(sp.apart(sp.nsimplify(F), s), s, tp))


def degrau(num, den, T=30, n=30001):
    t, y = signal.step((num, den), T=np.linspace(0, T, n))
    return t, y


def sobressinal(y, final):
    return (y.max() - final) / final


# ---------------------------------------------------------------- cadastro e acervo

def test_controle_cadastrada_com_acervo_proprio_e_a_mesma_ia():
    assert SC.nome == 'Sistemas de Controle' and SC.itens.exists() and SC.indice.exists()
    assert not SC.livro_supabase and SC.rigor.strip() == (ROOT / 'disciplinas/controle/rigor.md').read_text(encoding='utf-8').strip()
    assert all(c['disciplina'] == 'controle' for c in read_json(SC.indice)['chunks'])
    for outra in ('paa', 'sd', 'oac', 'calc3', 'fis2', 'ed', 'bd', 'prob', 'circ', 'sinais'):
        d = disciplinas.obter(outra)
        assert NA_BUSCA.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    bruto = [d for d in read_json(ROOT / 'disciplinas/disciplinas.json')['disciplinas'] if d['id'] == 'controle'][0]
    assert not {'modelo', 'model', 'provedor', 'endpoint', 'prompt', 'chave'} & set(bruto)
    assert read_json(SC.indice)['embedding_model'] == read_json(disciplinas.obter('sinais').indice)['embedding_model']


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas controle --embeddings`."""
    gerados = disciplinas.registros(SC)
    assert gerados == read_json(SC.itens)
    assert NA_BUSCA == {x['id'] for x in gerados if x['confiabilidade'] in ('media', 'alta')}
    assert read_json(SC.indice)['modo'] == 'hibrido'


def test_blocos_cabem_no_trecho_e_formulas_fecham():
    for x in ITENS.values():
        assert len(x['texto']) <= 2200, x['id']
        sem_destaque = x['texto'].replace('$$', '')
        assert x['texto'].count('$$') % 2 == 0 and sem_destaque.count('$') % 2 == 0, x['id']
        assert '**Verificação:**' in x['texto'], x['id']


def test_notas_de_ia_sem_revisao_ficam_fora_da_busca():
    notas = [x for x in ITENS.values() if x['natureza'] == 'nota_da_equipe_ia']
    assert sorted(x['id'] for x in notas) == ['controle-nota-ia-projeto-controladores', 'controle-nota-ia-resposta-frequencia']
    assert all(x['status_curadoria'] == 'candidato' and x['revisao_humana'] == 'pendente' for x in notas)
    assert {x['id'] for x in notas}.isdisjoint(NA_BUSCA)
    assert not any(x.get('revisao_humana') == 'feita' or x.get('revisao_professor') for x in ITENS.values())


def test_topicos_com_anotacoes_tem_bloco_na_busca():
    """Critério de liberação: todo tópico "Sim" (01 a 07) tem bloco na busca; 08 e 09 ficam "a confirmar"."""
    na_busca = {ITENS[x]['assunto'] for x in NA_BUSCA}
    sim = set(SC.assuntos) - {'controle-08-resposta-frequencia', 'controle-09-projeto-controladores'}
    assert na_busca == sim and len(sim) == 7


# ---------------------------------------------------------------- status das resoluções

CORRIGIDAS = {'controle-anot-fracoes-parciais', 'controle-anot-circuito-rc', 'controle-anot-diagrama-blocos',
              'controle-anot-segunda-ordem', 'controle-anot-revisao-segunda-ordem', 'controle-anot-erro-regime-tipo',
              'controle-anot-lugar-raizes-regras', 'controle-anot-routh'}


def test_resolucoes_tem_status_e_dizem_no_texto():
    turma = [x for x in ITENS.values() if x['natureza'] == 'material_da_disciplina']
    assert len(turma) == 22
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    for x in turma:
        assert f"Status da resolução: {rotulo[x['status_resolucao']]}" in x['texto'], x['id']
        assert x['verificacao'] == 'conferida_por_codigo' and x['revisao_humana'] == 'pendente'
    assert {x['id'] for x in turma if x['status_resolucao'] == 'corrigida'} == CORRIGIDAS
    assert all('correç' in texto(c).lower() or 'complemento' in texto(c).lower() for c in CORRIGIDAS)


# ---------------------------------------------------------------- 01 Laplace e função de transferência

def test_tvf_so_quando_estavel():
    F1 = 7 * (s + 5) / (2 * s * (s ** 2 + 2 * s + 3))
    assert all(sp.re(p) < 0 for p in sp.roots(sp.denom(sp.cancel(s * F1)), s))
    assert sp.limit(s * F1, s, 0) == sp.Rational(35, 6)
    F2 = 4 / (s * (s ** 2 - 5 * s + 6))
    f2 = ilaplace(F2)
    assert sp.simplify(f2 - (sp.Rational(2, 3) - 2 * sp.exp(2 * tp) + sp.Rational(4, 3) * sp.exp(3 * tp))) == 0
    assert sp.limit(f2, tp, sp.oo) == sp.oo and sp.limit(s * F2, s, 0) == sp.Rational(2, 3)
    assert '35}{6}' in texto('controle-anot-laplace-tvf') and 'não se aplica' in texto('controle-anot-laplace-tvf')


def test_fracoes_parciais_tres_exemplos():
    y1 = ilaplace((s + 1) / (s * (s + 2) * (s + 3)))
    assert sp.simplify(y1 - (sp.Rational(1, 6) + sp.exp(-2 * tp) / 2 - sp.Rational(2, 3) * sp.exp(-3 * tp))) == 0
    th = math.atan2(8, -6)
    assert math.isclose(math.degrees(th), 126.87, abs_tol=0.01)
    t = np.linspace(0, 3, 301)
    _, y = signal.step(([10], [1, 12, 100]), T=t)
    assert np.allclose(y, 0.1 + np.exp(-6 * t) / 8 * np.cos(8 * t - th - math.pi / 2), atol=1e-6)
    y3 = ilaplace((s ** 2 + 2 * s + 3) / (s + 1) ** 3)
    assert sp.simplify(y3 - (sp.exp(-tp) + tp ** 2 * sp.exp(-tp))) == 0
    assert sp.simplify(y3 - (sp.exp(-tp) + tp ** 2 * sp.exp(-3 * tp))) != 0  # erro das anotações
    assert 't^2e^{-t},' in texto('controle-anot-fracoes-parciais')


# ---------------------------------------------------------------- 02 modelagem

def test_massa_mola_amortecedor():
    m, b, K = sp.symbols('m b K', positive=True)
    X, F = sp.symbols('X F')
    G = sp.solve(sp.Eq(m * s ** 2 * X + b * s * X + K * X, F), X)[0] / F
    assert sp.simplify(G - 1 / (m * s ** 2 + b * s + K)) == 0
    assert G.subs(s, 0) == 1 / K
    raizes = np.roots([1, 2, 5])
    assert np.allclose(sorted(raizes, key=lambda z: z.imag), [-1 - 2j, -1 + 2j])
    assert math.isclose(2 / (2 * math.sqrt(5)), 0.447, abs_tol=1e-3)
    assert '\\frac{1}{ms^2 + bs + K}' in texto('controle-anot-massa-mola-amortecedor')


def test_suspensao_de_duas_massas():
    M1, M2, K1, K2, b = sp.symbols('M1 M2 K1 K2 b', positive=True)
    X1, X2, F = sp.symbols('X1 X2 F')
    sol = sp.solve([(M1 * s ** 2 + b * s + K1) * X1 - (b * s + K1) * X2,
                    (M2 * s ** 2 + b * s + K1 + K2) * X2 - (b * s + K1) * X1 - F], [X1, X2])
    G = sp.simplify(sol[X1] / F)
    esperado = (b * s + K1) / (M1 * M2 * s ** 4 + b * (M1 + M2) * s ** 3 + (M1 * K1 + M2 * K1 + M1 * K2) * s ** 2
                               + b * K2 * s + K1 * K2)
    assert sp.simplify(G - esperado) == 0 and sp.simplify(G.subs(s, 0)) == 1 / K2


def test_circuito_dois_capacitores_sinal_corrigido():
    R1, R2, C1, C2 = sp.symbols('R1 R2 C1 C2', positive=True)
    Vi, V1, Vo = sp.symbols('Vi V1 Vo')
    sol = sp.solve([(V1 - Vi) / R1 + C1 * s * V1 + (V1 - Vo) / R2,
                    C2 * s * (Vi - Vo) + (V1 - Vo) / R2], [V1, Vo])
    G = sp.simplify(sol[Vo] / Vi)
    esperado = (C1 * C2 * R1 * R2 * s ** 2 + C2 * (R1 + R2) * s + 1) / (
        C1 * C2 * R1 * R2 * s ** 2 + (C1 * R1 + C2 * R1 + C2 * R2) * s + 1)
    assert sp.simplify(G - esperado) == 0
    assert sp.simplify(G.subs(s, 0)) == 1 and sp.limit(G, s, sp.oo) == 1


# ---------------------------------------------------------------- 03 diagramas de blocos

def test_realimentacao_negativa_e_positiva():
    G, H, R, Y = sp.symbols('G H R Y')
    assert sp.simplify(sp.solve(sp.Eq(Y, G * (R - H * Y)), Y)[0] / R - G / (1 + G * H)) == 0
    assert sp.simplify(sp.solve(sp.Eq(Y, G * (R + H * Y)), Y)[0] / R - G / (1 - G * H)) == 0
    g = 2 / (s + 1)
    assert sp.simplify(g / (1 + g) - 2 / (s + 3)) == 0
    assert '1 - GH' in texto('controle-anot-diagrama-blocos')


def test_circuito_rlc_por_blocos():
    R1, R2, L, C = sp.symbols('R1 R2 L C', positive=True)
    Vi, Vc, Vo, I1, I2 = sp.symbols('Vi Vc Vo I1 I2')
    sol = sp.solve([I1 - (Vi - Vc) / R1, Vc - (I1 - I2) / (C * s), I2 - (Vc - Vo) / (L * s), Vo - R2 * I2],
                   [Vc, Vo, I1, I2])
    G = sp.simplify(sol[Vo] / Vi)
    assert sp.simplify(G - R2 / (R1 * L * C * s ** 2 + (R1 * R2 * C + L) * s + R1 + R2)) == 0


# ---------------------------------------------------------------- 04 estabilidade

def test_bibo_exemplos():
    ya = ilaplace(2 / (s ** 2 * (s + 2)))
    assert sp.simplify(ya - (-sp.Rational(1, 2) + tp + sp.exp(-2 * tp) / 2)) == 0
    yb = ilaplace(2 / (s ** 2 + 4) ** 2)
    assert sp.simplify(yb - (sp.sin(2 * tp) / 8 - tp * sp.cos(2 * tp) / 4)) == 0
    assert all(r.real < 0 for r in np.roots([1, 3, 2]))
    assert any(r.real > 0 for r in np.roots([1, 7, -8, 4, 5, 1]))


def routh_primeira_coluna(coefs, eps=None):
    n = len(coefs)
    linhas = [list(coefs[0::2]), list(coefs[1::2])]
    largura = len(linhas[0])
    linhas = [l + [0] * (largura - len(l)) for l in linhas]
    while len(linhas) < n:
        a, b = linhas[-2], linhas[-1]
        if b[0] == 0:
            b[0] = eps
        nova = [(b[0] * a[i + 1] - a[0] * b[i + 1]) / b[0] for i in range(largura - 1)] + [0]
        linhas.append(nova)
    return [l[0] for l in linhas]


def mudancas(col):
    return sum(1 for a, b in zip(col, col[1:]) if a * b < 0)


def test_routh_exemplos():
    c1 = routh_primeira_coluna([sp.Integer(x) for x in (1, 4, 3, 2, 1, 4, 4)])
    assert c1 == [1, 4, sp.Rational(5, 2), 2, 3, sp.Rational(-76, 15), 4] and mudancas(c1) == 2
    assert sum(r.real > 0 for r in np.roots([1, 4, 3, 2, 1, 4, 4])) == 2
    # polinômio como escrito nas anotações (2s²): outra coluna, mesma conclusão
    c1b = routh_primeira_coluna([sp.Integer(x) for x in (1, 4, 3, 2, 2, 4, 4)])
    assert c1b == [1, 4, sp.Rational(5, 2), sp.Rational(2, 5), 16, sp.Rational(-5, 2), 4] and mudancas(c1b) == 2
    assert sum(r.real > 0 for r in np.roots([1, 4, 3, 2, 2, 4, 4])) == 2
    c2 = routh_primeira_coluna([1.0, 1, 5, 5, 12, 10], eps=1e-6)
    assert mudancas(c2) == 2 and sum(r.real > 0 for r in np.roots([1, 1, 5, 5, 12, 10])) == 2


def test_routh_faixa_de_ganho():
    K = sp.Symbol('K', positive=True)
    G = (s + 1) / (s * (s - 1) * (s + 6))
    den = sp.expand(sp.numer(sp.together(1 + K * G)))
    assert sp.Poly(den, s).all_coeffs() == [1, 5, K - 6, K]
    for k, estavel in ((8, True), (7, False)):
        assert all(r.real < 0 for r in np.roots([1, 5, k - 6, k])) == estavel
    assert np.allclose(sorted(np.abs(np.roots([1, 5, 1.5, 7.5]).imag))[-1], math.sqrt(1.5))


def test_revisao_sensor_oscilacao():
    raizes = np.roots([1, 1.1, 0.1, 0.11])
    assert np.allclose(sorted(raizes, key=lambda z: z.imag), [-0.3162j, -1.1, 0.3162j], atol=1e-4)
    assert math.isclose(2 * math.pi / math.sqrt(0.1), 19.87, abs_tol=0.01)
    C, Gp, H = sp.Rational(55, 100) / s, 2 / (s + 1), sp.Rational(1, 10) / (s + sp.Rational(1, 10))
    Gmf = sp.cancel(C * Gp / (1 + C * Gp * H))
    assert sp.simplify(Gmf - sp.Rational(11, 10) * (s + sp.Rational(1, 10)) / (s ** 3 + sp.Rational(11, 10) * s ** 2
                                                                                + s / 10 + sp.Rational(11, 100))) == 0


# ---------------------------------------------------------------- 05 resposta temporal

def test_primeira_ordem():
    assert math.isclose(-math.log(0.02), 3.91, abs_tol=0.01) and math.isclose(math.log(9), 2.197, abs_tol=1e-3)
    t, y = degrau([8], [1, 5], T=2, n=20001)
    assert math.isclose(np.interp(0.2, t, y), 1.011, abs_tol=1e-3)
    fora = np.where(np.abs(y - 1.6) > 0.02 * 1.6)[0][-1]
    assert math.isclose(t[fora + 1], 0.78, abs_tol=0.01)


def test_segunda_ordem_formulas_e_correcoes():
    for z, mp in ((0.5, 16.3), (0.6, 9.5), (0.7, 4.6)):
        assert math.isclose(100 * math.exp(-z * math.pi / math.sqrt(1 - z * z)), mp, abs_tol=0.05)
    t, y = degrau([1], [1, 1, 1], T=30)
    wd = math.sqrt(0.75)
    assert math.isclose(y.max(), 1.163, abs_tol=1e-3) and math.isclose(t[y.argmax()], math.pi / wd, abs_tol=0.01)
    tr = np.interp(0.9, y[:4000], t[:4000]) - np.interp(0.1, y[:4000], t[:4000])
    assert math.isclose(tr, 1.64, abs_tol=0.01)
    razao = [(math.pi - math.acos(z)) / math.sqrt(1 - z * z) for z in (0.4, 0.8)]
    assert math.isclose(razao[0], 2.16, abs_tol=0.01) and math.isclose(razao[1], 4.16, abs_tol=0.01)
    assert 'Correç' in texto('controle-anot-segunda-ordem')


def test_especificacoes_por_ganho():
    def mp(K):
        _, y = degrau([2 * K], [1, 4, 2 * K])
        return sobressinal(y, 1.0)
    assert math.isclose(mp(4.2), 0.05, abs_tol=0.003) and mp(3) < 0.05 and mp(5) > 0.05
    z = 2 / math.sqrt(2 * 4.2)
    assert z >= 0.69 and math.isclose(math.sqrt(2 * 0.5), 1.0)


def test_polo_e_zero_adicionais():
    def mp(beta):
        _, y = degrau([1], np.polymul([1 / beta, 1], [1, 1, 1]), T=80, n=80001)
        return sobressinal(y, 1.0)
    assert mp(5) < 0.163 and mp(1.5) < mp(5) and mp(0.5) < 0.005
    Y2 = 6 * (s + sp.Rational(11, 10)) / (sp.Rational(11, 10) * s * (s + 1) * (s + 6))
    y2 = ilaplace(Y2)
    assert sp.simplify(y2 - (1 - sp.Rational(6, 55) * sp.exp(-tp) - sp.Rational(49, 55) * sp.exp(-6 * tp))) == 0
    assert math.isclose(6 / 55, 0.109, abs_tol=1e-3) and math.isclose(49 / 55, 0.891, abs_tol=1e-3)
    y1 = ilaplace(6 / (s * (s + 1) * (s + 6)))
    assert sp.simplify(y1 - (1 - sp.Rational(6, 5) * sp.exp(-tp) + sp.exp(-6 * tp) / 5)) == 0
    mz = [sobressinal(degrau([1 / b, 1], [1, 1, 1])[1], 1.0) for b in (5, 1.5, 0.5)]
    assert mz[0] < mz[1] < mz[2]


def test_revisao_primeira_ordem():
    assert math.isclose(-15 * math.log(0.05), 45, abs_tol=0.1)
    assert sp.limit(s * (1 - 1 / (15 * s + 1)) * sp.Rational(1, 3) / s ** 2, s, 0) == 5
    t = np.linspace(0, 120, 12001)
    _, y, _ = signal.lsim(([1], [15, 1]), t / 3, t)
    assert math.isclose(t[-1] / 3 - y[-1], 5, abs_tol=0.02)
    K, tau = 24, 25
    assert K / (1 + K) == 0.96
    tt, yy = degrau([K], [tau, 1 + K], T=5, n=5001)
    assert math.isclose(np.interp(1, tt, yy), 0.607, abs_tol=2e-3)


def test_revisao_segunda_ordem():
    t, y = degrau([6], [1, 2, 8], T=10, n=100001)
    assert math.isclose(y.max(), 0.979, abs_tol=1e-3) and math.isclose(t[y.argmax()], 1.19, abs_tol=0.01)
    z = 1 / math.sqrt(8)
    assert math.isclose((math.pi - math.acos(z)) / (math.sqrt(8) * math.sqrt(1 - z * z)), 0.73, abs_tol=0.01)
    t, y = degrau([20], [1, 6, 36], T=5, n=50001)
    assert math.isclose(y.max(), 0.646, abs_tol=1e-3) and math.isclose(t[y.argmax()], 0.605, abs_tol=0.005)
    errado = math.exp(-0.5 * math.pi * math.sqrt(0.75))
    assert math.isclose(errado, 0.2565, abs_tol=1e-3)  # fórmula das anotações
    assert math.isclose(0.55 * (1 + errado), 0.691, abs_tol=1e-3)  # anotações com ganho arredondado 0,55 and not math.isclose(y.max(), 0.691, abs_tol=0.01)
    for alfa, sub in ((6, False), (1, True), (4, True)):
        assert ((1 + alfa) / 6 < 1) == sub
    assert math.isclose(1 / ((1 + 1) / 6 * 3), 1.0)


# ---------------------------------------------------------------- 06 erro em regime

def test_erro_tipo_e_parabola_corrigida():
    G = 1 / (s * (s + 1))
    assert sp.limit(s * G, s, 0) == 1
    assert sp.limit(s * (1 / s) / (1 + G), s, 0) == 0 and sp.limit(s * (1 / s ** 2) / (1 + G), s, 0) == 1
    assert sp.laplace_transform(tp ** 2 / 2, tp, s, noconds=True) == 1 / s ** 3
    assert sp.laplace_transform(tp ** 2, tp, s, noconds=True) == 2 / s ** 3
    t = np.linspace(0, 60, 60001)
    _, y, _ = signal.lsim(([1], [1, 1, 1]), t, t)
    assert math.isclose(t[-1] - y[-1], 1, abs_tol=1e-3)


def test_erro_realimentacao_nao_unitaria():
    G, H = 2 / (s + 1), (s + 2) / (s + 3)
    Gmf = sp.cancel(G / (1 + G * H))
    assert sp.simplify(Gmf - 2 * (s + 3) / (s ** 2 + 6 * s + 7)) == 0
    assert sp.limit(s * (1 - Gmf) / s, s, 0) == sp.Rational(1, 7)
    _, y = degrau([2, 6], [1, 6, 7], T=20)
    assert math.isclose(y[-1], 6 / 7, abs_tol=1e-4)


def test_erro_por_perturbacao():
    C, G, Gw = 1 / (s + 1), 1 / s, sp.Rational(1, 10) / (s + 10)
    Gmf, Gwmf = sp.cancel(C * G / (1 + C * G)), sp.cancel(Gw * G / (1 + C * G))
    assert sp.simplify(Gmf - 1 / (s ** 2 + s + 1)) == 0
    assert -sp.limit(Gwmf, s, 0) == -sp.Rational(1, 100)
    assert sp.limit(s * C * G, s, 0) == 1
    assert sp.limit(-s * Gwmf / s ** 2, s, 0) == -sp.oo


# ---------------------------------------------------------------- 07 lugar das raízes

def test_lugar_das_raizes_k_sobre_s_s_mais_2():
    assert np.allclose(sorted(np.roots([1, 2, 0.5])), [-1 - math.sqrt(0.5), -1 + math.sqrt(0.5)])
    assert np.allclose(np.roots([1, 2, 1]), [-1, -1])
    assert np.allclose(sorted(np.roots([1, 2, 5]), key=lambda z: z.imag), [-1 - 2j, -1 + 2j])
    assert sp.solve(sp.diff(s * (s + 2), s), s) == [-1]
    assert np.allclose(np.roots([1, 1, 0.25]), [-0.5, -0.5])


def test_lugar_das_raizes_regras_exemplo():
    G = (s + 2) / (s ** 2 + 2 * s + 3)
    ramif = sp.solve(sp.numer(sp.together(sp.diff(1 / G, s))), s)
    assert set(ramif) == {-2 + sp.sqrt(3), -2 - sp.sqrt(3)}
    K = sp.simplify(-1 / G.subs(s, -2 - sp.sqrt(3)))
    assert sp.simplify(K - (2 + 2 * sp.sqrt(3))) == 0
    assert sp.simplify(-1 / G.subs(s, -2 + sp.sqrt(3))) < 0  # −0,27 exigiria K negativo
    assert np.allclose(np.roots([1, 2 + 5.4641, 3 + 2 * 5.4641]), [-3.732, -3.732], atol=2e-3)
    p1 = complex(-1, math.sqrt(2))
    partida = 180 + math.degrees(math.atan2((p1 + 2).imag, (p1 + 2).real)) - 90
    assert math.isclose(partida, 144.7, abs_tol=0.05)


# ---------------------------------------------------------------- busca

EXEMPLOS = [
    ('Como reduzir um diagrama de blocos com realimentação negativa?', {'controle-anot-diagrama-blocos'}),
    ('Como calcular o sobressinal de um sistema de segunda ordem?', {'controle-anot-segunda-ordem', 'controle-anot-revisao-segunda-ordem'}),
    ('Qual o erro em regime para entrada degrau num sistema tipo 1?', {'controle-anot-erro-regime-tipo'}),
    ('Como desenhar o lugar das raízes de G(s) = K/(s(s+2))?', {'controle-anot-lugar-raizes-intro', 'controle-anot-lugar-raizes-regras'}),
    ('Como montar a função de transferência de um sistema massa-mola-amortecedor?', {'controle-anot-massa-mola-amortecedor'}),
]
VARIANTES = [
    (r'Como achar $\frac{Y(s)}{R(s)}$ com realimentação negativa $H(s)$?',
     'Como achar Y de s sobre R de s com realimentação negativa H de s?', EXEMPLOS[0][1]),
    (r'Qual o $M_p$ de $\frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$?',
     'Qual o sobressinal Mp de ômega n ao quadrado sobre s ao quadrado mais 2 zeta ômega n s mais ômega n ao quadrado?', EXEMPLOS[1][1]),
    (r'Qual o $e_{ss}$ ao degrau com $K_p$ num sistema tipo 1?',
     'Qual o erro ess ao degrau com a constante Kp num sistema tipo 1?', EXEMPLOS[2][1]),
    (r'Lugar das raízes de $G(s) = \frac{K}{s(s+2)}$',
     'Lugar das raízes de G de s igual a K sobre s vezes s mais 2', EXEMPLOS[3][1]),
    (r'Função de transferência $\frac{X(s)}{F(s)}$ de $m\ddot x + b\dot x + kx = f$',
     'Função de transferência X de s sobre F de s de m x dois pontos mais b x ponto mais k x igual a f', EXEMPLOS[4][1]),
]
FORA = ['Como simplificar uma função com mapa de Karnaugh?', 'Como fazer um LEFT JOIN em SQL?', 'Me conte uma piada']


def test_exemplos_do_cadastro_sao_os_testados():
    assert list(SC.exemplos) == [p for p, _ in EXEMPLOS]


@pytest.mark.parametrize('pergunta, aceitos', EXEMPLOS)
def test_perguntas_de_exemplo_trazem_o_bloco_certo(pergunta, aceitos):
    assert aceitos & set(hibrida(pergunta))


@pytest.mark.parametrize('latex, simples, aceitos', VARIANTES)
def test_latex_e_texto_simples_trazem_o_mesmo_bloco(latex, simples, aceitos):
    assert aceitos & set(hibrida(latex)) and aceitos & set(hibrida(simples))


@pytest.mark.parametrize('pergunta', FORA)
def test_pergunta_de_outra_area_nao_traz_material(pergunta):
    assert hibrida(pergunta) == []


def test_isolamento_com_sinais_e_circuitos():
    """Nas duas direções: os acervos de Sinais e Circuitos não trazem blocos de Controle, e vice-versa."""
    sinais, circ = disciplinas.obter('sinais'), disciplinas.obter('circ')
    for p, _ in EXEMPLOS:
        assert not any(x.startswith('controle-') for x in buscar(p, sinais) + buscar(p, circ))
    for p in list(sinais.exemplos) + list(circ.exemplos):
        assert not any(x.startswith(('sinais-', 'circ-')) for x in buscar(p))


# ---------------------------------------------------------------- KaTeX, catálogo e restrições

FORMULA = re.compile(r'\$\$(.+?)\$\$|\$(.+?)\$', re.S)


@pytest.mark.skipif(not shutil.which('node'), reason='node indisponível')
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for x in ITENS.values() for a, b in FORMULA.findall(x['texto'])]
    assert len(formulas) > 200
    katex = (ROOT / 'backend/web/vendor/katex/katex.min.js').as_posix()
    script = (f"const k=require({json.dumps(katex)});const fs=require('fs');"
              "const erros=[];for(const f of JSON.parse(fs.readFileSync(0,'utf8'))){"
              "try{k.renderToString(f,{throwOnError:true})}catch(e){erros.push(f+' :: '+e.message)}}"
              "console.log(JSON.stringify(erros))")
    r = subprocess.run(['node', '-e', script], input=json.dumps(formulas), capture_output=True, text=True,
                       encoding='utf-8', check=True)
    assert json.loads(r.stdout) == []


def test_catalogo_completo_e_coerente():
    obrigatorios = {'id', 'nome', 'autoria', 'url', 'idioma', 'formato', 'notacao', 'topicos', 'licenca', 'acesso',
                    'prioridade', 'uso', 'justificativa'}
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f['id']
        assert f['prioridade'] in ('alta', 'media', 'referencia') and f['uso'] in ('acervo', 'citada', 'referencia')
        assert set(f['topicos']) <= set(SC.assuntos), f['id']
    assert {x for i_ in ITENS.values() for x in i_['fontes_catalogo']} - {'nenhuma'} <= set(CATALOGO)
    assert {k for k, f in CATALOGO.items() if f['uso'] == 'acervo'} == {'ufal-controle-anotacoes-otavio-2026-2'}
    aut = CATALOGO['ufal-controle-anotacoes-otavio-2026-2']['autorizacao_transcricao']
    assert aut['aprovacao_professor'] == 'não declarada'
    for protegido in ('ogata-engenharia-controle-moderno', 'dorf-bishop-sistemas-controle-modernos', 'nise-control-systems-engineering'):
        assert CATALOGO[protegido]['uso'] == 'referencia'


def test_anotacoes_e_imagens_fora_do_repositorio():
    arquivos = [p for p in (ROOT / 'disciplinas/controle').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.webp', '.docx', '.pptx')]
    for x in ITENS.values():
        if x['natureza'] == 'material_da_disciplina':
            assert x['publicacao_transcricao'].startswith('autorizada pelo autor') and 'fora do repositório' in x['licenca']
    rastreados = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout
    assert not [l for l in rastreados.splitlines() if re.search(r'_26\d{4}_\d{6}\.pdf$', l)]


def test_documentacao_lista_fontes_e_blocos():
    curadoria = (ROOT / 'disciplinas/controle/CURADORIA.md').read_text(encoding='utf-8')
    assert [k for k in CATALOGO if f'`{k}`' not in curadoria] == []
    assert [k for k in ITENS if f'`{k}`' not in curadoria] == []
