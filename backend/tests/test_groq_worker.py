"""Groq na cascata e o PC como worker do modelo local."""
import asyncio
import dataclasses
import json

import httpx
from fastapi.testclient import TestClient

from backend.config import Settings
from backend.llm import LLM, PREFERIR_LOCAL, Model, Unavailable


def _settings(**kw):
    base = Settings(gemini_api_key="g", gemini_models=("gemini-x",), groq_api_key="q",
                    groq_models=("openai/gpt-oss-120b",), local_model="tutoron-local")
    return dataclasses.replace(base, **kw)


def test_ordem_da_cascata_local_primeiro_no_gratis():
    llm = LLM(_settings())
    marca = PREFERIR_LOCAL.set(True)
    try:
        assert [m.provider for m in llm.cascade()] == ["ollama", "groq", "gemini"]
    finally:
        PREFERIR_LOCAL.reset(marca)
    assert [m.provider for m in llm.cascade()] == ["groq", "gemini", "ollama"]


def test_pc_desligado_sai_da_cascata_e_volta_ao_registrar():
    llm = LLM(_settings(worker_token="segredo"))
    marca = PREFERIR_LOCAL.set(True)
    try:
        assert [m.provider for m in llm.cascade()] == ["groq", "gemini"]  # sem esperar o prazo do local
        llm.registrar_worker("https://abc.trycloudflare.com/")
        assert llm.ollama_url == "https://abc.trycloudflare.com"
        assert llm.cascade()[0] == Model("ollama", "tutoron-local")
        llm.worker_visto -= 1000  # passou do prazo sem aviso
        assert llm.ollama_url is None
    finally:
        PREFERIR_LOCAL.reset(marca)


def test_groq_le_o_stream_no_formato_openai():
    corpos = []

    def responder(request):
        corpos.append((str(request.url), request.headers["authorization"], json.loads(request.content)))
        linhas = [{"choices": [{"delta": {"role": "assistant"}}]}, {"choices": [{"delta": {"content": "Pense "}}]},
                  {"choices": [{"delta": {"content": "no caso base."}}]}]
        texto = "".join("data: " + json.dumps(x) + "\n\n" for x in linhas) + "data: [DONE]\n\n"
        return httpx.Response(200, text=texto)

    async def rodar():
        async with httpx.AsyncClient(transport=httpx.MockTransport(responder)) as c:
            llm = LLM(_settings(), client=c)
            return "".join([x async for x in llm._groq(Model("groq", "openai/gpt-oss-120b"), "s", "p")])

    assert asyncio.run(rodar()) == "Pense no caso base."
    url, auth, corpo = corpos[0]
    assert url.startswith("https://api.groq.com/openai/v1/") and auth == "Bearer q"
    assert corpo["stream"] and corpo["reasoning_effort"] == "low" and corpo["messages"][0]["role"] == "system"


def test_groq_429_pausa_o_modelo():
    async def rodar():
        transporte = httpx.MockTransport(lambda r: httpx.Response(429, headers={"retry-after": "120"}, text="{}"))
        async with httpx.AsyncClient(transport=transporte) as c:
            llm = LLM(_settings(), client=c)
            try:
                [x async for x in llm._groq(Model("groq", "m"), None, "p")]
            except Unavailable as exc:
                return exc.pause_s

    assert asyncio.run(rodar()) == 120.0


def test_chamadas_ao_pc_levam_a_senha_do_worker():
    vistos = []

    def responder(request):
        vistos.append((str(request.url), request.headers.get("x-tutoron-worker")))
        return httpx.Response(200, text='{"message":{"content":"pista"},"done":true}\n')

    async def rodar():
        async with httpx.AsyncClient(transport=httpx.MockTransport(responder)) as c:
            llm = LLM(_settings(worker_token="segredo", local_thinking=False), client=c)
            llm._thinking["tutoron-local"] = False
            llm.registrar_worker("https://pc.trycloudflare.com")
            return "".join([x async for x in llm._ollama(Model("ollama", "tutoron-local"), "s", "p")])

    assert asyncio.run(rodar()) == "pista"
    assert vistos == [("https://pc.trycloudflare.com/api/chat", "segredo")]


def test_rota_de_registro_exige_o_token(tmp_path):
    from backend import main
    s = _settings(worker_token="segredo", data_dir=tmp_path, gemini_api_key="")
    with TestClient(main.create_app(settings=s, warm_up=False)) as c:
        url = {"url": "https://pc.trycloudflare.com"}
        assert c.post("/api/worker/registrar", json=url).status_code == 403
        assert c.post("/api/worker/registrar", json=url, headers={"Authorization": "Bearer errado"}).status_code == 403
        assert c.post("/api/worker/registrar", json={"url": "http://interno:11434"},
                      headers={"Authorization": "Bearer segredo"}).status_code == 422  # só https
        assert c.post("/api/worker/registrar", json=url, headers={"Authorization": "Bearer segredo"}).json()["ok"]
        assert c.get("/api/status").json()["local"]["pc_conectado"]


def test_proxy_do_pc_recusa_sem_senha_e_rotas_fora_da_lista():
    import importlib.util
    from pathlib import Path
    spec = importlib.util.spec_from_file_location("worker_pc", Path(__file__).resolve().parents[2] / "scripts" / "worker_pc.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    with TestClient(mod.criar_proxy("http://127.0.0.1:1", "segredo")) as c:
        assert c.post("/api/chat", json={}).status_code == 403
        assert c.post("/api/pull", json={}, headers={"x-tutoron-worker": "segredo"}).status_code == 404
        assert c.delete("/api/delete").status_code == 405
