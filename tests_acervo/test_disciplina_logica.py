"""Acervo de Lógica Aplicada à Computação e conferência das resoluções.

Os blocos parafraseiam slides, prova e listas da UFAL (Baldoino e Evandro) e slides da UFCG (Massoni).
Cada refutação, prova em dedução natural, consequência e contramodelo citado num bloco é recalculado aqui,
com o verificador de `tests_acervo/logica_verif.py`.
"""

import json
import re
import shutil
import subprocess

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search
from tests_acervo import logica_verif as lv

LOG = disciplinas.obter("logica")
PASTA = ROOT / "disciplinas/logica"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
ITENS = {i["id"]: i for i in read_json(LOG.itens)}
FRONTEIRA = ("discreta", "sd", "paa", "iec")
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "logica")
SEM_MATERIAL: set[str] = set()


def buscar(pergunta, d=LOG):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return ITENS[ident]["texto"]


# ---------------------------------------------------------------- cadastro e acervo


def test_logica_cadastrada_com_acervo_proprio():
    assert LOG.nome == "Lógica Aplicada à Computação" and LOG.itens.exists() and not LOG.livro_supabase
    ids = {c["id"] for c in read_json(LOG.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({LOG.itens, LOG.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert all(c["disciplina"] == "logica" for c in read_json(LOG.indice)["chunks"])
    # todo tópico da ementa com material da turma tem bloco na busca
    assert {i["assunto"] for i in ITENS.values()} == set(LOG.assuntos) - SEM_MATERIAL
    assert ids == set(ITENS)


def test_situacao_da_disciplina():
    assert LOG.situacao == "MVP" and not LOG.em_validacao and not LOG.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas logica --embeddings`."""
    gerados = disciplinas.registros(LOG)
    assert gerados == read_json(LOG.itens)
    assert {c["id"] for c in read_json(LOG.indice)["chunks"]} == {
        i["id"] for i in gerados if i["confiabilidade"] in ("media", "alta")
    }


def test_blocos_cabem_no_trecho_e_terminam_com_verificacao():
    for i in ITENS.values():
        assert len(i["texto"]) <= 2200, i["id"]
        assert "**Verificação:**" in i["texto"].strip().splitlines()[-1], i["id"]
        assert not re.search(r"[\x00-\x08\x0b-\x1f]", i["texto"]), i["id"]  # escape perdido (\t de \to, \n de \neg)


def test_nenhuma_nota_da_ia_e_nada_revisado_sem_registro():
    assert not [i for i, x in ITENS.items() if x["natureza"] == "nota_da_equipe_ia"]
    for p in LOG.materiais.glob("*.md"):
        cab = p.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, p.name


def test_resolucoes_tem_status_e_dizem_no_texto():
    status = {i: x["status_resolucao"] for i, x in ITENS.items()}
    assert set(status.values()) <= {"validada", "corrigida", "pendente_professor"}
    assert [i for i, s in status.items() if s == "pendente_professor"] == ["logica-prova1-q2-greve"]
    for i, x in ITENS.items():
        assert f"Status da resolução: {status[i]}" in x["texto"], i
        assert "não é gabarito do professor" in x["texto"], i
        if status[i] == "corrigida":
            assert "Correção" in x["texto"] or "corrig" in x["texto"].lower(), i


# ---------------------------------------------------------------- busca e isolamento


@pytest.mark.parametrize(
    "pergunta, aceitos",
    [
        (
            "Como provar que (¬P → Q) ∧ (R → ¬P) ⊨ Q ∨ ¬R por tabela-verdade?",
            {"logica-consequencia-logica-teoremas", "logica-semantica-tabela-verdade"},
        ),
        ("Qual a diferença entre ⊨ e ⊢?", {"logica-consequencia-vs-derivacao"}),
        ('Como negar "todo aluno estuda"?', {"logica-negacao-quantificadores"}),
        ("Como converter uma fórmula para forma normal conjuntiva?", {"logica-forma-normal-conjuntiva"}),
        (
            "Como provar p → q ⊢ ¬q → ¬p por dedução natural?",
            {"logica-deducao-natural-exemplos", "logica-deducao-natural-regras"},
        ),
        ("Como funciona o método dos tableaux?", {"logica-tableaux-proposicional"}),
        ("Como calcular o unificador mais geral?", {"logica-unificacao-mgu"}),
        ("O que é skolemização?", {"logica-forma-clausal-skolem"}),
        ("O que é uma cláusula de Horn?", {"logica-horn-prolog-sat"}),
    ],
)
def test_pergunta_de_logica_encontra_bloco_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize("pergunta", ["Qual a capital da França?", "Qual a receita de bolo de cenoura?"])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


@pytest.mark.parametrize(
    "pergunta",
    [
        "Como montar uma tabela-verdade?",
        "Como aplicar as leis de De Morgan?",
        "O que é uma prova por indução?",
        "O que é o problema SAT?",
    ],
)
def test_vocabulario_comum_fica_na_disciplina_escolhida(pergunta):
    """Fronteira com Discreta, SD, PAA e IEC: cada uma busca só no próprio índice."""
    assert all(i.startswith("logica-") for i in buscar(pergunta))
    for d in FRONTEIRA:
        assert not any(i.startswith("logica-") for i in buscar(pergunta, disciplinas.obter(d)))


def test_rigor_tem_fronteiras_e_metodos():
    for termo in ("Matemática Discreta", "Sistemas Digitais", "PAA", "\\models", "\\vdash", "contramodelo",
                  "numere as linhas", "Huth e Ryan", "**Verificação:**", "Não entregue a resolução"):  # fmt: skip
        assert termo in LOG.rigor, termo


# ---------------------------------------------------------------- conferência: proposicional

_CLAUS = re.compile(r"(\d+)\.\s*\$(\\\{.*?\\\}|\\square)\$(?:\s*\((?:negação da conclusão|\d+,\s*\d+)\))?")
_CITA = re.compile(r"\((\d+),\s*(\d+)\)")


def refutacoes(t):
    """Extrai as refutações numeradas ('1. $\\{P, Q\\}$; ... 7. $\\square$ (4, 6)') do texto de um bloco."""
    blocos, atual = [], None
    for m in _CLAUS.finditer(t):
        n = int(m.group(1))
        if n == 1:
            atual = ([], [])
            blocos.append(atual)
        c = lv.clausula(m.group(2))
        cita = _CITA.search(m.group(0))
        if cita:
            atual[1].append((c, int(cita.group(1)), int(cita.group(2))))
        else:
            assert not atual[1], f"cláusula de entrada depois de resolvente: {m.group(0)}"
            atual[0].append(c)
    return blocos


@pytest.mark.parametrize(
    "bloco, quantas",
    [
        ("logica-resolucao-proposicional", 2),
        ("logica-prova1-q1-tres-metodos", 1),
        ("logica-lista-q3-consequencias", 1),
        ("logica-lista-q5-q6-argumentos", 1),
    ],
)
def test_refutacoes_proposicionais_do_texto(bloco, quantas):
    achadas = refutacoes(texto(bloco))
    assert len(achadas) == quantas
    for entrada, passos in achadas:
        lv.confere_refutacao(entrada, passos)
        assert lv.insatisfazivel_clausulas(entrada)


def test_consequencias_e_contramodelos_proposicionais():
    c, cm = lv.consequencia, lv.contramodelos
    # T1/T2 e a pergunta do exemplo
    assert c([r"(\neg P\to Q)\land(R\to\neg P)"], r"Q\lor\neg R")
    assert c([r"((P\to\neg Q)\land(R\leftrightarrow\neg P)\land Q)"], "R")
    # argumentos clássicos
    assert c([r"Q\to P", r"(P\to\neg Q)\land(\neg P\to Q)"], "P")
    assert c([r"(B\to A)\land(A\to\neg B)\land(\neg A\to B)"], "A")
    assert c([], r"((A\to B)\land(B\to C)\land(\neg A\to C))\to C")
    assert c([], r"((A\to\neg C)\land(\neg A\to\neg B)\land(\neg B\to\neg C))\to\neg C")
    seis = [r"A\to B", r"B\to C", r"\neg A\to C", r"A\to\neg C", r"\neg A\to\neg B", r"\neg B\to\neg C"]
    assert not lv.satisfazivel(*seis)
    # tableau do chimarrão
    chim = [r"A\to B", r"A\lor D", r"C\land\neg B"]
    assert lv.satisfazivel(*chim) and not lv.satisfazivel(*chim, r"\neg(C\land D)")
    assert lv.valor(lv.parse(r"(A\to B)\land(A\lor D)\land(C\land\neg B)"), dict(A=False, B=False, C=True, D=True))
    # prova 1
    q1 = [r"\neg P\to Q", r"Q\lor R", r"R\lor W", r"R\to\neg P", r"W\to\neg Q"]
    assert c(q1, r"Q\land R")
    s1, s2 = r"g\to(t\lor(d\land a))", r"g\land t\land\neg a"
    assert not c([s1, s2], "d") and not c([s1, s2], r"\neg d") and c([s1, s2, r"t\to\neg d"], r"\neg d")
    assert cm([r"A\to(B\lor C)", "B"], r"A\to\neg C") == [dict(A=True, B=True, C=True)]
    # lista Q3
    assert c([r"p\to q", r"q\to r"], r"(q\to r)\to((p\to\neg r)\to\neg p)")
    assert c([r"q\to(p\land r)", r"\neg s\to\neg p", r"(p\land s)\to t"], r"q\to t")
    assert c([r"(p\to(q\to r))\land\neg r"], r"q\to\neg p")
    d = cm([r"(p\to q)\lor(\neg r\to s)"], r"(p\land\neg r)\to(p\land s)")
    assert dict(p=True, q=True, r=False, s=False) in d
    assert c([r"(p\to q)\land(r\to s)"], r"(p\lor r)\to(q\lor s)")
    f = r"\neg((q\to\neg r)\to(p\to(r\to\neg p)))"
    assert [v for v, b in lv.tabela(f) if b] == [dict(p=True, q=False, r=True)]
    assert c([f], r"\neg((p\to q)\land(\neg r\to\neg q))")
    assert c([], r"(p\to q)\to((r\to s)\to((p\land s)\to(q\land s)))")
    # lista Q5 e Q6
    assert cm([r"j\to(m\lor z)", r"\neg m"], r"z\to\neg j") == [dict(j=True, m=False, z=True)]
    assert c([r"c\to(a\to f)", r"\neg f"], r"a\to\neg c")


def test_conectivos_equivalencias_cnf_e_horn():
    e, c = lv.equivalentes, lv.consequencia
    # exercícios de concurso: só a alternativa indicada é consequência
    assert c([r"\neg L\to\neg C", r"J\to\neg L", r"\neg D\to C", r"F\to\neg D"], r"J\to\neg F")
    assert c([r"F\lor\neg G", r"\neg D\to\neg F", "G"], r"F\land D")
    assert e(r"M\to C", r"\neg C\to\neg M") and not e(r"M\to C", r"C\to M") and not e(r"M\to C", r"\neg M\to\neg C")
    assert e(r"\neg(A\land B)", r"\neg A\lor\neg B") and not e(r"E\to V", r"V\to E")
    # equivalências
    for a, b in [
        (r"p\leftrightarrow q", r"(p\to q)\land(q\to p)"),
        (r"p\to q", r"\neg(p\land\neg q)"),
        (r"A\to(B\to C)", r"(A\to B)\to(A\to C)"),
        (r"(C\land T)\to E", r"C\to(T\to E)"),
        (r"\neg(p\to q)", r"p\land\neg q"),
        (r"p\lor(q\land r)", r"(p\lor q)\land(p\lor r)"),
    ]:
        assert e(a, b), (a, b)
    # CNF
    assert e(r"T\lor E\to T", r"(\neg T\lor T)\land(\neg E\lor T)")
    assert e(r"P\leftrightarrow(Q\land R)", r"(\neg P\lor Q)\land(\neg P\lor R)\land(\neg Q\lor\neg R\lor P)")
    assert c([], r"(\neg Q\lor P\lor R\lor Q)\land(\neg P\lor R\lor P)")
    # Horn
    assert not lv.satisfazivel(r"(p\to\bot)\land(r\to p)\land(\top\to p)")
    assert lv.valor(lv.parse(r"(p\to r)\land(\top\to p)"), dict(p=True, r=True))
    # precedência: p → q ∧ r é p → (q ∧ r)
    assert lv.parse(r"p\to q\land r") == lv.parse(r"p\to(q\land r)")


# ---------------------------------------------------------------- conferência: dedução natural


def test_deducao_natural_do_texto():
    lv.confere_deducao(
        lv.deducao_do_texto(texto("logica-deducao-natural-regras")), ["p", r"\neg\neg(c\land d)"], r"\neg\neg p\land c"
    )
    t = texto("logica-deducao-natural-exemplos")
    casos = [
        ([r"p\to q"], r"\neg q\to\neg p"),
        ([r"\neg j\to\neg c"], r"c\to\neg\neg j"),
        ([r"a\to d"], r"z\lor a\to z\lor d"),
    ]
    inicios = [m.start() for m in re.finditer(r"^1\. ", t, re.M)]
    assert len(inicios) == len(casos)
    for inicio, (prem, conc) in zip(inicios, casos, strict=True):
        lv.confere_deducao(lv.deducao_do_texto(t, inicio), prem, conc)


def test_verificador_recusa_prova_errada():
    with pytest.raises(AssertionError):
        lv.confere_deducao([(1, r"p\to q", "premissa", ""), (2, "q", "→e", "1")], [r"p\to q"], "q")
    with pytest.raises(AssertionError):
        lv.confere_refutacao([lv.clausula("{P}"), lv.clausula("{Q}")], [(frozenset(), 1, 2)])


# ---------------------------------------------------------------- conferência: primeira ordem


def _r1(entrada, passos):
    lv.confere_refutacao1([lv.clausula1(x) for x in entrada], [(lv.clausula1(a), i, j) for a, i, j in passos])


def test_refutacoes_de_primeira_ordem():
    _r1(
        ["chama(a,b)", "usa(b,e)", "¬chama(x,y) ∨ depende(x,y)", "¬usa(x,y) ∨ depende(x,y)",
         "¬depende(x,z) ∨ ¬depende(z,y) ∨ depende(x,y)", "¬depende(a,e)"],
        [("depende(a,b)", 1, 3), ("depende(b,e)", 2, 4), ("¬depende(b,y) ∨ depende(a,y)", 5, 7),
         ("depende(a,e)", 8, 9), ("□", 6, 10)],
    )  # fmt: skip
    _r1(
        ["C(a)", "¬H(y) ∨ G(a,y)", "¬C(x) ∨ ¬V(y) ∨ ¬G(x,y)", "H(b)", "V(b)"],
        [("G(a,b)", 2, 4), ("¬V(y) ∨ ¬G(a,y)", 1, 3), ("¬G(a,b)", 5, 7), ("□", 6, 8)],
    )
    _r1(
        ["¬DE(x,y) ∨ ¬A(y) ∨ M(g(x))", "¬DE(x,y) ∨ ¬A(y) ∨ G(x,g(x))", "¬M(w)", "DE(b,c)", "A(c)"],
        [("¬A(c) ∨ M(g(b))", 1, 4), ("M(g(b))", 5, 6), ("□", 3, 7)],
    )
    _r1(
        ["¬D(x) ∨ ¬V(x) ∨ ¬F(x)", "¬A(x) ∨ ¬B(y) ∨ ¬E(x,y) ∨ F(x)", "¬Z(x) ∨ B(x)",
         "¬A(x) ∨ ¬V(x) ∨ ¬Z(y) ∨ E(x,y)", "¬D(x) ∨ A(x)", "Z(c)", "D(d)", "V(d)"],
        [("A(d)", 5, 7), ("B(c)", 3, 6), ("¬V(d) ∨ ¬Z(y) ∨ E(d,y)", 4, 9), ("¬Z(y) ∨ E(d,y)", 8, 11),
         ("E(d,c)", 6, 12), ("¬B(y) ∨ ¬E(d,y) ∨ F(d)", 2, 9), ("¬E(d,c) ∨ F(d)", 10, 14), ("F(d)", 13, 15),
         ("¬V(d) ∨ ¬F(d)", 1, 7), ("¬F(d)", 8, 17), ("□", 16, 18)],
    )  # fmt: skip
    _r1(
        ["¬E(x) ∨ V(x) ∨ vd(x,f(x))", "¬E(x) ∨ V(x) ∨ P(f(x))", "D(a)", "E(a)", "¬vd(a,y) ∨ D(y)",
         "¬D(x) ∨ ¬V(x)", "¬D(x) ∨ ¬P(x)"],
        [("¬V(a)", 3, 6), ("V(a) ∨ vd(a,f(a))", 1, 4), ("vd(a,f(a))", 8, 9), ("D(f(a))", 5, 10),
         ("V(a) ∨ P(f(a))", 2, 4), ("P(f(a))", 8, 12), ("¬P(f(a))", 7, 11), ("□", 13, 14)],
    )  # fmt: skip
    _r1(
        ["genitor(x,f(x)) ∨ feliz(x)", "¬voa(f(x)) ∨ feliz(x)", "¬verde(x) ∨ voa(x)",
         "¬genitor(y,x) ∨ ¬verde(y) ∨ verde(x)", "verde(a)", "¬feliz(a)"],
        [("genitor(a,f(a))", 1, 6), ("¬voa(f(a))", 2, 6), ("¬verde(f(a))", 3, 8),
         ("¬verde(a) ∨ verde(f(a))", 4, 7), ("verde(f(a))", 5, 10), ("□", 9, 11)],
    )  # fmt: skip
    _r1(
        ["¬P(x,y) ∨ R(x) ∨ Q(a)", "¬R(x) ∨ Q(f(x))", "P(a,b)", "¬Q(z)"],
        [("R(a) ∨ Q(a)", 1, 3), ("R(a)", 4, 5), ("Q(f(a))", 2, 6), ("□", 4, 7)],
    )
    t = texto("logica-resolucao-dragoes-zoologico")
    assert "19. $\\square$ (16, 18)" in t and "11. $\\neg V(d)\\lor\\neg Z(y)\\lor E(d,y)$ (4, 9)" in t


def test_literal_de_resposta_da_q9():
    c = lv.clausula1
    entrada = [c("¬P(x,y) ∨ R(x) ∨ Q(a)"), c("¬R(x) ∨ Q(f(x))"), c("P(a,b)"), c("¬Q(z) ∨ r(z)")]
    passo = [c("R(a) ∨ Q(a)"), c("R(a) ∨ r(a)"), c("Q(f(a)) ∨ r(a)"), c("r(f(a)) ∨ r(a)")]
    linhas = list(entrada)
    for alvo, (i, j) in zip(passo, [(1, 3), (4, 5), (2, 6), (4, 7)], strict=True):
        assert any(lv.mesma_clausula(alvo, r) for r in lv.resolventes1(linhas[i - 1], linhas[j - 1]))
        linhas.append(alvo)


def test_unificacao():
    t, u = lv.termo, lv.unificar
    s = u([t("P(x,f(y))"), t("P(a,f(b))")])
    assert s is not None and lv.resolver_mgu(s) == {"x": t("a"), "y": t("b")}
    assert u([t("P(x)"), t("P(f(x))")]) is None  # teste de ocorrência
    assert u([t("P(a)"), t("P(b)")]) is None


def _todos(U, f):
    return all(f(x) for x in U)


def _algum(U, f):
    return any(f(x) for x in U)


def test_semantica_de_primeira_ordem():
    A = "abc"
    R = {("a", "a"), ("a", "b"), ("a", "c"), ("b", "c"), ("c", "c")}
    F, i = {"b", "c"}, "a"
    assert _algum(A, lambda y: (i, y) in R) and i not in F
    assert _todos(A, lambda x: _algum(A, lambda y: (x, y) in R))
    assert not _todos(
        A, lambda x: _todos(A, lambda y: _todos(A, lambda z: not ((x, y) in R and (x, z) in R) or y == z))
    )
    p = [lambda U, I: _todos(U, lambda x: (x,) not in I["P"] or (x,) in I["Q"])]
    q = lambda U, I: not _todos(U, lambda x: (x,) in I["P"]) or _todos(U, lambda x: (x,) in I["Q"])  # noqa: E731
    assert lv.contramodelo_finito(p, q, {"P": 1, "Q": 1}) is None
    reciproca = lv.contramodelo_finito([q], p[0], {"P": 1, "Q": 1})
    assert reciproca is not None and reciproca[0] == 2
    U, I = range(2), {"P": {(0,)}, "Q": set()}
    assert q(U, I) and not p[0](U, I)


def test_negacao_de_todo_aluno_estuda():
    neg = lambda U, I: not _todos(U, lambda x: (x,) not in I["A"] or (x,) in I["E"])  # noqa: E731
    existe = lambda U, I: _algum(U, lambda x: (x,) in I["A"] and (x,) not in I["E"])  # noqa: E731
    nenhum = lambda U, I: _todos(U, lambda x: (x,) not in I["A"] or (x,) not in I["E"])  # noqa: E731
    assert lv.contramodelo_finito([neg], existe, {"A": 1, "E": 1}) is None
    assert lv.contramodelo_finito([existe], neg, {"A": 1, "E": 1}) is None
    assert lv.contramodelo_finito([neg], nenhum, {"A": 1, "E": 1}) is not None


def test_correcao_q1b_do_gabarito_difere_do_original():
    def gabarito(U, I):
        return _todos(U, lambda x: _todos(U, lambda y: ((x, y) in I["C"]) == (
            ((x,) not in I["P"] or (y,) in I["N"]) and ((x,) not in I["N"] or (y,) in I["P"]))))  # fmt: skip

    def corrigida(U, I):
        return _todos(U, lambda x: _todos(U, lambda y: (x, y) not in I["C"] or (
            ((x,) not in I["P"] or (y,) in I["N"]) and ((x,) not in I["N"] or (y,) in I["P"]))))  # fmt: skip

    preds = {"P": 1, "N": 1, "C": 2}
    assert lv.contramodelo_finito([corrigida], gabarito, preds, max_universo=2) is not None
    assert lv.contramodelo_finito([gabarito], corrigida, preds, max_universo=2) is None


def test_dragoes_precisam_de_s5_e_s6():
    def s(U, I):
        D, V, F, A, B, Z, E = (I[k] for k in "DVFABZE")
        return [
            _todos(U, lambda x: not ((x,) in D and (x,) in V and (x,) in F)),
            _todos(U, lambda x: _todos(U, lambda y: not ((x,) in A and (y,) in B and (x, y) in E) or (x,) in F)),
            _todos(U, lambda x: (x,) not in Z or (x,) in B),
            _todos(U, lambda x: _todos(U, lambda y: not ((x,) in A and (x,) in V and (y,) in Z) or (x, y) in E)),
            _todos(U, lambda x: (x,) not in D or (x,) in A),
            _algum(U, lambda x: (x,) in Z),
        ]

    s7 = lambda U, I: not _algum(U, lambda x: (x,) in I["D"] and (x,) in I["V"])  # noqa: E731
    preds = {**{k: 1 for k in "DVFABZ"}, "E": 2}
    for fora in (4, 5):  # sem S5, sem S6
        prem = [lambda U, I, k=k: s(U, I)[k] for k in range(6) if k != fora]
        achado = lv.contramodelo_finito(prem, s7, preds, max_universo=2)
        assert achado is not None and achado[0] <= 2
    tudo = [lambda U, I, k=k: s(U, I)[k] for k in range(6)]
    assert lv.contramodelo_finito(tudo, s7, preds, max_universo=2) is None


# ---------------------------------------------------------------- fórmulas, catálogo e restrições

FORMULA = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in ITENS.values():
        assert i["texto"].count("$") % 2 == 0, i["id"]
    assert LOG.rigor.count("$") % 2 == 0


@pytest.mark.skipif(not shutil.which("node"), reason="node indisponível")
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for i in ITENS.values() for a, b in FORMULA.findall(i["texto"])]
    formulas += [a or b for a, b in FORMULA.findall(LOG.rigor)]
    assert len(formulas) >= 300
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
        assert set(f["topicos"]) <= set(LOG.assuntos), f["id"]
    assert {i for i, f in CATALOGO.items() if f["uso"] == "acervo"} == {
        x for i in ITENS.values() for x in i["fontes_catalogo"]
    }
    livro = CATALOGO["huth-ryan-lics"]
    assert livro["uso"] == "referencia" and livro["acesso"].startswith("Não incluído") and not livro["url"]


def test_originais_e_dados_pessoais_fora_do_repositorio():
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()]
    assert not [
        p
        for p in arquivos
        if p.suffix.lower() in (".pdf", ".png", ".jpg", ".jpeg", ".heic", ".webp", ".docx", ".doc", ".zip", ".pptx")
    ]
    proibidos = re.compile(r"(?i)[\w.]+@[\w-]+\.\w+|groups\.google|dropbox|sites\.google|whatsapp|baldoino@")
    for p in [
        *LOG.materiais.glob("*.md"),
        LOG.itens,
        PASTA / "rigor.md",
        PASTA / "CURADORIA.md",
        PASTA / "fontes.json",
    ]:
        assert not proibidos.search(p.read_text(encoding="utf-8")), p.name
    for i in ITENS.values():
        assert "http" not in i["texto"], i["id"]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert [i for i in CATALOGO if f"`{i}`" not in curadoria] == []
    assert [i for i in ITENS if f"`{i}`" not in curadoria] == []
    assert "`logica`" in (ROOT / "docs/DISCIPLINAS.md").read_text(encoding="utf-8")
