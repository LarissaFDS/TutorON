"""Acervo de Ciência de Dados (Ciência da Computação) e conferência das resoluções.

Os blocos parafraseiam as provas e listas do Prof. Bruno Pimentel (IC-UFAL). As contas são refeitas
à mão e conferidas com NumPy, SciPy e scikit-learn, sempre com semente fixa.
"""

import math
import re

import numpy as np
import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

sklearn = pytest.importorskip("sklearn")
stats = pytest.importorskip("scipy.stats")
from scipy.cluster.hierarchy import linkage  # noqa: E402
from sklearn.cluster import KMeans  # noqa: E402
from sklearn.datasets import load_iris, make_blobs, make_circles, make_classification, make_moons  # noqa: E402
from sklearn.ensemble import RandomForestClassifier  # noqa: E402
from sklearn.feature_extraction.text import CountVectorizer  # noqa: E402
from sklearn.impute import KNNImputer, SimpleImputer  # noqa: E402
from sklearn.linear_model import Lasso, LinearRegression, LogisticRegression, Perceptron  # noqa: E402
from sklearn.metrics import recall_score, silhouette_score  # noqa: E402
from sklearn.model_selection import GridSearchCV, LeaveOneOut, StratifiedKFold, cross_val_score  # noqa: E402
from sklearn.naive_bayes import GaussianNB, MultinomialNB  # noqa: E402
from sklearn.neighbors import KNeighborsClassifier  # noqa: E402
from sklearn.svm import SVC  # noqa: E402
from sklearn.tree import DecisionTreeClassifier  # noqa: E402

CD = disciplinas.obter("cd")
PASTA = ROOT / "disciplinas/cd"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(CD.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "cd")
FRONTEIRA = ("am", "prob")


def buscar(pergunta, d=CD):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo


