"""Prompt do tutor e nomes legíveis das fontes (sem rede)."""
from pathlib import Path

from backend import prompts
from backend.rag import Trecho, contexto, nome_legivel

WEB = Path(__file__).resolve().parents[1] / "web"


def test_prompt_segue_o_roteiro_de_pd_e_nao_exige_verificacao():
    s = prompts.SISTEMA_TUTOR
    for trecho in ("Recorrência completa com casos base", "ANTES de qualquer código", "i-1 ou j-1",
                   "Pseudocódigo em português", "Rastreio", "Complexidade de tempo e de espaço"):
        assert trecho in s
    assert "Pedido de formato vem primeiro" in s and "esqueminha" in s
    assert '"**Verificação:**"' not in s and '"**Verificação:**"' in prompts.SISTEMA_TUTOR_ANTERIOR


def test_sem_material_o_bloco_some_e_nada_e_citado():
    p = prompts.prompt_tutor("Como funciona a mochila?", contexto([]))
    assert "MATERIAL" not in p and p.endswith("Como funciona a mochila?")


def test_material_usa_nomes_legiveis():
    t = Trecho("P1", "acervo", "Resolução de aluno de PAA", "S[i][s] = ...", "PAA_L5.pdf | página(s): 7, 8")
    p = prompts.prompt_tutor("Subset sum?", contexto([t]))
    assert "[Lista 5, p. 7-8] (Resolução de aluno de PAA)" in p and "[P1]" not in p
    assert t.publico()["nome"] == "Lista 5, p. 7-8" and t.publico()["rotulo"] == "P1"  # rotulo segue no payload


def test_nomes_legiveis():
    assert nome_legivel("página 48", "livro") == "Livro, p. 48"
    assert nome_legivel("PAA_L3.pdf | página(s): 4", "acervo") == "Lista 3, p. 4"
    assert nome_legivel("c01_prova1_2023-03_q2_algoritmo_x.md | página(s): não informada", "acervo") == "Prova"
    assert nome_legivel("e03_pd_substring_comum.md", "acervo") == "Material da equipe"
    assert nome_legivel("c09_lista7_q1_classes_resolucao.md | página(s): não informada", "acervo") == "Material da disciplina"


def test_site_mostra_o_nome_legivel_na_lista_de_fontes():
    assert "f.nome" in (WEB / "app.js").read_text(encoding="utf-8")
