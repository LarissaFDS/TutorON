"""Liga o modelo local do PC ao TutorON hospedado (o PC vira "worker").

Fluxo: servidor hospedado  --HTTPS-->  túnel Cloudflare  -->  este proxy (com senha)  -->  Ollama do PC

1. Sobe um proxy em 127.0.0.1:11435 que só aceita pedidos com o cabeçalho `x-tutoron-worker`
   igual a TUTORON_WORKER_TOKEN (o Ollama em si continua fechado na máquina).
2. Abre um túnel rápido da Cloudflare (.tools/cloudflared.exe) para esse proxy.
3. A cada minuto avisa o servidor (POST /api/worker/registrar) o endereço do túnel. Se o PC desligar,
   em 2,5 min o servidor tira o modelo local da cascata e responde com Groq/Gemini.

Uso:  7-Ligar-IA-Local.bat  (ou python scripts/worker_pc.py). Se o Ollama estiver desligado, ele é ligado
aqui mesmo, com as mesmas opções do 1-Iniciar-Servidor.bat. A janela mostra um painel a cada 5 s:
pedidos em andamento, total atendido, RAM e VRAM usadas pelo modelo, CPU e GPU do PC.
Precisa no .env: TUTORON_SERVIDOR_URL=https://<seu-app>  e  TUTORON_WORKER_TOKEN=<o mesmo do servidor>.
"""
from __future__ import annotations

import asyncio
import csv
import ctypes
import io
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
ESTADO = {"ativos": 0, "atendidos": 0, "erros": 0, "pico": 0, "servidor": "aguardando", "inicio": time.time()}
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
        geracao = caminho in ("api/chat", "api/generate")
        if geracao:
            ESTADO["ativos"] += 1
            ESTADO["pico"] = max(ESTADO["pico"], ESTADO["ativos"])
        try:
            resposta = await cliente.send(pedido, stream=True)
        except httpx.HTTPError:
            if geracao:
                ESTADO["ativos"] -= 1
                ESTADO["erros"] += 1
            return JSONResponse({"error": "ollama fora do ar"}, status_code=502)

        async def corpo():
            try:
                async for parte in resposta.aiter_raw():
                    yield parte
            finally:
                await resposta.aclose()
                if geracao:
                    ESTADO["ativos"] -= 1
                    ESTADO["atendidos" if resposta.status_code < 400 else "erros"] += 1
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
                ESTADO["servidor"] = (time.strftime("%H:%M ") + ("conectado" if r.status_code == 200
                                      else f"RECUSOU (HTTP {r.status_code}) {r.text[:80]}"))
            except httpx.HTTPError as exc:
                ESTADO["servidor"] = time.strftime("%H:%M ") + "site fora do ar: " + type(exc).__name__
            await asyncio.sleep(60)


# ---------------------------------------------------------------- painel (só Windows + nvidia-smi)
class _Memoria(ctypes.Structure):
    _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]


def _ram_pc() -> str:
    try:
        m = _Memoria(dwLength=ctypes.sizeof(_Memoria))
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
        usado = (m.ullTotalPhys - m.ullAvailPhys) / 2**30
        return f"{usado:.1f} de {m.ullTotalPhys / 2**30:.1f} GB ({m.dwMemoryLoad}%)"
    except Exception:  # noqa: BLE001
        return "?"


_cpu_antes: list[int] = []


def _cpu_pc() -> str:
    try:
        ocioso, kernel, usuario = (ctypes.c_ulonglong(), ctypes.c_ulonglong(), ctypes.c_ulonglong())
        ctypes.windll.kernel32.GetSystemTimes(ctypes.byref(ocioso), ctypes.byref(kernel), ctypes.byref(usuario))
        agora = [ocioso.value, kernel.value + usuario.value]
        antes = _cpu_antes[:] or agora
        _cpu_antes[:] = agora
        total = agora[1] - antes[1]
        return f"{100 * (1 - (agora[0] - antes[0]) / total):.0f}%" if total else "—"
    except Exception:  # noqa: BLE001
        return "?"


def _ram_ollama() -> str:
    try:
        saida = subprocess.run(["tasklist", "/FO", "CSV", "/NH"], capture_output=True, text=True, timeout=10,
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0)).stdout
        kb = sum(int(re.sub(r"\D", "", linha[4]) or 0) for linha in csv.reader(io.StringIO(saida))
                 if len(linha) > 4 and linha[0].lower().startswith("ollama"))
        return f"{kb / 2**20:.1f} GB"
    except Exception:  # noqa: BLE001
        return "?"


