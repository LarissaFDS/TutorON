"""Acervo de Aprendizagem de Máquina (Ciência da Computação) e conferência das resoluções.

Os blocos parafraseiam as provas e os exemplos dos slides do Prof. Aydano Machado (IC-UFAL). As contas
são refeitas à mão e conferidas com o scikit-learn, sempre com semente fixa.
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

sklearn = pytest.importorskip("sklearn")
from sklearn.cluster import DBSCAN, KMeans  # noqa: E402
from sklearn.datasets import load_iris, make_blobs, make_moons  # noqa: E402
from sklearn.decomposition import PCA  # noqa: E402
from sklearn.feature_selection import mutual_info_classif  # noqa: E402
from sklearn.impute import SimpleImputer  # noqa: E402
from sklearn.metrics import (  # noqa: E402
    accuracy_score,
    adjusted_rand_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score  # noqa: E402
from sklearn.neighbors import KNeighborsClassifier  # noqa: E402
from sklearn.preprocessing import MinMaxScaler  # noqa: E402
from sklearn.tree import DecisionTreeClassifier  # noqa: E402

AM = disciplinas.obter("am")
PASTA = ROOT / "disciplinas/am"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(AM.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "am")
FRONTEIRA = ("prob", "bd")


def buscar(pergunta, d=AM):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo


def test_am_cadastrada_com_acervo_proprio():
    assert AM.nome == "Aprendizagem de Máquina" and AM.itens.exists()
    ids = {c["id"] for c in read_json(AM.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({AM.itens, AM.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(AM.assuntos)
    assert ids == set(TODOS)
    cursos = (ROOT / "disciplinas/cursos.json").read_text(encoding="utf-8")
    # optativa da ênfase Sistemas Inteligentes, fora da matriz de cursos.json (ver CURADORIA.md)
    assert cursos.count('"acervo": "am"') == 0


def test_situacao_da_disciplina():
    assert AM.situacao == "em validação" and AM.em_validacao


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas am --embeddings`."""
    assert disciplinas.registros(AM) == read_json(AM.itens)


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
    corrigidas = [i["id"] for i in TODOS.values() if i.get("status_resolucao") == "corrigida"]
    assert corrigidas == ["am-aprendizagem-por-reforco-q-learning-exploracao-explotacao-equacao"]


def test_sem_dados_pessoais_livros_nem_binarios():
    textos = " ".join(i["texto"] for i in TODOS.values()) + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"matr[ií]cula:? *\d", textos, re.I)
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"].startswith("Protegido") or f["id"] == "turma-resumos-am":
            assert f["uso"] == "referencia", f["id"]
    soltos = [p for p in PASTA.rglob("*") if p.suffix.lower() in (".pdf", ".docx", ".pptx", ".png", ".jpg", ".jpeg")]
    assert not soltos


PERGUNTAS = [
    (
        "O que é aprendizagem de máquina e quando existe a real necessidade de aplicá-la?",
        "am-definicao-quando-usar-supervisionada-nao-supervisionada-reforco",
    ),
    (
        "Quais os três tipos de aprendizagem de máquina?",
        "am-definicao-quando-usar-supervisionada-nao-supervisionada-reforco",
    ),
    (
        "Como se dá o processo de descoberta de conhecimento em banco de dados?",
        "am-kdd-descoberta-de-conhecimento-etapas-mineracao-de-dados",
    ),
    ("Quais as etapas do KDD?", "am-kdd-descoberta-de-conhecimento-etapas-mineracao-de-dados"),
    (
        "Como calcular entropia e ganho de informação no ID3?",
        "am-arvore-de-decisao-id3-entropia-ganho-de-informacao-taxa-de-erro",
    ),
    (
        "Como escolher o valor de k no kNN?",
        "am-k-nn-vizinhos-mais-proximos-distancia-euclidiana-escolha-de-k-normalizacao",
    ),
    (
        "Que metodologia usar para construir e avaliar classificadores?",
        "am-metodologia-avaliar-classificadores-holdout-validacao-cruzada-k-fold-estratificada",
    ),
    (
        "O que é validação cruzada k-fold estratificada?",
        "am-metodologia-avaliar-classificadores-holdout-validacao-cruzada-k-fold-estratificada",
    ),
    (
        "Como calcular precisão e recall na matriz de confusão?",
        "am-matriz-de-confusao-acuracia-precisao-cobertura-recall-f1",
    ),
    (
        "Por que existe a necessidade da redução de dimensionalidade?",
        "am-reducao-de-dimensionalidade-selecao-de-atributos-pca-maldicao-da-dimensionalidade",
    ),
    ("Descreva o algoritmo k-means", "am-agrupamento-k-means-k-medoids-dbscan-algoritmo-passo-a-passo"),
    ("Como funciona o DBSCAN?", "am-agrupamento-k-means-k-medoids-dbscan-algoritmo-passo-a-passo"),
    (
        "Que algoritmo de clustering usar para cada base da figura?",
        "am-qual-algoritmo-de-agrupamento-para-cada-base-formas-ruido",
    ),
    (
        "Descreva o algoritmo Apriori de regras de associação",
        "am-apriori-regras-de-associacao-suporte-confianca-juncao-e-poda",
    ),
    ("O que é lift em regras de associação?", "am-medidas-de-interesse-lift-dependencia-entre-itens-regras-ilusorias"),
    (
        "Explique a aprendizagem por reforço e o Q-learning",
        "am-aprendizagem-por-reforco-q-learning-exploracao-explotacao-equacao",
    ),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Descreva o algoritmo Apriori de regras de associação", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a transformada de Laplace de um degrau?")


