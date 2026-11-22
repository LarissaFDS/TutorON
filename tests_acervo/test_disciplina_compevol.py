"""Acervo de Computação Evolucionária (Ciência da Computação) e conferência das resoluções.

Os blocos parafraseiam as apostilas e as atividades da turma 2021.1. Os algoritmos são executados
aqui com semente fixa, em Python puro e NumPy.
"""

import itertools
import math
import random
import re

import numpy as np
import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

CE = disciplinas.obter("compevol")
PASTA = ROOT / "disciplinas/compevol"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(CE.itens)}
OUTRAS = tuple(
    d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "compevol"
)
FRONTEIRA = ("am", "cd")


def buscar(pergunta, d=CE):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo


def test_compevol_cadastrada_com_acervo_proprio():
    assert CE.nome == "Computação Evolucionária" and CE.itens.exists()
    ids = {c["id"] for c in read_json(CE.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({CE.itens, CE.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(CE.assuntos)
    assert ids == set(TODOS)
    cursos = (ROOT / "disciplinas/cursos.json").read_text(encoding="utf-8")
    # optativa da ênfase Sistemas Inteligentes, fora da matriz de cursos.json (ver CURADORIA.md)
    assert cursos.count('"acervo": "compevol"') == 0


def test_situacao_da_disciplina():
    assert CE.situacao == "em validação" and CE.em_validacao


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas compevol --embeddings`."""
    assert disciplinas.registros(CE) == read_json(CE.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert len(t) <= 2200, i["id"]
        ultima = t.strip().splitlines()[-1]
        assert "**Verificação:**" in ultima, i["id"]
        assert "não é gabarito do professor" in t and "Status da resolução:" in t, i["id"]
        assert re.search(r"`(test_\w+)`", ultima).group(1) in globals(), i["id"]
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, arq.name
        for f in re.search(r"fontes_catalogo: (.+)", cab).group(1).split(","):
            assert f.strip() in CATALOGO, (arq.name, f)


def test_sem_dados_pessoais_livros_nem_binarios():
    textos = " ".join(i["texto"] for i in TODOS.values()) + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"matr[ií]cula:? *\d", textos, re.I)
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"].startswith("Protegido"):
            assert f["uso"] == "referencia", f["id"]
    soltos = [p for p in PASTA.rglob("*") if p.suffix.lower() in (".pdf", ".docx", ".pptx", ".png", ".jpg", ".jpeg")]
    assert not soltos


PERGUNTAS = [
    (
        "Como achar o máximo de x sen(10πx) + 1 com algoritmo genético?",
        "compevol-algoritmo-genetico-otimizacao-maximo-global-x-sen-10-pi-x",
    ),
    ("O que é máximo local e máximo global?", "compevol-algoritmo-genetico-otimizacao-maximo-global-x-sen-10-pi-x"),
    (
        "Quantos bits preciso para representar x com 6 casas decimais?",
        "compevol-representacao-binaria-decodificacao-numero-de-bits-precisao",
    ),
    ("Como funciona a seleção por roleta?", "compevol-selecao-roleta-torneio-ranking-elitismo-aptidao-relativa"),
    (
        "Qual a diferença entre seleção por torneio e por roleta?",
        "compevol-selecao-roleta-torneio-ranking-elitismo-aptidao-relativa",
    ),
    (
        "Como funciona o cruzamento de um ponto e a mutação?",
        "compevol-cruzamento-um-ponto-dois-pontos-uniforme-mutacao-bit-taxa",
    ),
    (
        "Quais os passos de um algoritmo genético?",
        "compevol-algoritmo-genetico-completo-python-geracoes-criterio-de-parada",
    ),
    (
        "O que é o teorema dos esquemas?",
        "compevol-teorema-dos-esquemas-ordem-comprimento-definidor-blocos-construtivos",
    ),
    (
        "Como calcular a ordem e o comprimento definidor de um esquema?",
        "compevol-teorema-dos-esquemas-ordem-comprimento-definidor-blocos-construtivos",
    ),
    ("Como otimizar a função F6 de Schaffer?", "compevol-representacao-real-funcao-f6-schaffer-dois-parametros"),
    (
        "Qual a regra do 1/5 nas estratégias evolutivas?",
        "compevol-estrategias-evolutivas-1-mais-1-regra-do-um-quinto-mu-lambda",
    ),
    (
        "Por que o AG escapa de ótimos locais melhor que a subida de encosta?",
        "compevol-ag-versus-subida-de-encosta-otimos-locais-memeticos-ilhas-estado-fixo",
    ),
    (
        "Como resolver o caixeiro-viajante com algoritmo genético?",
        "compevol-caixeiro-viajante-representacao-por-permutacao-cruzamento-ox-mutacao-por-troca",
    ),
    (
        "Qual a diferença entre controle de parâmetros determinístico, adaptativo e autoadaptativo?",
        "compevol-controle-de-parametros-deterministico-adaptativo-autoadaptativo-graficos",
    ),
    (
        "O que é dominância de Pareto em otimização multiobjetivo?",
        "compevol-otimizacao-multiobjetivo-dominancia-de-pareto-frente-soma-ponderada-nsga",
    ),
    (
        "Como fazer alinhamento múltiplo de DNA com algoritmo evolucionário?",
        "compevol-alinhamento-multiplo-de-dna-score-alfa-beta-delta-gaps-algoritmo-evolucionario",
    ),
    (
        "Como evoluir estratégias para o dilema do prisioneiro?",
        "compevol-dilema-do-prisioneiro-estrategias-evoluidas-axelrod-codificacao-70-bits",
    ),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Qual a regra do 1/5 nas estratégias evolutivas?", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a impedância de um indutor?")


# ---------------------------------------------------------------- conferência das resoluções


def f1(x):
    return x * math.sin(10 * math.pi * x) + 1


def test_maximo_de_x_sen():
    x = np.linspace(-1, 2, 3_000_001)
    f = x * np.sin(10 * np.pi * x) + 1
    i = f.argmax()
    assert x[i] == pytest.approx(1.8505, abs=1e-3) and f[i] == pytest.approx(2.8503, abs=1e-3)
    picos = np.flatnonzero((f[1:-1] > f[:-2]) & (f[1:-1] > f[2:])) + 1
    assert len(picos) > 10
    perto = picos[np.abs(x[picos] - 1.65) < 0.05]
    assert len(perto) == 1 and f[perto[0]] == pytest.approx(2.65, abs=0.01)


def _decodifica(bits, a, b):
    return a + (b - a) * int("".join(map(str, bits)), 2) / (2 ** len(bits) - 1)


def test_bits_e_decodificacao():
    valores = 3 * 10**6
    L = math.ceil(math.log2(valores))
    assert L == 22 and 2 ** (L - 1) < valores <= 2**L
    assert _decodifica([1] * 22, -1, 2) == 2 and _decodifica([0] * 22, -1, 2) == -1
    assert _decodifica([1] + [0] * 21, -1, 2) == pytest.approx(0.5, abs=1e-6)

    def gray(n):
        return n ^ (n >> 1)

    assert bin(7 ^ 8).count("1") == 4
    assert all(bin(gray(n) ^ gray(n + 1)).count("1") == 1 for n in range(1000))


def test_roleta_e_torneio():
    crom = ["1100", "0100", "0001", "1110", "0111", "1001"]
    apt = [15 * int(c, 2) - int(c, 2) ** 2 for c in crom]
    assert apt == [36, 44, 14, 14, 56, 54] and sum(apt) == 218
    fatias = [round(100 * a / 218, 1) for a in apt]
    assert fatias == [16.5, 20.2, 6.4, 6.4, 25.7, 24.8]
    r = random.Random(0)
    giros = r.choices(range(6), weights=apt, k=100_000)
    for i, a in enumerate(apt):
        assert giros.count(i) / 1000 == pytest.approx(100 * a / 218, abs=0.5)
    n = 6
    melhor = sum(max(r.randrange(n), r.randrange(n)) == n - 1 for _ in range(100_000)) / 100_000
    assert melhor == pytest.approx(1 - (1 - 1 / n) ** 2, abs=0.01)


def test_cruzamento_e_mutacao():
    p1, p2, k = "00110011", "10110000", 1
    assert (p2[:k] + p1[k:], p1[:k] + p2[k:]) == ("10110011", "00110000")
    r = random.Random(0)
    a, b = [r.randint(0, 1) for _ in range(20)], [r.randint(0, 1) for _ in range(20)]
    filho = [x if r.random() < 0.5 else y for x, y in zip(a, b, strict=True)]
    assert all(g in (x, y) for g, x, y in zip(filho, a, b, strict=True))
    for _ in range(100):
        alfa, x, y = r.random(), r.uniform(-5, 5), r.uniform(-5, 5)
        assert min(x, y) <= alfa * x + (1 - alfa) * y <= max(x, y)
    mutados = [sum(r.random() < 0.01 for _ in range(22)) for _ in range(20_000)]
    assert np.mean(mutados) == pytest.approx(0.22, abs=0.02)
    assert mutados.count(0) / len(mutados) == pytest.approx(0.99**22, abs=0.01)
    assert round(0.99**22, 2) == 0.80


def ag(f, a, b, bits=22, n=50, geracoes=100, pc=0.8, pm=0.01, semente=0, historico=None):
    r = random.Random(semente)

    def dec(c):
        return _decodifica(c, a, b)

    pop = [[r.randint(0, 1) for _ in range(bits)] for _ in range(n)]
    for _ in range(geracoes):
        apt = [f(dec(c)) for c in pop]
        melhor = pop[max(range(n), key=apt.__getitem__)]
        if historico is not None:
            historico.append(max(apt))

        def torneio(pop=pop, apt=apt):
            i, j = r.randrange(n), r.randrange(n)
            return pop[i] if apt[i] > apt[j] else pop[j]

        nova = [melhor[:]]
        while len(nova) < n:
            p1, p2 = torneio()[:], torneio()[:]
            if r.random() < pc:
                k = r.randrange(1, bits)
                p1, p2 = p1[:k] + p2[k:], p2[:k] + p1[k:]
            for c in (p1, p2):
                nova.append([1 - g if r.random() < pm else g for g in c])
        pop = nova[:n]
    x = max(map(dec, pop), key=f)
    return x, f(x)


def test_ag_completo():
    for s in range(5):
        hist = []
        x, fx = ag(f1, -1, 2, semente=s, historico=hist)
        assert fx > 2.84, (s, x, fx)
        assert all(b >= a for a, b in itertools.pairwise(hist))


def test_esquemas():
    h = "*0*1*10*"
    fixas = [i + 1 for i, c in enumerate(h) if c != "*"]
    assert fixas == [2, 4, 6, 7] and len(fixas) == 4 and fixas[-1] - fixas[0] == 5
    casam = [
        "".join(c)
        for c in itertools.product("01", repeat=4)
        if all(p in ("*", b) for p, b in zip("1**0", c, strict=True))
    ]
    assert casam == ["1000", "1010", "1100", "1110"]
    cadeia = "10110010"
    esquemas = {"".join(e) for e in itertools.product(*[(b, "*") for b in cadeia])}
    assert len(esquemas) == 2**8
    # cota do teorema: 10 cópias, aptidão 20% acima da média, pc = 0,8, pm = 0,01
    cota = 10 * 1.2 * (1 - 0.8 * 5 / 7 - 4 * 0.01)
    assert cota == pytest.approx(10 * 1.2 * (1 - 4 / 7 - 0.04)) and 4 < cota < 6


def f6(x, y):
    r2 = x * x + y * y
    return 0.5 - (math.sin(math.sqrt(r2)) ** 2 - 0.5) / (1 + 0.001 * r2) ** 2


def test_funcao_f6():
    assert f6(0, 0) == 1
    assert f6(math.pi, 0) == pytest.approx(0.990, abs=1e-3)
    assert 2**27 < 200 * 10**6 <= 2**28
    r = random.Random(0)
    lim = 100.0
    pop = [(r.uniform(-lim, lim), r.uniform(-lim, lim)) for _ in range(100)]
    for g in range(300):
        apt = [f6(*p) for p in pop]
        nova = [pop[max(range(100), key=apt.__getitem__)]]
        sigma = 10 * 0.98**g + 0.01
        while len(nova) < 100:
            i, j, k, m = (r.randrange(100) for _ in range(4))
            pa = pop[i] if apt[i] > apt[j] else pop[j]
            pb = pop[k] if apt[k] > apt[m] else pop[m]
            alfa = r.random()
            filho = [alfa * u + (1 - alfa) * v for u, v in zip(pa, pb, strict=True)]
            filho = tuple(min(lim, max(-lim, c + r.gauss(0, sigma))) for c in filho)
            nova.append(filho)
        pop = nova
    assert max(f6(*p) for p in pop) > 0.99


def _esfera(v):
    return sum(c * c for c in v)


def test_estrategia_evolutiva():
    r = random.Random(0)
    x, sigma, sucessos, sigmas = [5.0, -3.0], 1.0, 0, []
    for t in range(1, 2001):
        y = [c + r.gauss(0, sigma) for c in x]
        if _esfera(y) < _esfera(x):
            x, sucessos = y, sucessos + 1
        if t % 20 == 0:
            sigma = sigma / 0.82 if sucessos / 20 > 0.2 else sigma * 0.82
            sucessos = 0
            sigmas.append(sigma)
    assert _esfera(x) < 1e-3 and sigmas[-1] < sigmas[0]
    p, s = [3.0, -2.0], 0.5
    for _ in range(300):  # (1+5)-ES maximizando F = -x² - y² + 4
        filhos = [[c + r.gauss(0, s) for c in p] for _ in range(5)]
        p = max([p, *filhos], key=lambda v: 4 - _esfera(v))
        s = max(0.001, 0.98 * s)
    assert 4 - _esfera(p) > 4 - 1e-3


def test_subida_de_encosta_e_ag():
    r = random.Random(0)
    finais = []
    for _ in range(20):
        x = r.uniform(-1, 2)
        while True:
            viz = [v for v in (x - 0.001, x + 0.001) if -1 <= v <= 2]
            melhor = max(viz, key=f1)
            if f1(melhor) <= f1(x):
                break
            x = melhor
        finais.append(f1(x))
    assert sum(v < 2.84 for v in finais) > 10
    assert ag(f1, -1, 2, semente=0)[1] > 2.84
    # memético: o melhor do AG refinado por subida de encosta
    x, _ = ag(f1, -1, 2, geracoes=30, semente=1)
    while f1(x + 1e-5) > f1(x) or f1(x - 1e-5) > f1(x):
        x = x + 1e-5 if f1(x + 1e-5) > f1(x) else x - 1e-5
    assert f1(x) > 2.85


def ox(p1, p2, i, j):
    n = len(p1)
    filho = [None] * n
    filho[i : j + 1] = p1[i : j + 1]
    resto = [c for c in p2[j + 1 :] + p2[: j + 1] if c not in filho]
    for k, c in zip([(j + 1 + t) % n for t in range(n - (j - i + 1))], resto, strict=True):
        filho[k] = c
    return filho


def _comprimento(rota, d):
    return sum(d[rota[k]][rota[(k + 1) % len(rota)]] for k in range(len(rota)))


def test_caixeiro_viajante():
    assert ox([0, 1, 2, 3, 4, 5, 6, 7], [3, 7, 5, 1, 6, 0, 2, 4], 2, 4) == [1, 6, 2, 3, 4, 0, 7, 5]
    r = random.Random(0)
    for _ in range(1000):
        a, b = r.sample(range(8), 8), r.sample(range(8), 8)
        i = r.randrange(8)
        j = r.randrange(i, 8)
        assert sorted(ox(a, b, i, j)) == list(range(8))
    pts = [(r.random(), r.random()) for _ in range(8)]
    d = [[math.dist(p, q) for q in pts] for p in pts]
    otimo = min(_comprimento((0, *p), d) for p in itertools.permutations(range(1, 8)))
    pop = [r.sample(range(8), 8) for _ in range(40)]
    for _ in range(150):
        pop.sort(key=lambda s: _comprimento(s, d))
        nova = [pop[0]]
        while len(nova) < 40:
            pa, pb = (min(r.sample(pop, 2), key=lambda s: _comprimento(s, d)) for _ in range(2))
            i = r.randrange(8)
            j = r.randrange(i, 8)
            f = ox(pa, pb, i, j)
            if r.random() < 0.3:
                i, j = sorted(r.sample(range(8), 2))
                f[i : j + 1] = reversed(f[i : j + 1])
            nova.append(f)
        pop = nova
    assert min(_comprimento(s, d) for s in pop) == pytest.approx(otimo)


def _ee(controle, geracoes=400, semente=0):
    r = random.Random(semente)
    x, sigma, sucessos, sigmas, avaliacoes = [4.0, 4.0], 1.0, 0, [], 0
    tau = 1 / math.sqrt(2)
    for t in range(geracoes):
        if controle == "deterministico":
            sigma = 1.0 * 0.99**t
        if controle == "autoadaptativo":  # (1,10)-EE: cada filho carrega o próprio sigma
            filhos = []
            for _ in range(10):
                s_f = sigma * math.exp(tau * r.gauss(0, 1))
                filhos.append((s_f, [c + r.gauss(0, s_f) for c in x]))
            avaliacoes += 10
            sigma, x = min(filhos, key=lambda f: _esfera(f[1]))
            sigmas.append(sigma)
            continue
        s2 = sigma
        y = [c + r.gauss(0, s2) for c in x]
        avaliacoes += 1
        if _esfera(y) < _esfera(x):
            x, sucessos = y, sucessos + 1
        if controle == "adaptativo" and (t + 1) % 10 == 0:
            sigma = sigma / 0.82 if sucessos / 10 > 0.2 else sigma * 0.82
            sucessos = 0
        sigmas.append(sigma)
    return x, sigmas, avaliacoes


def test_controle_de_parametros():
    _, sig, _ = _ee("deterministico")
    assert sig[100] == pytest.approx(0.99**100)
    for c in ("adaptativo", "autoadaptativo"):
        x, sig, _ = _ee(c)
        assert _esfera(x) < 0.05 and sig[-1] < sig[0], c
    n, t = 50, 30
    acumulado = list(itertools.accumulate([n] * t))
    assert acumulado[-1] == n * t


def domina(a, b):
    return all(x <= y for x, y in zip(a, b, strict=True)) and any(x < y for x, y in zip(a, b, strict=True))


def frentes(pontos):
    restantes, saida = list(pontos), []
    while restantes:
        f = [p for p in restantes if not any(domina(q, p) for q in restantes)]
        saida.append(f)
        restantes = [p for p in restantes if p not in f]
    return saida


def test_multiobjetivo():
    A, B, C, D = (1, 5), (2, 3), (3, 4), (4, 1)
    assert domina(B, C) and not domina(A, B) and not domina(B, A)
    assert frentes([A, B, C, D]) == [[A, B, D], [C]]
    r = random.Random(0)
    pts = [(r.random(), r.random()) for _ in range(50)]
    fs = frentes(pts)
    assert sum(map(len, fs)) == 50
    for k in range(1, len(fs)):
        assert all(any(domina(q, p) for q in fs[k - 1]) for p in fs[k])
    escolhas = {min([A, B, D], key=lambda p, w=w: w * p[0] + (1 - w) * p[1]) for w in (0.1, 0.5, 0.9)}
    assert len(escolhas) > 1


def score(linhas, alfa=1, beta=0, delta=-1):
    x = y = z = 0
    for s, t in itertools.combinations(linhas, 2):
        for a, b in zip(s, t, strict=True):
            if a == "-" and b == "-":
                continue
            if "-" in (a, b):
                z += 1
            elif a == b:
                x += 1
            else:
                y += 1
    return x, y, z, alfa * x + beta * y + delta * z


def test_alinhamento_score():
    linhas = ["ACGT", "A-GT", "AC-T"]
    assert score(linhas) == (8, 0, 4, 4)
    assert [s.replace("-", "") for s in linhas] == ["ACGT", "AGT", "ACT"]


def test_dilema_do_prisioneiro():
    assert 4**3 + 6 == 70
    pag = {("C", "C"): 3, ("C", "D"): 0, ("D", "C"): 5, ("D", "D"): 1}

    def olho_por_olho(outro):
        return outro[-1] if outro else "C"

    def sempre_trair(_):
        return "D"

    def jogar(e1, e2, rodadas=200):
        h1, h2, p1, p2 = [], [], 0, 0
        for _ in range(rodadas):
            a, b = e1(h2), e2(h1)
            h1.append(a)
            h2.append(b)
            p1, p2 = p1 + pag[a, b], p2 + pag[b, a]
        return p1, p2

    assert jogar(olho_por_olho, olho_por_olho) == (600, 600)
    assert jogar(sempre_trair, olho_por_olho) == (204, 199)
