"""Contas (Supabase Auth), cota por conta e gravação no banco, com um banco falso em memória."""
import dataclasses

import pytest
from fastapi.testclient import TestClient

from backend import tarefas
from backend.contas import Contas
from backend.cota import Cota
from backend.dados import USUARIO, Registro
from backend.tests.test_api import _sleep_curto
from backend.tests.test_disciplinas import sem_embedding
from backend.tests.test_llm import FakeLLM

ALUNO = {"x-forwarded-for": "200.17.1.10"}


class BancoFalso:
    """Mesma interface de backend.banco.Banco, guardando tudo em listas."""

    def __init__(self):
        self.tabelas: dict[str, list[dict]] = {}
        self.tokens = {"tok-ana": {"id": "11111111-1111-1111-1111-111111111111", "email": "Ana@Exemplo.com",
                                   "user_metadata": {"full_name": "Ana"}},
                       "tok-adm": {"id": "22222222-2222-2222-2222-222222222222", "email": "prof@exemplo.com"}}
        self.consultas_auth = 0

    def inserir(self, tabela, linha, upsert=None):
        linhas = linha if isinstance(linha, list) else [linha]
        dest = self.tabelas.setdefault(tabela, [])
        for nova in linhas:
            if upsert:
                chave = upsert.split(",")
                velha = next((r for r in dest if all(r.get(k) == nova.get(k) for k in chave)), None)
                if velha is not None:
                    velha.update(nova)
                    continue
            dest.append(dict(nova))

    inserir_agora = inserir

    def esperar(self, timeout=0):
        pass

    def _filtra(self, tabela, params):
        linhas = self.tabelas.get(tabela, [])
        for k, v in (params or {}).items():
            if k in ("select", "order"):
                continue
            linhas = [r for r in linhas if str(r.get(k)) == v.removeprefix("eq.")]
        return linhas

    def selecionar(self, tabela, params=None):
        if tabela == "uso_por_usuario":
            por = {}
            for u in self.tabelas.get("uso_tokens", []):
                r = por.setdefault(u["quem"], {"quem": u["quem"], "tokens": 0, "perguntas": 0, "ultimo": u["data"]})
                r["tokens"] += u["tokens"]
                r["perguntas"] += u["tipo"] == "pergunta"
            return list(por.values())
        return [dict(r) for r in self._filtra(tabela, params)]

    def atualizar(self, tabela, filtro, dados):
        for r in self._filtra(tabela, filtro):
            r.update(dados)

    def apagar(self, tabela, filtro):
        alvo = self._filtra(tabela, filtro)
        self.tabelas[tabela] = [r for r in self.tabelas.get(tabela, []) if r not in alvo]

    def usuario_do_token(self, token, chave_publica):
        self.consultas_auth += 1
        return self.tokens.get(token)


@pytest.fixture
def site(tmp_path, monkeypatch):
    from backend import banco as banco_mod
    from backend import main
    falso = BancoFalso()
    monkeypatch.setattr(banco_mod, "criar", lambda settings: falso)
    monkeypatch.setattr(tarefas.asyncio, "sleep", _sleep_curto)
    llm = FakeLLM({"g1": ("ok", "resposta do tutor"), "tutoron-local": ("ok", "resposta local")}, local_model="tutoron-local")
    llm.settings = dataclasses.replace(llm.settings, data_dir=tmp_path, cota_tokens=500, cota_janela_h=24,
                                       url_publica="", supabase_url="https://x.supabase.co",
                                       supabase_anon_key="anon", exigir_login=True, admins=("prof@exemplo.com",))
    llm.embed = sem_embedding
    with TestClient(main.create_app(settings=llm.settings, llm=llm, warm_up=False)) as c:
        c.banco = falso
        yield c


def test_config_publica_nao_vaza_chave_de_servico(site):
    cfg = site.get("/api/config").json()
    assert cfg == {"contas": True, "exigir_login": True, "supabase_url": "https://x.supabase.co",
                   "supabase_anon_key": "anon"}


def test_sem_login_pede_conta_e_com_login_responde(site):
    r = site.post("/api/perguntar", json={"pergunta": "Teorema Mestre"}, headers=ALUNO)
    assert r.status_code == 401 and "Entre com sua conta" in r.json()["erro"]
    site.cookies.set("tutoron_sessao", "tok-ana")
    r = site.post("/api/perguntar", json={"pergunta": "Teorema Mestre"}, headers=ALUNO)
    assert r.status_code == 200
    eu = site.get("/api/eu", headers=ALUNO).json()
    assert eu["logado"] and eu["conta"]["nome"] == "Ana" and eu["conta"]["email"] == "ana@exemplo.com"
    assert not eu["admin"] and eu["cota"]["usados"] > 0
    # Perfil criado, uso gravado por conta, e o token conferido no Supabase só uma vez (cache).
    assert site.banco.tabelas["perfis"][0]["id"].startswith("1111")
    assert {u["quem"] for u in site.banco.tabelas["uso_tokens"]} == {"u:11111111-1111-1111-1111-111111111111"}
    assert site.banco.consultas_auth == 1


