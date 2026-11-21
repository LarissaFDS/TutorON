"""Acervo de Geometria Analítica e conferência das contas.

Os blocos parafraseiam provas de 2016.2 e 2017.1 da disciplina (fotos não versionadas), com resolução
da equipe TutorON. Cada número que aparece num bloco é recalculado aqui com SymPy.
"""

import json
import re
import shutil
import subprocess

import pytest
import sympy as sp
from sympy import Matrix, sqrt
from sympy import Rational as Q

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

GA = disciplinas.obter("ga")
PASTA = ROOT / "disciplinas/ga"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
ITENS = {i["id"]: i for i in read_json(GA.itens)}
OUTRAS = ("paa", "sd", "oac", "calc3", "prob", "ed", "prog1", "discreta", "fis2", "varcomp")
x, y, z, t = sp.symbols("x y z t", real=True)


def buscar(pergunta, d=GA):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return ITENS[ident]["texto"]


def M(*v):
    return Matrix(v)


def proj(w, u):
    return (w.dot(u) / u.dot(u)) * u


def dist_plano(p, n, d):
    return sp.simplify(abs(n.dot(p) + d) / n.norm())


# ---------------------------------------------------------------- cadastro e acervo


def test_ga_cadastrada_com_acervo_proprio():
    assert GA.nome == "Geometria Analítica" and GA.itens.exists() and GA.indice.exists() and not GA.livro_supabase
    ids = {c["id"] for c in read_json(GA.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({GA.itens, GA.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert all(c["disciplina"] == "ga" for c in read_json(GA.indice)["chunks"])
    assert {i["assunto"] for i in ITENS.values()} == set(GA.assuntos)  # nenhum tópico sem bloco na busca
    assert ids == set(ITENS)


def test_situacao_da_disciplina():
    assert GA.situacao == "MVP" and not GA.em_validacao and not GA.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas ga --embeddings`."""
    gerados = disciplinas.registros(GA)
    assert gerados == read_json(GA.itens)
    assert {c["id"] for c in read_json(GA.indice)["chunks"]} == {
        i["id"] for i in gerados if i["confiabilidade"] in ("media", "alta")
    }


def test_blocos_cabem_no_trecho_e_terminam_com_verificacao():
    for i in ITENS.values():
        assert len(i["texto"]) <= 2200, i["id"]  # backend/rag.py corta acima disso
        assert "**Verificação:**" in i["texto"].strip().splitlines()[-1], i["id"]


def test_nenhuma_nota_da_ia_e_nada_revisado_sem_registro():
    assert not [i for i, x in ITENS.items() if x["natureza"] == "nota_da_equipe_ia"]
    for p in GA.materiais.glob("*.md"):
        cab = p.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, p.name


# ---------------------------------------------------------------- busca e isolamento


@pytest.mark.parametrize(
    "pergunta, aceitos",
    [
        ("Como achar a equação do plano por três pontos?", {"ga-plano-tres-pontos"}),
        ("Como calcular a distância entre duas retas reversas?", {"ga-distancia-retas-reversas"}),
        ("Como identificar uma cônica pela equação?", {"ga-identificar-conicas"}),
        ("Para que serve o produto misto?", {"ga-produto-vetorial-misto", "ga-distancia-ponto-plano-deducao"}),
        ("Como achar o centro e o raio de uma esfera?", {"ga-esferas-equacao"}),
        ("Como calcular a projeção ortogonal de um vetor sobre outro?", {"ga-vetores-decomposicao-projecao"}),
        ("Como achar os focos e as assíntotas de uma hipérbole?", {"ga-hiperbole"}),
        ("O que é uma superfície de revolução?", {"ga-superficies-revolucao"}),
        ("Como encontrar o plano tangente a uma esfera?", {"ga-esfera-plano-tangente"}),
    ],
)
def test_pergunta_de_ga_encontra_bloco_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize("pergunta", ["Qual a capital da França?", "Como declarar um ponteiro em C?"])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


@pytest.mark.parametrize(
    "pergunta",
    [
        "Como achar a equação do plano por três pontos?",
        "Como calcular o produto vetorial?",
        "Qual a distância de um ponto a um plano?",
        "Como calcular o plano tangente?",
        "O que é um vetor normal?",
    ],
)
def test_vocabulario_comum_fica_na_disciplina_escolhida(pergunta):
    """Fronteira com Cálculo 3 (e as demais): cada disciplina busca só no próprio índice, nos dois sentidos."""
    assert all(i.startswith("ga-") for i in buscar(pergunta))
    for d in OUTRAS:
        assert not any(i.startswith("ga-") for i in buscar(pergunta, disciplinas.obter(d)))


def test_rigor_tem_fronteiras_e_formas_da_equacao():
    for termo in ("Cálculo 3", "Álgebra Linear", "vetor diretor", "vetor normal", "paramétrica", "geral",
                  "reduzida", "**Verificação:**", "Não entregue a resolução"):  # fmt: skip
        assert termo in GA.rigor, termo


# ---------------------------------------------------------------- resoluções e correções


def test_resolucoes_tem_status_e_dizem_no_texto():
    rotulo = {
        "validada": "validada",
        "corrigida": "corrigida",
        "pendente_professor": "pendente de confirmação do professor",
    }
    assert all("status_resolucao" in i for i in ITENS.values())
    contagem = {s: sum(i["status_resolucao"] == s for i in ITENS.values()) for s in rotulo}
    assert contagem == {"validada": 25, "corrigida": 1, "pendente_professor": 3}
    for i in ITENS.values():
        assert f"Status da resolução: {rotulo[i['status_resolucao']]}" in i["texto"], i["id"]
        assert "gabarito oficial" not in i["texto"].lower()
        if i["status_resolucao"] == "corrigida":
            assert "Divergência" in i["texto"] and "Correções da equipe" in i["texto"], i["id"]
            assert "não é gabarito do professor" in i["texto"], i["id"]


# ---------------------------------------------------------------- contas


def test_vetores_projecao_forcas_figura():
    w, u = M(7, -1), M(1, -1)
    assert proj(w, u) == M(4, -4) and w - proj(w, u) == M(3, 3)
    w, u = M(5, -2), M(1, -3)
    assert proj(w, u) == M(Q(11, 10), Q(-33, 10)) and w - proj(w, u) == M(Q(39, 10), Q(13, 10))
    a, b = sp.symbols("a b")
    assert sp.solve(list(a * M(-3, -4) + b * M(-1, 2) - M(2, 1)), [a, b]) == {a: Q(-1, 2), b: Q(-1, 2)}
    F, F1, F2 = M(Q(3, 2), sqrt(3) / 2), M(2, 0), M(Q(-1, 2), -sqrt(3) / 2)
    assert F.norm() == sqrt(3)
    assert sp.solve(list(a * F1 + b * F2 - F), [a, b]) == {a: Q(1, 2), b: -1}
    assert sp.solve(list(a * F1 + b * F2 - 2 * F), [a, b]) == {a: 1, b: -2}
    uu, vv = M(3, 0), M(3, 3 * sqrt(3))
    assert uu - vv == M(0, -3 * sqrt(3)) and (uu - vv).norm() ** 2 == 27 == 9 + 36 - 2 * 3 * 6 * Q(1, 2)


def test_vetores_angulos():
    def ang(p, q):
        return float(sp.deg(sp.acos(p.dot(q) / (p.norm() * q.norm()))))

    u, v = M(1, 0), 3 * M(Q(1, 2), sqrt(3) / 2)
    assert (
        (u - 2 * v).dot(u + v) == Q(-37, 2) and (u - 2 * v).norm() ** 2 == 31 and sp.simplify((u + v).norm() ** 2) == 13
    )
    assert abs(ang(u - 2 * v, u + v) - 157.2) < 0.05
    u, v = M(2, 0), M(sqrt(2) / 2, sqrt(2) / 2)
    assert abs(ang(2 * u + v, u - 3 * v) - 101.8) < 0.05


def test_triangulos_e_paralelogramo():
    A, B, C = M(3, 3), M(0, 1), M(1, 6)
    assert (B - A).dot(C - A) == 0
    p = proj(A - B, C - B)
    assert p == M(Q(1, 2), Q(5, 2)) and B + p == M(Q(1, 2), Q(7, 2)) and (B + p - A).dot(C - B) == 0
    A, B, C = M(-2, -3), M(5, 2), M(-1, 3)
    assert {tuple(B + C - A), tuple(A + C - B), tuple(A + B - C)} == {(6, 8), (-8, -2), (4, -4)}
    h = (C - A) - proj(C - A, B - A)
    assert h == M(Q(-5, 2), Q(7, 2)) and sp.simplify(h.norm() * (B - A).norm()) == 37
    assert Matrix([[1, 2], [1, 1]]).det() == -1
    A, B, C = M(1, 1), M(4, 0), M(3, 4)
    angs = []
    for P, R, S in ((A, B, C), (B, A, C), (C, A, B)):
        angs.append(float(sp.deg(sp.acos((R - P).dot(S - P) / ((R - P).norm() * (S - P).norm())))))
    assert [round(a, 1) for a in angs] == [74.7, 57.5, 47.7] and abs(sum(angs) - 180) < 1e-9
    assert proj(C - A, B - A) == Q(3, 10) * M(3, -1) and proj(C - B, B - A) == Q(-7, 10) * M(3, -1)
    assert A + proj(C - A, B - A) == M(Q(19, 10), Q(7, 10))
    assert abs(Matrix([[3, -1], [2, 3]]).det()) / 2 == Q(11, 2)


def test_demonstracoes_vetoriais():
    a, b = sp.symbols("a1 a2", real=True), sp.symbols("b1 b2", real=True)
    va, vb = M(*a), M(*b)
    s, tt = sp.symbols("s tt")
    sol = sp.solve(list(s * (va + vb) - (va + tt * (vb - va))), [s, tt], dict=True)
    assert sol == [{s: Q(1, 2), tt: Q(1, 2)}]
    assert sp.expand((va + vb).dot(va - vb)) == sp.expand(va.dot(va) - vb.dot(vb))
    assert M(1, 1).dot(M(-1, 1)) == 0


def test_retas_no_plano():
    assert M(1, 2).dot(M(2, -1)) == 0 and M(-2, 2).dot(M(1, 1)) == 0
    assert 2 * M(1, 2) - M(1, 1) == M(1, 3)
    assert -2 - 2 + 4 == 0 and -2 - 2 * 2 + 6 == 0
    assert sp.simplify(abs(4 - 2) / sqrt(5)) == 2 / sqrt(5)
    assert Matrix([[3, 2], [4, 9]]).det() == 19
    assert abs(2 * 2 - 3 * 5 - 8) == 19
    s = sp.solve([x - y, 3 * x + 4 * y - 12], [x, y])
    assert s == {x: Q(12, 7), y: Q(12, 7)}

    def ang(p, q):
        return float(sp.deg(sp.acos(abs(p.dot(q)) / (p.norm() * q.norm()))))

    assert round(ang(M(1, -1), M(3, 4)), 2) == 81.87
    assert round(ang(M(1, -1), M(-2, 5)), 1) == 23.2
    assert round(ang(M(2, -1), M(1, -3)), 6) == 45


def test_produto_vetorial_misto_plano_tres_pontos():
    A, B, C, D = M(1, 2, 1), M(2, -1, 3), M(-3, 0, 3), M(4, 2, 2)
    n = (B - A).cross(C - A)
    assert n == M(-2, -10, -14) and n.norm() == 10 * sqrt(3) and abs(n.dot(D - A)) == 20
    A = M(1, 2, 2)
    B = M(1, -1, 3)
    n = (B - A).cross(C - A)
    assert n == M(-1, -4, -12) and n.norm() == sqrt(161) and abs(n.dot(D - A)) == 3
    assert dist_plano(D, n, -n.dot(A)) == 3 / sqrt(161)
    k = sp.symbols("k")
    A, B, C, D = M(1, 1, 1), M(2, -1, 3), M(3, 1, k), M(3, 2, 1)
    assert sp.solve(Matrix.hstack(B - A, C - A, D - A).det(), k) == [Q(9, 5)]
    u, v = M(1, -3, 2), M(-4, -2, 2)
    assert u.cross(v).norm() ** 2 == u.dot(u) * v.dot(v) - u.dot(v) ** 2 == 300
    A, B, C, P = M(1, 2, 2), M(0, -1, 3), M(3, -1, 1), M(4, 2, 3)
    n = (B - A).cross(C - A)
    assert n == M(6, 1, 9) and n.dot(A) == 26 == n.dot(B) == n.dot(C)
    assert dist_plano(P, n, -26) == 27 / sqrt(118) == sp.simplify(abs(n.dot(P - A)) / n.norm())
    r = M(1 - t, 2 + 3 * t, 2 + t)
    assert sp.solve(n.dot(r) - 26, t) == [0]
    A, B, C = M(2, 0, 1), M(0, 1, 0), M(1, 1, 1)
    n = (B - A).cross(C - A)
    assert n == M(1, 1, -1) and n.dot(A) == 1 and dist_plano(M(1, 2, 3), n, -1) == 1 / sqrt(3)
    assert dist_plano(M(1, 4, -1), M(3, -2, 1), -2) == 8 / sqrt(14)
    u = M(1, 2, 2)
    assert sum((c / u.norm()) ** 2 for c in u) == 1


def test_distancia_retas_reversas_cubo():
    a = sp.symbols("a", positive=True)
    d1, d2, w = M(1, 1, 1), M(0, 0, 1), M(a, 0, 0)
    c = d1.cross(d2)
    assert c == M(1, -1, 0) and sp.simplify(abs(c.dot(w)) / c.norm()) == a * sqrt(2) / 2
    seg = M(a, 0, a / 2) - M(a / 2, a / 2, a / 2)
    assert seg.dot(d1) == 0 == seg.dot(d2) and sp.simplify(seg.norm()) == a * sqrt(2) / 2


def test_planos():
    lam = Q(-3, 2)
    assert lam * M(5, 2, 1) == M(Q(-15, 2), -3, Q(-3, 2)) and lam * -4 == 6
    assert 3 * M(1, -1, 2, 3) == M(3, -3, 6, 9)
    r = M(1 - 2 * t, 3 + t, -2 - 2 * t)
    (t0,) = sp.solve(r[0] - r[1] + 2 * r[2] + 3, t)
    assert t0 == Q(-3, 7) and r.subs(t, t0) == M(Q(13, 7), Q(18, 7), Q(-8, 7))
    s, tt = sp.symbols("s tt")
    p = M(1 + 2 * s - tt, -s - 2 * tt, 2 - s + tt)
    assert sp.solve(sp.expand(3 * p[0] - p[1] + p[2] - 1), s) == [Q(-2, 3)]
    reta = p.subs(s, Q(-2, 3))
    assert sp.expand(reta.subs(tt, 0)) == M(Q(-1, 3), Q(2, 3), Q(8, 3))
    assert sp.expand(reta.subs(tt, 1) - reta.subs(tt, 0)) == M(-1, -2, 1)
    n2 = M(2, -1, -1).cross(M(-1, -2, 1))
    assert n2 == M(-3, -1, -5) and M(-1, -2, 1).dot(n2) == 0 == M(-1, -2, 1).dot(M(3, -1, 1))
    assert M(1, -2, 0).dot(M(2, 1, 2)) == 0 == M(0, -2, 1).dot(M(2, 1, 2))


def test_circunferencias_e_esferas():
    for P in (M(8, 6), M(6, 4), M(4, 6)):
        assert (P - M(6, 6)).norm() == 2
    assert sp.simplify(abs(2 * 3 - 3) / sqrt(5)) ** 2 == Q(9, 5)
    c = M(1, 2)
    assert 9 / sqrt(5) > 3
    P = c - 3 / sqrt(5) * M(2, 1)
    assert sp.simplify((P - c).norm()) == 3 and sp.simplify(abs(2 * P[0] + P[1] + 5) / sqrt(5)) == sp.simplify(
        9 / sqrt(5) - 3
    )
    assert sp.expand((x - 4) ** 2 + (y + 3) ** 2 - 25) == x**2 - 8 * x + y**2 + 6 * y
    assert Matrix([[0, -1], [1, 0]]) * M(4, -3) == M(3, 4)  # rotação de pi/2 leva o centro (4, -3) em (3, 4)
    e = x**2 + y**2 + z**2 - 4 * x - 6 * y - 10 * z + 13
    assert sp.expand((x - 2) ** 2 + (y - 3) ** 2 + (z - 5) ** 2 - 25 - e) == 0
    A, B = M(3, -1, 2), M(1, 4, -3)
    assert (A + B) / 2 == M(2, Q(3, 2), Q(-1, 2)) and (B - A).dot(B - A) / 4 == Q(27, 2)
    assert (M(1, 2, 3) - M(Q(3, 2), -2, 0)).dot(M(1, 2, 3) - M(Q(3, 2), -2, 0)) == Q(101, 4)
    assert dist_plano(M(1, 0, 3), M(2, 1, -2), 1) == 1
    cc = sp.symbols("c")
    (c0,) = sp.solve((M(cc, cc, cc) - M(0, 1, -1)).dot(M(2, 3, 1)), cc)
    assert c0 == Q(1, 3) and (M(c0, c0, c0) - M(0, 1, -1)).dot(M(c0, c0, c0) - M(0, 1, -1)) == Q(7, 3)
    # planos tangentes
    C, P = M(Q(3, 2), -2, 0), M(1, 0, sqrt(2))
    assert (P - C).dot(P - C) == Q(25, 4) and 2 * (P - C) == M(-1, 4, 2 * sqrt(2))
    assert sp.simplify(2 * (P - C).dot(P)) == 3
    C, P = M(1, 0, Q(3, 2)), M(0, sqrt(2), 1)
    assert (
        (P - C).dot(P - C) == Q(13, 4)
        and 2 * (P - C) == M(-2, 2 * sqrt(2), -1)
        and sp.simplify(2 * (P - C).dot(P)) == 3
    )
    C, n = M(1, 2, -1), M(2, 1, 2)
    d = sp.Abs(n.dot(C) - 5) / n.norm()
    assert d == 1 and sqrt(4 - d**2) == sqrt(3)
    centro = C - (n.dot(C) - 5) / n.dot(n) * n
    assert centro == M(Q(5, 3), Q(7, 3), Q(-1, 3)) and n.dot(centro) == 5


def test_parabolas():
    e = 2 * ((x - 2) ** 2 + (y - 2) ** 2) - (x + y) ** 2
    assert sp.expand(e) == x**2 - 2 * x * y + y**2 - 8 * x - 8 * y + 16 and e.subs({x: 1, y: 1}) == 0
    a, b, c = sp.symbols("a b c")
    vx = -b / (2 * a)
    assert sp.simplify((a * x**2 + b * x + c).subs(x, vx) - (-(b**2 - 4 * a * c) / (4 * a))) == 0
    assert sp.expand((y - 1) ** 2 - 4 * (x + Q(1, 4)) - (y**2 - 2 * y - 4 * x)) == 0
    assert sp.sqrt((Q(3, 4) - Q(3, 4)) ** 2 + (3 - 1) ** 2) == 2 == 3 / 4 + 5 / 4 - 0  # foco e diretriz x = -5/4
    assert sp.solve(4 - 3 - a * (1 - 2) ** 2, a) == [1]
    # parábola foco (0,0), diretriz y = -2
    assert sp.expand(x**2 + y**2 - (y + 2) ** 2 - (x**2 - 4 * (y + 1))) == 0
    assert sp.solve(x**2 - 4 * (-5 + 1), x) == [] or all(not s.is_real for s in sp.solve(x**2 + 16, x))
    m, k = sp.symbols("m k", real=True)
    disc = sp.discriminant(x**2 - 4 * (m * x + k + 1), x)
    assert sp.expand(disc - 16 * (m**2 + 1 + k)) == 0
    assert sp.solve(x**2 - 4, x) == [-2, 2]


def test_elipses():
    assert sp.expand(sp.Rational(1, 7) * (x - 1) ** 2 + y**2 / 8 - 1).subs({x: 1, y: 2 * sqrt(2)}) == 0
    d = sp.sqrt((1 - 1) ** 2 + (2 * sqrt(2) - 1) ** 2) + sp.sqrt((2 * sqrt(2) + 1) ** 2)
    assert sp.simplify(d) == 4 * sqrt(2)
    a, b = sp.symbols("a b", positive=True)
    assert sp.expand(((a + b) / 2) ** 2 - ((b - a) / 2) ** 2) == a * b
    e = 40 * x**2 - 24 * x * y + 33 * y**2 + 168 * x - 168 * y
    for X, Y in ((0, 0), (Q(-3, 2) - Q(7, 2) * Q(3, 5), 2 - Q(7, 2) * Q(4, 5))):
        assert e.subs({x: X, y: Y}) == 0  # origem e um vértice do eixo maior
    k = sp.symbols("k")
    assert set(sp.solve(Q(4, 9) + k**2 / 4 - 1, k)) == {2 * sqrt(5) / 3, -2 * sqrt(5) / 3}
    kk = 2 * sqrt(5) / 3
    ry = sp.solve(2 * x / 9 + kk * y / 4 - 1, y)[0]
    assert sp.simplify(sp.discriminant(sp.expand(x**2 / 9 + ry**2 / 4 - 1), x)) == 0
    e = 9 * x**2 - 18 * x + 4 * y**2 + 8 * y - 23
    assert sp.expand(9 * (x - 1) ** 2 + 4 * (y + 1) ** 2 - 36 - e) == 0 and e.subs({x: 1, y: 2}) == 0
    f1, f2 = M(1, -1 + sqrt(5)), M(1, -1 - sqrt(5))
    assert sp.simplify((M(3, -1) - f1).norm() + (M(3, -1) - f2).norm()) == 6


def test_hiperboles():
    e = x**2 - 9 * y**2 - 14 + 4 * x + 18 * y
    assert sp.expand((x + 2) ** 2 - 9 * (y - 1) ** 2 - 9 - e) == 0
    e = 4 * x**2 - y**2 - 16 * x - 6 * y + 3
    assert sp.expand(4 * (x - 2) ** 2 - (y + 3) ** 2 - 4 - e) == 0
    u, w = (x + y) / sqrt(2), (y - x) / sqrt(2)
    assert sp.expand(6 * (u**2 / 2 - w**2 / 6 - 1)) == sp.expand(x**2 + 4 * x * y + y**2 - 6)
    P = M(1, 1)
    d = abs((P - M(2, 2)).norm() - (P - M(-2, -2)).norm())
    assert sp.simplify(d) == 2 * sqrt(2) and 8 - 2 == 6


def test_identificar_e_rotacionar_conicas():
    e = 4 * (y - 2) ** 2 - x**2 + 2 * x - 4
    assert sp.expand(4 * (y - 2) ** 2 - (x - 1) ** 2 - 3 - e) == 0
    assert sp.simplify(e.subs({x: 1, y: 2 + sqrt(3) / 2})) == 0
    e = 2 * x**2 + y**2 - x + 4 * y + 1
    assert sp.expand(2 * (x - Q(1, 4)) ** 2 + (y + 2) ** 2 - Q(25, 8) - e) == 0
    assert sp.simplify(e.subs({x: Q(1, 4), y: -2 + 5 / (2 * sqrt(2))})) == 0
    e = 4 * (y - 2) ** 2 + x**2 + 2 * x - 4
    assert sp.expand((x + 1) ** 2 + 4 * (y - 2) ** 2 - 5 - e) == 0
    e = 2 * x**2 - y**2 - x + 4 * y + 1
    assert sp.expand(2 * (x - Q(1, 4)) ** 2 - (y - 2) ** 2 + Q(39, 8) - e) == 0
    R = lambda th: Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])  # noqa: E731
    r30 = R(sp.pi / 6)
    assert sp.simplify(r30 * M(0, 2)) == M(-1, sqrt(3))
    assert sp.simplify(r30 * M(0, sqrt(13))) == M(-sqrt(13) / 2, sqrt(39) / 2)
    assert sp.simplify(r30 * M(3, 2) - M(3 * sqrt(3) / 2 - 1, Q(3, 2) + sqrt(3))) == M(0, 0)
    r45 = R(sp.pi / 4)
    assert sp.simplify(r45 * M(0, 1)) == M(-sqrt(2) / 2, sqrt(2) / 2)
    assert sp.simplify(r45 * M(0, Q(3, 2))) == M(-3 * sqrt(2) / 4, 3 * sqrt(2) / 4)
    xo, yo = R(-sp.pi / 4) * M(x, y)
    nova = sp.expand(2 * (2 * yo - xo**2 - 2))
    alvo = x**2 + 2 * x * y + y**2 + 2 * sqrt(2) * x - 2 * sqrt(2) * y + 4
    assert sp.simplify(nova + alvo) == 0
    assert sp.simplify(alvo.subs({x: -sqrt(2) / 2, y: sqrt(2) / 2})) == 0


def test_quadricas_e_revolucao():
    el = x**2 / 4 + y**2 / 16 + z**2 / 9 - 1
    assert el.subs(x, 0) == y**2 / 16 + z**2 / 9 - 1 and el.subs(y, 0) == x**2 / 4 + z**2 / 9 - 1
    e = y**2 - x**2 + z - 2 * y - 1
    assert sp.expand(z - (2 + x**2 - (y - 1) ** 2) - e) == 0 and e.subs({x: 1, y: 1, z: 3}) == 0
    f = 3 * x**2 + 2 * y**2 + 4 * z**2 - 2 * x * y - 2 * y * z + 2 * x * z
    assert sp.expand((x - y) ** 2 + (y - z) ** 2 + (x + z) ** 2 + x**2 + 2 * z**2 - f) == 0
    A = Matrix([[3, -1, 1], [-1, 2, -1], [1, -1, 4]])
    assert [A[:i, :i].det() for i in (1, 2, 3)] == [3, 5, 17]
    m = sp.symbols("m")
    assert set(sp.solve(m**2 - 1, m)) == {-1, 1}
    rho = sp.symbols("rho", positive=True)
    assert sp.solve(rho**3 - rho, rho) == [1]
    th = sp.symbols("th")
    p = M(sp.cos(th), 1, sp.sin(th))
    assert sp.simplify(p[1] ** 2 - (p[0] ** 2 + p[2] ** 2) ** 3) == 0
    assert sp.simplify(p[1] ** 2 - (p[0] ** 2 + p[2] ** 2)) == 0
    par = (x - 3) ** 2 / Q(25, 8) + (y + 1) ** 2 / 8 - z
    assert par.subs({x: 3 + Q(5, 2), y: -1, z: 2}) == 0 and par.subs({x: 3, y: 3, z: 2}) == 0


# ---------------------------------------------------------------- fórmulas, catálogo e restrições

FORMULA = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in ITENS.values():
        assert i["texto"].count("$") % 2 == 0, i["id"]


@pytest.mark.skipif(not shutil.which("node"), reason="node indisponível")
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for i in ITENS.values() for a, b in FORMULA.findall(i["texto"])]
    formulas += [a or b for a, b in FORMULA.findall(GA.rigor)]
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
        assert set(f["topicos"]) <= set(GA.assuntos), f["id"]
    assert {x for i in ITENS.values() for x in i["fontes_catalogo"]} <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f["uso"] == "acervo"} == {
        x for i in ITENS.values() if i["natureza"] == "material_da_disciplina" for x in i["fontes_catalogo"]
    }
    for protegido in ("steinbruch-winterle", "reis-silva", "boulos-camargo"):
        assert CATALOGO[protegido]["uso"] == "referencia" and "Não incluído" in CATALOGO[protegido]["acesso"]
    assert CATALOGO["ufal-ga-ementa"]["uso"] == "indisponivel"


def test_originais_e_dados_pessoais_fora_do_repositorio():
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()]
    assert not [
        p
        for p in arquivos
        if p.suffix.lower() in (".pdf", ".png", ".jpg", ".jpeg", ".heic", ".webp", ".docx", ".doc", ".zip", ".gif")
    ]
    proibidos = re.compile(r"(?i)[\w.]+@[\w-]+\.\w+|groups\.google|dropbox|sites\.google|whatsapp|chat\.whatsapp")
    for p in [*GA.materiais.glob("*.md"), GA.itens, PASTA / "rigor.md", PASTA / "CURADORIA.md", PASTA / "fontes.json"]:
        assert not proibidos.search(p.read_text(encoding="utf-8")), p.name
    for i in ITENS.values():
        assert "http" not in i["texto"], i["id"]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert [i for i in CATALOGO if f"`{i}`" not in curadoria] == []
    assert [i for i in ITENS if f"`{i}`" not in curadoria] == []
    assert "`ga`" in (ROOT / "docs/DISCIPLINAS.md").read_text(encoding="utf-8")
