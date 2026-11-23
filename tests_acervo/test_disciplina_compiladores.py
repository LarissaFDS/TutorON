"""Acervo de Compiladores (Ciência da Computação) e conferência dos exercícios em Python.

Os blocos parafraseiam as provas de Compiladores do IC-UFAL (2013 a 2017.1), os enunciados dos trabalhos de
2017.1 e as provas de 2009 e 2010 do Prof. Marcus Ramos que estão na pasta da turma. FIRST, FOLLOW, tabelas
LL(1) e SLR(1), precedência de operadores, geração de código e verificação de tipos são refeitos aqui.
"""

import itertools
import random
import re

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

COMP = disciplinas.obter("compiladores")
PASTA = ROOT / "disciplinas/compiladores"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(COMP.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "compiladores")
FRONTEIRA = ("lfa", "clp", "paa")
TEXTO = " ".join(i["texto"] for i in TODOS.values())


def buscar(pergunta, d=COMP):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def bloco(prefixo):
    return next(i["texto"] for k, i in TODOS.items() if k.startswith(prefixo))


# ---------------------------------------------------------------- cadastro e acervo


def test_compiladores_cadastrada_com_acervo_proprio():
    assert COMP.nome == "Compiladores" and COMP.itens.exists()
    ids = {c["id"] for c in read_json(COMP.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({COMP.itens, COMP.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(COMP.assuntos)
    assert ids == set(TODOS)


def test_situacao_da_disciplina():
    assert COMP.situacao == "MVP" and not COMP.em_validacao and not COMP.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas compiladores --embeddings`."""
    assert disciplinas.registros(COMP) == read_json(COMP.itens)


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


def test_sem_dados_pessoais_livro_audio_nem_binarios():
    textos = TEXTO + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"matr[ií]c(ula)?\.?:? *\d", textos, re.I)
    # alunos que aparecem nas cópias de provas, respostas e trabalhos
    for nome in ("Luiz Carvalho", "Harnon", "Vanessa", "Maxwell", "Roland", "Leonildo", "Adeilson", "Arthur", "Dalton", "Helynne"):
        assert nome not in textos
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"].startswith("Protegido"):
            assert f["uso"] == "referencia", f["id"]
    exts = (".pdf", ".docx", ".odt", ".xlsx", ".png", ".jpg", ".jpeg", ".m4a", ".mp3", ".zip", ".o", ".class")
    assert not [p for p in PASTA.rglob("*") if p.suffix.lower() in exts]
    for padrao in ("*Price*Toscani*", "*Principios*Tecnicas*Ferramentas*", "*Princípios*técnicas*", "Voz 0*", "*AudiosAB2*"):
        assert not list(ROOT.rglob(padrao)), padrao


PERGUNTAS = [
    ("O que é bootstrapping de compiladores?", "comp-conceitos"),
    ("Qual a diferença entre fases e passos de compilação?", "comp-conceitos"),
    ("Como representar um compilador com diagramas T?", "comp-conceitos"),
    ("Qual o papel do analisador léxico e como ele coopera com o sintático?", "comp-analise-lexica"),
    ("Como reconhecer números com expoente usando expressão regular?", "comp-analise-lexica"),
    ("Como calcular os conjuntos FIRST e FOLLOW?", "comp-conjuntos-first"),
    ("Essa gramática é LL(1)?", "comp-conjuntos-first"),
    ("Como eliminar a recursão à esquerda e fatorar a gramática?", "comp-transformar-gramatica"),
    ("Como montar a tabela do analisador preditivo tabular?", "comp-analisador-descendente"),
    ("analisador descendente recursivo", "comp-analisador-descendente"),
    ("Como funciona a análise de precedência de operadores?", "comp-analisador-de-precedencia"),
    ("O que é uma gramática de operadores?", "comp-analisador-de-precedencia"),
    ("Como montar a tabela SLR(1) com itens LR(0)?", "comp-analise-ascendente"),
    ("O que é handle na análise ascendente empilha e reduz?", "comp-analise-ascendente"),
    ("Qual a diferença entre atributos herdados e sintetizados?", "comp-traducao-dirigida"),
    ("Como gerar código para o comando repeat until?", "comp-geracao-de-codigo-para-comandos"),
    ("Quantas iterações tem um laço controlado por contador?", "comp-geracao-de-codigo-para-comandos"),
    ("Como gerar código de três endereços para uma expressão?", "comp-codigo-de-tres-enderecos"),
    ("Qual a diferença entre a AST e o grafo de sintaxe DAG?", "comp-codigo-de-tres-enderecos"),
    ("Como fazer a verificação de tipos com coerção convreal?", "comp-analise-semantica"),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    achados = buscar(pergunta)[:3]
    assert any(a.startswith(esperado) for a in achados), achados


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Como montar a tabela SLR(1) com itens LR(0)?", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a impedância de um indutor?")
    assert not buscar("Me conte uma piada")


# ---------------------------------------------------------------- ferramentas de gramática
# Gramática: dict não-terminal -> lista de alternativas (tuplas de símbolos); () é a vazia.

FIM = "$"


def first_follow(g, inicio):
    first = {a: set() for a in g}

    def first_seq(seq):
        r = set()
        for s in seq:
            f = first[s] if s in g else {s}
            r |= f - {""}
            if "" not in f:
                return r
        return r | {""}

    mudou = True
    while mudou:
        mudou = False
        for a, alts in g.items():
            for alt in alts:
                f = first_seq(alt)
                if not f <= first[a]:
                    first[a] |= f
                    mudou = True
    follow = {a: set() for a in g}
    follow[inicio].add(FIM)
    mudou = True
    while mudou:
        mudou = False
        for a, alts in g.items():
            for alt in alts:
                for i, s in enumerate(alt):
                    if s not in g:
                        continue
                    f = first_seq(alt[i + 1 :])
                    novo = (f - {""}) | (follow[a] if "" in f else set())
                    if not novo <= follow[s]:
                        follow[s] |= novo
                        mudou = True
    return first_seq, first, follow


def tabela_ll1(g, inicio):
    first_seq, _, follow = first_follow(g, inicio)
    tab, conflitos = {}, []
    for a, alts in g.items():
        for alt in alts:
            f = first_seq(alt)
            for t in (f - {""}) | (follow[a] if "" in f else set()):
                if (a, t) in tab:
                    conflitos.append((a, t))
                tab[(a, t)] = alt
    return tab, conflitos


def preditivo(g, inicio, tokens):
    tab, _ = tabela_ll1(g, inicio)
    pilha, entrada, usadas = [FIM, inicio], [*tokens, FIM], []
    while pilha:
        topo, tk = pilha.pop(), entrada[0]
        if topo not in g:
            if topo != tk:
                return None
            entrada.pop(0)
        elif (topo, tk) in tab:
            alt = tab[(topo, tk)]
            usadas.append((topo, alt))
            pilha.extend(reversed(alt))
        else:
            return None
    return usadas


def linguagem(g, inicio, n):
    """Cadeias de terminais de tamanho <= n (busca em largura nas formas sentenciais)."""
    vistas, saida, fila = set(), set(), [(inicio,)]
    while fila:
        f = fila.pop()
        if f in vistas or sum(s not in g for s in f) > n or len(f) > n + 4:
            continue
        vistas.add(f)
        i = next((k for k, s in enumerate(f) if s in g), None)
        if i is None:
            saida.add("".join(f))
            continue
        fila.extend(f[:i] + alt + f[i + 1 :] for alt in g[f[i]])
    return saida


# ---------------------------------------------------------------- conferências


def test_diagramas_t():
    def compila(prog, comp):  # prog e comp = (fonte, objeto, escrito_em); x86n = código x86 não otimizado
        assert prog[2] == comp[0] and comp[2].startswith("x86")
        return (prog[0], prog[1], "x86")

    c = compila(("Java1", "x86n", "C"), ("C", "x86", "x86"))
    assert c == ("Java1", "x86n", "x86")
    for velho, novo in (("Java1", "Java2"), ("Java2", "Java")):
        c = compila((novo, "x86n", velho), c)
        assert c == (novo, "x86n", "x86")
    otim = compila(("Java", "x86", "Java"), c)
    assert compila(("Java", "x86", "Java"), otim) == ("Java", "x86", "x86")
    t = bloco("comp-conceitos")
    assert "Java1/x86n/x86" in t and "erros de sintaxe" in t


def test_reconhecedor_de_numeros():
    t = bloco("comp-analise-lexica")
    codigo = re.search(r"```python\n(.+?)```", t, re.S).group(1)
    ns = {}
    exec(codigo, ns)  # noqa: S102 - código do próprio bloco
    numero = ns["numero"]
    er = re.compile(r"[+-]?(\d+(\.\d*)?|\.\d+)(e[+-]?\d+)?")
    for s in ("123", "-45.312", "+.76", "5.44e2", "+0.88e-35"):
        assert numero(s) and er.fullmatch(s), s
    for s in (".", "e5", "1e", "+-1", "", "1.2.3"):
        assert not numero(s) and not er.fullmatch(s), s
    alfabeto = "+-.e1"
    for n in range(1, 6):
        for tup in itertools.product(alfabeto, repeat=n):
            s = "".join(tup)
            assert numero(s) == bool(er.fullmatch(s)), s
    g = {"S": [("W", "Z")], "W": [("X",), ("Y",)], "X": [("x",), ("x", "X")], "Y": [("y",), ("y", "Y")], "Z": [("z",), ("z", "Z")]}
    assert linguagem(g, "S", 5) == {s for n in range(2, 6) for s in map("".join, itertools.product("xyz", repeat=n)) if re.fullmatch(r"(x+|y+)z+", s)}


def test_first_follow_ll1():
    g = {
        "S": [("b", "X", "c"), ("a", "a", "Y", "c", "b"), ("c", "c", "Z", "a", "a")],
        "X": [("a", "b", "c"), ()],
        "Y": [("a", "Y"), ("b", "Y"), ()],
        "Z": [("X", "b"), ("c", "Y", "c")],
    }
    first_seq, _, follow = first_follow(g, "S")
    assert follow["X"] == {"b", "c"} and follow["Y"] == {"c"}
    assert first_seq(("X", "b")) == {"a", "b"}
    assert tabela_ll1(g, "S")[1] == []
    g2 = {"S": [("a", "b", "X", "c"), ("a", "a", "Y", "b", "c"), ("c", "c", "Z", "a", "a")], "X": [("X", "c"), ("a", "b", "c"), ()], "Y": [("a", "Y"), ("b", "Y"), ()], "Z": [("X", "c"), ("c", "Y", "a")]}
    assert ("S", "a") in tabela_ll1(g2, "S")[1]
    g3 = {"S": [("A", "b")], "A": [("a",), ("B",), ()], "B": [("b",), ()]}
    _, _, f3 = first_follow(g3, "S")
    assert f3["A"] == {"b"} and tabela_ll1(g3, "S")[1]
    g4 = {"S": [("a", "S", "e"), ("B",)], "B": [("b", "B", "e"), ("C",)], "C": [("c", "B", "e"), ("d",)]}
    assert tabela_ll1(g4, "S")[1] == []
    t = bloco("comp-conjuntos-first")
    assert "FOLLOW$(X) = \\{b, c\\}$" in t


def test_transformacao_ll1():
    orig = {"S": [("a", "X", "b"), ("a", "Y", "c"), ("a", "a", "Z", "d")], "X": [("b", "X"), ("b", "c")], "Y": [("c", "Y"), ("c", "b")], "Z": [("d", "Z"), ()]}
    nova = {
        "S": [("a", "S'")],
        "S'": [("X", "b"), ("Y", "c"), ("a", "d", "Z")],
        "X": [("b", "X'")],
        "X'": [("X",), ("c",)],
        "Y": [("c", "Y'")],
        "Y'": [("Y",), ("b",)],
        "Z": [("d", "Z"), ()],
    }
    assert tabela_ll1(orig, "S")[1]
    assert tabela_ll1(nova, "S")[1] == []
    _, _, fo = first_follow(orig, "S")
    assert fo["Z"] == {"d"}
    assert linguagem(orig, "S", 8) == linguagem(nova, "S", 8)
    for s in linguagem(nova, "S", 8):
        assert preditivo(nova, "S", list(s)) is not None, s


EXPR = {
    "E": [("T", "E'")],
    "E'": [("+", "T", "E'"), ()],
    "T": [("F", "T'")],
    "T'": [("*", "F", "T'"), ()],
    "F": [("(", "E", ")"), ("id",)],
}


def test_preditivo_tabular():
    tab, conf = tabela_ll1(EXPR, "E")
    assert conf == []
    assert tab[("E'", ")")] == () and tab[("T'", "+")] == () and tab[("F", "(")] == ("(", "E", ")")
    assert len(tab) == 13
    usadas = preditivo(EXPR, "E", ["id", "+", "id", "*", "id"])
    assert len(usadas) == 11
    assert [a for a, _ in usadas] == ["E", "T", "F", "T'", "E'", "T", "F", "T'", "F", "T'", "E'"]
    assert preditivo(EXPR, "E", ["id", "+", "*", "id"]) is None
    assert preditivo(EXPR, "E", ["(", "id", ")", "*", "id"]) is not None


def test_precedencia_de_operadores():
    prec = {"+": (1, "esq"), "*": (2, "esq"), "^": (3, "dir")}

    def rel(a, b):  # relação entre o terminal da pilha (a) e o token (b)
        if a == "$":
            return "<" if b != "$" else "ok"
        if b == "$":
            return ">"
        if a == "id":
            return ">"
        if b == "id":
            return "<"
        (pa, assoc), (pb, _) = prec[a], prec[b]
        if pa != pb:
            return ">" if pa > pb else "<"
        return ">" if assoc == "esq" else "<"

    def analisa(tokens):
        pilha, ent, reducoes = ["$"], [*tokens, "$"], []
        while True:
            a = next(s for s in reversed(pilha) if s != "E")
            r = rel(a, ent[0])
            if r == "ok":
                return reducoes
            if r == "<":
                pilha.append(ent.pop(0))
            else:
                if pilha[-1] == "id":
                    pilha[-1] = "E"
                    reducoes.append("id")
                else:
                    assert pilha[-3:-2] == ["E"] and pilha[-1] == "E"
                    reducoes.append(f"E{pilha[-2]}E")
                    del pilha[-3:]
                    pilha.append("E")

    assert analisa(["id", "+", "id", "*", "id"]) == ["id", "id", "id", "E*E", "E+E"]
    assert analisa(["id", "*", "id", "+", "id"]) == ["id", "id", "E*E", "id", "E+E"]
    assert analisa(["id", "^", "id", "^", "id"]) == ["id", "id", "id", "E^E", "E^E"]
    # questão 9: gramática b) é LL(1), respeita a precedência e recusa opr encadeado
    g = {
        "Eb": [("Rel", "Or'")],
        "Or'": [("or", "Rel", "Or'"), ()],
        "Rel": [("Not", "Rel'")],
        "Rel'": [("opr", "Not"), ()],
        "Not": [("not", "Not"), ("true",), ("false",), ("id",)],
    }
    assert tabela_ll1(g, "Eb")[1] == []
    assert preditivo(g, "Eb", ["not", "id", "opr", "id", "or", "true"]) is not None
    assert preditivo(g, "Eb", ["id", "opr", "id", "opr", "id"]) is None
    assert preditivo(g, "Eb", ["id", "or", "id", "or", "not", "not", "id"]) is not None
    # gramática original é de operadores: sem não-terminais vizinhos e sem vazia
    orig = [["Eb", "or", "Eb"], ["Eb", "opr", "Eb"], ["not", "Eb"], ["true"], ["false"], ["id"]]
    assert all(p and not any(a == b == "Eb" for a, b in itertools.pairwise(p)) for p in orig)


def test_slr():
    g = [("S'", ("E",)), ("E", ("E", "+", "T")), ("E", ("T",)), ("T", ("T", "*", "F")), ("T", ("F",)), ("F", ("(", "E", ")")), ("F", ("id",))]
    nts = {a for a, _ in g}

    def fecho(itens):
        itens = set(itens)
        mudou = True
        while mudou:
            mudou = False
            for p, k in list(itens):
                corpo = g[p][1]
                if k < len(corpo) and corpo[k] in nts:
                    for q, (a, _) in enumerate(g):
                        if a == corpo[k] and (q, 0) not in itens:
                            itens.add((q, 0))
                            mudou = True
        return frozenset(itens)

    def vai(itens, x):
        return fecho({(p, k + 1) for p, k in itens if k < len(g[p][1]) and g[p][1][k] == x})

    estados = [fecho({(0, 0)})]
    trans = {}
    for i in itertools.count():
        if i == len(estados):
            break
        simbolos = {g[p][1][k] for p, k in estados[i] if k < len(g[p][1])}
        for x in sorted(simbolos):
            j = vai(estados[i], x)
            if j not in estados:
                estados.append(j)
            trans[(i, x)] = estados.index(j)
    assert len(estados) == 12
    gd = {}
    for a, corpo in g[1:]:
        gd.setdefault(a, []).append(corpo)
    _, _, follow = first_follow(gd, "E")
    action = {}
    for i, est in enumerate(estados):
        for p, k in est:
            a, corpo = g[p]
            if k < len(corpo):
                if corpo[k] not in nts:
                    mov = ("e", trans[(i, corpo[k])])
                    assert action.get((i, corpo[k]), mov) == mov
                    action[(i, corpo[k])] = mov
            elif p == 0:
                action[(i, FIM)] = ("aceita",)
            else:
                for t in follow[a]:
                    assert (i, t) not in action, "conflito SLR"
                    action[(i, t)] = ("r", p)
    pilha, ent, red = [0], ["id", "*", "id", "+", "id", FIM], []
    while True:
        mov = action[(pilha[-1], ent[0])]
        if mov[0] == "aceita":
            break
        if mov[0] == "e":
            pilha.append(mov[1])
            ent.pop(0)
        else:
            a, corpo = g[mov[1]]
            del pilha[len(pilha) - len(corpo) :]
            pilha.append(trans[(pilha[-1], a)])
            red.append(f"{a}->{''.join(corpo)}")
    assert red == ["F->id", "T->F", "F->id", "T->T*F", "E->T", "F->id", "T->F", "E->E+T"]
    assert "**12 estados**" in bloco("comp-analise-ascendente")


def executa(codigo, mem):
    """Executa uma lista de instruções: ('rot', L), ('goto', L), ('if>', a, b, L), ('=', destino, expr)."""
    rot = {ins[1]: k for k, ins in enumerate(codigo) if ins[0] == "rot"}
    pc, passos = 0, 0
    while pc < len(codigo):
        ins = codigo[pc]
        passos += 1
        assert passos < 10_000
        if ins[0] == "goto":
            pc = rot[ins[1]]
            continue
        if ins[0] == "if>":
            if mem[ins[1]] > mem[ins[2]]:
                pc = rot.get(ins[3], len(codigo))
                continue
        elif ins[0] == "iff":  # desvia para o rótulo do caso: ('iff', condição, rótulo_true, rótulo_false)
            pc = rot.get(ins[2] if ins[1](mem) else ins[3], len(codigo))
            continue
        elif ins[0] == "=":
            mem[ins[1]] = ins[2](mem)
        pc += 1
    return mem


def test_if_then_else():
    def se(cond, l1, l2=None):
        prox, t, f = "fim", "Ltrue", "Lfalse"
        el = [("iff", cond, t, f if l2 else prox)]
        if l2 is None:
            return [*el, ("rot", t), *l1, ("rot", prox)]
        sr = [("rot", f), *l2]
        return [*el, ("rot", t), *l1, ("goto", prox), *sr, ("rot", prox)]

    um = [("=", "y", lambda m: 1)]
    dois = [("=", "y", lambda m: 2)]
    assert executa(se(lambda m: m["x"] > 0, um, dois), {"x": 5, "y": 0})["y"] == 1
    assert executa(se(lambda m: m["x"] > 0, um, dois), {"x": -5, "y": 0})["y"] == 2
    assert executa(se(lambda m: m["x"] > 0, um), {"x": -5, "y": 0})["y"] == 0
    t = bloco("comp-traducao-dirigida")
    assert "`Sr = end | else L end`" in t and "Sr.false = EL.false" in t


def test_lacos():
    # repeat i = i + 1 until i >= 3 (esquema da resolução correta)
    repeat = [("rot", "Lfalse"), ("=", "i", lambda m: m["i"] + 1), ("rot", "Lprox"), ("iff", lambda m: m["i"] >= 3, "fim", "Lfalse"), ("rot", "fim")]
    assert executa(repeat, {"i": 0})["i"] == 3
    assert executa(repeat, {"i": 7})["i"] == 8  # o corpo roda ao menos uma vez

    def para(i0, fim, passo):
        cod = [
            ("=", "i", lambda m: i0),
            ("goto", "prim"),
            ("rot", "Lprox"),
            ("=", "i", lambda m: m["i"] + passo),
            ("rot", "prim"),
            ("=", "lim", lambda m: fim),
            ("if>", "i", "lim", "Sprox"),
            ("=", "voltas", lambda m: m["voltas"] + 1),
            ("goto", "Lprox"),
            ("rot", "Sprox"),
        ]
        return executa(cod, {"voltas": 0})["voltas"]

    for i0, fim, k in [(1, 10, 3), (1, 9, 3), (5, 1, 1), (0, 0, 2), (2, 20, 5)]:
        n = max(0, (fim - i0 + k) // k)
        assert para(i0, fim, k) == n == len(range(i0, fim + 1, k)), (i0, fim, k)
    assert para(1, 10, 3) == 4


def test_tres_enderecos():
    quad = [("*", "a", "b", "T1"), ("+", "T1", "c", "T2"), ("+", "b", "c", "T3"), ("/", "T3", "d", "T4"), ("-", "T2", "T4", "T5"), ("=", "T5", None, "x")]
    ops = {"*": lambda p, q: p * q, "+": lambda p, q: p + q, "/": lambda p, q: p / q, "-": lambda p, q: p - q}
    rnd = random.Random(7)
    for _ in range(50):
        m = {v: rnd.uniform(1, 9) for v in "abcd"}
        for op, a1, a2, r in quad:
            m[r] = m[a1] if op == "=" else ops[op](m[a1], m[a2])
        a, b, c, d = (m[v] for v in "abcd")
        assert abs(m["x"] - (a * b + c - (b + c) / d)) < 1e-9
    t = bloco("comp-codigo-de-tres-enderecos")
    assert "| 4 | - | T2 | T4 | T5 |" in t


def test_verificacao_de_tipos():
    simbolos = {"i": "Int", "r": "Real"}

    class ErroTipo(Exception):
        pass

    def gera(atrib):
        alvo, expr = atrib
        cod, n = [], [0]

        def temp():
            n[0] += 1
            return f"t{n[0]}"

        def visita(e):
            if isinstance(e, str):
                tipo = simbolos.get(e, "Indef")
                if tipo == "Indef":
                    raise ErroTipo(e)
                return tipo, e
            op, esq, dir_ = e
            (te, ne), (td, nd) = visita(esq), visita(dir_)
            if te == td == "Int":
                r = temp()
                cod.append(f"{r} = {ne} {op}int {nd}")
                return "Int", r
            if te == "Int":
                t = temp()
                cod.append(f"{t} = convreal {ne}")
                ne = t
            if td == "Int":
                t = temp()
                cod.append(f"{t} = convreal {nd}")
                nd = t
            r = temp()
            cod.append(f"{r} = {ne} {op}real {nd}")
            return "Real", r

        tipo, nome = visita(expr)
        ta = simbolos.get(alvo, "Indef")
        if ta == "Indef" or (ta == "Int" and tipo == "Real"):
            raise ErroTipo(alvo)
        if ta == "Real" and tipo == "Int":
            t = temp()
            cod.append(f"{t} = convreal {nome}")
            nome = t
        cod.append(f"{alvo} ={ta.lower()} {nome}")
        return cod

    # r = i + r * i: a multiplicação é avaliada antes (filho direito de +)
    cod = gera(("r", ("+", "i", ("*", "r", "i"))))
    assert cod == ["t1 = convreal i", "t2 = r *real t1", "t3 = convreal i", "t4 = t3 +real t2", "r =real t4"]
    assert gera(("i", ("+", "i", "i"))) == ["t1 = i +int i", "i =int t1"]
    with pytest.raises(ErroTipo):
        gera(("i", "r"))
    with pytest.raises(ErroTipo):
        gera(("r", ("+", "z", "i")))
    t = bloco("comp-analise-semantica")
    assert "t4 = t3 +real t2" in t and "estreitamento" in t
