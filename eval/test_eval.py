"""Harness de avaliação sem rede: critérios, notas do juiz, relatório e geração presa ao mesmo modelo."""
import asyncio
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matriz  # noqa: E402
from backend.llm import AllUnavailable, Model, Result  # noqa: E402
from backend.rag import Trecho  # noqa: E402
from prompt_candidato import SISTEMA_NOVO, nome_legivel, prompt_novo  # noqa: E402


def test_conjunto_dourado_tem_as_tres_perguntas_do_aluno_e_temas_validos():
    qs = matriz.perguntas()
    assert len(qs) >= 15 and len({q["id"] for q in qs}) == len(qs)
    assert sum(q["original_aluno"] for q in qs) == 3
    assert all(q["tema"] in matriz.CRITERIOS_POR_TEMA and q["referencia"] for q in qs)


def test_criterios_dependem_do_tema_e_do_pedido_de_formato():
    assert matriz.criterios({"tema": "pd"}) == "abcde"
    assert matriz.criterios({"tema": "guloso", "pedido_formato": "esquema"}) == "def"


def test_juiz_com_nota_fora_da_escala_ou_faltando_e_rejeitado():
    q = {"tema": "guloso"}
    assert matriz.validar_notas({"d": {"nota": 4, "motivo": "ok"}, "e": {"nota": 5}}, q)["d"]["nota"] == 4
    with pytest.raises(ValueError):
        matriz.validar_notas({"d": {"nota": 7}, "e": {"nota": 5}}, q)
    with pytest.raises(ValueError):
        matriz.validar_notas({"d": {"nota": 4}}, q)


def test_nomes_legiveis_das_fontes():
    assert nome_legivel("Resolução de aluno de PAA", "PAA_L5.pdf | página(s): 7, 8", "acervo") == "Lista 5, p. 7-8"
    assert nome_legivel("Livro", "página 48", "livro") == "Livro, p. 48"
    assert nome_legivel("x", "c01_prova1_2023-03_q2_algoritmo_x.md | página(s): não informada", "acervo") == "Prova"


def test_prompt_novo_sem_material_nao_finge_contexto_e_nao_exige_verificacao():
    assert "MATERIAL" not in prompt_novo("Pergunta?", [])
    t = Trecho("P1", "acervo", "Resolução de aluno de PAA", "texto", "PAA_L5.pdf | página(s): 4, 5")
    assert "[Lista 5, p. 4-5]" in prompt_novo("Pergunta?", [t])
    assert '"**Verificação:**"' not in SISTEMA_NOVO and "pseudocódigo em português" in SISTEMA_NOVO.lower()


class _LLMFalso:
    def __init__(self, falhas):
        self.falhas, self.chamadas = falhas, []
        self.breaker = type("B", (), {"reset": lambda self, m: None})()

    async def complete(self, sistema, prompt, *, models):
        self.chamadas.append(models)
        if len(self.chamadas) <= self.falhas:
            raise AllUnavailable([{"modelo": models[0].key, "resultado": "HTTP 429"}])
        return Result(text="resposta", model=models[0], seconds=1.0, attempts=[])


def test_geracao_tenta_de_novo_no_mesmo_modelo_e_nunca_troca():
    llm, m = _LLMFalso(falhas=2), Model("gemini", "forte")
    r = asyncio.run(matriz.gerar_uma(llm, m, None, "p", esperas=(0, 0, 0)))
    assert r["texto"] == "resposta" and all(ms == [m] for ms in llm.chamadas) and len(llm.chamadas) == 3
    r = asyncio.run(matriz.gerar_uma(_LLMFalso(falhas=9), m, None, "p", esperas=(0,)))
    assert r["texto"] is None and "indisponível" in r["erro"]


def test_relatorio_calcula_efeitos_pareados(tmp_path, monkeypatch):
    monkeypatch.setattr(matriz, "RESULTS", tmp_path)
    qs = matriz.perguntas()[:2]
    monkeypatch.setattr(matriz, "perguntas", lambda filtro=None: qs)
    linhas = []
    for q in qs:
        for papel, base in (("forte", 4), ("lite", 3)):
            for condicao, extra in (("generico", 0), ("atual_rag", -1), ("novo_rag", 1)):
                nota = max(1, min(5, base + extra))
                linhas.append({"id": q["id"], "papel": papel, "modelo": f"gemini:{papel}", "condicao": condicao,
                               "notas": {c: {"nota": nota, "motivo": ""} for c in matriz.criterios(q)}})
    (tmp_path / "notas.jsonl").write_text("\n".join(json.dumps(x) for x in linhas), encoding="utf-8")
    resumo = matriz.relatorio(None)
    assert resumo["efeitos"]["forte: TutorON atual - genérico"] == {"dif": -1.0, "n": 2, "vence": 0, "perde": 2}
    assert resumo["efeitos"]["modelo (forte - lite): generico"]["dif"] == 1.0
    assert resumo["criterio_sucesso"]["lite"]["iguala_ou_supera"] is True
    assert (tmp_path / "relatorio.md").read_text(encoding="utf-8").startswith("# Matriz")


