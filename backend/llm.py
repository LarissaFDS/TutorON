"""Cascata de modelos: Gemini (vários modelos, em ordem) e, por último, o TutorON local.

Como a troca é rápida:

- Todas as chamadas usam streaming. Um modelo só é escolhido quando entrega o
  primeiro trecho de texto; erro HTTP (503, 429, 404…) ou demora acima do
  prazo passa imediatamente para o próximo, sem novas tentativas.
- Um modelo que falhou fica em pausa por alguns segundos (disjuntor), então
  as próximas perguntas nem tentam o modelo que acabou de cair.
- O primeiro modelo da lista que responder é o que responde ao aluno.
"""
from __future__ import annotations

import asyncio
import contextvars
import json
import logging
import time
from collections.abc import AsyncIterator
from dataclasses import dataclass, field

import httpx

from .config import Settings

logger = logging.getLogger("tutoron.llm")

# Desliga o raciocínio do modelo local na tentativa de resgate (responde em ~25 s em vez de ~60 s).
SEM_RACIOCINIO: contextvars.ContextVar[bool] = contextvars.ContextVar("sem_raciocinio", default=False)

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:streamGenerateContent?alt=sse"


class Unavailable(Exception):
    """O modelo não pôde responder agora; tentar o próximo da cascata."""

    def __init__(self, reason: str, pause_s: float, info: dict | None = None):
        super().__init__(reason)
        self.reason = reason
        self.pause_s = pause_s
        self.info = info or {}  # detalhes para o log (ex.: retryDelay e cota do 429)


class AllUnavailable(Exception):
    def __init__(self, attempts: list[dict]):
        super().__init__("Nenhum modelo disponível")
        self.attempts = attempts


@dataclass(frozen=True)
class Model:
    provider: str  # "gemini" | "ollama"
    name: str

    @property
    def key(self) -> str:
        return f"{self.provider}:{self.name}"

    @property
    def label(self) -> str:
        if self.provider == "gemini":
            return " ".join(part.capitalize() for part in self.name.split("-"))
        return f"{self.name} (local)"


def pause_for_status(status: int) -> float:
    if status == 429:
        return 60.0  # cota: esperar mais
    if status in (400, 401, 403, 404):
        return 600.0  # modelo inexistente ou chave sem acesso
    return 20.0  # 500/502/503/504: sobrecarga momentânea


def retry_delay(corpo: bytes) -> float:
    """Espera informada pelo Google no 429 (cota diária esgotada pode ser de horas), limitada a 1 h."""
    espera = detalhes_429(corpo).get("retry_delay_s")
    return min(3600.0, espera) if espera else 0.0


def detalhes_429(corpo: bytes) -> dict:
    """O que o corpo do 429 diz sobre a cota, para o log: retryDelay (sem limite), quotaId das
    violações e se a cota esgotada é por dia ou por minuto. Campos ausentes ficam de fora."""
    info: dict = {}
    try:
        detalhes = json.loads(corpo).get("error", {}).get("details", [])
        for d in detalhes if isinstance(detalhes, list) else []:
            if not isinstance(d, dict):
                continue
            if "retryDelay" in d:
                info["retry_delay_s"] = float(str(d["retryDelay"]).rstrip("s"))
            for v in d.get("violations", []) or []:
                if isinstance(v, dict) and v.get("quotaId"):
                    info.setdefault("quota_ids", []).append(str(v["quotaId"]))
    except (ValueError, AttributeError, TypeError):
        return info
    ids = " ".join(info.get("quota_ids", []))
    if "PerDay" in ids:
        info["cota"] = "por_dia"
    elif "PerMinute" in ids:
        info["cota"] = "por_minuto"
    return info


