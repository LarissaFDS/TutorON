"""Acervo de Cálculo 1 e conferência das contas.

Os blocos parafraseiam provas, listas e resoluções de Cálculo 1 do IM-UFAL (fotos e PDFs não versionados),
com resolução da equipe TutorON. Cada número que aparece num bloco é recalculado aqui com SymPy
ou conferido numericamente.
"""

import json
import re
import shutil
import subprocess

import pytest
import sympy as sp
from sympy import Rational as Q
from sympy import cbrt, cos, cosh, diff, exp, limit, log, oo, pi, sin, sinh, solve, sqrt, tan

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

C1 = disciplinas.obter("calc1")
PASTA = ROOT / "disciplinas/calc1"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
ITENS = {i["id"]: i for i in read_json(C1.itens)}
OUTRAS = ("calc3", "fis1", "fis2", "ga", "paa", "prob", "discreta", "varcomp", "circ", "sinais", "lfa", "ed")
x, h, t = sp.symbols("x h t", real=True)


def buscar(pergunta, d=C1):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def iguais(a, b):
    d = sp.simplify(a - b)
    if d == 0:
        return True
    livres = sorted(d.free_symbols, key=str)  # identidades trigonométricas que o simplify não fecha
    return bool(livres) and all(abs(complex(d.subs({s: v for s in livres}).evalf())) < 1e-9 for v in (0.3, 0.71, 1.3))


# ---------------------------------------------------------------- cadastro e acervo