def test_token_invalido_e_convidado(site):
    site.cookies.set("tutoron_sessao", "falsificado")
    assert site.post("/api/perguntar", json={"pergunta": "Teorema Mestre"}, headers=ALUNO).status_code == 401


def test_admin_define_limite_por_conta_e_zera(site):
    site.cookies.set("tutoron_sessao", "tok-ana")
    assert site.get("/api/admin/usuarios", headers=ALUNO).status_code == 403
    site.post("/api/perguntar", json={"pergunta": "Teorema Mestre"}, headers=ALUNO)  # cria o perfil
    site.cookies.set("tutoron_sessao", "tok-adm")
    ana = "u:11111111-1111-1111-1111-111111111111"
    r = site.post(f"/api/admin/usuarios/{ana}/limite", json={"limite": 1}, headers=ALUNO).json()
    assert r.get("limite") == 1, r
    assert site.banco.tabelas["perfis"][0]["limite_tokens"] == 1
    lista = site.get("/api/admin/usuarios", headers=ALUNO).json()["usuarios"]
    assert any(u["quem"] == ana and u["limite_proprio"] == 1 and u["email"] == "ana@exemplo.com" for u in lista)
    site.cookies.set("tutoron_sessao", "tok-ana")
    assert site.post("/api/perguntar", json={"pergunta": "Teorema Mestre"}, headers=ALUNO).status_code == 402
    site.cookies.set("tutoron_sessao", "tok-adm")
    assert site.post(f"/api/admin/usuarios/{ana}/zerar", headers=ALUNO).json()["usados"] == 0
    assert site.post(f"/api/admin/usuarios/{ana}/limite", json={"limite": None}, headers=ALUNO).json()["limite"] == 500


def test_cota_le_uso_do_dia_do_banco(tmp_path):
    banco = BancoFalso()
    Cota(tmp_path / "a.json", 100, 24, banco=banco).cobrar("u:x", 70)
    # Outro servidor (ou um reinício sem os arquivos, como na hospedagem) enxerga o mesmo uso.
    outra = Cota(tmp_path / "outro" / "b.json", 100, 24, banco=banco)
    assert outra.situacao("u:x")["usados"] == 70


def test_registro_grava_no_banco_com_a_conta(tmp_path):
    banco = BancoFalso()
    reg = Registro(tmp_path, banco)
    marca = USUARIO.set("u:abc")
    try:
        reg.anexar("perguntas.jsonl", {"id": "p1", "pergunta": "oi"})
        reg.anexar("outro.jsonl", {"id": "x"})  # arquivo sem tabela: só local
    finally:
        USUARIO.reset(marca)
    assert banco.tabelas == {"perguntas": [{"id": "p1", "usuario": "u:abc", "dados": {"id": "p1", "pergunta": "oi"}}]}


def test_contas_desligadas_sem_supabase():
    c = Contas(None, "")
    assert not c.ativas and c.usuario("qualquer") is None


def test_convidado_tem_limite_menor_e_e_levado_a_criar_conta(site, monkeypatch):
    import dataclasses
    from backend import main
    s = dataclasses.replace(site.app.state.llm.settings, exigir_login=False, cota_convidado=5)
    from backend import banco as banco_mod
    monkeypatch.setattr(banco_mod, "criar", lambda settings: site.banco)
    with TestClient(main.create_app(settings=s, llm=site.app.state.llm, warm_up=False)) as c:
        c.cookies.set("tutoron_id", "c_visitante")
        eu = c.get("/api/eu", headers=ALUNO).json()
        assert eu["cota"]["convidado"] and eu["cota"]["limite"] == 5 and eu["cota"]["limite_conta"] == 500
        assert c.post("/api/perguntar", json={"pergunta": "x" * 100}, headers=ALUNO).status_code == 200
        r = c.post("/api/perguntar", json={"pergunta": "Teorema Mestre"}, headers=ALUNO)
        assert r.status_code == 401 and "Crie uma conta" in r.json()["erro"]
        c.cookies.set("tutoron_sessao", "tok-ana")  # com conta: limite normal
        assert c.get("/api/eu", headers=ALUNO).json()["cota"]["limite"] == 500
