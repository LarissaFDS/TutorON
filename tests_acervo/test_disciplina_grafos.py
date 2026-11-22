"""Acervo de Teoria dos Grafos (Ciência da Computação) e conferência das resoluções.

Os blocos parafraseiam a lista 2020.1 do Prof. Rian Gabriel Pinheiro, a 2ª avaliação de 2016.2 do
Prof. Leonardo Viana (IC-UFAL) e os tópicos dos slides da Profa. Patrícia Machado (UFCG). Cada fato
numérico citado nos blocos é conferido aqui com NetworkX ou por força bruta.
"""

import itertools
import random
import re

import pytest

nx = pytest.importorskip("networkx")

from acervo import disciplinas  # noqa: E402
from acervo.common import ROOT, read_json  # noqa: E402
from acervo.retrieval import search  # noqa: E402

GRAFOS = disciplinas.obter("grafos")
PASTA = ROOT / "disciplinas/grafos"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(GRAFOS.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "grafos")
FRONTEIRA = ("ed", "paa", "discreta")


def buscar(pergunta, d=GRAFOS):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def tem(ident, *trechos):
    faltam = [n for n in trechos if n not in TODOS[ident]["texto"]]
    assert not faltam, f"{ident}: {faltam}"


def aleatorios(qtd=40, semente=7):
    rnd = random.Random(semente)
    for _ in range(qtd):
        yield nx.gnp_random_graph(rnd.randint(2, 11), rnd.random(), seed=rnd.randint(0, 10**6))


def colorivel(g, k):
    ordem = sorted(g, key=g.degree, reverse=True)
    cor = {}

    def passo(i):
        if i == len(ordem):
            return True
        v = ordem[i]
        usadas = {cor[u] for u in g[v] if u in cor}
        for c in range(k):
            if c not in usadas:
                cor[v] = c
                if passo(i + 1):
                    return True
                del cor[v]
        return False

    return passo(0)


def cromatico(g):
    return next(k for k in range(1, len(g) + 1) if colorivel(g, k))


def hamiltoniano(g):
    nos = list(g)
    n, inicio = len(nos), nos[0]

    def estende(caminho, vistos):
        if len(caminho) == n:
            return g.has_edge(caminho[-1], inicio)
        return any(estende(caminho + [u], vistos | {u}) for u in g[caminho[-1]] if u not in vistos)

    return estende([inicio], {inicio})


# ---------------------------------------------------------------- cadastro e acervo


