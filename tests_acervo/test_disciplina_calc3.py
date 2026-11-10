"""Acervo de Cálculo 3 e conferência das resoluções.

As resoluções afirmam valores (ângulos, pontos, limites, constantes de EDPs). Aqui cada conta é
refeita com SymPy e, quando há equação a resolver, conferida também numericamente.
"""
import dataclasses
import math
import shutil

import pytest
import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search, tokens

CALC3 = disciplinas.obter('calc3')
FONTES = read_json(ROOT / 'disciplinas/calc3/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {i['id']: i for i in read_json(CALC3.itens)}
x, y, t, h, th = sp.symbols('x y t h theta', real=True)


def buscar(pergunta, d=CALC3):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


@pytest.fixture(scope='module')
def notas_aprovadas(tmp_path_factory):
    """Cópia do acervo com as notas da equipe promovidas: testa a busca que elas terão depois da revisão."""
    raiz = tmp_path_factory.mktemp('calc3')
    shutil.copytree(CALC3.materiais, raiz / 'm')
    for p in (raiz / 'm').glob('n*.md'):
        p.write_text(p.read_text(encoding='utf-8').replace('curadoria: candidato', 'curadoria: aprovado'),
                     encoding='utf-8')
    d = dataclasses.replace(CALC3, materiais=raiz / 'm', itens=raiz / 'itens.json', indice=raiz / 'indice.json')
    disciplinas.construir(d, root=raiz)
    return d


# ---------------------------------------------------------------- cadastro e acervo

def test_calc3_cadastrada_com_acervo_proprio():
    assert CALC3.nome == 'Cálculo 3' and CALC3.itens.exists() and CALC3.indice.exists()
    assert CALC3.situacao == 'beta' and not CALC3.em_validacao and 'não foi validado pelo professor' in CALC3.aviso and not CALC3.livro_supabase
    outros = [disciplinas.obter(i) for i in ('paa', 'sd', 'oac')]
    ids = {c['id'] for c in read_json(CALC3.indice)['chunks']}
    for d in outros:
        assert ids.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    assert all(c['disciplina'] == 'calc3' for c in read_json(CALC3.indice)['chunks'])


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas calc3 --embeddings`."""
    gerados = disciplinas.registros(CALC3)
    assert gerados == read_json(CALC3.itens)
    assert {c['id'] for c in read_json(CALC3.indice)['chunks']} == {
        i['id'] for i in gerados if i['confiabilidade'] in ('media', 'alta')}


def test_blocos_cabem_no_trecho_e_formulas_fecham():
    for i in ITENS.values():
        assert len(i['texto']) <= 2200, i['id']
        sem_destaque = i['texto'].replace('$$', '')
        assert i['texto'].count('$$') % 2 == 0 and sem_destaque.count('$') % 2 == 0, i['id']  # KaTeX inteiro


def test_notas_da_equipe_sao_candidatas_e_ficam_fora_da_busca():
    notas = [i for i in ITENS.values() if i['natureza'] == 'nota_da_equipe_ia']
    assert len(notas) == 5 and all(i['status_curadoria'] == 'candidato' for i in notas)
    assert {i['id'] for i in notas}.isdisjoint({c['id'] for c in read_json(CALC3.indice)['chunks']})


# ---------------------------------------------------------------- busca

def test_latex_vira_os_mesmos_tokens_que_unicode():
    assert set(tokens('f(x,y) = x²y')) == set(tokens('$f(x,y)=x^2y$')) == set(tokens('f(x,y)=x^{2}y'))
    assert tokens(r'$\mathbf{r}(t) = \langle t, t^2 \rangle$') == ['t2']
    assert 'lim' in tokens(r'$\lim_{(x,y)\to(0,0)}$') and 'nabla' in tokens(r'$\nabla f$')


@pytest.mark.parametrize('pergunta, esperado', [
    ('Onde a cardioide r = 1 + sen θ tem tangente horizontal?', 'calc3-ab1-2024-q3-cardioide'),
    ('Como calcular o comprimento de arco de uma curva paramétrica?', 'calc3-resumo-comprimento-de-arco'),
    ('Projétil com x = t³/4 + 2t: qual a altura máxima e o ângulo de lançamento?', 'calc3-ab1-2024-q1-projetil'),
    ('Quando duas partículas colidem numa elipse e numa circunferência?', 'calc3-ab1-2024-q2-colisao'),
    ('O limite de x³y/(x⁶ + 2y²) na origem existe?', 'calc3-reav-2024-q1q2-limite-parciais'),
    ('Para que valores e^(Ax+Bt) satisfaz a equação do calor?', 'calc3-ab2-2024-q3q4-edp'),
    ('Como achar o vetor normal N e o binormal B?', 'calc3-notion-curvatura-tnb'),
    ('O que são curvas de nível de uma função de duas variáveis?', 'calc3-notion-funcoes-varias-variaveis'),
])
def test_pergunta_de_calc3_encontra_material_da_turma(pergunta, esperado):
    assert buscar(pergunta)[0] == esperado


@pytest.mark.parametrize('latex, texto, esperado', [
    (r'Qual a curvatura de $\mathbf r(t)=\langle t,t^2,t^3\rangle$ em t=0?',
     'Qual a curvatura de r(t) = (t, t², t³) em t = 0?', 'calc3-nota-curvatura-exemplo'),
    (r'Calcule $D_{\mathbf u}f(1,2)$ para $f(x,y)=x^2y$ na direção $\langle 3,4\rangle$',
     'derivada direcional de f(x,y) = x²y em (1,2) na direção (3,4)', 'calc3-nota-gradiente-derivada-direcional'),
    (r'Equação do plano pelos pontos $(1,0,0)$, $(0,2,0)$, $(0,0,3)$',
     'equação do plano que passa por (1,0,0), (0,2,0) e (0,0,3)', 'calc3-nota-plano-tres-pontos'),
])
def test_latex_e_texto_simples_trazem_o_mesmo_bloco(notas_aprovadas, latex, texto, esperado):
    assert buscar(latex, notas_aprovadas)[0] == buscar(texto, notas_aprovadas)[0] == esperado


def test_limite_xy_sobre_x2_y2_nas_duas_notacoes(notas_aprovadas):
    """Em LaTeX a AB2 Q1 (xy/√(x²+y²)) vem antes; a nota do limite que não existe vem logo atrás."""
    for p in (r'O limite $\lim_{(x,y)\to(0,0)} \frac{xy}{x^2+y^2}$ existe?',
              'o limite de xy/(x²+y²) quando (x,y) tende a (0,0) existe?'):
        assert 'calc3-nota-limite-xy-sobre-x2-y2' in buscar(p, notas_aprovadas)[:2]


def test_sem_nota_aprovada_gradiente_nao_traz_material():
    """Hoje a turma não tem material de gradiente: a busca não preenche o lugar com outro assunto."""
    assert not any('gradiente' in i for i in buscar('derivada direcional de f(x,y) = x²y em (1,2) na direção (3,4)'))


def test_vocabulario_comum_fica_na_disciplina_escolhida():
    oac = disciplinas.obter('oac')
    for pergunta in ('O que é um vetor?', 'Como calcular uma derivada?', 'O que é o vetor tangente?'):
        assert all(i.startswith('calc3-') for i in buscar(pergunta))
        assert all(i.startswith('oac-') for i in buscar(pergunta, oac))


@pytest.mark.parametrize('pergunta', ['Explique a heurística de Dijkstra para grafos esparsos',
                                      'Como funciona o pipeline de 5 estágios do RISC-V?',
                                      'Qual a capital da França?'])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


# ---------------------------------------------------------------- status das resoluções

def test_resolucoes_da_turma_tem_status_e_dizem_no_texto():
    turma = [i for i in ITENS.values() if i['natureza'] == 'material_da_disciplina']
    assert len(turma) == 16
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    for i in turma:
        assert f"Status da resolução: {rotulo[i['status_resolucao']]}" in i['texto'], i['id']
    provas = [i for i in turma if i['tipo'] == 'prova']
    assert len(provas) == 7 and all(i['status_resolucao'] == 'pendente_professor' for i in provas)
    corrigidas = {i['id'] for i in turma if i['status_resolucao'] == 'corrigida'}
    assert corrigidas == {'calc3-lista-limites-varias-variaveis', 'calc3-notion-parametrizacao', 'calc3-notion-curvatura-tnb'}
    assert all('correç' in ITENS[c]['texto'].lower() for c in corrigidas)


# ---------------------------------------------------------------- AB1

def test_ab1_q1_projetil():
    b = sp.symbols('b', positive=True)
    X, Y = t**3 / 4 + 2 * t, b * t - t**2
    v0 = sp.sqrt(sp.diff(X, t)**2 + sp.diff(Y, t)**2).subs(t, 0)
    assert sp.solve(sp.Eq(v0, 2 * sp.sqrt(101)), b) == [20]
    Y = Y.subs(b, 20)
    assert math.degrees(math.atan(20 / 2)) == pytest.approx(84.29, abs=0.01)
    assert sp.solve(sp.diff(Y, t), t) == [10] and Y.subs(t, 10) == 100
    assert sp.solve(Y, t) == [0, 20] and X.subs(t, 20) == 2040
    assert sp.solve(sp.diff(X, t), t) == []  # x' > 0: sem tangente vertical em t real


def test_ab1_q2_colisao():
    p1, p2 = (3 * sp.sin(t), 2 * sp.cos(t)), (-3 + sp.cos(t), 1 + sp.sin(t))
    assert sp.simplify(p1[0]**2 / 9 + p1[1]**2 / 4) == 1 and sp.simplify((p2[0] + 3)**2 + (p2[1] - 1)**2) == 1
    tc = 3 * sp.pi / 2
    assert (p1[0].subs(t, tc), p1[1].subs(t, tc)) == (-3, 0) == (p2[0].subs(t, tc), p2[1].subs(t, tc))
    perto = [k * 2 * math.pi / 20000 for k in range(20001)
             if math.dist((3 * math.sin(k * 2 * math.pi / 20000), 2 * math.cos(k * 2 * math.pi / 20000)),
                          (-3 + math.cos(k * 2 * math.pi / 20000), 1 + math.sin(k * 2 * math.pi / 20000))) < 1e-3]
    assert perto and all(abs(s - 3 * math.pi / 2) < 1e-3 for s in perto)  # única colisão


def test_ab1_q3_cardioide():
    r = 1 + sp.sin(th)
    X, Y = r * sp.cos(th), r * sp.sin(th)
    dX, dY = sp.diff(X, th), sp.diff(Y, th)
    assert sp.simplify(dY / dX).subs(th, sp.pi / 3).simplify() == -1
    for a, ponto in ((sp.pi / 2, (0, 2)), (7 * sp.pi / 6, (-sp.sqrt(3) / 4, -sp.Rational(1, 4))),
                     (11 * sp.pi / 6, (sp.sqrt(3) / 4, -sp.Rational(1, 4)))):
        assert sp.simplify(dY.subs(th, a)) == 0 and sp.simplify(dX.subs(th, a)) != 0
        assert (sp.simplify(X.subs(th, a)), sp.simplify(Y.subs(th, a))) == ponto
    assert dX.subs(th, 3 * sp.pi / 2) == 0 == dY.subs(th, 3 * sp.pi / 2)  # cúspide na origem


# ---------------------------------------------------------------- AB2, reavaliação e listas

def parcial_pela_definicao(f, v):
    return sp.limit(sp.simplify((f.subs(v, v + h) - f) / h), h, 0)


def test_ab2():
    m, a = sp.symbols('m alpha', real=True)
    f = x * y / sp.sqrt(x**2 + y**2)
    assert sp.limit(f.subs(y, m * x), x, 0, '+') == 0 and sp.limit(f.subs(y, a * x**2), x, 0, '+') == 0
    assert sp.simplify((sp.Abs(f) / sp.Abs(x)).subs({x: 3, y: 4})) <= 1  # confronto: |f| ≤ |x|
    assert parcial_pela_definicao(x / y, x) == 1 / y
    assert sp.simplify(parcial_pela_definicao(x / y, y) + x / y**2) == 0
    A, B, lam, de = sp.symbols('A B lambda delta')
    u = sp.exp(A * x + B * t)
    assert sp.solve(sp.simplify((sp.diff(u, t) - sp.diff(u, x, 2)) / u), B) == [A**2]
    g = sp.cos(lam * x) * sp.exp(de * y)
    assert set(sp.solve(sp.simplify((sp.diff(g, x, 2) + sp.diff(g, y, 2)) / g), de)) == {-lam, lam}


def test_reavaliacao():
    m = sp.symbols('m', real=True)
    f = x**3 * y / (x**6 + 2 * y**2)
    assert sp.limit(f.subs(y, m * x), x, 0) == 0 and sp.simplify(f.subs(y, x**3)) == sp.Rational(1, 3)
    assert sp.simplify(parcial_pela_definicao(x / (x + y**2), x) - y**2 / (x + y**2)**2) == 0
    assert sp.expand(parcial_pela_definicao(x * y**2 - x**3 * y, y)) == 2 * x * y - x**3
    T = (x**2 + y**2)**sp.Rational(-1, 2)
    assert sp.simplify(sp.diff(T, x, 2) + sp.diff(T, y, 2) - T**3) == 0
    A, B = sp.symbols('A B', nonzero=True)
    u = sp.sin(A * x) * sp.exp(-B * t)
    assert sp.solve(sp.simplify((sp.diff(u, t) - sp.diff(u, x, 2)) / u), B) == [A**2]


def test_lista_de_limites():
    m = sp.symbols('m', real=True)
    f = sp.Abs(x) / (sp.Abs(x) + sp.Abs(y))
    ao_longo = sp.simplify(f.subs(y, m * x).subs(x, sp.Rational(1, 10)))
    assert sp.simplify(ao_longo - 1 / (1 + sp.Abs(m))) == 0  # a correção: módulo em m
    assert ao_longo.subs(m, -1) == sp.Rational(1, 2) and ao_longo.subs(m, 0) == 1
    assert sp.limit((1 + x)**(2 / x), x, 0) == sp.E**2
    assert (1 + 1e-6)**(2 / 1e-6) == pytest.approx(math.e**2, rel=1e-5)


def test_lista_de_derivadas_parciais():
    assert parcial_pela_definicao(x * y**2, x) == y**2 and parcial_pela_definicao(x * y**2, y) == 2 * x * y
    tt = sp.symbols('t', positive=True)
    u = sp.exp(-x**2 / (4 * tt)) / (2 * sp.sqrt(sp.pi * tt))
    assert sp.simplify(sp.diff(u, tt) - sp.diff(u, x, 2)) == 0
    assert sp.diff(x * y, y) != sp.diff(x**2, x)  # Clairaut: não existe f
    mm = sp.symbols('m')
    u = sp.sin(mm * x) * sp.exp(-mm**2 * t)
    assert sp.simplify(sp.diff(u, t) - sp.diff(u, x, 2)) == 0
    a, b, c, d = sp.symbols('a b c d')
    f = a * x**3 + b * x**2 * y + c * x * y**2 + d * y**3
    assert sp.solve(sp.Poly(sp.diff(f, x, 2) + sp.diff(f, y, 2), x, y).coeffs(), (b, c)) == {b: -3 * d, c: -3 * a}


def test_resumos_e_anotacoes():
    r = sp.symbols('r', positive=True)
    assert sp.integrate(r**2 * (1 - sp.cos(th))**2, (th, 0, 2 * sp.pi)) == 3 * sp.pi * r**2  # cicloide
    assert sp.integrate(2 * sp.pi * sp.sin(t), (t, 0, sp.pi)) == 4 * sp.pi  # esfera
    hel = sp.Matrix([sp.cos(t), sp.sin(t), t])
    assert sp.simplify(hel.diff(t).norm()) == sp.sqrt(2)
    assert sp.solve(sp.Eq(2 * t + 2, x), t) == [x / 2 - 1] and sp.simplify((x / 2 - 1) + 1) == x / 2


# ---------------------------------------------------------------- notas da equipe

def test_nota_curvatura():
    rv = sp.Matrix([t, t**2, t**3])
    d1, d2 = rv.diff(t), rv.diff(t, 2)
    assert list(d1.cross(d2)) == [6 * t**2, -6 * t, 2]
    kappa = d1.cross(d2).norm() / d1.norm()**3
    assert sp.simplify(kappa.subs(t, 0)) == 2


def test_nota_gradiente():
    f = x**2 * y
    grad = sp.Matrix([sp.diff(f, x), sp.diff(f, y)]).subs({x: 1, y: 2})
    assert list(grad) == [4, 1]
    assert grad.dot(sp.Matrix([3, 4]) / 5) == sp.Rational(16, 5) and grad.norm() == sp.sqrt(17)


def test_nota_limite_e_plano_e_polares():
    m = sp.symbols('m', real=True)
    assert sp.simplify((x * y / (x**2 + y**2)).subs(y, m * x)) == m / (1 + m**2)
    P, Q, R = sp.Matrix([1, 0, 0]), sp.Matrix([0, 2, 0]), sp.Matrix([0, 0, 3])
    n = (Q - P).cross(R - P)
    assert list(n) == [6, 3, 2] and all(n.dot(p) == 6 for p in (P, Q, R))
    r = 1 + sp.sin(th)
    assert sp.integrate(r**2 / 2, (th, 0, 2 * sp.pi)) == 3 * sp.pi / 2
    assert sp.Integral(sp.sqrt(r**2 + sp.diff(r, th)**2), (th, 0, 2 * sp.pi)).evalf() == pytest.approx(8)


# ---------------------------------------------------------------- catálogo e restrições

def test_catalogo_completo_e_coerente():
    obrigatorios = {'id', 'nome', 'autoria', 'url', 'idioma', 'formato', 'notacao', 'topicos', 'licenca', 'acesso',
                    'prioridade', 'uso', 'justificativa'}
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f['id']
        assert f['prioridade'] in ('alta', 'media', 'referencia')
        assert f['uso'] in ('acervo', 'citada', 'referencia', 'candidato', 'indisponivel')
        assert set(f['topicos']) <= set(CALC3.assuntos), f['id']
    citadas = {c for i in ITENS.values() for c in i['fontes_catalogo']}
    assert citadas <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f['uso'] == 'acervo'} == {
        c for i in ITENS.values() if i['natureza'] == 'material_da_disciplina' for c in i['fontes_catalogo']}


def test_obras_protegidas_e_fotos_fora_do_repositorio():
    for ident in ('stewart-calculo-vol2', 'ufal-calc3-listas-stewart', 'pauls-online-notes-calc3'):
        assert CATALOGO[ident]['uso'] == 'referencia'
    texto = (ROOT / 'disciplinas/calc3/fontes.json').read_text(encoding='utf-8') + ''.join(
        i['texto'] + i['fonte_original'] for i in ITENS.values())
    assert 'archive.org' not in texto  # nem o livro nem o manual de soluções
    arquivos = [p for p in (ROOT / 'disciplinas/calc3').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.docx', '.pptx')]


def test_documentacao_lista_todas_as_fontes():
    curadoria = (ROOT / 'disciplinas/calc3/CURADORIA.md').read_text(encoding='utf-8')
    assert [i for i in CATALOGO if f'`{i}`' not in curadoria] == []
    assert [i for i in ITENS if f'`{i}`' not in curadoria] == []
