"""Liga o modelo local do PC ao TutorON hospedado (o PC vira "worker").

Fluxo: servidor hospedado  --HTTPS-->  túnel Cloudflare  -->  este proxy (com senha)  -->  Ollama do PC

1. Sobe um proxy em 127.0.0.1:11435 que só aceita pedidos com o cabeçalho `x-tutoron-worker`
   igual a TUTORON_WORKER_TOKEN (o Ollama em si continua fechado na máquina).
2. Abre um túnel rápido da Cloudflare (.tools/cloudflared.exe) para esse proxy.
3. A cada minuto avisa o servidor (POST /api/worker/registrar) o endereço do túnel. Se o PC desligar,
   em 2,5 min o servidor tira o modelo local da cascata e responde com Groq/Gemini.

Uso (no PC, com o Ollama ligado):  python scripts/worker_pc.py   (ou 7-Ligar-IA-Local.bat)
Precisa no .env: TUTORON_SERVIDOR_URL=https://<seu-app>  e  TUTORON_WORKER_TOKEN=<o mesmo do servidor>.
"""
from __future__ import annotations

import asyncio
import os
import re
import secrets
import subprocess
import sys
import threading
import time
from pathlib import Path

import httpx
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
from backend.config import load_settings  # noqa: E402  (carrega o .env)

PORTA = 11435
ROTAS = {"/api/chat", "/api/show", "/api/embed", "/api/tags", "/api/ps", "/api/generate"}


def criar_proxy(ollama: str, token: str) -> FastAPI:
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
    cliente = httpx.AsyncClient(timeout=httpx.Timeout(300, connect=5))

    @app.api_route("/{caminho:path}", methods=["GET", "POST"])
    async def repassar(caminho: str, request: Request):
        recebido = request.headers.get("x-tutoron-worker", "")
        if not (recebido and secrets.compare_digest(recebido, token)):
            return JSONResponse({"error": "não autorizado"}, status_code=403)
        if "/" + caminho not in ROTAS:
            return JSONResponse({"error": "rota não permitida"}, status_code=404)
        pedido = cliente.build_request(request.method, ollama + "/" + caminho, content=await request.body(),
                                       headers={"content-type": request.headers.get("content-type", "application/json")})
        resposta = await cliente.send(pedido, stream=True)

        async def corpo():
            try:
                async for parte in resposta.aiter_raw():
                    yield parte
            finally:
                await resposta.aclose()
        return StreamingResponse(corpo(), status_code=resposta.status_code,
                                 media_type=resposta.headers.get("content-type"))
    return app


def abrir_tunel() -> tuple[subprocess.Popen, str]:
    exe = RAIZ / ".tools" / "cloudflared.exe"
    if not exe.exists():
        sys.exit("Falta .tools/cloudflared.exe (o 1-Iniciar-Servidor.bat baixa na primeira vez).")
    proc = subprocess.Popen([str(exe), "tunnel", "--no-autoupdate", "--url", f"http://127.0.0.1:{PORTA}"],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8",
                            errors="replace")
    fim = time.monotonic() + 60
    while time.monotonic() < fim:
        linha = proc.stdout.readline()
        m = re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", linha or "")
        if m:
            threading.Thread(target=lambda: [None for _ in proc.stdout], daemon=True).start()  # esvazia o log
            return proc, m.group(0)
    proc.kill()
    sys.exit("O túnel da Cloudflare não abriu em 60 s. Verifique a internet e tente de novo.")


async def avisar(servidor: str, token: str, url: str) -> None:
    async with httpx.AsyncClient(timeout=15) as c:
        while True:
            try:
                r = await c.post(servidor + "/api/worker/registrar", json={"url": url},
                                 headers={"Authorization": "Bearer " + token})
                print(time.strftime("%H:%M:%S"), "servidor:", "ok" if r.status_code == 200 else f"HTTP {r.status_code} {r.text[:120]}")
            except httpx.HTTPError as exc:
                print(time.strftime("%H:%M:%S"), "servidor fora do ar:", type(exc).__name__)
            await asyncio.sleep(60)


def main() -> None:
    s = load_settings()
    servidor = os.environ.get("TUTORON_SERVIDOR_URL", "").rstrip("/")
    if not (servidor and s.worker_token):
        sys.exit("Defina TUTORON_SERVIDOR_URL e TUTORON_WORKER_TOKEN no .env.")
    try:
        httpx.get(s.ollama_url + "/api/tags", timeout=5).raise_for_status()
    except httpx.HTTPError:
        sys.exit("O Ollama não está ligado. Abra o 1-Iniciar-Servidor.bat (ele liga o Ollama) e rode de novo.")
    proc, url = abrir_tunel()
    print("Túnel do modelo local:", url)
    config = uvicorn.Config(criar_proxy(s.ollama_url, s.worker_token), host="127.0.0.1", port=PORTA, log_level="warning")
    servidor_proxy = uvicorn.Server(config)

    async def tudo():
        await asyncio.gather(servidor_proxy.serve(), avisar(servidor, s.worker_token, url))
    try:
        asyncio.run(tudo())
    except KeyboardInterrupt:
        pass
    finally:
        proc.terminate()


if __name__ == "__main__":
    main()