def test_calc1_cadastrada_com_acervo_proprio():
    assert C1.nome == "Cálculo 1" and C1.itens.exists() and C1.indice.exists() and not C1.livro_supabase
    ids = {c["id"] for c in read_json(C1.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({C1.itens, C1.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert all(c["disciplina"] == "calc1" for c in read_json(C1.indice)["chunks"])
    assert {i["assunto"] for i in ITENS.values()} == set(C1.assuntos)  # nenhum tópico sem bloco na busca
    assert ids == set(ITENS)


def test_situacao_da_disciplina():
    assert C1.situacao == "MVP" and not C1.em_validacao and not C1.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas calc1 --embeddings`."""
    gerados = disciplinas.registros(C1)
    assert gerados == read_json(C1.itens)
    assert {c["id"] for c in read_json(C1.indice)["chunks"]} == {
        i["id"] for i in gerados if i["confiabilidade"] in ("media", "alta")
    }


def test_blocos_cabem_no_trecho_e_terminam_com_verificacao():
    for i in ITENS.values():
        assert len(i["texto"]) <= 2200, i["id"]  # backend/rag.py corta acima disso
        assert "**Verificação:**" in i["texto"].strip().splitlines()[-1], i["id"]


def test_nenhuma_nota_da_ia_e_nada_revisado_sem_registro():
    assert not [i for i, x in ITENS.items() if x["natureza"] == "nota_da_equipe_ia"]
    for p in C1.materiais.glob("*.md"):
        cab = p.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, p.name


# ---------------------------------------------------------------- busca e isolamento


@pytest.mark.parametrize(
    "pergunta, aceitos",
    [
        ("Como derivar √(2x+1) pela definição?", {"calc1-derivada-pela-definicao"}),
        ("Quando posso usar a regra de L'Hospital?", {"calc1-regra-lhospital"}),
        ("Quais são as assíntotas de x²/(x−1)?", {"calc1-assintotas-limites-infinito", "calc1-esboco-grafico"}),
        ("Como resolver o problema da escada que desliza na parede?", {"calc1-taxas-relacionadas"}),
        ("Qual o cilindro de volume máximo inscrito num cone?", {"calc1-otimizacao-geometrica"}),
        ("Como achar a reta tangente usando derivação implícita?", {"calc1-derivacao-implicita"}),
        ("Como usar a aproximação linear para estimar uma raiz?", {"calc1-aproximacao-linear"}),
        ("Como achar o máximo e o mínimo absolutos num intervalo fechado?", {"calc1-extremos-absolutos"}),
        ("O que diz o Teorema do Valor Médio?", {"calc1-tvm-rolle"}),
        ("Como achar a primitiva com condição inicial?", {"calc1-primitivas-condicoes"}),
        ("Como escolher as constantes para a função por partes ser contínua?", {"calc1-continuidade-por-partes"}),
        ("Qual a derivada do seno hiperbólico?", {"calc1-funcoes-hiperbolicas"}),
        ("Como calcular o limite de (cos x)^(1/x) quando x tende a 0?", {"calc1-cc-limites-potencias-log", "calc1-regra-lhospital"}),
        ("Qual o terreno de 200 m² com cerca de menor custo?", {"calc1-cc-otimizacao-cercas"}),
        ("Como esboçar o gráfico de x³/(x² − 1)?", {"calc1-cc-esboco-x3-sobre-x2-menos-1", "calc1-esboco-grafico"}),
        ("Como achar y sabendo a terceira derivada 2 − 6x e um ponto de máximo em (0, 2)?", {"calc1-cc-primitivas-tvm-estimativa", "calc1-primitivas-condicoes"}),
    ],
)
def test_pergunta_de_calc1_encontra_bloco_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize("pergunta", ["Qual a capital da França?", "Como declarar um ponteiro em C?"])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


@pytest.mark.parametrize(
    "pergunta",
    [
        "Como calcular a derivada?",
        "Como achar o máximo de uma função?",
        "O que é a regra da cadeia?",
        "Como calcular a velocidade a partir da posição?",
        "Como calcular uma integral?",
    ],
)
def test_vocabulario_comum_fica_na_disciplina_escolhida(pergunta):
    """Fronteiras com Cálculo 3 e Física 1 (e as demais): cada disciplina busca só no próprio índice."""
    assert all(i.startswith("calc1-") for i in buscar(pergunta))
    for d in OUTRAS:
        assert not any(i.startswith("calc1-") for i in buscar(pergunta, disciplinas.obter(d)))


def test_rigor_tem_dominio_hipoteses_e_fronteiras():
    for termo in ("domínio", "forma indeterminada", "L'Hospital", "TVM", "Rolle", "hipóteses", "Cálculo 2",
                  "Cálculo 3", "Física 1", "**Verificação:**", "Não entregue a resolução"):  # fmt: skip
        assert termo in C1.rigor, termo


def test_resolucoes_tem_status_e_dizem_no_texto():
    rotulo = {
        "validada": "validada",
        "corrigida": "corrigida",
        "pendente_professor": "pendente de confirmação do professor",
    }
    contagem = {s: sum(i["status_resolucao"] == s for i in ITENS.values()) for s in rotulo}
    assert contagem == {"validada": 22, "corrigida": 3, "pendente_professor": 2}
    for i in ITENS.values():
        assert f"Status da resolução: {rotulo[i['status_resolucao']]}" in i["texto"], i["id"]
        assert "gabarito oficial" not in i["texto"].lower()
        if i["status_resolucao"] == "corrigida":
            assert "Divergência" in i["texto"] and "Correções da equipe" in i["texto"], i["id"]
            assert "não é gabarito do professor" in i["texto"], i["id"]


# ---------------------------------------------------------------- contas


def test_funcoes_inequacoes_modulo():
    f = -cos(x) + sin(x) + log(99)
    assert iguais(diff(f, x), sqrt(2) * sin(x + pi / 4))
    assert diff(f, x).subs(x, 0) == 1 and diff(f, x).subs(x, pi) == -1
    g = sp.Abs(x - 5) / (x - 5)
    assert limit(g, x, 5, "+") == 1 and limit(g, x, 5, "-") == -1
    assert limit(3 ** tan(x / 2) * sin(x), x, -pi, "+") == 0


def test_limites_e_continuidade():
    a = sp.symbols("a", positive=True)
    assert iguais(limit((cbrt(a * x + 1) - 1) / x, x, 0), a / 3)
    assert limit(1 / (x - 10) - 20 / (x**2 - 100), x, 10) == Q(1, 20)
    assert limit((x ** Q(1, 5) - 1) / (x ** Q(1, 3) - 1), x, 1) == Q(3, 5)
    assert limit((x ** Q(1, 3) - 1) / (sqrt(x) - 1), x, 1) == Q(2, 3)
    assert sp.floor(2.5) / sp.floor(-2.5) + sp.floor(-2.5) / sp.floor(2.5) == Q(-13, 6)
    c, k, m, n = sp.symbols("c k m n")
    assert solve([c + k - 1, 4 * c + k + 8], [c, k]) == {c: -3, k: 4}
    assert solve([m + 3 + n + 1, 4 * m + 6 + n - (2 * m + n)], [m, n]) == {m: -3, n: -1}
    assert limit((x**2 - 16) / (x**2 - 3 * x - 4), x, 4) == Q(8, 5)
    assert limit((2 * x**2 + 5 * x - 3) / (x**2 - 2 * x - 15), x, -3) == Q(7, 8)
    assert limit(sqrt(1 - x**2), x, 1, "-") == 0


def test_tvi_e_pendencia_do_sinal():
    g = x**2 - cos(x)
    assert g.subs(x, 0) == -1 and g.subs(x, pi) > 0
    assert (4 * x**2 + x + sin(x) - 12).subs(x, 2) > 0
    assert len(sp.real_roots(sp.Poly(x**3 + 15 * x + 1, x))) == 1
    raizes = sp.real_roots(sp.Poly(x**3 - 15 * x + 1, x))
    assert len(raizes) == 3 and all(-4 <= float(r) <= 4 for r in raizes)
    assert [(x**3 - 15 * x + 1).subs(x, v) for v in (-4, 0, 1, 4)] == [-3, 1, -13, 5]


def test_assintotas_e_limites_no_infinito():
    f = (x**2 + x - 2) / (x**3 + 2 * x**2 - 3 * x)
    assert limit(f, x, 1) == Q(3, 4) and limit(f, x, oo) == 0
    assert limit(f, x, 0, "+") in (oo, -oo) and limit(f, x, -3, "+") in (oo, -oo)
    g = x / sqrt(x**2 + 1)
    assert limit(g, x, oo) == 1 and limit(g, x, -oo) == -1
    assert iguais(limit(sqrt(3 * x**2 + 8 * x + 6) - sqrt(3 * x**2 + 3 * x + 1), x, oo), 5 / (2 * sqrt(3)))
    assert limit(sqrt(x**2 + x) - sqrt(x**2 - x), x, oo) == 1
    assert limit(sqrt(9 * x**2 + 2) / (4 * x + 3), x, -oo) == Q(-3, 4)


def test_derivada_pela_definicao():
    f = sqrt(2 * x + 1)
    assert iguais(limit((f.subs(x, x + h) - f) / h, h, 0), 1 / sqrt(2 * x + 1))
    a = limit((x**3 - 27) / (x**2 - 9), x, 3)
    assert a == Q(9, 2) and f.subs(x, a) == sqrt(10) and iguais(diff(f, x).subs(x, a), 1 / sqrt(10))
    g = sqrt(2 * x**2 + 4 * x)
    assert g.subs(x, 2) == 4 and limit((g.subs(x, 2 + h) - 4) / h, h, 0) == Q(3, 2)
    k = 1 / sqrt(x + 2)
    assert limit((k.subs(x, 2 + h) - k.subs(x, 2)) / h, h, 0) == Q(-1, 16)
    r = (2 * x + 1) / (3 * x - 2)
    assert iguais((r.subs(x, 1 + h) - r.subs(x, 1)) / h, -7 / (3 * h + 1))


def test_retas_tangentes():
    a = sp.symbols("a")
    assert diff(sqrt(x + 4), x).subs(x, 5) == Q(1, 6)
    assert solve(3 + (x - 5) / 6 - (-3 - (x - 5) / 6), x) == [-13]
    assert iguais(diff(x ** Q(-1, 3), x).subs(x, 2), -1 / (6 * cbrt(2)))
    assert set(solve(1 - (a**3 + 1) - 3 * a**2 * (1 - a), a)) == {0, Q(3, 2)}
    reta = Q(27, 4) * x - Q(23, 4)
    assert reta.subs(x, 1) == 1 and reta.subs(x, Q(3, 2)) == Q(35, 8) == (x**3 + 1).subs(x, Q(3, 2))


def test_diferenciabilidade():
    f = sp.Abs(x - 5) + sp.Abs(x + 8)
    assert limit((f.subs(x, 5 + h) - f.subs(x, 5)) / h, h, 0, "+") == 2
    assert limit((f.subs(x, 5 + h) - f.subs(x, 5)) / h, h, 0, "-") == 0
    assert limit((f.subs(x, -8 + h) - f.subs(x, -8)) / h, h, 0, "-") == -2
    g = sp.Abs(x - 1) * log(x, 3)
    for lado in "+-":
        assert limit(g.subs(x, 1 + h) / h, h, 0, lado) == 0
    assert limit((exp(h) - 1) / h, h, 0, "+") == 1


def test_regra_da_cadeia_tangente_horizontal_corrigida():
    y = 5 ** (sin(2 * x + 3) ** 2)
    assert iguais(diff(y, x), 2 * log(5) * sin(4 * x + 6) * y)
    pts = {n: ((n * pi - 6) / 4) for n in (1, 2, 3, 4)}
    assert [sp.simplify(y.subs(x, v)) for v in pts.values()] == [5, 1, 5, 1]
    z = sin(4 * x) ** 2 / 8 - sin(3 * x) ** 2 / 6 + sin(99) ** 99
    assert iguais(diff(z, x), cos(7 * x) * sin(x))
    w = log(1 / cos(x) + tan(x)) - x
    assert iguais(diff(w, x), 1 / cos(x) - 1)


def test_derivacao_implicita():
    y = sp.symbols("y")
    F = x**2 + x * y + y**2 - 3
    assert set(solve(F.subs(x, 1), y)) == {1, -2}
    dy = sp.idiff(F, y, x)
    assert dy.subs({x: 1, y: 1}) == -1 and dy.subs({x: 1, y: -2}) == 0
    G = x**2 + x * y + y**2 - 7
    dg = sp.idiff(G, y, x)
    assert {dg.subs({x: s * sqrt(7), y: 0}) for s in (1, -1)} == {-2}
    assert {dg.subs({x: 0, y: s * sqrt(7)}) for s in (1, -1)} == {Q(-1, 2)}
    H = x**3 * y**3 - 2 * x * y - 6 * x - y - 1
    assert solve(H.subs(x, 0), y) == [-1] and sp.idiff(H, y, x).subs({x: 0, y: -1}) == -4


def test_derivadas_log_exponencial_inversas():
    f = x + exp(2 * x)
    assert f.subs(x, 0) == 1 and 1 / diff(f, x).subs(x, 0) == Q(1, 3)
    p = sp.symbols("p", positive=True)
    assert iguais(diff(p ** log(p), p), p ** log(p) * 2 * log(p) / p)
    assert iguais(diff((1 + 1 / p) ** p, p), (1 + 1 / p) ** p * (log(1 + 1 / p) - 1 / (p + 1)))
    assert iguais(diff(log(2) / log(x), x).subs(x, 2), -1 / (2 * log(2)))
    assert diff(-log(x), x).subs(x, 2) == Q(-1, 2)
    g = sp.asin(x) / sqrt(1 - x**2)
    assert iguais(diff(g, x).subs(x, sqrt(2) / 2), 2 + pi / 2)


def test_funcoes_hiperbolicas():
    n = sp.symbols("n", integer=True)
    assert iguais(((cosh(x) - sinh(x)) ** n).rewrite(exp), (cosh(n * x) - sinh(n * x)).rewrite(exp))
    f = sinh(x) + x + 3
    assert iguais(diff(f, x, 2), sinh(x)) and diff(f, x).subs(x, 0) == 2 and f.subs(x, 0) == 3
    assert solve(f - sinh(x), x) == [-3]
    g = sinh(x + cosh(x - 1))
    assert iguais(diff(g, x).subs(x, 1), cosh(2))
    corte_y = sinh(2) - cosh(2)
    corte_x = 1 - sp.tanh(2)
    assert iguais(corte_y.rewrite(exp), -exp(-2)) and iguais(corte_x.rewrite(exp), 2 / (exp(4) + 1))
    assert iguais((-corte_y * corte_x / 2).rewrite(exp), exp(-2) / (exp(4) + 1))
    assert iguais(sp.tanh(log(2)).rewrite(exp), Q(3, 5)) and 2 * log(2) * 2 * 3 == 12 * log(2)


def test_taxas_relacionadas():
    hh, taxa = sp.symbols("hh taxa", positive=True)
    V = 4 * pi / 75 * hh**3  # dV/dt = V'(h) dh/dt
    assert solve(diff(V, hh).subs(hh, 5) * taxa - 25 * pi, taxa) == [Q(25, 4)]
    th = pi / 3
    D = sqrt(16**2 + 8**2 - 2 * 16 * 8 * cos(th))
    assert iguais(D, 8 * sqrt(3))
    assert iguais(256 * sin(th) * (-11 * pi / 360) / (2 * D), -11 * pi / 45)
    assert -Q(10) * 2 / (2 * 40) == Q(-1, 4)
    a = 4 * sqrt(3)
    assert iguais(pi * a**2 / 2 * sqrt(3), 24 * sqrt(3) * pi)


def test_aproximacao_linear():
    L = 16 + Q(1, 6) * (63 - 64)
    assert L == Q(95, 6) and abs(float(63 ** Q(2, 3)) - float(L)) < 1e-3
    assert abs(float(sin(pi / 3 + pi / 360)) - float(sqrt(3) / 2 + pi / 720)) < 1e-4
    assert Q(2, 3) * pi * 1 * 2 * Q(5, 100) == pi / 15
    assert 3 + Q(24, 100) / 6 == Q(304, 100) and abs(float(sqrt(9.24)) - 3.04) < 1e-3


def test_extremos():
    f = x ** Q(1, 3) + x ** Q(4, 3)
    assert solve(diff(f, x), x) == [Q(-1, 4)]
    assert iguais(sp.real_root(Q(-1, 4), 3) + sp.real_root(Q(-1, 4), 3) ** 4, -3 / (4 * cbrt(4)))
    g = 10 * x * (2 - log(x))
    assert solve(diff(g, x), x) == [sp.E] and g.subs(x, sp.E) == 10 * sp.E and g.subs(x, 1) == 20
    assert iguais(g.subs(x, sp.E**2), 0)
    k = cos(x) ** 2 - 2 * sin(x)
    assert [k.subs(x, v) for v in (0, pi / 2, 3 * pi / 2, 2 * pi)] == [1, -2, 2, 1]
    assert (sin(x) ** 4 - sin(x) ** 2).subs(x, pi / 4) == Q(-1, 4)
    s = sin(sp.atan(x))
    assert iguais(s.subs(x, sqrt(3)), sqrt(3) / 2) and iguais(s.subs(x, 2 * sqrt(2)), 2 * sqrt(2) / 3)
    assert solve(diff(x ** (1 / x), x), x) == [sp.E]


def test_tvm_rolle():
    f = (x + 8) / (2 * x - 4)
    assert (f.subs(x, 4) - f.subs(x, 0)) / 4 == Q(5, 4)
    assert iguais(diff(f, x), -20 / (2 * x - 4) ** 2)
    assert sp.real_roots(sp.Poly(x**3 + 8, x)) == [-2]
    assert Q(10 - (-1), 4 - 2) == Q(11, 2) > 5
    assert float(tan(1)) > 1


def test_esboco_de_grafico():
    f = x / (x**2 - 4)
    assert iguais(diff(f, x), -(x**2 + 4) / (x**2 - 4) ** 2)
    assert iguais(diff(f, x, 2), 2 * x * (x**2 + 12) / (x**2 - 4) ** 3)
    g = (4 * x**2 + 8) / (-2 * x - 1)
    assert iguais(g, -2 * x + 1 + 9 / (-2 * x - 1))
    assert set(solve(diff(g, x), x)) == {-2, 1} and g.subs(x, -2) == 8 and g.subs(x, 1) == -4
    assert iguais(diff(g, x), -8 * (x**2 + x - 2) / (2 * x + 1) ** 2)
    assert iguais(diff(g, x, 2), -72 / (2 * x + 1) ** 3)
    assert limit(g - (-2 * x + 1), x, oo) == 0


def test_lhospital():
    assert limit((tan(x) - x) / x**3, x, 0) == Q(1, 3)
    assert limit(x / sp.cot(x) - pi / (2 * cos(x)), x, pi / 2) == -1
    assert limit(((exp(x) + sp.E) / exp(x)) ** exp(x), x, oo) == sp.exp(sp.E)
    assert limit(log(1 + x) / x**2, x, 0, "+") == oo and limit(log(1 + x) / x**2, x, 0, "-") == -oo
    assert float((1 + x).subs(x, -0.01) ** (1 / 0.01**2)) < 1e-40  # lado esquerdo tende a 0
    th = sp.symbols("th", positive=True)
    assert limit(((th - sin(th)) / 2) / (sin(th) * (1 - cos(th)) / 2), th, 0, "+") == Q(1, 3)
    assert limit(sin(x) / (x + 1), x, 0) == 0


def test_otimizacao():
    r, R, H, th, hh, l = sp.symbols("r R H th hh l", positive=True)
    V = pi * H * (r**2 - r**3 / R)
    assert solve(diff(V, r), r) == [2 * R / 3] and iguais(V.subs(r, 2 * R / 3), 4 * pi * R**2 * H / 27)
    A = 400 * sin(th) * (1 + cos(th))
    assert iguais(diff(A, th).subs(th, pi / 3), 0) and iguais(A.subs(th, pi / 3), 300 * sqrt(3))
    assert float(A.subs(th, pi / 4)) < float(A.subs(th, pi / 3))
    Vc = pi / 3 * hh**2 * (2 * R - hh)
    assert solve(diff(Vc, hh), hh) == [4 * R / 3] and iguais(Vc.subs(hh, 4 * R / 3), 32 * pi * R**3 / 81)
    Aw = x**2 / (4 * pi) + ((l - x) / 4) ** 2
    assert iguais(solve(diff(Aw, x), x)[0], pi * l / (pi + 4))
    C = 8 * x**2 + 16000 / x
    assert solve(diff(C, x), x) == [10] and C.subs(x, 10) == 2400 and Q(40000, 100) == 400
    assert C.subs(x, 9) > 2400 and C.subs(x, 11) > 2400


def test_primitivas_e_integral():
    assert iguais(diff((x - 1) ** 3, x, 2), 6 * (x - 1)) and diff((x - 1) ** 3, x).subs(x, 2) == 3
    assert ((x - 1) ** 3).subs(x, 2) == 1
    f = x + 4 / x**2 + 2
    assert iguais(diff(f, x), 1 - 8 / x**3) and f.subs(x, 2) == 5
    c1 = sp.symbols("c1")
    F = x**2 - Q(2, 3) * x**3 + c1 * x + 2
    assert solve(F.subs(x, -1) - 3, c1) == [Q(2, 3)]
    F = F.subs(c1, Q(2, 3))
    gg = (3 * x**2 - 2 * x**3) / 3
    assert iguais(diff(F, x, 2), 2 - 4 * x) and solve(F - gg, x) == [-3] and F.subs(x, -3) == 27
    n, i = sp.symbols("n i", positive=True, integer=True)
    soma = sp.summation((2 * i / n - 2) * 2 / n, (i, 1, n))
    assert limit(soma, n, oo) == -2 and abs(float(soma.subs(n, 1000)) + 1.998) < 1e-9
    assert sp.integrate(x - 2, (x, 1, 5)) == 4 and sp.integrate(sp.Abs(x - 2), (x, 1, 5)) == 5


# ---------------------------------------------------------------- fórmulas, catálogo e restrições

FORMULA = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in ITENS.values():
        assert i["texto"].count("$") % 2 == 0, i["id"]


@pytest.mark.skipif(not shutil.which("node"), reason="node indisponível")
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for i in ITENS.values() for a, b in FORMULA.findall(i["texto"])]
    formulas += [a or b for a, b in FORMULA.findall(C1.rigor)]
    assert len(formulas) >= 100
    katex = (ROOT / "backend/web/vendor/katex/katex.min.js").as_posix()
    script = (
        f"const k=require({json.dumps(katex)});const fs=require('fs');"
        "const erros=[];for(const f of JSON.parse(fs.readFileSync(0,'utf8'))){"
        "try{k.renderToString(f,{throwOnError:true})}catch(e){erros.push(f+' :: '+e.message)}}"
        "console.log(JSON.stringify(erros))"
    )
    r = subprocess.run(
        ["node", "-e", script], input=json.dumps(formulas), capture_output=True, text=True, encoding="utf-8", check=True
    )
    assert json.loads(r.stdout) == []


def test_catalogo_completo_e_coerente():
    obrigatorios = {"id", "nome", "autoria", "url", "idioma", "formato", "isa", "topicos", "licenca", "acesso",
                    "prioridade", "uso", "justificativa"}  # fmt: skip
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f["id"]
        assert f["prioridade"] in ("alta", "media", "referencia")
        assert f["uso"] in ("acervo", "citada", "referencia", "candidato", "indisponivel")
        assert set(f["topicos"]) <= set(C1.assuntos), f["id"]
    assert {x for i in ITENS.values() for x in i["fontes_catalogo"]} <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f["uso"] == "acervo"} == {
        x for i in ITENS.values() if i["natureza"] == "material_da_disciplina" for x in i["fontes_catalogo"]
    }
    for protegido in ("stewart-calculo", "stewart-solucoes", "apostol-calculus", "stewart-calculo-slides-cengage"):
        assert CATALOGO[protegido]["uso"] == "referencia" and "Protegido" in CATALOGO[protegido]["licenca"]
    for protegido in ("stewart-calculo", "stewart-solucoes", "apostol-calculus"):
        assert "Não incluído" in CATALOGO[protegido]["acesso"]
    assert CATALOGO["openstax-calculus-v1"]["uso"] != "acervo"


def test_originais_e_dados_pessoais_fora_do_repositorio():
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()]
    assert not [
        p
        for p in arquivos
        if p.suffix.lower()
        in (".pdf", ".png", ".jpg", ".jpeg", ".heic", ".webp", ".docx", ".doc", ".zip", ".gif", ".pptx")
    ]
    proibidos = re.compile(
        r"(?i)[\w.]+@[\w-]+\.\w+|groups\.google|dropbox|sites\.google|whatsapp|facebook|fb\.com|instagram"
    )
    for p in [*C1.materiais.glob("*.md"), C1.itens, PASTA / "rigor.md", PASTA / "CURADORIA.md", PASTA / "fontes.json"]:
        assert not proibidos.search(p.read_text(encoding="utf-8")), p.name
    for i in ITENS.values():
        assert "http" not in i["texto"], i["id"]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert [i for i in CATALOGO if f"`{i}`" not in curadoria] == []
    assert [i for i in ITENS if f"`{i}`" not in curadoria] == []
    assert "`calc1`" in (ROOT / "docs/DISCIPLINAS.md").read_text(encoding="utf-8")


# ---------------------------------------------------------------- complemento de Ciência da Computação


def test_blocos_de_cc_dizem_curso_e_turma():
    novos = {i for i in ITENS if i.startswith("calc1-cc-")}
    assert novos == {"calc1-cc-limites-potencias-log", "calc1-cc-primitivas-tvm-estimativa",
                     "calc1-cc-otimizacao-cercas", "calc1-cc-esboco-x3-sobre-x2-menos-1"}  # fmt: skip
    for md in C1.materiais.glob("c*-cc-*.md"):
        cab = md.read_text(encoding="utf-8").split("---")[1]
        assert re.search(r"^curso: Ciência da Computação \(UFAL\)", cab, re.M), md.name


def test_contas_das_provas_de_2006_e_2007():
    xp = sp.symbols("x", positive=True)
    assert sp.limit((sp.exp(xp) + xp) ** (1 / xp), xp, 0, "+") == sp.E**2
    assert sp.limit(sp.cos(x) ** (1 / x), x, 0) == 1
    assert sp.limit(sp.sqrt(xp) * sp.log(xp), xp, 0, "+") == 0
    assert sp.limit(xp * sp.log(sp.exp(xp) - 1), xp, 0, "+") == 0
    assert sp.limit(sp.log(xp) / (xp - sp.sqrt(xp)), xp, 1) == 2
    f = x**3 / 6 - sp.sin(x) + sp.pi**2 * x / 8 + sp.pi**2 / 16
    assert sp.simplify(sp.diff(f, x, 2) - (x + sp.sin(x))) == 0
    assert sp.simplify(sp.diff(f, x).subs(x, sp.pi / 2) - sp.pi**2 / 4) == 0 and f.subs(x, 0) == sp.pi**2 / 16
    assert sp.simplify(f.subs(x, sp.pi) - (7 * sp.pi**3 / 24 + sp.pi**2 / 16)) == 0
    g = x**4 / 4 + Q(3, 4)
    assert sp.diff(g, x).subs(x, -1) == -1 and g.subs(x, -1) == 1
    y = -(x**4) / 4 + x**3 / 3 + x**2 / 2 + 2
    assert sp.expand(sp.diff(y, x, 3)) == 2 - 6 * x and y.subs(x, 0) == 2 and sp.diff(y, x).subs(x, 0) == 0
    assert sp.diff(y, x, 2).subs(x, 1) == 0 and y.subs(x, 1) == Q(31, 12)
    assert sp.diff(y, x, 2).subs(x, 0) == 1  # mínimo, não máximo: o enunciado erra
    h = 2 * sp.sqrt(xp) + Q(2, 3) * xp ** Q(3, 2) - Q(8, 3)
    assert sp.simplify(sp.diff(h, xp) - (1 + xp) / sp.sqrt(xp)) == 0 and h.subs(xp, 1) == 0
    assert (2 + 2 * 3, 2 + 3 * 3) == (8, 11)


def test_otimizacao_e_esboco_das_provas_de_2006_e_2007():
    xp = sp.symbols("x", positive=True)
    P = 2 * xp + 400 / xp
    assert solve(sp.diff(P, xp), xp) == [10 * sp.sqrt(2)] and P.subs(xp, 10 * sp.sqrt(2)) == 40 * sp.sqrt(2)
    A = xp * (150 - Q(3, 2) * xp)
    assert solve(sp.diff(A, xp), xp) == [50] and A.subs(xp, 50) == 3750 and 6 * 50 + 4 * 75 == 600
    f = x**3 / (x**2 - 1)
    assert sp.factor(sp.diff(f, x)) == x**2 * (x**2 - 3) / ((x - 1) ** 2 * (x + 1) ** 2)
    assert sp.simplify(sp.diff(f, x, 2) - 2 * x * (x**2 + 3) / (x**2 - 1) ** 3) == 0
    assert sp.limit(f - x, x, sp.oo) == 0 and sp.limit(f, x, 1, "+") == sp.oo and sp.limit(f, x, 1, "-") == -sp.oo
    assert sp.simplify(f.subs(x, sp.sqrt(3)) - 3 * sp.sqrt(3) / 2) == 0