class Breaker:
    """Pausa modelos que acabaram de falhar."""

    def __init__(self):
        self._until: dict[str, float] = {}
        self._reason: dict[str, str] = {}

    def is_paused(self, model: Model) -> bool:
        return self._until.get(model.key, 0) > time.monotonic()

    def trip(self, model: Model, reason: str, seconds: float) -> None:
        self._until[model.key] = time.monotonic() + seconds
        self._reason[model.key] = reason

    def reset(self, model: Model) -> None:
        self._until.pop(model.key, None)
        self._reason.pop(model.key, None)

    def state(self) -> dict[str, dict]:
        now = time.monotonic()
        return {key: {"pausado_por_s": round(until - now), "motivo": self._reason.get(key, "")}
                for key, until in self._until.items() if until > now}


@dataclass
class Result:
    text: str
    model: Model
    seconds: float
    attempts: list[dict] = field(default_factory=list)
    finish: str = ""


def degradado(modelo: Model, tentativas: list[dict], cascata: list[Model]) -> bool:
    """A resposta veio do último Gemini da cascata (o flash-lite, o "piso") porque os modelos
    melhores falharam ou estavam em pausa? Cancelado por outro ter respondido não conta como falha."""
    gemini = [m for m in cascata if m.provider == "gemini"]
    if len(gemini) < 2 or modelo != gemini[-1]:
        return False
    melhores = {m.key for m in gemini[:-1]}
    return any(t["modelo"] in melhores and t["resultado"] != "respondeu"
               and not t["resultado"].startswith("cancelado") for t in tentativas)