# ---------------------------------------------------------------- conferência das resoluções


def _iris():
    x, y = load_iris(return_X_y=True)
    return x, y


def _q_learning(n=5, episodios=300, alfa=0.5, gama=0.9, eps=0.2, semente=0):
    r = random.Random(semente)
    q = [[0.0, 0.0] for _ in range(n)]  # ações: 0 = esquerda, 1 = direita
    for _ in range(episodios):
        s = 0
        while s != n - 1:
            a = r.randrange(2) if r.random() < eps else max((0, 1), key=lambda k: (q[s][k], k))
            s2 = max(0, s - 1) if a == 0 else s + 1
            recompensa = 1.0 if s2 == n - 1 else 0.0
            alvo = recompensa + (0.0 if s2 == n - 1 else gama * max(q[s2]))
            q[s][a] += alfa * (alvo - q[s][a])
            s = s2
    return q


def test_tres_tipos_com_scikit_learn():
    x, y = _iris()
    acc = cross_val_score(KNeighborsClassifier(5), x, y, cv=StratifiedKFold(5, shuffle=True, random_state=0)).mean()
    assert acc > 0.9
    grupos = KMeans(3, n_init=10, random_state=0).fit_predict(x)  # sem usar y
    assert len(set(grupos)) == 3 and adjusted_rand_score(y, grupos) > 0.6
    q = _q_learning()
    assert all(q[s][1] > q[s][0] for s in range(4))


def test_kdd_preprocessamento_muda_o_resultado():
    rng = np.random.default_rng(0)
    x, y = make_blobs(300, centers=2, n_features=2, random_state=0)
    ruido = rng.normal(0, 1000, size=(300, 1))  # atributo irrelevante em escala enorme
    xb = np.hstack([x, ruido])
    cv = StratifiedKFold(5, shuffle=True, random_state=0)
    cru = cross_val_score(KNeighborsClassifier(5), xb, y, cv=cv).mean()
    xn = MinMaxScaler().fit_transform(xb)
    norm = cross_val_score(KNeighborsClassifier(5), xn, y, cv=cv).mean()
    assert norm > cru + 0.1
    faltando = np.array([[1.0, np.nan], [3.0, 4.0], [np.nan, 8.0]])
    cheio = SimpleImputer(strategy="mean").fit_transform(faltando)
    assert not np.isnan(cheio).any() and cheio[0, 1] == 6.0 and cheio[2, 0] == 2.0


def _h(*contagens):
    t = sum(contagens)
    return -sum(c / t * math.log2(c / t) for c in contagens if c)


def test_entropia_ganho_e_erro_ponderado():
    assert round(_h(9, 5), 3) == 0.940
    depois = 8 / 14 * _h(6, 2) + 6 / 14 * _h(3, 3)
    assert round(depois, 3) == 0.892 and round(_h(9, 5) - depois, 3) == 0.048
    erro = sum(e * n / 13 for e, n in [(0, 3), (0, 1), (0.25, 4), (1 / 3, 3), (0, 2)])
    assert math.isclose(erro, 2 / 13) and round(erro, 2) == 0.15
    # a árvore com critério de entropia põe na raiz o atributo de maior ganho
    rng = np.random.default_rng(1)
    bom = rng.integers(0, 2, 200)
    ruim = rng.integers(0, 2, 200)
    y = np.where(rng.random(200) < 0.9, bom, 1 - bom)
    arv = DecisionTreeClassifier(criterion="entropy", max_depth=1, random_state=0).fit(np.c_[ruim, bom], y)
    assert arv.tree_.feature[0] == 1


