"""Acervo de Cálculo 4 (Engenharia de Computação, ECOM023) e conferência das resoluções com SymPy.

Os blocos parafraseiam a prova 2 do Prof. Gleydson Santos da Silva (cálculo vetorial) e as anotações da aula de
função impulso. Potenciais, integrais de linha e de superfície, Stokes, divergência e a EDO com impulso são
refeitos aqui.
"""

import re

import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

CALC4 = disciplinas.obter("calc4")
PASTA = ROOT / "disciplinas/calc4"
CATALOGO = {f["id"]: f for f in read_json(PASTA / "fontes.json")["fontes"]}
TODOS = {i["id"]: i for i in read_json(CALC4.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "calc4")
TEXTO = " ".join(i["texto"] for i in TODOS.values())
x, y, z, t = sp.symbols("x y z t", real=True)


def buscar(pergunta, d=CALC4):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def rot(F):
    P, Q, R = F
    return (sp.diff(R, y) - sp.diff(Q, z), sp.diff(P, z) - sp.diff(R, x), sp.diff(Q, x) - sp.diff(P, y))


# ---------------------------------------------------------------- cadastro e acervo


def test_calc4_cadastrada_com_acervo_proprio():
    assert CALC4.nome == "Cálculo 4" and CALC4.itens.exists()
    ids = {c["id"] for c in read_json(CALC4.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({CALC4.itens, CALC4.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(CALC4.assuntos)
    assert ids == set(TODOS) and len(TODOS) == 5


def test_situacao_da_disciplina():
    assert CALC4.situacao == "MVP" and not CALC4.em_validacao and not CALC4.aviso


def test_entra_no_quarto_periodo_de_ecom():
    from backend import cursos

    reg = next(d for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] == "calc4")
    assert reg["cursos"] == {"ecom": 4}
    assert "calc4" in cursos.preferidas("ecom", 4)


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas calc4 --embeddings`."""
    assert disciplinas.registros(CALC4) == read_json(CALC4.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    rotulo = {"validada": "validada", "pendente_professor": "pendente de confirmação do professor"}
    for i in TODOS.values():
        texto = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert i["status_curadoria"] == "aprovado", i["id"]
        assert len(texto) <= 2200, i["id"]
        assert texto.count("$$") % 2 == 0, i["id"]
        ultima = texto.strip().splitlines()[-1]
        assert "**Verificação:**" in ultima, i["id"]
        assert "não é gabarito do professor" in texto, i["id"]
        assert "Status da resolução: " + rotulo[i["status_resolucao"]] in texto, i["id"]
        nomes = re.findall(r"`(test_\w+)`", ultima)
        assert nomes and all(n in globals() for n in nomes), i["id"]
    provas = [i for i in TODOS.values() if i["tipo"] == "prova"]
    assert len(provas) == 4 and all(i["status_resolucao"] == "pendente_professor" for i in provas)
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, arq.name
        for f in re.search(r"fontes_catalogo: (.+)", cab).group(1).split(","):
            assert f.strip() in CATALOGO and CATALOGO[f.strip()]["uso"] == "acervo", (arq.name, f)


def test_livros_e_material_incerto_ficam_so_no_catalogo():
    for fid in ("stewart-calculo-vol2", "boyce-diprima-edo", "ufal-calc4-resumo-impulso"):
        assert CATALOGO[fid]["uso"] == "referencia"
    assert all(f["arquivo_local"] is None for f in CATALOGO.values())


def test_sem_dados_pessoais():
    textos = TEXTO + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"\b\d{8,}\b", textos)  # matrículas


def test_busca_acha_o_bloco_certo():
    assert "calc4-p2-q1-campo-conservativo" in buscar("campo conservativo e função potencial")[:3]
    assert "calc4-p2-q4-divergencia-caixa" in buscar("teorema da divergência numa caixa")[:3]
    assert "calc4-impulso-delta-dirac-laplace" in buscar("transformada de Laplace do delta de Dirac")[:3]


def test_fronteiras():
    for d in map(disciplinas.obter, ("calc3", "sinais")):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
    assert not buscar("Como funciona um flip-flop JK?")


# ---------------------------------------------------------------- conferência das resoluções


def test_p2_q1_campo_conservativo():
    P, Q = x**2, y**2
    assert sp.diff(Q, x) == sp.diff(P, y) == 0
    f = x**3 / 3 + y**3 / 3
    assert sp.diff(f, x) == P and sp.diff(f, y) == Q
    pelo_potencial = f.subs({x: 2, y: 8}) - f.subs({x: -1, y: 2})
    xt, yt = t, 2 * t**2
    integrando = sp.expand(P.subs({x: xt, y: yt}) * sp.diff(xt, t) + Q.subs({x: xt, y: yt}) * sp.diff(yt, t))
    assert integrando == t**2 + 16 * t**5
    assert pelo_potencial == sp.integrate(integrando, (t, -1, 2)) == 171


def test_p2_q2_area_da_esfera():
    r = sp.symbols("r", positive=True)
    ph, th = sp.symbols("phi theta", real=True)
    R = sp.Matrix([r * sp.sin(ph) * sp.cos(th), r * sp.sin(ph) * sp.sin(th), r * sp.cos(ph)])
    n = R.diff(ph).cross(R.diff(th))
    assert sp.simplify(n.dot(n) - (r**2 * sp.sin(ph)) ** 2) == 0
    assert sp.simplify(n - r * sp.sin(ph) * R) == sp.zeros(3, 1)
    assert sp.integrate(r**2 * sp.sin(ph), (ph, 0, sp.pi), (th, 0, 2 * sp.pi)) == 4 * sp.pi * r**2


def test_p2_q3_stokes_plano():
    F = (z, -2 * x, 3 * y)
    assert rot(F) == (3, 1, -2)
    n = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    assert sp.simplify(sp.Matrix(rot(F)).dot(n) - 2 / sp.sqrt(3)) == 0
    u = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
    w = n.cross(u)  # u, w ortonormais no plano, com u × w = n (anti-horário visto de cima)
    assert sp.simplify(u.cross(w) - n) == sp.zeros(3, 1)
    for centro, rho in (((sp.Rational(1, 3),) * 3, 1), ((1, 0, 0), 2), ((0, 2, -1), sp.Rational(1, 2))):
        c = sp.Matrix(centro)
        assert sum(c) == 1
        curva = c + rho * (sp.cos(t) * u + sp.sin(t) * w)
        dr = curva.diff(t)
        Ft = sp.Matrix([e.subs({x: curva[0], y: curva[1], z: curva[2]}) for e in F])
        integral = sp.integrate(sp.simplify(Ft.dot(dr)), (t, 0, 2 * sp.pi))
        assert sp.simplify(integral - 2 / sp.sqrt(3) * sp.pi * rho**2) == 0


def test_p2_q4_divergencia_caixa():
    a, b, c = sp.symbols("a b c", positive=True)
    F = (x**2 * y * z, x * y**2 * z, x * y * z**2)
    div = sum(sp.diff(Fi, v) for Fi, v in zip(F, (x, y, z)))
    assert sp.simplify(div - 6 * x * y * z) == 0
    tripla = sp.integrate(div, (x, 0, a), (y, 0, b), (z, 0, c))
    assert sp.simplify(tripla - 3 * a**2 * b**2 * c**2 / 4) == 0
    faces = (
        sp.integrate(F[0].subs(x, a), (y, 0, b), (z, 0, c))
        - sp.integrate(F[0].subs(x, 0), (y, 0, b), (z, 0, c))
        + sp.integrate(F[1].subs(y, b), (x, 0, a), (z, 0, c))
        - sp.integrate(F[1].subs(y, 0), (x, 0, a), (z, 0, c))
        + sp.integrate(F[2].subs(z, c), (x, 0, a), (y, 0, b))
        - sp.integrate(F[2].subs(z, 0), (x, 0, a), (y, 0, b))
    )
    assert sp.simplify(faces - tripla) == 0


def test_impulso_delta_dirac():
    assert sp.integrate((t**2 + 3 * t + 5) * sp.DiracDelta(t - 2), (t, -sp.oo, sp.oo)) == 15
    s = sp.symbols("s", positive=True)
    tp = sp.symbols("tp", positive=True)
    assert sp.laplace_transform(sp.DiracDelta(tp - 2), tp, s, noconds=True) == sp.exp(-2 * s)
    Y = (sp.exp(-sp.pi * s) - sp.exp(-2 * sp.pi * s)) / (s**2 + 4)
    yt = sp.inverse_laplace_transform(Y, s, tp)
    esperado = sp.sin(2 * tp) / 2 * (sp.Heaviside(tp - sp.pi) - sp.Heaviside(tp - 2 * sp.pi))
    for v in (1, 3.5, 4, 5, 6, 7, 9):
        assert abs(float(yt.subs(tp, v)) - float(esperado.subs(tp, v))) < 1e-12
    # entre os golpes, y = sen(2t)/2 resolve y'' + 4y = 0, com y(π) = 0 e y'(π) = 1 (salto do impulso)
    meio = sp.sin(2 * tp) / 2
    assert sp.simplify(sp.diff(meio, tp, 2) + 4 * meio) == 0
    assert meio.subs(tp, sp.pi) == 0 and sp.diff(meio, tp).subs(tp, sp.pi) == 1
    assert sp.diff(meio, tp).subs(tp, 2 * sp.pi) == 1  # o golpe −1 em 2π zera a velocidade
