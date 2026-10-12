"""Servidor do TutorON: site único com modo Tutor e modo Validação A/B.

Rotas públicas (podem ser acessadas pela internet via túnel):

    GET  /                    site (modo Tutor e modo Validação)
    POST /api/perguntar       modo Tutor, resposta em streaming (SSE)
    POST /api/feedback        "ajudou?" / "tem erro" de uma resposta do modo Tutor
    POST /api/comparar        modo Validação: gera as respostas A e B (cegas)
    POST /api/avaliar         modo Validação: grava as notas do aluno
    GET  /api/status          modelos disponíveis agora
    POST /api/v1/questions    compatibilidade com a CLI (frontend/cli.py)

Rotas só desta máquina (bloqueadas quando a requisição vem pelo túnel):

    GET  /resultados          painel com o resumo das avaliações
    GET  /api/resultados      o mesmo resumo em JSON
"""
from __future__ import annotations

import asyncio
import json
import logging
import secrets
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Literal

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator

from . import prompts
from .config import Settings, load_settings
from .dados import Limitador, Registro, agora, novo_id
from .llm import LLM, AllUnavailable, Model
from .rag import contexto, recuperar
from .resultados import resumo

logger = logging.getLogger("tutoron.backend")
WEB = Path(__file__).resolve().parent / "web"

MSG_INDISPONIVEL = ("Nenhum modelo conseguiu responder agora (Gemini sobrecarregado e TutorON local desligado). "
                    "Tente de novo em alguns segundos.")


# ---------------------------------------------------------------------------
# Esquemas
# ---------------------------------------------------------------------------

class Pergunta(BaseModel):
    pergunta: str = Field(..., min_length=3, max_length=4000)
    contexto: str | None = Field(default=None, max_length=8000)

    @field_validator("pergunta")
    @classmethod
    def nao_vazia(cls, valor: str) -> str:
        if len(valor.strip()) < 3:
            raise ValueError("Escreva a pergunta.")
        return valor.strip()


class Feedback(BaseModel):
    id: str = Field(..., max_length=40)
    util: bool | None = None
    erro_matematico: bool = False
    comentario: str = Field(default="", max_length=1500)


Nota = Field(..., ge=1, le=5)


class NotasLado(BaseModel):
    clareza: int = Nota
    confianca: int = Nota
    utilidade: int = Nota
    erro_matematico: bool = False


class Avaliacao(BaseModel):
    sessao: str = Field(..., max_length=60)
    preferida: Literal["A", "B", "empate"]
    A: NotasLado
    B: NotasLado
    comentario: str = Field(default="", max_length=1500)
    curso: str = Field(default="", max_length=100)
    periodo: str = Field(default="", max_length=30)


class QuestionRequest(BaseModel):
    """Contrato antigo de /api/v1/questions, usado pela CLI."""
    question: str = Field(..., min_length=1, max_length=4000)
    context: str | None = Field(default=None, max_length=8000)

    @field_validator("question")
    @classmethod
    def question_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("question must not be blank")
        return value.strip()


class QuestionResponse(BaseModel):
    answer: str
    source: str
    metadata: dict[str, Any] = Field(default_factory=dict)


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def cliente(request: Request) -> str:
    return (request.headers.get("cf-connecting-ip")
            or request.headers.get("x-forwarded-for", "").split(",")[0].strip()
            or (request.client.host if request.client else "desconhecido"))


def requisicao_local(request: Request) -> bool:
    """Verdadeiro só para quem está nesta máquina. O túnel sempre envia cf-connecting-ip."""
    if request.headers.get("cf-connecting-ip") or request.headers.get("x-forwarded-for"):
        return False
    return bool(request.client and request.client.host in ("127.0.0.1", "::1", "localhost", "testclient"))


def sse(evento: dict) -> str:
    return "data: " + json.dumps(evento, ensure_ascii=False) + "\n\n"


def rotulo_modelo(provedor: str, modelo: str) -> str:
    return Model(provedor, modelo).label


# ---------------------------------------------------------------------------
# Aplicação
# ---------------------------------------------------------------------------

