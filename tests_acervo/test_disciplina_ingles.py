"""Acervo de Inglês Instrumental e conferência das respostas dos exercícios no próprio texto.

O único material da turma é o texto de uma prova de proficiência em leitura (início do artigo de revisão de
Pavela, 2016, CC BY-NC 4.0), sem questões. Os exercícios são da equipe; cada trecho em inglês citado num bloco
(entre aspas curvas) está em `tests_acervo/ingles_trechos.json`, e cada resposta verificável (número, núcleo,
referente, forma passiva) é refeita aqui. Com `TUTORON_INGLES_ORIGINAIS` apontando para a pasta com `prova.docx`
e `wilson.xml` (fora do repositório), os trechos também são conferidos nos textos originais.
"""

import hashlib
import html
import json
import os
import re
import subprocess
import zipfile
from pathlib import Path

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

ING = disciplinas.obter("ingles")
FONTES = read_json(ROOT / "disciplinas/ingles/fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
ITENS = {x["id"]: x for x in read_json(ING.itens)}
NA_BUSCA = {c["id"] for c in read_json(ING.indice)["chunks"]}
VETORES = json.loads((ROOT / "eval/relevancia-vetores.json").read_text(encoding="utf-8"))
TRECHOS = read_json(ROOT / "tests_acervo/ingles_trechos.json")
CITACAO = re.compile(r"“(.+?)”")


def norm(t):
    return re.sub(r"\s+", " ", html.unescape(t).replace("\xa0", " ")).strip()


def texto(ident):
    return ITENS[f"ingles-{ident}"]["texto"]


def citados(ident):
    return [norm(q) for q in CITACAO.findall(texto(ident))]


def buscar(pergunta, d=ING):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def hibrida(pergunta, d=ING):
    return [
        r["id"]
        for r in search(
            pergunta,
            k=4,
            vector=VETORES[pergunta],
            min_similarity=0.45,
            hub_penalty=True,
            itens=d.itens,
            indice=d.indice,
        )
    ]


PROVA = " ".join(TRECHOS["prova"])
WILSON = " ".join(TRECHOS["wilson"])

ORIGINAIS = Path(os.environ.get("TUTORON_INGLES_ORIGINAIS", "")) if os.environ.get("TUTORON_INGLES_ORIGINAIS") else None
precisa_originais = pytest.mark.skipif(
    not (ORIGINAIS and (ORIGINAIS / "prova.docx").exists() and (ORIGINAIS / "wilson.xml").exists()),
    reason="TUTORON_INGLES_ORIGINAIS não aponta para prova.docx e wilson.xml (ficam fora do repositório)",
)


def paragrafos_prova():
    xml = zipfile.ZipFile(ORIGINAIS / "prova.docx").read("word/document.xml").decode("utf-8")
    brutos = re.sub(r"<[^>]+>", "", re.sub(r"</w:p>", "\n", xml)).split("\n")
    return [norm(p) for p in brutos if norm(p)]


def texto_wilson():
    xml = (ORIGINAIS / "wilson.xml").read_text(encoding="utf-8")
    return re.sub(r"\s+([,.;:])", r"\1", norm(re.sub(r"<[^>]+>", " ", xml))), xml


# ---------------------------------------------------------------- cadastro e acervo


def test_ingles_cadastrada_com_acervo_proprio_e_a_mesma_ia():
    assert ING.nome == "Inglês Instrumental" and ING.itens.exists() and ING.indice.exists()
    assert (
        not ING.livro_supabase
        and ING.rigor.strip() == (ROOT / "disciplinas/ingles/rigor.md").read_text(encoding="utf-8").strip()
    )
    assert all(c["disciplina"] == "ingles" for c in read_json(ING.indice)["chunks"])
    for outra in disciplinas.todas():
        if outra.id != "ingles":
            assert NA_BUSCA.isdisjoint({c["id"] for c in read_json(outra.indice)["chunks"]}), outra.id
    bruto = [d for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] == "ingles"][0]
    assert not {"modelo", "model", "provedor", "endpoint", "prompt", "chave"} & set(bruto)
    assert bruto["situacao"] == "em validação" and "aviso" not in bruto
    assert read_json(ING.indice)["embedding_model"] == read_json(disciplinas.obter("varcomp").indice)["embedding_model"]


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas ingles --embeddings`."""
    gerados = disciplinas.registros(ING)
    assert gerados == read_json(ING.itens)
    assert NA_BUSCA == {x["id"] for x in gerados if x["confiabilidade"] in ("media", "alta")}
    assert read_json(ING.indice)["modo"] == "hibrido"


def test_blocos_cabem_no_trecho_e_terminam_com_verificacao():
    for x in ITENS.values():
        assert len(x["texto"]) <= 2200, x["id"]
        assert "**Verificação:**" in x["texto"], x["id"]
        assert "$" not in x["texto"], x["id"]  # sem fórmulas: nada para o KaTeX quebrar


def test_nenhuma_nota_de_ia_sem_revisao_na_busca():
    assert not [x for x in ITENS.values() if x["natureza"] == "nota_da_equipe_ia" and x["id"] in NA_BUSCA]
    assert not any(x.get("revisao_humana") == "feita" or x.get("revisao_professor") for x in ITENS.values())
    assert all(x["revisao_humana"] == "pendente" for x in ITENS.values())


def test_todos_os_topicos_tem_bloco_na_busca():
    assert {ITENS[x]["assunto"] for x in NA_BUSCA} == set(ING.assuntos)
    assert set(CATALOGO["ufal-ingles-texto-prova"]["topicos"]) == set(ING.assuntos)


def test_status_dos_exercicios():
    for x in ITENS.values():
        assert x["status_resolucao"] in ("validada", "pendente_professor"), x["id"]
        assert x["verificacao"] == "conferida_por_codigo", x["id"]
        if x["status_resolucao"] == "pendente_professor":
            assert "Status da resolução: pendente de confirmação do professor" in x["texto"], x["id"]
        assert "Exercício da equipe TutorON" in x["texto"], x["id"]
        assert "Prof." not in x["texto"], x["id"]  # o professor da turma não foi identificado


# ---------------------------------------------------------------- trechos citados


def test_todo_trecho_citado_esta_no_arquivo_de_trechos():
    todos = set(TRECHOS["prova"]) | set(TRECHOS["wilson"])
    citacoes = {q for x in ITENS.values() for q in map(norm, CITACAO.findall(x["texto"]))}
    assert citacoes == todos
    assert all(len(q.split()) <= 35 for q in todos)  # só trechos curtos


@precisa_originais
def test_trechos_estao_nos_textos_originais():
    prova = " ".join(paragrafos_prova())
    assert hashlib.sha256(prova.encode()).hexdigest() == TRECHOS["sha256_prova_normalizada"]
    wilson, xml = texto_wilson()
    assert [q for q in TRECHOS["prova"] if q not in prova] == []
    assert [q for q in TRECHOS["wilson"] if q not in wilson] == []
    assert "creativecommons.org/licenses/by/4.0" in xml


@precisa_originais
def test_skimming_primeiras_frases_abrem_os_paragrafos_em_ordem():
    paragrafos = paragrafos_prova()[1:]  # o primeiro é o título
    assert len(paragrafos) == TRECHOS["paragrafos_prova"] == 6
    aberturas = [q for q in citados("prova-skimming-hipotese") if any(p.startswith(q) for p in paragrafos)]
    assert len(aberturas) == 6
    assert [next(i for i, p in enumerate(paragrafos) if p.startswith(q)) for q in aberturas] == list(range(6))
    assert paragrafos_prova()[0].startswith(citados("prova-skimming-hipotese")[0])


@pytest.mark.parametrize(
    "numeros",
    [("10 and 90%", "35–40%"), ("10 billion by 2050",), ("350 to 500 million", "1 million deaths"), ("30-fold",)],
)
def test_scanning_numeros_estao_no_texto_e_no_bloco(numeros):
    for n in numeros:
        assert n in PROVA and n in texto("prova-scanning")
    assert "approximately 2 million people" in PROVA and "2.5 billion people" in PROVA and "22 000 deaths" in PROVA


NUCLEOS = {
    "storage pests": "pests",
    "disease transmitters": "transmitters",
    "mosquito-borne viral diseases": "diseases",
    "dengue haemorrhagic fever": "fever",
    "hamster reticulum cell sarcoma": "sarcoma",
}


def test_grupos_nominais_nucleo_e_a_ultima_palavra():
    bloco = texto("grupos-nominais")
    for grupo, nucleo in NUCLEOS.items():
        assert grupo in PROVA and grupo.split()[-1] == nucleo
        assert re.search(rf"núcleo:? \*{nucleo}\*", bloco, re.I), nucleo
    # O caso da pergunta de exemplo fica para o aluno: o bloco ensina o método, não entrega a tradução
    # (com a tradução pronta, o revisor reprovava a pista do tutor; veja CURADORIA.md).
    assert '"plant extract based insecticides"' in bloco and "inseticidas à base" not in bloco


PASSIVA = re.compile(r"\b(is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?(\w+ed|taught|built|done|known)\b")


def test_voz_passiva_cada_trecho_tem_to_be_e_participio():
    contraexemplos = {"is very important", "has increased"}
    assert contraexemplos <= set(citados("voz-passiva"))
    trechos = [q for q in citados("voz-passiva") if q not in contraexemplos]
    assert len(trechos) == 8
    assert all(PASSIVA.search(q) for q in trechos), [q for q in trechos if not PASSIVA.search(q)]
    # Os contraexemplos do bloco não são passivas.
    assert not PASSIVA.search("the incidence has increased 30-fold") and not PASSIVA.search("is very important")
    assert "is experienced by infants" in PROVA  # agente com by
    assert PASSIVA.search("most scientists are never taught".replace("never ", "")) and "are never taught" in WILSON


def test_tempos_verbais_auxiliares():
    assert "has increased" in PROVA and "We are talking" in PROVA and "may be explained" in PROVA
    assert "we should have concerns" in PROVA and "was highlighted" in PROVA


REFERENTES = [
    ("where they are used", "insecticides"),
    ("which may range", "damage"),
    ("some transmit", "some mosquito species"),
    ("their frequent use which keeps rising", "insecticides"),
    ("their use is being gradually abandoned", "four main groups of insecticides"),
]


@precisa_originais
def test_referencia_pronominal_referente_vem_antes_no_mesmo_paragrafo():
    for trecho, referente in REFERENTES:
        p = next(p for p in paragrafos_prova() if trecho in p)
        assert referente in p[: p.index(trecho)], trecho
    assert "it was hypothesized" in PROVA


def test_referencia_pronominal_no_bloco():
    bloco = texto("referencia-pronominal")
    for trecho, _ in REFERENTES:
        assert any(trecho in q for q in citados("referencia-pronominal")), trecho
    assert "*they* = os inseticidas" in bloco and "*which* = o dano" in bloco


AFIXOS = (
    "insecticidal substances",
    "Phytophagous insects",
    "extremely harmful diseases",
    "gradually abandoned",
    "morbidity and mortality",
    "toxicity",
    "persistence in the environment",
    "domesticated animals",
    "oncogenesis",
    "arboviruses",
)


@precisa_originais
def test_palavras_dos_afixos_estao_no_texto_original():
    prova = " ".join(paragrafos_prova()).lower()
    assert [p for p in AFIXOS if p.lower() not in prova] == []


def test_afixos_e_marcadores_no_bloco():
    assert [p for p in AFIXOS if p.lower() not in texto("afixos").lower()] == []
    marcadores = ("However", "Therefore", "Likewise", "For instance")
    for m in marcadores:
        assert any(q.startswith(m) for q in citados("marcadores-discurso")), m


def test_cognatos_e_dicionario():
    assert "it is actually doing what it is intended to do" in WILSON
    assert "topical issue" in PROVA and "to pose severe health" in PROVA
    for palavra in ("vectors", "economic burden", "outbreaks", "topical issue"):
        assert any(palavra in q for q in citados("dicionario-contexto")), palavra
    assert "*actually* = na verdade" in texto("cognatos-falsos-cognatos")


def test_texto_de_computacao():
    bloco = texto("compreensao-texto-computacao")
    assert "30% or more of their time developing software" in WILSON and "*30% or more*" in bloco
    assert "90% or more of them are primarily self-taught" in WILSON and "*90% or more*" in bloco
    assert "Make names consistent, distinctive, and meaningful." in WILSON


@precisa_originais
def test_box1_de_wilson_tem_oito_praticas():
    wilson, _ = texto_wilson()
    praticas = [
        "Write programs for people, not computers.",
        "Let the computer do the work.",
        "Make incremental changes.",
        "Don't repeat yourself (or others).",
        "Plan for mistakes.",
        "Optimize software only after it works correctly.",
        "Document design and purpose, not mechanics.",
        "Collaborate.",
    ]
    box = wilson[
        wilson.index("Box 1. Summary of Best Practices") : wilson.index("Write Programs for People, Not Computers")
    ]
    assert [p for p in praticas if p not in box] == []
    assert "o Box 1 de Wilson et al. tem 8 práticas" in texto("estrutura-artigo-cientifico")


# ---------------------------------------------------------------- busca e isolamento

EXEMPLOS = [
    ("O que é skimming e scanning?", {"ingles-prova-skimming-hipotese", "ingles-prova-scanning"}),
    (
        'Como identificar o núcleo de um grupo nominal como "plant extract based insecticides"?',
        {"ingles-grupos-nominais"},
    ),
    ('Qual a diferença entre "actually" e "atualmente"?', {"ingles-cognatos-falsos-cognatos"}),
    ("Como reconhecer a voz passiva num texto técnico?", {"ingles-voz-passiva"}),
    ('A quem se refere "they" em "where they are used to eliminate damage"?', {"ingles-referencia-pronominal"}),
]
FORA = [
    "Como simplificar uma função com mapa de Karnaugh?",
    "Como fazer um LEFT JOIN em SQL?",
    "Me conte uma piada",
    "Qual a transformada de Laplace de e^{-at}?",
    "Como calcular a variância de uma variável aleatória?",
]


def test_exemplos_do_cadastro_sao_os_testados():
    assert list(ING.exemplos) == [p for p, _ in EXEMPLOS]


@pytest.mark.parametrize("pergunta, aceitos", EXEMPLOS)
def test_perguntas_de_exemplo_trazem_o_bloco_certo(pergunta, aceitos):
    assert aceitos & set(hibrida(pergunta))


def test_skimming_e_scanning_traz_os_dois_blocos():
    assert {"ingles-prova-skimming-hipotese", "ingles-prova-scanning"} <= set(hibrida("O que é skimming e scanning?"))


@pytest.mark.parametrize("pergunta", FORA)
def test_pergunta_de_outra_area_nao_traz_material(pergunta):
    assert hibrida(pergunta) == []


def test_isolamento_com_disciplinas_de_computacao():
    """Nas duas direções: ED, BD e PAA não trazem blocos de Inglês, e Inglês não traz blocos deles."""
    fronteira = [disciplinas.obter(i) for i in ("ed", "bd", "paa")]
    for p, _ in EXEMPLOS:
        for d in fronteira:
            assert not any(x.startswith("ingles-") for x in buscar(p, d))
    for d in fronteira:
        for p in d.exemplos:
            assert all(x.startswith("ingles-") for x in buscar(p))


# ---------------------------------------------------------------- catálogo e restrições


def test_catalogo_completo_e_coerente():
    obrigatorios = {
        "id",
        "nome",
        "autoria",
        "url",
        "idioma",
        "formato",
        "notacao",
        "topicos",
        "licenca",
        "acesso",
        "prioridade",
        "uso",
        "justificativa",
    }
    for f in FONTES:
        assert obrigatorios <= set(f), f["id"]
        assert f["prioridade"] in ("alta", "media", "referencia") and f["uso"] in ("acervo", "citada", "referencia")
        assert set(f["topicos"]) <= set(ING.assuntos), f["id"]
    assert {x for i_ in ITENS.values() for x in i_["fontes_catalogo"]} <= set(CATALOGO)
    assert {k for k, f in CATALOGO.items() if f["uso"] == "acervo"} == {
        "ufal-ingles-texto-prova",
        "pavela-2016-pps",
        "wilson-2014-best-practices",
    }
    assert "CC BY-NC 4.0" in CATALOGO["pavela-2016-pps"]["licenca"]
    assert "CC BY 4.0" in CATALOGO["wilson-2014-best-practices"]["licenca"]
    for protegido in ("pinto-grasping-the-meaning", "dubin-reading-by-all-means", "fromm-ufu-leitura-instrumental"):
        assert CATALOGO[protegido]["uso"] == "referencia"


def test_prova_e_binarios_fora_do_repositorio():
    arquivos = [p for p in (ROOT / "disciplinas/ingles").rglob("*") if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in (".pdf", ".png", ".jpg", ".jpeg", ".webp", ".docx", ".xml")]
    rastreados = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
    assert not [l for l in rastreados.splitlines() if re.search(r"Prova de Profici|journal\.pbio|\.docx$", l, re.I)]


@precisa_originais
def test_nome_dos_metadados_do_docx_nao_foi_versionado():
    core = zipfile.ZipFile(ORIGINAIS / "prova.docx").read("docProps/core.xml").decode("utf-8")
    nomes = {n.strip() for n in re.findall(r"<(?:dc:creator|cp:lastModifiedBy)>([^<]+)<", core) if n.strip()}
    assert nomes
    pasta = [p.read_text(encoding="utf-8") for p in (ROOT / "disciplinas/ingles").rglob("*") if p.is_file()]
    pasta.append((ROOT / "tests_acervo/ingles_trechos.json").read_text(encoding="utf-8"))
    assert not [n for n in nomes for t in pasta if n in t]


def test_documentacao_lista_fontes_e_blocos():
    curadoria = (ROOT / "disciplinas/ingles/CURADORIA.md").read_text(encoding="utf-8")
    assert [k for k in CATALOGO if f"`{k}`" not in curadoria] == []
    assert [k for k in ITENS if f"`{k}`" not in curadoria] == []
