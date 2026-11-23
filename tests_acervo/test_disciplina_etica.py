"""Acervo de Computação, Sociedade e Ética (Ciência da Computação) e conferência das citações.

Os blocos orientam as avaliações escritas do IC-UFAL (2020.2). As citações da LGPD são conferidas
contra uma tabela tirada do texto oficial no Planalto (consulta de 22/11/2026).
"""

import re

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

ETICA = disciplinas.obter("etica")
PASTA = ROOT / "disciplinas/etica"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(ETICA.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "etica")
FRONTEIRA = ("metodologia", "seguranca")
TEXTO = " ".join(i["texto"] for i in TODOS.values())


def buscar(pergunta, d=ETICA):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def bloco(prefixo):
    return next(i["texto"] for k, i in TODOS.items() if k.startswith(prefixo))


# ---------------------------------------------------------------- cadastro e acervo


def test_etica_cadastrada_com_acervo_proprio():
    assert ETICA.nome == "Computação, Sociedade e Ética" and ETICA.itens.exists()
    ids = {c["id"] for c in read_json(ETICA.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({ETICA.itens, ETICA.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(ETICA.assuntos)
    assert ids == set(TODOS)


def test_situacao_da_disciplina():
    assert ETICA.situacao == "MVP" and not ETICA.em_validacao and not ETICA.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas etica --embeddings`."""
    assert disciplinas.registros(ETICA) == read_json(ETICA.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert len(t) <= 2200, i["id"]
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


def test_sem_dados_pessoais_nem_binarios():
    textos = TEXTO + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"matr[ií]cula:? *\d", textos, re.I)
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"].startswith("Protegido"):
            assert f["uso"] == "referencia", f["id"]
    soltos = [p for p in PASTA.rglob("*") if p.suffix.lower() in (".pdf", ".docx", ".pptx", ".png", ".jpg", ".jpeg")]
    assert not soltos


def test_codigo_ieee_nao_e_numerado_nem_reproduzido():
    # a página oficial não foi lida: o bloco não pode inventar itens do código
    assert not re.search(r"IEEE[^.]{0,40}\b(item|cláusula|seção) *\d", TEXTO, re.I)


PERGUNTAS = [
    (
        "Como fazer uma análise crítica de artigo científico sobre ética e moral?",
        "etica-analise-critica-de-artigo-cientifico-etica-e-moral-resumo-por-secao-perguntas-conclusao",
    ),
    (
        "Qual a diferença entre ética e moral?",
        "etica-analise-critica-de-artigo-cientifico-etica-e-moral-resumo-por-secao-perguntas-conclusao",
    ),
    (
        "Como estruturar a pesquisa com introdução, desenvolvimento e considerações finais?",
        "etica-como-escrever-a-pesquisa-introducao-desenvolvimento-consideracoes-finais-referencias-video-criterios",
    ),
    (
        "Uso das tecnologias de informação durante a pandemia de COVID-19",
        "etica-uso-das-tecnologias-de-informacao-e-comunicacao-na-pandemia-de-covid-19-ensino-remoto-privacidade-exclusao-digital",
    ),
    (
        "Questões ambientais e computação verde",
        "etica-questoes-ambientais-e-computacao-verde-energia-de-data-centers-pue-lixo-eletronico",
    ),
    (
        "Educação a distância: questões atuais e perspectivas para o futuro",
        "etica-educacao-a-distancia-questoes-atuais-e-perspectivas-para-o-futuro-acesso-evasao-qualidade",
    ),
    (
        "Como elaborar um código de conduta ética para uma instituição de ensino?",
        "etica-codigo-de-conduta-etica-instituicao-de-ensino-superior-alunos-colaboradores-plataforma-de-ensino",
    ),
    (
        "Estudo de caso de inteligência artificial com a técnica dos 4 passos e o código IEEE",
        "etica-estudo-de-caso-inteligencia-artificial-tecnica-dos-4-passos-codigo-de-etica-ieee-vies-algoritmico",
    ),
    (
        "Quais os princípios da LGPD, como finalidade, adequação e necessidade?",
        "etica-lgpd-lei-geral-de-protecao-de-dados-dado-pessoal-sensivel-principios-bases-legais-direitos-do-titular",
    ),
    (
        "Quais os direitos do titular dos dados na LGPD?",
        "etica-lgpd-direitos-do-titular-revisao-de-decisao-automatizada-criancas-e-adolescentes-sancoes",
    ),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Quais os princípios da LGPD, como finalidade, adequação e necessidade?", d)).isdisjoint(
            TODOS
        )
    assert not buscar("Como calcular a impedância de um indutor?")


# ---------------------------------------------------------------- avaliações


def test_roteiro_analise_critica():
    t = bloco("etica-analise-critica").lower()
    assert "seção por seção" in t and "perguntas sugestivas" in t and "análise da conclusão" in t


def test_criterios_somam_50():
    criterios = {"escrito": 25, "video": 10, "dupla": 10, "referencias": 5}
    assert sum(criterios.values()) == 50 and 2 * sum(criterios.values()) == 100
    t = bloco("etica-como-escrever")
    assert all(f"0 a {v}" in t for v in criterios.values())


def test_pue():
    def pue(total, ti):
        return total / ti

    assert pue(1500, 1000) == 1.5
    assert pue(1000, 1000) == 1  # o total inclui a TI, então nunca fica abaixo de 1
    assert "PUE de 1,5" in bloco("etica-questoes-ambientais")


def test_codigo_tem_partes_essenciais():
    t = bloco("etica-codigo-de-conduta").lower()
    for parte in (
        "abrangência",
        "regras por tema",
        "canal de denúncia",
        "apuração",
        "medidas disciplinares",
        "revisão",
    ):
        assert parte in t, parte


def test_quatro_passos_na_ordem():
    t = bloco("etica-estudo-de-caso")
    passos = ["Reunir os dados relevantes", "Analisar os dados", "Negociar um acordo", "Avaliar as alternativas"]
    posicoes = [t.index(p) for p in passos]
    assert posicoes == sorted(posicoes)


# ---------------------------------------------------------------- LGPD (tabela conferida no Planalto)

ART5 = {
    "I": "dado pessoal",
    "II": "dado pessoal sensível",
    "III": "dado anonimizado",
    "V": "titular",
    "VI": "controlador",
    "VII": "operador",
    "VIII": "encarregado",
    "X": "tratamento",
}
ART6 = [
    "finalidade",
    "adequação",
    "necessidade",
    "livre acesso",
    "qualidade dos dados",
    "transparência",
    "segurança",
    "prevenção",
    "não discriminação",
    "responsabilização e prestação de contas",
]
ROMANOS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
ART7 = {
    "I": "consentimento",
    "II": "obrigação legal",
    "V": "contrato",
    "VII": "proteção da vida",
    "VIII": "tutela da saúde",
    "IX": "legítimo interesse",
    "X": "proteção do crédito",
}


def test_lgpd_principios_e_bases():
    lgpd = bloco("etica-lgpd-lei-geral")
    for inc, termo in ART5.items():
        assert re.search(rf"\*\*{termo}\*\* \({inc}\)", lgpd), (inc, termo)
    pos = [lgpd.index(p) for p in ART6]
    assert len(ART6) == 10 and pos == sorted(pos)
    for inc, termo in ART7.items():
        assert re.search(rf"{termo}\*?\*? \({inc}\)", lgpd), (inc, termo)
    # citações espalhadas nos outros blocos
    assert "art. 5º, II" in TEXTO and "art. 6º, III" in TEXTO and "art. 6º, IX" in TEXTO
    assert ART6[ROMANOS.index("III")] == "necessidade" and ART6[ROMANOS.index("IX")] == "não discriminação"
    assert ART5["II"] == "dado pessoal sensível"
    assert "art. 20" in TEXTO


def test_lgpd_direitos():
    t = bloco("etica-lgpd-direitos")
    assert "(art. 18)" in t and "**art. 20**" in t and "(art. 14)" in t and "(art. 52)" in t
    assert "melhor interesse" in t and "um dos pais" in t
    # valores da multa não foram conferidos no texto: o bloco não os cita
    assert "R$" not in t and "%" not in t
