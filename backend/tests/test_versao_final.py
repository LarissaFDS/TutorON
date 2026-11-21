"""Versão final: curso e período, limite diário, planos simulados, modo completo e pré-visualização do link."""
import dataclasses
import datetime as dt

import pytest
from fastapi.testclient import TestClient

from backend import cursos, prompts, tarefas
from backend.cota import PAGOS, Cota
from backend.disciplina_auto import identificar
from backend.llm import LLM, PREFERIR_LOCAL
from backend.tests.test_api import _sleep_curto, esperar
from backend.tests.test_disciplinas import sem_embedding
from backend.tests.test_llm import FakeLLM, settings

ALUNO = {"x-forwarded-for": "200.17.1.10"}  # requisição de fora do PC (não é administrador)


@pytest.fixture
def site(tmp_path, monkeypatch):
    from backend import main
    monkeypatch.setattr(tarefas.asyncio, "sleep", _sleep_curto)
    llm = FakeLLM({"g1": ("ok", "resposta do tutor"), "tutoron-local": ("ok", "resposta local")}, local_model="tutoron-local")
    llm.settings = dataclasses.replace(llm.settings, data_dir=tmp_path, cota_tokens=200, cota_janela_h=24,
                                       url_publica="")
    llm.embed = sem_embedding
    llm.chamadas = []
    original = llm._provider

    def provedor(model, system, prompt):
        llm.chamadas.append((model, system, prompt))
        return original(model, system, prompt)
    llm._provider = provedor
    with TestClient(main.create_app(settings=llm.settings, llm=llm, warm_up=False)) as c:
        c.llm, c.tmp = llm, tmp_path
        yield c


# ------------------------------------------------------------------ cursos e períodos
def test_matrizes_do_ic_sem_eletivas_e_com_os_acervos_certos():
    dados = cursos.publico()
    ecom = next(c for c in dados["cursos"] if c["id"] == "ecom")
    cc = next(c for c in dados["cursos"] if c["id"] == "cc")
    assert len(ecom["periodos"]) == 10 and len(cc["periodos"]) == 8
    nomes = [d["nome"] for c in (ecom, cc) for p in c["periodos"] for d in p["disciplinas"]]
    assert not any("letiva" in n for n in nomes)
    assert cursos.preferidas("ecom", 3) == ("lfa", "fis2", "calc3", "sd")
    assert cursos.preferidas("ecom", 5) == ("paa",) and cursos.preferidas("ecom", 7) == ("bd",)
    assert set(cursos.preferidas("cc", 2)) == {"ed", "bd", "oac"} and set(cursos.preferidas("cc", 4)) == {"paa", "lfa"}
    from acervo import disciplinas
    ids = {d.id for d in disciplinas.todas()}
    assert {d["acervo"] for c in (ecom, cc) for p in c["periodos"] for d in p["disciplinas"] if d["acervo"]} <= ids


def test_perfil_calibra_sem_inventar():
    p = cursos.perfil("ecom", 3, "paa")
    assert "Engenharia de Computação" in p and "3º" in p and "Sistemas Digitais" in p
    assert "5º período" in p  # PAA é do 5º: o aluno está adiantado ou revisando
    assert cursos.perfil(None, None) is None and not cursos.valido("xyz", 1) and not cursos.valido("ecom", 99)


def test_periodo_desempata_e_decide_sem_sinal():
    # "pilha" é sinal de PAA e de ED; no 2º período de EC, ED é a do período.
    assert identificar("Como implemento uma pilha com ponteiros?", preferidas=("ed",)) == "ed"
    # Sem nenhum sinal, o período com uma única disciplina com material decide.
    assert identificar("Não entendi a questão 3 da lista", preferidas=("paa",)) == "paa"
    assert identificar("Não entendi a questão 3 da lista", preferidas=("fis2", "calc3", "sd")) is None
    # Sinal claro de outra disciplina continua valendo.
    assert identificar("Como agrupar no Karnaugh?", preferidas=("paa",)) == "sd"


