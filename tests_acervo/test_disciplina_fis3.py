"""Acervo de Física 3 (Engenharia de Computação, ECOM022) e conferência das resoluções com SymPy.

Os blocos parafraseiam as duas questões da prova 1 (2025) do Prof. Alexandre de Morais Carvalho (IF-UFAL):
Lei de Gauss num cilindro maciço e potencial no eixo de uma coroa circular. As contas são refeitas aqui.
"""

import re

import pytest
import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

FIS3 = disciplinas.obter("fis3")
PASTA = ROOT / "disciplinas/fis3"
CATALOGO = {f["id"]: f for f in read_json(PASTA / "fontes.json")["fontes"]}
TODOS = {i["id"]: i for i in read_json(FIS3.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "fis3")
TEXTO = " ".join(i["texto"] for i in TODOS.values())
EPS0 = 8.8541878128e-12


def buscar(pergunta, d=FIS3):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo


def test_fis3_cadastrada_com_acervo_proprio():
    assert FIS3.nome == "Física 3" and FIS3.itens.exists()
    ids = {c["id"] for c in read_json(FIS3.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({FIS3.itens, FIS3.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(FIS3.assuntos)
    assert ids == set(TODOS) and len(TODOS) == 2


def test_situacao_da_disciplina():
    assert FIS3.situacao == "MVP" and not FIS3.em_validacao and not FIS3.aviso


def test_entra_no_quarto_periodo_de_ecom():
    from backend import cursos

    reg = next(d for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] == "fis3")
    assert reg["cursos"] == {"ecom": 4}
    assert "fis3" in cursos.preferidas("ecom", 4)


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas fis3 --embeddings`."""
    assert disciplinas.registros(FIS3) == read_json(FIS3.itens)


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


def test_livro_e_resolucao_manuscrita_ficam_so_no_catalogo():
    for fid in ("halliday-eletromagnetismo", "ufal-fis3-resolucao-prova1"):
        assert CATALOGO[fid]["uso"] == "referencia"
    assert all(f["arquivo_local"] is None for f in CATALOGO.values())
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in (".pdf", ".png", ".jpg", ".html")]


def test_sem_dados_pessoais():
    textos = TEXTO + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"\b\d{8,}\b", textos)


@pytest.mark.parametrize(
    ("pergunta", "esperado"),
    [
        ("Como achar o campo elétrico dentro de um cilindro maciço carregado com a Lei de Gauss?", "fis3-prova1-q1-gauss-cilindro"),
        ("Qual o campo elétrico fora de um cilindro infinito com densidade de carga uniforme?", "fis3-prova1-q1-gauss-cilindro"),
        ("Como achar o potencial no eixo de uma coroa circular de raio interno e raio externo com densidade superficial de carga?", "fis3-prova1-q2-potencial-coroa"),
        ("Como dividir uma distribuição em anéis para somar o potencial no eixo?", "fis3-prova1-q2-potencial-coroa"),
    ],
)
def test_quatro_perguntas_reais_acham_o_bloco_certo(pergunta, esperado):
    assert buscar(pergunta)[:1] == [esperado], buscar(pergunta)


def test_fronteiras():
    for d in map(disciplinas.obter, ("fis1", "fis2", "calc4")):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
    assert not buscar("Como funciona um flip-flop JK?")


# ---------------------------------------------------------------- conferência das resoluções


def test_prova1_q1_gauss_cilindro():
    r, R, rho, L, eps = sp.symbols("r R rho L epsilon_0", positive=True)
    dentro = sp.solve(sp.Eq(sp.Symbol("E") * 2 * sp.pi * r * L, rho * sp.pi * r**2 * L / eps), sp.Symbol("E"))[0]
    fora = sp.solve(sp.Eq(sp.Symbol("E") * 2 * sp.pi * r * L, rho * sp.pi * R**2 * L / eps), sp.Symbol("E"))[0]
    assert sp.simplify(dentro - rho * r / (2 * eps)) == 0
    assert sp.simplify(fora - rho * R**2 / (2 * eps * r)) == 0
    assert sp.simplify(dentro.subs(r, R) - fora.subs(r, R)) == 0  # contínuo em r = R
    # divergente em coordenadas cilíndricas: (1/r) d(r E)/dr
    assert sp.simplify(sp.diff(r * dentro, r) / r - rho / eps) == 0
    assert sp.simplify(sp.diff(r * fora, r) / r) == 0


def test_prova1_q2_potencial_coroa():
    rp, z, a, b, sig, eps = sp.symbols("r_p z a b sigma epsilon_0", positive=True)
    integral = sp.integrate(sig * 2 * sp.pi * rp / sp.sqrt(z**2 + rp**2), (rp, a, b)) / (4 * sp.pi * eps)
    fechada = sig / (2 * eps) * (sp.sqrt(z**2 + b**2) - sp.sqrt(z**2 + a**2))
    assert sp.simplify(integral - fechada) == 0
    R = 0.130
    sigma = 6.20e-12 / 1e-4  # pC/cm² → C/m²
    assert sigma == pytest.approx(6.20e-8)
    v = float(fechada.subs({sig: sigma, eps: EPS0, z: 2 * R, b: R, a: 0.2 * R}))
    assert v == pytest.approx(102.9, abs=0.1)
    assert sigma / (2 * EPS0) == pytest.approx(3.50e3, rel=1e-3)
