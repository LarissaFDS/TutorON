"""Acervo de Conceitos de Linguagens de Programação (Ciência da Computação) e conferência das resoluções.

Os blocos parafraseiam as provas do Prof. Alcino Dall'Igna Jr. (IC-UFAL). Os exemplos em C são
compilados aqui com o gcc (pulados se não houver compilador); Ruby, Haskell e Prolog, que não estão
no ambiente de testes, são reproduzidos em Python com a mesma semântica.
"""

import gc
import keyword
import re
import shutil
import subprocess
import weakref

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

CLP = disciplinas.obter("clp")
PASTA = ROOT / "disciplinas/clp"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(CLP.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "clp")
FRONTEIRA = ("prog1", "lfa", "projsw")


def buscar(pergunta, d=CLP):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def compilar_c(codigo, tmp_path, nome="p"):
    if not shutil.which("gcc"):
        pytest.skip("gcc não encontrado")
    fonte = tmp_path / f"{nome}.c"
    fonte.write_text(codigo, encoding="utf-8")
    exe = tmp_path / f"{nome}.exe"
    return subprocess.run(["gcc", "-std=c99", "-Wall", "-o", str(exe), str(fonte)], capture_output=True, text=True), exe


def rodar_c(codigo, tmp_path, nome="p"):
    r, exe = compilar_c(codigo, tmp_path, nome)
    assert r.returncode == 0, r.stderr
    p = subprocess.run([str(exe)], capture_output=True, text=True, timeout=30)
    return p.returncode, p.stdout.split(), r.stderr


# ---------------------------------------------------------------- cadastro e acervo


