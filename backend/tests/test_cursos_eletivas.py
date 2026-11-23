"""Grade de períodos: nenhuma disciplina disponível fica fora da janela "Em que ponto do curso você está?"."""
from __future__ import annotations

import json
from pathlib import Path

from fastapi.testclient import TestClient

from backend import cursos, main
from backend.config import Settings

CADASTRO = Path(__file__).resolve().parents[2] / "disciplinas" / "disciplinas.json"


def _disponiveis() -> list[str]:
    dados = json.loads(CADASTRO.read_text(encoding="utf-8"))
    return [d["id"] for d in dados["disciplinas"] if d.get("situacao") != "em validação"]


def _visiveis(c: dict) -> list[str]:
    na_grade = [x["acervo"] for p in c["periodos"] for x in p["disciplinas"] if x.get("acervo")]
    return na_grade + [x["acervo"] for x in c["eletivas"]["disciplinas"]]


def test_api_cursos_mostra_toda_disciplina_disponivel_em_cada_curso(tmp_path):
    settings = Settings(groq_api_key="", gemini_api_key="", data_dir=tmp_path)
    with TestClient(main.create_app(settings=settings, warm_up=False)) as site:
        dados = site.get("/api/cursos").json()
    assert dados["cursos"]
    for c in dados["cursos"]:
        faltam = [i for i in _disponiveis() if i not in _visiveis(c)]
        assert not faltam, f"{c['id']}: disciplinas fora da janela de períodos: {faltam}"
        assert c["eletivas"]["nome"] == "Eletivas, ênfases e outras"
        # Grupo de eletivas não repete o que já está num período.
        na_grade = {x["acervo"] for p in c["periodos"] for x in p["disciplinas"]}
        assert not na_grade & {x["acervo"] for x in c["eletivas"]["disciplinas"]}


def _base():
    dados = {"cursos": [{"id": "cc", "nome": "CC", "instituicao": "IC", "periodos": [
        {"numero": 1, "disciplinas": [{"nome": "Programação 1"}]},
        {"numero": 6, "disciplinas": [{"nome": "Compiladores"}]}]}]}
    cadastro = {"disciplinas": [
        {"id": "prog1", "nome": "Programação 1", "situacao": "MVP"},
        {"id": "seg", "nome": "Segurança", "situacao": "MVP", "cursos": {"cc": 6}},
        {"id": "pln", "nome": "PLN", "situacao": "MVP", "cursos": {"cc": "eletiva"}},
        {"id": "solta", "nome": "Sem campo", "situacao": "MVP"},
        {"id": "rob", "nome": "Robótica", "situacao": "em validação", "cursos": {"cc": 1}}]}
    return cursos._ligar_acervos(dados, cadastro)["cursos"][0]


def test_campo_cursos_poe_no_periodo_e_em_preferidas(monkeypatch):
    c = _base()
    p6 = c["periodos"][1]["disciplinas"]
    assert [x.get("acervo") for x in p6] == [None, "seg"]
    assert [x["acervo"] for x in c["eletivas"]] == ["pln", "solta"]
    monkeypatch.setattr(cursos, "_dados", lambda: {"cursos": [c]})
    assert cursos.preferidas("cc", 6) == ("seg",)
    # A disciplina extra não vira "obrigatória" no perfil mandado à IA.
    assert "Segurança" not in cursos.perfil("cc", 6).split("Use isso")[0].replace("Curso:", "")


def test_em_validacao_nao_aparece():
    c = _base()
    tudo = [x.get("acervo") for p in c["periodos"] for x in p["disciplinas"]] + [x["acervo"] for x in c["eletivas"]]
    assert "rob" not in tudo
    real = cursos.publico()
    em_val = {d["id"] for d in json.loads(CADASTRO.read_text(encoding="utf-8"))["disciplinas"]
              if d.get("situacao") == "em validação"}
    for cc in real["cursos"]:
        assert not em_val & {x["acervo"] for x in cc["eletivas"]["disciplinas"]}
