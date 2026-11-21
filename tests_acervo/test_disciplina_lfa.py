"""Acervo de Linguagens Formais, Autômatos e Computabilidade e conferência das resoluções.

Os blocos parafraseiam listas e provas da UFAL, as apostilas da Profa. Simone Prado (UNESP) e as notas das
aulas de Sipser; cada autômato, gramática, máquina e programa citado é simulado por `tests_acervo/lfa_verif.py`.
"""

import hashlib
import json
import re
import shutil
import subprocess
import unicodedata
from itertools import product

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search
from tests_acervo import lfa_verif as lv

LFA = disciplinas.obter("lfa")
PASTA = ROOT / "disciplinas/lfa"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(LFA.itens)}
ITENS = {i: x for i, x in TODOS.items() if x["natureza"] == "material_da_disciplina"}
NOTAS = {i: x for i, x in TODOS.items() if x["natureza"] == "nota_da_equipe_ia"}
FRONTEIRA = ("paa", "logica", "discreta")
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "lfa")


def buscar(pergunta, d=LFA):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return TODOS[ident]["texto"]


def tem(ident, *trechos):
    faltam = [n for n in trechos if n not in texto(ident)]
    assert not faltam, f"{ident}: {faltam}"


# ---------------------------------------------------------------- cadastro e acervo


