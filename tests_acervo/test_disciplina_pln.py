"""Acervo de Processamento de Linguagem Natural (Ciência da Computação) e conferência dos exemplos.

Os blocos parafraseiam as listas 1 a 6 do Prof. Thales Vieira (IC-UFAL). Os exemplos parecidos são
conferidos com `re`, NumPy e scikit-learn, sempre com semente fixa.
"""

import re
from collections import Counter

import numpy as np
import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

sklearn = pytest.importorskip("sklearn")
from sklearn.cluster import KMeans  # noqa: E402
from sklearn.datasets import make_blobs  # noqa: E402
from sklearn.decomposition import NMF, PCA, LatentDirichletAllocation, TruncatedSVD  # noqa: E402
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.manifold import TSNE, trustworthiness  # noqa: E402
from sklearn.metrics import (  # noqa: E402
    accuracy_score,
    adjusted_rand_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    silhouette_score,
)
from sklearn.metrics.pairwise import cosine_similarity  # noqa: E402
from sklearn.model_selection import train_test_split  # noqa: E402
from sklearn.naive_bayes import MultinomialNB  # noqa: E402
from sklearn.pipeline import make_pipeline  # noqa: E402
from sklearn.svm import LinearSVC  # noqa: E402

PLN = disciplinas.obter("pln")
PASTA = ROOT / "disciplinas/pln"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(PLN.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "pln")
FRONTEIRA = ("am", "cd")


def buscar(pergunta, d=PLN):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo


