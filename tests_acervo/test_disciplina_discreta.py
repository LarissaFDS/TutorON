"""Acervo de Matemática Discreta e conferência das contas.

Os blocos parafraseiam os slides e a Lista 01 do Prof. Lucas Amorim, notas do Prof. Pablo Sampaio (UFRPE),
material do Prof. Leandro Balby Marinho (UFCG), o livro de Evaristo e Perdigão e, só por seção, o de
Albertson e Hutchinson. Cada número que aparece num bloco é recalculado aqui.
"""

import itertools
import json
import math
import re
import shutil
import subprocess

import pytest
import sympy

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

MD = disciplinas.obter("discreta")
PASTA = ROOT / "disciplinas/discreta"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
ITENS = {i["id"]: i for i in read_json(MD.itens)}
OUTRAS = ("paa", "sd", "oac", "calc3", "prob", "ed", "prog1")


def buscar(pergunta, d=MD):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return ITENS[ident]["texto"]


# ---------------------------------------------------------------- cadastro e acervo


def test_discreta_cadastrada_com_acervo_proprio():
    assert MD.nome == "Matemática Discreta" and MD.itens.exists() and MD.indice.exists() and not MD.livro_supabase
    ids = {c["id"] for c in read_json(MD.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({MD.itens, MD.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert all(c["disciplina"] == "discreta" for c in read_json(MD.indice)["chunks"])
    assert {i["assunto"] for i in ITENS.values()} == set(MD.assuntos)  # nenhum tópico sem bloco na busca
    assert ids == set(ITENS)


def test_situacao_da_disciplina():
    assert MD.situacao == "MVP" and not MD.em_validacao and not MD.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas discreta --embeddings`."""
    gerados = disciplinas.registros(MD)
    assert gerados == read_json(MD.itens)
    assert {c["id"] for c in read_json(MD.indice)["chunks"]} == {
        i["id"] for i in gerados if i["confiabilidade"] in ("media", "alta")
    }


def test_blocos_cabem_no_trecho_e_terminam_com_verificacao():
    for i in ITENS.values():
        assert len(i["texto"]) <= 2200, i["id"]  # backend/rag.py corta acima disso
        assert "**Verificação:**" in i["texto"].strip().splitlines()[-1], i["id"]


def test_nenhuma_nota_da_ia_e_nada_revisado_sem_registro():
    assert not [i for i, x in ITENS.items() if x["natureza"] == "nota_da_equipe_ia"]
    for p in MD.materiais.glob("*.md"):
        cab = p.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, p.name


# ---------------------------------------------------------------- busca e isolamento


@pytest.mark.parametrize(
    "pergunta, aceitos",
    [
        ("Como provar por indução que 1 + 2 + … + n = n(n+1)/2?", {"discreta-inducao"}),
        ("Como mostrar que uma relação é de equivalência?", {"discreta-relacoes-equivalencia"}),
        ("Como calcular o inverso de 7 módulo 26?", {"discreta-congruencias-inverso"}),
        ("Quantos anagramas tem a palavra ARARA?", {"discreta-permutacoes-combinacoes"}),
        ("Como funciona a criptografia RSA?", {"discreta-rsa"}),
        ("Qual o mdc de 414 e 662 pelo algoritmo de Euclides?", {"discreta-mdc-primos"}),
        ("Quanto é -17 mod 5?", {"discreta-divisao-bases"}),
        ("O que é o princípio da casa dos pombos?", {"discreta-principios-contagem"}),
        ("Quais são os postulados de Peano?", {"discreta-peano-recursao"}),
        ("Como provar que raiz de 2 é irracional?", {"discreta-absurdo-contraexemplo"}),
        ("Quando uma função é injetiva e sobrejetiva?", {"discreta-funcoes"}),
        ("Qual a soma dos graus de um grafo?", {"discreta-grafos"}),
        ("Como resolver uma recorrência pela equação característica?", {"discreta-recorrencias"}),
        ("O que é um monoide?", {"discreta-estruturas-algebricas"}),
        ("Como resolver 7x ≡ 12 (mod 40)?", {"discreta-cc-congruencias-lineares"}),
        ("Quantas soluções tem 9x congruente a 18 mod 45?", {"discreta-cc-congruencias-lineares"}),
        ("Como resolver um sistema pelo teorema chinês do resto?", {"discreta-cc-teorema-chines-resto"}),
        ("Quanto é 3^2021 mod 7?", {"discreta-cc-fermat-potencias-rsa"}),
        ("Como calcular uma potência grande módulo um primo com o pequeno teorema de Fermat?", {"discreta-cc-fermat-potencias-rsa"}),
        ("Quais pares inserir para a relação virar de equivalência?", {"discreta-cc-relacoes-fecho-ordem"}),
        ("Como achar f composta com a inversa de g?", {"discreta-cc-funcoes-bijecao-composta", "discreta-funcoes"}),
        ("Como provar por indução que 2^(2n) - 1 é divisível por 3?", {"discreta-cc-provas-paridade-inducao-euclides", "discreta-inducao"}),
        ("Como escrever {2x | x inteiro, 6 < x < 12} por extensão?", {"discreta-cc-conjuntos-extensao-leis"}),
    ],
)
def test_pergunta_de_discreta_encontra_bloco_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize("pergunta", ["Qual a capital da França?", "Como declarar um ponteiro em C?"])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


@pytest.mark.parametrize(
    "pergunta",
    [
        "Como provar por indução?",
        "O que é uma relação de recorrência?",
        "O que é um grafo conexo?",
        "Como simplificar uma expressão booleana?",
        "Quantas combinações de 3 elementos?",
    ],
)
def test_vocabulario_comum_fica_na_disciplina_escolhida(pergunta):
    """Fronteiras com PAA, ED, SD e Probabilidade: cada disciplina busca só no próprio índice, nos dois sentidos."""
    assert all(i.startswith("discreta-") for i in buscar(pergunta))
    for d in OUTRAS:
        assert not any(i.startswith("discreta-") for i in buscar(pergunta, disciplinas.obter(d)))


def test_rigor_tem_fronteiras_e_nao_entrega_lista():
    for termo in ("Lógica Aplicada", "Sistemas Digitais", "PAA", "ordem importa", "Não entregue a resolução"):
        assert termo in MD.rigor, termo


# ---------------------------------------------------------------- resoluções e correções


def test_resolucoes_tem_status_e_dizem_no_texto():
    rotulo = {
        "validada": "validada",
        "corrigida": "corrigida",
        "pendente_professor": "pendente de confirmação do professor",
    }
    resolvidas = [i for i in ITENS.values() if "status_resolucao" in i]
    assert len(resolvidas) == 27
    for i in resolvidas:
        assert f"Status da resolução: {rotulo[i['status_resolucao']]}" in i["texto"], i["id"]
        assert "gabarito oficial" not in i["texto"].lower()
        if i["status_resolucao"] == "corrigida":
            assert "Divergência" in i["texto"] and "Correções da equipe" in i["texto"], i["id"]
            assert "não é gabarito do professor" in i["texto"], i["id"]


def test_logica_e_demonstracoes():
    p, q = sympy.symbols("p q")
    assert sympy.simplify_logic(sympy.Implies(p, q) ^ (~p | q)) is sympy.false
    assert all(n * n + 1 >= 2 * n for n in range(-50, 50))
    assert 2 * 3 * 5 * 7 * 11 * 13 + 1 == 30031 == 59 * 509
    assert sympy.sqrt(2).is_rational is False
    assert (4 + 3) % (2 + 3) != 0 and (2 * 3 - 7 * 3) % 3 == 0 and (2 - 7) % 3 != 0


def test_conjuntos_da_lista01():
    U, A, B = set(range(10)), {1, 2, 3, 4, 5}, {0, 3, 6}
    assert A & B == {3} and A | B == set(range(7)) and A - B == {1, 2, 4, 5}
    assert U - B == {1, 2, 4, 5, 7, 8, 9} and (U - B) - A == {7, 8, 9}
    um = {1}
    assert um - (um - um) != (um - um) - um


def test_relacoes():
    S = {1, 2, 3, 4}
    R = {(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (4, 1), (3, 4)}
    fecho = set(R)
    while True:
        novo = fecho | {(a, d) for a, b in fecho for c, d in fecho if b == c}
        if novo == fecho:
            break
        fecho = novo
    assert fecho == set(itertools.product(S, S))
    assert {(x, x) for x in S} - R == {(2, 2), (3, 3), (4, 4)}
    assert {(b, a) for a, b in R} - R == {(2, 1), (3, 1), (3, 2), (4, 2), (1, 4), (4, 3)}
    P = [2, 3, 5, 7, 21, 42, 105, 210]
    minimais = [x for x in P if not any(y != x and x % y == 0 for y in P)]
    assert minimais == [2, 3, 5, 7] and all(210 % x == 0 for x in P)
    T = [1, 2, 3, 6, 12, 18]
    assert sum(1 for a in T for b in T if b % a == 0) == 19


def test_funcoes_e_inducao():
    assert math.perm(6, 4) == 360
    assert all(sum(range(1, n + 1)) == n * (n + 1) // 2 for n in range(1, 200))
    assert all((n**3 - n) % 6 == 0 for n in range(-100, 100))


def test_peano_hanoi_e_recorrencias():
    def hanoi(n):
        return 1 if n == 1 else 2 * hanoi(n - 1) + 1

    assert all(hanoi(n) == 2**n - 1 for n in range(1, 13))
    a = [None, 1, 0]
    for _ in range(3, 11):
        a.append(a[-1] + a[-2])
    assert (a[3], a[5], a[10]) == (1, 2, 21)
    s = {1: 4}
    for n in range(2, 31):
        s[n] = 2 * s[n - 1] + 3
    assert all(s[n] == 2 ** (n + 1) + 3 * (2 ** (n - 1) - 1) == 7 * 2 ** (n - 1) - 3 for n in s)
    n = sympy.symbols("n", integer=True)
    f = sympy.Function("a")
    sol = sympy.rsolve(f(n) - 5 * f(n - 1) + 6 * f(n - 2), f(n), {f(0): 1, f(1): 4})
    assert sympy.simplify(sol - (2 * 3**n - 2**n)) == 0


def test_divisao_e_bases():
    for x in range(-200, 201):
        for b in range(1, 21):
            q, r = divmod(x, b)
            assert x == b * q + r and 0 <= r < b
    assert divmod(-17, 5) == (-4, 3) and 100 % 7 == 2
    assert bin(37) == "0b100101" and int("2A", 16) == 42 and 0b1011 + 0b0110 == 0b10001 == 17


def test_mdc_bezout_primos():
    assert math.gcd(414, 662) == 2 and 3 * 26 - 11 * 7 == 1
    assert sympy.factorint(360) == {2: 3, 3: 2, 5: 1} and len(list(sympy.primerange(2, 101))) == 25
    assert math.gcd(12, 18) * math.lcm(12, 18) == 12 * 18 and (4 * 9) % 6 == 0


def test_inverso_modular_e_rsa():
    assert pow(7, -1, 26) == 15 and 7 * 15 == 4 * 26 + 1 and math.gcd(2, 26) == 2
    p, q, c = 97, 53, 7
    n, phi = p * q, (p - 1) * (q - 1)
    d = pow(c, -1, phi)
    assert (n, phi, d) == (5141, 4992, 4279) and 7 * 4279 == 6 * 4992 + 1
    C = pow(165, c, n)
    assert C == 4813 and pow(C, d, n) == 165 and ord("A") + 100 == 165
    assert pow(5, -1, 126 * 192) == 9677 and 127 * 193 == 24511
    cesar = "".join(chr((ord(x) - 65 + 3) % 26 + 65) if x != " " else x for x in "DEZ HORAS")
    assert cesar == "GHC KRUDV"


def test_estruturas_algebricas_e_booleana():
    for m in range(2, 13):
        inv = {a for a in range(1, m) if math.gcd(a, m) == 1}
        sem_divisor_de_zero = all((a * b) % m for a in range(1, m) for b in range(1, m))
        assert sem_divisor_de_zero == sympy.isprime(m)
        if m == 6:
            assert inv == {1, 5}
    assert (5 - 3) - 1 != 5 - (3 - 1)
    for x, y, z in itertools.product((0, 1), repeat=3):
        assert x | x == x and x | (x & y) == x and 1 - (x | y) == (1 - x) & (1 - y)
        assert x | (y & z) == (x | y) & (x | z)
    S = [frozenset(c) for k in range(4) for c in itertools.combinations((1, 2, 3), k)]
    U = frozenset((1, 2, 3))
    assert all(U - (a | b) == (U - a) & (U - b) and a | (a & b) == a for a in S for b in S)


def test_contagem():
    digitos = range(10)
    assert len(list(itertools.product(digitos, repeat=3))) == 1000
    assert len(list(itertools.permutations(digitos, 3))) == 720 and 1000 - 720 == 280
    assert 26**3 * 10**4 == 175_760_000
    assert sum(1 for k in range(1, 101) if k % 2 == 0 or k % 3 == 0) == 67 == 50 + 33 - 16
    assert math.ceil(25 / 12) == 3
    assert len(set(itertools.permutations("ARARA"))) == 10 == math.factorial(5) // (math.factorial(3) * 2)
    assert len(set(itertools.permutations("BANANA"))) == 60
    assert (math.factorial(5), math.perm(10, 3), math.comb(10, 3), math.comb(9, 2)) == (120, 720, 120, 36)
    assert sum(1 for t in itertools.product(range(8), repeat=3) if sum(t) == 7) == 36


def test_grafos():
    assert all(r * (r - 1) // 2 == len(list(itertools.combinations(range(r), 2))) for r in range(1, 11))
    assert math.comb(5, 2) == 10 and (3 + 3 + 3) % 2 == 1
    import random

    rnd = random.Random(0)
    for v in range(2, 30):  # árvore aleatória: cada vértice novo se liga a um anterior
        arestas = [(k, rnd.randrange(k)) for k in range(1, v)]
        graus = [sum(k in e for e in arestas) for k in range(v)]
        assert len(arestas) == v - 1 and sum(graus) == 2 * len(arestas)


# ---------------------------------------------------------------- fórmulas, catálogo e restrições

FORMULA = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in ITENS.values():
        assert i["texto"].count("$") % 2 == 0, i["id"]


@pytest.mark.skipif(not shutil.which("node"), reason="node indisponível")
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for i in ITENS.values() for a, b in FORMULA.findall(i["texto"])]
    assert len(formulas) >= 30
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
        assert set(f["topicos"]) <= set(MD.assuntos), f["id"]
    assert {x for i in ITENS.values() for x in i["fontes_catalogo"]} <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f["uso"] == "acervo"} == {
        x for i in ITENS.values() if i["natureza"] == "material_da_disciplina" for x in i["fontes_catalogo"]
    }
    for ref in ("albertson-hutchinson-solucoes", "ila-capitulos-5-6", "respostas-introducao-algebra"):
        assert CATALOGO[ref]["uso"] == "referencia"


def test_originais_e_dados_pessoais_fora_do_repositorio():
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()]
    assert not [
        p
        for p in arquivos
        if p.suffix.lower() in (".pdf", ".png", ".jpg", ".jpeg", ".docx", ".doc", ".zip", ".pptx", ".gif")
    ]
    proibidos = re.compile(r"(?i)[\w.]+@[\w-]+\.\w+|groups\.google|dropbox|sites\.google|whatsapp|chat\.whatsapp")
    for p in [*MD.materiais.glob("*.md"), MD.itens, PASTA / "rigor.md", PASTA / "CURADORIA.md", PASTA / "fontes.json"]:
        assert not proibidos.search(p.read_text(encoding="utf-8")), p.name
    for i in ITENS.values():
        assert "http" not in i["texto"], i["id"]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert [i for i in CATALOGO if f"`{i}`" not in curadoria] == []
    assert [i for i in ITENS if f"`{i}`" not in curadoria] == []
    assert "`discreta`" in (ROOT / "docs/DISCIPLINAS.md").read_text(encoding="utf-8")


# ---------------------------------------------------------------- complemento de Ciência da Computação

CC = (
    "discreta-cc-conjuntos-extensao-leis",
    "discreta-cc-relacoes-fecho-ordem",
    "discreta-cc-funcoes-bijecao-composta",
    "discreta-cc-provas-paridade-inducao-euclides",
    "discreta-cc-congruencias-lineares",
    "discreta-cc-teorema-chines-resto",
    "discreta-cc-fermat-potencias-rsa",
)


def test_blocos_de_cc_dizem_curso_e_turma():
    assert set(CC) <= set(ITENS)
    for md in MD.materiais.glob("s*-cc-*.md"):
        cab = md.read_text(encoding="utf-8").split("---")[1]
        assert re.search(r"^curso: Ciência da Computação \(UFAL\)", cab, re.M), md.name
    texto = " ".join(ITENS[i]["texto"] for i in CC)
    assert not re.search(r"(?i)lilian|giselly|isidoro|mesquita|fl[aá]vio|farias", texto)  # monitores e aluno


def test_conjuntos_e_relacoes_das_provas_de_cc():
    U = set(range(11))
    A, B = {1, 2, 3, 4, 5}, {0, 3, 6, 7}
    assert (A & B, A | B, A - B, U - B, (U - B) - A) == ({3}, set(range(8)), {1, 2, 4, 5}, {1, 2, 4, 5, 8, 9, 10}, {8, 9, 10})
    assert {2 * x for x in range(7, 12)} == {14, 16, 18, 20, 22}
    assert {x * x for x in range(-9, 10)} == {k * k for k in range(10)}
    assert {x for x in range(-10, 11) if x * x < 10} == set(range(-3, 4))
    assert {x - y for x in range(1, 10, 2) for y in range(1, 10, 2) if x < y} == {-8, -6, -4, -2}
    V = range(4)
    for bits_a in range(16):
        for bits_b in range(16):
            a = {i for i in V if bits_a >> i & 1}
            b = {i for i in V if bits_b >> i & 1}
            ac, bc = set(V) - a, set(V) - b
            assert (a & b) | (a & bc) == a
            assert ((a & b) | (a & bc)) & (ac | b) == a & b
            assert (a | b) | (a & b) == a | b and (a & b) | (a - b) == a

    def fecho(r, dom):
        r = set(r) | {(x, x) for x in dom}
        while True:
            n = r | {(y, x) for x, y in r} | {(x, w) for x, y in r for z, w in r if y == z}
            if n == r:
                return r
            r = n

    r = {(0, 0), (1, 1), (1, 3), (3, 0)}
    assert fecho(r, range(4)) - r == {(0, 1), (0, 3), (1, 0), (3, 1), (3, 3), (2, 2)} and len(fecho(r, range(4))) == 10
    assert len(fecho({(0, 1), (1, 2), (3, 3)}, range(4))) == 10
    assert len(fecho({(0, 0), (1, 1), (1, 3), (3, 0), (2, 3), (3, 1), (3, 2)}, range(4))) == 16
    o = {(1, 1), (2, 2), (3, 3), (4, 4), (3, 2), (2, 4), (3, 4)}
    assert all((x, z) in o for x, y in o for w, z in o if y == w)
    assert not [(x, y) for x, y in o if x != y and (y, x) in o]
    g = {(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 4)}
    assert (2, 2) not in g and all((x, z) in g for x, y in g for w, z in g if y == w)
    R = {(1, "a"), (2, "a"), (1, "b"), (3, "b")}
    comp = lambda s: {(x, z) for x, y in R for w, z in s if y == w}  # noqa: E731
    assert comp({("a", "j"), ("b", "w")}) == {(1, "j"), (2, "j"), (1, "w"), (3, "w")}
    assert comp({(1, "j"), (2, "w")}) == set()


def test_funcoes_e_provas_de_cc():
    from fractions import Fraction as Fr

    assert (lambda x: x * x + x)(Fr(2 + 5, 2)) == Fr(63, 4)
    assert (lambda x: x * x + 2 * x)(Fr(2 - 4, 3)) == Fr(-8, 9)
    assert (lambda x: x * x + 2 * x)(2 + 2) == 24 and (1 + 2) + 2 == 5
    assert [10**n - 5 for n in range(1, 5)] == [5, 95, 995, 9995]
    assert len({"b", "b", "d", "c"}) < 4
    for p, q, r in itertools.product((False, True), repeat=3):
        assert ((p and not (not p or q)) or (p and q)) == p
        assert ((not p or r) or (not q or r)) == (not (p and q) or r)
    assert all((2 ** (2 * n) - 1) % 3 == 0 and sum(range(1, n + 1)) == n * (n + 1) // 2 for n in range(1, 201))
    assert 4040 == 32 * 125 + 40 and 125 == 3 * 40 + 5 and math.gcd(4040, 125) == 5


def test_aritmetica_modular_das_provas_de_cc():
    from sympy.ntheory.modular import crt

    assert (-155 % 19, -82 % 15, -27 % 10) == (16, 8, 3)
    assert [pow(a, -1, m) for a, m in ((8, 25), (11, 135), (5, 21), (7, 29), (7, 40), (7, 23))] == [22, 86, 17, 25, 23, 10]
    sol = lambda a, b, m: [x for x in range(m) if (a * x - b) % m == 0]  # noqa: E731
    assert sol(7, 12, 40) == [36] and sol(2, 7, 17) == [12] and sol(3, 7, 20) == [9]
    assert sol(9, 18, 45) == list(range(2, 45, 5)) and sol(21, 6, 69) == [20, 43, 66]
    for m, r, x in (((3, 5, 7), (2, 4, 6), 104), ((5, 6, 7), (1, 2, 3), 206), ((3, 7, 11), (1, 2, 1), 100), ((3, 7, 8), (1, 2, 3), 163)):
        M = math.prod(m)
        assert crt(m, r) == (x, M)
        assert [y for y in range(M) if all(y % mi == ri for mi, ri in zip(m, r))] == [x]
    assert 35 * 2 * 2 + 21 * 4 + 15 * 6 == 314 and 314 % 105 == 104
    assert (pow(3, 2021, 7), pow(8, 1330, 13), pow(4, 883, 5), pow(2, 2021, 3)) == (5, 12, 4, 2)
    assert 2021 == 6 * 336 + 5 and 1330 == 12 * 110 + 10
    assert all(pow(a, p - 1, p) == 1 for p in (5, 7, 13) for a in range(1, p))