def test_filtro_por_prefixo_pega_so_as_tres_originais():
    assert [q["id"].split("-")[0] for q in matriz.perguntas("A1,A2,A3")] == ["A1", "A2", "A3"]


def _nota(q, papel, condicao, nota, juiz="juiz-neutro", modelo=None):
    return {"id": q["id"], "papel": papel, "modelo": modelo or f"gemini:{papel}", "condicao": condicao, "juiz": juiz,
            "notas": {c: {"nota": nota, "motivo": ""} for c in matriz.criterios(q)}}


def test_relatorio_parcial_so_com_as_tres_originais(tmp_path, monkeypatch):
    monkeypatch.setattr(matriz, "RESULTS", tmp_path)
    originais = matriz.perguntas("A1,A2,A3")
    linhas = [_nota(q, "forte", c, n) for q in originais for c, n in (("generico", 4), ("novo_rag", 5))]
    linhas.append(_nota(originais[0], "forte", "atual_rag", 2))
    (tmp_path / "notas.jsonl").write_text("\n".join(json.dumps(x) for x in linhas), encoding="utf-8")
    resumo = matriz.relatorio(None)
    md = (tmp_path / "relatorio.md").read_text(encoding="utf-8")
    assert "resultado parcial" in md and "em 3 de 15 perguntas" in md
    assert "| forte novo_rag | 5 | 5 | 5 | 5 | 5 | 5.00 |" in md  # nota por critério a-e nas originais
    assert resumo["criterio_sucesso"]["forte"] == {"novo_rag": 5.0, "generico": 4.0, "perguntas": 3,
                                                   "iguala_ou_supera": True, "originais_a_b_d_ao_menos_4": True}
    assert resumo["efeitos"]["forte: TutorON atual - genérico"]["n"] == 1


def test_relatorio_mede_autopreferencia_quando_juiz_tambem_e_avaliado(tmp_path, monkeypatch):
    monkeypatch.setattr(matriz, "RESULTS", tmp_path)
    q = matriz.perguntas("A1")[0]
    linhas = []
    for papel, modelo in (("forte", "gemini:g-forte"), ("lite", "gemini:g-lite")):
        linhas.append(_nota(q, papel, "generico", 3, juiz="g-neutro", modelo=modelo))
        # O juiz g-forte dá +2 às próprias respostas e +0 às do lite, em relação ao juiz neutro.
        linhas.append(_nota(q, papel, "generico", 5 if papel == "forte" else 3, juiz="g-forte", modelo=modelo))
    (tmp_path / "notas.jsonl").write_text("\n".join(json.dumps(x) for x in linhas), encoding="utf-8")
    resumo = matriz.relatorio(None)
    assert resumo["juiz"] == "g-neutro"  # tabelas principais usam o juiz que não é avaliado
    assert resumo["vies_do_juiz"]["g-forte vs g-neutro"]["autopreferencia"] == 2.0
    assert "Viés do juiz" in (tmp_path / "relatorio.md").read_text(encoding="utf-8")


def test_folha_cega_embaralha_esconde_bracos_e_tira_citacoes():
    import folha_cega

    respostas = []
    for q in matriz.perguntas("A1,A2,A3"):
        for braco in folha_cega.BRACOS:
            texto = f"Resposta do braço {braco}. Ver (Lista 5, p. 7-8) e [P1, L2]." if braco != "generico" \
                else f"Resposta do braço {braco}."
            respostas.append({"id": q["id"], "papel": "forte", "modelo": "gemini:x", "condicao": braco, "texto": texto})
    folha, mapa = folha_cega.montar(respostas, "forte", semente=1, manter_citacoes=False)
    assert folha == folha_cega.montar(respostas, "forte", semente=1, manter_citacoes=False)[0]  # reproduzível
    assert "Lista 5" not in folha and "[P1" not in folha and "atual_rag" not in folha.split("Resposta do braço")[0]
    assert all(sorted(v["condicao"] for v in p.values()) == sorted(folha_cega.BRACOS) for p in mapa["perguntas"].values())
    assert folha.count("### Resposta ") == 9 and "Qual resposta você prefere?" in folha
    with pytest.raises(SystemExit):
        folha_cega.montar(respostas[:-1], "forte", semente=1, manter_citacoes=False)
