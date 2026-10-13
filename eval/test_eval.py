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