def test_pln_cadastrada_com_acervo_proprio():
    assert PLN.nome == "Processamento de Linguagem Natural" and PLN.itens.exists()
    ids = {c["id"] for c in read_json(PLN.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({PLN.itens, PLN.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(PLN.assuntos)
    assert ids == set(TODOS)
    cursos = (ROOT / "disciplinas/cursos.json").read_text(encoding="utf-8")
    # eletiva de CC, fora da matriz de cursos.json (ver CURADORIA.md)
    assert cursos.count('"acervo": "pln"') == 0


def test_situacao_da_disciplina():
    assert PLN.situacao == "em validação" and PLN.em_validacao


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas pln --embeddings`."""
    assert disciplinas.registros(PLN) == read_json(PLN.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert len(t) <= 2200, i["id"]
        ultima = t.strip().splitlines()[-1]
        assert "**Verificação:**" in ultima, i["id"]
        assert "não é gabarito do professor" in t and "Status da resolução:" in t, i["id"]
        assert "avaliativas" in t, i["id"]
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
        "Como validar o formato de um CPF com expressão regular?",
        "pln-expressoes-regulares-padroes-cpf-letras-minusculas-underscore-validacao",
    ),
    (
        "Como usar grupos nomeados para extrair campos de um endereço com regex?",
        "pln-expressoes-regulares-extrair-campos-grupos-nomeados-endereco-url-referencia-apa",
    ),
    (
        "Como extrair todas as URLs de um texto?",
        "pln-expressoes-regulares-extrair-campos-grupos-nomeados-endereco-url-referencia-apa",
    ),
    (
        "Como tokenizar os textos e criar o vetor de contagens bag-of-words?",
        "pln-pre-processamento-minusculas-pontuacao-numeros-tokenizacao-bag-of-words-frequentes",
    ),
    (
        "Qual a diferença entre stemização e lematização?",
        "pln-stopwords-rotulacao-pos-stemizacao-lematizacao-comparar-frequencias",
    ),
    (
        "Como achar o documento mais parecido com similaridade do cosseno e TF-IDF?",
        "pln-similaridade-do-cosseno-countvectorizer-tf-idf-documento-mais-parecido",
    ),
    (
        "Como treinar regressão logística e Naive Bayes para classificar textos?",
        "pln-classificacao-de-textos-regressao-logistica-naive-bayes-matriz-de-confusao-70-30",
    ),
    (
        "Como comparar LDA, SVD e NMF na modelagem de tópicos?",
        "pln-modelagem-de-topicos-lda-svd-lsa-nmf-numero-de-topicos-palavras-relevantes",
    ),
    (
        "Como aplicar PCA preservando 95% da variância e o método do cotovelo no k-means?",
        "pln-agrupamento-de-textos-pca-95-por-cento-variancia-k-means-metodo-do-cotovelo",
    ),
    (
        "Qual a diferença entre t-SNE e UMAP?",
        "pln-projecao-multidimensional-t-sne-umap-visualizar-grupos-tempo-e-qualidade",
    ),
    (
        "Como achar as palavras mais parecidas com word2vec?",
        "pln-word2vec-palavras-mais-parecidas-buscador-de-documentos-distancia-media-doc2vec",
    ),
    (
        "Como treinar uma LSTM para gerar texto prevendo a próxima palavra?",
        "pln-redes-neurais-para-texto-embedding-convolucional-lstm-geracao-de-texto-proxima-palavra",
    ),
    (
        "Como extrair entidades de pessoa e lugar com spaCy?",
        "pln-spacy-etiquetas-pos-entidades-nomeadas-pessoa-lugar-contar-uma-vez-por-documento",
    ),
    (
        "Como funciona o modelo seq2seq de tradução com codificador e decodificador?",
        "pln-traducao-seq2seq-codificador-decodificador-lstm-nivel-de-caractere-teacher-forcing",
    ),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Como extrair entidades de pessoa e lugar com spaCy?", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a impedância de um indutor?")


# ---------------------------------------------------------------- conferência dos exemplos


def test_regex_padroes():
    def maiusculas_hifen(s):
        return re.search(r"[A-Z]+-", s) is not None

    def cep_valido(s):
        return re.fullmatch(r"\d{5}-?\d{3}", s) is not None

    assert maiusculas_hifen("ABC-def") and not maiusculas_hifen("abc-")
    assert cep_valido("57002-220") and cep_valido("57002220")
    for ruim in ("5700-2220", "57002-22", "57002-2200", "5700a-220", "57002_220"):
        assert not cep_valido(ruim), ruim


AGENDA = re.compile(
    r"(?P<evento>[^,]+), sala (?P<sala>\d+)"
    r"(?:, bloco (?P<bloco>\w+))?"
    r", (?P<hora>\d{1,2}h\d{2})\. (?P<cidade>[^,]+), (?P<uf>[A-Z]{2})\.",
    re.I,
)


def test_regex_extracao():
    m = AGENDA.fullmatch("Reunião, sala 12, bloco B, 14h30. Maceió, AL.")
    assert m.groupdict() == {
        "evento": "Reunião",
        "sala": "12",
        "bloco": "B",
        "hora": "14h30",
        "cidade": "Maceió",
        "uf": "AL",
    }
    m = AGENDA.fullmatch("Aula, SALA 3, 8h00. São Paulo, SP.")
    assert m["bloco"] is None and m["cidade"] == "São Paulo"
    assert AGENDA.fullmatch("Reunião às 14h30 em Maceió") is None
    texto = "Veja https://ufal.br/ic e http://exemplo.com/a?b=1."
    urls = [u.rstrip(".") for u in re.findall(r"https?://[^\s]+", texto)]
    assert urls == ["https://ufal.br/ic", "http://exemplo.com/a?b=1"]


TEXTOS = ["O gato subiu.", "O cão e o gato!", "Em 2021 o cão dormiu."]


def limpa(t):
    t = re.sub(r"\w*\d\w*", " ", t).lower()
    return re.sub(r"[^\w\s]", " ", t)


def test_preprocessamento_bow():
    tokens = [limpa(t).split() for t in TEXTOS]
    assert tokens == [["o", "gato", "subiu"], ["o", "cão", "e", "o", "gato"], ["em", "o", "cão", "dormiu"]]
    vocab = sorted({w for t in tokens for w in t})
    assert vocab == ["cão", "dormiu", "e", "em", "gato", "o", "subiu"]
    assert [tokens[1].count(w) for w in vocab] == [1, 0, 1, 0, 1, 2, 0]
    cv = CountVectorizer(preprocessor=limpa, token_pattern=r"(?u)\b\w+\b")
    x = cv.fit_transform(TEXTOS)
    assert list(cv.get_feature_names_out()) == vocab
    assert x.toarray()[1].tolist() == [1, 0, 1, 0, 1, 2, 0]
    freq = dict(zip(vocab, x.sum(axis=0).A1.tolist(), strict=True))
    assert max(freq, key=freq.get) == "o" and freq["o"] == 4 and freq["gato"] == freq["cão"] == 2
    assert [len(t) for t in TEXTOS] == [13, 15, 21]


def test_stopwords_e_stem():
    stop = {"o", "e", "os", "para"}
    tokens = "o gato e os gatos correram para o gato".split()
    assert Counter(tokens)["gato"] == 2
    sem = [t for t in tokens if t not in stop]
    assert sem == ["gato", "gatos", "correram", "gato"]

    def stem_plural(w):
        return w[:-1] if w.endswith("s") and len(w) > 3 else w

    contagem = Counter(map(stem_plural, sem))
    assert contagem == {"gato": 3, "correram": 1} and not stop & set(contagem)


def test_cosseno_count_tfidf():
    docs = ["futebol gol time gol", "time jogo campeonato", "futebol gol goleiro"]
    for vet in (CountVectorizer(), TfidfVectorizer()):
        s = cosine_similarity(vet.fit_transform(docs))
        assert s[0, 0] == pytest.approx(1)
        np.fill_diagonal(s, -1)  # o próprio documento não conta
        assert s[0].argmax() == 2
    cont = CountVectorizer().fit_transform(docs).toarray()
    a, c = cont[0], cont[2]
    assert cosine_similarity(cont)[0, 2] == pytest.approx(a @ c / (np.linalg.norm(a) * np.linalg.norm(c)))
    assert cosine_similarity(cont)[0, 2] == pytest.approx(0.707, abs=1e-3)
    tf = cosine_similarity(TfidfVectorizer().fit_transform(docs))
    assert tf[0, 2] == pytest.approx(0.634, abs=1e-3) and tf[0, 1] == pytest.approx(0.193, abs=1e-3)
    assert cosine_similarity(cont)[0, 1] == pytest.approx(0.236, abs=1e-3)
    tv = TfidfVectorizer().fit(["casa bola", "casa dedo", "casa fio"])
    assert tv.idf_[tv.vocabulary_["casa"]] == pytest.approx(1.0)


ESPORTE = [
    "o time venceu o jogo",
    "gol no fim da partida",
    "o técnico escalou o time",
    "torcida lotou o estádio",
    "o atacante marcou um gol",
    "campeonato terminou com vitória",
    "goleiro defendeu o pênalti",
    "partida de futebol no estádio",
    "time perdeu o campeonato",
    "jogador fez gol de cabeça",
]
POLITICA = [
    "o senado aprovou a lei",
    "deputado votou contra o projeto",
    "eleição para prefeito",
    "ministro anunciou o orçamento",
    "governo enviou projeto de lei",
    "câmara rejeitou a proposta",
    "candidato fez campanha na eleição",
    "presidente sancionou a lei",
    "partido lançou candidato",
    "votação do orçamento no senado",
]


def test_classificacao_textos():
    textos = (ESPORTE + POLITICA) * 3
    rotulos = ([1] * len(ESPORTE) + [0] * len(POLITICA)) * 3
    xtr, xte, ytr, yte = train_test_split(textos, rotulos, test_size=0.3, stratify=rotulos, random_state=0)
    for vet, clf in (
        (TfidfVectorizer, LogisticRegression(max_iter=1000)),
        (CountVectorizer, MultinomialNB()),
        (TfidfVectorizer, LinearSVC()),
    ):
        modelo = make_pipeline(vet(), clf).fit(xtr, ytr)
        pred = modelo.predict(xte)
        assert accuracy_score(yte, pred) > 0.8
        vn, fp, fn, vp = confusion_matrix(yte, pred).ravel()
        p, r = vp / (vp + fp), vp / (vp + fn)
        assert precision_score(yte, pred) == pytest.approx(p) and recall_score(yte, pred) == pytest.approx(r)
        assert f1_score(yte, pred) == pytest.approx(2 * p * r / (p + r))


V_ESPORTE = "time jogo gol partida campeonato estádio torcida goleiro".split()
V_CULINARIA = "bolo farinha ovos forno panela receita alho feijão".split()


def _top(componentes, nomes, k=5):
    return [set(nomes[np.argsort(c)[::-1][:k]]) for c in componentes]


def test_topicos():
    rng = np.random.default_rng(0)
    docs = [" ".join(rng.choice(V_ESPORTE, 6)) for _ in range(20)] + [
        " ".join(rng.choice(V_CULINARIA, 6)) for _ in range(20)
    ]
    assunto = np.array([0] * 20 + [1] * 20)
    cont = CountVectorizer()
    xc = cont.fit_transform(docs)
    tfidf = TfidfVectorizer()
    xt = tfidf.fit_transform(docs)
    modelos = [
        (NMF(2, random_state=0, init="nndsvd"), xt, tfidf),
        (LatentDirichletAllocation(2, random_state=0, max_iter=100), xc, cont),
    ]
    for modelo, x, vet in modelos:
        w = modelo.fit_transform(x)
        tops = _top(modelo.components_, vet.get_feature_names_out())
        assert any(t <= set(V_ESPORTE) for t in tops) and any(t <= set(V_CULINARIA) for t in tops), (modelo, tops)
        assert adjusted_rand_score(assunto, w.argmax(axis=1)) == pytest.approx(1), modelo
    # SVD: pesos com sinal, difíceis de ler; os documentos projetados ainda separam os assuntos
    w = TruncatedSVD(2, random_state=0).fit_transform(xt)
    grupos = KMeans(2, n_init=10, random_state=0).fit_predict(w)
    assert adjusted_rand_score(assunto, grupos) == pytest.approx(1)


def test_pca_e_cotovelo():
    x, y = make_blobs(300, n_features=50, centers=3, cluster_std=1.0, random_state=0)
    pca = PCA(n_components=0.95, random_state=0).fit(x)
    acum = np.cumsum(PCA(random_state=0).fit(x).explained_variance_ratio_)
    assert pca.n_components_ == np.searchsorted(acum, 0.95) + 1
    xp = pca.transform(x)
    rotulos = {}
    for nome, dados in (("projetado", xp), ("original", x)):
        inercias = [KMeans(k, n_init=10, random_state=0).fit(dados).inertia_ for k in range(1, 8)]
        assert all(b < a for a, b in zip(inercias, inercias[1:], strict=False))
        quedas = [inercias[i - 1] / inercias[i] for i in range(1, len(inercias))]
        ganho = [quedas[i] / quedas[i + 1] for i in range(len(quedas) - 1)]
        assert int(np.argmax(ganho)) + 2 == 3, nome
        rotulos[nome] = KMeans(3, n_init=10, random_state=0).fit_predict(dados)
    assert adjusted_rand_score(rotulos["projetado"], rotulos["original"]) == pytest.approx(1)


def test_tsne():
    x, y = make_blobs(150, n_features=20, centers=3, random_state=0)
    emb = TSNE(n_components=2, perplexity=30, random_state=0, init="pca").fit_transform(x)
    assert trustworthiness(x, emb, n_neighbors=5) > 0.9
    assert silhouette_score(emb, y) > 0.5


def _cos(a, b):
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))


def test_buscador_dm():
    vet = {
        "felino": np.array([1.0, 0.1, 0.0]),
        "gato": np.array([0.9, 0.2, 0.0]),
        "leão": np.array([0.8, 0.0, 0.2]),
        "cão": np.array([0.6, 0.5, 0.0]),
        "imposto": np.array([0.0, 0.1, 1.0]),
        "lei": np.array([0.1, 0.0, 0.9]),
        "senado": np.array([0.0, 0.2, 0.9]),
    }
    docs = {"animais": ["gato", "leão", "cão"], "politica": ["imposto", "lei", "senado"], "misto": ["gato", "lei"]}

    def dm(w, doc, k=10):
        dist = sorted(1 - _cos(vet[w], vet[p]) for p in doc if p in vet)[:k]
        return sum(dist) / len(dist)

    assert 1 - _cos(vet["gato"], vet["gato"]) == pytest.approx(0)
    ordem = sorted(docs, key=lambda d: dm("felino", docs[d]))
    assert ordem == ["animais", "misto", "politica"]
    parecidas = sorted((p for p in vet if p != "felino"), key=lambda p: -_cos(vet["felino"], vet[p]))[:3]
    assert parecidas == ["gato", "leão", "cão"]
    assert dm("felino", ["gato"] * 15, k=10) == pytest.approx(1 - _cos(vet["felino"], vet["gato"]))


def test_janelas_proxima_palavra():
    toks = "o gato subiu no telhado de casa".split()
    pares = [(toks[i : i + 4], toks[i + 4]) for i in range(len(toks) - 4)]
    assert len(pares) == len(toks) - 4 == 3
    assert pares[0] == (["o", "gato", "subiu", "no"], "telhado") and pares[-1][1] == "casa"
    bigramas = {a: b for a, b in zip(toks, toks[1:], strict=False)}
    bigramas["casa"] = "o"
    janela, gerado = ["o", "gato", "subiu", "no"], []
    for _ in range(10):
        prox = bigramas[janela[-1]]
        gerado.append(prox)
        janela = janela[1:] + [prox]
        assert len(janela) == 4
    assert len(gerado) == 10 and gerado[:3] == ["telhado", "de", "casa"]


def test_contagem_uma_vez_por_documento():
    docs = [
        [("Ana", "PER"), ("Ana", "PER"), ("Ana", "PER"), ("Maceió", "LOC")],
        [("Bruno", "PER"), ("Recife", "LOC")],
        [("Bruno", "PER"), ("Ana", "PER")],
        [("Bruno", "PER")],
    ]
    simples = Counter(t for d in docs for t, r in d if r == "PER")
    por_doc = Counter()
    for d in docs:
        por_doc.update({t for t, r in d if r == "PER"})
    assert simples.most_common(1)[0] == ("Ana", 4)
    assert por_doc == {"Bruno": 3, "Ana": 2}
    assert {t for d in docs for t, r in d if r == "LOC"} == {"Maceió", "Recife"}


def test_dados_seq2seq():
    pares = [("Go.", "Vai."), ("Hi.", "Oi.")]
    alvos = ["\t" + b + "\n" for _, b in pares]
    ent_chars = sorted({c for a, _ in pares for c in a})
    sai_chars = sorted({c for t in alvos for c in t})
    max_ent, max_sai = max(len(a) for a, _ in pares), max(len(t) for t in alvos)
    enc = np.zeros((len(pares), max_ent, len(ent_chars)))
    dec = np.zeros((len(pares), max_sai, len(sai_chars)))
    alvo = np.zeros_like(dec)
    for i, ((a, _), t) in enumerate(zip(pares, alvos, strict=True)):
        for j, c in enumerate(a):
            enc[i, j, ent_chars.index(c)] = 1
        for j, c in enumerate(t):
            dec[i, j, sai_chars.index(c)] = 1
            if j > 0:
                alvo[i, j - 1, sai_chars.index(c)] = 1
    assert enc.shape == (2, 3, len(ent_chars)) and dec.shape == (2, 6, len(sai_chars))
    assert dec[0, 0, sai_chars.index("\t")] == 1 and alvo[0, 4, sai_chars.index("\n")] == 1
    assert np.array_equal(alvo[:, :-1], dec[:, 1:])
