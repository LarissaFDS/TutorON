"""Acervo de Física 2 e conferência das resoluções.

Os blocos afirmam valores numéricos (forças de equilíbrio, pressões, períodos, entropias) e fórmulas
corrigidas das anotações da turma. Aqui as contas são refeitas em SI e as fórmulas conferidas com SymPy.
"""
import json
import math
import re
import shutil
import subprocess

import pytest
import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search, tokens

FIS2 = disciplinas.obter('fis2')
FONTES = read_json(ROOT / 'disciplinas/fis2/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {i['id']: i for i in read_json(FIS2.itens)}
G, g = 6.67e-11, 9.8


def buscar(pergunta, d=FIS2):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return ITENS[ident]['texto']


# ---------------------------------------------------------------- cadastro e acervo

def test_fis2_cadastrada_com_acervo_proprio():
    assert FIS2.nome == 'Física 2' and FIS2.itens.exists() and FIS2.indice.exists() and not FIS2.livro_supabase
    assert FIS2.situacao == 'beta' and not FIS2.em_validacao and 'não foi validado pelo professor' in FIS2.aviso
    outros = [disciplinas.obter(i) for i in ('paa', 'sd', 'oac')]
    ids = {c['id'] for c in read_json(FIS2.indice)['chunks']}
    for d in outros:
        assert {d.itens, d.indice}.isdisjoint({FIS2.itens, FIS2.indice})
        assert ids.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    assert all(c['disciplina'] == 'fis2' for c in read_json(FIS2.indice)['chunks'])
    assert {i['assunto'] for i in ITENS.values()} == set(FIS2.assuntos)  # os nove capítulos têm material


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas fis2 --embeddings`."""
    gerados = disciplinas.registros(FIS2)
    assert gerados == read_json(FIS2.itens)
    assert {c['id'] for c in read_json(FIS2.indice)['chunks']} == {
        i['id'] for i in gerados if i['confiabilidade'] in ('media', 'alta')}


def test_blocos_cabem_no_trecho():
    for i in ITENS.values():
        assert len(i['texto']) <= 2200, i['id']  # backend/rag.py corta acima disso


def test_notas_da_ia_e_resolucoes_pendentes_ficam_fora_da_busca():
    na_busca = {c['id'] for c in read_json(FIS2.indice)['chunks']}
    notas = {i for i, x in ITENS.items() if x['natureza'] == 'nota_da_equipe_ia'}
    pendentes = {i for i, x in ITENS.items() if x.get('status_resolucao') == 'pendente_professor'}
    assert notas == {'fis2-nota-escolher-metodo', 'fis2-nota-processos-termodinamicos'}
    assert pendentes == {'fis2-lista-fluidos-q5', 'fis2-notion-q9-lista1'}
    assert na_busca.isdisjoint(notas | pendentes)
    assert all(ITENS[i]['confiabilidade'] == 'nao_verificada' for i in notas | pendentes)


def test_nenhum_bloco_aprovado_pelo_professor_ou_revisado_por_humano():
    for p in (ROOT / 'disciplinas/fis2/materiais').glob('*.md'):
        cab = p.read_text(encoding='utf-8').split('---')[1]
        assert 'revisao_humana: pendente' in cab and 'revisao_professor' not in cab, p.name


# ---------------------------------------------------------------- busca e notação

@pytest.mark.parametrize('pergunta, aceitos', [
    ('Por que um bloco de madeira flutua e uma pedra do mesmo volume afunda?', {'fis2-notion-fluidos-pascal-arquimedes'}),
    ('Como calcular o trabalho de um gás ideal numa expansão isotérmica?',
     {'fis2-notion-gas-ideal-cinetica', 'fis2-notion-primeira-lei', 'fis2-notion-entropia'}),
    ('Qual o período de um pêndulo simples de 1 m?', {'fis2-notion-pendulos'}),
    ('Quantos nós tem o terceiro harmônico de uma corda presa nas duas pontas?', {'fis2-notion-ondas-estacionarias'}),
    ('Como calcular a variação de entropia numa expansão livre?', {'fis2-notion-entropia'}),
    ('Qual a eficiência de Carnot entre 500 K e 300 K?', {'fis2-notion-maquinas-carnot'}),
    ('Como funciona o efeito Doppler?', {'fis2-notion-batimentos-doppler'}),
    ('Por que a temperatura precisa estar em kelvin na lei dos gases?', {'fis2-notion-gas-ideal-cinetica'}),
])
def test_pergunta_de_fisica_encontra_material_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize('variantes', [
    ('Por que p = p0 + \\rho g h?', 'Por que p = p0 + rô g h no fundo da piscina?', 'Por que p = p0 + ρgh?'),
    ('Quanto vale 1.01e5 Pa em torr?', 'Quanto vale 1 atm em torr?', 'Quanto vale 1,01×10^5 Pa em torr?'),
])
def test_variantes_de_notacao_chegam_ao_mesmo_bloco(variantes):
    assert {buscar(v)[0] for v in variantes} == {'fis2-notion-fluidos-hidrostatica'}


def test_letras_gregas_somem_no_tokenizador_e_os_blocos_trazem_o_nome():
    """Limitação conhecida: tokens() guarda só [a-z0-9]. Por isso os blocos escrevem rô/rho e ômega por extenso."""
    assert tokens('ρgh') == ['gh'] and tokens('ω = 2πf') == []
    assert 'rho' in tokens(texto('fis2-notion-fluidos-hidrostatica'))


def test_pergunta_fora_do_acervo_nao_inventa_material():
    assert buscar('Explique a heurística de Dijkstra para grafos esparsos') == []


def test_vocabulario_comum_fica_na_disciplina_escolhida():
    for pergunta in ('Como somar vetores?', 'Qual a frequência de ressonância?', 'Como calcular a integral?', 'O que é fluxo?'):
        assert all(i.startswith('fis2-') for i in buscar(pergunta))
        for d in ('paa', 'sd', 'oac'):
            assert not any(i.startswith('fis2-') for i in buscar(pergunta, disciplinas.obter(d)))


# ---------------------------------------------------------------- resoluções: status explícito

def test_resolucoes_tem_status_e_dizem_no_texto():
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    listas = [i for i in ITENS.values() if i.get('resolucao') or 'status_resolucao' in i]
    resolvidas = [i for i in ITENS.values() if 'status_resolucao' in i]
    assert len(resolvidas) == 13
    for i in resolvidas:
        assert f"Status da resolução: {rotulo[i['status_resolucao']]}" in i['texto'], i['id']
        assert 'gabarito oficial' not in i['texto'].lower()
    corrigidas = {i['id'] for i in resolvidas if i['status_resolucao'] == 'corrigida'}
    assert corrigidas == {'fis2-lista-fluidos-q1', 'fis2-lista-fluidos-q4', 'fis2-lista-gravitacao-q1-q5'}
    assert all('Divergência' in texto(i) for i in corrigidas)  # diz o que mudou em relação à resolução da turma
    assert listas


def test_anotacoes_corrigidas_dizem_o_que_mudou():
    t = {i: x['texto'] for i, x in ITENS.items() if i.startswith('fis2-notion-')}
    assert '760 torr' in t['fis2-notion-fluidos-hidrostatica'] and 'manométrica' in t['fis2-notion-fluidos-hidrostatica']
    assert 'peso do fluido deslocado' in t['fis2-notion-fluidos-pascal-arquimedes']
    assert 'estacionário' in t['fis2-notion-fluidos-escoamento'] and '"sem torque" está errada' in t['fis2-notion-fluidos-escoamento']
    assert '2ea' in t['fis2-notion-gravitacao-energia-kepler']
    assert r'6{,}02\times10^{23}' in t['fis2-notion-temperatura-calor']
    assert r'\tfrac12 kT' in t['fis2-notion-calores-especificos-adiabatica']
    assert '**permanece constante** num processo reversível' in t['fis2-notion-entropia']


# ---------------------------------------------------------------- fórmulas conferidas com SymPy

def test_formulas_corrigidas_das_anotacoes():
    G_, M, m, d, L, x, r, R = sp.symbols('G M m d L x r R', positive=True)
    # barra alinhada: integral de G m (M/L) dx / x² de d a d+L
    assert sp.simplify(sp.integrate(G_ * m * M / L / x ** 2, (x, d, d + L)) - G_ * M * m / (d * (d + L))) == 0
    # dentro da esfera uniforme: F = G M m r / R³
    assert sp.simplify(G_ * (M * r ** 3 / R ** 3) * m / r ** 2 - G_ * M * m * r / R ** 3) == 0
    # órbita circular: E = -K
    K, U = G_ * M * m / (2 * r), -G_ * M * m / r
    assert sp.simplify(K + U + K) == 0
    # MHS: a = -ω² x
    t, w, xm, phi = sp.symbols('t omega x_m phi', real=True)
    xt = xm * sp.cos(w * t + phi)
    assert sp.simplify(sp.diff(xt, t, 2) + w ** 2 * xt) == 0
    # barra pendurada pela ponta: I = mL²/3 e g = 8π²L/(3T²)
    Ip = m * L ** 2 / 12 + m * (L / 2) ** 2
    assert sp.simplify(Ip - m * L ** 2 / 3) == 0
    T, gg = sp.symbols('T g', positive=True)
    assert sp.solve(sp.Eq(T, 2 * sp.pi * sp.sqrt(Ip / (m * gg * L / 2))), gg) == [8 * sp.pi ** 2 * L / (3 * T ** 2)]
    # isotérmica: W = ∫ nRT/V dV = nRT ln(Vf/Vi)
    n, Rg, Tk, V, Vi, Vf = sp.symbols('n R T V V_i V_f', positive=True)
    assert sp.simplify(sp.integrate(n * Rg * Tk / V, (V, Vi, Vf)) - n * Rg * Tk * sp.log(Vf / Vi)) == 0


def test_exemplos_numericos_das_anotacoes():
    assert 101325 / 133.322 == pytest.approx(760, abs=0.1)
    assert 2 * math.pi * math.sqrt(1 / g) == pytest.approx(2.0, abs=0.01)  # pêndulo de 1 m
    assert 0.60 * 1000 == 600
    assert 8.31 * math.log(2) == pytest.approx(5.76, abs=0.01)  # expansão livre, 1 mol dobrando o volume
    assert 1 - 300 / 500 == pytest.approx(0.40)
    assert round(500 * 353 / 343, 1) == 514.6 and round(500 * 343 / 333, 1) == 515.0  # Doppler
    assert 2.00 * 8.31 * 300 * math.log(2) == pytest.approx(3.46e3, abs=5)
    assert math.sqrt(2 * G * 5.98e24 / 6.37e6) == pytest.approx(11.2e3, rel=0.01)
    n = 3  # terceiro harmônico: n ventres e n + 1 nós
    nos = [k / n for k in range(n + 1)]
    assert len(nos) == 4 and len(nos) - 1 == n


# ---------------------------------------------------------------- resoluções das listas

def test_lista_equilibrio():
    P = 1360 * g
    fd = P * 1.27 / 3.05
    assert (round(fd / 2), round((P - fd) / 2)) == (2775, 3889)
    T = 0.85 * g * math.hypot(0.080, 0.042) / 0.080
    assert (round(T, 1), round(0.85 * g * 0.042 / 0.080, 1)) == (9.4, 4.4)
    td = (784 * 1.5 + 588 * 2.5) / 5.0
    assert (round(784 + 588 - td, 1), round(td, 1)) == (842.8, 529.2)
    h = math.sqrt(5.0 ** 2 - 2.5 ** 2)
    fj = (98 * 1.25 + 735 * 3.0 * 0.5) / h
    assert round(fj) == 283 and round(math.hypot(fj, 833)) == 880 and round(math.degrees(math.atan2(833, fj))) == 71
    assert round(0.010 * 0.335 / 0.045, 4) == 0.0744


def test_lista_fluidos():
    assert round(0.08 / 1.08, 3) == 0.074  # 7,4 %, não 0,074 %
    assert 1.0e5 - 480 / 77 == pytest.approx(99993.77, abs=0.01)
    assert round((1.30 + 0.25 + 0.32) * g, 1) == 18.3
    torr = 133.322
    dp = 1.06e3 * g * 2.0 / torr
    assert (round(250 - dp), round(250 + dp, -1), round(2 * dp, -1)) == (94, 410, 310)
    assert round(1300 * 4e-4 * g * (1.560 - 0.854) ** 2 / 4, 3) == 0.635
    assert round(20000 * (3.80 / 53.0) ** 2) == 103
    assert round(3e4 * 0.05 / (18 * g), 1) == 8.5
    assert round(0.5 * (2.0 * g / 5.0) * 0.2 ** 2, 4) == 0.0784
    m = 800 * 0.5 * 4 / 3 * math.pi * 0.090 ** 3
    assert round(m, 2) == 1.22 and round(m / (4 / 3 * math.pi * (0.090 ** 3 - 0.080 ** 3)), -1) == 1340


def test_lista_gravitacao():
    assert round(math.sqrt(6.6e-11 * 5.2 * 2.4 / 2.3e-12), 2) == 18.92  # a resolução da turma
    assert round(math.sqrt(G * 5.2 * 2.4 / 2.3e-12), 1) == 19.0
    assert math.sqrt(G * 5.98e24 / 4.9) - 6.37e6 == pytest.approx(2.65e6, rel=0.005)


def test_lista_oscilacoes():
    assert (2 * 0.25, 1 / 0.5, 36 / 2) == (0.5, 2.0, 18)
    k = 362.5 * (2 * math.pi * 3.00) ** 2
    assert k == pytest.approx(1.29e5, rel=2e-3) and math.sqrt(k / 453.75) / (2 * math.pi) == pytest.approx(2.68, abs=0.005)
    w = math.sqrt(100 / 2.00)
    xm = math.hypot(0.129, 3.415 / w)
    theta = math.atan2(-3.415 / (w * xm), 0.129 / xm)
    phi = theta - w * 1.0
    assert round(xm, 3) == 0.500 and round(phi, 2) == -8.38
    assert round(xm * math.cos(phi), 3) == -0.251 and round(-w * xm * math.sin(phi), 2) == 3.06
    w = math.sqrt(123 / 0.100)
    assert round(w / (2 * math.pi), 2) == 5.58 and round(400 / w ** 2, 3) == 0.325
    assert round(math.hypot(0.100, 13.6 / w), 3) == 0.400


# ---------------------------------------------------------------- LaTeX renderiza no KaTeX do site

FORMULA = re.compile(r'\$\$(.+?)\$\$|\$(.+?)\$', re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in ITENS.values():
        assert i['texto'].count('$') % 2 == 0, i['id']


@pytest.mark.skipif(not shutil.which('node'), reason='node indisponível')
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for i in ITENS.values() for a, b in FORMULA.findall(i['texto'])]
    assert len(formulas) > 100
    katex = (ROOT / 'backend/web/vendor/katex/katex.min.js').as_posix()
    script = (f"const k=require({json.dumps(katex)});const fs=require('fs');"
              "const erros=[];for(const f of JSON.parse(fs.readFileSync(0,'utf8'))){"
              "try{k.renderToString(f,{throwOnError:true})}catch(e){erros.push(f+' :: '+e.message)}}"
              "console.log(JSON.stringify(erros))")
    r = subprocess.run(['node', '-e', script], input=json.dumps(formulas), capture_output=True, text=True,
                       encoding='utf-8', check=True)
    assert json.loads(r.stdout) == []


# ---------------------------------------------------------------- catálogo e restrições

def test_catalogo_completo_e_coerente():
    obrigatorios = {'id', 'nome', 'autoria', 'url', 'idioma', 'formato', 'isa', 'topicos', 'licenca', 'acesso',
                    'prioridade', 'uso', 'justificativa'}
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f['id']
        assert f['prioridade'] in ('alta', 'media', 'referencia')
        assert f['uso'] in ('acervo', 'citada', 'referencia', 'candidato', 'indisponivel')
        assert set(f['topicos']) <= set(FIS2.assuntos), f['id']
    assert {x for i in ITENS.values() for x in i['fontes_catalogo']} <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f['uso'] == 'acervo'} == {
        x for i in ITENS.values() if i['natureza'] == 'material_da_disciplina' for x in i['fontes_catalogo']}


def test_livro_e_imagens_fora_do_repositorio():
    for ident in ('halliday-fundamentos-vol2', 'openstax-university-physics-v1', 'openstax-university-physics-v2'):
        assert CATALOGO[ident]['uso'] == 'referencia'
    arquivos = [p for p in (ROOT / 'disciplinas/fis2').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.docx', '.pptx', '.gif')]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (ROOT / 'disciplinas/fis2/CURADORIA.md').read_text(encoding='utf-8')
    assert [i for i in CATALOGO if f'`{i}`' not in curadoria] == []
    assert [i for i in ITENS if f'`{i}`' not in curadoria] == []
    assert '`fis2`' in (ROOT / 'docs/DISCIPLINAS.md').read_text(encoding='utf-8')
