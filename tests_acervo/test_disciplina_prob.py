"""Acervo de Probabilidade e Estatística e conferência das resoluções.

Os blocos afirmam probabilidades, médias e variâncias. Aqui cada valor é refeito com `fractions`/SymPy
(exato), com `scipy.stats` (distribuições) e, quando a afirmação é de probabilidade, com uma simulação
de Monte Carlo pequena com semente fixa. Os erros encontrados nas anotações do aluno são conferidos
como erros e não podem aparecer no acervo como afirmação.
"""
import dataclasses
import json
import math
import re
import shutil
import subprocess
from fractions import Fraction as Fr
from math import comb, perm

import numpy as np
import pytest
import sympy as sp
from scipy import stats

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

PROB = disciplinas.obter('prob')
FONTES = read_json(ROOT / 'disciplinas/prob/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {i['id']: i for i in read_json(PROB.itens)}
NA_BUSCA = {c['id'] for c in read_json(PROB.indice)['chunks']}
VETORES = json.loads((ROOT / 'eval/relevancia-vetores.json').read_text(encoding='utf-8'))
RNG = np.random.default_rng(2025)


def texto(ident):
    return ITENS[ident]['texto']


def buscar(pergunta, d=PROB):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def hibrida(pergunta, d=PROB):
    """A mesma busca do backend (corte e penalidade de hub), com o embedding real gravado da pergunta."""
    return [r['id'] for r in search(pergunta, k=4, vector=VETORES[pergunta], min_similarity=0.45, hub_penalty=True,
                                    itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo

def test_prob_cadastrada_com_acervo_proprio_e_a_mesma_ia():
    assert PROB.nome == 'Probabilidade e Estatística' and PROB.itens.exists() and PROB.indice.exists()
    assert not PROB.livro_supabase and PROB.rigor.strip() == (ROOT / 'disciplinas/prob/rigor.md').read_text(encoding='utf-8').strip()
    assert all(c['disciplina'] == 'prob' for c in read_json(PROB.indice)['chunks'])
    for outra in ('paa', 'sd', 'oac', 'calc3', 'fis2', 'ed', 'bd'):
        d = disciplinas.obter(outra)
        assert NA_BUSCA.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    # Nada de modelo, chave ou prompt próprio: o cadastro só tem os campos comuns.
    bruto = [d for d in read_json(ROOT / 'disciplinas/disciplinas.json')['disciplinas'] if d['id'] == 'prob'][0]
    assert not {'modelo', 'model', 'provedor', 'endpoint', 'prompt', 'chave'} & set(bruto)
    assert read_json(PROB.indice)['embedding_model'] == read_json(disciplinas.obter('bd').indice)['embedding_model']


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas prob --embeddings`."""
    gerados = disciplinas.registros(PROB)
    assert gerados == read_json(PROB.itens)
    assert NA_BUSCA == {i['id'] for i in gerados if i['confiabilidade'] in ('media', 'alta')}
    assert read_json(PROB.indice)['modo'] == 'hibrido'


def test_blocos_cabem_no_trecho_e_formulas_fecham():
    for i in ITENS.values():
        assert len(i['texto']) <= 2200, i['id']
        sem_destaque = i['texto'].replace('$$', '')
        assert i['texto'].count('$$') % 2 == 0 and sem_destaque.count('$') % 2 == 0, i['id']
        assert '**Verificação:**' in i['texto'], i['id']


def test_notas_de_ia_sem_revisao_ficam_fora_da_busca():
    notas = [i for i in ITENS.values() if i['natureza'] == 'nota_da_equipe_ia']
    assert len(notas) == 6
    assert all(i['status_curadoria'] == 'candidato' and i['revisao_humana'] == 'pendente' for i in notas)
    assert {i['id'] for i in notas}.isdisjoint(NA_BUSCA)
    assert not any(i.get('revisao_humana') == 'feita' or i.get('revisao_professor') for i in ITENS.values())


def test_topicos_com_anotacoes_tem_bloco_na_busca():
    """Critério de liberação: todo tópico marcado "Sim" no mapeamento (01 a 07; 08 e 09 também têm) está na busca."""
    na_busca = {ITENS[i]['assunto'] for i in NA_BUSCA}
    assert set(PROB.assuntos[:9]) <= na_busca
    assert not set(PROB.assuntos[9:]) & na_busca  # descritiva, inferência e regressão: só notas candidatas


# ---------------------------------------------------------------- status das resoluções

def test_resolucoes_tem_status_e_dizem_no_texto():
    turma = [i for i in ITENS.values() if i['natureza'] == 'material_da_disciplina']
    assert len(turma) == 19
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    for i in turma:
        assert f"Status da resolução: {rotulo[i['status_resolucao']]}" in i['texto'], i['id']
    corrigidas = {i['id'] for i in turma if i['status_resolucao'] == 'corrigida'}
    assert corrigidas == {'prob-anot-conceitos-probabilidade', 'prob-anot-contagem', 'prob-anot-va-continua',
                          'prob-anot-esperanca-variancia', 'prob-anot-binomial', 'prob-anot-combinacao-linear-normais'}
    assert all('**Correç' in texto(c) for c in corrigidas)
    assert {i['id'] for i in turma if i['status_resolucao'] == 'pendente_professor'} == {'prob-anot-elevador'}


# ---------------------------------------------------------------- erros das anotações (conferidos como erros)

def test_erro_variancia_da_diferenca():
    """Anotação: Var(X − Y) = Var(X) − Var(Y). Errado: as variâncias somam."""
    x, y = RNG.normal(0, 3, 200_000), RNG.normal(0, 2, 200_000)
    assert np.var(x - y) == pytest.approx(9 + 4, rel=0.02)
    assert abs(np.var(x - y) - (9 - 4)) > 5
    assert 'Var}(X - Y) = \\operatorname{Var}(X) + \\operatorname{Var}(Y)' in texto('prob-anot-esperanca-variancia')


def test_erro_soma_de_dbinom_para_p_x_menor_igual_3():
    """Anotação: P(X ≤ 3) = dbinom(1) + … + dbinom(4). Certo: de 0 a 3."""
    b = stats.binom(10, 0.3)
    assert sum(b.pmf(k) for k in range(4)) == pytest.approx(b.cdf(3)) == pytest.approx(0.6496, abs=5e-5)
    assert sum(b.pmf(k) for k in range(1, 5)) != pytest.approx(b.cdf(3), abs=0.01)


def test_erro_multiplo_de_uma_normal_e_notacao_do_exemplo_1():
    """Anotação: Var(nX) = nσ². Vale para a soma de n cópias independentes; Var(nX) = n²σ²."""
    x = RNG.normal(75, 10, (200_000, 8))
    assert np.var(8 * x[:, 0]) == pytest.approx(64 * 100, rel=0.02)
    assert np.var(x.sum(axis=1)) == pytest.approx(8 * 100, rel=0.02)
    # 16,81 e 106,09 só fecham como variâncias (desvios 4,1 e 10,3).
    assert math.sqrt(16.81) == pytest.approx(4.1) and math.sqrt(106.09) == pytest.approx(10.3)
    assert math.sqrt(16.81 + 106.09) == pytest.approx(11.086, abs=1e-3)
    assert stats.norm(204, math.sqrt(122.9)).cdf(200) == pytest.approx(0.3591, abs=5e-5)


def test_erro_arranjo_e_condicoes_das_regras():
    assert perm(5, 2) == 20 and comb(5, 2) == 10 and perm(5, 2) == math.factorial(2) * comb(5, 2)
    omega = set(range(1, 7))
    par, b, c = {2, 4, 6}, {1, 2}, {1, 3}
    P = lambda e: Fr(len(e), len(omega))  # noqa: E731
    assert P(par & b) == P(par) * P(b) and par & b  # independentes, não disjuntos
    assert P(par | c) == P(par) + P(c) and P(par & c) != P(par) * P(c)  # disjuntos, não independentes


def test_erro_densidade_sem_intervalo_e_fda_nao_decrescente():
    x = sp.symbols('x')
    assert sp.integrate(x / 4, (x, 1, 3)) == 1
    assert sp.integrate(x / 4, (x, 0, 3)) != 1  # sem o intervalo [1, 3] não é densidade
    assert sp.integrate(x / 4, (x, 1, 2)) == sp.Rational(3, 8)
    F = stats.binom(2, 0.5).cdf
    assert F(0.2) == F(0.7) == 0.25  # constante entre valores: não decrescente, não "sempre crescente"


def test_erros_nao_aparecem_como_afirmacao():
    todo = '\n'.join(i['texto'] for i in ITENS.values())
    assert 'operatorname{Var}(X - Y) = \\operatorname{Var}(X) - \\operatorname{Var}(Y)' not in todo
    assert '\\sigma^2(X - Y) = \\sigma^2(X) - \\sigma^2(Y)' in texto('prob-anot-esperanca-variancia')  # citado como erro
    assert 'esquecem o zero e incluem o 4' in texto('prob-anot-binomial')
    assert '\\operatorname{Var}(nX) = n^2\\sigma^2' in texto('prob-anot-combinacao-linear-normais')
    assert 'não decrescente' in texto('prob-anot-va-continua')


# ---------------------------------------------------------------- resoluções das anotações

def test_bayes_maquinas():
    pa, pb, pc = Fr(1, 2), Fr(3, 10), Fr(1, 5)
    da, db, dc = Fr(2, 100), Fr(3, 100), Fr(5, 100)
    pd = da * pa + db * pb + dc * pc
    assert pd == Fr(29, 1000)
    post = [da * pa / pd, db * pb / pd, dc * pc / pd]
    assert post == [Fr(10, 29), Fr(9, 29), Fr(10, 29)] and sum(post) == 1
    assert float(post[0]) == pytest.approx(0.3448, abs=5e-5)
    maq = RNG.choice(3, 200_000, p=[0.5, 0.3, 0.2])
    defeito = RNG.random(200_000) < np.array([0.02, 0.03, 0.05])[maq]
    freq = np.bincount(maq[defeito], minlength=3) / defeito.sum()
    assert freq == pytest.approx([10 / 29, 9 / 29, 10 / 29], abs=0.02)


def test_bayes_teste_diagnostico():
    pos = Fr(95, 100) * Fr(1, 100) + Fr(5, 100) * Fr(99, 100)
    assert pos == Fr(59, 1000) and float(Fr(95, 10000) / pos) == pytest.approx(0.1610, abs=5e-5)
    doente = RNG.random(500_000) < 0.01
    positivo = np.where(doente, RNG.random(500_000) < 0.95, RNG.random(500_000) < 0.05)
    assert doente[positivo].mean() == pytest.approx(0.161, abs=0.01)


def test_contagem_comissao_e_va_discreta():
    assert comb(7, 2) + 7 == 28 and Fr(12, 52) == Fr(3, 13)
    assert math.factorial(5) // (math.factorial(3) * math.factorial(2)) == 10
    p = Fr(comb(14, 2) * comb(21, 1) + comb(14, 3), comb(35, 3))
    assert p == Fr(2275, 6545) and float(p) == pytest.approx(0.3476, abs=5e-5)
    h = stats.hypergeom(35, 14, 3)
    assert h.sf(1) == pytest.approx(float(p)) and h.mean() == pytest.approx(1.2)
    assert [round(h.pmf(k), 3) for k in range(4)] == [0.203, 0.449, 0.292, 0.056]
    assert sum(Fr(comb(14, k) * comb(21, 3 - k), comb(35, 3)) for k in range(4)) == 1


def test_esperanca_variancia_dado():
    xs = range(1, 7)
    ex, ex2 = sum(Fr(x, 6) for x in xs), sum(Fr(x * x, 6) for x in xs)
    assert ex == Fr(7, 2) and ex2 == Fr(91, 6) and ex2 - ex**2 == Fr(35, 12)


def test_discretas():
    assert stats.randint(1, 11).var() == pytest.approx(((10 - 1 + 1)**2 - 1) / 12) == pytest.approx(8.25)
    assert stats.bernoulli(0.3).var() == pytest.approx(0.21)
    g = stats.geom(0.2)
    assert g.pmf(3) == pytest.approx(0.128) and g.cdf(3) == pytest.approx(1 - 0.8**3) == pytest.approx(0.488)
    assert stats.poisson.sf(4, 3) == pytest.approx(0.1847, abs=5e-5)
    assert stats.poisson.sf(2, 3) == pytest.approx(1 - math.exp(-3) * (1 + 3 + 4.5))
    assert stats.poisson.pmf(10, 15 * 40 / 60) == pytest.approx(0.1251, abs=5e-5)
    assert sum(stats.poisson.pmf(k, 3) for k in range(51)) == pytest.approx(1)


def test_normal_cinco_tipos_e_tabela():
    n = stats.norm(40, 10)
    assert n.cdf(50) == stats.norm.cdf(1) == pytest.approx(0.8413, abs=5e-5)
    assert n.sf(35) == pytest.approx(0.6915, abs=5e-5)
    assert n.cdf(60) - n.cdf(25) == pytest.approx(0.9104, abs=5e-5)
    assert n.cdf(30) + n.sf(55) == pytest.approx(0.2255, abs=5e-5)
    assert n.ppf(0.95) == pytest.approx(56.45, abs=5e-3) and n.isf(0.10) == pytest.approx(n.ppf(0.90))
    assert n.ppf(0.90) == pytest.approx(52.82, abs=5e-3)
    assert stats.norm.cdf(1) - 0.5 == pytest.approx(0.3413, abs=5e-5)  # tabela de área entre 0 e z


def test_uniforme_continua():
    u = stats.uniform(0, 10)
    assert u.cdf(5) - u.cdf(2) == pytest.approx(0.3) and u.var() == pytest.approx(100 / 12)


def test_exponencial_e_falta_de_memoria():
    assert stats.expon(scale=5).cdf(5) == pytest.approx(0.6321, abs=5e-5)
    assert stats.expon(scale=5).sf(10) == pytest.approx(0.1353, abs=5e-5)
    assert stats.expon(scale=3).sf(2) == pytest.approx(0.5134, abs=5e-5)
    assert stats.expon(scale=3).cdf(4) - stats.expon(scale=3).cdf(2) == pytest.approx(0.2498, abs=5e-5)
    assert stats.expon(scale=4).sf(5) == stats.expon(scale=1 / 15).sf(5 / 60) == pytest.approx(0.2865, abs=5e-5)
    assert stats.expon(scale=8).sf(8) == stats.poisson.pmf(0, 1) == pytest.approx(0.3679, abs=5e-5)
    t = RNG.exponential(5, 400_000)
    assert (t[t > 5] > 15).mean() == pytest.approx((t > 10).mean(), abs=0.01) == pytest.approx(math.exp(-2), abs=0.01)


def test_combinacao_linear_e_elevador():
    liq = stats.norm(910, math.sqrt(500))
    assert liq.cdf(850) == pytest.approx(0.0036, abs=5e-5)
    assert liq.sf(870) == pytest.approx(0.9632, abs=5e-5)
    assert liq.cdf(920) - liq.cdf(860) == pytest.approx(0.6600, abs=5e-5)
    sim = RNG.normal(1000, 20, 200_000) - RNG.normal(90, 10, 200_000)
    assert sim.std() == pytest.approx(22.36, abs=0.2)
    assert stats.norm(600, 10 * math.sqrt(8)).sf(650) == pytest.approx(0.0385, abs=5e-5)
    assert (RNG.normal(75, 10, (200_000, 8)).sum(axis=1) > 650).mean() == pytest.approx(0.0385, abs=0.003)


def test_aproximacao_normal():
    aprox = stats.norm(60, math.sqrt(42))
    assert aprox.sf(49.5) == pytest.approx(0.9474, abs=5e-5)
    assert stats.binom(200, 0.3).sf(49) == pytest.approx(0.9494, abs=5e-5)
    assert aprox.sf(50) == pytest.approx(0.9386, abs=5e-5)
    assert abs(aprox.sf(49.5) - 0.9494) < abs(aprox.sf(50) - 0.9494)  # a correção de continuidade aproxima
    assert stats.norm(1000, math.sqrt(1000)).cdf(950.5) == pytest.approx(0.0588, abs=5e-5)
    assert stats.poisson.cdf(950, 1000) == pytest.approx(0.0578, abs=5e-5)


def test_notas_da_equipe():
    import statistics as st
    d = [2, 4, 4, 5, 7, 9]
    assert st.median(d) == 4.5 and st.variance(d) == pytest.approx(6.1667, abs=5e-5)
    assert st.pvariance(d) == pytest.approx(5.1389, abs=5e-5)
    assert stats.norm.sf(1.2) == pytest.approx(0.1151, abs=5e-5)
    assert stats.gamma(36, scale=5 / 36).sf(6) == pytest.approx(0.1184, abs=5e-5)
    assert stats.t.ppf(0.975, 15) == pytest.approx(2.1314, abs=5e-5)
    assert 2 * stats.t.sf(2.5, 24) == pytest.approx(0.0197, abs=5e-5)
    assert 1.96 * math.sqrt(0.3 * 0.7 / 400) == pytest.approx(0.0449, abs=5e-5)
    assert list(np.polyfit([1, 2, 3, 4, 5], [2, 4, 5, 4, 5], 1)) == pytest.approx([0.6, 2.2])
    assert np.corrcoef([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])[0, 1] == pytest.approx(0.7746, abs=5e-5)
    assert stats.hypergeom(35, 14, 3).mean() == pytest.approx(1.2)


# ---------------------------------------------------------------- busca

@pytest.mark.parametrize('pergunta, esperado', [
    ('Qual a diferença entre eventos independentes e mutuamente exclusivos?', 'prob-anot-conceitos-probabilidade'),
    ('Como calcular P(X > 2) numa Poisson com média 3?', 'prob-anot-poisson'),
    ('O que significa a falta de memória da distribuição exponencial?', 'prob-anot-exponencial'),
    ('Se X e Y são normais independentes, qual a distribuição de 2X − Y?', 'prob-anot-combinacao-linear-normais'),
    ('Como padronizar uma normal e usar a tabela?', 'prob-anot-normal-padronizacao'),
    ('Teorema de Bayes: teste positivo para doença rara', 'prob-anot-bayes-teste-diagnostico'),
    ('Qual a variância de X − Y?', 'prob-anot-esperanca-variancia'),
])
def test_perguntas_de_exemplo_trazem_o_bloco_certo(pergunta, esperado):
    assert buscar(pergunta)[0] == esperado
    assert esperado in hibrida(pergunta) if pergunta in VETORES else True


@pytest.mark.parametrize('latex, simples, esperado', [
    (r'Calcule $P(X > 2)$ para $X \sim \text{Poisson}(\lambda = 3)$',
     'Como calcular P(X > 2) numa Poisson com média 3?', 'prob-anot-poisson'),
    (r'Por que $P(X > s + t \mid X > s) = P(X > t)$ na exponencial?',
     'O que significa a falta de memória da distribuição exponencial?', 'prob-anot-exponencial'),
    (r'Qual a distribuição de $W = 2X - Y$ com $X \sim N(\mu_X, \sigma_X^2)$ e $Y \sim N(\mu_Y, \sigma_Y^2)$ independentes?',
     'Se X e Y são normais independentes, qual a distribuição de 2X − Y?', 'prob-anot-combinacao-linear-normais'),
    (r'Como achar $\Phi(z)$ com $z = (x - \mu)/\sigma$ na tabela?',
     'Como padronizar uma normal e usar a tabela?', 'prob-anot-normal-padronizacao'),
    (r'$P(A \cap B) = P(A)P(B)$ ou $P(A \cup B) = P(A) + P(B)$: quando vale cada uma?',
     'Qual a diferença entre eventos independentes e mutuamente exclusivos?', 'prob-anot-conceitos-probabilidade'),
])
def test_latex_e_texto_simples_trazem_o_mesmo_bloco(latex, simples, esperado):
    assert esperado in hibrida(latex) and esperado in hibrida(simples)


@pytest.mark.parametrize('pergunta', ['Qual o período de um pêndulo simples de 1 m?', 'Como fazer um LEFT JOIN em SQL?',
                                      'Me conte uma piada'])
def test_pergunta_de_outra_area_nao_traz_material(pergunta):
    assert hibrida(pergunta) == []


def test_isolamento_com_as_disciplinas_de_fronteira():
    calc3, fis2 = disciplinas.obter('calc3'), disciplinas.obter('fis2')
    # Probabilidade com Cálculo 3 ou Física 2 selecionada: nada de prob, nem material da outra por engano.
    assert hibrida('Como calcular P(X > 2) numa Poisson com média 3?', calc3) == []
    assert hibrida('O que significa a falta de memória da distribuição exponencial?', fis2) == []
    # No outro sentido: o índice de prob nunca devolve blocos de Cálculo 3 ou Física 2.
    for p in ('Como calcular uma integral dupla em coordenadas polares?', 'Qual o período de um pêndulo simples?',
              'O que é a distribuição de velocidades de Maxwell?'):
        assert all(i.startswith('prob-') for i in buscar(p))
        assert not any(i.startswith('prob-') for i in buscar(p, calc3) + buscar(p, fis2))


# ---------------------------------------------------------------- KaTeX, catálogo e restrições

FORMULA = re.compile(r'\$\$(.+?)\$\$|\$(.+?)\$', re.S)


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


def test_catalogo_completo_e_coerente():
    obrigatorios = {'id', 'nome', 'autoria', 'url', 'idioma', 'formato', 'notacao', 'topicos', 'licenca', 'acesso',
                    'prioridade', 'uso', 'justificativa'}
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f['id']
        assert f['prioridade'] in ('alta', 'media', 'referencia') and f['uso'] in ('acervo', 'citada', 'referencia')
        assert set(f['topicos']) <= set(PROB.assuntos), f['id']
    assert {x for i in ITENS.values() for x in i['fontes_catalogo']} <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f['uso'] == 'acervo'} == {
        x for i in ITENS.values() if i['natureza'] == 'material_da_disciplina' for x in i['fontes_catalogo']}
    assert 'NC-SA' in CATALOGO['openstax-introductory-statistics-2e']['licenca']
    for protegida in ('bussab-morettin', 'magalhaes-lima-nocoes', 'verzani-simpler'):
        assert CATALOGO[protegida]['uso'] == 'referencia'


def test_anotacoes_e_imagens_fora_do_repositorio():
    arquivos = [p for p in (ROOT / 'disciplinas/prob').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.webp', '.docx', '.pptx')]
    for i in ITENS.values():
        if i['natureza'] == 'material_da_disciplina':
            assert i['publicacao_transcricao'].startswith('não autorizada') and 'PDFs não estão' in i['licenca']
    rastreados = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout
    assert not [l for l in rastreados.splitlines() if re.search(r'(_25\d{4}_\d{6}\.pdf|Probabilidade.*\.(pdf|png|jpe?g))$', l)]


def test_documentacao_lista_fontes_e_blocos():
    curadoria = (ROOT / 'disciplinas/prob/CURADORIA.md').read_text(encoding='utf-8')
    assert [i for i in CATALOGO if f'`{i}`' not in curadoria] == []
    assert [i for i in ITENS if f'`{i}`' not in curadoria] == []
