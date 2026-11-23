"""Acervo de Inteligência Artificial (Ciência da Computação) e conferência das contas e algoritmos.

Os blocos parafraseiam as listas de 2020.2 do Prof. Evandro de Barros Costa (IC-UFAL), as aulas dele de
RCR e lógica e os slides do Prof. Jacson R. C. Silva (UFES) usados na turma. Cada conta dos blocos é
refeita aqui em Python.
"""

import heapq
import itertools
import re
from collections import Counter
from math import log2

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

IA = disciplinas.obter("ia")
PASTA = ROOT / "disciplinas/ia"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(IA.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "ia")
FRONTEIRA = ("am", "logica", "pln", "compevol")
TEXTO = " ".join(i["texto"] for i in TODOS.values())


def buscar(pergunta, d=IA):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def bloco(prefixo):
    return next(i["texto"] for k, i in TODOS.items() if k.startswith(prefixo))


# ---------------------------------------------------------------- cadastro e acervo


def test_ia_cadastrada_com_acervo_proprio():
    assert IA.nome == "Inteligência Artificial" and IA.itens.exists()
    ids = {c["id"] for c in read_json(IA.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({IA.itens, IA.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(IA.assuntos)
    assert ids == set(TODOS)


def test_situacao_da_disciplina():
    assert IA.situacao == "MVP" and not IA.em_validacao and not IA.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas ia --embeddings`."""
    assert disciplinas.registros(IA) == read_json(IA.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert len(t) <= 2600, i["id"]
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


def test_nenhuma_nota_de_ia_na_busca():
    for i in TODOS.values():
        assert i["status_curadoria"] == "aprovado" and i["natureza"] != "nota_da_equipe_ia", i["id"]


def test_sem_dados_pessoais_livro_nem_binarios():
    textos = TEXTO + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"matr[ií]cula:? *\d", textos, re.I)
    assert "Lisboa" not in textos and "Lucas" not in textos  # aluno das cópias respondidas
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"].startswith("Protegido"):
            assert f["uso"] == "referencia", f["id"]
    soltos = [
        p for p in PASTA.rglob("*") if p.suffix.lower() in (".pdf", ".docx", ".ppt", ".pptx", ".png", ".jpg", ".jpeg")
    ]
    assert not soltos
    assert not list(ROOT.rglob("artificial-intelligence-modern-approach*"))
    assert not list(ROOT.rglob("IIA+-+IA_cap*"))


PERGUNTAS = [
    ("O que é um agente inteligente com sensores e atuadores?", "ia-definicao-de-ia-agentes"),
    ("Qual a diferença entre busca em largura e em profundidade?", "ia-busca-nao-informada"),
    ("Quantos nós a busca com aprofundamento iterativo examina?", "ia-busca-nao-informada"),
    ("Como funciona o algoritmo A estrela?", "ia-busca-heuristica"),
    ("Busca A* com custo do caminho e heurística", "ia-busca-heuristica"),
    ("O que é uma heurística admissível?", "ia-busca-heuristica"),
    ("Subida na colina e máximo local", "ia-busca-heuristica"),
    ("Como resolver o problema das oito rainhas como satisfação de restrições?", "ia-problema-de-satisfacao"),
    ("Como funciona a poda alfa-beta?", "ia-arvore-de-jogos-minimax"),
    ("Qual o valor minimax da raiz?", "ia-arvore-de-jogos-minimax"),
    ("O que é base de conhecimento e mecanismo de inferência?", "ia-representacao-de-conhecimento"),
    ("Quando uma fórmula é satisfatível, válida ou tautologia?", "ia-logica-proposicional"),
    ("Regras de inferência: dilema construtivo e absorção", "ia-regras-de-inferencia"),
    ("Como provar R usando modus ponens e silogismo hipotético?", "ia-regras-de-inferencia"),
    ("Como fazer encadeamento para frente e para trás?", "ia-encadeamento"),
    ("Quais os componentes de um sistema especialista?", "ia-sistemas-especialistas"),
    ("Árvore de decisão ID3 para avaliação de risco de crédito", "ia-aprendizado-arvore-de-decisao"),
    ("O que é o ciclo dos 4 Rs do raciocínio baseado em casos?", "ia-raciocinio-baseado-em-casos"),
    ("Como fazer inferência numa rede bayesiana?", "ia-incerteza-redes-bayesianas"),
    ("Como funciona a inferência fuzzy de Mamdani?", "ia-logica-fuzzy"),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    achados = buscar(pergunta)[:3]
    assert any(a.startswith(esperado) for a in achados), achados


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Como funciona a poda alfa-beta?", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a impedância de um indutor?")


# ---------------------------------------------------------------- conferências


def test_aspirador_reativo():
    sujo = {"A": True, "B": True}
    local = "A"
    for _ in range(4):
        if sujo[local]:
            sujo[local] = False
        else:
            local = "B" if local == "A" else "A"
    assert not any(sujo.values())
    assert "sensores" in bloco("ia-definicao") and "atuadores" in bloco("ia-definicao")


ARVORE = {"A": "BC", "B": "DE", "C": "FG", "D": "HI"}


def _visita(largura):
    lista, ordem = ["A"], []
    while lista:
        n = lista.pop(0)
        ordem.append(n)
        filhos = list(ARVORE.get(n, ""))
        lista = lista + filhos if largura else filhos + lista
    return ",".join(ordem)


def test_ordens_profundidade_largura():
    assert _visita(False) == "A,B,D,H,I,E,C,F,G"
    assert _visita(True) == "A,B,C,D,E,F,G,H,I"
    t = bloco("ia-busca-nao-informada")
    assert "A, B, D, H, I, E, C, F, G" in t and "A, B, C, D, E, F, G, H, I" in t


def test_contagem_bpai():
    b, d = 10, 4
    assert sum(b**i for i in range(d + 1)) == 11111 == (b ** (d + 1) - 1) // (b - 1)
    assert sum((d + 1 - i) * b**i for i in range(d + 1)) == 12345
    assert sum((2 + 1 - i) * 2**i for i in range(3)) == 11  # exemplo do slide com b = 2, d = 2
    t = bloco("ia-busca-nao-informada")
    assert "11.111" in t and "12.345" in t


GRAFO = {"S": {"A": 1, "B": 4}, "A": {"B": 2, "G": 12}, "B": {"G": 3}, "G": {}}
H = {"S": 5, "A": 4, "B": 2, "G": 0}


def _melhor_primeiro(usa_g):
    fila = [(H["S"], 0, "S", ["S"])]
    while fila:
        _, g, n, cam = heapq.heappop(fila)
        if n == "G":
            return g, cam
        for m, c in GRAFO[n].items():
            heapq.heappush(fila, ((g + c if usa_g else 0) + H[m], g + c, m, cam + [m]))


def test_a_estrela_e_gulosa():
    # h é admissível: nunca passa do custo real até G
    real = {"S": 6, "A": 5, "B": 3, "G": 0}
    assert all(H[n] <= real[n] for n in H)
    assert _melhor_primeiro(True) == (6, ["S", "A", "B", "G"])
    assert _melhor_primeiro(False) == (7, ["S", "B", "G"])
    t = bloco("ia-busca-heuristica")
    assert "custo 6" in t and "custo 7" in t


def rainhas(n, parcial=()):
    if len(parcial) == n:
        yield parcial
    for lin in range(n):
        if all(lin != l and abs(lin - l) != len(parcial) - c for c, l in enumerate(parcial)):
            yield from rainhas(n, parcial + (lin,))


def test_oito_rainhas():
    sol = list(rainhas(8))
    assert len(sol) == 92
    for s in sol:
        for (c1, l1), (c2, l2) in itertools.combinations(enumerate(s), 2):
            assert l1 != l2 and abs(l1 - l2) != abs(c1 - c2)
    assert "92 soluções" in bloco("ia-problema-de-satisfacao")


def _alfabeta(no, maximiza, alfa, beta, vistas):
    if isinstance(no, int):
        vistas.append(no)
        return no
    v = float("-inf") if maximiza else float("inf")
    for filho in no:
        r = _alfabeta(filho, not maximiza, alfa, beta, vistas)
        if maximiza:
            v, alfa = max(v, r), max(alfa, r)
        else:
            v, beta = min(v, r), min(beta, r)
        if alfa >= beta:
            break
    return v


def test_minimax_alfa_beta():
    arvore = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
    assert max(min(f) for f in arvore) == 3
    vistas = []
    assert _alfabeta(arvore, True, float("-inf"), float("inf"), vistas) == 3
    assert vistas == [3, 12, 8, 2, 14, 5, 2]  # 4 e 6 podadas
    assert "4 e 6 **são podadas**" in bloco("ia-arvore-de-jogos")


REGRAS = [({"P", "Q"}, "R"), ({"S"}, "T"), ({"T"}, "P"), ({"S"}, "V"), ({"V"}, "Q")]


def para_frente(fatos, regras=REGRAS):
    fatos = set(fatos)
    while True:
        novos = {c for prem, c in regras if prem <= fatos} - fatos
        if not novos:
            return fatos
        fatos |= novos


def para_tras(obj, fatos, regras=REGRAS, pilha=()):
    if obj in fatos:
        return True
    if obj in pilha:
        return False
    return any(all(para_tras(p, fatos, regras, pilha + (obj,)) for p in prem) for prem, c in regras if c == obj)


def test_tell_ask():
    bc = []

    def tell(regra):
        bc.append(regra)

    def ask(q, fatos):
        return q in para_frente(fatos, bc)

    tell(({"chove"}, "molhado"))
    tell(({"molhado", "frio"}, "gelo"))
    assert ask("molhado", {"chove"}) and not ask("gelo", {"chove"})
    assert ask("gelo", {"chove", "frio"})


def _vale(f, modelo):
    return f(*modelo)


def _tautologia(f, n):
    return all(f(*m) for m in itertools.product([True, False], repeat=n))


def imp(a, b):
    return (not a) or b


def test_validade_tabela_verdade():
    assert _tautologia(lambda p, q, r: imp(imp(p, q) and imp(q, r) and p, r), 3)
    a = lambda p, q: imp(p, not q) and imp(not p, q)  # noqa: E731
    modelos = [m for m in itertools.product([True, False], repeat=2) if _vale(a, m)]
    assert modelos and len(modelos) < 4 and all(p != q for p, q in modelos)
    assert "**satisfatível e inválida**" in bloco("ia-logica-proposicional")


def test_regras_de_inferencia_corretas():
    regras = {
        "modus ponens": (lambda p, q, r, s: imp(p, q) and p, lambda p, q, r, s: q),
        "modus tollens": (lambda p, q, r, s: imp(p, q) and not q, lambda p, q, r, s: not p),
        "silogismo hipotético": (lambda p, q, r, s: imp(p, q) and imp(q, r), lambda p, q, r, s: imp(p, r)),
        "silogismo disjuntivo": (lambda p, q, r, s: (p or q) and not p, lambda p, q, r, s: q),
        "dilema construtivo": (lambda p, q, r, s: imp(p, q) and imp(r, s) and (p or r), lambda p, q, r, s: q or s),
        "absorção": (lambda p, q, r, s: imp(p, q), lambda p, q, r, s: imp(p, p and q)),
        "simplificação": (lambda p, q, r, s: p and q, lambda p, q, r, s: p),
        "conjunção": (lambda p, q, r, s: p and q, lambda p, q, r, s: p and q),
        "adição": (lambda p, q, r, s: p, lambda p, q, r, s: p or q),
    }
    for nome, (prem, conc) in regras.items():
        assert _tautologia(lambda *m, a=prem, c=conc: imp(a(*m), c(*m)), 4), nome
    # a prova da lista chega a R
    assert "R" in para_frente({"S"})
    t = bloco("ia-regras-de-inferencia")
    assert t.index("(11) $P \\land Q$") < t.index("(12) $R$")


def test_encadeamento_frente_e_tras():
    assert para_frente({"S"}) == {"S", "T", "V", "P", "Q", "R"}
    assert para_tras("R", {"S"})
    assert "R" not in para_frente(set()) and not para_tras("R", set())
    assert "até nada mudar" in bloco("ia-encadeamento")


def test_explicacao_como():
    regras = {"R2": ({"S"}, "T"), "R3": ({"T"}, "P"), "R4": ({"S"}, "V"), "R5": ({"V"}, "Q"), "R1": ({"P", "Q"}, "R")}
    fatos, usadas = {"S"}, []
    mudou = True
    while mudou:
        mudou = False
        for nome, (prem, c) in regras.items():
            if prem <= fatos and c not in fatos:
                fatos.add(c)
                usadas.append(nome)
                mudou = True
    assert "R" in fatos and usadas[-1] == "R1" and set(usadas) == set(regras)
    assert '"como?"' in bloco("ia-sistemas-especialistas")


CREDITO = """Ruim,Alta,Nenhuma,0a15k,Alto
Desconhecida,Alta,Nenhuma,15a35k,Alto
Desconhecida,Baixa,Nenhuma,15a35k,Moderado
Desconhecida,Baixa,Nenhuma,0a15k,Alto
Desconhecida,Baixa,Nenhuma,Acimade35k,Baixo
Desconhecida,Baixa,Adequada,Acimade35k,Baixo
Ruim,Baixa,Nenhuma,0a15k,Alto
Ruim,Baixa,Adequada,Acimade35k,Moderado
Boa,Baixa,Nenhuma,Acimade35k,Baixo
Boa,Alta,Adequada,Acimade35k,Baixo
Boa,Alta,Nenhuma,0a15k,Alto
Boa,Alta,Nenhuma,15a35k,Moderado
Boa,Alta,Nenhuma,Acimade35k,Baixo
Ruim,Alta,Nenhuma,15a35k,Alto"""


def _h(linhas):
    n = len(linhas)
    return -sum(c / n * log2(c / n) for c in Counter(r[-1] for r in linhas).values())


def test_id3_credito():
    dados = [linha.split(",") for linha in CREDITO.splitlines()]
    assert Counter(r[-1] for r in dados) == {"Alto": 6, "Baixo": 5, "Moderado": 3}
    assert round(_h(dados), 3) == 1.531
    ganhos = {}
    for a, nome in enumerate(["histórico", "dívida", "garantia", "renda"]):
        resto = sum(
            len(s) / len(dados) * _h(s) for v in {r[a] for r in dados} for s in [[r for r in dados if r[a] == v]]
        )
        ganhos[nome] = round(_h(dados) - resto, 3)
    assert ganhos == {"histórico": 0.266, "dívida": 0.063, "garantia": 0.206, "renda": 0.966}
    assert max(ganhos, key=ganhos.get) == "renda"
    assert {r[-1] for r in dados if r[3] == "0a15k"} == {"Alto"}
    t = bloco("ia-aprendizado-arvore")
    assert all(f"{v:.3f}".replace(".", ",") in t for v in ganhos.values()) and "1{,}531" in t


def test_rbc_similaridade():
    pesos = {"marca": 1, "modelo": 1, "sintoma": 2}
    base = {
        "bateria": {"marca": "X", "modelo": "8", "sintoma": "nao_liga"},
        "tela": {"marca": "Y", "modelo": "A30", "sintoma": "touch"},
    }
    novo = {"marca": "X", "modelo": "9", "sintoma": "nao_liga"}

    def sim(a, b):
        return sum(p * (a[k] == b[k]) for k, p in pesos.items()) / sum(pesos.values())

    sims = {k: sim(novo, c) for k, c in base.items()}
    assert sims == {"bateria": 0.75, "tela": 0.0}
    assert max(sims, key=sims.get) == "bateria"
    assert "**Recuperar:**" in bloco("ia-raciocinio") and "**Reter:**" in bloco("ia-raciocinio")


def test_rede_bayesiana():
    pi, pb = 0.5, 0.5
    pa = {(True, True): 0.9, (True, False): 0.7, (False, True): 0.6, (False, False): 0.2}

    def p(i, b):
        return (pi if i else 1 - pi) * (pb if b else 1 - pb)

    p_a = sum(p(i, b) * pa[i, b] for i in (True, False) for b in (True, False))
    p_ia = sum(p(True, b) * pa[True, b] for b in (True, False)) / p_a
    assert round(p_a, 6) == 0.6 and round(p_ia, 3) == 0.667
    t = bloco("ia-incerteza")
    assert "= 0{,}6$" in t and "0{,}667" in t


def _tri(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    return (x - a) / (b - a) if x <= b else (c - x) / (c - b)


def test_mamdani_centroide():
    media, generosa = (5, 12.5, 20), (15, 25, 35)
    forca_media, forca_generosa = 0.6, 0.4
    zs = [i / 100 for i in range(0, 2501)]
    mu = [max(min(forca_media, _tri(z, *media)), min(forca_generosa, _tri(z, *generosa))) for z in zs]
    centroide = sum(z * m for z, m in zip(zs, mu, strict=True)) / sum(mu)
    assert media[1] < centroide < generosa[1]
    assert abs(centroide - media[1]) < abs(centroide - generosa[1])
    t = bloco("ia-logica-fuzzy")
    assert "**mínimo**" in t and "**máximo**" in t and "**centroide**" in t
