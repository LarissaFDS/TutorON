"""Acervo de Física Experimental 3 (Engenharia de Computação, ECOM026) e conferência das explicações com SymPy.

Os blocos parafraseiam o roteiro do Experimento 2 ("Campo a partir do potencial", Laboratório de Ensino do
IF-UFAL): equipotenciais numa cuba eletrolítica, blindagem por um anel condutor e as questões do roteiro.
Relatórios de alunos não entram no acervo.
"""

import re

import pytest
import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

LAB = disciplinas.obter("fislab3")
PASTA = ROOT / "disciplinas/fislab3"
CATALOGO = {f["id"]: f for f in read_json(PASTA / "fontes.json")["fontes"]}
TODOS = {i["id"]: i for i in read_json(LAB.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "fislab3")
TEXTO = " ".join(i["texto"] for i in TODOS.values())
x, y = sp.symbols("x y", real=True)


def buscar(pergunta, d=LAB):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def campo(V):
    return sp.Matrix([-sp.diff(V, x), -sp.diff(V, y)])


# ---------------------------------------------------------------- cadastro e acervo


def test_fislab3_cadastrada_com_acervo_proprio():
    assert LAB.nome == "Física Experimental 3" and LAB.itens.exists()
    ids = {c["id"] for c in read_json(LAB.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({LAB.itens, LAB.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(LAB.assuntos)
    assert ids == set(TODOS) and len(TODOS) == 3


def test_situacao_da_disciplina():
    assert LAB.situacao == "MVP" and not LAB.em_validacao and not LAB.aviso


def test_entra_no_quarto_periodo_de_ecom():
    from backend import cursos

    reg = next(d for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] == "fislab3")
    assert reg["cursos"] == {"ecom": 4}
    assert "fislab3" in cursos.preferidas("ecom", 4)


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas fislab3 --embeddings`."""
    assert disciplinas.registros(LAB) == read_json(LAB.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        texto = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert i["status_curadoria"] == "aprovado", i["id"]
        assert i["status_resolucao"] == "pendente_professor", i["id"]
        assert len(texto) <= 2200, i["id"]
        assert texto.count("$$") % 2 == 0, i["id"]
        ultima = texto.strip().splitlines()[-1]
        assert "**Verificação:**" in ultima, i["id"]
        assert "não é gabarito do professor" in texto, i["id"]
        assert "Status da resolução: pendente de confirmação do professor" in texto, i["id"]
        nomes = re.findall(r"`(test_\w+)`", ultima)
        assert nomes and all(n in globals() for n in nomes), i["id"]
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, arq.name
        for f in re.search(r"fontes_catalogo: (.+)", cab).group(1).split(","):
            assert f.strip() in CATALOGO and CATALOGO[f.strip()]["uso"] == "acervo", (arq.name, f)


def test_relatorios_de_alunos_ficam_fora():
    assert all(f["arquivo_local"] is None for f in CATALOGO.values())
    assert set(CATALOGO) == {"ufal-fislab3-roteiro-exp2", "halliday-eletromagnetismo"}
    assert CATALOGO["halliday-eletromagnetismo"]["uso"] == "referencia"
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in (".pdf", ".png", ".jpg", ".ggb", ".html")]


def test_sem_dados_pessoais():
    textos = TEXTO + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"\b\d{8,}\b", textos)


@pytest.mark.parametrize(
    ("pergunta", "esperado"),
    [
        ("Como mapear linhas equipotenciais na cuba eletrolítica com o multímetro?", "fislab3-exp2-equipotenciais-cuba"),
        ("Por que as linhas de campo são perpendiculares às equipotenciais?", "fislab3-exp2-equipotenciais-cuba"),
        ("O anel de latão na cuba é uma blindagem eletrostática perfeita?", "fislab3-exp2-blindagem-anel"),
        ("Existe contradição em fazer eletrostática com correntes iônicas na solução?", "fislab3-exp2-correntes-e-bateria"),
        ("Por que os polos de uma bateria ligados só ao ar ficam isolados?", "fislab3-exp2-correntes-e-bateria"),
    ],
)
def test_perguntas_reais_acham_o_bloco_certo(pergunta, esperado):
    assert buscar(pergunta)[:1] == [esperado], buscar(pergunta)


def test_fronteiras():
    for d in map(disciplinas.obter, ("fis3",)):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
    assert not buscar("Como funciona um flip-flop JK?")


# ---------------------------------------------------------------- conferência das explicações


def duas_linhas(a=1):
    return sp.log(sp.sqrt((x + a) ** 2 + y**2)) - sp.log(sp.sqrt((x - a) ** 2 + y**2))


def test_campo_perpendicular_as_equipotenciais():
    V = duas_linhas()
    E = campo(V)
    tangente = sp.Matrix([sp.diff(V, y), -sp.diff(V, x)])  # direção em que V não muda
    assert sp.simplify(E.dot(tangente)) == 0
    # E aponta para onde V diminui: E·∇V = −|∇V|² < 0
    ponto = {x: sp.Rational(1, 3), y: sp.Rational(1, 2)}
    assert (E.dot(-E)).subs(ponto) < 0
    # placas paralelas: V linear, campo uniforme
    d, V0 = sp.symbols("d V_0", positive=True)
    assert campo(V0 * x / d) == sp.Matrix([-V0 / d, 0])


def test_anel_condutor_blinda_o_interior():
    r, th = sp.symbols("r theta", positive=True)
    E0, R = sp.symbols("E_0 R", positive=True)
    # anel condutor aterrado num campo uniforme E0 x̂ (2D): fora, V = −E0 (r − R²/r) cos θ; dentro, V = 0
    fora = -E0 * (r - R**2 / r) * sp.cos(th)
    lap = sp.diff(r * sp.diff(fora, r), r) / r + sp.diff(fora, th, 2) / r**2
    assert sp.simplify(lap) == 0
    assert sp.simplify(fora.subs(r, R)) == 0  # mesmo potencial em toda a borda
    dentro = sp.Integer(0)
    assert sp.diff(dentro, r) == 0 and sp.diff(dentro, th) == 0  # E = 0 dentro
    assert sp.limit(fora / (-E0 * r * sp.cos(th)), r, sp.oo) == 1  # longe, volta ao campo uniforme


def test_meio_condutor_tem_o_mesmo_potencial_da_eletrostatica():
    V = duas_linhas()
    assert sp.simplify(sp.diff(V, x, 2) + sp.diff(V, y, 2)) == 0
    # ponteira fixa na origem (V = 0, equipotencial x = 0): a leitura troca de sinal ao cruzá-la
    assert V.subs({x: 0, y: 2}) == 0
    assert V.subs({x: sp.Rational(1, 2), y: 0}) > 0 > V.subs({x: -sp.Rational(1, 2), y: 0})
