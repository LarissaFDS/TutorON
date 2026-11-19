"""Acervo de Sinais e Sistemas e conferência das resoluções.

Cada resultado escrito num bloco é refeito aqui com SymPy (integrais, `apart`, `dsolve`, transformadas) ou
SciPy/numpy (convolução numérica, coeficientes de Fourier por integração, `freqresp`, `lsim`, `step`).
Os erros encontrados nas anotações do aluno são conferidos como erros, e a correção como correção.
"""
import cmath
import json
import math
import re
import shutil
import subprocess

import numpy as np
import pytest
import sympy as sp
from scipy import integrate, signal

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

SS = disciplinas.obter('sinais')
FONTES = read_json(ROOT / 'disciplinas/sinais/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {x['id']: x for x in read_json(SS.itens)}
NA_BUSCA = {c['id'] for c in read_json(SS.indice)['chunks']}
VETORES = json.loads((ROOT / 'eval/relevancia-vetores.json').read_text(encoding='utf-8'))
t, tau, w = sp.symbols('t tau omega', real=True)
s = sp.Symbol('s')
tp = sp.Symbol('t', positive=True)


def texto(ident):
    return ITENS[ident]['texto']


def buscar(pergunta, d=SS):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def hibrida(pergunta, d=SS):
    """A mesma busca do backend (corte e penalidade de hub), com o embedding real gravado da pergunta."""
    return [r['id'] for r in search(pergunta, k=4, vector=VETORES[pergunta], min_similarity=0.45, hub_penalty=True,
                                    itens=d.itens, indice=d.indice)]


def ilaplace(F):
    """Inversa por frações parciais (mais rápida e estável que inverse_laplace_transform genérica)."""
    return sp.simplify(sp.inverse_laplace_transform(sp.apart(sp.nsimplify(F), s), s, tp))


# ---------------------------------------------------------------- cadastro e acervo

def test_sinais_cadastrada_com_acervo_proprio_e_a_mesma_ia():
    assert SS.nome == 'Sinais e Sistemas' and SS.itens.exists() and SS.indice.exists()
    assert not SS.livro_supabase and SS.rigor.strip() == (ROOT / 'disciplinas/sinais/rigor.md').read_text(encoding='utf-8').strip()
    assert all(c['disciplina'] == 'sinais' for c in read_json(SS.indice)['chunks'])
    for outra in ('paa', 'sd', 'oac', 'calc3', 'fis2', 'ed', 'bd', 'prob', 'circ'):
        d = disciplinas.obter(outra)
        assert NA_BUSCA.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    bruto = [d for d in read_json(ROOT / 'disciplinas/disciplinas.json')['disciplinas'] if d['id'] == 'sinais'][0]
    assert not {'modelo', 'model', 'provedor', 'endpoint', 'prompt', 'chave'} & set(bruto)
    assert read_json(SS.indice)['embedding_model'] == read_json(disciplinas.obter('circ').indice)['embedding_model']


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas sinais --embeddings`."""
    gerados = disciplinas.registros(SS)
    assert gerados == read_json(SS.itens)
    assert NA_BUSCA == {x['id'] for x in gerados if x['confiabilidade'] in ('media', 'alta')}
    assert read_json(SS.indice)['modo'] == 'hibrido'


def test_blocos_cabem_no_trecho_e_formulas_fecham():
    for x in ITENS.values():
        assert len(x['texto']) <= 2200, x['id']
        sem_destaque = x['texto'].replace('$$', '')
        assert x['texto'].count('$$') % 2 == 0 and sem_destaque.count('$') % 2 == 0, x['id']
        assert '**Verificação:**' in x['texto'], x['id']


def test_notas_de_ia_sem_revisao_ficam_fora_da_busca():
    notas = [x for x in ITENS.values() if x['natureza'] == 'nota_da_equipe_ia']
    assert [x['id'] for x in notas] == ['sinais-nota-ia-tempo-discreto']
    assert all(x['status_curadoria'] == 'candidato' and x['revisao_humana'] == 'pendente' for x in notas)
    assert {x['id'] for x in notas}.isdisjoint(NA_BUSCA)
    assert not any(x.get('revisao_humana') == 'feita' or x.get('revisao_professor') for x in ITENS.values())


def test_topicos_com_anotacoes_tem_bloco_na_busca():
    """Critério de liberação: todo tópico "Sim" do mapeamento (01 a 10) tem bloco na busca; 11 fica "a confirmar"."""
    na_busca = {ITENS[x]['assunto'] for x in NA_BUSCA}
    sim = set(SS.assuntos) - {'sinais-11-tempo-discreto'}
    assert na_busca == sim and len(sim) == 10


# ---------------------------------------------------------------- status das resoluções

CORRIGIDAS = {'sinais-anot-numeros-complexos', 'sinais-anot-exponenciais', 'sinais-anot-degrau-rampa-impulso',
              'sinais-anot-memoria-causalidade', 'sinais-anot-bibo-invariancia', 'sinais-anot-edo-solucao',
              'sinais-anot-fracoes-parciais-complexos', 'sinais-anot-revisao-bibo', 'sinais-anot-revisao-realimentacao',
              'sinais-anot-questoes-prova'}


def test_resolucoes_tem_status_e_dizem_no_texto():
    turma = [x for x in ITENS.values() if x['natureza'] == 'material_da_disciplina']
    assert len(turma) == 28
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    for x in turma:
        assert f"Status da resolução: {rotulo[x['status_resolucao']]}" in x['texto'], x['id']
        assert x['verificacao'] == 'conferida_por_codigo' and x['revisao_humana'] == 'pendente'
    assert {x['id'] for x in turma if x['status_resolucao'] == 'corrigida'} == CORRIGIDAS
    assert all('correç' in texto(c).lower() or 'completou' in texto(c) for c in CORRIGIDAS)


# ---------------------------------------------------------------- 01 complexos

def test_complexos_polar_e_angulo_com_parte_real_negativa():
    r, th = cmath.polar(2 + 3j)
    assert math.isclose(r, math.sqrt(13)) and math.isclose(math.degrees(th), 56.31, abs_tol=0.01)
    # erro das anotações: atan(b/a) para a < 0 cai no quadrante errado
    assert math.isclose(math.degrees(math.atan(8 / -6)), -53.13, abs_tol=0.01)
    assert math.isclose(math.degrees(cmath.phase(-6 + 8j)), 126.87, abs_tol=0.01)
    z = 2 + 3j
    assert cmath.isclose(1 / z, (1 / r) * cmath.exp(-1j * th)) and cmath.isclose(z * z.conjugate(), abs(z) ** 2)
    assert not cmath.isclose(z.conjugate(), r * cmath.exp(1j * th))
    assert '126{,}87' in texto('sinais-anot-numeros-complexos')


# ---------------------------------------------------------------- 02 operações no tempo

def _x_exemplo(tau_):
    if -1 <= tau_ < 0:
        return 1.0
    if 0 <= tau_ <= 1:
        return tau_
    if 1 < tau_ <= 2:
        return 1.0
    return 0.0


def test_escalonamento_x_menos_t_sobre_2_mais_1():
    y = lambda t_: _x_exemplo(-t_ / 2 + 1)
    assert y(1) == 0.5 and y(3) == 1 and y(5) == 0 and y(-1) == 1 and y(-3) == 0
    assert y(0) == 1 and math.isclose(y(1.5), 0.25)


def _x_lista(tau_):
    if -6 <= tau_ < -3:
        return -(tau_ + 6) / 3
    if -3 <= tau_ < 0:
        return 1.0
    if 0 <= tau_ <= 3:
        return 1 - tau_ / 3
    return 0.0


def test_lista_transformacoes_pontos():
    assert _x_lista(-4.5 * 1) == -0.5
    assert _x_lista(-4.5 / 3 * 1) == 1  # x(−t/3) em t = 4,5
    assert _x_lista(2 - 6.5) == -0.5  # x(2 − t) em t = 6,5
    assert _x_lista(-(-1.5)) == 0.5  # x(−t) em t = −1,5 (meio da rampa de 0 a 1 em [−3, 0])
    assert _x_lista(3 + (-7.5)) == -0.5  # x(3 + t) em t = −7,5


# ---------------------------------------------------------------- 03 sinais elementares

def test_constante_de_tempo_valores():
    assert [round(math.exp(-k), 4) for k in range(1, 6)] == [0.3679, 0.1353, 0.0498, 0.0183, 0.0067]
    assert 'cai para' in texto('sinais-anot-exponenciais')


def test_degrau_escalonado_so_vale_para_a_positivo():
    u = lambda x: 1 if x >= 0 else 0
    a, t0 = -2, -4  # u(−2t + 4) = u(at − t0)
    assert u(a * 0 - t0) == 1 and u(a * 3 - t0) == 0
    # a fórmula das anotações, u(t − t0/a) = u(t − 2), daria o oposto:
    assert u(0 - t0 / a) == 0 and u(3 - t0 / a) == 1
    assert all(u(a * x - t0) == u(t0 / a - x) for x in np.linspace(-5, 5, 41))


def test_integrais_com_impulso():
    D = sp.DiracDelta
    casos = [(sp.cos(2 * t) * D(t), 1), (sp.sin(2 * t) * D(t - sp.pi / 4), 1),
             (sp.cos(2 * (t - sp.pi / 4)) * D(t - sp.pi / 4), 1), (sp.sin(t - 1) * D(t - 2), sp.sin(1)),
             (sp.sin(t - 1) * D(2 * t - 4), sp.sin(1) / 2)]
    for f, esperado in casos:
        assert sp.simplify(sp.integrate(f, (t, -sp.oo, sp.oo)) - esperado) == 0


# ---------------------------------------------------------------- 04 propriedades

def test_cascata_nao_linear_depende_da_ordem():
    T1, T2 = (lambda u: 2 * u), (lambda u: u + 1)
    assert T2(T1(3)) == 7 and T1(T2(3)) == 8


def test_ohmimetro():
    rx = lambda a: 9000 / a - 100
    assert (rx(15), rx(30), rx(90)) == (500, 200, 0)
    assert math.isclose(90000 * 0.1 / (100 + 500), 15)


def test_rc_com_memoria_derivada():
    R, C, v0 = sp.symbols('R C v0', positive=True)
    u = sp.Function('u')
    y = R * u(t) + sp.Integral(u(tau), (tau, 0, t)) / C + v0
    assert sp.simplify(y.diff(t) - (R * u(t).diff(t) + u(t) / C)) == 0
    assert 't \\ge 0' in texto('sinais-anot-memoria-causalidade')


def test_x_de_2t_e_variante_contraexemplo():
    p = lambda x: 1.0 if 0 <= x <= 1 else 0.0
    sistema = lambda x: (lambda t_: x(2 * t_))
    T = 1
    atrasa_saida = lambda t_: sistema(p)(t_ - T)
    atrasa_entrada = sistema(lambda x: p(x - T))
    assert atrasa_entrada(0.75) == 1 and atrasa_saida(0.75) == 0
    assert atrasa_saida(1.25) == 1 and atrasa_entrada(1.25) == 0
    assert 'Variante' in texto('sinais-anot-bibo-invariancia')


def test_indutor_nao_bibo_e_invariante():
    L = sp.Symbol('L', positive=True)
    rampa = sp.integrate(1 / L, (tau, 0, tp))
    assert sp.limit(rampa, tp, sp.oo) == sp.oo
    a = sp.Symbol('a', positive=True)
    assert sp.simplify(sp.integrate(sp.exp(-a * tau) / L, (tau, 0, tp)) - (1 - sp.exp(-a * tp)) / (a * L)) == 0


def test_sen2t_variante_e_linear_e_u2_nao_linear():
    u1, u2, a1, a2, T = sp.symbols('u1 u2 a1 a2 T')
    S = lambda u, tt: sp.sin(2 * tt) * u
    assert sp.simplify(S(a1 * u1 + a2 * u2, t) - (a1 * S(u1, t) + a2 * S(u2, t))) == 0
    assert sp.expand((a1 * u1 + a2 * u2) ** 2 - (a1 * u1 ** 2 + a2 * u2 ** 2)) != 0
    assert S(1, sp.pi / 4 - sp.pi / 4) == 0 and S(1, sp.pi / 4) == 1  # y(t − T) ≠ T[u(t − T)]
    assert sp.sin(2 * sp.pi / 2) == 0  # saída nula para qualquer u: não invertível


def test_integral_janela_causal_sse_alfa_maior_igual_1():
    def y(t_, alfa):
        a, b = t_ - alfa, t_ + 1 - alfa
        return max(0.0, b - max(a, 0.0)) if b > 0 else 0.0  # u = degrau
    assert y(-0.2, 1) == 0 and math.isclose(y(0.5, 1), 0.5) and y(2, 1) == 1
    assert math.isclose(y(-0.2, 0.5), 0.3)


# ---------------------------------------------------------------- 05 convolução

def test_convolucao_de_exponenciais():
    y = sp.integrate(sp.exp(-tau) * sp.exp(-2 * (tp - tau)), (tau, 0, tp))
    assert sp.simplify(y - (sp.exp(-tp) - sp.exp(-2 * tp))) == 0
    assert sp.simplify(sp.apart(1 / ((s + 1) * (s + 2)), s) - (1 / (s + 1) - 1 / (s + 2))) == 0


def test_resposta_ao_degrau_de_e_menos_3t():
    assert sp.simplify(sp.integrate(sp.exp(-3 * tau), (tau, 0, tp)) - (1 - sp.exp(-3 * tp)) / 3) == 0
    assert sp.integrate(sp.exp(-3 * tau), (tau, 0, sp.oo)) == sp.Rational(1, 3)


def _pecas_pulso_rampa(t_):
    if -1 <= t_ < 1:
        return (t_ + 1) ** 2 / 6
    if 1 <= t_ < 2:
        return 2 * t_ / 3
    if 2 <= t_ < 4:
        return -(t_ ** 2 - 2 * t_ - 8) / 6
    return 0.0


def test_convolucao_pulso_rampa_intervalos():
    dt = 1e-3
    tx = np.arange(-1, 1, dt)
    tg = np.arange(0, 3, dt)
    y = np.convolve(np.ones_like(tx), tg / 3) * dt
    ty = tx[0] + tg[0] + np.arange(len(y)) * dt
    for t_ in (-0.5, 0.5, 1.5, 2.5, 3.5):
        assert abs(np.interp(t_, ty, y) - _pecas_pulso_rampa(t_)) < 5e-3
    assert math.isclose(_pecas_pulso_rampa(1), 2 / 3) and math.isclose(_pecas_pulso_rampa(2), 4 / 3)
    assert abs(_pecas_pulso_rampa(4 - 1e-12)) < 1e-9 and math.isclose(np.sum(y) * dt, 3, rel_tol=1e-2)
    T_ = sp.Symbol('T', positive=True)
    lado1 = sp.integrate(1, (tau, 0, tp))
    lado2 = sp.integrate(1, (tau, tp - T_, T_))
    assert lado1 == tp and sp.simplify(lado2 - (2 * T_ - tp)) == 0  # dois pulsos: triângulo


def test_convolucao_exponencial_com_janela():
    y1 = sp.integrate(3 * sp.exp(-tau / 2), (tau, 0, tp))
    y2 = sp.integrate(3 * sp.exp(-tau / 2), (tau, tp - 2, tp))
    assert sp.simplify(y1 - 6 * (1 - sp.exp(-tp / 2))) == 0
    assert sp.simplify(y2 - 6 * (sp.E - 1) * sp.exp(-tp / 2)) == 0
    assert sp.simplify((y1 - y2).subs(tp, 2)) == 0
    dt = 1e-3
    tt = np.arange(0, 10, dt)
    yn = np.convolve(3 * np.exp(-tt / 2), (tt < 2).astype(float))[:len(tt)] * dt
    exato = np.where(tt < 2, 6 * (1 - np.exp(-tt / 2)), 6 * (math.e - 1) * np.exp(-tt / 2))
    assert np.max(np.abs(yn - exato)) < 1e-2


# ---------------------------------------------------------------- 06 EDO

def test_raizes_caracteristicas_e_edo_primeira_ordem():
    lam = sp.Symbol('lam')
    assert set(sp.roots(lam ** 2 + 5 * lam + 6)) == {-2, -3} and sp.roots(lam ** 2 + 4 * lam + 4) == {-2: 2}
    y = sp.Function('y')
    sol = sp.dsolve(y(t).diff(t) + 2 * y(t) - 2, y(t), ics={y(0): 4}).rhs
    assert sp.simplify(sol - (1 + 3 * sp.exp(-2 * t))) == 0


def test_diagrama_integradores_sinal_da_entrada():
    a0, a1, a2, a3, b0 = sp.symbols('a0 a1 a2 a3 b0', nonzero=True)
    u, y0, y1, y2 = sp.symbols('u y0 y1 y2')
    y3 = b0 / a3 * u - a2 / a3 * y2 - a1 / a3 * y1 - a0 / a3 * y0
    assert sp.simplify(a3 * y3 + a2 * y2 + a1 * y1 + a0 * y0 - b0 * u) == 0
    assert 'Correção' in texto('sinais-anot-edo-solucao')


# ---------------------------------------------------------------- 07 série de Fourier

def _ck(x, T0, k):
    w0 = 2 * math.pi / T0
    re_ = integrate.quad(lambda t_: x(t_) * math.cos(k * w0 * t_), 0, T0, limit=200)[0]
    im_ = integrate.quad(lambda t_: -x(t_) * math.sin(k * w0 * t_), 0, T0, limit=200)[0]
    return complex(re_, im_) / T0


def test_serie_cosseno():
    c = [_ck(lambda t_: math.cos(2 * math.pi * t_), 1, k) for k in range(-2, 3)]
    assert np.allclose(c, [0, 0.5, 0, 0.5, 0], atol=1e-9)


def test_serie_onda_quadrada():
    V, T0 = 2.0, 1.0
    x = lambda t_: V if (t_ % T0) < T0 / 2 else -V
    for k in range(1, 8):
        esperado = -2j * V / (k * math.pi) if k % 2 else 0
        assert abs(_ck(x, T0, k) - esperado) < 1e-6
    assert abs(_ck(x, T0, 0)) < 1e-9
    w0 = 2 * math.pi / T0
    soma = lambda t_: sum(4 * V / (k * math.pi) * math.sin(k * w0 * t_) for k in range(1, 200, 2))
    assert abs(soma(0.25) - V) < 0.02 and abs(soma(0.75) + V) < 0.02
    assert '4V' in texto('sinais-anot-serie-fourier-quadrada')


def test_serie_exponencial_periodica():
    T0 = math.pi
    x = lambda t_: math.exp(-(t_ % T0) / 2)
    K = 2 * (1 - math.exp(-math.pi / 2)) / math.pi
    assert math.isclose(K, 0.504, abs_tol=5e-4)
    for k in range(-3, 4):
        assert abs(_ck(x, T0, k) - K / (1 + 4j * k)) < 1e-6
    c1 = K / (1 + 4j)
    assert abs(c1 - (0.0297 - 0.1186j)) < 5e-4 and '0{,}0297' in texto('sinais-anot-serie-fourier-exponencial')


# ---------------------------------------------------------------- 08 transformada de Fourier

def test_tf_exponencial_e_pulso():
    a = sp.Symbol('a', positive=True)
    assert sp.simplify(sp.integrate(sp.exp(-a * tp) * sp.exp(-sp.I * w * tp), (tp, 0, sp.oo), conds='none')
                       - 1 / (a + sp.I * w)) == 0
    V, T = sp.symbols('V T', positive=True)
    X = sp.integrate(V * sp.exp(-sp.I * w * t), (t, -T / 2, T / 2))
    for wv in (0.3, 1.0, 2.5, -1.7):
        val = (X - 2 * V * sp.sin(w * T / 2) / w).subs({V: 1, T: 2, w: wv})
        assert abs(complex(sp.N(val))) < 1e-12
    re_ = integrate.quad(lambda t_: math.cos(t_), -1, 1)[0]
    assert math.isclose(re_, 2 * math.sin(1)) and math.isclose(2 * math.sin(1), 1.683, abs_tol=1e-3)
    # convenção normalizada: numpy.sinc(fT) com f = ω/2π dá o mesmo valor
    assert math.isclose(2 * np.sinc(1 / (2 * math.pi) * 2), 2 * math.sin(1) / 1)


def test_resposta_senoidal_g_j2():
    sis = signal.lti([10], [1, 3, 2])
    _, H = signal.freqresp(sis, [2.0])
    assert math.isclose(abs(H[0]), 1.5811, abs_tol=1e-4)
    assert math.isclose(math.degrees(cmath.phase(H[0])), -108.43, abs_tol=0.01)
    tt = np.linspace(0, 20, 20001)
    u = 5 * np.cos(2 * tt + math.radians(40))
    _, y, _ = signal.lsim(sis, u, tt)
    yss = 5 * abs(H[0]) * np.cos(2 * tt + math.radians(40) + cmath.phase(H[0]))
    assert np.max(np.abs(y[-2000:] - yss[-2000:])) < 1e-3
    assert math.isclose(5 * abs(H[0]), 7.906, abs_tol=1e-3)


# ---------------------------------------------------------------- 09 Laplace

def test_tabela_de_laplace():
    a, om = sp.symbols('a omega', positive=True)
    L = lambda f: sp.laplace_transform(f, tp, s, noconds=True)
    assert sp.simplify(L(sp.exp(a * tp)) - 1 / (s - a)) == 0
    assert sp.simplify(L(sp.cos(om * tp)) - s / (s ** 2 + om ** 2)) == 0
    assert sp.simplify(L(sp.sin(om * tp)) - om / (s ** 2 + om ** 2)) == 0
    assert sp.simplify(L(tp ** 3) - 6 / s ** 4) == 0
    assert sp.simplify(L(sp.exp(-a * tp) * sp.cos(om * tp)) - (s + a) / ((s + a) ** 2 + om ** 2)) == 0


def test_rl_com_degrau():
    V, R, Lh = sp.symbols('V R L', positive=True)
    I = V / (s * (R + Lh * s))
    i = sp.inverse_laplace_transform(sp.apart(I, s), s, tp)
    assert sp.simplify(i - V / R * (1 - sp.exp(-R * tp / Lh))) == 0
    assert sp.limit(s * I, s, 0) == V / R


# ---------------------------------------------------------------- 10 função de transferência

def test_funcao_transferencia_do_circuito():
    Y, U, Vc = sp.symbols('Y U Vc')
    sol = sp.solve([sp.Eq(U, sp.Rational(5, 2) * Y + s * Y + Vc), sp.Eq(Y, Vc / 2 + s * Vc)], [Y, Vc], dict=True)[0]
    G = sp.simplify(sol[Y] / U)
    assert sp.simplify(G - (s + sp.Rational(1, 2)) / (s ** 2 + 3 * s + sp.Rational(9, 4))) == 0
    assert sp.roots(s ** 2 + 3 * s + sp.Rational(9, 4)) == {sp.Rational(-3, 2): 2}
    assert G.subs(s, 0) == sp.Rational(2, 9)


def test_fracoes_parciais_polos_reais():
    y = ilaplace((7 * s + 10) / ((s ** 2 + 3 * s + 2) * (s + 5)))
    esperado = -sp.Rational(25, 12) * sp.exp(-5 * tp) + sp.Rational(3, 4) * sp.exp(-tp) + sp.Rational(4, 3) * sp.exp(-2 * tp)
    assert sp.simplify(y - esperado) == 0 and esperado.subs(tp, 0) == 0
    yf = sp.Function('y')
    sol = sp.dsolve(yf(t).diff(t, 2) + 4 * yf(t).diff(t) + 3 * yf(t) - 6, yf(t),
                    ics={yf(0): 1, yf(t).diff(t).subs(t, 0): -1}).rhs
    assert sp.simplify(sol - (2 - 2 * sp.exp(-t) + sp.exp(-3 * t))) == 0


def test_fracoes_parciais_polos_complexos_e_multiplos():
    theta = math.atan2(8, -6)
    assert math.isclose(math.degrees(theta), 126.87, abs_tol=0.01)
    tt = np.linspace(0, 2, 401)
    _, yst = signal.step(signal.lti([150], [1, 12, 100]), T=tt)
    formula = 1.5 + 15 / 8 * np.exp(-6 * tt) * np.cos(8 * tt - theta - math.pi / 2)
    assert np.max(np.abs(yst - formula)) < 1e-6
    y = ilaplace(8 / (s * (s + 2) ** 3))
    esperado = 1 - 2 * tp ** 2 * sp.exp(-2 * tp) - 2 * tp * sp.exp(-2 * tp) - sp.exp(-2 * tp)
    assert sp.simplify(y - esperado) == 0
    assert 'Correção' in texto('sinais-anot-fracoes-parciais-complexos')


def test_revisao_bibo_polos_e_regra_corrigida():
    G = (s + 1) / (s ** 2 + 3 * s - 4)
    assert set(sp.roots(sp.denom(G))) == {1, -4} and sp.roots(sp.numer(G)) == {-1: 1}
    assert any(sp.re(p) >= 0 for p in sp.roots(sp.denom(G)))  # não BIBO
    g = ilaplace(G)
    assert sp.simplify(g - (sp.Rational(2, 5) * sp.exp(tp) + sp.Rational(3, 5) * sp.exp(-4 * tp))) == 0
    K1, K2 = 8, 2
    assert sp.cancel((s + 1) / (s ** 2 + (3 + K2) * s - (4 - K1))) == 1 / (s + 4)
    assert sp.simplify(ilaplace(1 / (s + 4) ** 3) - tp ** 2 / 2 * sp.exp(-4 * tp)) == 0
    tx = texto('sinais-anot-revisao-bibo')
    assert 'parte real negativa' in tx and 'correção' in tx.lower()


def test_revisao_realimentacao_e_polo_imaginario():
    K = sp.Symbol('K')
    G = (s + 2) / (s ** 2 - 1)
    assert sp.simplify(G / (1 + K * G) - (s + 2) / (s ** 2 + K * s + 2 * K - 1)) == 0
    ks = sp.solve(K ** 2 - 8 * K + 4, K)
    assert set(ks) == {4 - 2 * sp.sqrt(3), 4 + 2 * sp.sqrt(3)}
    for k in ks:
        assert sp.simplify(k ** 2 - 4 * (2 * k - 1)) == 0  # discriminante nulo: polo duplo em −K/2
        assert sp.simplify((s ** 2 + k * s + 2 * k - 1).subs(s, -k / 2)) == 0 and float(-k / 2) < 0
    y = ilaplace(100 / ((s + 1) * (s ** 2 + 100)))
    esperado = sp.Rational(100, 101) * (sp.exp(-tp) - sp.cos(10 * tp) + sp.sin(10 * tp) / 10)
    assert sp.simplify(y - esperado) == 0
    th = math.degrees(cmath.phase(-10 + 1j))
    assert math.isclose(th, 174.29, abs_tol=0.01) and math.isclose(math.degrees(math.atan(1 / -10)), -5.71, abs_tol=0.01)
    tt = np.linspace(0, 3, 301)
    alt = 100 / 101 * np.exp(-tt) + 10 / math.sqrt(101) * np.cos(10 * tt - math.radians(th))
    assert np.allclose(alt, [float(esperado.subs(tp, x)) for x in tt], atol=1e-9)


def test_questoes_de_prova():
    yf = sp.Function('y')
    K = sp.Rational(9, 8)
    assert sp.roots(s ** 2 + 3 * s + 2 * K) == {sp.Rational(-3, 2): 2}
    y1 = ilaplace(2 * K / (s * (s ** 2 + 3 * s + 2 * K)))
    assert sp.simplify(y1 - (1 - sp.exp(-3 * tp / 2) - sp.Rational(3, 2) * tp * sp.exp(-3 * tp / 2))) == 0
    passo = 1 - 2 * sp.exp(tp) + sp.exp(2 * tp)
    h = passo.diff(tp)
    G = sp.simplify(sp.laplace_transform(h, tp, s, noconds=True))
    assert sp.simplify(G - 2 / (s ** 2 - 3 * s + 2)) == 0
    k1, k2 = 0, 3
    assert sp.expand(s ** 2 + (2 * k2 - 3) * s + 2 * (1 + k1)) == s ** 2 + 3 * s + 2
    M = sp.Rational(1, 17)
    sol = sp.dsolve(yf(t).diff(t, 2) + 2 * yf(t).diff(t) + yf(t) / 2 - sp.exp(-4 * t) / 2, yf(t),
                    ics={yf(0): M, yf(t).diff(t).subs(t, 0): -4 * M}).rhs
    assert sp.simplify(sol - M * sp.exp(-4 * t)) == 0


# ---------------------------------------------------------------- busca

EXEMPLOS = [
    ('Como saber se y(t) = x(2t) é invariante no tempo?', {'sinais-anot-bibo-invariancia'}),
    ('Como calcular a convolução de dois pulsos retangulares?', {'sinais-anot-convolucao-pulsos'}),
    ('Quais os coeficientes da série de Fourier de uma onda quadrada?', {'sinais-anot-serie-fourier-quadrada'}),
    ('Como saber se G(s) = (s+1)/(s²+3s−4) é BIBO estável?', {'sinais-anot-revisao-bibo'}),
    ('Qual a transformada de Fourier de um pulso retangular?', {'sinais-anot-tf-pulso'}),
]
VARIANTES = [
    (r'O sistema $y(t) = x(2t)$ é invariante no tempo?', 'O sistema y de t igual a x de 2t é invariante no tempo?', EXEMPLOS[0][1]),
    (r'Calcule $\mathrm{rect}(t) * \mathrm{rect}(t)$ pela integral de convolução',
     'Calcule a convolução de um pulso retangular com ele mesmo', EXEMPLOS[1][1]),
    (r'Quais os $c_k$ da série de Fourier de uma onda quadrada de amplitude $V$?',
     'Quais os coeficientes ck da série de Fourier de uma onda quadrada de amplitude V?', EXEMPLOS[2][1]),
    (r'$G(s) = \frac{s+1}{s^2+3s-4}$ é BIBO estável?', 'G de s igual a s mais 1 sobre s ao quadrado mais 3s menos 4 é BIBO estável?',
     EXEMPLOS[3][1]),
    (r'Qual a transformada $X(\omega)$ de $\mathrm{rect}(t/T)$?', 'Qual a transformada de Fourier X de ômega do pulso retangular de largura T?',
     EXEMPLOS[4][1]),
]
FORA = ['Como simplificar uma função com mapa de Karnaugh?', 'Como fazer um LEFT JOIN em SQL?', 'Me conte uma piada',
        'Qual o equivalente de Thévenin com fonte dependente?']


def test_exemplos_do_cadastro_sao_os_testados():
    assert list(SS.exemplos) == [p for p, _ in EXEMPLOS]


@pytest.mark.parametrize('pergunta, aceitos', EXEMPLOS)
def test_perguntas_de_exemplo_trazem_o_bloco_certo(pergunta, aceitos):
    assert aceitos & set(hibrida(pergunta))


@pytest.mark.parametrize('latex, simples, aceitos', VARIANTES)
def test_latex_e_texto_simples_trazem_o_mesmo_bloco(latex, simples, aceitos):
    assert aceitos & set(hibrida(latex)) and aceitos & set(hibrida(simples))


@pytest.mark.parametrize('pergunta', FORA[:3])
def test_pergunta_de_outra_area_nao_traz_material(pergunta):
    assert hibrida(pergunta) == []


def test_isolamento_com_as_disciplinas_de_fronteira():
    """Fronteiras com acervo: Circuitos Elétricos e Cálculo 3, nas duas direções. Controle e Comunicações não têm acervo."""
    circ, calc3 = disciplinas.obter('circ'), disciplinas.obter('calc3')
    for p, _ in EXEMPLOS:
        assert not any(x.startswith('sinais-') for x in buscar(p, circ) + buscar(p, calc3))
    for p in ('Como calcular o equivalente de Thévenin com uma fonte dependente?',
              'Como calcular uma integral dupla em coordenadas polares?'):
        assert not any(x.startswith(('circ-', 'calc3-')) for x in buscar(p))
    assert not any(x.startswith('sinais-') for x in buscar(FORA[3], circ))


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
        assert set(f['topicos']) <= set(SS.assuntos), f['id']
    assert {x for i_ in ITENS.values() for x in i_['fontes_catalogo']} - {'nenhuma'} <= set(CATALOGO)
    assert {k for k, f in CATALOGO.items() if f['uso'] == 'acervo'} == {'ufal-sinais-anotacoes-otavio-2026-1'}
    aut = CATALOGO['ufal-sinais-anotacoes-otavio-2026-1']['autorizacao_transcricao']
    assert aut['data'] == '2026-11-18' and aut['aprovacao_professor'] == 'não declarada'
    for protegido in ('lathi-sinais-sistemas-lineares', 'oppenheim-willsky-signals-systems', 'haykin-veen-sinais-sistemas'):
        assert CATALOGO[protegido]['uso'] == 'referencia'


def test_anotacoes_e_imagens_fora_do_repositorio():
    arquivos = [p for p in (ROOT / 'disciplinas/sinais').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.webp', '.docx', '.pptx')]
    for x in ITENS.values():
        if x['natureza'] == 'material_da_disciplina':
            assert x['publicacao_transcricao'].startswith('autorizada pelo autor') and 'fora do repositório' in x['licenca']
    rastreados = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout
    assert not [l for l in rastreados.splitlines() if re.search(r'_26\d{4}_\d{6}\.pdf$', l)]


def test_documentacao_lista_fontes_e_blocos():
    curadoria = (ROOT / 'disciplinas/sinais/CURADORIA.md').read_text(encoding='utf-8')
    assert [k for k in CATALOGO if f'`{k}`' not in curadoria] == []
    assert [k for k in ITENS if f'`{k}`' not in curadoria] == []
