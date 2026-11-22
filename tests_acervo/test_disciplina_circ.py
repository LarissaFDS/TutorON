"""Acervo de Circuitos Elétricos e conferência das resoluções.

Cada circuito descrito num bloco é remontado aqui, a partir da descrição em palavras do próprio bloco, e
resolvido com análise nodal modificada exata (SymPy, `circ_mna`): tensões, Thévenin pela fonte de teste e
balanço de potências (a soma das potências absorvidas tem de dar zero). As respostas de segunda ordem são
refeitas com `dsolve`. Os erros encontrados nas anotações do aluno são conferidos como erros.
"""
import json
import re
import shutil
import subprocess

import pytest
import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search
from tests_acervo.circ_mna import I, R, V, i, resolver, thevenin, v

CIRC = disciplinas.obter('circ')
FONTES = read_json(ROOT / 'disciplinas/circ/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {x['id']: x for x in read_json(CIRC.itens)}
NA_BUSCA = {c['id'] for c in read_json(CIRC.indice)['chunks']}
VETORES = json.loads((ROOT / 'eval/relevancia-vetores.json').read_text(encoding='utf-8'))
t = sp.Symbol('t', nonnegative=True)


def texto(ident):
    return ITENS[ident]['texto']


def buscar(pergunta, d=CIRC):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def hibrida(pergunta, d=CIRC):
    """A mesma busca do backend (corte e penalidade de hub), com o embedding real gravado da pergunta."""
    return [r['id'] for r in search(pergunta, k=4, vector=VETORES[pergunta], min_similarity=0.45, hub_penalty=True,
                                    itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo

def test_circ_cadastrada_com_acervo_proprio_e_a_mesma_ia():
    assert CIRC.nome == 'Circuitos Elétricos' and CIRC.itens.exists() and CIRC.indice.exists()
    assert not CIRC.livro_supabase and CIRC.rigor.strip() == (ROOT / 'disciplinas/circ/rigor.md').read_text(encoding='utf-8').strip()
    assert all(c['disciplina'] == 'circ' for c in read_json(CIRC.indice)['chunks'])
    for outra in ('paa', 'sd', 'oac', 'calc3', 'fis2', 'ed', 'bd', 'prob'):
        d = disciplinas.obter(outra)
        assert NA_BUSCA.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    bruto = [d for d in read_json(ROOT / 'disciplinas/disciplinas.json')['disciplinas'] if d['id'] == 'circ'][0]
    assert not {'modelo', 'model', 'provedor', 'endpoint', 'prompt', 'chave'} & set(bruto)
    assert read_json(CIRC.indice)['embedding_model'] == read_json(disciplinas.obter('bd').indice)['embedding_model']


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas circ --embeddings`."""
    gerados = disciplinas.registros(CIRC)
    assert gerados == read_json(CIRC.itens)
    assert NA_BUSCA == {x['id'] for x in gerados if x['confiabilidade'] in ('media', 'alta')}
    assert read_json(CIRC.indice)['modo'] == 'hibrido'


def test_blocos_cabem_no_trecho_e_formulas_fecham():
    for x in ITENS.values():
        assert len(x['texto']) <= 2200, x['id']
        sem_destaque = x['texto'].replace('$$', '')
        assert x['texto'].count('$$') % 2 == 0 and sem_destaque.count('$') % 2 == 0, x['id']
        assert '**Verificação:**' in x['texto'], x['id']


def test_notas_de_ia_sem_revisao_ficam_fora_da_busca():
    notas = [x for x in ITENS.values() if x['natureza'] == 'nota_da_equipe_ia']
    assert len(notas) == 3
    assert all(x['status_curadoria'] == 'candidato' and x['revisao_humana'] == 'pendente' for x in notas)
    assert {x['id'] for x in notas}.isdisjoint(NA_BUSCA)
    assert not any(x.get('revisao_humana') == 'feita' or x.get('revisao_professor') for x in ITENS.values())


def test_topicos_com_anotacoes_tem_bloco_na_busca():
    """Critério de liberação: todo tópico "Sim" no mapeamento (01 a 05 e 08) tem bloco na busca."""
    na_busca = {ITENS[x]['assunto'] for x in NA_BUSCA}
    sim = {'circ-01-grandezas-potencia', 'circ-02-kirchhoff-nodal-malhas', 'circ-03-superposicao-transformacao',
           'circ-04-thevenin-norton', 'circ-05-maxima-transferencia', 'circ-06-amp-op', 'circ-07-primeira-ordem',
           'circ-08-segunda-ordem'}
    assert na_busca == sim
    assert set(CIRC.assuntos) - sim == {'circ-09-fasores'}


# ---------------------------------------------------------------- status das resoluções

def test_resolucoes_tem_status_e_dizem_no_texto():
    turma = [x for x in ITENS.values() if x['natureza'] == 'material_da_disciplina' and x['id'].startswith('circ-anot-')]
    assert len(turma) == 23
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    for x in turma:
        assert f"Status da resolução: {rotulo[x['status_resolucao']]}" in x['texto'], x['id']
        assert x['verificacao'] == 'conferida_por_codigo' and x['revisao_humana'] == 'pendente'
    corrigidas = {x['id'] for x in turma if x['status_resolucao'] == 'corrigida'}
    assert corrigidas == {'circ-anot-grandezas-ohm', 'circ-anot-superposicao-superno-ab1-q3', 'circ-anot-thevenin-ex2',
                          'circ-anot-segunda-ordem-conceitos', 'circ-anot-rlc-revisao-q1'}
    assert all('Correç' in texto(c) for c in corrigidas)


# ---------------------------------------------------------------- circuitos remontados (MNA exata)

def test_mna_balanco_de_potencias_fecha():
    els = [V('E', 'n', '0', 24), R('R2', 'n', 'a', 2), R('R8', 'a', '0', 8), I('F', 'a', '0', 4)]
    _, _, pot = resolver(els)
    assert sum(pot.values()) == 0


def test_thevenin_fonte_dependente_3ix():
    ix = i('R8')
    els = [V('E', 'n', '0', 24), R('R2', 'n', 'a', 2), I('D', 'a', 'n', 3 * ix), I('F', 'a', '0', 4), R('R8', 'a', '0', 8)]
    assert thevenin(els, 'a', '0') == (8, 1)
    _, _, pot = resolver(els)
    assert sum(pot.values()) == 0
    # desligar a dependente daria 2 ∥ 8 = 1,6 Ω: o erro típico citado no bloco
    assert thevenin([e for e in els if e.nome != 'D'], 'a', '0')[1] == sp.Rational(8, 5)
    assert 'V_{Th} = 8' in texto('circ-anot-thevenin-fonte-dependente') and 'R_{Th} = 1' in texto('circ-anot-thevenin-fonte-dependente')


def test_thevenin_prova_antiga_6i0():
    els = [I('S', '0', 'n1', 2), R('R4', 'n1', '0', 4), V('D', 'n1', 'm', 6 * i('R4')), R('R8', 'm', 'a', 8)]
    assert thevenin(els, 'a', '0') == (-4, 6)


def test_thevenin_160i_delta():
    els = [I('S', '0', 'n', 4), R('R60', 'n', '0', 60), R('R20', 'n', 'q', 20), V('D', 'q', 'a', 160 * i('R40')),
           R('R80', 'a', '0', 80), R('R40', 'a', '0', 40)]
    assert thevenin(els, 'a', '0') == (30, 10)


def test_maxima_transferencia_ab1_q5():
    els = [V('E', 's', '0', 18), R('R6', 's', 'm', 6), R('R3', 'm', '0', 3), R('R2', 'm', 'a', 2),
           I('D', 'a', 'm', v('m') / 4)]
    vth, rth = thevenin(els, 'a', '0')
    assert (vth, rth) == (3, 3) and vth ** 2 / (4 * rth) == sp.Rational(3, 4)
    RL = sp.Symbol('RL', positive=True)
    p = RL * (vth / (rth + RL)) ** 2
    assert sp.solve(sp.diff(p, RL), RL) == [rth]


def test_maxima_transferencia_vphi():
    vphi = v('m') - v('k')
    els = [V('E', 'L', '0', 100), V('D', 'p', 'L', vphi), R('Rp', 'p', 'a', 4), R('R1', 'L', 'm', 4), R('R2', 'm', 'a', 4),
           R('R3', 'm', 'k', 4), V('E2', 'k', '0', 20)]
    vth, rth = thevenin(els, 'a', '0')
    assert (vth, rth) == (120, 3) and vth ** 2 / (4 * rth) == 1200


def test_maxima_transferencia_y_delta():
    els = [V('E1', 'a', 'x', 60), R('Ra', 'x', '0', 20), R('Ra2', 'a', '2', 20), R('R2', '2', 'y', 20), V('E2', 'y', '0', 100),
           I('F', '2', 'b', 1), R('R40a', '2', 'b', 40), R('R40b', '2', 'b', 40), R('Rb', 'b', '0', 20)]
    assert thevenin(els, 'a', 'b') == (20, 20)
    assert sp.Rational(3 * 400, 20) == 60  # R_Δ da estrela de três braços de 20 Ω


# ---------------------------------------------------------------- segunda ordem (dsolve)

def _resolver(eq, x, ci):
    return sp.simplify(sp.dsolve(eq, x, ics=ci).rhs)


def test_rlc_critico_ab2_q1():
    R_, L_, C_ = 5, sp.Rational(1, 8), sp.Rational(1, 50)
    alfa, w0 = sp.Rational(R_) / (2 * L_), 1 / sp.sqrt(L_ * C_)
    assert alfa == w0 == 20
    x = sp.Function('x')
    sol = _resolver(x(t).diff(t, 2) + 40 * x(t).diff(t) + 400 * x(t), x(t), {x(0): 0, x(t).diff(t).subs(t, 0): 16})
    assert sp.simplify(sol - 16 * t * sp.exp(-20 * t)) == 0


def test_rlc_superamortecido_ab2_q2():
    x = sp.Function('x')
    sol = _resolver(x(t).diff(t, 2) + 6 * x(t).diff(t) + 8 * x(t) - 16, x(t), {x(0): 1, x(t).diff(t).subs(t, 0): 0})
    assert sp.simplify(sol - (2 - 2 * sp.exp(-2 * t) + sp.exp(-4 * t))) == 0
    assert 3 > sp.sqrt(8)  # α > ω0


def test_rlc_critico_revisao_q1_capacitor_apos_chave():
    """Forma (A1 + A2 t)e^{-20t} com i(0) = 0: só sobra o termo em t."""
    x = sp.Function('x')
    A2 = sp.Rational(-48, 5)
    sol = _resolver(x(t).diff(t, 2) + 40 * x(t).diff(t) + 400 * x(t), x(t), {x(0): 0, x(t).diff(t).subs(t, 0): A2})
    assert sp.simplify(sol - A2 * t * sp.exp(-20 * t)) == 0
    assert 'v_C(0^-) = 24' in texto('circ-anot-rlc-revisao-q1') and 'chave abre' in texto('circ-anot-rlc-revisao-q1')


def test_rlc_subamortecido_revisao_q2():
    x = sp.Function('x')
    sol = _resolver(x(t).diff(t, 2) + 6 * x(t).diff(t) + 25 * x(t) + 300, x(t), {x(0): -8, x(t).diff(t).subs(t, 0): 0})
    esperado = sp.exp(-3 * t) * (4 * sp.cos(4 * t) + 3 * sp.sin(4 * t)) - 12
    assert sp.simplify(sol - esperado) == 0


# ---------------------------------------------------------------- erros das anotações (conferidos como erros)

def test_erro_solucao_particular_chamada_de_homogenea():
    """Anotação: r = a ± bj ⇒ y_p = e^{at}(A cos bt + B sen bt). Isso é a homogênea: anula o lado esquerdo."""
    a, b, A, B = sp.symbols('a b A B', real=True)
    y = sp.exp(a * t) * (A * sp.cos(b * t) + B * sp.sin(b * t))
    homog = y.diff(t, 2) - 2 * a * y.diff(t) + (a ** 2 + b ** 2) * y
    assert sp.simplify(homog) == 0
    assert 'homogênea' in texto('circ-anot-segunda-ordem-conceitos')


def test_erro_rth_40_ohms_no_exercicio_2():
    assert '25' in texto('circ-anot-thevenin-ex2') and '40' in texto('circ-anot-thevenin-ex2')
    assert not re.search(r'R_\{Th\}\s*=\s*40\s*\\?\s*Ω\.?\s*$', texto('circ-anot-thevenin-ex2'), re.M)


def test_erro_superposicao_com_denominador_errado():
    assert sp.Rational(-32, 6) - 16 == sp.Rational(-128, 6)  # a conta riscada das anotações
    assert sp.Rational(-32, 3) - 16 == sp.Rational(-80, 3)  # 4 A dá −32/3 V; com o resto, −80/3 V
    assert r'v_x = 0 - v_D = -\tfrac{80}{3}' in texto('circ-anot-superposicao-superno-ab1-q3')


# ---------------------------------------------------------------- busca

EXEMPLOS = [
    ('Como calcular o equivalente de Thévenin com uma fonte dependente?',
     {'circ-anot-thevenin-fonte-dependente', 'circ-anot-thevenin-prova-antiga', 'circ-anot-thevenin-dependentes-ex6-ex11'}),
    ('Qual a condição para máxima transferência de potência?', {'circ-anot-maxima-transferencia'}),
    ('Como resolver um circuito RLC série subamortecido?', {'circ-anot-rlc-revisao-q2', 'circ-anot-segunda-ordem-conceitos'}),
    ('Quando uso um supernó na análise nodal?', {'circ-anot-superposicao-superno-ab1-q3'}),
    ('Como achar as condições iniciais do capacitor depois que a chave abre?',
     {'circ-anot-rlc-revisao-q1', 'circ-anot-segunda-ordem-conceitos', 'circ-anot-rlc-ab2-q2'}),
]


def test_exemplos_do_cadastro_sao_os_testados():
    assert list(CIRC.exemplos) == [p for p, _ in EXEMPLOS]


@pytest.mark.parametrize('pergunta, aceitos', EXEMPLOS)
def test_perguntas_de_exemplo_trazem_o_bloco_certo(pergunta, aceitos):
    assert aceitos & set(hibrida(pergunta))


@pytest.mark.parametrize('latex, simples, aceitos', [
    (r'Como calcular $R_{Th} = V_T/I_T$ quando há fonte dependente?',
     'Como calcular o equivalente de Thévenin com uma fonte dependente?', EXEMPLOS[0][1]),
    (r'Por que $P_{max} = V_{Th}^2/(4R_{Th})$ quando $R_L = R_{Th}$?',
     'Qual a condição para máxima transferência de potência?', EXEMPLOS[1][1]),
    (r"Resolva $v'' + 6v' + 25v = 0$ num RLC com $\alpha < \omega_0$",
     'Como resolver um circuito RLC série subamortecido?', EXEMPLOS[2][1]),
])
def test_latex_e_texto_simples_trazem_o_mesmo_bloco(latex, simples, aceitos):
    assert aceitos & set(hibrida(latex)) and aceitos & set(hibrida(simples))


@pytest.mark.parametrize('pergunta', ['Como simplificar uma função com mapa de Karnaugh?', 'Como fazer um LEFT JOIN em SQL?',
                                      'Me conte uma piada', 'Como montar um contador síncrono com flip-flops?'])
def test_pergunta_de_outra_area_nao_traz_material(pergunta):
    assert hibrida(pergunta) == []


def test_isolamento_com_as_disciplinas_de_fronteira():
    sd, fis2 = disciplinas.obter('sd'), disciplinas.obter('fis2')
    assert hibrida('Como calcular o equivalente de Thévenin com uma fonte dependente?', sd) == []
    for p in ('Como simplificar uma função com mapa de Karnaugh?', 'Qual o período de um pêndulo simples?',
              'Como montar um contador síncrono com flip-flops?'):
        assert all(x.startswith('circ-') for x in buscar(p))
        assert not any(x.startswith('circ-') for x in buscar(p, sd) + buscar(p, fis2))
    for p, _ in EXEMPLOS:
        assert not any(x.startswith('circ-') for x in buscar(p, sd) + buscar(p, fis2))


# ---------------------------------------------------------------- KaTeX, catálogo e restrições

FORMULA = re.compile(r'\$\$(.+?)\$\$|\$(.+?)\$', re.S)


@pytest.mark.skipif(not shutil.which('node'), reason='node indisponível')
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for x in ITENS.values() for a, b in FORMULA.findall(x['texto'])]
    assert len(formulas) > 100
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
        assert set(f['topicos']) <= set(CIRC.assuntos), f['id']
    assert {x for i_ in ITENS.values() for x in i_['fontes_catalogo']} - {'nenhuma'} <= set(CATALOGO)
    assert {k for k, f in CATALOGO.items() if f['uso'] == 'acervo'} == {'ufal-circ-anotacoes-otavio-2026-1',
                                                                         'ufal-circ-davi-2017'}
    aut = CATALOGO['ufal-circ-anotacoes-otavio-2026-1']['autorizacao_transcricao']
    assert aut['data'] == '2026-11-18' and aut['aprovacao_professor'] == 'não declarada'
    assert CATALOGO['nilsson-riedel-circuitos']['uso'] == 'referencia'


def test_anotacoes_e_imagens_fora_do_repositorio():
    arquivos = [p for p in (ROOT / 'disciplinas/circ').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.webp', '.docx', '.pptx')]
    for x in ITENS.values():
        if x['natureza'] == 'material_da_disciplina' and x['id'].startswith('circ-anot-'):
            assert x['publicacao_transcricao'].startswith('autorizada pelo autor') and 'fora do repositório' in x['licenca']
    rastreados = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout
    assert not [l for l in rastreados.splitlines() if re.search(r'_26\d{4}_\d{6}\.pdf$', l)]


def test_documentacao_lista_fontes_e_blocos():
    curadoria = (ROOT / 'disciplinas/circ/CURADORIA.md').read_text(encoding='utf-8')
    assert [k for k in CATALOGO if f'`{k}`' not in curadoria] == []
    assert [k for k in ITENS if f'`{k}`' not in curadoria] == []