def _gpu() -> str:
    try:
        saida = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.used,memory.total,utilization.gpu,temperature.gpu",
                                "--format=csv,noheader,nounits"], capture_output=True, text=True, timeout=10,
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0)).stdout.strip().splitlines()[0]
        nome, usado, total, uso, temp = [x.strip() for x in saida.split(",")]
        return f"{nome}: VRAM {int(usado) / 1024:.1f} de {int(total) / 1024:.1f} GB, uso {uso}%, {temp} °C"
    except Exception:  # noqa: BLE001
        return "sem nvidia-smi"


async def painel(ollama: str, url: str) -> None:
    async with httpx.AsyncClient(timeout=5) as c:
        while True:
            try:
                carregados = [f"{m['name']} ({m.get('size_vram', 0) / 2**30:.1f} GB na GPU)"
                              for m in (await c.get(ollama + "/api/ps")).json().get("models", [])]
            except Exception:  # noqa: BLE001
                carregados = ["OLLAMA NÃO RESPONDE"]
            ram_ollama, gpu = await asyncio.gather(asyncio.to_thread(_ram_ollama), asyncio.to_thread(_gpu))
            minutos = int((time.time() - ESTADO["inicio"]) // 60)
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 72)
            print(f" TutorON - IA local ligada ao site            ligado há {minutos // 60}h{minutos % 60:02d}")
            print("=" * 72)
            print(f" Site ............ {ESTADO['servidor']}")
            print(f" Túnel ........... {url}")
            print(f" Respondendo agora {ESTADO['ativos']}   (pico: {ESTADO['pico']}; o Ollama faz "
                  f"{os.environ.get('OLLAMA_NUM_PARALLEL', '2')} de cada vez, o resto espera na fila)")
            print(f" Atendidas ....... {ESTADO['atendidos']}   erros: {ESTADO['erros']}")
            print(f" Modelo na memória {', '.join(carregados) or 'nenhum (carrega na 1ª pergunta)'}")
            print(f" RAM do Ollama ... {ram_ollama}")
            print(f" RAM do PC ....... {_ram_pc()}    CPU: {_cpu_pc()}")
            print(f" GPU ............. {gpu}")
            print("-" * 72)
            print(" Deixe esta janela aberta. Fechar = o site passa a usar Groq/Gemini em até 2,5 min.")
            await asyncio.sleep(5)


def ligar_ollama(ollama: str) -> None:
    """Liga o Ollama portátil do projeto com as mesmas opções do 1-Iniciar-Servidor.bat."""
    try:
        httpx.get(ollama + "/api/tags", timeout=3).raise_for_status()
        return
    except httpx.HTTPError:
        pass
    exe = RAIZ / ".tools" / "ollama" / "ollama.exe"
    if not exe.exists():
        sys.exit("O Ollama não está ligado e não achei .tools/ollama. Abra o 1-Iniciar-Servidor.bat uma vez.")
    ambiente = os.environ | {"OLLAMA_MODELS": str(RAIZ / ".tools" / "models"), "OLLAMA_HOST": "127.0.0.1:11434",
                             "OLLAMA_KEEP_ALIVE": "60m", "OLLAMA_FLASH_ATTENTION": "1",
                             "OLLAMA_KV_CACHE_TYPE": "q8_0"}
    ambiente.setdefault("OLLAMA_NUM_PARALLEL", "2")
    os.environ["OLLAMA_NUM_PARALLEL"] = ambiente["OLLAMA_NUM_PARALLEL"]
    logs = RAIZ / "dados" / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    print("Ligando o Ollama...")
    subprocess.Popen([str(exe), "serve"], env=ambiente, stdout=open(logs / "ollama.log", "ab"),
                     stderr=subprocess.STDOUT, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    for _ in range(60):
        time.sleep(0.5)
        try:
            httpx.get(ollama + "/api/tags", timeout=2).raise_for_status()
            return
        except httpx.HTTPError:
            continue
    sys.exit("O Ollama não ligou em 30 s. Veja dados/logs/ollama.log.")


def main() -> None:
    s = load_settings()
    servidor = os.environ.get("TUTORON_SERVIDOR_URL", "").rstrip("/")
    if not (servidor and s.worker_token):
        sys.exit("Defina TUTORON_SERVIDOR_URL e TUTORON_WORKER_TOKEN no .env.")
    ligar_ollama(s.ollama_url)
    proc, url = abrir_tunel()
    print("Túnel do modelo local:", url)
    config = uvicorn.Config(criar_proxy(s.ollama_url, s.worker_token), host="127.0.0.1", port=PORTA, log_level="warning")
    servidor_proxy = uvicorn.Server(config)

    async def tudo():
        await asyncio.gather(servidor_proxy.serve(), avisar(servidor, s.worker_token, url),
                             painel(s.ollama_url, url))
    try:
        asyncio.run(tudo())
    except KeyboardInterrupt:
        pass
    finally:
        proc.terminate()


if __name__ == "__main__":
    main()
