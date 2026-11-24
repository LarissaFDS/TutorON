"""Acervo de Álgebra Linear (ECOM011, Engenharia de Computação; também Ciência da Computação) e conferência.

Os blocos parafraseiam as listas 1 e 2 e os códigos-base em Python da lista 2 do material do 2º período.
Determinantes, postos, dimensões, mudanças de base e os axiomas em NumPy são refeitos aqui.
"""

import re

import numpy as np
import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

ALG = disciplinas.obter("alglin")
PASTA = ROOT / "disciplinas/alglin"
CATALOGO = {f["id"]: f for f in read_json(PASTA / "fontes.json")["fontes"]}
TODOS = {i["id"]: i for i in read_json(ALG.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "alglin")
TEXTO = " ".join(i["texto"] for i in TODOS.values())
M = sp.Matrix


def buscar(pergunta, d=ALG):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo


def test_alglin_cadastrada_com_acervo_proprio():
    assert ALG.nome == "Álgebra Linear" and ALG.itens.exists()
    ids = {c["id"] for c in read_json(ALG.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({ALG.itens, ALG.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(ALG.assuntos)
    assert ids == set(TODOS)


def test_situacao_da_disciplina():
    assert ALG.situacao == "MVP" and not ALG.em_validacao and not ALG.aviso


def test_entra_em_ecom_e_cc():
    reg = next(d for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] == "alglin")
    assert reg["cursos"] == {"ecom": 2, "cc": 3}


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas alglin --embeddings`."""
    assert disciplinas.registros(ALG) == read_json(ALG.itens)


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


def test_livros_protegidos_e_audio_ficam_fora():
    for fid in ("anton-algebra-linear", "anton-solucoes"):
        assert CATALOGO[fid]["uso"] == "referencia" and CATALOGO[fid]["arquivo_local"] is None
    assert not list(PASTA.rglob("*.wav")) and not list(PASTA.rglob("*.pdf"))


def test_sem_dados_pessoais():
    textos = TEXTO + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    # o relatório da lista 2 traz nomes de alunos e do professor: nenhum entra no acervo
    for nome in ("Larissa", "Otávio", "Glauber"):
        assert nome not in TEXTO


def test_busca_acha_o_bloco_certo():
    assert "alglin-lista2-espaco-coluna-mudanca-base" in buscar("matriz de mudança de base rotação 45 graus")[:3]
    assert "alglin-lista2-base-dimensao" in buscar("dimensão da soma e da interseção de subespaços")[:3]
    assert "alglin-lista2-codigo-axiomas-combinacao" in buscar("combinação linear em Python com NumPy")[:3]


# ---------------------------------------------------------------- conferência das resoluções


def test_lista1_axiomas_gerado_li():
    u, v, a = np.array([-1, 2]), np.array([3, 4]), 3

    def prod(a, u):
        return np.array([0, a * u[1]])

    assert (u + v).tolist() == [2, 6] and prod(a, u).tolist() == [0, 6]
    assert prod(1, u).tolist() != u.tolist()
    k = sp.Symbol("k")
    for v1, v2, w, normal, kk in (
        ((-1, 3, -1), (1, -2, 4), (5, k, 11), (10, 3, -1), -13),
        ((1, -2, 0), (2, -2, -1), (2, k, 2), (2, 1, 2), -8),
    ):
        assert list(M(v1).cross(M(v2))) == list(normal)
        assert sp.solve(M([v1, v2, w]).det(), k) == [kk]
    mats = [M([[1, 1], [0, 0]]), sp.eye(2), sp.ones(2)]
    assert M([list(m) for m in mats]).rank() == 3


def test_lista1_subespacos_planos():
    x = sp.Symbol("x")
    f, g = x - sp.Rational(1, 2), x**2 - sp.Rational(1, 3)
    assert sp.integrate(f, (x, 0, 1)) == 0 and sp.integrate(g, (x, 0, 1)) == 0
    assert sp.integrate(f + g, (x, 0, 1)) == 0 and sp.integrate(7 * f, (x, 0, 1)) == 0
    for u, v, n in (((0, 1, -2), (1, 1, 1), (3, -2, -1)), ((-1, 0, 3), (2, -1, 0), (3, 6, 1))):
        assert list(M(u).cross(M(v))) == list(n)
        assert M(n).dot(M(u)) == 0 and M(n).dot(M(v)) == 0
    C = M([[1, 2], [2, 4]])
    A, B = M([[2, -1], [4, -2]]), M([[-6, 3], [0, 0]])
    assert A * C == sp.zeros(2) and B * C == sp.zeros(2) and (A + 5 * B) * C == sp.zeros(2)


def test_lista2_base_dimensao():
    t = sp.Symbol("t")
    base = [1, t, sp.cos(2 * t), sp.exp(3 * t)]
    coords = [(-1, 2, 0, 0), (0, 1, 1, 0), (3, 0, 0, -1), (0, -1, 0, 1)]
    fs = [2 * t - 1, t + sp.cos(2 * t), 3 - sp.exp(3 * t), -t + sp.exp(3 * t)]
    for c, f in zip(coords, fs, strict=True):
        assert sp.simplify(sum(ci * b for ci, b in zip(c, base, strict=True)) - f) == 0
    assert M(coords).det() == 5
    W = M([[2, 0, 0, -2], [2, 0, -2, 0], [8, -2, -4, -2]])
    assert all(sum(r) == 0 for r in W.tolist()) and W.rank() == 3
    n1, n2 = M([1, -2, 3]), M([1, -1, 1])
    assert list(n1.cross(n2)) == [1, 2, 1]
    assert 2 + 2 - (3 - M([n1.T, n2.T]).rank()) == 3
    eqs = M([[1, -1, 1, -1], [2, 1, 2, 1]])
    inter = 4 - eqs.rank()
    assert inter == 2 and 3 + 3 - inter == 4 and (3 + 3 - inter) - inter == 2


def test_lista2_coluna_mudanca_base():
    A = M([[1, 3, 5], [1, 4, 3], [1, 1, 9]])
    B = M([[1, 2, 3], [-2, -3, -4], [7, 12, 17]])
    assert A.rank() == B.rank() == A.row_join(B).rank() == 2
    assert A.rank() + len(A.nullspace()) == 3
    P = M([[1, -1], [1, 1]]) / sp.sqrt(2)
    assert sp.simplify(P.T * P) == sp.eye(2)
    novo = sp.simplify(P.inv() * M([5, 6]))
    assert sp.simplify(novo - M([11 / sp.sqrt(2), 1 / sp.sqrt(2)])) == sp.zeros(2, 1)
    Pc, Q = M([[1, 1], [1, 2]]), M([[2, -1], [-1, 1]])
    assert Pc * Q == sp.eye(2)


def test_codigo_axiomas_combinacao():
    v = [
        np.array([1, 1j, 1], dtype="complex128"),
        np.array([4, 3, 2], dtype="complex128"),
        np.array([2 + 3j, complex(np.sqrt(3), np.pi), 3], dtype="complex128"),
    ]
    betas = [3 + 4j, np.exp(-np.pi / 2) + 0j, -12345 + 28413j]
    for b in betas:
        for g in betas:
            for u in v:
                assert np.allclose((b + g) * u, b * u + g * u)
                assert np.allclose(b * (g * u), (b * g) * u)
    errado = lambda b, u: abs(b) * u  # noqa: E731
    u = v[0]
    assert not np.allclose(errado(1 + 0j + (-1), u), errado(1, u) + errado(-1, u))
    assert np.allclose(v[1] + np.zeros(3) - v[1], 0)

    def combinacao(vetores, alvo):
        V = np.array(vetores, dtype=float).T
        ok = np.linalg.matrix_rank(V) == np.linalg.matrix_rank(np.column_stack([V, alvo]))
        coef = np.linalg.lstsq(V, alvo, rcond=None)[0] if ok else None
        return ok, coef

    ok, c = combinacao([[0, 0, 1], [0, 1, 0], [1, 0, 0]], np.array([1, 2, 3.0]))
    assert ok and np.allclose(c, [3, 2, 1])
    vs = [[3.5, 2.1, 2, 4], [5.25, 3.15, 3.0, 6.0], [4.2, 2.52, 2.4, 4.8], [-4.9, -2.94, -2.8, -5.6]]
    assert np.linalg.matrix_rank(np.array(vs)) == 1
    assert not combinacao(vs, np.array([1, 2, 3, 4.0]))[0]
    a1, a2 = np.array([30000.0, -100]), np.array([10000.0, 50])
    assert np.clip(a1 + a2, -32768, 32767).astype(np.int16).tolist() == [32767, -50]
