"""Acervo de Noções de Direito (Ciência da Computação) e conferência das citações.

Os blocos parafraseiam as avaliações de 2020.2 da Profa. Jessica Hind (IC-UFAL) e os slides
"Noções Iniciais". Só são citados com número os artigos conferidos no texto do Planalto em 22/11/2026.
"""

import hashlib
import re

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

DIR = disciplinas.obter("direito")
PASTA = ROOT / "disciplinas/direito"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(DIR.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "direito")
FRONTEIRA = ("etica", "seguranca")
TEXTO = " ".join(i["texto"] for i in TODOS.values())


def buscar(pergunta, d=DIR):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def bloco(prefixo):
    return next(i["texto"] for k, i in TODOS.items() if k.startswith(prefixo))


# ---------------------------------------------------------------- cadastro e acervo


def test_direito_cadastrada_com_acervo_proprio():
    assert DIR.nome == "Noções de Direito" and DIR.itens.exists()
    ids = {c["id"] for c in read_json(DIR.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({DIR.itens, DIR.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(DIR.assuntos)
    assert ids == set(TODOS)


def test_situacao_da_disciplina():
    assert DIR.situacao == "MVP" and not DIR.em_validacao and not DIR.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas direito --embeddings`."""
    assert disciplinas.registros(DIR) == read_json(DIR.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert len(t) <= 2200, i["id"]
        assert "não é aconselhamento jurídico" in t, i["id"]
        ultima = t.strip().splitlines()[-1]
        assert "**Verificação:**" in ultima, i["id"]
        assert "não é gabarito do professor" in t and "Status da resolução:" in t, i["id"]
        for nome in re.findall(r"`(test_\w+)`", ultima):
            assert nome in globals(), (i["id"], nome)
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, arq.name
        for f in re.search(r"fontes_catalogo: (.+)", cab).group(1).split(","):
            assert f.strip() in CATALOGO, (arq.name, f)


def test_sem_dados_pessoais_livro_nem_binarios():
    textos = TEXTO + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"matr[ií]cula:? *\d", textos, re.I)
    assert "Lisboa" not in textos  # nome do aluno das cópias respondidas
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"].startswith("Protegido"):
            assert f["uso"] == "referencia", f["id"]
    soltos = [
        p for p in PASTA.rglob("*") if p.suffix.lower() in (".pdf", ".docx", ".ppt", ".pptx", ".png", ".jpg", ".jpeg")
    ]
    assert not soltos
    assert not list(ROOT.rglob("int_direito_doc_01.pdf"))


CONFERIDOS = {("LINDB", "4º"), ("Constituição", "5º")}


def test_sem_artigo_nao_conferido():
    # só LINDB art. 4º e Constituição art. 5º foram lidos no texto oficial
    for m in re.finditer(r"art\. (\d+º?)", TEXTO):
        assert m.group(1) in {"4º", "5º"}, m.group(0)
    for lei in ("Código Civil", "Código de Processo Civil", "Código de Processo Penal"):
        for m in re.finditer(re.escape(lei), TEXTO):
            assert not re.match(r"[^.]{0,15}art\.", TEXTO[m.end() :]), lei


PERGUNTAS = [
    (
        "Qual a diferença entre Direito, Moral, Religião e Regras de Trato Social?",
        "direito-como-processo-de-adaptacao-social-direito-moral-religiao-regras-de-trato-social",
    ),
    (
        "Quais são as fontes do Direito: lei, costume e analogia?",
        "direito-fontes-do-direito-lei-costume-analogia-jurisprudencia-common-law-civil-law-lindb",
    ),
    (
        "A decisão de um juiz vale para todos os consumidores? Common law",
        "direito-fontes-do-direito-lei-costume-analogia-jurisprudencia-common-law-civil-law-lindb",
    ),
    (
        "O que fica no topo da pirâmide de Kelsen?",
        "direito-piramide-de-kelsen-hierarquia-das-normas-constituicao-tratados-de-direitos-humanos-supralegal",
    ),
    (
        "Qual a natureza dos tratados de direitos humanos não aprovados pelo rito qualificado?",
        "direito-piramide-de-kelsen-hierarquia-das-normas-constituicao-tratados-de-direitos-humanos-supralegal",
    ),
    (
        "Quem julga crimes contra a humanidade?",
        "direito-internacional-dos-direitos-humanos-pos-segunda-guerra-nazismo-soberania-criticas-tribunal-penal-internacional",
    ),
    (
        "Diferenças entre o pensamento de Kant e Hegel sobre o Estado",
        "direito-kant-e-hegel-moralidade-sociedade-civil-e-estado-imperativo-categorico-dialetica",
    ),
    (
        "O que é dirigismo contratual?",
        "direito-funcao-social-do-contrato-dirigismo-contratual-propriedade-usar-gozar-dispor-reivindicar-sequela",
    ),
    (
        "Direito de sequela decorre de qual faculdade do domínio?",
        "direito-funcao-social-do-contrato-dirigismo-contratual-propriedade-usar-gozar-dispor-reivindicar-sequela",
    ),
    (
        "O hash do código-fonte é requisito para registrar o quê no INPI?",
        "direito-propriedade-intelectual-software-registro-inpi-hash-codigo-fonte-direito-autoral-patente-marca-trade-dress",
    ),
    (
        "O que é trade dress?",
        "direito-propriedade-intelectual-software-registro-inpi-hash-codigo-fonte-direito-autoral-patente-marca-trade-dress",
    ),
    (
        "Como usar uma conversa de WhatsApp como prova?",
        "direito-digital-provas-whatsapp-ata-notarial-prova-ilicita-teoria-dos-frutos-da-arvore-envenenada",
    ),
    (
        "O que é a teoria dos frutos da árvore envenenada?",
        "direito-digital-provas-whatsapp-ata-notarial-prova-ilicita-teoria-dos-frutos-da-arvore-envenenada",
    ),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("O que é a teoria dos frutos da árvore envenenada?", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a impedância de um indutor?")


# ---------------------------------------------------------------- conferências


def test_ordens_normativas():
    ordens = {
        "Direito": ("segurança e à justiça", True),
        "Moral": ("aperfeiçoamento", False),
        "Religião": ("supraterrena", False),
        "Regras de trato social": ("cortesia", False),
    }
    t = bloco("direito-como-processo")
    assert all(fim in t for fim, _ in ordens.values())
    assert [o for o, (_, coerc) in ordens.items() if coerc] == ["Direito"]


def test_lindb_art4():
    t = bloco("direito-fontes")
    assert "LINDB, art. 4º" in t
    for base in ("**analogia**", "**costumes**", "**princípios gerais de direito**"):
        assert base in t


def test_tres_quintos():
    def tres_quintos(n):
        return -(-3 * n // 5)  # teto

    assert tres_quintos(513) == 308 and tres_quintos(81) == 49
    t = bloco("direito-piramide")
    assert "308 dos 513" in t and "49 dos 81" in t and "art. 5º, §3º" in t


def test_hierarquia_kelsen():
    piramide = ["Constituição", "leis", "decretos", "contratos"]
    t = bloco("direito-piramide")
    pos = [t.index(n) for n in piramide]
    assert pos == sorted(pos)


def test_tribunais_e_competencias():
    julga = {"TPI": "pessoas", "Corte Interamericana": "Estados"}
    t = bloco("direito-internacional")
    assert f"o TPI julga **{julga['TPI']}**" in t and f"julga **{julga['Corte Interamericana']}**" in t


def test_kant_hegel_conceitos():
    t = bloco("direito-kant")
    k, h = t.index("**Kant:**"), t.index("**Hegel:**")
    for c in ("imperativo categórico", "publicidade"):
        assert k < t.index(c) < h
    for c in ("dialética", "eticidade", "sociedade civil"):
        assert t.index(c, h) > h


def test_faculdades_do_dominio():
    t = bloco("direito-funcao-social")
    for f in ("**usar:**", "**gozar**", "**dispor:**", "**reivindicar**"):
        assert f in t
    assert "decorre da faculdade de **reivindicar**" in t


def test_hash_do_codigo_fonte():
    codigo = b"def soma(a, b):\n    return a + b\n"
    h1 = hashlib.sha256(codigo).hexdigest()
    h2 = hashlib.sha256(codigo.replace(b"+", b"-")).hexdigest()
    assert h1 != h2 and len(h1) == 64
    assert h1 == hashlib.sha256(codigo).hexdigest()


def _admissivel(prova, provas):
    p = provas[prova]
    if p["ilicita"]:
        return False
    origem = p.get("deriva_de")
    if origem and not _admissivel(origem, provas) and not p.get("fonte_independente"):
        return False
    return True


def test_prova_derivada():
    provas = {
        "grampo": {"ilicita": True},
        "busca": {"ilicita": False, "deriva_de": "grampo"},
        "testemunha": {"ilicita": False, "deriva_de": "grampo", "fonte_independente": True},
        "documento": {"ilicita": False},
    }
    assert not _admissivel("grampo", provas) and not _admissivel("busca", provas)
    assert _admissivel("testemunha", provas) and _admissivel("documento", provas)
    assert "art. 5º, LVI" in bloco("direito-digital")
