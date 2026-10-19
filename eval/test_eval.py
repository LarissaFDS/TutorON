"""Harness de avaliação sem rede: critérios, notas do juiz, relatório e geração presa ao mesmo modelo."""
import asyncio
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import decidir  # noqa: E402
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


def test_calibracao_recomenda_o_maior_limiar_sem_perder_acerto_conhecido():
    import diagnostico

    sims = {"Q1": [("bom", "b2-04-programacao-dinamica", 0.62), ("ruido", "b1-02-divisao-e-conquista", 0.57)],
            "Q2": [("c09", "b2-06-np-completude", 0.66), ("hub", "b1-02-divisao-e-conquista", 0.60)]}
    temas = {"Q1": "pd", "Q2": "np"}
    linhas = diagnostico.tabela_calibracao(sims, temas, {"Q1": ["bom"], "Q2": ["c09", "nao_indexado"]},
                                           limiares=[0.55, 0.60, 0.625, 0.65])
    por = {l["limiar"]: l for l in linhas}
    assert por[0.55]["blocos"] == 4 and por[0.55]["mesmo_assunto"] == 2
    assert por[0.60]["blocos"] == 3 and por[0.625]["esperados_perdidos"] == ["Q1:bom"]
    assert por[0.65]["vazias"] == 1
    assert diagnostico.recomendar(linhas) == 0.60  # "nao_indexado" não conta como perdido


def test_roteamento_resume_cota_e_degradacao_quando_o_log_tem(tmp_path):
    import diagnostico

    log = tmp_path / "perguntas.jsonl"
    log.write_text(json.dumps({"data": "2026-10-13T10:00:00+00:00", "modelo": "lite", "degradado": True,
                               "tentativas": [{"modelo": "gemini:forte", "resultado": "HTTP 429", "cota": "por_dia",
                                               "retry_delay_s": 7200.0},
                                              {"modelo": "gemini:lite", "resultado": "respondeu"}]}) + "\n",
                   encoding="utf-8")
    md = diagnostico.roteamento([log])
    assert "Respostas degradadas (lite depois de falha dos melhores): 1 de 1" in md
    assert "| gemini:forte | 1 | 0 | 0 | 7200.0 |" in md


def test_braco_atual_da_matriz_fica_congelado_no_prompt_de_12_10():
    import prompt_anterior

    assert '"**Verificação:**"' in prompt_anterior.SISTEMA  # o prompt antigo exigia a linha
    p = prompt_anterior.prompt("Q?", [Trecho("P1", "acervo", "Lista", "texto", "PAA_L5.pdf | página(s): 4")])
    assert "[P1] Lista — PAA_L5.pdf" in p
    assert "Nenhum trecho do material" in prompt_anterior.prompt("Q?", [])


def test_saida_separa_as_rodadas(tmp_path, monkeypatch):
    monkeypatch.setattr(matriz, "RESULTS", matriz.RESULTS)  # restaura depois do teste
    q = matriz.perguntas("A1")[0]
    for rodada, nota in (("rodada1", 3), ("rodada2", 5)):
        pasta = matriz.usar_saida(str(tmp_path / rodada))
        pasta.mkdir()
        (pasta / "notas.jsonl").write_text(json.dumps(_nota(q, "forte", "atual_rag", nota)), encoding="utf-8")
        matriz.relatorio(None)
    r1 = json.loads((tmp_path / "rodada1" / "resumo.json").read_text(encoding="utf-8"))
    r2 = json.loads((tmp_path / "rodada2" / "resumo.json").read_text(encoding="utf-8"))
    assert r1["notas"]["juiz-neutro"] == {f"{q['id']}|forte|atual_rag": 3.0}
    assert r2["medias"]["forte|atual_rag"] == 5.0
    assert not (tmp_path / "relatorio.md").exists()


# ---------------------------------------------------------------------- decidir.py e preflight.py

def _rodada(tmp_path, monkeypatch, nome, notas_por_braco, criterio=None, juizes=("juiz-neutro",)):
    """Resumo sintético pelo próprio relatorio(): notas_por_braco = {(papel, condicao): nota}."""
    monkeypatch.setattr(matriz, "RESULTS", tmp_path / nome)
    (tmp_path / nome).mkdir()
    linhas = []
    for q in matriz.perguntas("A1,A2,A3"):
        for (papel, condicao), nota in notas_por_braco.items():
            for juiz in juizes:
                n = _nota(q, papel, condicao, nota, juiz=juiz)
                if criterio and (papel, condicao) == criterio[0]:
                    n["notas"][criterio[1]]["nota"] = criterio[2]
                linhas.append(n)
    (tmp_path / nome / "notas.jsonl").write_text("\n".join(json.dumps(x) for x in linhas), encoding="utf-8")
    return matriz.relatorio(None)