def test_knn_exemplo_e_escala():
    treino = np.array([[1, 1], [2, 2], [5, 5], [6, 5], [1, 2]])
    classes = np.array(["+", "+", "-", "-", "+"])
    p = np.array([2, 3])
    d = np.sqrt(((treino - p) ** 2).sum(axis=1))
    assert [round(v, 2) for v in d] == [2.24, 1.0, 3.61, 4.47, 1.41]
    viz = np.argsort(d)[:3]
    assert list(viz) == [1, 4, 0]
    assert KNeighborsClassifier(3).fit(treino, classes).predict([p])[0] == "+"
    # um atributo irrelevante em escala de milhares (renda) domina a distância
    renda = np.array([5000, 1000, 1100, 9000, 8000])
    com_renda = np.c_[treino, renda]
    pr = np.r_[p, 1050]
    dr = np.sqrt(((com_renda - pr) ** 2).sum(axis=1))
    assert set(np.argsort(dr)[:3]) == {0, 1, 2} != set(viz)
    normal = MinMaxScaler().fit(np.r_[com_renda, [pr]])
    assert KNeighborsClassifier(3).fit(normal.transform(com_renda), classes).predict(normal.transform([pr]))[0] == "+"


def test_kfold_estratificado():
    x, y = _iris()
    y = np.where(y == 0, 0, 1)  # 50 × 100: desbalanceado
    testados = []
    for treino, teste in StratifiedKFold(5, shuffle=True, random_state=0).split(x, y):
        testados += list(teste)
        assert math.isclose(y[teste].mean(), y.mean(), abs_tol=0.01)
        assert not set(treino) & set(teste)
    assert sorted(testados) == list(range(len(y)))
    rng = np.random.default_rng(0)
    xr, yr = rng.normal(size=(200, 5)), rng.integers(0, 2, 200)  # rótulos aleatórios
    arv = DecisionTreeClassifier(random_state=0)
    assert arv.fit(xr, yr).score(xr, yr) == 1.0
    assert cross_val_score(arv, xr, yr, cv=StratifiedKFold(5, shuffle=True, random_state=0)).mean() < 0.65


def test_matriz_de_confusao():
    real = ["diabetes"] * 60 + ["normal"] * 40
    prev = ["diabetes"] * 40 + ["normal"] * 20 + ["diabetes"] * 10 + ["normal"] * 30
    m = confusion_matrix(real, prev, labels=["diabetes", "normal"])
    assert m.tolist() == [[40, 20], [10, 30]]
    kw = {"pos_label": "diabetes"}
    assert accuracy_score(real, prev) == 0.70
    assert precision_score(real, prev, **kw) == 0.80
    assert round(recall_score(real, prev, **kw), 3) == 0.667
    assert round(f1_score(real, prev, **kw), 3) == 0.727
    assert recall_score(real, prev, pos_label="normal") == 0.75  # especificidade


def test_reducao_de_dimensionalidade():
    x, y = _iris()
    rng = np.random.default_rng(0)
    xr = np.hstack([x, rng.normal(0, 3, size=(len(y), 50))])
    cv = StratifiedKFold(5, shuffle=True, random_state=0)
    so_iris = cross_val_score(KNeighborsClassifier(5), x, y, cv=cv).mean()
    com_ruido = cross_val_score(KNeighborsClassifier(5), xr, y, cv=cv).mean()
    assert com_ruido < so_iris - 0.1
    mi = mutual_info_classif(xr, y, random_state=0)
    assert set(np.argsort(mi)[-4:]) == {0, 1, 2, 3}
    assert PCA(2).fit(x).explained_variance_ratio_.sum() > 0.95


