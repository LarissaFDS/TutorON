"""Rotas do site com modelos e RAG falsos: nada sai para a rede."""
import json
import time

import pytest
from fastapi.testclient import TestClient

from backend import tarefas
from backend.rag import Trecho
from backend.tests.test_llm import FakeLLM


def montar(tmp_path, monkeypatch, roteiro, **kw):
    from backend import main

    async def recuperar(pergunta, llm, settings, disciplina=None):
        return [Trecho("P1", "acervo", "Prova de PAA", "T(n)=2T(n/2)+n", "prova1.pdf")]
    monkeypatch.setattr(tarefas, "recuperar", recuperar)
    monkeypatch.setattr(tarefas.asyncio, "sleep", _sleep_curto)
    llm = FakeLLM(roteiro, **kw)
    llm.settings = llm.settings.__class__(**{**llm.settings.__dict__, "data_dir": tmp_path, "rate_limit_per_10min": 5})
    return main.create_app(settings=llm.settings, llm=llm, warm_up=False), llm


_sleep_original = tarefas.asyncio.sleep


async def _sleep_curto(segundos, *a, **kw):
    return await _sleep_original(min(segundos, 0.01), *a, **kw)


@pytest.fixture
def cliente(tmp_path, monkeypatch):
    app, _ = montar(tmp_path, monkeypatch, {"g1": ("ok", "resposta $\\Theta(n \\log n)$")})
    with TestClient(app) as c:
        c.tmp = tmp_path
        yield c


def esperar(c, criada, limite=10):
    fim = time.monotonic() + limite
    while time.monotonic() < fim:
        t = c.get(f"/api/tarefas/{criada['id']}").json()
        if t["status"] in ("pronta", "erro"):
            return t
        time.sleep(0.02)
    raise AssertionError("tarefa não terminou")


def test_pagina_e_status(cliente):
    html = cliente.get("/").text
    assert "Fase MVP" in html and "monitoria" not in html.lower() and "UFAL" not in html
    assert cliente.get("/design.css").status_code == 200
    assert cliente.get("/api/status").json()["gemini"]["habilitado"] is True


def test_perguntar_por_tarefa_registra(cliente):
    criada = cliente.post("/api/perguntar", json={"pergunta": "Quanto custa o merge sort?"}).json()
    assert criada["status"] in ("fila", "gerando")  # responde na hora, sem esperar a IA
    t = esperar(cliente, criada)
    assert t["status"] == "pronta" and t["texto"].startswith("resposta") and t["fontes"][0]["rotulo"] == "P1"
    linha = json.loads((cliente.tmp / "perguntas.jsonl").read_text(encoding="utf-8").splitlines()[0])
    assert linha["modelo"] == "g1" and linha["id"] == t["id_resposta"]
    assert cliente.post("/api/feedback", json={"id": t["id_resposta"], "util": False, "erro_matematico": True}).json()["salvo"]


def test_comparar_e_avaliar_cegos(cliente):
    criada = cliente.post("/api/comparar", json={"pergunta": "Explique o Teorema Mestre"}).json()
    par = esperar(cliente, criada)
    assert {"sessao", "pergunta", "A", "B"} <= set(par)
    assert "tutoron" not in json.dumps(par) and "generico" not in json.dumps(par)  # nada revela os lados
    notas = {"clareza": 4, "confianca": 5, "utilidade": 4, "erro_matematico": False}
    corpo = {"sessao": par["sessao"], "preferida": "A", "A": notas, "B": {**notas, "erro_matematico": True}}
    assert cliente.post("/api/avaliar", json=corpo).json() == {"salvo": True}
    # Reenvio (rede caiu depois de gravar): não pode dar erro nem duplicar.
    assert cliente.post("/api/avaliar", json=corpo).json() == {"salvo": True}
    linhas = (cliente.tmp / "validacao" / "avaliacoes.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(linhas) == 1
    linha = json.loads(linhas[0])
    assert linha["preferida_condicao"] == ("tutoron" if linha["lado_tutoron"] == "A" else "generico")
    assert set(linha["respostas"]) == {"tutoron", "generico"}
    assert cliente.post("/api/avaliar", json={**corpo, "sessao": "inexistente"}).status_code == 400


def test_todos_fora_tenta_de_novo_e_responde(tmp_path, monkeypatch):
    """Primeira rodada sem nenhum modelo; na segunda o local volta (ex.: Ollama reiniciou)."""
    app, llm = montar(tmp_path, monkeypatch, {})
    original = llm._provider
    chamadas = {"n": 0}

    def provedor(model, system, prompt):
        if model.provider == "ollama":
            chamadas["n"] += 1
            if chamadas["n"] >= 2:
                llm.roteiro[model.name] = ("ok", "resposta do local")
        return original(model, system, prompt)
    llm._provider = provedor
    with TestClient(app) as c:
        t = esperar(c, c.post("/api/perguntar", json={"pergunta": "O que é DP?"}).json())
        assert t["status"] == "pronta" and t["texto"] == "resposta do local"
        par = esperar(c, c.post("/api/comparar", json={"pergunta": "O que é DP?"}).json())
        assert par["status"] == "pronta" and par["A"] and par["B"]


def test_nenhum_modelo_nunca_deixa_tarefa_pendurada(tmp_path, monkeypatch):
    app, _ = montar(tmp_path, monkeypatch, {})
    with TestClient(app) as c:
        t = esperar(c, c.post("/api/perguntar", json={"pergunta": "O que é DP?"}).json())
        assert t["status"] == "erro" and t["mensagem"]
        t = esperar(c, c.post("/api/comparar", json={"pergunta": "O que é DP?"}).json())
        assert t["status"] == "erro" and t["mensagem"]


def test_tarefa_inexistente(cliente):
    r = cliente.get("/api/tarefas/naoexiste")
    assert r.status_code == 404 and "erro" in r.json()


def test_validacao_de_entrada(cliente):
    assert cliente.post("/api/perguntar", json={"pergunta": "  "}).status_code == 422
    r = cliente.post("/api/avaliar", json={"sessao": "x", "preferida": "A", "A": {"clareza": 9}, "B": {}})
    assert r.status_code == 422 and "erro" in r.json()


def test_limite_por_cliente_nao_conta_consultas(cliente):
    criada = cliente.post("/api/perguntar", json={"pergunta": "pergunta 0"}, headers={"cf-connecting-ip": "1.2.3.4"}).json()
    for _ in range(20):  # consultar o andamento não gasta o limite
        cliente.get(f"/api/tarefas/{criada['id']}")
    codigos = [cliente.post("/api/perguntar", json={"pergunta": f"pergunta {i}"},
                            headers={"cf-connecting-ip": "1.2.3.4"}).status_code for i in range(1, 6)]
    assert codigos[:4] == [200] * 4 and codigos[-1] == 429


def test_rotas_locais_bloqueadas_pelo_tunel(cliente):
    assert cliente.get("/api/resultados").status_code == 200
    assert cliente.get("/api/resultados", headers={"cf-connecting-ip": "1.2.3.4"}).status_code == 404
    assert cliente.get("/resultados", headers={"x-forwarded-for": "1.2.3.4"}).status_code == 404
    assert cliente.post("/api/reiniciar-modelos", headers={"cf-connecting-ip": "1.2.3.4"}).status_code == 404


def test_cli_compativel(cliente):
    r = cliente.post("/api/v1/questions", json={"question": "O que é DP?"})
    assert r.status_code == 200 and r.json()["answer"].startswith("resposta")