def test_cd_cadastrada_com_acervo_proprio():
    assert CD.nome == "Ciência de Dados" and CD.itens.exists()
    ids = {c["id"] for c in read_json(CD.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({CD.itens, CD.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(CD.assuntos)
    assert ids == set(TODOS)
    cursos = (ROOT / "disciplinas/cursos.json").read_text(encoding="utf-8")
    # optativa da ênfase Sistemas Inteligentes, fora da matriz de cursos.json (ver CURADORIA.md)
    assert cursos.count('"acervo": "cd"') == 0


def test_situacao_da_disciplina():
    assert CD.situacao == "em validação" and CD.em_validacao


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas cd --embeddings`."""
    assert disciplinas.registros(CD) == read_json(CD.itens)


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
        "Qual a diferença entre Ciência de Dados e Aprendizagem de Máquina?",
        "cd-ciencia-de-dados-definicao-diferenca-aprendizagem-de-maquina-estatistica-mineracao",
    ),
    ("Quais são os 5 Vs do Big Data?", "cd-big-data-3-vs-5-vs-volume-velocidade-variedade-veracidade-valor-desafios"),
    (
        "Quais os desafios do cientista de dados com Big Data?",
        "cd-big-data-3-vs-5-vs-volume-velocidade-variedade-veracidade-valor-desafios",
    ),
    (
        "Crie um vetor com mediana menor que a média",
        "cd-estatistica-em-ciencia-de-dados-media-mediana-assimetria-teste-de-normalidade",
    ),
    (
        "Como remover outliers e tratar valores faltantes no pré-processamento?",
        "cd-pre-processamento-valores-faltantes-duplicatas-ruido-outliers-reducao-de-dados",
    ),
    (
        "Quando usar leave-one-out em vez de k-fold?",
        "cd-avaliacao-de-modelos-overfitting-leave-one-out-k-fold-f-measure-knn-iris",
    ),
    (
        "Como definir o número de grupos no agrupamento hierárquico?",
        "cd-agrupamento-hierarquico-dendrograma-numero-de-grupos-cotovelo-silhueta",
    ),
    ("Compare k-NN e k-means", "cd-knn-versus-k-means-semelhancas-diferencas-deficiencias-do-knn-quando-usar"),
    (
        "Classifique o texto what do you mean com Naive Bayes",
        "cd-naive-bayes-quando-usar-classificacao-de-texto-what-do-you-mean",
    ),
    (
        "Quais as vantagens da árvore de decisão e do Random Forest?",
        "cd-arvore-de-decisao-vantagens-interpretacao-regras-random-forest-importancia",
    ),
    (
        "Quando usar regressão logística em vez de regressão linear múltipla?",
        "cd-regressao-linear-multipla-logistica-quando-usar-selecao-de-variaveis-predicao",
    ),
    (
        "Qual a vantagem do SVM sobre o perceptron?",
        "cd-perceptron-versus-svm-margem-maxima-kernel-redes-neurais-parametros",
    ),
    (
        "Quais os componentes de uma série temporal?",
        "cd-series-temporais-componentes-tendencia-sazonalidade-ciclo-ruido-descoberta-de-informacao",
    ),
    (
        "Como construir um sistema de meta-aprendizado com meta-base e meta-aprendiz?",
        "cd-meta-aprendizado-meta-caracteristicas-meta-base-meta-aprendiz-recomendar-algoritmos",
    ),
    (
        "Quais as seis etapas da visualização de dados para apresentar resultados?",
        "cd-visualizacao-de-dados-seis-etapas-contar-historia-engajamento-grafico",
    ),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Quais são os 5 Vs do Big Data?", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a impedância de um indutor?")


# ---------------------------------------------------------------- conferência das resoluções


def _texto(prefixo):
    return next(i["texto"] for i in TODOS.values() if i["id"].startswith(prefixo))


def test_fundamentos_tem_as_diferencas():
    t = _texto("cd-ciencia-de-dados-definicao")
    for termo in ("Estatística", "Aprendizagem de Máquina", "Mineração de Dados", "Big Data", "domínio"):
        assert termo in t, termo
    b = _texto("cd-big-data")
    for v in ("Volume", "Velocidade", "Variedade", "Veracidade", "Valor", "Desafios"):
        assert v in b, v


def test_media_em_blocos_como_mapreduce():
    v = np.random.default_rng(0).normal(50, 10, 1_000_000)
    parciais = [(b.sum(), len(b)) for b in np.array_split(v, 37)]  # "map" por bloco
    soma = sum(s for s, _ in parciais)  # "reduce"
    n = sum(k for _, k in parciais)
    assert n == len(v) and math.isclose(soma / n, v.mean(), rel_tol=1e-9)


def test_media_mediana_e_normalidade():
    v1, v2 = np.array([1, 2, 3, 4, 100]), np.array([-100, 1, 2, 3, 4])
    assert np.median(v1) == 3 and v1.mean() == 22 and np.median(v1) < v1.mean()
    assert np.median(v2) == 2 and v2.mean() == -18 and np.median(v2) > v2.mean()
    rng = np.random.default_rng(0)
    assert stats.shapiro(rng.normal(0, 1, 200)).pvalue > 0.05
    assert stats.shapiro(rng.exponential(1, 200)).pvalue < 0.05


def test_preprocessamento():
    x = np.array([[1.0, 2.0], [1.0, 2.0], [3.0, 4.0]])
    assert len(np.unique(x, axis=0)) == 2
    faltando = np.array([[1.0, 10.0], [2.0, np.nan], [3.0, 30.0], [10.0, 100.0]])
    media = SimpleImputer(strategy="mean").fit_transform(faltando)
    assert media[1, 1] == pytest.approx(140 / 3)
    knn = KNNImputer(n_neighbors=2).fit_transform(faltando)
    assert knn[1, 1] == pytest.approx(20.0)  # vizinhos mais próximos: as linhas com 1 e 3
    v = np.r_[np.random.default_rng(0).normal(50, 5, 200), 100]
    q1, q3 = np.percentile(v, [25, 75])
    assert 100 > q3 + 1.5 * (q3 - q1)
    assert abs((100 - v.mean()) / v.std(ddof=1)) > 3


def test_knn_iris_f_measure():
    x, y = load_iris(return_X_y=True)
    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    for k in (1, 3, 5, 7, 15):
        f = cross_val_score(KNeighborsClassifier(n_neighbors=k), x, y, cv=cv, scoring="f1_macro")
        assert f.mean() > 0.9, k
    px, py = x[::5], y[::5]
    assert len(px) == 30 and LeaveOneOut().get_n_splits(px) == 30
    assert len(cross_val_score(KNeighborsClassifier(3), px, py, cv=LeaveOneOut())) == 30


def test_numero_de_grupos():
    x, _ = make_blobs(200, centers=[(0, 0), (10, 0), (0, 10), (10, 10)], cluster_std=0.6, random_state=0)
    alturas = linkage(x, method="ward")[:, 2]
    # o maior salto fica entre a junção que deixa 4 grupos e a seguinte
    assert len(alturas) - np.argmax(np.diff(alturas)) == 4
    sil = {k: silhouette_score(x, KMeans(k, n_init=10, random_state=0).fit_predict(x)) for k in range(2, 8)}
    assert max(sil, key=sil.get) == 4


def test_knn_versus_kmeans():
    x, _ = load_iris(return_X_y=True)
    with pytest.raises(TypeError):
        KNeighborsClassifier(3).fit(x)  # supervisionado: precisa de y
    assert KMeans(3, n_init=10, random_state=0).fit(x).cluster_centers_.shape == (3, 4)
    rng = np.random.default_rng(0)
    a = rng.normal(0, 1, (300, 2))
    b = rng.normal(1.5, 1, (300, 2))
    tx, ty = np.r_[a[200:], b[200:]], np.r_[np.zeros(100), np.ones(100)]
    eq = KNeighborsClassifier(15).fit(np.r_[a[:200], b[:200]], np.r_[np.zeros(200), np.ones(200)])
    des = KNeighborsClassifier(15).fit(np.r_[a[:200], b[:15]], np.r_[np.zeros(200), np.ones(15)])
    assert recall_score(ty, des.predict(tx)) < recall_score(ty, eq.predict(tx)) - 0.2


STMT = ["They are novels", "This is how I bought the book", "I like fictions", "This is my book"]
QUESTION = ["have you read this book", "who is the author", "what are the characters", "what is your favorite book"]


def test_naive_bayes_texto():
    pal = {c: " ".join(f).lower().split() for c, f in (("stmt", STMT), ("question", QUESTION))}
    assert len(pal["stmt"]) == 17 and len(pal["question"]) == 18
    v = len(set(pal["stmt"]) | set(pal["question"]))
    assert v == 22

    def verossimilhanca(c):
        return math.prod((pal[c].count(w) + 1) / (len(pal[c]) + v) for w in ("what", "you"))

    assert verossimilhanca("question") == pytest.approx(6 / 1600)
    assert verossimilhanca("stmt") == pytest.approx(1 / 1521)
    vet = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
    x = vet.fit_transform(STMT + QUESTION)
    nb = MultinomialNB(alpha=1.0).fit(x, ["stmt"] * 4 + ["question"] * 4)
    assert len(vet.vocabulary_) == 22
    assert nb.predict(vet.transform(["what do you mean"]))[0] == "question"


def test_arvore_e_random_forest():
    x = np.array([[25, 110], [35, 120], [45, 150], [60, 145], [65, 115], [50, 160]])
    y = ["normal", "normal", "risco", "risco", "normal", "risco"]
    arv = DecisionTreeClassifier(random_state=0).fit(x, y)
    assert arv.score(x, y) == 1.0
    assert arv.tree_.feature[0] == 1 and arv.tree_.threshold[0] == pytest.approx(132.5)
    rng = np.random.default_rng(0)
    xs = rng.normal(size=(500, 5))
    ys = (xs[:, 2] + 0.3 * rng.normal(size=500) > 0).astype(int)
    rf = RandomForestClassifier(200, random_state=0).fit(xs, ys)
    assert np.argmax(rf.feature_importances_) == 2


def test_regressao():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(500, 5))  # colunas 2, 3 e 4 são inúteis
    y = 3 + 2 * x[:, 0] - x[:, 1] + 0.3 * rng.normal(size=500)
    lr = LinearRegression().fit(x, y)
    assert lr.intercept_ == pytest.approx(3, abs=0.1)
    assert lr.coef_[:2] == pytest.approx([2, -1], abs=0.1)
    lasso = Lasso(alpha=0.1).fit(x, y)
    assert np.all(lasso.coef_[2:] == 0) and np.all(lasso.coef_[:2] != 0)
    yb = (x[:, 0] + 0.5 * rng.normal(size=500) > 0).astype(int)
    log = LogisticRegression().fit(x, yb)
    grade = np.zeros((5, 5))
    grade[:, 0] = np.linspace(-2, 2, 5)
    pr = log.predict_proba(grade)[:, 1]
    assert np.all((pr > 0) & (pr < 1)) and np.all(np.diff(pr) > 0)


def test_svm_e_perceptron():
    x, y = make_circles(400, factor=0.3, noise=0.05, random_state=0)
    cv = StratifiedKFold(5, shuffle=True, random_state=0)
    assert cross_val_score(Perceptron(random_state=0), x, y, cv=cv).mean() < 0.7
    assert cross_val_score(SVC(kernel="rbf"), x, y, cv=cv).mean() > 0.95
    grade = GridSearchCV(SVC(), {"C": [0.1, 1, 10, 100], "gamma": [0.01, 0.1, 1]}, cv=cv).fit(x, y)
    assert grade.best_params_["C"] in (0.1, 1, 10, 100) and grade.best_score_ > 0.95


def test_decomposicao():
    t = np.arange(120)
    y = 10 + 0.5 * t + 5 * np.sin(2 * np.pi * t / 12) + np.random.default_rng(0).normal(0, 0.5, 120)
    pesos = np.r_[0.5, np.ones(11), 0.5] / 12  # média móvel centrada 2x12
    tendencia = np.convolve(y, pesos, mode="valid")  # alinhada a t = 6..113
    tt = t[6:-6]
    assert np.polyfit(tt, tendencia, 1)[0] == pytest.approx(0.5, abs=0.05)
    resto = y[6:-6] - tendencia
    sazonal = np.array([resto[(tt % 12) == m].mean() for m in range(12)])
    assert (sazonal.max() - sazonal.min()) / 2 == pytest.approx(5, abs=0.5)


def test_meta_aprendizado():
    meta_x, meta_y = [], []
    cv = StratifiedKFold(5, shuffle=True, random_state=0)
    for s in range(40):
        if s % 2:
            x, y = make_classification(40, 50, n_informative=3, n_redundant=0, random_state=s)
        else:
            x, y = make_moons(300, noise=0.25, random_state=s)
        knn = cross_val_score(KNeighborsClassifier(5), x, y, cv=cv).mean()
        nb = cross_val_score(GaussianNB(), x, y, cv=cv).mean()
        meta_x.append([len(x), x.shape[1], float(np.mean(y))])
        meta_y.append("knn" if knn >= nb else "nb")
    meta_y = np.array(meta_y)
    base = max(np.mean(meta_y == c) for c in set(meta_y))
    acerto = cross_val_score(DecisionTreeClassifier(max_depth=2, random_state=0), meta_x, meta_y, cv=5).mean()
    assert acerto >= base


def test_recebidos_processados():
    recebidos = [160, 184, 241, 149, 180, 161, 132, 202, 160, 139, 149, 177]
    processados = [160, 184, 237, 148, 181, 150, 123, 156, 126, 104, 124, 140]
    dif = [r - p for r, p in zip(recebidos, processados, strict=True)]
    assert max(dif[:5]) <= 4
    assert dif[5:] == [11, 9, 46, 34, 35, 25, 37] and sum(dif[5:]) == 197