def create_app(settings: Settings | None = None, llm: LLM | None = None, warm_up: bool = True) -> FastAPI:
    settings = settings or load_settings()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.llm = llm or LLM(settings)
        app.state.registro = Registro(settings.data_dir)
        app.state.limitador = Limitador(settings.rate_limit_per_10min)
        tarefa = asyncio.create_task(app.state.llm.warm_up()) if warm_up else None
        yield
        if tarefa:
            tarefa.cancel()
        if llm is None:
            await app.state.llm.client.aclose()

    app = FastAPI(title="TutorON", version="1.0.0", lifespan=lifespan,
                  docs_url=None, redoc_url=None, openapi_url=None)
    app.mount("/static", StaticFiles(directory=WEB), name="static")

    def limitar(request: Request) -> None:
        if not app.state.limitador.permitir(cliente(request)):
            raise HTTPException(429, "Muitas perguntas em pouco tempo. Aguarde alguns minutos e tente de novo.")

    @app.exception_handler(HTTPException)
    async def erro_http(request: Request, exc: HTTPException):
        return JSONResponse({"erro": exc.detail}, status_code=exc.status_code)

    @app.exception_handler(Exception)
    async def erro_inesperado(request: Request, exc: Exception):
        logger.exception("Erro inesperado em %s", request.url.path)
        return JSONResponse({"erro": "Erro inesperado no servidor. Tente de novo."}, status_code=500)

    from fastapi.exceptions import RequestValidationError

    @app.exception_handler(RequestValidationError)
    async def erro_validacao(request: Request, exc: RequestValidationError):
        detalhe = exc.errors()[0] if exc.errors() else {}
        campo = ".".join(str(p) for p in detalhe.get("loc", [])[1:])
        return JSONResponse({"erro": f"Dados inválidos ({campo}): {detalhe.get('msg', '')}"}, status_code=422)

    # ------------------------------------------------------------------ páginas
    @app.get("/", include_in_schema=False)
    async def pagina() -> FileResponse:
        return FileResponse(WEB / "index.html", headers={"Cache-Control": "no-cache"})

    @app.get("/design.css", include_in_schema=False)
    async def design_css() -> Response:
        from design import stylesheet
        return Response(stylesheet(), media_type="text/css; charset=utf-8", headers={"Cache-Control": "no-cache"})

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/api/status")
    async def status(request: Request) -> dict:
        local = await app.state.llm.local_status()
        dados = {
            "gemini": {"habilitado": settings.gemini_enabled, "modelos": list(settings.gemini_models)},
            "local": local,
            "pausados": app.state.llm.breaker.state(),
            "livro_supabase": settings.supabase_enabled,
        }
        if requisicao_local(request):
            url = settings.data_dir / "url-publica.txt"
            dados["url_publica"] = url.read_text(encoding="utf-8-sig").strip() if url.exists() else None
        return dados

    # ------------------------------------------------------------------ modo Tutor
    @app.post("/api/perguntar")
    async def perguntar(corpo: Pergunta, request: Request) -> StreamingResponse:
        limitar(request)
        llm_: LLM = app.state.llm
        registro: Registro = app.state.registro

        async def eventos():
            ident = novo_id()
            trechos = await recuperar(corpo.pergunta, llm_, settings)
            yield sse({"tipo": "fontes", "fontes": [t.publico() for t in trechos]})
            prompt = prompts.prompt_tutor(corpo.pergunta, contexto(trechos), corpo.contexto)
            partes: list[str] = []
            try:
                async for evento in llm_.stream(prompts.SISTEMA_TUTOR, prompt):
                    if await request.is_disconnected():
                        return
                    if evento["tipo"] == "texto":
                        partes.append(evento["texto"])
                    elif evento["tipo"] == "reiniciar":
                        partes.clear()
                    elif evento["tipo"] == "modelo":
                        evento["rotulo"] = rotulo_modelo(evento["provedor"], evento["modelo"])
                    elif evento["tipo"] == "fim":
                        evento["id"] = ident
                        registro.anexar("perguntas.jsonl", {
                            "id": ident, "data": agora(), "pergunta": corpo.pergunta, "contexto": corpo.contexto,
                            "resposta": "".join(partes), "provedor": evento["provedor"], "modelo": evento["modelo"],
                            "segundos": evento["segundos"], "tentativas": evento["tentativas"],
                            "fontes": [t.publico() for t in trechos]})
                    yield sse(evento)
            except AllUnavailable as exc:
                registro.anexar("perguntas.jsonl", {"id": ident, "data": agora(), "pergunta": corpo.pergunta,
                                                    "erro": "nenhum_modelo", "tentativas": exc.attempts})
                yield sse({"tipo": "erro", "mensagem": MSG_INDISPONIVEL})

        return StreamingResponse(eventos(), media_type="text/event-stream",
                                 headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})

    @app.post("/api/feedback")
    async def feedback(corpo: Feedback) -> dict:
        app.state.registro.anexar("feedback.jsonl", {"data": agora(), **corpo.model_dump()})
        return {"salvo": True}

    # ------------------------------------------------------------------ modo Validação
    async def gerar_par(pergunta: str, contexto_aluno: str | None) -> dict:
        llm_: LLM = app.state.llm
        trechos = await recuperar(pergunta, llm_, settings)
        prompt_tutor = prompts.prompt_tutor(pergunta, contexto(trechos), contexto_aluno)
        prompt_gen = prompts.prompt_generico(pergunta, contexto_aluno)
        modelos_genericos = llm_.cascade(local_model=settings.local_generic_model)
        tutor, generico = await asyncio.gather(
            llm_.complete(prompts.SISTEMA_TUTOR, prompt_tutor),
            llm_.complete(None, prompt_gen, models=modelos_genericos),
            return_exceptions=True)
        if isinstance(tutor, BaseException):
            raise tutor
        # Comparação justa: o genérico deve usar o mesmo modelo de base do TutorON,
        # só sem material e sem as instruções. Se a cascata caiu em outro, refaz.
        alvo = tutor.model if tutor.model.provider == "gemini" else Model("ollama", settings.local_generic_model)
        if isinstance(generico, BaseException) or generico.model != alvo:
            try:
                generico = await llm_.complete(None, prompt_gen, models=[alvo])
            except AllUnavailable:
                if isinstance(generico, BaseException):
                    raise
        return {
            "tutoron": {"texto": tutor.text, "provedor": tutor.model.provider, "modelo": tutor.model.name,
                        "segundos": tutor.seconds, "tentativas": tutor.attempts,
                        "fontes": [t.publico() for t in trechos], "sistema": "TutorON (RAG + prompt)"},
            "generico": {"texto": generico.text, "provedor": generico.model.provider, "modelo": generico.model.name,
                         "segundos": generico.seconds, "tentativas": generico.attempts,
                         "sistema": "Genérico (mesmo modelo, sem material nem instruções)"},
        }

    @app.post("/api/comparar")
    async def comparar(corpo: Pergunta, request: Request) -> dict:
        limitar(request)
        try:
            par = await gerar_par(corpo.pergunta, corpo.contexto)
        except AllUnavailable:
            raise HTTPException(503, MSG_INDISPONIVEL)
        ordem = ["tutoron", "generico"]
        secrets.SystemRandom().shuffle(ordem)
        sessao = novo_id()
        app.state.registro.nova_comparacao({
            "sessao": sessao, "data": agora(), "pergunta": corpo.pergunta, "contexto": corpo.contexto,
            "lados": {"A": ordem[0], "B": ordem[1]}, "respostas": par})
        # A identidade de cada lado nunca sai do servidor.
        return {"sessao": sessao, "pergunta": corpo.pergunta,
                "A": par[ordem[0]]["texto"], "B": par[ordem[1]]["texto"]}

    @app.post("/api/avaliar")
    async def avaliar(corpo: Avaliacao) -> dict:
        comparacao = app.state.registro.concluir_comparacao(corpo.sessao)
        if not comparacao:
            raise HTTPException(400, "Esta comparação já foi avaliada ou expirou. Gere uma nova.")
        lados = comparacao["lados"]
        notas = {lados["A"]: corpo.A.model_dump(), lados["B"]: corpo.B.model_dump()}
        app.state.registro.anexar("validacao/avaliacoes.jsonl", {
            "sessao": corpo.sessao, "data": agora(), "data_comparacao": comparacao["data"],
            "pergunta": comparacao["pergunta"], "contexto": comparacao.get("contexto"),
            "preferida": corpo.preferida,
            "preferida_condicao": "empate" if corpo.preferida == "empate" else lados[corpo.preferida],
            "lado_tutoron": "A" if lados["A"] == "tutoron" else "B",
            "notas": notas, "notas_por_lado": {"A": corpo.A.model_dump(), "B": corpo.B.model_dump()},
            "comentario": corpo.comentario, "curso": corpo.curso, "periodo": corpo.periodo,
            "respostas": comparacao["respostas"]})
        return {"salvo": True}

    # ------------------------------------------------------------------ resultados (só local)
    @app.get("/api/resultados")
    async def api_resultados(request: Request) -> dict:
        if not requisicao_local(request):
            raise HTTPException(404, "Não encontrado.")
        return resumo(app.state.registro)

    @app.get("/resultados", include_in_schema=False)
    async def pagina_resultados(request: Request) -> FileResponse:
        if not requisicao_local(request):
            raise HTTPException(404, "Não encontrado.")
        return FileResponse(WEB / "resultados.html", headers={"Cache-Control": "no-cache"})

    # ------------------------------------------------------------------ compatibilidade (CLI)
    @app.post("/api/v1/questions", response_model=QuestionResponse)
    async def ask_question(payload: QuestionRequest, request: Request) -> QuestionResponse:
        limitar(request)
        trechos = await recuperar(payload.question, app.state.llm, settings)
        try:
            resultado = await app.state.llm.complete(
                prompts.SISTEMA_TUTOR, prompts.prompt_tutor(payload.question, contexto(trechos), payload.context))
        except AllUnavailable:
            raise HTTPException(503, MSG_INDISPONIVEL)
        return QuestionResponse(answer=resultado.text, source=f"{resultado.model.provider}-rag", metadata={
            "model": resultado.model.name, "latency_ms": round(resultado.seconds * 1000),
            "chunks_used": len(trechos), "sources": [t.publico() for t in trechos], "attempts": resultado.attempts})

    return app


app = create_app()