def test_lfa_cadastrada_com_acervo_proprio():
    assert LFA.nome == "Linguagens Formais, Autômatos e Computabilidade" and LFA.itens.exists()
    assert not LFA.livro_supabase
    ids = {c["id"] for c in read_json(LFA.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({LFA.itens, LFA.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert all(c["disciplina"] == "lfa" for c in read_json(LFA.indice)["chunks"])
    assert {i["assunto"] for i in ITENS.values()} == set(LFA.assuntos)
    assert ids == set(ITENS)
    cursos = (ROOT / "disciplinas/cursos.json").read_text(encoding="utf-8")
    assert cursos.count('"acervo": "lfa"') == 2


def test_situacao_da_disciplina():
    assert LFA.situacao == "MVP" and not LFA.em_validacao and not LFA.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas lfa --embeddings`."""
    gerados = disciplinas.registros(LFA)
    assert gerados == read_json(LFA.itens)
    assert {c["id"] for c in read_json(LFA.indice)["chunks"]} == {
        i["id"] for i in gerados if i["confiabilidade"] in ("media", "alta")
    }


def test_blocos_cabem_no_trecho_e_terminam_com_verificacao():
    for i in TODOS.values():
        assert len(i["texto"]) <= 2200, i["id"]
        assert "**Verificação:**" in i["texto"].strip().splitlines()[-1], i["id"]
        assert not re.search(r"[\x00-\x08\x0b-\x1f]", i["texto"]), i["id"]


def test_notas_da_ia_fora_da_busca_e_nada_revisado_sem_registro():
    indice = {c["id"] for c in read_json(LFA.indice)["chunks"]}
    assert NOTAS and indice.isdisjoint(NOTAS)
    assert all(x["status_curadoria"] == "candidato" for x in NOTAS.values())
    for p in LFA.materiais.glob("*.md"):
        cab = p.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, p.name


def test_resolucoes_tem_status_e_dizem_no_texto():
    status = {i: x["status_resolucao"] for i, x in ITENS.items() if "status_resolucao" in x}
    assert {i for i, x in ITENS.items() if x["tipo"] in ("prova", "lista", "exercicio_resolvido")} <= set(status)
    assert {i for i, s in status.items() if s == "pendente_professor"} == {
        "lfa-maquina-de-turing-definicao-perguntas",
        "lfa-prova2-funcao-f-quatro-componentes",
        "lfa-lista-decidibilidade-afd-m-figura",
    }
    for i, s in status.items():
        t = texto(i)
        assert f"Status da resolução: {s}" in t and "não é gabarito do professor" in t, i
        if s == "corrigida":
            assert "**Correção:**" in t, i
        if s == "pendente_professor":
            assert "**Pendente:**" in t, i


# ---------------------------------------------------------------- busca e isolamento


@pytest.mark.parametrize(
    "pergunta, aceitos",
    [
        ("Como construir um AFD para cadeias com número par de zeros?", {"lfa-afd-numero-par-de-zeros"}),
        ("Como converter um AFN em AFD?", {"lfa-afn-para-afd-subconjuntos", "lfa-afn-para-afd-exemplos-corrigidos"}),
        (
            "Como usar o lema do bombeamento para provar que aⁿbⁿ não é regular?",
            {"lfa-lema-do-bombeamento-anbn", "lfa-bombeamento-mesmo-numero-a-b-corrigido"},
        ),
        ("Por que o problema da parada é indecidível?", {"lfa-problema-da-parada-indecidivel"}),
        ("Como minimizar um AFD pela tabela de pares?", {"lfa-minimizacao-afd-tabela-de-pares"}),
        ("Quando uma gramática é ambígua?", {"lfa-ambiguidade-gramatica-linguagem-inerente"}),
        ("Como passar uma gramática para a forma normal de Chomsky?", {"lfa-forma-normal-de-chomsky"}),
        (
            "Qual a diferença entre linguagem decidível e reconhecível?",
            {"lfa-decidivel-vs-reconhecivel-diagonalizacao"},
        ),
        ("O que diz a tese de Church-Turing?", {"lfa-tese-de-church-turing-modelos"}),
    ],
)
def test_pergunta_de_lfa_encontra_bloco_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize("pergunta", ["Qual a capital da França?", "Qual a receita de bolo de cenoura?"])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


@pytest.mark.parametrize(
    "pergunta",
    ["O que é um problema NP-completo?", "Como provar por indução?", "O que é uma tabela-verdade?",
     "O que é um conjunto enumerável?"],
)  # fmt: skip
def test_vocabulario_comum_fica_na_disciplina_escolhida(pergunta):
    """Fronteira com PAA, Lógica e Discreta: cada disciplina busca só no próprio índice, nos dois sentidos."""
    assert all(i.startswith("lfa-") for i in buscar(pergunta))
    for d in FRONTEIRA:
        assert not any(i.startswith("lfa-") for i in buscar(pergunta, disciplinas.obter(d)))


def test_rigor_tem_fronteiras_e_metodos():
    for termo in ("tabela de transição", "(Q, \\Sigma, \\delta, q_0, F)", "fecho-ε", "toda", "redução",
                  "Projeto e Análise de Algoritmos", "Lógica Aplicada", "Matemática Discreta", "Sipser",
                  "**Verificação:**", "Não entregue a resolução completa", "em palavras"):  # fmt: skip
        assert termo in LFA.rigor, termo


# ---------------------------------------------------------------- linguagens e autômatos finitos

AB = "ab"
PAR = lv.AFD("pi", "01", {("p", "0"): "i", ("p", "1"): "p", ("i", "0"): "p", ("i", "1"): "i"}, "p", {"p"})


def test_operacoes_sobre_linguagens():
    for n in range(7):
        potencia = {""}
        for _ in range(n):
            potencia = {x + y for x in potencia for y in ("", "a")}
        assert potencia == {"a" * k for k in range(n + 1)}
    L = ["0", "11", "10"]
    assert len({x + y for x in L for y in L}) == 9


def test_afd_numero_par_de_zeros():
    for w in lv.palavras("01", 10):
        assert PAR.aceita(w) == (w.count("0") % 2 == 0), w
    assert all(map(PAR.aceita, ["", "1", "00", "1001", "010"]))
    assert not any(map(PAR.aceita, ["0", "01", "000", "10100"]))
    tem("lfa-afd-numero-par-de-zeros", "| → $p$ (final) | $i$ | $p$ |", "| $i$ | $p$ | $i$ |")


def test_afd_aa_ou_bb():
    d = {("q0", "a"): "q1", ("q0", "b"): "q2", ("q1", "a"): "qf", ("q1", "b"): "q2",
         ("q2", "a"): "q1", ("q2", "b"): "qf", ("qf", "a"): "qf", ("qf", "b"): "qf"}  # fmt: skip
    m = lv.AFD(["q0", "q1", "q2", "qf"], AB, d, "q0", {"qf"})
    assert m.total()
    for w in lv.palavras(AB, 10):
        assert m.aceita(w) == ("aa" in w or "bb" in w), w
    parcial = lv.AFD("pq", "a", {("p", "a"): "q"}, "p", {"q"})
    completo = parcial.completo()
    assert completo.total() and lv.contraexemplo(parcial, completo) is None


def test_afn_sufixo_aaa():
    n = lv.AFN(["q0", "q1", "q2", "qf"], AB,
               {("q0", "a"): {"q0", "q1"}, ("q0", "b"): {"q0"}, ("q1", "a"): {"q2"}, ("q2", "a"): {"qf"}}, "q0", {"qf"})  # fmt: skip
    m = n.subconjuntos()
    assert sorted(map(lv.nome, m.Q)) == ["<q0,q1,q2,qf>", "<q0,q1,q2>", "<q0,q1>", "<q0>"]
    assert [lv.nome(x) for x in m.F] == ["<q0,q1,q2,qf>"]
    for w in lv.palavras(AB, 10):
        assert m.aceita(w) == n.aceita(w) == w.endswith("aaa"), w


def test_afn_com_transicao_vazia_usa_fecho():
    n = lv.AFN(["a", "b", "c"], "x", {("a", lv.VAZIO): {"b"}, ("b", "x"): {"c"}}, "a", {"c"})
    m = n.subconjuntos()
    assert m.q0 == frozenset({"a", "b"}) and m.aceita("x") and not m.aceita("")


def test_afn_afd_exemplo_09_corrigido():
    n = lv.AFN(["q0", "q1", "qf"], "01",
               {("q0", "0"): {"q0", "qf"}, ("q0", "1"): {"qf"}, ("qf", "0"): {"q1"}, ("qf", "1"): {"q1"},
                ("q1", "1"): {"q1"}}, "q0", {"qf"})  # fmt: skip
    m = n.subconjuntos()
    assert {lv.nome(x) for x in m.Q} == {"<q0>", "<q0,qf>", "<qf>", "<q0,q1,qf>", "<q1,qf>", "<q1>", "∅"}
    assert {lv.nome(x) for x in m.F} == {"<qf>", "<q0,qf>", "<q0,q1,qf>", "<q1,qf>"}
    for w in lv.palavras("01", 10):
        assert m.aceita(w) == n.aceita(w), w
    apostila = lv.AFD(m.Q, m.S, m.d, m.q0, [x for x in m.Q if lv.nome(x) in ("<qf>", "<q0,qf>", "<q0,q1,qf>")])
    assert n.aceita("01") and not apostila.aceita("01")
    tem("lfa-afn-para-afd-exemplos-corrigidos", "**quatro** finais", "\\emptyset")


def test_afn_afd_exemplo_11_corrigido():
    n = lv.AFN(["q0", "q1", "q2", "qf"], AB,
               {("q0", "a"): {"q0", "q1"}, ("q0", "b"): {"q0", "q2"}, ("q1", "a"): {"qf"}, ("q2", "b"): {"qf"},
                ("qf", "a"): {"qf"}, ("qf", "b"): {"qf"}}, "q0", {"qf"})  # fmt: skip
    m = n.subconjuntos()
    assert {lv.nome(x) for x in m.Q} == {"<q0>", "<q0,q1>", "<q0,q2>", "<q0,q1,qf>", "<q0,q2,qf>"}
    assert {lv.nome(x) for x in m.F} == {"<q0,q1,qf>", "<q0,q2,qf>"}
    assert len(m.minimo().Q) == 4
    for w in lv.palavras(AB, 10):
        assert m.aceita(w) == ("aa" in w or "bb" in w), w


def test_minimizacao_seis_para_quatro_estados():
    d = {("q0", "a"): "q2", ("q0", "b"): "q1", ("q1", "a"): "q1", ("q1", "b"): "q0", ("q2", "a"): "q4",
         ("q2", "b"): "q5", ("q3", "a"): "q5", ("q3", "b"): "q4", ("q4", "a"): "q3", ("q4", "b"): "q2",
         ("q5", "a"): "q2", ("q5", "b"): "q3"}  # fmt: skip
    m = lv.AFD([f"q{i}" for i in range(6)], AB, d, "q0", {"q0", "q4", "q5"})
    assert m.classes() == [["q0"], ["q1"], ["q2", "q3"], ["q4", "q5"]]
    assert len(m.minimo().Q) == 4 and lv.contraexemplo(m, m.minimo()) is None


# ---------------------------------------------------------------- ER, gramáticas regulares e fechamento


def sem_aa(w):
    return "aa" not in w


def cada_a_com_b(w):
    return all((i > 0 and w[i - 1] == "b") or (i + 1 < len(w) and w[i + 1] == "b") for i, c in enumerate(w) if c == "a")


def test_expressoes_regulares_da_atividade():
    afn = lv.er_para_afn("(b+c+a(b+c))*(λ+a)", "abc")
    for w in lv.palavras("abc", 7):
        assert afn.aceita(w) == sem_aa(w), w
    afn = lv.er_para_afn("λ+(λ+a)(b+ba+baa)*(b+ba)", AB)
    for w in lv.palavras(AB, 11):
        assert afn.aceita(w) == cada_a_com_b(w), w
    errada = lv.er_para_afn("λ+(λ+a)(b+ba+baab)*(b+ba)", AB)
    assert cada_a_com_b("baaba") and not errada.aceita("baaba")
    tem("lfa-expressoes-regulares-sem-aa-cada-a-com-b", "(b + c + a(b+c))^*(\\varepsilon + a)",
        "\\varepsilon + (\\varepsilon + a)(b + ba + baa)^*(b + ba)")  # fmt: skip


def test_gramatica_regular_do_par_de_zeros():
    g = lv.gramatica("P -> 0I | 1P | λ ; I -> 0P | 1I")
    for w in lv.palavras("01", 8):
        assert lv.gera(g, w, "P") == PAR.aceita(w), w
    assert lv.afd_equivale_er(PAR, "(1*01*0)*1*")


def test_produto_comeca_e_termina_com_a():
    m1 = lv.AFD(["q0", "q1", "q2"], AB, {("q0", "a"): "q1", ("q0", "b"): "q2", ("q1", "a"): "q1", ("q1", "b"): "q1",
                                         ("q2", "a"): "q2", ("q2", "b"): "q2"}, "q0", {"q1"})  # fmt: skip
    m2 = lv.AFD(["r0", "r1"], AB, {("r0", "a"): "r1", ("r0", "b"): "r0", ("r1", "a"): "r1", ("r1", "b"): "r0"},
                "r0", {"r1"})  # fmt: skip
    d = {((p, q), a): (m1.d[p, a], m2.d[q, a]) for p in m1.Q for q in m2.Q for a in AB}
    Q = [(p, q) for p in m1.Q for q in m2.Q]
    inter = lv.AFD(Q, AB, d, ("q0", "r0"), [(p, q) for p, q in Q if p in m1.F and q in m2.F])
    uniao = lv.AFD(Q, AB, d, ("q0", "r0"), [(p, q) for p, q in Q if p in m1.F or q in m2.F])
    assert len(inter.acessiveis()) == 5
    assert {x for x in uniao.acessiveis() if x not in uniao.F} == {("q0", "r0"), ("q2", "r0")}
    for w in lv.palavras(AB, 9):
        assert inter.aceita(w) == (w.startswith("a") and w.endswith("a")), w
        assert uniao.aceita(w) == (w.startswith("a") or w.endswith("a")), w


# ---------------------------------------------------------------- não regularidade


def decomposicoes(w, p):
    for i in range(p + 1):
        for j in range(i + 1, p + 1):
            yield w[:i], w[i:j], w[j:]


def test_bombeamento_anbn_para_toda_decomposicao():
    def em_L(s):
        n = len(s) // 2
        return s == "a" * n + "b" * n

    for p in range(1, 9):
        for x, y, z in decomposicoes("a" * p + "b" * p, p):
            assert not em_L(x + y * 2 + z) and not em_L(x + z), (p, x, y)


def test_bombeamento_mesmo_numero_de_a_e_b():
    def em_L(s):
        return s.count("a") == s.count("b")

    for n in range(1, 8):
        assert all(not em_L(u + v * 2 + z) for u, v, z in decomposicoes("a" * n + "b" * n, n))
        assert any(all(em_L(u + v * i + z) for i in range(4)) for u, v, z in decomposicoes("ab" * n, n)) == (n >= 2)


def test_linguagem_infinita_aa_baa():
    m = lv.AFD(["q0", "q1", "q2"], AB, {("q0", "a"): "q1", ("q1", "a"): "q2", ("q2", "b"): "q0"}, "q0", {"q2"})
    assert [w for w in lv.palavras(AB, 6) if m.aceita(w)] == ["aa", "aabaa"]
    assert all(m.aceita("aa" + "baa" * k) for k in range(6))


# ---------------------------------------------------------------- livres de contexto


def test_exemplo_04_nao_e_ambiguo():
    g = lv.gramatica("S -> AT | TB ; T -> aTb | λ ; A -> aA | a ; B -> bB | b")
    for w in lv.palavras(AB, 8):
        n = len(w) - len(w.lstrip("a"))
        esperado = w == "a" * n + "b" * (len(w) - n) and n != len(w) - n
        assert lv.gera(g, w) == esperado, w
        if esperado:
            assert lv.derivacoes_mais_a_esquerda(g, w) == 1, w
    assert lv.derivacoes_mais_a_esquerda(g, "aaab") == 1


def test_ambiguidade_expressoes():
    amb = lv.gramatica("S -> S+S | S*S | (S) | a")
    nao_amb = lv.gramatica("E -> E+T | T ; T -> T*F | F ; F -> (E) | a")
    assert lv.derivacoes_mais_a_esquerda(amb, "a+a*a") == 2
    assert lv.derivacoes_mais_a_esquerda(nao_amb, "a+a*a", "E") == 1
    for w in lv.palavras("a+*", 7):
        assert lv.gera(amb, w) == lv.gera(nao_amb, w, "E"), w
    assert lv.derivacoes_mais_a_esquerda(lv.gramatica("S -> a | S+S"), "a+a+a") == 2
    assert lv.derivacoes_mais_a_esquerda(lv.gramatica("S -> a | a+S"), "a+a+a") == 1


def test_simplificacao_preserva_a_linguagem():
    gs = [lv.gramatica(t) for t in ("S -> aXa | bXb | λ ; X -> a | b | Y ; Y -> ab | λ",
                                    "S -> aXa | bXb | aa | bb | λ ; X -> a | b | Y ; Y -> ab",
                                    "S -> aXa | bXb | aa | bb | λ ; X -> a | b | ab ; Y -> ab")]  # fmt: skip
    esperado = {"", "aa", "bb", "aaa", "aba", "bab", "bbb", "aaba", "babb"}
    for g in gs:
        assert {w for w in lv.palavras(AB, 6) if lv.gera(g, w)} == esperado


def test_forma_normal_de_chomsky():
    original = lv.gramatica("S -> S+S | S*S | [S] | x")
    fnc = lv.gramatica("S -> S D1 | S D2 | C[ D3 | x ; D1 -> C+ S ; D2 -> C* S ; D3 -> S C] ; "
                       "C+ -> + ; C* -> * ; C[ -> [ ; C] -> ]")  # fmt: skip
    producoes = [alt for alts in fnc.values() for alt in alts]
    assert len(producoes) == 11
    assert all((len(a) == 2 and all(s in fnc for s in a)) or (len(a) == 1 and a[0] not in fnc) for a in producoes)
    for w in lv.palavras("x+*[]", 5):
        assert lv.gera(original, w) == lv.gera(fnc, w), w


def test_automato_com_pilha_do_exemplo_19():
    V = lv.VAZIO
    d = {("q0", "a", "0"): [("q1", "10"), ("q3", "")], ("q0", V, "0"): [("q3", "")], ("q1", "a", "1"): [("q1", "11")],
         ("q1", "b", "1"): [("q2", "")], ("q2", "b", "1"): [("q2", "")], ("q2", V, "0"): [("q3", "")]}  # fmt: skip
    aceitas = [w for w in lv.palavras(AB, 6) if lv.ap_aceita(d, "q0", "0", {"q3"}, w)]
    assert aceitas == ["", "a", "ab", "aabb", "aaabbb"]


# ---------------------------------------------------------------- máquinas de Turing

B_ = lv.BRANCO


def _mt_iguais():
    d = {("ini", B_): ("qa", B_, "D"), ("ini", "0"): ("c0", "▷", "D"), ("ini", "1"): ("c1", "▷", "D")}
    for x in "01":
        for y in "01":
            d["c" + x, y] = ("c" + y, x, "D")
        d["c" + x, B_] = ("volta", x, "E")
    d |= {("m", "X"): ("m", "X", "D"), ("m", "0"): ("a1", "X", "D"), ("m", "1"): ("a0", "X", "D"),
          ("m", B_): ("qa", B_, "D")}  # fmt: skip
    for proc, alvo, outro in (("a1", "1", "0"), ("a0", "0", "1")):
        d[proc, outro] = (proc, outro, "D")
        d[proc, "X"] = (proc, "X", "D")
        d[proc, alvo] = ("volta", "X", "E")
        d[proc, B_] = ("qr", B_, "D")
    for s in "01X":
        d["volta", s] = ("volta", s, "E")
    d["volta", "▷"] = ("m", "▷", "D")
    return d


def test_mt_mesmo_numero_de_0_e_1():
    d = _mt_iguais()
    assert len(d) == 25
    for w in lv.palavras("01", 10):
        assert (lv.mt(d, w, inicial="ini")[0] == "qa") == (w.count("0") == w.count("1")), w


def test_mt_insere_separador():
    d = {("q0", "0"): ("q1", "0", "D"), ("q0", "1"): ("q0", "1", "D"), ("q0", B_): ("qa", B_, "D"),
         ("q1", "0"): ("q1", "0", "D"), ("q1", "1"): ("c1", "#", "D"), ("q1", B_): ("qa", B_, "D"),
         ("c1", "0"): ("c0", "1", "D"), ("c1", "1"): ("c1", "1", "D"), ("c1", B_): ("v", "1", "E"),
         ("c0", "0"): ("c0", "0", "D"), ("c0", "1"): ("c1", "0", "D"), ("c0", B_): ("v", "0", "E"),
         ("v", "0"): ("v", "0", "E"), ("v", "1"): ("v", "1", "E"), ("v", "#"): ("q0", "#", "D")}  # fmt: skip
    assert len(d) == 15
    for w in lv.palavras("01", 9):
        estado, fita = lv.mt(d, w)
        assert estado == "qa" and fita == w.replace("01", "0#1"), w
    assert lv.mt(d, "0101")[1] == "0#10#1"


def test_mt_cabeca_fica_na_primeira_celula():
    d = {("q0", "0"): ("q1", "0", "E"), ("q1", "0"): ("qa", "1", "D")}
    assert lv.mt(d, "0") == ("qa", "1")


# ---------------------------------------------------------------- programas LPM e funções recursivas

_n = [0]


def dec(x):
    """x ← x ∸ 1 só com zero, inc, copia e LOOP."""
    _n[0] += 1
    a, b = f"_a{_n[0]}", f"_b{_n[0]}"
    return [("zero", a), ("zero", b), ("loop", x, [("copia", b, a), ("inc", a)]), ("copia", x, b)]


def e_zero(u, x):
    return [("zero", u), ("inc", u), ("loop", x, [("zero", u)])]


def mult(s, t, y):
    return [("zero", s), ("loop", t, [("loop", y, [("inc", s)])])]


def monus(d, s, x):
    return [("copia", d, s), ("loop", x, dec(d))]


ALUNO = [("zero", "Z"), ("copia", "T", "X"),
         ("loop", "X", [*mult("S", "T", "Y"), *monus("D", "X", "S"), *e_zero("E", "D"),
                        ("loop", "E", [("copia", "Z", "T")]), *dec("T")])]  # fmt: skip
CORRIGIDO = [("zero", "Z"), ("zero", "T"),
             ("loop", "X", [("inc", "T"), *mult("S", "T", "Y"), *monus("D", "S", "X"), *e_zero("E", "D"),
                            ("loop", "E", [("inc", "Z")])]),
             *e_zero("H", "Y"), ("loop", "H", [("zero", "Z")])]  # fmt: skip


def test_divisao_inteira_em_lpm():
    erros = 0
    for x in range(10):
        for y in range(6):
            certo = x // y if y else 0
            assert lv.lpm(CORRIGIDO, X=x, Y=y)["Z"] == certo, (x, y)
            aluno = lv.lpm(ALUNO, X=x, Y=y)["Z"]
            assert aluno == ((-(-x // y)) if y else 0), (x, y)
            if x < 8 and y < 5:
                erros += aluno != certo
    assert erros == 15
    assert lv.lpm(ALUNO, X=7, Y=2)["Z"] == 4
    tem("lfa-lpm-divisao-inteira-loop-sem-goto", "15 dos 40", "\\lceil X/Y \\rceil")


def test_para_passo_2_e_while():
    corpo = [("loop", "X", [("inc", "soma")]), ("inc", "vezes")]
    para = [("zero", "X"), *[("inc", "X")] * 5, ("rotulo", "L"), ("zero", "J"), *[("inc", "J")] * 10,
            ("copia", "M", "X"), ("loop", "J", dec("M")), *e_zero("Lb", "M"),
            ("loop", "Lb", [*corpo, ("inc", "X"), ("inc", "X"), ("goto", "L")])]  # fmt: skip
    v = lv.lpm(para)
    assert (v["vezes"], v["soma"], v["X"]) == (3, 5 + 7 + 9, 11)
    sem_goto = [("zero", "X"), *[("inc", "X")] * 5, ("zero", "N"), *[("inc", "N")] * 3,
                ("loop", "N", [*corpo, ("inc", "X"), ("inc", "X")])]  # fmt: skip
    w = lv.lpm(sem_goto)
    assert (w["vezes"], w["soma"], w["X"]) == (3, 21, 11)
    enquanto = [("rotulo", "L"), ("se_zero_goto", "x", "FIM"), *dec("x"), ("goto", "L"), ("rotulo", "FIM")]
    assert all(lv.lpm(enquanto, x=k)["x"] == 0 for k in range(21))


def test_funcoes_recursivas_primitivas():
    dois = lv.comp(lv.suc, lv.comp(lv.suc, lv.zero))
    f = (lv.comp(lv.SOMA, lv.proj(0), lv.proj(1)),
         lv.comp(lv.SOMA, lv.proj(1), lambda *xs: lv.MULT(dois(*xs), xs[2])),
         lv.comp(lv.POT, lv.proj(2), lv.proj(2)))  # fmt: skip

    def t(x, y, z):
        v = lv.MONUS(y, x)
        return lv.MULT(lv.SG(v), lv.SG(lv.MONUS(v, z)))

    for x, y, z in product(range(6), repeat=3):
        assert tuple(g(x, y, z) for g in f) == (x + y, y + 2 * z, z**z)
        assert t(x, y, z) == int(0 < x - y < z), (x, y, z)
        assert lv.PRED(x) == max(x - 1, 0) and lv.MONUS(y, x) == max(x - y, 0)


def test_prova2_funcao_f():
    prog = [("copia", "s1", "x"), ("loop", "y", [("inc", "s1")]), ("loop", "z", [("inc", "s1")]),
            ("zero", "s2"), ("loop", "z", [("inc", "s2"), ("inc", "s2")]),
            ("copia", "s3", "x"), ("inc", "s3"), ("inc", "s3"),
            ("copia", "s4", "y"), ("loop", "y", [("inc", "s4")])]  # fmt: skip
    for x, y, z in product(range(6), repeat=3):
        v = lv.lpm(prog, x=x, y=y, z=z)
        esperado = (x + y + z, 2 * z, x + 2, 2 * y)
        assert (v["s1"], v["s2"], v["s3"], v["s4"]) == esperado
        assert (lv.SOMA(lv.SOMA(x, y), z), lv.SOMA(z, z), lv.suc(lv.suc(x)), lv.SOMA(y, y)) == esperado
    tem("lfa-prova2-funcao-f-quatro-componentes", "(6, 6, 3, 4)")


# ---------------------------------------------------------------- decidibilidade


def test_enumeracao_e_diagonal():
    lista = list(lv.palavras("01", 6))
    for n in range(7):
        assert lista.index("0" * n) == 2**n - 1
    linguagens = [{w for w in lista[:8] if (hash((k, w)) ^ k) % 2} for k in range(8)]
    diagonal = {lista[k] for k in range(8) if lista[k] not in linguagens[k]}
    assert all((lista[k] in diagonal) != (lista[k] in linguagens[k]) for k in range(8))


def test_decisores_de_afd_e_er():
    assert lv.er_gera("(1*01*0)*1*", "1001", "01") and not lv.er_gera("(1*01*0)*1*", "10", "01")
    assert lv.afd_equivale_er(PAR, "(1*01*0)*1*") and lv.afd_equivale_er(PAR, "(1+01*0)*")
    assert not lv.afd_equivale_er(PAR, "(00)*1*")
    assert lv.contraexemplo(PAR, lv.er_para_afn("(00)*1*", "01").subconjuntos()) == "010"
    tudo = lv.AFD(["u"], AB, {("u", "a"): "u", ("u", "b"): "u"}, "u", {"u"})
    assert lv.afd_aceita_tudo(tudo) and not lv.afd_aceita_tudo(PAR)
    assert not lv.afd_aceita_tudo(lv.AFD(["u"], AB, {("u", "a"): "u"}, "u", {"u"}))


def test_diagonal_do_problema_da_parada():
    tabela = [[(i * 7 + j * 3) % 2 == 0 for j in range(8)] for i in range(8)]
    d = [not tabela[i][i] for i in range(8)]
    assert all(d != linha for linha in tabela)


# ---------------------------------------------------------------- fórmulas, catálogo e restrições

FORMULA = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in TODOS.values():
        assert i["texto"].count("$") % 2 == 0, i["id"]


@pytest.mark.skipif(not shutil.which("node"), reason="node indisponível")
def test_formulas_renderizam_no_katex_do_site():
    textos = [i["texto"] for i in TODOS.values()] + [LFA.rigor]
    formulas = [a or b for t in textos for a, b in FORMULA.findall(t)]
    assert len(formulas) >= 50
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
        assert set(f["topicos"]) <= set(LFA.assuntos), f["id"]
    citadas = {x for i in TODOS.values() for x in i["fontes_catalogo"]}
    assert citadas <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f["uso"] == "acervo"} <= citadas
    for protegido in ("sipser-livro", "menezes-livro", "hopcroft", "diverio-menezes"):
        f = CATALOGO[protegido]
        assert f["uso"] == "referencia" and f["acesso"].startswith("Não incluído") and not f["url"]
    assert "Eliana" in CATALOGO["ufal-eliana-lista-2014-1"]["autoria"]


def _palavras_hash(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return {hashlib.sha256(p.encode()).hexdigest()[:16] for p in re.findall(r"[a-z]+", t)}


# Primeiro nome do aluno que resolveu a lista de 2014.1 (aparece no nome do arquivo), guardado só como hash.
NOME_DO_ALUNO = {"10b05c446ea776cd"}
MATRICULAS = re.compile(r"\b14130254\b")


def test_originais_e_dados_pessoais_fora_do_repositorio():
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()]
    assert not [
        p
        for p in arquivos
        if p.suffix.lower() in (".pdf", ".doc", ".docx", ".jar", ".png", ".jpg", ".jpeg", ".heic", ".webp", ".zip")
    ]
    proibidos = re.compile(r"(?i)[\w.]+@[\w-]+\.\w+|groups\.google|dropbox|sites\.google|whatsapp|aluno:\s*\w")
    for p in [
        *LFA.materiais.glob("*.md"),
        LFA.itens,
        PASTA / "rigor.md",
        PASTA / "CURADORIA.md",
        PASTA / "fontes.json",
    ]:
        conteudo = p.read_text(encoding="utf-8")
        assert not proibidos.search(conteudo), p.name
        assert not MATRICULAS.search(conteudo), p.name
        assert not _palavras_hash(conteudo) & NOME_DO_ALUNO, p.name
    for i in TODOS.values():
        assert "http" not in i["texto"], i["id"]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert [i for i in CATALOGO if f"`{i}`" not in curadoria] == []
    assert [i for i in TODOS if f"`{i}`" not in curadoria] == []
    assert "`lfa`" in (ROOT / "docs/DISCIPLINAS.md").read_text(encoding="utf-8")