BASE = {("forte", "generico"): 4, ("forte", "atual_sem_rag"): 4, ("forte", "atual_rag"): 4, ("forte", "novo_rag"): 4,
        ("lite", "generico"): 4, ("lite", "atual_sem_rag"): 4, ("lite", "atual_rag"): 4, ("lite", "novo_rag"): 4}


def test_decidir_aprova_prompt_so_se_todos_os_modelos_passam(tmp_path, monkeypatch):
    r1 = _rodada(tmp_path, monkeypatch, "ok", BASE)
    assert decidir.decidir(r1)["a"]["aprovado"] is True
    # Um critério b = 3 numa original do lite basta para manter o #25 em rascunho.
    r1 = _rodada(tmp_path, monkeypatch, "b3", BASE, criterio=(("lite", "novo_rag"), "b", 3))
    d = decidir.decidir(r1)
    assert d["a"]["aprovado"] is False and d["a"]["por_papel"]["forte"]["ok"] is True
    # novo_rag abaixo do genérico também reprova.
    r1 = _rodada(tmp_path, monkeypatch, "abaixo", {**BASE, ("forte", "generico"): 5})
    assert decidir.decidir(r1)["a"]["aprovado"] is False


def test_decidir_roteamento_usa_o_braco_que_vai_a_producao_e_limiar_0_5(tmp_path, monkeypatch):
    assert decidir.LIMIAR_ROTEAMENTO == 0.5
    # Prompt reprovado (novo < genérico) -> roteamento olha atual_rag: forte - lite = 1.0.
    r1 = _rodada(tmp_path, monkeypatch, "r1", {**BASE, ("forte", "generico"): 5, ("lite", "atual_rag"): 3})
    b = decidir.decidir(r1)["b"]
    assert b == {"braco": "atual_rag", "dif": 1.0, "abrir_pr": True}
    # Prompt aprovado -> olha novo_rag, onde forte e lite empatam.
    r1 = _rodada(tmp_path, monkeypatch, "r2", {**BASE, ("lite", "atual_rag"): 3})
    assert decidir.decidir(r1)["b"] == {"braco": "novo_rag", "dif": 0.0, "abrir_pr": False}


def test_decidir_h4_no_limiar_menos_0_3(tmp_path, monkeypatch):
    assert decidir.LIMIAR_H4 == -0.3
    sintetico = {"modelos": {"forte": "x", "lite": "y"},
                 "efeitos": {"forte: RAG (com - sem), prompt atual": {"dif": -0.3},
                             "lite: RAG (com - sem), prompt atual": {"dif": 0.5}}}
    assert decidir.h4(sintetico)["confirmada"] is True
    sintetico["efeitos"]["forte: RAG (com - sem), prompt atual"]["dif"] = -0.29
    assert decidir.h4(sintetico)["confirmada"] is False
    assert decidir.h4({"modelos": {"forte": "x"}, "efeitos": {}})["confirmada"] is None


def test_decidir_curadoria_e_pareada_com_o_mesmo_juiz(tmp_path, monkeypatch):
    r1 = _rodada(tmp_path, monkeypatch, "rodada1", BASE, juizes=("juiz-neutro", "outro"))
    r2 = _rodada(tmp_path, monkeypatch, "rodada2",
                 {("forte", "atual_rag"): 5, ("forte", "novo_rag"): 4, ("lite", "atual_rag"): 3, ("lite", "novo_rag"): 4},
                 juizes=("outro",))
    d = decidir.decidir(r1, r2)
    assert d["d"]["juiz"] == "outro"  # o juiz da rodada 1 não julgou a rodada 2
    assert d["d"]["bracos"]["forte|atual_rag"] == {"dif": 1.0, "n": 3, "vence": 3, "perde": 0, "efeito": "ajudou"}
    assert d["d"]["bracos"]["lite|atual_rag"]["efeito"] == "piorou"
    assert d["d"]["bracos"]["forte|novo_rag"]["efeito"] == "sem efeito claro"
    assert d["a_curadoria"]["por_papel"]["forte"]["iguala_ou_supera"] is True
    texto = decidir.texto(d)
    assert "(d) Efeito da curadoria" in texto and "heurísticos" in texto


def test_decidir_sem_juiz_comum_nao_inventa_efeito(tmp_path, monkeypatch):
    r1 = _rodada(tmp_path, monkeypatch, "rodada1", BASE, juizes=("a",))
    r2 = _rodada(tmp_path, monkeypatch, "rodada2", {("forte", "atual_rag"): 5}, juizes=("b",))
    d = decidir.decidir(r1, r2)
    assert d["d"] == {"juiz": None, "bracos": {}} and d["a_curadoria"]["aprovado"] is None


def test_preflight_estima_chamadas_das_duas_rodadas():
    import preflight

    assert preflight.estimar(3, ["generico", "atual_sem_rag", "atual_rag", "novo_sem_rag", "novo_rag"], 2, 4)[
        "chamadas"] == 90
    assert preflight.estimar(3, ["atual_rag", "novo_rag"], 2, 4)["chamadas"] == 36
