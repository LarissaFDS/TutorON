"""Disciplina "em validação" fica fora do atendimento normal, decidido no servidor.

SD saiu da validação para "beta" (21/10/2026) e é atendida sem nenhuma liberação. A barreira continua
valendo para qualquer disciplina cadastrada como "em validação": aqui, uma disciplina fictícia (CALC)
recebe 403 em /api/perguntar, /api/comparar e /api/v1/questions, mesmo chamando a API direto.
"""
import json

import pytest
from fastapi.testclient import TestClient

from acervo import disciplinas
from backend import tarefas
from backend.config import load_settings
from backend.tests.test_api import _sleep_curto, esperar
from backend.tests.test_disciplinas import sem_embedding
from backend.tests.test_llm import FakeLLM


def rotas(d, pergunta="O que é um latch SR?"):
    return [("/api/perguntar", {"pergunta": pergunta, "disciplina": d}),
            ("/api/comparar", {"pergunta": pergunta, "disciplina": d}),
            ("/api/v1/questions", {"question": pergunta, "subject": d})]


@pytest.fixture
def com_calc(tmp_path, monkeypatch):
    """Cadastro real (PAA e SD) + CALC "Em validação". A regra vem só do cadastro, sem código novo."""
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


def cliente(tmp_path, monkeypatch, liberadas=()):
    from backend import main
    monkeypatch.setattr(tarefas.asyncio, "sleep", _sleep_curto)
    llm = FakeLLM({"g1": ("ok", "resposta do tutor")})
    llm.settings = llm.settings.__class__(**{**llm.settings.__dict__, "data_dir": tmp_path,
                                             "disciplinas_em_validacao_liberadas": tuple(liberadas)})
    llm.embed = sem_embedding
    llm.chamadas = []
    original = llm._provider
    llm._provider = lambda m, s, p: llm.chamadas.append((m, s)) or original(m, s, p)
    c = TestClient(main.create_app(settings=llm.settings, llm=llm, warm_up=False))
    c.llm = llm
    return c


@pytest.fixture
def producao(tmp_path, monkeypatch, com_calc):
    with cliente(tmp_path, monkeypatch) as c:
        yield c


def test_situacao_no_cadastro(com_calc):
    assert disciplinas.obter("sd").situacao == "beta" and not disciplinas.obter("sd").em_validacao
    assert not disciplinas.obter("paa").em_validacao and disciplinas.obter("calc").em_validacao


def test_padrao_e_desligado(monkeypatch):
    monkeypatch.delenv("TUTORON_LIBERAR_EM_VALIDACAO", raising=False)
    assert load_settings().disciplinas_em_validacao_liberadas == ()
    monkeypatch.setenv("TUTORON_LIBERAR_EM_VALIDACAO", " CALC , fis ")
    assert load_settings().disciplinas_em_validacao_liberadas == ("calc", "fis")


@pytest.mark.parametrize("rota, corpo", rotas("sd"))
def test_sd_atendida_sem_liberacao(producao, rota, corpo):
    r = producao.post(rota, json=corpo)
    assert r.status_code == 200
    if rota != "/api/v1/questions":
        assert esperar(producao, r.json())["status"] == "pronta"
    else:
        assert r.json()["metadata"]["subject"] == "sd"
    sistemas = [s for _, s in producao.llm.chamadas if s]  # o genérico da A/B não tem instruções
    assert sistemas and all("Sistemas Digitais (SD)" in s for s in sistemas)  # chegou à IA compartilhada


@pytest.mark.parametrize("rota, corpo", rotas("calc", "Regra da cadeia?"))
def test_disciplina_em_validacao_recusada_em_todas_as_rotas(producao, rota, corpo):
    r = producao.post(rota, json=corpo)  # chamada direta à API: o site não participa
    assert r.status_code == 403 and "Cálculo 1" in r.json()["erro"] and "em validação" in r.json()["erro"]
    assert producao.llm.chamadas == []  # nem busca nem IA


@pytest.mark.parametrize("corpo", [{"pergunta": "Teorema Mestre para T(n) = 2T(n/2) + n"},
                                   {"pergunta": "Teorema Mestre para T(n) = 2T(n/2) + n", "disciplina": "paa"}])
def test_paa_continua_disponivel(producao, corpo):
    assert esperar(producao, producao.post("/api/perguntar", json=corpo).json())["status"] == "pronta"
    assert esperar(producao, producao.post("/api/comparar", json=corpo).json())["status"] == "pronta"
    r = producao.post("/api/v1/questions", json={"question": corpo["pergunta"], "subject": "paa"})
    assert r.status_code == 200


@pytest.mark.parametrize("liberadas", [("calc",), ("todas",)])
def test_liberacao_explicita_vale_para_disciplina_em_validacao(tmp_path, monkeypatch, com_calc, liberadas):
    with cliente(tmp_path, monkeypatch, liberadas=liberadas) as c:
        for rota, corpo in rotas("calc", "Regra da cadeia?"):
            assert c.post(rota, json=corpo).status_code == 200


def test_liberar_outra_disciplina_nao_libera_calc(tmp_path, monkeypatch, com_calc):
    with cliente(tmp_path, monkeypatch, liberadas=("fis",)) as c:
        assert c.post("/api/perguntar", json={"pergunta": "Regra da cadeia?", "disciplina": "calc"}).status_code == 403


@pytest.mark.parametrize("rota, corpo", rotas("quimica"))
def test_disciplina_desconhecida_continua_422(producao, rota, corpo):
    assert producao.post(rota, json=corpo).status_code == 422


def test_lista_informa_disponibilidade_e_aviso_beta(producao):
    lista = {d["id"]: d for d in producao.get("/api/disciplinas").json()["disciplinas"]}
    assert lista["paa"]["disponivel"] and lista["sd"]["disponivel"] and not lista["calc"]["disponivel"]
    assert lista["sd"]["situacao"] == "beta" and not lista["sd"]["em_validacao"]
    assert lista["sd"]["aviso"].startswith("Sistemas Digitais — versão beta.")
    assert "podem conter erros" in lista["sd"]["aviso"] and lista["paa"]["aviso"] == ""


def test_site_mostra_e_troca_o_aviso_beta():
    """O site usa o aviso do cadastro ao escolher a disciplina (também via ?disciplina=sd, que passa pela
    mesma função) e o esconde quando a disciplina não tem aviso. Conferência estática do JS e do HTML."""
    from backend.main import WEB
    js = (WEB / "app.js").read_text(encoding="utf-8")
    html = (WEB / "index.html").read_text(encoding="utf-8")
    corpo = js[js.index("function escolherDisciplina"):js.index("(async function carregarDisciplinas")]
    assert "beta.textContent = d.aviso || ''" in corpo and "beta.hidden = !d.aviso" in corpo
    assert "escolherDisciplina(disciplinas[pedida] ? pedida : dados.padrao)" in js
    assert "escolherDisciplina($('disciplina').value)" in js
    nota = html.split("masthead__nota")[1].split("</p>")[0]
    assert 'id="disciplina-beta"' in html and "em validação" not in nota and "beta" in nota
