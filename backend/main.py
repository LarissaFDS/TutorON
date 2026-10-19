"""Servidor do TutorON: site único com modo Tutor e modo Validação A/B.

Rotas públicas (podem ser acessadas pela internet via túnel):

    GET  /                    site (modo Tutor e modo Validação)
    POST /api/perguntar       modo Tutor: cria a tarefa e responde na hora com o id
    POST /api/comparar        modo Validação: cria a tarefa que gera as respostas A e B (cegas)
    GET  /api/tarefas/{id}    andamento da tarefa (o site consulta a cada segundo)
    POST /api/feedback        "ajudou?" / "tem erro" de uma resposta do modo Tutor
    POST /api/avaliar         modo Validação: grava as notas do aluno
    GET  /api/status          modelos disponíveis agora
    GET  /api/disciplinas     disciplinas cadastradas (mesma IA, acervos separados)
    POST /api/v1/questions    compatibilidade com a CLI (frontend/cli.py)

Rotas só desta máquina (bloqueadas quando a requisição vem pelo túnel):

    GET  /resultados          painel com o resumo das avaliações
    GET  /api/resultados      o mesmo resumo em JSON
    POST /api/reiniciar-modelos  libera os modelos em pausa e recarrega o modelo local
"""
from __future__ import annotations

import asyncio
import logging
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Literal

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator

from acervo import disciplinas

from .config import Settings, load_settings
from .dados import Limitador, Registro, agora
from .llm import LLM, Model
from .resultados import resumo
from .tarefas import Tarefas

logger = logging.getLogger("tutoron.backend")
WEB = Path(__file__).resolve().parent / "web"

MSG_INDISPONIVEL = "Não conseguimos gerar a resposta agora. Tente de novo em alguns instantes."


# ---------------------------------------------------------------------------
# Esquemas
# ---------------------------------------------------------------------------

def disciplina_cadastrada(valor: str | None) -> str | None:
    """Sem disciplina, vale a padrão (PAA). Disciplina desconhecida é erro do pedido, não do servidor."""
    if valor is None or not valor.strip():
        return None
    try:
        return disciplinas.obter(valor).id
    except KeyError:
        raise ValueError("Disciplina não cadastrada.") from None


