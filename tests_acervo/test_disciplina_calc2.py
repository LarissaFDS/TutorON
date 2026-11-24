"""Acervo de Cálculo 2 (Engenharia de Computação, ECOM010) e conferência das resoluções com SymPy.

Os blocos parafraseiam as listas 4, 7 e 8 e a revisão da prova 4 da Profa. Xu Yang e a prova final que estão
no material do 2º período. Primitivas, somas, testes de convergência e séries de potências são refeitos aqui.
"""

import re

import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

CALC2 = disciplinas.obter("calc2")
PASTA = ROOT / "disciplinas/calc2"
CATALOGO = {f["id"]: f for f in read_json(PASTA / "fontes.json")["fontes"]}
TODOS = {i["id"]: i for i in read_json(CALC2.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "calc2")
TEXTO = " ".join(i["texto"] for i in TODOS.values())
x, n, N = sp.symbols("x n N", positive=True)


def buscar(pergunta, d=CALC2):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def zero(e):
    return sp.simplify(e) == 0


def primitiva(F, f):
    return zero(sp.diff(F, x) - f)


def serie_confere(f, termos, ordem, x0=0):
    s = sp.series(f, x, x0, ordem).removeO()
    return zero(sp.expand(s - termos))


# ---------------------------------------------------------------- cadastro e acervo


def test_calc2_cadastrada_com_acervo_proprio():
    assert CALC2.nome == "Cálculo 2" and CALC2.itens.exists()
    ids = {c["id"] for c in read_json(CALC2.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({CALC2.itens, CALC2.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(CALC2.assuntos)
    assert ids == set(TODOS)


def test_situacao_da_disciplina():
    assert CALC2.situacao == "MVP" and not CALC2.em_validacao and not CALC2.aviso


def test_entra_no_segundo_periodo_de_ecom():
    reg = next(d for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] == "calc2")
    assert reg["cursos"] == {"ecom": 2}


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas calc2 --embeddings`."""
    assert disciplinas.registros(CALC2) == read_json(CALC2.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert i["status_curadoria"] == "aprovado", i["id"]
        assert len(t) <= 2800, i["id"]
        ultima = t.strip().splitlines()[-1]
        assert "**Verificação:**" in ultima, i["id"]
        assert "não é gabarito do professor" in t and "Status da resolução:" in t, i["id"]
        nomes = re.findall(r"`(test_\w+)`", ultima)
        assert nomes, i["id"]
        for nome in nomes:
            assert nome in globals(), (i["id"], nome)
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, arq.name
        for f in re.search(r"fontes_catalogo: (.+)", cab).group(1).split(","):
            assert f.strip() in CATALOGO, (arq.name, f)


def test_livros_protegidos_ficam_so_no_catalogo():
    for fid in ("stewart-calculo-vol1", "stewart-solucoes-ingles"):
        assert CATALOGO[fid]["uso"] == "referencia" and CATALOGO[fid]["arquivo_local"] is None
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "stewart" not in re.search(r"fontes_catalogo: (.+)", cab).group(1), arq.name


def test_sem_dados_pessoais():
    textos = TEXTO + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)


def test_busca_acha_o_bloco_certo():
    assert "calc2-lista4-integracao-por-partes" in buscar("integração por partes de x cos x")[:3]
    assert "calc2-revisao-prova4-raio-intervalo" in buscar("raio e intervalo de convergência")[:3]
    assert "calc2-revisao-prova4-representacao-taylor" in buscar("série de Maclaurin de sen 2x")[:3]


# ---------------------------------------------------------------- conferência das resoluções


def test_lista4_partes():
    assert primitiva(x * sp.sin(x) + sp.cos(x), x * sp.cos(x))
    assert primitiva(x**5 * (5 * sp.log(x) - 1) / 25, x**4 * sp.log(x))
    assert primitiva(2 * (sp.sqrt(x) - 1) * sp.exp(sp.sqrt(x)), sp.exp(sp.sqrt(x)))
    assert zero(sp.integrate((x**2 + 1) * sp.exp(-x), (x, 0, 1)) - (3 - 6 / sp.E))
    assert zero(sp.integrate(x * sp.exp(-x), (x, 1, 5)) - (2 / sp.E - 6 * sp.exp(-5)))
    alvo = sp.log(2) / 2 - sp.Rational(1, 2)
    assert abs(float(sp.Integral(sp.sin(x) * sp.log(sp.cos(x)), (x, 0, sp.pi / 3)).evalf()) - float(alvo)) < 1e-12


def test_lista4_trigonometricas():
    assert primitiva(x / 2 + sp.sin(2 * x) / 4, sp.cos(x) ** 2)
    assert primitiva(sp.cos(x) ** 5 / 5 - sp.cos(x) ** 3 / 3, sp.sin(x) ** 3 * sp.cos(x) ** 2)
    assert sp.integrate(sp.sin(x) ** 7 * sp.cos(x) ** 5, (x, 0, sp.pi / 2)) == sp.Rational(1, 120)
    assert zero(sp.integrate(sp.tan(x) ** 4, (x, 0, sp.pi / 4)) - (sp.pi / 4 - sp.Rational(2, 3)))
    # sqrt(1 + cos 2x) = sqrt(2) cos x em [0, pi/6]
    assert zero(sp.integrate(sp.sqrt(2) * sp.cos(x), (x, 0, sp.pi / 6)) - sp.sqrt(2) / 2)
    m, k = 2, 3
    assert sp.integrate(sp.sin(m * x) * sp.cos(k * x), (x, -sp.pi, sp.pi)) == 0
    assert sp.integrate(sp.sin(m * x) * sp.sin(k * x), (x, -sp.pi, sp.pi)) == 0
    assert sp.integrate(sp.sin(m * x) ** 2, (x, -sp.pi, sp.pi)) == sp.pi


def test_lista7_series():
    assert sp.limit((n + 1) / (2 * n + 1), n, sp.oo) == sp.Rational(1, 2)
    assert zero(sp.limit(sp.E - sp.exp(1 / (N + 1)), N, sp.oo) - (sp.E - 1))
    assert zero(sp.apart(2 / (n**2 + 4 * n + 3), n) - (1 / (n + 1) - 1 / (n + 3)))
    assert sp.summation(2 / (n**2 + 4 * n + 3), (n, 1, sp.oo)) == sp.Rational(5, 6)
    r = sp.cos(1)
    assert abs(float(r)) < 1
    assert abs(float(sum(r**k for k in range(1, 200))) - float(r / (1 - r))) < 1e-12
    assert sp.integrate(1 / (x * sp.log(x)), (x, 2, sp.oo)) == sp.oo
    assert sp.integrate(x * sp.exp(-x), (x, 1, sp.oo)).is_finite
    assert sp.limit(sp.sin(1 / n) / (1 / n), n, sp.oo) == 1
    assert all(1 / sp.factorial(k) <= sp.Rational(1, 2 ** (k - 1)) for k in range(1, 30))


def test_lista8_alternadas_razao_raiz():
    # razão com L = 1 não decide: sum 1/n diverge e sum 1/n^2 converge, ambas com L = 1
    assert sp.limit((1 / (n + 1)) / (1 / n), n, sp.oo) == 1
    assert sp.limit((1 / (n + 1) ** 2) / (1 / n**2), n, sp.oo) == 1
    assert sp.summation(1 / n**2, (n, 1, sp.oo)).is_finite and sp.summation(1 / n, (n, 1, sp.oo)) == sp.oo
    # série alternada: b_n = 1/n decresce e tende a 0, logo sum (-1)^n/n converge (a ln 2)
    assert zero(sp.summation((-1) ** (n + 1) / n, (n, 1, sp.oo)) - sp.log(2))


def test_revisao_raio_intervalo():
    # raio pela razão: sum x^n/(n 5^n) tem R = 5; sum (2x)^n tem R = 1/2
    assert 1 / sp.limit((1 / ((n + 1) * 5 ** (n + 1))) / (1 / (n * 5**n)), n, sp.oo) == 5
    assert 1 / sp.limit(2 ** (n + 1) / 2**n, n, sp.oo) == sp.Rational(1, 2)


def test_revisao_representacao_taylor():
    o = 9
    assert serie_confere(1 / (x + 10), sum((-1) ** k * x**k / 10 ** (k + 1) for k in range(o)), o)
    assert serie_confere(sp.log(5 - x), sp.log(5) - sum(x**k / (k * 5**k) for k in range(1, o)), o)
    assert serie_confere(x**2 / (1 - 2 * x) ** 2, sum((k + 1) * 2**k * x ** (k + 2) for k in range(o - 2)), o)
    assert serie_confere(sp.sin(x) ** 2, x**2 - x**4 / 3 + 2 * x**6 / 45, 8)
    assert serie_confere(x**2 * sp.atan(x**3), sum((-1) ** k * x ** (6 * k + 5) / (2 * k + 1) for k in range(3)), 18)
    assert zero(sp.apart((x + 2) / (2 * x**2 - x - 1), x) - (1 / (x - 1) - 1 / (2 * x + 1)))
    assert zero(sp.expand(-1 + 3 * (x + 1) - 3 * (x + 1) ** 2 + (x + 1) ** 3) - x**3)
    y = sp.Symbol("y")
    s = sp.series(1 / y, y, -3, 6).removeO()
    assert zero(sp.expand(s + sum((y + 3) ** k / sp.Integer(3) ** (k + 1) for k in range(6))))


def test_prova_final():
    t = sp.Symbol("t")
    f = (2 * x - 1) * sp.exp(3 * x) / (sp.exp(x) - 1)
    assert zero(f - ((2 * x - 1) * sp.exp(2 * x) + sp.exp(-x) * f))
    assert sp.integrate(t**2, (t, 0, 1)) + sp.integrate(sp.sqrt(t), (t, 0, 1)) == 1
    assert zero(sp.integrate(1 / (x**2 - x + 1), (x, 0, sp.Rational(1, 2))) - sp.pi / (3 * sp.sqrt(3)))
    soma = sum(sp.Rational((-1) ** k, 8**k) * (sp.Rational(2, 3 * k + 1) + sp.Rational(1, 3 * k + 2)) for k in range(60))
    assert abs(float(3 * sp.sqrt(3) / 4 * soma) - float(sp.pi)) < 1e-12
    wallis = [sp.integrate(sp.sin(x) ** k, (x, 0, sp.pi / 2)) for k in (2, 4, 6)]
    assert wallis == [sp.pi / 4, 3 * sp.pi / 16, 5 * sp.pi / 32]