def test_clp_cadastrada_com_acervo_proprio():
    assert CLP.nome == "Conceitos de Linguagens de Programação" and CLP.itens.exists()
    ids = {c["id"] for c in read_json(CLP.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({CLP.itens, CLP.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(CLP.assuntos)
    assert ids == set(TODOS)
    cursos = (ROOT / "disciplinas/cursos.json").read_text(encoding="utf-8")
    # sem ligação em cursos.json: o 4º período de CC mudaria as preferidas fixadas em test_versao_final (ver CURADORIA.md)
    assert cursos.count('"acervo": "clp"') == 0


def test_situacao_da_disciplina():
    assert CLP.situacao == "MVP" and not CLP.em_validacao and not CLP.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas clp --embeddings`."""
    assert disciplinas.registros(CLP) == read_json(CLP.itens)


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
    for nome in ("Rubem", "Vanessa", "Rivo", "Daniel Borges", "Luiz Felipe"):
        assert nome not in textos
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"] == "Protegido" or f["id"] == "turma-respostas-e-trabalhos-clp":
            assert f["uso"] == "referencia", f["id"]
    soltos = [
        p
        for p in PASTA.rglob("*")
        if p.suffix.lower() in (".pdf", ".docx", ".ppt", ".pptx", ".png", ".jpg", ".jpeg", ".tex")
    ]
    assert not soltos


PERGUNTAS = [
    (
        "Caracterize legibilidade, escritabilidade e confiabilidade",
        "clp-razoes-criterios-legibilidade-escritabilidade-confiabilidade",
    ),
    (
        "Qual premissa guiou o FORTRAN, o COBOL e o PL/I?",
        "clp-razoes-criterios-legibilidade-escritabilidade-confiabilidade",
    ),
    ("Qual a diferença entre palavras reservadas e palavras-chave?", "clp-palavras-reservadas-versus-palavras-chave"),
    (
        "Quando ocorre a vinculação à memória de variáveis estáticas e dinâmicas de pilha?",
        "clp-vinculacao-memoria-tempo-de-vida-estaticas-pilha-heap",
    ),
    ("O que é escopo e ambiente de referência?", "clp-escopo-estatico-dinamico-ambiente-de-referencia"),
    (
        "Defina coerção, verificação de tipo e tipagem forte",
        "clp-coercao-verificacao-de-tipo-tipagem-forte-conversao-int-float",
    ),
    ("Converter int para float perde precisão?", "clp-coercao-verificacao-de-tipo-tipagem-forte-conversao-int-float"),
    ("Como C implementa compatibilidade de tipos?", "clp-compatibilidade-de-tipos-por-nome-por-estrutura-em-c"),
    (
        "Calcule o endereço de A[j,k] com armazenamento por coluna",
        "clp-arrays-armazenamento-por-linha-por-coluna-calculo-de-endereco",
    ),
    ("O que é row major e column major?", "clp-arrays-armazenamento-por-linha-por-coluna-calculo-de-endereco"),
    ("O que é referência elíptica em registros?", "clp-registros-referencia-qualificacao-completa-eliptica-cobol"),
    ("O que são dangling pointers e memory leak?", "clp-ponteiros-pendentes-vazamento-de-memoria-dangling-pointer"),
    (
        "Avalie r = c > b > a se os operadores relacionais forem associativos à esquerda",
        "clp-precedencia-associatividade-ordem-de-avaliacao-c-maior-b-maior-a",
    ),
    ("O que é avaliação em curto-circuito?", "clp-efeito-colateral-avaliacao-curto-circuito-sobrecarga-de-operadores"),
    (
        "Quais as vantagens e desvantagens de sobrecarregar operadores?",
        "clp-efeito-colateral-avaliacao-curto-circuito-sobrecarga-de-operadores",
    ),
    (
        "Como resolver o problema do else pendente em ifs aninhados?",
        "clp-seletores-aninhados-else-pendente-dangling-else",
    ),
    (
        "Qual a diferença entre passagem por valor-resultado e por referência?",
        "clp-passagem-de-parametros-modelos-semanticos-valor-resultado-referencia",
    ),
    (
        "Qual a saída do código Ruby com yield?",
        "clp-iterador-ruby-yield-haskell-avaliacao-preguicosa-prolog-mundo-fechado",
    ),
    (
        "Explique a suposição de mundo fechado do Prolog",
        "clp-iterador-ruby-yield-haskell-avaliacao-preguicosa-prolog-mundo-fechado",
    ),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Qual a diferença entre passagem por valor-resultado e por referência?", d)).isdisjoint(TODOS)
    assert not buscar("Como funciona um flip-flop JK?")
    assert not set(buscar("Como calcular a transformada de Laplace de um degrau?"))


# ---------------------------------------------------------------- conferência das resoluções


def test_criterios_nao_tem_conta():
    t = TODOS["clp-razoes-criterios-legibilidade-escritabilidade-confiabilidade"]["texto"]
    for termo in ("Legibilidade", "Escritabilidade", "Confiabilidade", "FORTRAN", "COBOL", "PL/I"):
        assert termo in t


def test_palavras_reservadas_e_chave():
    assert keyword.iskeyword("while")
    with pytest.raises(SyntaxError):
        compile("while = 1", "<x>", "exec")
    assert keyword.issoftkeyword("match")
    compile("match = 3", "<x>", "exec")
    assert keyword.iskeyword("async")


def test_tempo_de_vida_em_c(tmp_path):
    _, out, _ = rodar_c(
        r"""#include <stdio.h>
#include <stdlib.h>
int conta(void) { static int n = 0; int k = 0; n++; k++; return n * 10 + k; }
int *cria(void) { int *p = malloc(sizeof *p); *p = 42; return p; }
int main(void) {
    int a = conta(), b = conta(), c = conta();
    int *p = cria();
    printf("%d %d %d %d\n", a, b, c, *p);
    free(p);
    return 0;
}""",
        tmp_path,
    )
    assert out == ["11", "21", "31", "42"]


def test_escopo_estatico_e_dinamico():
    codigo = 'x = "global"\ndef mostra():\n    return x\ndef chama():\n    x = "local de chama"\n    return mostra()\nr = chama()\n'
    ns = {}
    exec(codigo, ns)
    assert ns["r"] == "global"

    # interpretador mínimo com escopo dinâmico: a busca segue a pilha de chamadas
    pilha = [{"x": "global"}]

    def ref(nome):
        for amb in reversed(pilha):
            if nome in amb:
                return amb[nome]
        raise NameError(nome)

    def mostra_din():
        pilha.append({})
        try:
            return ref("x")
        finally:
            pilha.pop()

    def chama_din():
        pilha.append({"x": "local de chama"})
        try:
            return mostra_din()
        finally:
            pilha.pop()

    assert chama_din() == "local de chama"


def test_conversoes_em_c(tmp_path):
    _, out, _ = rodar_c(
        r"""#include <stdio.h>
int main(void) {
    int grande = 16777217;
    float f = (float)grande;
    int volta = (int)f;
    int trunc = (int)3.9f;
    int maximo = 2147483647;
    double d = (double)maximo;
    printf("%d %d %d %d\n", volta, trunc, (int)d, (int)(float)16777216 == 16777216);
    return 0;
}""",
        tmp_path,
    )
    assert out == ["16777216", "3", "2147483647", "1"]


def test_compatibilidade_em_c(tmp_path):
    r, _ = compilar_c(
        "struct a { int x; float y; };\nstruct b { int x; float y; };\nint main(void) { struct a u = {1, 2.0f}; struct b v; v = u; return v.x; }\n",
        tmp_path,
        "structs",
    )
    assert r.returncode != 0 and "incompatible types" in r.stderr
    r, _ = compilar_c(
        "typedef float celsius;\nint main(void) { float f = 1.5f; celsius c = f; return (int)c - 1; }\n",
        tmp_path,
        "typedef",
    )
    assert r.returncode == 0 and "warning" not in r.stderr


def test_enderecos_por_coluna_e_por_linha():
    i1, s1, i2, s2, t, base = 2, 5, -1, 3, 4, 1000
    nl, nc = s1 - i1 + 1, s2 - i2 + 1
    por_coluna = [(j, k) for k in range(i2, s2 + 1) for j in range(i1, s1 + 1)]
    por_linha = [(j, k) for j in range(i1, s1 + 1) for k in range(i2, s2 + 1)]
    for j in range(i1, s1 + 1):
        for k in range(i2, s2 + 1):
            end_col = base + ((k - i2) * nl + (j - i1)) * t
            end_lin = base + ((j - i1) * nc + (k - i2)) * t
            assert por_coluna[(end_col - base) // t] == (j, k)
            assert por_linha[(end_lin - base) // t] == (j, k)
    m = [[3, 4, 7], [6, 2, 5], [1, 3, 8]]
    assert [v for linha in m for v in linha] == [3, 4, 7, 6, 2, 5, 1, 3, 8]
    assert [m[i][j] for j in range(3) for i in range(3)] == [3, 6, 1, 4, 2, 3, 7, 5, 8]


def test_referencia_eliptica():
    campos = [
        ("EMPLOYEE-RECORD", "EMPLOYEE-NAME", "FIRST"),
        ("EMPLOYEE-RECORD", "EMPLOYEE-NAME", "MIDDLE"),
        ("EMPLOYEE-RECORD", "EMPLOYEE-NAME", "LAST"),
        ("EMPLOYEE-RECORD", "HOURLY-RATE"),
    ]

    def resolver(ref, campos):
        nomes = [n.strip() for n in ref.split(" OF ")]  # campo OF pai OF avô...

        def casa(c):
            if c[-1] != nomes[0]:
                return False
            resto = list(reversed(c[:-1]))
            pos = 0
            for n in nomes[1:]:
                while pos < len(resto) and resto[pos] != n:
                    pos += 1
                if pos == len(resto):
                    return False
                pos += 1
            return True

        return [c for c in campos if casa(c)]

    for ref in (
        "FIRST",
        "FIRST OF EMPLOYEE-NAME",
        "FIRST OF EMPLOYEE-RECORD",
        "FIRST OF EMPLOYEE-NAME OF EMPLOYEE-RECORD",
    ):
        assert resolver(ref, campos) == [campos[0]]
    outros = campos + [("MANAGER-RECORD", "FIRST")]
    assert len(resolver("FIRST", outros)) == 2
    assert resolver("FIRST OF EMPLOYEE-NAME", outros) == [campos[0]]


def test_ponteiros_pendentes_e_vazamento(tmp_path):
    r, _ = compilar_c(
        "#include <stdlib.h>\nint *f(void) { int local = 1; return &local; }\n"
        "int main(void) { int *p = malloc(100 * sizeof *p); p = malloc(100 * sizeof *p); free(p); return f() == 0; }\n",
        tmp_path,
    )
    assert r.returncode == 0 and "address of local variable" in r.stderr

    class No:
        pass

    a, b = No(), No()
    a.outro, b.outro = b, a
    ref = weakref.ref(a)
    del a, b
    gc.collect()
    assert ref() is None


def precedencia_ordem(tokens, nivel, assoc_esq=True):
    """Analisador por precedência: devolve a ordem (1, 2, ...) de avaliação de cada operador, na ordem do texto.
    `tokens` usa 'u-' para o menos unário; parênteses são tokens."""
    ordem, cont, pos = {}, [0], [0]

    def prox():
        return tokens[pos[0]] if pos[0] < len(tokens) else None

    def primario():
        t = prox()
        if t == "(":
            pos[0] += 1
            expr(0)
            pos[0] += 1  # ')'
        elif t == "u-":
            i = pos[0]
            pos[0] += 1
            expr(nivel["u-"])
            cont[0] += 1
            ordem[i] = cont[0]
        else:
            pos[0] += 1

    def expr(minimo):
        primario()
        while prox() in nivel and prox() != "u-" and nivel[prox()] >= minimo:
            i, op = pos[0], prox()
            pos[0] += 1
            expr(nivel[op] + (1 if assoc_esq else 0))
            cont[0] += 1
            ordem[i] = cont[0]

    expr(0)
    return [ordem[i] for i in sorted(ordem)]


def test_precedencia_e_associatividade(tmp_path):
    rc, out, _ = rodar_c(
        '#include <stdio.h>\nint main(void) { int a = 5, b = 6, c = 7, r; r = c > b > a; printf("%d %d\\n", r, c > (b > a)); return 0; }\n',
        tmp_path,
    )
    assert out == ["0", "1"]
    assert (7 > 6 > 5) is True  # em Python a comparação é encadeada
    nivel = {"*": 6, "/": 6, "not": 6, "+": 5, "-": 5, "&": 5, "mod": 5, "u-": 4, ">": 3, "and": 2, "or": 1, "xor": 1}
    assert precedencia_ordem(["u-", "a", "+", "b"], nivel) == [2, 1]
    assert precedencia_ordem(["a", "*", "(", "b", "-", "1", ")", "/", "c", "mod", "d"], nivel) == [2, 1, 3, 4]


def test_efeito_colateral_e_curto_circuito(tmp_path):
    _, out, _ = rodar_c(
        r"""#include <stdio.h>
int main(void) {
    int a = 5, b = 2, v[3] = {1, 2, 3}, i = 0, n = 3, chave = 9;
    if ((a > b) || (b++ / 3)) {}
    int b1 = b;
    a = 0;
    if ((a > b) || (b++ / 3)) {}
    while (i < n && v[i] != chave) i++;
    printf("%d %d %d\n", b1, b, i);
    return 0;
}""",
        tmp_path,
    )
    assert out == ["2", "3", "3"]

    class Vetor:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __add__(self, o):
            return Vetor(self.x + o.x, self.y + o.y)

    s = Vetor(1, 2) + Vetor(3, 4)
    assert (s.x, s.y) == (4, 6)


def test_else_pendente(tmp_path):
    _, out, _ = rodar_c(
        r"""#include <stdio.h>
int main(void) {
    int soma = 1, conta = 0, resultado = -1, r2 = -1;
    if (soma == 0)
        if (conta == 0)
            resultado = 0;
        else
            resultado = 1;
    if (soma == 0) { if (conta == 0) r2 = 0; } else r2 = 1;
    printf("%d %d\n", resultado, r2);
    return 0;
}""",
        tmp_path,
    )
    assert out == ["-1", "1"]


def test_passagem_de_parametros(tmp_path):
    amb = {"global": 1}

    def f_referencia(nome):
        amb[nome] = amb[nome] + 10
        amb["global"] = amb["global"] * 2

    def f_valor_resultado(nome):
        x = amb[nome]
        x = x + 10
        amb["global"] = amb["global"] * 2
        amb[nome] = x

    f_referencia("global")
    assert amb["global"] == 22
    amb["global"] = 1
    f_valor_resultado("global")
    assert amb["global"] == 11
    _, out, _ = rodar_c(
        '#include <stdio.h>\nint global = 1;\nvoid f(int *x) { *x = *x + 10; global = global * 2; }\nint main(void) { f(&global); printf("%d\\n", global); return 0; }\n',
        tmp_path,
    )
    assert out == ["22"]


def test_ruby_haskell_prolog():
    def f(u):
        p, s = 1, 1
        while p <= u:
            yield p
            p, s = s, p + s

    termos = list(f(5))
    assert termos == [1, 1, 2, 3, 5] and sum(termos) == 12

    def r(lista, passos):
        if not lista:
            return []
        passos.append(lista)
        return r(lista[1:], passos) + [lista[0]]

    passos = []
    assert r([6, 2, 5], passos) == [5, 2, 6] and passos == [[6, 2, 5], [2, 5], [5]]

    fatos = {("pai", "joao", "ana")}

    def prova(meta):
        return meta in fatos

    def nao(meta):  # negação por falha
        return not prova(meta)

    assert prova(("pai", "joao", "ana")) and not prova(("pai", "joao", "pedro"))
    assert nao(("pai", "joao", "pedro"))
