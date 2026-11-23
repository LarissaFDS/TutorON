"""Acervo de Interação Humano-Computador (Ciência da Computação) e conferência dos exemplos.

Os blocos parafraseiam os slides de design centrado no usuário e as etapas do projeto de microteste
de usabilidade (IC-UFAL, 2020.2). As contas (SUS, contraste do WCAG, taxa de sucesso) e os exemplos
estruturados são conferidos aqui.
"""

import re

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

IHC = disciplinas.obter("ihc")
PASTA = ROOT / "disciplinas/ihc"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(IHC.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "ihc")
FRONTEIRA = ("projsw", "metodologia")


def buscar(pergunta, d=IHC):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo


def test_ihc_cadastrada_com_acervo_proprio():
    assert IHC.nome == "Interação Humano-Computador" and IHC.itens.exists()
    ids = {c["id"] for c in read_json(IHC.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({IHC.itens, IHC.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(IHC.assuntos)
    assert ids == set(TODOS)


def test_situacao_da_disciplina():
    assert IHC.situacao == "MVP" and not IHC.em_validacao and not IHC.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas ihc --embeddings`."""
    assert disciplinas.registros(IHC) == read_json(IHC.itens)


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


def test_sem_dados_pessoais_dos_trabalhos_nem_binarios():
    textos = " ".join(i["texto"] for i in TODOS.values()) + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"matr[ií]cula:? *\d", textos, re.I)
    assert "youtu.be" not in textos  # vídeos com participantes não entram
    assert not re.search(r"\bNota: *\d", textos)
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"].startswith("Protegido"):
            assert f["uso"] == "referencia", f["id"]
    soltos = [p for p in PASTA.rglob("*") if p.suffix.lower() in (".pdf", ".docx", ".pptx", ".png", ".jpg", ".jpeg")]
    assert not soltos


PERGUNTAS = [
    (
        "O que foi o caso Therac-25 e o que ensina sobre interfaces?",
        "ihc-nova-informatica-excelencia-no-design-utilizacao-universal-therac-25-iran-air-655",
    ),
    (
        "O que é utilização universal segundo Shneiderman?",
        "ihc-nova-informatica-excelencia-no-design-utilizacao-universal-therac-25-iran-air-655",
    ),
    (
        "Quais são os métodos centrados no usuário?",
        "ihc-metodos-centrados-no-usuario-regra-de-ouro-entrevista-etnografia-teste-de-utilizacao-feedback-do-cliente",
    ),
    (
        "Qual a regra de ouro do design: conheça seus usuários",
        "ihc-metodos-centrados-no-usuario-regra-de-ouro-entrevista-etnografia-teste-de-utilizacao-feedback-do-cliente",
    ),
    (
        "Como fazer um microteste de usabilidade com pensamento em voz alta?",
        "ihc-microteste-de-usabilidade-perfil-iniciante-intermediario-avancado-pensamento-em-voz-alta",
    ),
    (
        "Como listar as tarefas do usuário numa árvore e comparar com o modelo mental?",
        "ihc-arvore-de-tarefas-caminho-previsto-modelo-mental-do-usuario-comparar-desvios",
    ),
    ("O que é uma persona e como elaborar?", "ihc-personas-conceito-alan-cooper-dados-reais-como-elaborar-exemplo"),
    ("Como calcular a pontuação do SUS?", "ihc-system-usability-scale-sus-questionario-10-itens-calculo-da-pontuacao"),
    ("Quais são as 10 heurísticas de Nielsen?", "ihc-dez-heuristicas-de-nielsen-avaliacao-heuristica-severidade"),
    (
        "Como tornar a interface acessível para idosos e pessoas com deficiência?",
        "ihc-acessibilidade-letramento-digital-idosos-pessoas-com-deficiencia-wcag",
    ),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Como calcular a pontuação do SUS?", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a impedância de um indutor?")


# ---------------------------------------------------------------- h01 e h02


def _mensagem_util(msg):
    m = msg.lower()
    diz_o_que = any(p in m for p in ("não foi", "falhou", "inválid", "excede", "não pode"))
    diz_como = any(p in m for p in ("tente", "verifique", "digite", "use ", "corrija"))
    return diz_o_que and diz_como


def test_mensagem_de_erro_util():
    assert not _mensagem_util("Malfunction 54")
    assert _mensagem_util("A dose excede o limite. Verifique o valor digitado e confirme.")


METODOS = {"avaliação das necessidades": "antes", "teste de utilização": "durante", "feedback do cliente": "depois"}


def test_metodos_por_fase():
    assert set(METODOS.values()) == {"antes", "durante", "depois"}
    assert METODOS["teste de utilização"] == "durante"


# ---------------------------------------------------------------- h03 microteste

REGISTRO = [
    {"tarefa": "ver saldo", "sucesso": True, "segundos": 40},
    {"tarefa": "pagar boleto", "sucesso": False, "segundos": 180},
    {"tarefa": "ver extrato", "sucesso": True, "segundos": 50},
    {"tarefa": "trocar senha", "sucesso": True, "segundos": 90},
]


def test_sucesso_e_tempo_por_tarefa():
    taxa = sum(r["sucesso"] for r in REGISTRO) / len(REGISTRO)
    tempo_ok = [r["segundos"] for r in REGISTRO if r["sucesso"]]
    assert taxa == 0.75
    assert sum(tempo_ok) / len(tempo_ok) == 60


# ---------------------------------------------------------------- h04 árvore de tarefas

PREVISTO = ["abrir app", "em cartaz", "filme", "data", "horário", "assento", "confirmar", "pagar"]


def _comparar(previsto, observado):
    fora = [p for p in observado if p not in previsto]
    abandono = None if observado and observado[-1] == previsto[-1] else (observado[-1] if observado else None)
    return {"passos_a_mais": len(observado) - len(previsto), "fora_da_arvore": fora, "abandono": abandono}


def test_comparar_caminho_previsto():
    assert _comparar(PREVISTO, PREVISTO) == {"passos_a_mais": 0, "fora_da_arvore": [], "abandono": None}
    desvio = [
        "abrir app",
        "menu",
        "promoções",
        "em cartaz",
        "filme",
        "data",
        "horário",
        "assento",
        "confirmar",
        "pagar",
    ]
    r = _comparar(PREVISTO, desvio)
    assert r["passos_a_mais"] == 2 and r["fora_da_arvore"] == ["menu", "promoções"] and r["abandono"] is None
    parou = ["abrir app", "em cartaz", "filme", "data"]
    assert _comparar(PREVISTO, parou)["abandono"] == "data"


# ---------------------------------------------------------------- h05 personas

PERSONA = {
    "nome": ("Dona Lúcia", "ilustrativo"),
    "objetivos": ("saber quando o ônibus passa", "entrevistas"),
    "frustracoes": ("letras pequenas, mapas confusos", "observação"),
    "experiencia": ("iniciante", "questionário"),
    "cenario": ("no ponto, com sol na tela", "observação"),
}


def test_persona_tem_campos_essenciais():
    assert {"objetivos", "frustracoes", "experiencia", "cenario"} <= set(PERSONA)
    assert all(origem for _, origem in PERSONA.values())


# ---------------------------------------------------------------- h06 SUS


def sus(respostas):
    assert len(respostas) == 10 and all(1 <= r <= 5 for r in respostas)
    impares = sum(r - 1 for r in respostas[0::2])
    pares = sum(5 - r for r in respostas[1::2])
    return 2.5 * (impares + pares)


def test_pontuacao_sus():
    assert sus([4, 2, 5, 1, 4, 2, 4, 2, 5, 1]) == 85
    assert sus([5, 1] * 5) == 100
    assert sus([1, 5] * 5) == 0
    assert sus([3] * 10) == 50


# ---------------------------------------------------------------- h07 heurísticas

HEURISTICAS = [
    "Visibilidade do estado do sistema",
    "Correspondência entre o sistema e o mundo real",
    "Controle e liberdade do usuário",
    "Consistência e padrões",
    "Prevenção de erros",
    "Reconhecer em vez de lembrar",
    "Flexibilidade e eficiência de uso",
    "Design estético e minimalista",
    "Ajudar a reconhecer, diagnosticar e recuperar erros",
    "Ajuda e documentação",
]


def test_heuristicas_de_nielsen():
    assert len(HEURISTICAS) == 10 == len(set(HEURISTICAS))
    texto = TODOS["ihc-dez-heuristicas-de-nielsen-avaliacao-heuristica-severidade"]["texto"]
    posicoes = [texto.index(h) for h in HEURISTICAS]
    assert posicoes == sorted(posicoes)
    problemas = {"Malfunction 54": 9, "sem desfazer ao apagar": 3, "ícone de olho sem rótulo": 6}
    assert all(HEURISTICAS[n - 1] for n in problemas.values())


# ---------------------------------------------------------------- h08 contraste


def _luminancia(hexcor):
    def canal(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (int(hexcor[i : i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * canal(r) + 0.7152 * canal(g) + 0.0722 * canal(b)


def contraste(a, b):
    la, lb = sorted((_luminancia(a), _luminancia(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def test_razao_de_contraste():
    assert contraste("#000000", "#FFFFFF") == pytest.approx(21)
    assert contraste("#336699", "#336699") == pytest.approx(1)
    assert contraste("#777777", "#FFFFFF") < 4.5 < contraste("#767676", "#FFFFFF")
