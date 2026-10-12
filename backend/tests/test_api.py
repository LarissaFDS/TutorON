"""Rotas do site com modelos e RAG falsos: nada sai para a rede."""
import json

import pytest
from fastapi.testclient import TestClient

from backend import main
from backend.rag import Trecho
from backend.tests.test_llm import FakeLLM


@pytest.fixture
def cliente(tmp_path, monkeypatch):
    async def recuperar(pergunta, llm, settings):
        return [Trecho("P1", "acervo", "Prova de PAA", "T(n)=2T(n/2)+n", "prova1.pdf")]
    monkeypatch.setattr(main, "recuperar", recuperar)
    llm = FakeLLM({"g1": ("ok", "resposta $\\Theta(n \\log n)$")})
    llm.settings = llm.settings.__class__(**{**llm.settings.__dict__, "data_dir": tmp_path, "rate_limit_per_10min": 5})
    app = main.create_app(settings=llm.settings, llm=llm, warm_up=False)
    with TestClient(app) as c:
        c.tmp = tmp_path
        yield c


def eventos(resposta):
    return [json.loads(b[6:]) for b in resposta.text.split("\n\n") if b.startswith("data: ")]


def test_pagina_e_status(cliente):
    assert cliente.get("/").status_code == 200
    assert "TutorON" in cliente.get("/design.css").text or cliente.get("/design.css").status_code == 200
    s = cliente.get("/api/status").json()
    assert s["gemini"]["habilitado"] is True


def test_perguntar_streaming_registra(cliente):
    r = cliente.post("/api/perguntar", json={"pergunta": "Quanto custa o merge sort?"})
    evs = eventos(r)
    assert evs[0]["tipo"] == "fontes" and evs[0]["fontes"][0]["rotulo"] == "P1"
    assert any(e["tipo"] == "modelo" and e["modelo"] == "g1" for e in evs)
    fim = evs[-1]
    assert fim["tipo"] == "fim" and fim["id"]
    linha = json.loads((cliente.tmp / "perguntas.jsonl").read_text(encoding="utf-8").splitlines()[0])
    assert linha["resposta"].startswith("resposta") and linha["modelo"] == "g1"
    assert cliente.post("/api/feedback", json={"id": fim["id"], "util": False, "erro_matematico": True}).json()["salvo"]


def test_comparar_e_avaliar_cegos(cliente):
    par = cliente.post("/api/comparar", json={"pergunta": "Explique o Teorema Mestre"}).json()
    assert set(par) == {"sessao", "pergunta", "A", "B"}  # nada revela qual é o TutorON
    notas = {"clareza": 4, "confianca": 5, "utilidade": 4, "erro_matematico": False}
    r = cliente.post("/api/avaliar", json={"sessao": par["sessao"], "preferida": "A", "A": notas,
                                           "B": {**notas, "erro_matematico": True}, "comentario": "=cmd"})
    assert r.json() == {"salvo": True}
    linha = json.loads((cliente.tmp / "validacao" / "avaliacoes.jsonl").read_text(encoding="utf-8"))
    assert linha["lado_tutoron"] in ("A", "B")
    assert linha["preferida_condicao"] == ("tutoron" if linha["lado_tutoron"] == "A" else "generico")
    assert set(linha["respostas"]) == {"tutoron", "generico"}
    assert linha["respostas"]["tutoron"]["fontes"][0]["rotulo"] == "P1"
    # Não dá para votar duas vezes na mesma comparação.
    assert cliente.post("/api/avaliar", json={"sessao": par["sessao"], "preferida": "B", "A": notas, "B": notas}).status_code == 400


def test_validacao_de_entrada(cliente):
    assert cliente.post("/api/perguntar", json={"pergunta": "  "}).status_code == 422
    r = cliente.post("/api/avaliar", json={"sessao": "x", "preferida": "A", "A": {"clareza": 9}, "B": {}})
    assert r.status_code == 422 and "erro" in r.json()


def test_limite_por_cliente(cliente):
    codigos = [cliente.post("/api/perguntar", json={"pergunta": f"pergunta {i}"},
                            headers={"cf-connecting-ip": "1.2.3.4"}).status_code for i in range(6)]
    assert codigos[-1] == 429


def test_resultados_so_na_maquina_local(cliente):
    assert cliente.get("/api/resultados").status_code == 200
    assert cliente.get("/api/resultados", headers={"cf-connecting-ip": "1.2.3.4"}).status_code == 404
    assert cliente.get("/resultados", headers={"x-forwarded-for": "1.2.3.4"}).status_code == 404


def test_cli_compativel(cliente):
    r = cliente.post("/api/v1/questions", json={"question": "O que é DP?"})
    assert r.status_code == 200 and r.json()["source"] == "gemini-rag"