def test_grafos_cadastrada_com_acervo_proprio():
    assert GRAFOS.nome == "Teoria dos Grafos" and GRAFOS.itens.exists()
    ids = {c["id"] for c in read_json(GRAFOS.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({GRAFOS.itens, GRAFOS.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(GRAFOS.assuntos)
    assert ids == set(TODOS)
    cursos = (ROOT / "disciplinas/cursos.json").read_text(encoding="utf-8")
    assert cursos.count('"acervo": "grafos"') == 1


def test_situacao_da_disciplina():
    assert GRAFOS.situacao == "em validação" and GRAFOS.em_validacao


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas grafos --embeddings`."""
    assert disciplinas.registros(GRAFOS) == read_json(GRAFOS.itens)


def test_blocos_sao_material_revisavel_e_com_fonte():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert len(t) <= 2200, i["id"]
        assert "**Verificação:**" in t.strip().splitlines()[-1], i["id"]
        assert "não é gabarito do professor" in t and "Status da resolução: validada" in t, i["id"]
        nome_teste = re.search(r"`(test_\w+)`", t.strip().splitlines()[-1]).group(1)
        assert nome_teste in globals(), (i["id"], nome_teste)
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, arq.name
        for f in re.search(r"fontes_catalogo: (.+)", cab).group(1).split(","):
            assert f.strip() in CATALOGO, (arq.name, f)


def test_sem_dados_pessoais_nem_livros():
    textos = " ".join(i["texto"] for i in TODOS.values())
    textos += (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"\b\d{8,}\b", textos)  # matrículas
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"] in ("Protegido", "Trabalho de aluno identificado"):
            assert f["uso"] == "referencia", f["id"]


PERGUNTAS = [
    ("Por que a quantidade de vértices de grau ímpar é par?", "grafos-graus-aperto-de-maos-kn-bipartido"),
    ("Quantos grafos não isomorfos existem com 4 vértices?", "grafos-isomorfismo-onze-grafos-quatro-vertices"),
    ("Como provar que um grafo com grau mínimo 2 tem um ciclo?", "grafos-arvores-conexo-minimo-ciclo-bicoloracao"),
    ("Qual a relação entre conexidade de vértices kappa, de arestas lambda e grau mínimo?", "grafos-conectividade-kappa-lambda-delta-pontes"),
    ("Dá para enfileirar todas as peças do dominó? Tem a ver com grafo euleriano?", "grafos-euleriano-grau-par-ponte-domino"),
    ("Por que o grafo de Petersen não é hamiltoniano?", "grafos-hamiltoniano-petersen-kij-caixeiro"),
    ("Dá para cobrir com dominós um tabuleiro sem as quinas opostas?", "grafos-emparelhamento-tabuleiro-cobertura"),
    ("Todo grafo com 6 vértices tem triângulo ou conjunto independente de tamanho 3?", "grafos-cliques-independentes-ramsey"),
    ("Qual o número cromático do grafo de Petersen?", "grafos-coloracao-vertices-delta-mais-um-petersen"),
    ("Como montar um horário escolar com coloração de arestas?", "grafos-coloracao-arestas-petersen-vizing-horario"),
    ("Por que K3,3 não é planar? O problema das três casas", "grafos-planares-euler-k33-casas"),
    ("Como funciona o Ford-Fulkerson e o corte mínimo?", "grafos-fluxo-maximo-corte-minimo-ford-fulkerson"),
    ("Como fazer ordenação topológica num grafo sem circuitos?", "grafos-digrafos-graus-entrada-saida-aciclicos"),
    ("Como achar a árvore geradora mínima com Kruskal?", "grafos-arvore-geradora-minima-caminho-minimo"),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nao_trazem_blocos_de_grafos():
    for d in map(disciplinas.obter, FRONTEIRA):
        ids = {c["id"] for c in read_json(d.indice)["chunks"]}
        assert ids.isdisjoint(TODOS)
        assert set(buscar("Por que o grafo de Petersen não é hamiltoniano?", d)).isdisjoint(TODOS)
    assert not buscar("Como funciona um flip-flop JK?")


# ---------------------------------------------------------------- conferência das resoluções


def test_graus_e_arestas():
    for g in aleatorios():
        assert sum(d for _, d in g.degree) == 2 * g.number_of_edges()
        assert sum(1 for _, d in g.degree if d % 2) % 2 == 0
    for n in range(1, 9):
        assert nx.complete_graph(n).number_of_edges() == n * (n - 1) // 2
    assert nx.complete_graph(5).number_of_edges() == 10
    assert nx.complete_bipartite_graph(3, 4).number_of_edges() == 12
    for n in range(2, 13):
        assert max(a * (n - a) for a in range(n + 1)) == n * n // 4
    tem("grafos-graus-aperto-de-maos-kn-bipartido", "$K_5$ tem 10 arestas")


def test_onze_grafos_de_quatro_vertices():
    pares = list(itertools.combinations(range(4), 2))
    classes = []
    for mascara in range(2**6):
        g = nx.Graph()
        g.add_nodes_from(range(4))
        g.add_edges_from(p for k, p in enumerate(pares) if mascara >> k & 1)
        if not any(nx.is_isomorphic(g, h) for h in classes):
            classes.append(g)
    assert len(classes) == 11
    por_m = [sum(1 for h in classes if h.number_of_edges() == m) for m in range(7)]
    assert por_m == [1, 1, 2, 3, 2, 1, 1]
    sequencias = {(h.number_of_edges(), tuple(sorted(d for _, d in h.degree))) for h in classes}
    assert len(sequencias) == 11


def test_arvores():
    rnd = random.Random(3)
    for n in range(2, 15):
        t = nx.random_labeled_tree(n, seed=rnd.randint(0, 999)) if hasattr(nx, "random_labeled_tree") else nx.random_tree(n, seed=n)
        assert t.number_of_edges() == n - 1 and nx.is_bipartite(t)
    for g in aleatorios():
        if len(g) and min(d for _, d in g.degree) >= 2:
            assert nx.cycle_basis(g)
        for ciclo in nx.cycle_basis(g):
            h = g.copy()
            h.remove_edge(ciclo[0], ciclo[1])
            assert nx.number_connected_components(h) == nx.number_connected_components(g)


def test_conectividade():
    a = nx.complete_graph(4)
    b = nx.relabel_nodes(nx.complete_graph(4), {0: 3, 1: 4, 2: 5, 3: 6})
    juntos = nx.compose(a, b)  # dividem o vértice 3
    assert (nx.node_connectivity(juntos), nx.edge_connectivity(juntos), min(d for _, d in juntos.degree)) == (1, 3, 3)
    ponte = nx.disjoint_union(nx.complete_graph(4), nx.complete_graph(4))
    ponte.add_edge(0, 4)
    assert (nx.node_connectivity(ponte), nx.edge_connectivity(ponte), min(d for _, d in ponte.degree)) == (1, 1, 3)
    for g in aleatorios():
        if len(g) > 1 and nx.is_connected(g):
            assert nx.node_connectivity(g) <= nx.edge_connectivity(g) <= min(d for _, d in g.degree)


def test_euleriano():
    k7 = nx.complete_graph(7)
    assert k7.number_of_edges() == 21 and nx.is_eulerian(k7)
    for g in aleatorios(80):
        if all(d % 2 == 0 for _, d in g.degree):
            assert not list(nx.bridges(g))
        if len(g) > 1 and nx.is_connected(g):
            h = g.copy()
            impares = [v for v, d in g.degree if d % 2]
            if impares:
                h.add_edges_from(("x", v) for v in impares)
            assert nx.is_eulerian(h)


def test_hamiltoniano():
    assert not hamiltoniano(nx.petersen_graph())
    assert hamiltoniano(nx.complete_bipartite_graph(3, 3))
    assert not hamiltoniano(nx.complete_bipartite_graph(2, 3))
    rnd = random.Random(11)
    for _ in range(10):
        pts = [(rnd.random(), rnd.random()) for _ in range(7)]
        g = nx.complete_graph(7)
        for u, v in g.edges:
            g[u][v]["weight"] = ((pts[u][0] - pts[v][0]) ** 2 + (pts[u][1] - pts[v][1]) ** 2) ** 0.5
        t = nx.minimum_spanning_tree(g)
        ordem = list(nx.dfs_preorder_nodes(t, 0)) + [0]
        atalho = sum(g[a][b]["weight"] for a, b in itertools.pairwise(ordem))
        otimo = min(
            sum(g[a][b]["weight"] for a, b in itertools.pairwise((0, *p, 0))) for p in itertools.permutations(range(1, 7))
        )
        w_t = t.size(weight="weight")
        assert w_t <= otimo + 1e-9 and atalho <= 2 * w_t + 1e-9


def test_emparelhamento():
    g = nx.grid_2d_graph(8, 8)
    g.remove_nodes_from([(0, 0), (7, 7)])
    assert len(g) == 62 and len(nx.max_weight_matching(g, maxcardinality=True)) == 30
    for g in aleatorios(20):
        for r in range(len(g) + 1):
            for s in itertools.combinations(g, r):
                indep = not any(g.has_edge(u, v) for u, v in itertools.combinations(s, 2))
                resto = set(g) - set(s)
                cobre = all(u in resto or v in resto for u, v in g.edges)
                assert indep == cobre


def test_cliques_e_ramsey():
    c5 = nx.cycle_graph(5)
    assert max(len(c) for c in nx.find_cliques(c5)) == 2
    assert max(len(c) for c in nx.find_cliques(nx.complement(c5))) == 2
    arestas = list(itertools.combinations(range(6), 2))
    triangulos = [[arestas.index(p) for p in itertools.combinations(t, 2)] for t in itertools.combinations(range(6), 3)]
    for mascara in range(2**15):
        assert any(len({mascara >> k & 1 for k in t}) == 1 for t in triangulos)
    for g in aleatorios():
        omega = max((len(c) for c in nx.find_cliques(g)), default=0)
        comp = nx.complement(g)
        alfa_comp = max(
            (r for r in range(len(g) + 1) for s in itertools.combinations(comp, r)
             if not any(comp.has_edge(u, v) for u, v in itertools.combinations(s, 2))),
            default=0,
        )
        assert omega == alfa_comp
        if len(g) >= 2:
            graus = [d for _, d in g.degree]
            assert len(set(graus)) < len(graus)


def test_coloracao_vertices():
    p = nx.petersen_graph()
    assert cromatico(p) == 3
    for g in aleatorios():
        cores = nx.greedy_color(g)
        delta = max((d for _, d in g.degree), default=0)
        assert max(cores.values(), default=0) + 1 <= delta + 1
    for m, n in [(2, 3), (4, 5), (8, 8)]:
        grade = nx.grid_2d_graph(m, n)
        assert nx.is_bipartite(grade) and all((i + j) % 2 != (k + w) % 2 for (i, j), (k, w) in grade.edges)


def test_coloracao_arestas():
    assert cromatico(nx.line_graph(nx.petersen_graph())) == 4
    rnd = random.Random(5)
    for _ in range(10):
        b = nx.bipartite.random_graph(4, 5, 0.6, seed=rnd.randint(0, 999))
        if b.number_of_edges():
            delta = max(d for _, d in b.degree)
            assert colorivel(nx.line_graph(b), delta)
    resto = nx.petersen_graph()
    resto.remove_edges_from(nx.max_weight_matching(resto, maxcardinality=True))
    assert sorted(len(c) for c in nx.connected_components(resto)) == [5, 5]


def test_planaridade():
    assert not nx.check_planarity(nx.complete_graph(5))[0]
    assert not nx.check_planarity(nx.complete_bipartite_graph(3, 3))[0]
    assert not nx.check_planarity(nx.petersen_graph())[0]
    assert nx.complete_bipartite_graph(3, 3).number_of_edges() == 9 > 2 * 6 - 4
    opcoes = {"a": (8, 12), "b": (5, 10), "c": (6, 15), "d": (7, 21), "e": (9, 22)}
    assert [k for k, (n, m) in opcoes.items() if m <= 3 * n - 6] == ["a"]
    assert 2 * (3 * 11 - 6) == 54 < 55
    g = nx.disjoint_union(nx.cycle_graph(4), nx.complete_graph(3))
    assert nx.check_planarity(g)[0]
    n, m, c = len(g), g.number_of_edges(), nx.number_connected_components(g)
    # cada componente conexa tem m_i - n_i + 2 faces; a face externa é a mesma para todas
    f_conexas = sum(h.number_of_edges() - len(h) + 2 for h in (g.subgraph(k) for k in nx.connected_components(g))) - (c - 1)
    assert n - m + f_conexas - c == 1


def test_fluxo():
    rede = nx.DiGraph()
    rede.add_edges_from([("s", "A"), ("s", "B"), ("A", "t"), ("B", "t")], capacity=1000)
    rede.add_edge("A", "B", capacity=1)
    valor, _ = nx.maximum_flow(rede, "s", "t")
    corte, _ = nx.minimum_cut(rede, "s", "t")
    assert valor == corte == 2000
    f = {e: 0 for e in rede.edges}
    aumentos = 0
    while sum(f[("s", v)] for v in "AB") < 2000:
        if aumentos % 2 == 0:
            caminho = [("s", "A", 1), ("A", "B", 1), ("B", "t", 1)]
        else:
            caminho = [("s", "B", 1), ("A", "B", -1), ("A", "t", 1)]
        for u, v, sinal in caminho:
            f[(u, v)] += sinal
            assert 0 <= f[(u, v)] <= rede[u][v]["capacity"]
        aumentos += 1
    assert aumentos == 2000
    rnd = random.Random(2)
    for _ in range(20):
        g = nx.gnp_random_graph(8, 0.4, seed=rnd.randint(0, 999), directed=True)
        for u, v in g.edges:
            g[u][v]["capacity"] = rnd.randint(1, 9)
        assert nx.maximum_flow_value(g, 0, 7) == nx.minimum_cut_value(g, 0, 7)


def test_digrafos():
    rnd = random.Random(9)
    for _ in range(20):
        g = nx.gnp_random_graph(9, 0.3, seed=rnd.randint(0, 999), directed=True)
        assert sum(d for _, d in g.in_degree) == g.number_of_edges() == sum(d for _, d in g.out_degree)
        dag = nx.DiGraph((u, v) for u, v in g.edges if u < v)
        dag.add_nodes_from(g)
        ordem = {v: k for k, v in enumerate(nx.topological_sort(dag))}
        assert all(ordem[u] < ordem[v] for u, v in dag.edges)
        assert any(d == 0 for _, d in dag.in_degree)
    with pytest.raises(nx.NetworkXUnfeasible):
        list(nx.topological_sort(nx.DiGraph([(1, 2), (2, 3), (3, 1)])))


def test_agm_e_dijkstra():
    g = nx.Graph()
    g.add_weighted_edges_from([("A", "B", 1), ("B", "C", 2), ("A", "C", 4), ("C", "D", 1), ("B", "D", 5)])
    t = nx.minimum_spanning_tree(g, algorithm="kruskal")
    assert t.size(weight="weight") == 4 and {frozenset(e) for e in t.edges} == {
        frozenset("AB"),
        frozenset("CD"),
        frozenset("BC"),
    }
    assert [nx.dijkstra_path_length(g, "A", v) for v in "BCD"] == [1, 3, 4]
    # peso negativo: fixar B (distância 2) cedo erra, pois A→C→B custa 3 - 2 = 1
    d = nx.DiGraph()
    d.add_weighted_edges_from([("A", "B", 2), ("A", "C", 3), ("C", "B", -2)])
    fixado_cedo = 2
    assert nx.bellman_ford_path_length(d, "A", "B") == 1 < fixado_cedo
