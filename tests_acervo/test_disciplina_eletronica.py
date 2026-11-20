"""Acervo de Eletrônica e conferência das resoluções.

Cada circuito descrito num bloco é remontado aqui a partir da descrição em palavras e resolvido com SymPy
(análise nodal com o modelo do diodo escolhido e conferência da hipótese de estado; malhas do TBJ na região
ativa e conferência da região). Os erros encontrados nas anotações do aluno são conferidos como erros, e a
correção como correção. ngspice não está instalado; a "simulação" do ceifador é uma varredura da entrada com
o modelo de queda constante, conferindo a hipótese em cada ponto.
"""
import json
import math
import re
import shutil
import subprocess

import numpy as np
import pytest
import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

EL = disciplinas.obter('eletronica')
FONTES = read_json(ROOT / 'disciplinas/eletronica/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {x['id']: x for x in read_json(EL.itens)}
NA_BUSCA = {c['id'] for c in read_json(EL.indice)['chunks']}
VETORES = json.loads((ROOT / 'eval/relevancia-vetores.json').read_text(encoding='utf-8'))
VBE = 0.7


def texto(ident):
    return ITENS[ident]['texto']


def tem(ident, *trechos):
    t = texto(ident)
    return all(x in t for x in trechos)


def buscar(pergunta, d=EL):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def hibrida(pergunta, d=EL):
    return [r['id'] for r in search(pergunta, k=4, vector=VETORES[pergunta], min_similarity=0.45, hub_penalty=True,
                                    itens=d.itens, indice=d.indice)]


def tbj(VCC, RB, RC, RE, beta, VBB=None, RF=0.0):
    """Ponto Q na região ativa. Malha da base: VBB = RB IB + VBE + RE IE (+ RC IE se houver realimentação RF)."""
    IB, IC, IE, VCE = sp.symbols('IB IC IE VCE')
    VBB = VCC if VBB is None else VBB
    rc_base = RC if RF else 0
    sol = sp.solve([sp.Eq(VBB, (RB + RF) * IB + VBE + RE * IE + rc_base * IE), sp.Eq(IC, beta * IB),
                    sp.Eq(IE, IC + IB), sp.Eq(VCC, (RC * IE if RF else RC * IC) + VCE + RE * IE)], [IB, IC, IE, VCE])
    return {k.name: float(v) for k, v in sol.items()}


# ---------------------------------------------------------------- cadastro e acervo

def test_eletronica_cadastrada_com_acervo_proprio_e_a_mesma_ia():
    assert EL.nome == 'Eletrônica' and EL.itens.exists() and EL.indice.exists()
    assert not EL.livro_supabase and EL.rigor.strip() == (ROOT / 'disciplinas/eletronica/rigor.md').read_text(encoding='utf-8').strip()
    assert all(c['disciplina'] == 'eletronica' for c in read_json(EL.indice)['chunks'])
    for outra in ('paa', 'sd', 'oac', 'calc3', 'fis2', 'ed', 'bd', 'prob', 'circ', 'sinais', 'controle'):
        d = disciplinas.obter(outra)
        assert NA_BUSCA.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    bruto = [d for d in read_json(ROOT / 'disciplinas/disciplinas.json')['disciplinas'] if d['id'] == 'eletronica'][0]
    assert not {'modelo', 'model', 'provedor', 'endpoint', 'prompt', 'chave'} & set(bruto)
    assert read_json(EL.indice)['embedding_model'] == read_json(disciplinas.obter('controle').indice)['embedding_model']


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas eletronica --embeddings`."""
    gerados = disciplinas.registros(EL)
    assert gerados == read_json(EL.itens)
    assert NA_BUSCA == {x['id'] for x in gerados if x['confiabilidade'] in ('media', 'alta')}
    assert read_json(EL.indice)['modo'] == 'hibrido'


def test_blocos_cabem_no_trecho_e_formulas_fecham():
    for x in ITENS.values():
        assert len(x['texto']) <= 2200, x['id']
        sem_destaque = x['texto'].replace('$$', '')
        assert x['texto'].count('$$') % 2 == 0 and sem_destaque.count('$') % 2 == 0, x['id']
        assert '**Verificação:**' in x['texto'], x['id']


def test_notas_de_ia_sem_revisao_ficam_fora_da_busca():
    notas = [x for x in ITENS.values() if x['natureza'] == 'nota_da_equipe_ia']
    assert sorted(x['id'] for x in notas) == ['eletronica-nota-ia-filtro-capacitivo', 'eletronica-nota-ia-mosfet',
                                              'eletronica-nota-ia-zener']
    assert all(x['status_curadoria'] == 'candidato' and x['revisao_humana'] == 'pendente' for x in notas)
    assert {x['id'] for x in notas}.isdisjoint(NA_BUSCA)
    assert not any(x.get('revisao_humana') == 'feita' or x.get('revisao_professor') for x in ITENS.values())


def test_topicos_com_anotacoes_tem_bloco_na_busca():
    """Critério de liberação: todo tópico "Sim" tem bloco na busca; Zener e MOSFET ficam "a confirmar"."""
    na_busca = {ITENS[x]['assunto'] for x in NA_BUSCA}
    sim = set(EL.assuntos) - {'eletronica-05-zener', 'eletronica-09-mosfet'}
    assert na_busca == sim and len(sim) == 7
    assert set(CATALOGO['ufal-eletronica-anotacoes-otavio-2026-2']['topicos']) == sim


# ---------------------------------------------------------------- status das resoluções

CORRIGIDAS = {'eletronica-anot-diodo-modelos', 'eletronica-anot-meia-onda', 'eletronica-anot-ceifador-paralelo',
              'eletronica-anot-emissor-tensoes-nos', 'eletronica-anot-realimentacao-coletor', 'eletronica-anot-modelo-re'}
PENDENTES = {'eletronica-anot-ponte-resistores-quadro'}


def test_resolucoes_tem_status_e_dizem_no_texto():
    turma = [x for x in ITENS.values() if x['natureza'] == 'material_da_disciplina']
    assert len(turma) == 19
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    for x in turma:
        assert f"Status da resolução: {rotulo[x['status_resolucao']]}" in x['texto'], x['id']
        assert x['verificacao'] == 'conferida_por_codigo' and x['revisao_humana'] == 'pendente'
    assert {x['id'] for x in turma if x['status_resolucao'] == 'corrigida'} == CORRIGIDAS
    assert {x['id'] for x in turma if x['status_resolucao'] == 'pendente_professor'} == PENDENTES
    assert all('**Correção' in texto(c) for c in CORRIGIDAS)


# ---------------------------------------------------------------- 01/02 diodo

def test_pico_e_rms():
    assert math.isclose(220 * math.sqrt(2), 311.13, abs_tol=0.01)
    assert math.isclose(120 * math.sqrt(2), 170, abs_tol=0.3)
    assert tem('eletronica-anot-diodo-modelos', '220\\sqrt{2} \\approx 311')


def test_porta_and_logica_negativa():
    Vo = 0 - VBE
    I = (Vo - (-5)) / 2.2e3
    assert I > 0 and (-5 - Vo) < VBE  # D2 conduz, D1 reverso com −4,3 V
    assert math.isclose(-5 - Vo, -4.3) and math.isclose(I * 1e3, 1.95, abs_tol=0.005)
    assert tem('eletronica-anot-porta-and-diodos', 'V_o = -0{,}7$ V', '-4{,}3$ V', '1{,}95$ mA')


def test_diodo_em_serie_com_onda_quadrada():
    I = (12 - VBE) / 4e3
    assert math.isclose(I * 1e3, 2.825) and math.isclose(I * 1.8e3, 5.085)
    vo_b = 12 - VBE + 4
    assert math.isclose(vo_b, 15.3) and math.isclose(vo_b / 10e3 * 1e3, 1.53)
    assert (-12) - (0 - 4) == -8  # diodo de (b) bloqueado em −12 V
    assert tem('eletronica-anot-diodo-serie-quadrada', '5{,}085', '15{,}3$ V', 'V_D = -8$ V')


# ---------------------------------------------------------------- 03 retificadores

def _media_rms(f, n=200000):
    t = np.linspace(0, 1, n, endpoint=False)
    v = f(2 * np.pi * t)
    return v.mean(), math.sqrt((v ** 2).mean())


def test_meia_onda_e_correcao_da_corrente_rms():
    vp = 220 * math.sqrt(2) - 0.984
    med, rms = _media_rms(lambda w: np.maximum(vp * np.sin(w), 0))
    assert math.isclose(med, 98.72, abs_tol=0.01) and math.isclose(rms, vp / 2, rel_tol=1e-4)
    imax, imed = vp / 10, med / 10
    assert math.isclose(imax / 2, 15.5, abs_tol=0.02)  # I_rms = I_max/2
    assert not math.isclose(imed / 2, imax / 2, rel_tol=0.1)  # o erro da revisão (I_med/2 = 4,9 A)
    assert tem('eletronica-anot-meia-onda', '98{,}72', 'I_{rms} = I_{max}/2', '15,5 A')


def test_onda_completa_em_ponte():
    vp = 220 * math.sqrt(2) - 2 * 0.983
    med, _ = _media_rms(lambda w: np.abs(vp * np.sin(w)))
    assert math.isclose(vp, 309.16, abs_tol=0.01) and math.isclose(med, 196.82, abs_tol=0.01)
    assert math.isclose(220 * math.sqrt(2) - 0.983, 310.14, abs_tol=0.01)
    assert tem('eletronica-anot-onda-completa-ponte', '309{,}16', '196{,}82', '120 Hz')


def test_ponte_ideal_100v():
    assert math.isclose(100 / 2.2e3 * 1e3, 45.45, abs_tol=0.005) and math.isclose(200 / math.pi, 63.66, abs_tol=0.005)
    assert tem('eletronica-anot-ponte-100v-piv', '45{,}45', 'PIV $= V_m = 100$ V')


def test_ponte_com_dois_diodos_e_resistores_nodal():
    R = sp.Integer(2200)
    Vo, VB = sp.symbols('Vo VB')
    pos = sp.solve([Vo - VB - 100, VB / R + Vo / R], [Vo, VB])  # D2 liga o nó de cima à saída
    assert pos[Vo] == 50 and -pos[Vo] < 0  # D1: ânodo no terra, cátodo em +50 V → reverso
    neg = sp.solve([(Vo - 100) / R + Vo / R], [Vo])  # D1 prende o nó de cima no terra, VB = 100
    assert neg[Vo] == 50 and 0 - neg[Vo] < 0  # D2: ânodo em 0, cátodo em 50 → reverso
    assert math.isclose(100 / math.pi, 31.83, abs_tol=0.005)
    assert tem('eletronica-anot-ponte-resistores', 'v_o = 50$', '31{,}8$ V')


def test_exercicio_31_divisor_por_tres():
    assert math.isclose(170 * 1.1 / 3.3, 56.67, abs_tol=0.005) and math.isclose(0.636 * 170 / 3, 36.04, abs_tol=0.005)
    assert ITENS['eletronica-anot-ponte-resistores-quadro']['status_resolucao'] == 'pendente_professor'


# ---------------------------------------------------------------- 04 ceifadores e grampeadores

def test_ceifador_paralelo_corrigido():
    def saida(vi):
        vo = vi / 2  # hipótese: diodo desligado
        if vo < VBE:
            return vo
        vo = VBE  # diodo ligado; confere corrente direta no diodo
        assert (vi - vo) / 1e3 - vo / 1e3 > 0
        return vo
    vi = np.linspace(-10, 10, 4001)
    vo = np.array([saida(v) for v in vi])
    assert math.isclose(vo.max(), 0.7) and math.isclose(vo.min(), -5)
    assert math.isclose(vi[np.argmax(vo >= VBE - 1e-12)], 1.4, abs_tol=0.01)
    assert saida(1.0) == 0.5  # erro da anotação: ela daria 0,7 V em todo o semiciclo positivo
    assert math.isclose((10 - VBE) / 1e3 * 1e3, 9.3)
    assert tem('eletronica-anot-ceifador-paralelo', 'v_i \\ge 1{,}4$ V', '9{,}3$ mA')


@pytest.mark.parametrize('vref, baixo, alto', [(0, 0, 40), (-5, -5, 35), (-10, -10, 30)])
def test_grampeadores(vref, baixo, alto):
    vc = -20 - vref  # diodo conduz em vi = −20 V
    vo = 20 - vc
    assert (vref, vo) == (baixo, alto) and vref - vo < 0 and vo - vref == 40


# ---------------------------------------------------------------- 06/07 TBJ

def test_polarizacao_fixa_e_saturacao():
    q50, q100 = tbj(12, 240e3, 2.2e3, 0, 50), tbj(12, 240e3, 2.2e3, 0, 100)
    assert math.isclose(q50['IB'] * 1e6, 47.08, abs_tol=0.005)
    assert math.isclose(q50['IC'] * 1e3, 2.354, abs_tol=0.001) and math.isclose(q50['VCE'], 6.82, abs_tol=0.005)
    assert math.isclose(q100['IC'] * 1e3, 4.708, abs_tol=0.001) and math.isclose(q100['VCE'], 1.64, abs_tol=0.005)
    icsat = 12 / 2.2e3
    assert q100['IC'] < icsat and q100['VCE'] > 0.2
    q120 = tbj(12, 240e3, 2.2e3, 0, 120)
    assert q120['IC'] > icsat and q120['VCE'] < 0  # hipótese "ativa" falha: saturado
    assert tem('eletronica-anot-polarizacao-fixa', '5{,}45', 'Na saturação não use $I_C = \\beta I_B$')


def test_polarizacao_estavel_no_emissor():
    q50, q100 = tbj(20, 430e3, 2e3, 1e3, 50), tbj(20, 430e3, 2e3, 1e3, 100)
    assert math.isclose(q50['IB'] * 1e6, 40.12, abs_tol=0.005) and math.isclose(q50['VCE'], 13.94, abs_tol=0.005)
    assert math.isclose(q100['IC'] * 1e3, 3.635, abs_tol=0.001) and math.isclose(q100['VCE'], 9.06, abs_tol=0.005)
    assert math.isclose((q100['IC'] / q50['IC'] - 1) * 100, 81.2, abs_tol=0.05)


def test_exercicio_parte2_refeito_e_erros_das_anotacoes():
    q = tbj(20, 430e3, 2e3, 1e3, 50)
    VE = q['IE'] * 1e3
    VB, VC = VE + VBE, 20 - 2e3 * q['IC']
    assert math.isclose(VE, 2.046, abs_tol=0.001) and math.isclose(VB, 2.746, abs_tol=0.001)
    assert math.isclose(VB, 20 - 430e3 * q['IB'], abs_tol=1e-9)
    assert math.isclose(VC, 15.99, abs_tol=0.005) and math.isclose(VC - VE, q['VCE'])
    assert VB - VC < 0  # junção BC reversa: ativa
    # erros: quedas tomadas por tensões de nó e VCE com sinal trocado
    assert math.isclose(430e3 * q['IB'], 17.25, abs_tol=0.01) and not math.isclose(430e3 * q['IB'], VB)
    assert math.isclose(2e3 * q['IC'], 4.01, abs_tol=0.01) and q['VCE'] > 0
    assert tem('eletronica-anot-emissor-tensoes-nos', '$+13{,}94$ V', '-13{,}24$ V', '**quedas**')


def test_divisor_de_tensao_thevenin():
    R1, R2 = 39e3, 3.9e3
    Rth, Vth = R1 * R2 / (R1 + R2), 22 * R2 / (R1 + R2)
    assert math.isclose(Rth, 3545.45, abs_tol=0.01) and math.isclose(Vth, 2.0)
    q50, q100 = tbj(22, Rth, 10e3, 1.5e3, 50, VBB=Vth), tbj(22, Rth, 10e3, 1.5e3, 100, VBB=Vth)
    assert math.isclose(q50['IB'] * 1e6, 16.24, abs_tol=0.005) and math.isclose(q50['VCE'], 12.64, abs_tol=0.005)
    assert math.isclose(q100['IC'] * 1e3, 0.838, abs_tol=0.001) and math.isclose(q100['VCE'], 12.35, abs_tol=0.005)
    assert math.isclose((q100['IC'] / q50['IC'] - 1) * 100, 3.25, abs_tol=0.01)
    # o circuito completo (sem Thévenin) dá o mesmo ponto Q
    VB, IB = sp.symbols('VB IB')
    s = sp.solve([(22 - VB) / R1 - VB / R2 - IB, VB - VBE - 101 * IB * 1.5e3], [VB, IB])
    assert math.isclose(float(s[IB]), q100['IB'], rel_tol=1e-9)


def test_realimentacao_de_coletor_completada():
    q = tbj(10, 0, 4.7e3, 1.2e3, 90, RF=250e3)
    assert math.isclose(q['IB'] * 1e6, 11.82, abs_tol=0.005) and math.isclose(q['IC'] * 1e3, 1.064, abs_tol=0.001)
    assert math.isclose(q['VCE'], 3.65, abs_tol=0.005)
    assert math.isclose(10 - 5.9e3 * q['IC'], 3.72, abs_tol=0.005)  # aproximação IE ≈ IC das anotações
    assert tem('eletronica-anot-realimentacao-coletor', '3{,}65$ V', '(3,72 V)')


def test_darlington():
    b1, b2 = sp.symbols('beta1 beta2')
    assert sp.expand((1 + b1) * (1 + b2) - 1) == b1 + b2 + b1 * b2
    assert tem('eletronica-anot-darlington', '\\beta_D = \\beta_1 + \\beta_2 + \\beta_1\\beta_2')


def test_projeto_rb_rc():
    IB = 2.5e-3 / 80
    RB, RC = (12 - VBE) / IB, 6 / 2.5e-3
    assert math.isclose(RB, 361.6e3) and math.isclose(RC, 2.4e3)
    q = tbj(12, RB, RC, 0, 80)
    assert math.isclose(q['IC'], 2.5e-3) and math.isclose(q['VCE'], 6.0)


# ---------------------------------------------------------------- 08 pequenos sinais

def test_modelo_re_emissor_comum_nodal():
    q = tbj(12, 470e3, 3e3, 0, 100)
    re_ = 0.026 / q['IE']
    assert math.isclose(q['IB'] * 1e6, 24.04, abs_tol=0.005) and math.isclose(re_, 10.71, abs_tol=0.005)
    beta, RB, RC = 100, 470e3, 3e3
    assert math.isclose(RB * beta * re_ / (RB + beta * re_), 1068, abs_tol=1)
    for ro, av, zo in ((None, -280, 3000), (50e3, -264.3, 2830)):
        vi, vo, ib = sp.symbols('vi vo ib')
        g_ro = 0 if ro is None else 1 / ro
        sol = sp.solve([ib - vi / (beta * re_), vo / RC + vo * g_ro + beta * ib], [vo, ib])
        assert math.isclose(float(sol[vo] / vi), av, abs_tol=0.2)
        assert math.isclose(1 / (1 / RC + g_ro), zo, abs_tol=0.5)
    assert tem('eletronica-anot-modelo-re', 'r_o \\approx V_A/I_{CQ}', '-264')


# ---------------------------------------------------------------- busca

EXEMPLOS = [
    ('Como saber se o diodo está conduzindo?', {'eletronica-anot-diodo-modelos'}),
    ('Qual a tensão de saída de um ceifador com diodo de silício e entrada de 10 V de pico?', {'eletronica-anot-ceifador-paralelo'}),
    ('Como calcular o ponto Q de um TBJ com polarização por divisor de tensão?', {'eletronica-anot-divisor-tensao'}),
    ('Qual a diferença entre retificador de meia onda e de onda completa?', {'eletronica-anot-onda-completa-ponte', 'eletronica-anot-meia-onda'}),
    ('Como saber se o transistor está saturado?', {'eletronica-anot-polarizacao-fixa'}),
]
VARIANTES = [
    (r'O diodo conduz se $V_A - V_K \ge 0{,}7$ V?', 'O diodo conduz se V A menos V K for maior que 0,7 volts?', EXEMPLOS[0][1]),
    (r'Como achar $I_B = \frac{V_{Th} - V_{BE}}{R_{Th} + (\beta+1)R_E}$ no divisor de tensão?',
     'Como achar I B igual a V Th menos V BE sobre R Th mais beta mais um vezes R E no divisor de tensão?', EXEMPLOS[2][1]),
    (r'Por que $V_{med} = 2V_p/\pi$ na onda completa e $V_p/\pi$ na meia onda?',
     'Por que a tensão média é dois vê pico sobre pi na onda completa e vê pico sobre pi na meia onda?', EXEMPLOS[3][1]),
    (r'Se $\beta I_B > I_{C,sat}$ o TBJ satura?',
     'Se beta vezes I B passar da corrente de saturação do coletor o transistor satura?', EXEMPLOS[4][1]),
]
FORA = ['Como simplificar uma função com mapa de Karnaugh?', 'Como fazer um LEFT JOIN em SQL?', 'Me conte uma piada']


def test_exemplos_do_cadastro_sao_os_testados():
    assert list(EL.exemplos) == [p for p, _ in EXEMPLOS]


@pytest.mark.parametrize('pergunta, aceitos', EXEMPLOS)
def test_perguntas_de_exemplo_trazem_o_bloco_certo(pergunta, aceitos):
    assert aceitos & set(hibrida(pergunta))


@pytest.mark.parametrize('latex, simples, aceitos', VARIANTES)
def test_latex_e_texto_simples_trazem_o_mesmo_bloco(latex, simples, aceitos):
    assert aceitos & set(hibrida(latex)) and aceitos & set(hibrida(simples))


@pytest.mark.parametrize('pergunta', FORA)
def test_pergunta_de_outra_area_nao_traz_material(pergunta):
    assert hibrida(pergunta) == []


def test_isolamento_com_circuitos_e_sistemas_digitais():
    """Nas duas direções: os acervos de Circuitos e SD não trazem blocos de Eletrônica, e vice-versa."""
    circ, sd = disciplinas.obter('circ'), disciplinas.obter('sd')
    for p, _ in EXEMPLOS:
        assert not any(x.startswith('eletronica-') for x in buscar(p, circ) + buscar(p, sd))
    for p in list(circ.exemplos) + list(sd.exemplos):
        assert not any(x.startswith(('circ-', 'sd-')) for x in buscar(p))


# ---------------------------------------------------------------- KaTeX, catálogo e restrições

FORMULA = re.compile(r'\$\$(.+?)\$\$|\$(.+?)\$', re.S)


@pytest.mark.skipif(not shutil.which('node'), reason='node indisponível')
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for x in ITENS.values() for a, b in FORMULA.findall(x['texto'])]
    assert len(formulas) > 150
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
        assert set(f['topicos']) <= set(EL.assuntos), f['id']
    assert {x for i_ in ITENS.values() for x in i_['fontes_catalogo']} - {'nenhuma'} <= set(CATALOGO)
    assert {k for k, f in CATALOGO.items() if f['uso'] == 'acervo'} == {'ufal-eletronica-anotacoes-otavio-2026-2'}
    assert CATALOGO['ufal-eletronica-anotacoes-otavio-2026-2']['autorizacao_transcricao']['aprovacao_professor'] == 'não declarada'
    for protegido in ('boylestad-dispositivos-eletronicos', 'sedra-smith-microeletronica'):
        assert CATALOGO[protegido]['uso'] == 'referencia'


def test_anotacoes_e_imagens_fora_do_repositorio():
    arquivos = [p for p in (ROOT / 'disciplinas/eletronica').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.webp', '.docx', '.pptx')]
    for x in ITENS.values():
        if x['natureza'] == 'material_da_disciplina':
            assert x['publicacao_transcricao'].startswith('autorizada pelo autor') and 'fora do repositório' in x['licenca']
    rastreados = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout
    assert not [l for l in rastreados.splitlines() if re.search(r'_26\d{4}_\d{6}\.pdf$', l)]


def test_documentacao_lista_fontes_e_blocos():
    curadoria = (ROOT / 'disciplinas/eletronica/CURADORIA.md').read_text(encoding='utf-8')
    assert [k for k in CATALOGO if f'`{k}`' not in curadoria] == []
    assert [k for k in ITENS if f'`{k}`' not in curadoria] == []
