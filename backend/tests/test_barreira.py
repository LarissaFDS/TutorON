"""Disciplina "em validação" fica fora do atendimento normal, decidido no servidor.

Sem TUTORON_LIBERAR_EM_VALIDACAO, SD (situação "em validação" no cadastro) é recusada com 403 em
/api/perguntar, /api/comparar e /api/v1/questions, mesmo chamando a API direto, sem o site.
"""
import json

import pytest
from fastapi.testclient import TestClient

from acervo import disciplinas
from backend.config import load_settings
from backend.tests.test_api import _sleep_curto, esperar
from backend.tests.test_disciplinas import sem_embedding
from backend.tests.test_llm import FakeLLM
from backend import tarefas

ROTAS = [("/api/perguntar", {"pergunta": "O que é um latch SR?", "disciplina": "sd"}),
         ("/api/comparar", {"pergunta": "O que é um latch SR?", "disciplina": "sd"}),
         ("/api/v1/questions", {"question": "O que é um latch SR?", "subject": "sd"})]


def cliente(tmp_path, monkeypatch, liberadas=()):
    from backend import main
    monkeypatch.setattr(tarefas.asyncio, "sleep", _sleep_curto)
    llm = FakeLLM({"g1": ("ok", "resposta do tutor")})
    llm.settings = llm.settings.__class__(**{**llm.settings.__dict__, "data_dir": tmp_path,
                                             "disciplinas_em_validacao_liberadas": tuple(liberadas)})
    llm.embed = sem_embedding
    llm.chamadas = []
    original = llm._provider
    llm._provider = lambda m, s, p: llm.chamadas.append(m) or original(m, s, p)
    c = TestClient(main.create_app(settings=llm.settings, llm=llm, warm_up=False))
    c.llm = llm
    return c


@pytest.fixture
def producao(tmp_path, monkeypatch):
    with cliente(tmp_path, monkeypatch) as c:
        yield c


@pytest.fixture
def validacao(tmp_path, monkeypatch):
    with cliente(tmp_path, monkeypatch, liberadas=("sd",)) as c:
        yield c


def test_cadastro_marca_sd_em_validacao_e_paa_nao():
    assert disciplinas.obter("sd").em_validacao and not disciplinas.obter("paa").em_validacao


def test_padrao_e_desligado(monkeypatch):
    monkeypatch.delenv("TUTORON_LIBERAR_EM_VALIDACAO", raising=False)
    assert load_settings().disciplinas_em_validacao_liberadas == ()
    monkeypatch.setenv("TUTORON_LIBERAR_EM_VALIDACAO", " SD , calc ")
    assert load_settings().disciplinas_em_validacao_liberadas == ("sd", "calc")


@pytest.mark.parametrize("rota, corpo", ROTAS)
def test_sd_recusada_em_todas_as_rotas_sem_liberacao(producao, rota, corpo):
    r = producao.post(rota, json=corpo)  # chamada direta à API: o site não participa
    assert r.status_code == 403 and "em validação" in r.json()["erro"]
    assert producao.llm.chamadas == []  # nem busca nem IA


@pytest.mark.parametrize("corpo", [{"pergunta": "Teorema Mestre para T(n) = 2T(n/2) + n"},
                                   {"pergunta": "Teorema Mestre para T(n) = 2T(n/2) + n", "disciplina": "paa"}])
def test_paa_continua_disponivel(producao, corpo):
    t = esperar(producao, producao.post("/api/perguntar", json=corpo).json())
    assert t["status"] == "pronta"
    par = esperar(producao, producao.post("/api/comparar", json=corpo).json())
    assert par["status"] == "pronta"
    r = producao.post("/api/v1/questions", json={"question": corpo["pergunta"], "subject": "paa"})
    assert r.status_code == 200


@pytest.mark.parametrize("rota, corpo", ROTAS)
def test_sd_funciona_com_liberacao_explicita(validacao, rota, corpo):
    r = validacao.post(rota, json=corpo)
    assert r.status_code == 200
    if rota != "/api/v1/questions":
        assert esperar(validacao, r.json())["status"] == "pronta"
    assert validacao.llm.chamadas  # a mesma IA compartilhada


def test_liberacao_todas_vale_para_qualquer_disciplina(tmp_path, monkeypatch):
    with cliente(tmp_path, monkeypatch, liberadas=("todas",)) as c:
        assert c.post(ROTAS[0][0], json=ROTAS[0][1]).status_code == 200


def test_liberar_outra_disciplina_nao_libera_sd(tmp_path, monkeypatch):
    with cliente(tmp_path, monkeypatch, liberadas=("calc",)) as c:
        assert c.post(ROTAS[0][0], json=ROTAS[0][1]).status_code == 403


@pytest.mark.parametrize("rota, corpo", [("/api/perguntar", {"pergunta": "O que é um latch?", "disciplina": "quimica"}),
                                         ("/api/comparar", {"pergunta": "O que é um latch?", "disciplina": "quimica"}),
                                         ("/api/v1/questions", {"question": "O que é um latch?", "subject": "quimica"})])
def test_disciplina_desconhecida_continua_422(producao, rota, corpo):
    assert producao.post(rota, json=corpo).status_code == 422


def test_lista_informa_disponibilidade(producao, validacao):
    lista = {d["id"]: d for d in producao.get("/api/disciplinas").json()["disciplinas"]}
    assert lista["paa"]["disponivel"] and not lista["sd"]["disponivel"] and lista["sd"]["em_validacao"]
    lista = {d["id"]: d for d in validacao.get("/api/disciplinas").json()["disciplinas"]}
    assert lista["sd"]["disponivel"]


def test_disciplina_futura_em_validacao_e_barrada_sem_codigo_novo(tmp_path, monkeypatch):
    """A regra vem só do cadastro: uma disciplina nova "em validação" é barrada do mesmo jeito."""
    registro = tmp_path / "disciplinas.json"
    base = json.loads(disciplinas.REGISTRO.read_text(encoding="utf-8"))
    raiz = disciplinas.REGISTRO.parent.parent
    for d in base["disciplinas"]:  # o cadastro temporário mora em tmp_path: caminhos absolutos
        for campo in ("itens", "indice", "materiais", "rigor"):
            if d.get(campo):
                d[campo] = str(raiz / d[campo])
    paa = next(d for d in base["disciplinas"] if d["id"] == "paa")
    base["disciplinas"].append({**paa, "id": "calc", "nome": "Cálculo 1", "sigla": "CALC", "livro_supabase": False,
                                "situacao": "Em validação"})
    registro.write_text(json.dumps(base), encoding="utf-8")
    original = disciplinas.obter
    monkeypatch.setattr(disciplinas, "obter", lambda ident=None, registro_=registro: original(ident, registro=registro_))
    monkeypatch.setattr(tarefas, "obter", disciplinas.obter)  # tarefas importou obter por nome
    monkeypatch.setattr(disciplinas, "todas", lambda: [original(d["id"], registro=registro) for d in base["disciplinas"]])
    with cliente(tmp_path, monkeypatch) as c:
        r = c.post("/api/perguntar", json={"pergunta": "Regra da cadeia?", "disciplina": "calc"})
        assert r.status_code == 403 and "Cálculo 1" in r.json()["erro"]
    with cliente(tmp_path, monkeypatch, liberadas=("calc",)) as c:
        assert c.post("/api/perguntar", json={"pergunta": "Regra da cadeia?", "disciplina": "calc"}).status_code == 200
