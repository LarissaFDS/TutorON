"""Acervo de Princípios de Comunicação e conferência das resoluções.

Cada resultado escrito num bloco é refeito aqui com NumPy (FFT, potência média, frequência instantânea),
SciPy (`special.jv`, `signal.butter`/`filtfilt`, `hilbert`) e SymPy (identidades). Os erros encontrados nas
anotações do aluno são conferidos como erros, e a correção como correção.
"""
import json
import math
import re
import shutil
import subprocess
from fractions import Fraction

import numpy as np
import pytest
import sympy as sp
from scipy import signal, special

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

PC = disciplinas.obter('pcom')
FONTES = read_json(ROOT / 'disciplinas/pcom/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {x['id']: x for x in read_json(PC.itens)}
NA_BUSCA = {c['id'] for c in read_json(PC.indice)['chunks']}
VETORES = json.loads((ROOT / 'eval/relevancia-vetores.json').read_text(encoding='utf-8'))
SEM_MATERIAL = {'pcom-03-ssb-vsb', 'pcom-07-amostragem-pcm', 'pcom-09-ruido-processos',
                'pcom-10-banda-base-codificacao-linha', 'pcom-11-enlaces-teoria-informacao'}


def texto(ident):
    return ITENS[ident]['texto']


def buscar(pergunta, d=PC):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def hibrida(pergunta, d=PC):
    return [r['id'] for r in search(pergunta, k=4, vector=VETORES[pergunta], min_similarity=0.45, hub_penalty=True,
                                    itens=d.itens, indice=d.indice)]


def linhas(x, fs):
    """Espectro bilateral normalizado (peso de cada impulso em Hz) para um trecho de duração inteira."""
    X = np.fft.fft(x) / len(x)
    f = np.fft.fftfreq(len(x), 1 / fs)
    return f, np.abs(X)


def peso(f, X, f0):
    return X[np.argmin(np.abs(f - f0))]


def ideal(x, fc, fs):
    """Passa-baixas ideal (o dos enunciados): zera o espectro acima de fc."""
    X = np.fft.fft(x)
    X[np.abs(np.fft.fftfreq(len(x), 1 / fs)) > fc] = 0
    return np.fft.ifft(X).real


def passa_baixas(x, fc, fs, ordem=6):
    b, a = signal.butter(ordem, fc / (fs / 2))
    return signal.filtfilt(b, a, x)


# ---------------------------------------------------------------- cadastro e acervo

def test_pcom_cadastrada_com_acervo_proprio_e_a_mesma_ia():
    assert PC.nome == 'Princípios de Comunicação' and PC.itens.exists() and PC.indice.exists()
    assert not PC.livro_supabase and PC.rigor.strip() == (ROOT / 'disciplinas/pcom/rigor.md').read_text(encoding='utf-8').strip()
    assert all(c['disciplina'] == 'pcom' for c in read_json(PC.indice)['chunks'])
    for outra in ('paa', 'sd', 'oac', 'calc3', 'fis2', 'ed', 'bd', 'prob', 'circ', 'sinais', 'controle'):
        d = disciplinas.obter(outra)
        assert NA_BUSCA.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    bruto = [d for d in read_json(ROOT / 'disciplinas/disciplinas.json')['disciplinas'] if d['id'] == 'pcom'][0]
    assert not {'modelo', 'model', 'provedor', 'endpoint', 'prompt', 'chave'} & set(bruto)
    assert read_json(PC.indice)['embedding_model'] == read_json(disciplinas.obter('sinais').indice)['embedding_model']


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas pcom --embeddings`."""
    gerados = disciplinas.registros(PC)
    assert gerados == read_json(PC.itens)
    assert NA_BUSCA == {x['id'] for x in gerados if x['confiabilidade'] in ('media', 'alta')}
    assert read_json(PC.indice)['modo'] == 'hibrido'


def test_blocos_cabem_no_trecho_e_formulas_fecham():
    for x in ITENS.values():
        assert len(x['texto']) <= 2200, x['id']
        sem_destaque = x['texto'].replace('$$', '')
        assert x['texto'].count('$$') % 2 == 0 and sem_destaque.count('$') % 2 == 0, x['id']
        assert '**Verificação:**' in x['texto'], x['id']


def test_notas_de_ia_sem_revisao_ficam_fora_da_busca():
    notas = [x for x in ITENS.values() if x['natureza'] == 'nota_da_equipe_ia']
    assert {x['assunto'] for x in notas} == SEM_MATERIAL and len(notas) == 5
    assert all(x['status_curadoria'] == 'candidato' and x['revisao_humana'] == 'pendente' for x in notas)
    assert {x['id'] for x in notas}.isdisjoint(NA_BUSCA)
    assert not any(x.get('revisao_humana') == 'feita' or x.get('revisao_professor') for x in ITENS.values())


def test_topicos_com_anotacoes_tem_bloco_na_busca():
    """Critério de liberação: todo tópico "Sim" (01, 02, 04, 05, 06, 08) tem bloco na busca."""
    na_busca = {ITENS[x]['assunto'] for x in NA_BUSCA}
    sim = set(PC.assuntos) - SEM_MATERIAL
    assert na_busca == sim and len(sim) == 6


# ---------------------------------------------------------------- status das resoluções

CORRIGIDAS = {'pcom-anot-fourier-cosseno-espectro', 'pcom-anot-identidades-produto-cossenos', 'pcom-anot-dsb-sc',
              'pcom-anot-demodulacao-coerente', 'pcom-anot-am-convencional-indice', 'pcom-prova-am-potencia-88w',
              'pcom-revisao-am-envoltoria', 'pcom-prova-filtro-cos2-8000t', 'pcom-lista1-produto-cossenos',
              'pcom-anot-largura-banda-am-dsb', 'pcom-anot-pm-fm-diferenca', 'pcom-anot-desvio-beta-carson',
              'pcom-lista2-fm-kf-bessel', 'pcom-lista2-fm-desvio-potencia'}
PENDENTES = {'pcom-prova-filtro-17khz', 'pcom-prova-angulo-dobra-amplitude', 'pcom-lista3-eficiencia-espectral',
             'pcom-lista4-exposicao-60hz', 'pcom-lista4-distancia-separacao'}


def test_resolucoes_tem_status_e_dizem_no_texto():
    turma = [x for x in ITENS.values() if x['natureza'] == 'material_da_disciplina']
    assert len(turma) == 28
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    for x in turma:
        assert f"Status da resolução: {rotulo[x['status_resolucao']]}" in x['texto'], x['id']
        assert x['verificacao'] == 'conferida_por_codigo' and x['revisao_humana'] == 'pendente'
    assert {x['id'] for x in turma if x['status_resolucao'] == 'corrigida'} == CORRIGIDAS
    assert {x['id'] for x in turma if x['status_resolucao'] == 'pendente_professor'} == PENDENTES
    assert all('correç' in texto(c).lower() or 'complemento' in texto(c).lower() for c in CORRIGIDAS)
    assert all('pendente' in texto(c).lower() or 'confirme' in texto(c).lower() for c in PENDENTES)


# ---------------------------------------------------------------- 01 sinais e espectro

def test_frequencia_instantanea_e_unidades():
    fs = 1e6
    t = np.arange(0, 0.01, 1 / fs)
    fi = np.diff(6000 * np.pi * t) / np.diff(t) / (2 * np.pi)
    assert np.allclose(fi, 3000)


def test_espectro_do_cosseno_meio_a_meio():
    fs = 20000
    t = np.arange(0, 1, 1 / fs)
    f, X = linhas(3 * np.cos(2 * np.pi * 1000 * t) + 2 * np.cos(2 * np.pi * 3000 * t), fs)
    for f0, w in ((1000, 1.5), (-1000, 1.5), (3000, 1.0), (-3000, 1.0)):
        assert math.isclose(peso(f, X, f0), w, abs_tol=1e-9)
    assert 'X(\\omega)' in texto('pcom-anot-fourier-cosseno-espectro')


def test_identidade_produto_de_cossenos_com_sinal_mais():
    a, b = sp.symbols('a b')
    assert sp.simplify(sp.cos(a) * sp.cos(b) - (sp.cos(a + b) + sp.cos(a - b)) / 2) == 0
    assert sp.simplify(sp.cos(a) * sp.cos(b) - (sp.cos(a + b) - sp.cos(a - b)) / 2) != 0  # erro da revisão
    assert sp.simplify(sp.cos(a) ** 2 - (1 + sp.cos(2 * a)) / 2) == 0
    t = np.linspace(0, 0.01, 1000)
    assert np.allclose(2 * np.cos(1000 * np.pi * t) * np.cos(5000 * np.pi * t),
                       np.cos(6000 * np.pi * t) + np.cos(4000 * np.pi * t))


# ---------------------------------------------------------------- 02 AM e DSB

def test_dsb_sc_sem_linha_da_portadora():
    fs = 200
    t = np.arange(0, 1, 1 / fs)
    f, X = linhas(np.cos(2 * np.pi * 2 * t) * np.cos(2 * np.pi * 10 * t), fs)
    for f0 in (8, 12, -8, -12):
        assert math.isclose(peso(f, X, f0), 0.25, abs_tol=1e-9)
    assert peso(f, X, 10) < 1e-12


def test_demodulacao_coerente_e_erro_de_fase():
    fs = 48000
    t = np.arange(0, 0.2, 1 / fs)
    m = np.cos(2 * np.pi * 300 * t)
    c = np.cos(2 * np.pi * 1500 * t)
    y = passa_baixas(m * c * c, 1000, fs)
    meio = slice(len(t) // 4, 3 * len(t) // 4)
    assert np.max(np.abs(y[meio] - m[meio] / 2)) < 0.01
    y90 = passa_baixas(m * c * np.cos(2 * np.pi * 1500 * t + np.pi / 2), 1000, fs)
    assert np.max(np.abs(y90[meio])) < 0.01
    f, X = linhas((1 + m) * c * c, fs)
    for f0 in (0, 300, 2700, 3000, 3300):
        assert peso(f, X, f0) > 0.05


def test_am_indice_e_tabela_de_amplitudes():
    fs, fc, fm = 100000, 10000, 1000
    t = np.arange(0, 0.1, 1 / fs)
    s = (2 + np.cos(2 * np.pi * fm * t)) * np.cos(2 * np.pi * fc * t)
    env = np.abs(signal.hilbert(s))[1000:-1000]
    emax, emin = env.max(), env.min()
    assert math.isclose(emax, 3, abs_tol=0.01) and math.isclose(emin, 1, abs_tol=0.01)
    assert math.isclose((emax - emin) / (emax + emin), 0.5, abs_tol=0.005)
    f, X = linhas(s, fs)
    assert math.isclose(peso(f, X, fc), 1.0, abs_tol=1e-9)  # A/2
    assert math.isclose(peso(f, X, fc + fm), 0.25, abs_tol=1e-9)  # A mu / 4
    assert 'B = A_c\\mu' in texto('pcom-anot-am-convencional-indice')


def potencia(x):
    return float(np.mean(x ** 2))


def test_potencia_e_eficiencia_do_am():
    t = np.arange(0, 1, 1 / 100000)
    c = np.cos(2 * np.pi * 10000 * t)
    m = np.cos(2 * np.pi * 1000 * t)
    assert math.isclose(potencia((1 + m) * c), 0.75, abs_tol=1e-9)
    assert math.isclose(potencia(m * c), 0.25, abs_tol=1e-9)
    assert max(mu ** 2 / (2 + mu ** 2) for mu in np.linspace(0, 1, 101)) == pytest.approx(1 / 3)


def test_simulacao_k_m():
    t = np.linspace(0, 1, 10001)
    for K, M, mu, emax, emin in ((1, 2, 0.5, 3, 1), (2, 1, 2, 3, -1), (1, 1, 1, 2, 0)):
        env = M + K * np.cos(2 * np.pi * t)
        assert K / M == mu and math.isclose(env.max(), emax) and math.isclose(env.min(), emin, abs_tol=1e-9)


def test_prova_am_88w():
    assert Fraction(8, 12) == Fraction(2, 3)
    assert 12 ** 2 / 2 + 2 * 4 ** 2 / 2 == 88
    assert Fraction(144, 2) * (1 + Fraction(4, 9) / 2) == 88  # (A²/2)(1 + μ²/2)
    t = np.arange(0, 1, 1 / 100000)
    s = (12 + 8 * np.cos(2 * np.pi * 500 * t)) * np.cos(2 * np.pi * 5000 * t)
    assert math.isclose(potencia(s), 88, abs_tol=1e-6)


def test_revisao_envoltoria():
    assert (Fraction(3) - 1) / (3 + 1) == Fraction(1, 2) and Fraction(8 - 4, 8 + 4) == Fraction(1, 3)
    assert math.isclose(1 / 5.5e-3, 2000 / 11) and math.isclose(1 / 0.5e-3, 2000)
    t = np.arange(0, 1, 1 / 100000)
    s = (6 + 2 * np.cos(2 * np.pi * 1000 * t)) * np.cos(2 * np.pi * 10000 * t)
    assert math.isclose(potencia(s), 19, abs_tol=1e-6)


def test_revisao_espectro_impulsos_e_potencia_das_bandas():
    fs = 8e6
    t = np.arange(800) / fs
    s = (24 + 12 * np.cos(2 * np.pi * 0.5e6 * t)) * np.cos(2 * np.pi * 1e6 * t)
    f, X = linhas(s, fs)
    assert math.isclose(peso(f, X, 1e6), 12, abs_tol=1e-6)
    assert math.isclose(peso(f, X, 0.5e6), 3, abs_tol=1e-6) and math.isclose(peso(f, X, 1.5e6), 3, abs_tol=1e-6)
    B = math.sqrt(4 * 25)
    assert B == 10 and B / Fraction(2, 5) == 25


def test_largura_de_banda_am():
    fs = 1e6
    t = np.arange(0, 0.01, 1 / fs)
    s = (1 + 0.5 * np.cos(2 * np.pi * 4000 * t)) * np.cos(2 * np.pi * 100000 * t)
    f, X = linhas(s, fs)
    ocupadas = sorted({abs(round(x)) for x in f[X > 1e-6]})
    assert ocupadas == [96000, 100000, 104000] and ocupadas[-1] - ocupadas[0] == 8000


# ---------------------------------------------------------------- 05 esquemas com filtros

def test_filtro_dsb_18000pi():
    assert (22000 - 18000) / 2 == 2000  # 2πB = 4000π
    fs = 200000
    t = np.arange(0, 0.05, 1 / fs)
    m = np.cos(2 * np.pi * 2000 * t)
    y = passa_baixas(2 * m * np.cos(18000 * np.pi * t) * np.cos(18000 * np.pi * t), 5000, fs)
    meio = slice(len(t) // 4, 3 * len(t) // 4)
    assert np.max(np.abs(y[meio] - m[meio])) < 0.01
    assert (2000, 2 * 9000 - 2000) == (2000, 16000)


def test_prova_cos2_8000t_espectro():
    fs = 40000 / np.pi  # amostragem em rad/s: ω_s = 80000
    t = np.arange(0, 2 * np.pi, 1 / fs)
    # m(t) = cos(500t): um tom dentro do triângulo |ω| ≤ 1000
    m = np.cos(500 * t)
    b = m * np.cos(2000 * t) * 2 * np.cos(8000 * t) ** 2
    f, X = linhas(b, fs)
    w = 2 * np.pi * f
    perto = lambda w0: X[np.argmin(np.abs(w - w0))]
    assert math.isclose(perto(2500), 0.25, abs_tol=1e-6)  # ½ · ½
    assert math.isclose(perto(14500), 0.125, abs_tol=1e-6) and math.isclose(perto(18500), 0.125, abs_tol=1e-6)
    assert perto(16000) < 1e-9
    assert 3000 < 13000 and 'bilateral' in texto('pcom-prova-filtro-cos2-8000t')


def test_prova_17khz_duas_convencoes():
    B = sp.Symbol('B', positive=True)
    assert sp.solve(sp.Eq((2 * sp.pi * B + 16000 * sp.pi) * 2, 34000 * sp.pi), B) == [500]
    assert sp.solve(sp.Eq(8000 + B, 17000), B) == [9000]
    assert 4 * sp.Rational(1, 2) * 2 == 4  # pico em A
    assert '500 Hz' in texto('pcom-prova-filtro-17khz') and '9 kHz' in texto('pcom-prova-filtro-17khz')


def test_prova_x_cos1000pi_cadeia_completa():
    fs = 100000
    t = np.arange(0, 0.1, 1 / fs)
    x = 2 * np.cos(1000 * np.pi * t)
    s = x * np.cos(5000 * np.pi * t)
    f, X = linhas(s, fs)
    for f0 in (2000, 3000, -2000, -3000):
        assert math.isclose(peso(f, X, f0), 0.5, abs_tol=1e-9)
    h = ideal(s, 2500, fs)
    y = ideal(4 * h * np.cos(5000 * np.pi * t), 3000, fs)
    meio = slice(len(t) // 4, 3 * len(t) // 4)
    assert np.max(np.abs(y[meio] - x[meio])) < 0.01


def test_lista1_produto_cossenos():
    t = np.linspace(0, 0.01, 2001)
    m = np.cos(3000 * t) * np.cos(5000 * t)
    assert np.allclose(m, (np.cos(2000 * t) + np.cos(8000 * t)) / 2)
    esperado = (np.cos(4000 * t) + np.cos(10000 * t) + np.cos(14000 * t) + np.cos(20000 * t)) / 4
    assert np.allclose(m * np.cos(12000 * t), esperado)
    fs = 80000 / np.pi  # ω_s = 160000 rad/s; 2π s cabem inteiros
    tt = np.arange(0, 2 * np.pi, 1 / fs)
    f, X = linhas(np.cos(3000 * tt) * np.cos(5000 * tt) * np.cos(12000 * tt), fs)
    w = 2 * np.pi * f
    for w0 in (4000, 10000, 14000, 20000):
        assert math.isclose(X[np.argmin(np.abs(w - w0))], 1 / 8, abs_tol=1e-6)  # amplitude 1/4, linha bilateral 1/8


# ---------------------------------------------------------------- 04 modulação angular

def desvio_hz(fase, t):
    return np.max(np.abs(np.diff(fase) / np.diff(t))) / (2 * np.pi)


def test_pm_fm_e_desvio():
    t = np.linspace(0, 1, 2000001)
    assert math.isclose(desvio_hz(15 * np.sin(2 * np.pi * 60 * t), t), 900, rel_tol=1e-4)
    assert math.isclose(75 / 15, 5) and 2 * (75 + 15) == 180
    potencia_dentro = special.jv(0, 5) ** 2 + 2 * sum(special.jv(n, 5) ** 2 for n in range(1, 7))
    assert potencia_dentro > 0.98


def test_lista2_bessel_beta_05():
    assert math.isclose(2 * np.pi * 2 / (2 * np.pi * 100), 0.02)
    amp = [10 * abs(special.jv(n, 0.5)) for n in range(5)]
    for a, e in zip(amp, (9.385, 2.423, 0.306, 0.026, 0.0016)):
        assert math.isclose(a, e, rel_tol=0.02)
    fs = 20000
    t = np.arange(0, 1, 1 / fs)
    f, X = linhas(10 * np.cos(2 * np.pi * 1000 * t + 0.5 * np.sin(2 * np.pi * 100 * t)), fs)
    assert math.isclose(2 * peso(f, X, 1100), amp[1], rel_tol=1e-6)


def test_lista2_desvio_e_potencia():
    t = np.linspace(0, 2e-3, 2000001)
    assert math.isclose(desvio_hz(15 * np.sin(2 * np.pi * 5000 * t), t), 75000, rel_tol=1e-4)
    assert 2 * 75 == 150 and 2 * (75 + 5) == 160 and 100 ** 2 / 2 == 5000
    t2 = np.linspace(0, 0.1, 1000001)
    assert math.isclose(desvio_hz(np.sin(100 * np.pi * t2), t2), 50, rel_tol=1e-4)
    fora = 1 - special.jv(0, 15) ** 2 - 2 * sum(special.jv(n, 15) ** 2 for n in range(1, 17))
    assert fora < 0.02
    fs = 1e5
    tt = np.arange(0, 1, 1 / fs)
    assert math.isclose(potencia(100 * np.cos(2 * np.pi * 10000 * tt + np.sin(2 * np.pi * 50 * tt))), 5000, rel_tol=1e-6)


def test_angulo_dobra_amplitude_fm_e_pm():
    assert 2 * (4 + 1) * 3 == 30
    df_fm = 24
    assert (df_fm / 2, 2 * (df_fm + 2)) == (12, 52)
    beta_pm = 8
    assert (beta_pm * 2, 2 * (beta_pm + 1) * 2) == (16, 36)
    assert 2 * (5 + 1) * 3 == 36


# ---------------------------------------------------------------- 06 modulação digital

def test_taxas_digitais():
    assert 200 / 50 == 4 and 2 ** 4 == 16
    assert (10e6 / 20) / math.log2(32) == 100e3
    assert 2.4e3 / 2 == 1.2e3 and 3e3 / 1 == 3e3
    assert 120e6 / math.log2(64) == 20e6
    assert 50e3 * math.log2(16) == 200e3


def test_eficiencia_espectral():
    assert math.log2(4) == 2 and math.log2(16) == 4
    assert math.isclose(1 / (1 + 0.5), 0.67, abs_tol=0.005)
    assert math.isclose(2 / (1 + 0.25), 1.6)  # QPSK com α = 0,25 (gabarito da bateria; fora do bloco)
    assert 'aplique os mesmos passos' in texto('pcom-lista3-eficiencia-espectral')
    W = 1
    assert (2 * W * 2) / (2 * W) == math.log2(4)


def test_simulacao_digital_mapas():
    ask2 = {'00': 1, '01': 2, '10': 3, '11': 4}
    assert [ask2[b] for b in ('10', '00', '11', '01', '00', '11')] == [3, 1, 4, 2, 1, 4]
    ask3 = {format(i, '03b'): i + 1 for i in range(8)}
    assert [ask3[b] for b in ('100', '011', '010', '011', '000', '111')] == [5, 4, 3, 4, 1, 8]
    for fase, inicio in ((90, 1), (180, 0), (270, -1)):
        assert math.isclose(math.sin(math.radians(fase)), inicio, abs_tol=1e-12)
    t = np.linspace(0, 1, 101)
    assert np.allclose(np.cos(2 * np.pi * t + np.pi / 2), -np.sin(2 * np.pi * t))
    assert 5 * 2 == 10 and 1 / 2 == 0.5


# ---------------------------------------------------------------- 08 exposição a campos

def test_lista4_limites_e_soma():
    lim = {(cat, f): Fraction(k, f) for cat, k in (('ocup', 500), ('pub', 250)) for f in (60, 360)}
    assert round(float(lim['pub', 60]), 2) == 4.17 and round(float(lim['ocup', 360]), 2) == 1.39
    assert round(float(lim['pub', 360]), 3) == 0.694
    med = {60: Fraction(55, 10), 360: Fraction(7, 10)}
    assert all(med[f] < lim['ocup', f] for f in med) and all(med[f] > lim['pub', f] for f in med)
    soma_o = sum(med[f] / lim['ocup', f] for f in med)
    soma_p = sum(med[f] / lim['pub', f] for f in med)
    assert round(float(soma_o), 3) == 1.164 and round(float(soma_p), 3) == 2.328


def test_lista4_distancia():
    assert math.isclose(6 * math.sqrt(22.5e-3) / 3, 0.3)
    assert math.isclose(23 * math.sqrt(90e-3) / 3, 2.3)
    assert math.isclose(6 * math.sqrt(90e-3) / 3, 0.6)


# ---------------------------------------------------------------- busca

EXEMPLOS = [
    ('Como se calcula a largura de banda de um sinal AM a partir da banda da mensagem?', {'pcom-anot-largura-banda-am-dsb'}),
    ('Como calcular a largura de banda de FM pela regra de Carson?', {'pcom-anot-desvio-beta-carson', 'pcom-lista2-fm-desvio-potencia'}),
    ('Qual a diferença entre PM e FM?', {'pcom-anot-pm-fm-diferenca'}),
    ('Como se calcula a eficiência espectral de uma modulação digital como a QPSK?', {'pcom-lista3-eficiencia-espectral'}),
    ('Qual a largura de banda do filtro para recuperar m(t) num esquema DSB?', {'pcom-revisao-filtro-dsb-18000pi', 'pcom-anot-demodulacao-coerente', 'pcom-prova-filtro-17khz',
                                                                                 'pcom-prova-filtro-cos2-8000t'}),
]
VARIANTES = [
    (r'Qual o $\mu$ de $s(t) = [A + B\cos(\omega_m t)]\cos(\omega_c t)$ no AM?',
     'Qual o índice de modulação mi de s de t igual a A mais B cosseno de ômega m t vezes cosseno de ômega c t no AM?',
     {'pcom-anot-am-convencional-indice'}),
    (r'Regra de Carson $B_T = 2(\Delta f + f_m)$ com $\beta = 5$',
     'Regra de Carson BT igual a 2 vezes delta f mais fm com beta igual a 5', EXEMPLOS[1][1]),
    (r'Na FM $\omega_i = \omega_c + k_f m(t)$ e na PM $\phi = k_p m(t)$: qual a diferença?',
     'Na FM a frequência instantânea é ômega c mais kf m de t e na PM a fase é kp m de t: qual a diferença?', EXEMPLOS[2][1]),
    (r'Eficiência espectral $\eta = R_b/B_T$ da QPSK',
     'Eficiência espectral eta igual a Rb sobre BT da QPSK', EXEMPLOS[3][1]),
    (r'Filtro para recuperar $m(t)$ de $2m(t)\cos(18000\pi t)$',
     'Filtro para recuperar m de t de 2 m de t cosseno de 18000 pi t', EXEMPLOS[4][1]),
]
FORA = ['Como simplificar uma função com mapa de Karnaugh?', 'Como fazer um LEFT JOIN em SQL?', 'Me conte uma piada']


def test_exemplos_do_cadastro_sao_os_testados():
    assert list(PC.exemplos) == [p for p, _ in EXEMPLOS]


@pytest.mark.parametrize('pergunta, aceitos', EXEMPLOS)
def test_perguntas_de_exemplo_trazem_o_bloco_certo(pergunta, aceitos):
    assert aceitos & set(hibrida(pergunta))


@pytest.mark.parametrize('latex, simples, aceitos', VARIANTES)
def test_latex_e_texto_simples_trazem_o_mesmo_bloco(latex, simples, aceitos):
    assert aceitos & set(hibrida(latex)) and aceitos & set(hibrida(simples))


@pytest.mark.parametrize('pergunta', FORA)
def test_pergunta_de_outra_area_nao_traz_material(pergunta):
    assert hibrida(pergunta) == []


def test_isolamento_com_sinais_e_fisica2():
    """Nas duas direções: os acervos de Sinais e Física 2 não trazem blocos de Comunicação, e vice-versa."""
    sinais, fis2 = disciplinas.obter('sinais'), disciplinas.obter('fis2')
    for p, _ in EXEMPLOS:
        assert not any(x.startswith('pcom-') for x in buscar(p, sinais) + buscar(p, fis2))
    for p in list(sinais.exemplos) + list(fis2.exemplos):
        assert all(x.startswith('pcom-') for x in buscar(p))


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
        assert set(f['topicos']) <= set(PC.assuntos), f['id']
    assert {x for i_ in ITENS.values() for x in i_['fontes_catalogo']} - {'nenhuma'} <= set(CATALOGO)
    assert {k for k, f in CATALOGO.items() if f['uso'] == 'acervo'} == {'ufal-pcom-anotacoes-otavio-2026-2'}
    aut = CATALOGO['ufal-pcom-anotacoes-otavio-2026-2']['autorizacao_transcricao']
    assert aut['aprovacao_professor'] == 'não declarada'
    for protegido in ('lathi-modern-digital-analog-communication', 'haykin-intro-sistemas-comunicacao',
                      'proakis-salehi-communication-systems-engineering'):
        assert CATALOGO[protegido]['uso'] == 'referencia'


def test_anotacoes_e_imagens_fora_do_repositorio():
    arquivos = [p for p in (ROOT / 'disciplinas/pcom').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.webp', '.docx', '.pptx')]
    for x in ITENS.values():
        if x['natureza'] == 'material_da_disciplina':
            assert x['publicacao_transcricao'].startswith('autorizada pelo autor') and 'fora do repositório' in x['licenca']
    rastreados = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout
    assert not [l for l in rastreados.splitlines() if re.search(r'_26\d{4}_\d{6}\.pdf$', l)]


def test_documentacao_lista_fontes_e_blocos():
    curadoria = (ROOT / 'disciplinas/pcom/CURADORIA.md').read_text(encoding='utf-8')
    assert [k for k in CATALOGO if f'`{k}`' not in curadoria] == []
    assert [k for k in ITENS if f'`{k}`' not in curadoria] == []