class Pergunta(BaseModel):
    pergunta: str = Field(..., min_length=3, max_length=4000)
    contexto: str | None = Field(default=None, max_length=6000)
    disciplina: str | None = Field(default=None, max_length=40)

    @field_validator("disciplina")
    @classmethod
    def disciplina_valida(cls, valor: str | None) -> str | None:
        return disciplina_cadastrada(valor)

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
    subject: str | None = Field(default=None, max_length=40)

    @field_validator("subject")
    @classmethod
    def subject_valido(cls, valor: str | None) -> str | None:
        return disciplina_cadastrada(valor)

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
        app.state.limitador_gravacao = Limitador(max(600, 2 * settings.rate_limit_per_10min))
        app.state.tarefas = Tarefas(app.state.llm, settings, app.state.registro)
        aquecimento = asyncio.create_task(app.state.llm.warm_up()) if warm_up else None
        yield
        if aquecimento:
            aquecimento.cancel()
        await app.state.tarefas.encerrar()
        if llm is None:
            await app.state.llm.client.aclose()

    app = FastAPI(title="TutorON", version="1.0.0", lifespan=lifespan,
                  docs_url=None, redoc_url=None, openapi_url=None)
    app.mount("/static", StaticFiles(directory=WEB), name="static")

    def limitar(request: Request) -> None:
        if not app.state.limitador.permitir(cliente(request)):
            raise HTTPException(429, "Muitas perguntas em pouco tempo. Aguarde alguns minutos e tente de novo.")

    def limitar_gravacao(request: Request) -> None:
        if not app.state.limitador_gravacao.permitir(cliente(request)):
            raise HTTPException(429, "Muitos envios em pouco tempo. Aguarde alguns minutos e tente de novo.")

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

    @app.get("/api/disciplinas")
    async def lista_disciplinas() -> dict:
        return {"padrao": disciplinas.obter().id, "disciplinas": [d.publico() for d in disciplinas.todas()]}

    # ------------------------------------------------------------------ modo Tutor e Validação (tarefas)
    @app.post("/api/perguntar")
    async def perguntar(corpo: Pergunta, request: Request) -> dict:
        limitar(request)
        return app.state.tarefas.perguntar(corpo.pergunta, corpo.contexto, corpo.disciplina).publico()

    @app.post("/api/comparar")
    async def comparar(corpo: Pergunta, request: Request) -> dict:
        limitar(request)
        return app.state.tarefas.comparar(corpo.pergunta, corpo.contexto, corpo.disciplina).publico()

    @app.get("/api/tarefas/{ident}")
    async def tarefa(ident: str) -> JSONResponse:
        t = app.state.tarefas.obter(ident[:40])
        if not t:
            raise HTTPException(404, "Esta resposta expirou ou o servidor foi reiniciado. Envie a pergunta de novo.")
        return JSONResponse(t.publico(), headers={"Cache-Control": "no-store"})

    @app.post("/api/feedback")
    async def feedback(corpo: Feedback, request: Request) -> dict:
        limitar_gravacao(request)
        app.state.registro.anexar("feedback.jsonl", {"data": agora(), **corpo.model_dump()})
        return {"salvo": True}

    @app.post("/api/avaliar")
    async def avaliar(corpo: Avaliacao, request: Request) -> dict:
        limitar_gravacao(request)
        comparacao = app.state.registro.concluir_comparacao(corpo.sessao)
        if not comparacao:
            if app.state.registro.ja_avaliada(corpo.sessao):
                return {"salvo": True}  # reenvio após queda de rede: a avaliação já está gravada
            raise HTTPException(400, "Esta comparação expirou. Gere uma nova.")
        lados = comparacao["lados"]
        notas = {lados["A"]: corpo.A.model_dump(), lados["B"]: corpo.B.model_dump()}
        app.state.registro.anexar("validacao/avaliacoes.jsonl", {
            "sessao": corpo.sessao, "data": agora(), "data_comparacao": comparacao["data"],
            "disciplina": comparacao.get("disciplina", disciplinas.obter().id),
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

    @app.post("/api/reiniciar-modelos")
    async def reiniciar_modelos(request: Request) -> dict:
        if not requisicao_local(request):
            raise HTTPException(404, "Não encontrado.")
        app.state.llm.breaker = type(app.state.llm.breaker)()
        await app.state.llm.warm_up()
        return {"ok": True, "local": await app.state.llm.local_status(), "tarefas_ativas": app.state.tarefas.ativas()}

    @app.get("/resultados", include_in_schema=False)
    async def pagina_resultados(request: Request) -> FileResponse:
        if not requisicao_local(request):
            raise HTTPException(404, "Não encontrado.")
        return FileResponse(WEB / "resultados.html", headers={"Cache-Control": "no-cache"})

    # ------------------------------------------------------------------ compatibilidade (CLI)
    @app.post("/api/v1/questions", response_model=QuestionResponse)
    async def ask_question(payload: QuestionRequest, request: Request) -> QuestionResponse:
        limitar(request)
        t = app.state.tarefas.perguntar(payload.question, payload.context, payload.subject)
        while t.concluida is None:
            await asyncio.sleep(0.5)
        if t.status != "pronta":
            raise HTTPException(503, MSG_INDISPONIVEL)
        return QuestionResponse(answer=t.texto, source="tutoron-rag", metadata={
            "model": t.rotulo, "latency_ms": round(t.resultado.get("segundos", 0) * 1000),
            "chunks_used": len(t.fontes), "sources": t.fontes, "subject": disciplinas.obter(payload.subject).id})

    return app


app = create_app()