def test_api_cursos_e_perfil_chegam_ao_prompt(site):
    assert site.get("/api/cursos").json()["padrao"] == "ecom"
    t = esperar(site, site.post("/api/perguntar", json={
        "pergunta": "Não entendi a questão 3 da lista", "disciplina": "auto", "curso": "ecom", "periodo": 5}).json())
    assert t["status"] == "pronta" and t["disciplina"] == "paa"
    prompt = site.llm.chamadas[0][2]
    assert "PERFIL ACADÊMICO DO ALUNO" in prompt and "5º" in prompt and "Projeto e Análise de Algoritmos" in prompt
    # Curso inválido é ignorado (não quebra a pergunta).
    t = esperar(site, site.post("/api/perguntar", json={"pergunta": "Teorema Mestre", "curso": "xyz", "periodo": 2}).json())
    assert t["status"] == "pronta"


# ------------------------------------------------------------------ limite diário e planos
def test_cota_diaria_renova_a_meia_noite(tmp_path):
    c = Cota(tmp_path / "c.json", limite=100, janela_h=24)
    c.cobrar("a", 150)
    s = c.situacao("a")
    assert not c.pode("a") and s["diaria"]
    amanha = (dt.datetime.now() + dt.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    assert s["renova_em"] == amanha.timestamp()
    c._uso["a"]["inicio"] -= 86400  # o uso foi ontem
    assert c.pode("a")


def test_plano_simulado_aumenta_o_limite_e_liga_o_modo_completo(tmp_path):
    c = Cota(tmp_path / "c.json", limite=100, janela_h=24)
    assert c.modo("a") == "padrao" and c.modo("a", dev=True) == "completo"
    c.cobrar("a", 150)
    assert not c.pode("a")
    c.ativar_plano("a", "estudante", "4242")
    assert c.pode("a") and c.modo("a") == "completo" and c.situacao("a")["limite"] == PAGOS["estudante"]["tokens_dia"]
    assert Cota(tmp_path / "c.json", 100, 24).plano("a")["id"] == "estudante"  # persiste
    with pytest.raises(ValueError):
        c.ativar_plano("a", "gratis")
    c.cancelar_plano("a")
    assert not c.pode("a") and c.modo("a") == "padrao"


def test_limite_esgotado_responde_402_e_plano_libera(site):
    site.cookies.set("tutoron_id", "c_teste")
    r = site.post("/api/perguntar", json={"pergunta": "x" * 1200}, headers=ALUNO)
    assert r.status_code == 200
    r = site.post("/api/perguntar", json={"pergunta": "Teorema Mestre de novo"}, headers=ALUNO)
    assert r.status_code == 402 and "renova amanhã à meia-noite" in r.json()["erro"] and "planos" in r.json()["erro"]
    assert site.post("/api/planos/ativar", json={"plano": "intensivo", "final_cartao": "4242"}, headers=ALUNO).json()["plano"] == "intensivo"
    assert site.post("/api/perguntar", json={"pergunta": "Teorema Mestre de novo"}, headers=ALUNO).status_code == 200
    # O número completo do cartão nunca é aceito pelo servidor.
    assert site.post("/api/planos/ativar", json={"plano": "estudante", "final_cartao": "4242424242424242"},
                     headers=ALUNO).status_code == 422
    assert site.post("/api/planos/ativar", json={"plano": "gratis"}, headers=ALUNO).status_code == 422


def test_administrador_nao_tem_limite(site):
    for _ in range(3):
        assert site.post("/api/perguntar", json={"pergunta": "x" * 1200}).status_code == 200
    c = site.get("/api/cota").json()
    assert c["admin"] and c["ilimitado"] and c["modo"] == "completo"


def test_gratis_usa_modelo_local_primeiro_e_pago_o_gemini():
    llm = LLM(settings())
    assert llm.cascade()[0].provider == "gemini"
    marca = PREFERIR_LOCAL.set(True)
    try:
        assert [m.provider for m in llm.cascade()] == ["ollama", "gemini", "gemini", "gemini"]
    finally:
        PREFERIR_LOCAL.reset(marca)


def test_pergunta_do_gratis_registra_o_modo(site):
    site.cookies.set("tutoron_id", "c_modo")
    t = esperar(site, site.post("/api/perguntar", json={"pergunta": "Teorema Mestre"}, headers=ALUNO).json())
    assert t["status"] == "pronta"
    import json
    linha = json.loads((site.tmp / "perguntas.jsonl").read_text(encoding="utf-8").splitlines()[-1])
    assert linha["modo_ia"] == "padrao" and linha["provedor"] == "ollama"


# ------------------------------------------------------------------ página, marca e link
def test_pagina_tem_pre_visualizacao_com_endereco_absoluto(site):
    html = site.get("/", headers={"host": "tutoron.exemplo.ts.net", "x-forwarded-proto": "https"}).text
    assert '<meta property="og:image" content="https://tutoron.exemplo.ts.net/static/marca/previa.png">' in html
    assert 'og:description' in html and 'twitter:card' in html and "{{BASE}}" not in html
    malicioso = site.get("/", headers={"host": 'x"><script>alert(1)</script>'}).text
    assert "<script>alert(1)" not in malicioso
    for arquivo in ("logo.svg", "previa.png", "icone-192.png", "icone-512.png", "apple-touch-icon.png", "favicon-32.png"):
        assert site.get(f"/static/marca/{arquivo}").status_code == 200
    m = site.get("/manifest.webmanifest").json()
    assert m["name"] == "TutorON" and m["icons"]
    assert site.get("/planos", follow_redirects=False).headers["location"] == "/#planos"


def test_url_publica_configurada_vence_o_host(site):
    from backend import main
    s = dataclasses.replace(site.llm.settings, url_publica="https://tutoron.com.br")
    with TestClient(main.create_app(settings=s, llm=site.llm, warm_up=False)) as c:
        assert 'content="https://tutoron.com.br/static/marca/previa.png"' in c.get("/").text


CONTROLE = ("Tenho uma planta G(s) = 1/(s(s+4)) com controlador proporcional K em malha fechada. "
            "Qual a faixa de K para a resposta ao degrau não ter overshoot?")


def test_disciplina_sem_acervo_e_orientada_com_conhecimento_geral(site):
    t = esperar(site, site.post("/api/perguntar", json={"pergunta": CONTROLE, "disciplina": "auto",
                                                        "curso": "ecom", "periodo": 6}).json())
    assert t["status"] == "pronta" and t["disciplina"] == "geral" and t["fontes"] == []
    sistema = site.llm.chamadas[0][1]
    assert "Disciplina sem material no TutorON" in sistema and "Não entregue o resultado final" in sistema
    # "Ainda não consegui" devolve a disciplina "geral" e continua funcionando.
    t2 = esperar(site, site.post("/api/perguntar", json={
        "pergunta": CONTROLE, "disciplina": "geral", "travou": "não sei achar o zeta",
        "historico": [{"ajuda": "pista", "texto": t["texto"]}]}).json())
    assert t2["status"] == "pronta" and t2["disciplina"] == "geral"
    # Sinal claro de uma disciplina com acervo continua indo para ela.
    t3 = esperar(site, site.post("/api/perguntar", json={"pergunta": "Como agrupar no Karnaugh?",
                                                         "disciplina": "auto"}).json())
    assert t3["disciplina"] == "sd"


def test_prompt_socratico_das_novas_disciplinas_traz_o_rigor_do_cadastro():
    from acervo import disciplinas
    for ident in ("oac", "calc3", "fis2", "ed", "bd"):
        d = disciplinas.obter(ident)
        assert d.rigor.strip()[:60] in prompts.sistema_socratico(d)
        assert "não autorizam entregar a resolução" in prompts.sistema_socratico(d)