def test_kmeans_passo_a_passo():
    x, _ = make_blobs(200, centers=3, random_state=2)
    c = x[[0, 1, 2]].copy()
    sse_ant = math.inf
    for _ in range(100):
        rotulos = np.argmin(((x[:, None] - c[None]) ** 2).sum(axis=2), axis=1)
        sse = ((x - c[rotulos]) ** 2).sum()
        assert sse <= sse_ant + 1e-9
        novo = np.array([x[rotulos == k].mean(axis=0) for k in range(3)])
        if np.allclose(novo, c):
            break
        c, sse_ant = novo, sse
    sk = KMeans(3, init=x[[0, 1, 2]], n_init=1).fit(x)
    assert adjusted_rand_score(sk.labels_, rotulos) == 1.0
    pts = np.vstack([x, [[100.0, 100.0]]])
    assert DBSCAN(eps=1.5, min_samples=5).fit_predict(pts)[-1] == -1


def test_escolha_por_forma_da_base():
    xb, yb = make_blobs(400, centers=4, cluster_std=0.6, random_state=0)
    xm, ym = make_moons(400, noise=0.05, random_state=0)
    rng = np.random.default_rng(0)
    ruido = rng.uniform(xm.min(0) - 0.5, xm.max(0) + 0.5, size=(40, 2))
    xr = np.vstack([xm, ruido])

    def ari(rot, y):
        return adjusted_rand_score(y, rot)

    assert ari(KMeans(4, n_init=10, random_state=0).fit_predict(xb), yb) > 0.9
    assert ari(DBSCAN(eps=0.2, min_samples=5).fit_predict(xm), ym) > ari(
        KMeans(2, n_init=10, random_state=0).fit_predict(xm), ym
    )
    db = DBSCAN(eps=0.15, min_samples=8).fit_predict(xr)
    km = KMeans(2, n_init=10, random_state=0).fit_predict(xr)
    assert ari(db[:400], ym) > ari(km[:400], ym)
    assert (db[400:] == -1).mean() > 0.7


TRANS = [
    {"pão", "leite"},
    {"pão", "fralda", "cerveja", "ovos"},
    {"leite", "fralda", "cerveja", "refri"},
    {"pão", "leite", "fralda", "cerveja"},
    {"pão", "leite", "fralda", "refri"},
]


def _sup(itens):
    return sum(set(itens) <= t for t in TRANS) / len(TRANS)


def _apriori(supmin):
    itens = sorted(set().union(*TRANS))
    nivel = [(i,) for i in itens if _sup([i]) >= supmin]
    todos = list(nivel)
    while nivel:
        freq = set(nivel)
        cand = [a + (b[-1],) for a in nivel for b in nivel if a[:-1] == b[:-1] and a[-1] < b[-1]]
        cand = [c for c in cand if all(s in freq for s in itertools.combinations(c, len(c) - 1))]
        nivel = [c for c in cand if _sup(c) >= supmin]
        todos += nivel
    return todos


def test_apriori():
    freq = _apriori(0.6)
    assert {f for f in freq if len(f) == 1} == {("cerveja",), ("fralda",), ("leite",), ("pão",)}
    assert {f for f in freq if len(f) == 2} == {
        ("leite", "pão"),
        ("fralda", "pão"),
        ("fralda", "leite"),
        ("cerveja", "fralda"),
    }
    assert _sup(["pão", "leite", "fralda"]) == 0.4
    assert _sup(["cerveja", "fralda"]) == 0.6 and _sup(["cerveja", "fralda"]) / _sup(["cerveja"]) == 1.0
    itens = sorted(set().union(*TRANS))
    forca = {c for k in range(1, 6) for c in itertools.combinations(itens, k) if _sup(c) >= 0.6}
    assert forca == set(freq)


def test_lift_dos_exemplos():
    regras = {  # sup(A), sup(B), sup(regra), conf, em %
        "independente": (8.77, 86.49, 7.58, 86.49),
        "negativa": (12.09, 76.07, 7.35, 60.78),
        "positiva": (32.94, 37.91, 27.01, 82.01),
    }
    for tipo, (sa, sb, sab, conf) in regras.items():
        assert math.isclose(sab / sa * 100, conf, abs_tol=0.5), tipo
        lift = (sab / 100) / ((sa / 100) * (sb / 100))
        classe = "independente" if abs(lift - 1) < 0.05 else ("positiva" if lift > 1 else "negativa")
        assert classe == tipo, (tipo, lift)
    assert round(27.01 / (32.94 * 37.91) * 100, 2) == 2.16


def test_q_learning_corredor():
    gama = 0.9
    q = _q_learning(gama=gama, episodios=500)
    assert all(q[s][1] > q[s][0] for s in range(4))
    assert math.isclose(q[3][1], 1.0, abs_tol=1e-3)
    assert math.isclose(q[2][1], gama, abs_tol=1e-2)
