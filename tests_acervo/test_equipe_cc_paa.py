"""Blocos de PAA da turma de Ciência da Computação (e06, e07): as contas e a redução são refeitas aqui.

Ficam em materiais/Equipe com revisado: false, fora da busca de produção até a revisão humana."""

import itertools
import math
import random
import subprocess

from acervo import equipe
from acervo.common import ROOT, read_json
from backend.rag import MAX_CHARS_TRECHO

PASTA = ROOT / equipe.PASTA
CC = {"e06": "e06_cc_assintotica_recorrencia.md", "e07": "e07_cc_np_clique_conjunto_independente.md"}


def corpo(nome):
    return equipe.ler(PASTA / nome)[1]


def test_blocos_de_cc_dizem_curso_e_ficam_fora_da_busca_ate_revisao():
    itens = {i["id"]: i for i in read_json(ROOT / "pipeline/02-acervo/itens.json", [])}
    for ident, nome in CC.items():
        meta, texto, _ = equipe.ler(PASTA / nome)
        assert meta["id"] == ident and meta["revisado"] == "false"
        assert "Curso: Ciência da Computação (UFAL)" in texto and "Status da resolução:" in texto
        assert texto.rstrip().splitlines()[-1].startswith("**Verificação:**")
        assert len(texto) <= MAX_CHARS_TRECHO
        assert itens[ident]["revisado"] is False and itens[ident]["texto"] == texto


def test_nenhum_nome_de_aluno_nem_pdf_da_turma_versionado():
    rastreados = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
    for termo in ("RafaelRocha", "Rafael Rocha", "PAA_Prova_0", "Vanessa", "Davis Fellipe", "Rubens"):
        assert termo not in rastreados
        assert all(termo not in corpo(n) for n in CC.values())


def T(n):
    return 0 if n == 1 else n**3 + T(n // 3)


def test_recorrencia_e_limites_da_prova_1():
    for x in range(1, 6):
        n = 3**x
        assert T(n) * 26 == 27 * (n**3 - 1)
    assert (T(3), T(9)) == (27, 756)
    n = 2**40
    lg = math.log2
    razoes = {
        "a": (n**4 + 100 * n**3) / (n**3 + 100 * n**4),
        "c": 2 * math.log(n, 3) / (3 * lg(n)),
        "e": math.log(n, 3) / math.log(n, 4),
    }
    assert round(razoes["a"], 2) == 0.01 and round(razoes["c"], 2) == 0.42 and round(razoes["e"], 2) == 1.26
    assert (2 / math.sqrt(3)) ** 200 > 1e12  # (b) 2^n / 3^(n/2) cresce sem limite
    m = 4096  # (f) com m = log2 n, log2 m / raiz(m) tende a 0
    assert lg(m) / math.sqrt(m) < 0.2
    assert math.lgamma(10**6 + 1) / (10**6 * math.log(3)) > 10  # (g) log n! / (n log 3) cresce
    texto = corpo(CC["e06"])
    assert "(27/26)(n^3 − 1)" in texto and "T(n) = Θ(n^3)" in texto


def maior(grafo, n, clique):
    for k in range(n, 0, -1):
        for s in itertools.combinations(range(n), k):
            if all((frozenset(p) in grafo) == clique for p in itertools.combinations(s, 2)):
                return k
    return 0


def test_clique_de_g_e_conjunto_independente_do_complemento():
    rnd = random.Random(7)
    pares = lambda n: [frozenset(p) for p in itertools.combinations(range(n), 2)]  # noqa: E731
    for _ in range(40):
        n = rnd.randint(1, 7)
        g = {p for p in pares(n) if rnd.random() < 0.5}
        complemento = set(pares(n)) - g
        assert maior(g, n, True) == maior(complemento, n, False)
        assert set(pares(n)) - complemento == g  # G'' = G
    assert "G'' = G" in corpo(CC["e07"])