class LLM:
    def __init__(self, settings: Settings, client: httpx.AsyncClient | None = None):
        self.settings = settings
        self.client = client or httpx.AsyncClient(timeout=httpx.Timeout(60, connect=5))
        self.breaker = Breaker()
        # Gerações locais simultâneas: o Ollama roda com OLLAMA_NUM_PARALLEL=2 (o melhor na RTX 4060).
        self.local_lock = asyncio.Semaphore(settings.local_parallel)
        self.local_waiting = 0  # pedidos esperando a GPU (mostrado ao aluno como posição na fila)
        self._thinking: dict[str, bool] = {}

    # ------------------------------------------------------------------ modelos
    def cascade(self, *, local_model: str | None = None) -> list[Model]:
        models = [Model("gemini", name) for name in self.settings.gemini_models] if self.settings.gemini_enabled else []
        models.append(Model("ollama", local_model or self.settings.local_model))
        return models

    # ------------------------------------------------------------------ provedores
    async def _gemini(self, model: Model, system: str | None, prompt: str) -> AsyncIterator[str]:
        body: dict = {
            "contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.3, "maxOutputTokens": 8192},
        }
        if system:
            body["systemInstruction"] = {"parts": [{"text": system}]}
        headers = {"x-goog-api-key": self.settings.gemini_api_key}
        try:
            async with self.client.stream("POST", GEMINI_URL.format(model=model.name), json=body, headers=headers,
                                          timeout=httpx.Timeout(self.settings.gemini_idle_s, connect=5)) as response:
                if response.status_code != 200:
                    corpo = await response.aread()
                    pausa = pause_for_status(response.status_code)
                    info = {}
                    if response.status_code == 429:
                        info = detalhes_429(corpo)
                        pausa = max(pausa, retry_delay(corpo))
                    raise Unavailable(f"HTTP {response.status_code}", pausa, info)
                async for line in response.aiter_lines():
                    if not line.startswith("data:"):
                        continue
                    try:
                        payload = json.loads(line[5:])
                    except json.JSONDecodeError:
                        continue
                    if "error" in payload:
                        raise Unavailable(f"erro no stream: {payload['error'].get('status', '')}", 20.0)
                    for candidate in payload.get("candidates", [])[:1]:
                        for part in candidate.get("content", {}).get("parts", []):
                            if part.get("text") and not part.get("thought"):
                                yield part["text"]
                        reason = candidate.get("finishReason")
                        if reason and reason not in ("STOP", "MAX_TOKENS"):
                            raise Unavailable(f"resposta interrompida ({reason})", 5.0)
        except httpx.TimeoutException as exc:
            raise Unavailable("tempo esgotado", 30.0) from exc
        except httpx.HTTPError as exc:
            raise Unavailable(f"rede: {type(exc).__name__}", 15.0) from exc

    async def supports_thinking(self, name: str) -> bool:
        """Modelos com raciocínio (qwen3…) erram bem menos contas com ele ligado."""
        if name not in self._thinking:
            try:
                info = (await self.client.post(self.settings.ollama_url + "/api/show", json={"model": name}, timeout=5)).json()
                self._thinking[name] = "thinking" in info.get("capabilities", [])
            except (httpx.HTTPError, ValueError):
                return False
        return self._thinking[name]

    async def _ollama(self, model: Model, system: str | None, prompt: str) -> AsyncIterator[str]:
        messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
        body = {"model": model.name, "messages": messages, "stream": True, "keep_alive": "60m",
                "options": {"temperature": 0.2, "num_ctx": self.settings.local_num_ctx, "num_predict": 8192}}
        if await self.supports_thinking(model.name):
            # Com 2+ pedidos esperando a GPU (turma inteira usando), responde sem raciocínio para a fila andar.
            pensar = self.settings.local_thinking and not SEM_RACIOCINIO.get() and self.local_waiting < 2
            body["think"] = pensar
            if pensar:
                # Recomendação do Qwen3 para o modo com raciocínio (temperatura baixa demais causa repetição).
                body["options"].update(temperature=0.6, top_p=0.95, top_k=20)
        try:
            async with self.client.stream("POST", self.settings.ollama_url + "/api/chat", json=body,
                                          timeout=httpx.Timeout(self.settings.local_first_chunk_s, connect=3)) as response:
                if response.status_code != 200:
                    await response.aread()
                    raise Unavailable(f"Ollama HTTP {response.status_code}", 10.0)
                async for line in response.aiter_lines():
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    if data.get("error"):
                        raise Unavailable(f"Ollama: {data['error'][:80]}", 10.0)
                    text = data.get("message", {}).get("content", "")
                    if text:
                        yield text
                    if data.get("done"):
                        break
        except httpx.TimeoutException as exc:
            raise Unavailable("Ollama: tempo esgotado", 10.0) from exc
        except httpx.HTTPError as exc:
            raise Unavailable("Ollama local desligado", 10.0) from exc

    def _provider(self, model: Model, system: str | None, prompt: str) -> AsyncIterator[str]:
        return self._gemini(model, system, prompt) if model.provider == "gemini" else self._ollama(model, system, prompt)

    # ------------------------------------------------------------------ cascata
    async def _start(self, model: Model, system: str | None, prompt: str, started: float) -> dict:
        """Abre o stream e espera o primeiro trecho. Devolve o competidor pronto ou o erro."""
        timeout = self.settings.local_first_chunk_s if model.provider == "ollama" else self.settings.gemini_first_chunk_s
        lock = self.local_lock if model.provider == "ollama" else None
        if lock:
            self.local_waiting += 1
            try:
                await lock.acquire()
            finally:
                self.local_waiting -= 1
        generator = self._provider(model, system, prompt)
        try:
            first = await asyncio.wait_for(generator.__anext__(), timeout)
        except BaseException as exc:
            await generator.aclose()
            if lock:
                lock.release()
            if isinstance(exc, asyncio.CancelledError):
                raise
            if isinstance(exc, asyncio.TimeoutError):
                exc = Unavailable("sem resposta no prazo", 30.0)
            elif isinstance(exc, StopAsyncIteration):
                exc = Unavailable("resposta vazia", 10.0)
            elif not isinstance(exc, Unavailable):
                exc = Unavailable(f"erro inesperado: {type(exc).__name__}", 15.0)
            return {"model": model, "error": exc, "t0": started}
        return {"model": model, "generator": generator, "first": first, "lock": lock, "t0": started}

    @staticmethod
    async def _discard(result: dict) -> None:
        if result.get("generator"):
            await result["generator"].aclose()
        if result.get("lock"):
            result["lock"].release()

    async def stream(self, system: str | None, prompt: str, *, models: list[Model] | None = None,
                     ) -> AsyncIterator[dict]:
        """Corrida escalonada entre os modelos. Gera eventos:
        {"tipo": "modelo"}, {"tipo": "texto"}, {"tipo": "reiniciar"}, {"tipo": "fim"}.

        O primeiro modelo da lista começa na hora. Se ele não entregar texto em
        ``TUTORON_ESCALONAMENTO_S`` segundos, ou falhar, o próximo também começa,
        sem cancelar o anterior. Quem entregar o primeiro trecho vence e os outros
        são cancelados. O modelo local entra quando todos os Gemini falharam ou
        depois de ``TUTORON_ESPERA_LOCAL_S`` segundos sem resposta.

        Lança AllUnavailable se nenhum modelo responder.
        """
        attempts: list[dict] = []
        start = time.monotonic()
        candidates = list(models or self.cascade())
        # Modelos em pausa ficam de fora (o último da lista nunca é descartado).
        queue = []
        for m in candidates[:-1]:
            if self.breaker.is_paused(m):
                attempts.append({"modelo": m.key, "resultado": "pulado (em pausa)"})
            else:
                queue.append(m)
        queue += candidates[-1:]
        running: dict[asyncio.Task, Model] = {}
        last_launch = start

        def launch() -> None:
            nonlocal last_launch
            model = queue.pop(0)
            running[asyncio.create_task(self._start(model, system, prompt, time.monotonic()))] = model
            last_launch = time.monotonic()

        def next_launch_at() -> float | None:
            if not queue:
                return None
            if queue[0].provider == "ollama":
                # O local entra depois de todos os Gemini, ou após a espera máxima.
                return start + self.settings.local_wait_s
            return last_launch + self.settings.stagger_s

        async def cancel_all() -> None:
            for task in running:
                task.cancel()
            for task, model in list(running.items()):
                try:
                    result = await task
                except (asyncio.CancelledError, Exception):
                    result = {}
                await self._discard(result)
                attempts.append({"modelo": model.key, "resultado": "cancelado (outro respondeu antes)"})
            running.clear()

        try:
            while queue or running:
                if not running:
                    launch()
                    if running[next(reversed(running))].provider == "ollama":
                        yield {"tipo": "aguarde", "provedor": "ollama"}
                when = next_launch_at()
                wait = None if when is None else max(0.0, when - time.monotonic())
                done, _ = await asyncio.wait(running, timeout=wait, return_when=asyncio.FIRST_COMPLETED)
                if not done:
                    launch()
                    if running[next(reversed(running))].provider == "ollama":
                        yield {"tipo": "aguarde", "provedor": "ollama"}
                    continue
                winner = None
                for task in done:
                    model = running.pop(task)
                    result = task.result()
                    if "error" in result:
                        exc = result["error"]
                        self.breaker.trip(model, exc.reason, exc.pause_s)
                        attempts.append({"modelo": model.key, "resultado": exc.reason,
                                         "segundos": round(time.monotonic() - result["t0"], 2), **exc.info})
                        logger.warning("Modelo %s indisponível: %s", model.key, exc.reason)
                    elif winner is None:
                        winner = result
                    else:  # dois chegaram juntos: fica o primeiro
                        await self._discard(result)
                if winner is None:
                    # Falhou: o próximo Gemini começa já (o local respeita a espera,
                    # a menos que não reste nenhum Gemini rodando).
                    if queue and (queue[0].provider != "ollama" or not running):
                        launch()
                        if running[next(reversed(running))].provider == "ollama":
                            yield {"tipo": "aguarde", "provedor": "ollama"}
                    continue

                await cancel_all()
                model, generator = winner["model"], winner["generator"]
                idle = self.settings.gemini_idle_s if model.provider == "gemini" else self.settings.local_first_chunk_s
                emitted = False
                try:
                    yield {"tipo": "modelo", "provedor": model.provider, "modelo": model.name}
                    yield {"tipo": "texto", "texto": winner["first"]}
                    emitted = True
                    while True:
                        try:
                            chunk = await asyncio.wait_for(generator.__anext__(), idle)
                        except StopAsyncIteration:
                            break
                        except asyncio.TimeoutError as exc:
                            raise Unavailable("parou de responder", 30.0) from exc
                        yield {"tipo": "texto", "texto": chunk}
                    self.breaker.reset(model)
                    attempts.append({"modelo": model.key, "resultado": "respondeu",
                                     "segundos": round(time.monotonic() - winner["t0"], 2)})
                    yield {"tipo": "fim", "provedor": model.provider, "modelo": model.name,
                           "segundos": round(time.monotonic() - start, 2), "tentativas": attempts}
                    return
                except Unavailable as exc:
                    self.breaker.trip(model, exc.reason, exc.pause_s)
                    attempts.append({"modelo": model.key, "resultado": exc.reason,
                                     "segundos": round(time.monotonic() - winner["t0"], 2), **exc.info})
                    if emitted:
                        yield {"tipo": "reiniciar", "motivo": f"{model.name} parou no meio da resposta"}
                finally:
                    await self._discard(winner)
            raise AllUnavailable(attempts)
        finally:
            await cancel_all()

    async def complete(self, system: str | None, prompt: str, *, models: list[Model] | None = None) -> Result:
        """Resposta completa (sem streaming) usando a mesma cascata."""
        parts: list[str] = []
        async for event in self.stream(system, prompt, models=models):
            if event["tipo"] == "texto":
                parts.append(event["texto"])
            elif event["tipo"] == "reiniciar":
                parts.clear()
            elif event["tipo"] == "fim":
                return Result(text="".join(parts).strip(), model=Model(event["provedor"], event["modelo"]),
                              seconds=event["segundos"], attempts=event["tentativas"])
        raise AllUnavailable([])

    # ------------------------------------------------------------------ utilidades
    async def embed(self, text: str) -> list[float] | None:
        """Embedding bge-m3 da pergunta, na CPU (0,3 s): assim o modelo de resposta não sai da GPU.
        None se o Ollama estiver desligado."""
        try:
            response = await self.client.post(self.settings.ollama_url + "/api/embed",
                                              json={"model": self.settings.embed_model, "input": [text],
                                                    "keep_alive": "60m", "options": {"num_gpu": 0}}, timeout=httpx.Timeout(30, connect=3))
            response.raise_for_status()
            return response.json()["embeddings"][0]
        except (httpx.HTTPError, KeyError, IndexError) as exc:
            logger.warning("Embedding indisponível: %s", type(exc).__name__)
            return None

    async def local_status(self) -> dict:
        try:
            tags = (await self.client.get(self.settings.ollama_url + "/api/tags", timeout=3)).json()
            loaded = (await self.client.get(self.settings.ollama_url + "/api/ps", timeout=3)).json()
        except (httpx.HTTPError, ValueError):
            return {"online": False}
        names = {m["name"] for m in tags.get("models", [])}
        wanted = self.settings.local_model if ":" in self.settings.local_model else self.settings.local_model + ":latest"
        return {"online": True, "modelo": self.settings.local_model, "instalado": wanted in names,
                "carregado": any(m["name"] == wanted for m in loaded.get("models", []))}

    async def warm_up(self) -> None:
        """Carrega o modelo local e o de embeddings na GPU para o fallback ser imediato."""
        for payload, path in (({"model": self.settings.embed_model, "input": ["aquecimento"], "keep_alive": "60m",
                                "options": {"num_gpu": 0}}, "/api/embed"),
                              ({"model": self.settings.local_model, "keep_alive": "60m"}, "/api/generate")):
            try:
                await self.client.post(self.settings.ollama_url + path, json=payload, timeout=180)
            except httpx.HTTPError:
                logger.warning("Não foi possível pré-carregar %s", payload["model"])
