"""
TutorOn backend — FastAPI application factory.

Exposes a single endpoint:

    POST /api/v1/questions

The AI service implementation is injected via FastAPI's dependency-injection
system, so tests and future integrations can swap implementations without
touching this file.
"""

from __future__ import annotations

import logging
import os
from typing import Any

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request

load_dotenv()
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field, field_validator

from .ai_service import AIRequest, AIResponse, AIService, AIServiceError, MockAIService, RealAIService

logger = logging.getLogger("tutoron.backend")


# ---------------------------------------------------------------------------
# Request / response schemas
# ---------------------------------------------------------------------------


class QuestionRequest(BaseModel):
    """
    Payload accepted by ``POST /api/v1/questions``.

    Attributes:
        question:   The academic question the student needs help with.
                    Must be a non-empty string.
        context:    Optional code snippet or surrounding text that provides
                    additional context for the AI service.
    """

    question: str = Field(
        ...,
        description="The academic question to be answered. Must not be empty.",
        examples=["Why does my binary search return -1 for a value that exists in the list?"],
    )
    context: str | None = Field(
        default=None,
        description="Optional code snippet or surrounding context.",
        examples=["def binary_search(arr, target):\n    lo, hi = 0, len(arr)"],
    )

    @field_validator("question")
    @classmethod
    def question_must_not_be_blank(cls, value: str) -> str:
        """Reject whitespace-only questions early, before they reach the AI service."""
        if not value.strip():
            raise ValueError("question must not be blank")
        return value.strip()


class ErrorDetail(BaseModel):
    """Structured error payload returned for all non-2xx responses."""

    code: str
    message: str


class ErrorResponse(BaseModel):
    """Top-level error envelope."""

    error: ErrorDetail


class QuestionResponse(BaseModel):
    """
    Normalised response returned by ``POST /api/v1/questions``.

    Attributes:
        answer:   The textual answer produced by the AI service.
        source:   Which backend produced the answer (``"mock"``, ``"openai"``,
                  etc.).  Useful for the team to see during the demo whether a
                  real model is wired in yet.
        metadata: Arbitrary key/value extras from the provider (latency,
                  token counts, model version, …).
    """

    answer: str
    source: str
    metadata: dict[str, Any] = Field(default_factory=dict)


# ---------------------------------------------------------------------------
# Dependency injection
# ---------------------------------------------------------------------------

def get_ai_service() -> AIService:
    """
    FastAPI dependency that provides the active AIService implementation.

    Swap out ``MockAIService()`` for any other :class:`AIService` subclass to
    wire in a real provider — the route handler below never needs to change.

    Returns:
        An instance of the currently active :class:`AIService` implementation.
    """
    provider = os.environ.get("TUTORON_AI_PROVIDER", "real").lower()
    if provider == "mock":
        return MockAIService()
    return RealAIService()


# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------


def create_app(ai_service_override: AIService | None = None) -> FastAPI:
    """
    Build and return the FastAPI application.

    Accepts an optional ``ai_service_override`` so tests can inject a custom
    (e.g. failing) service without monkey-patching global state.

    Args:
        ai_service_override: If provided, replaces the default
                             :func:`get_ai_service` dependency for every
                             request.  Intended for testing only.

    Returns:
        A configured :class:`FastAPI` instance ready to be served by Uvicorn.
    """
    app = FastAPI(
        title="TutorOn Backend",
        description=(
            "Minimal backend for the TutorOn academic micro-tutoring platform. "
            "Receives a student question, routes it through a pluggable AI service, "
            "and returns a normalised answer."
        ),
        version="0.1.0",
    )

    # Override the AI service dependency when running tests.
    if ai_service_override is not None:
        app.dependency_overrides[get_ai_service] = lambda: ai_service_override

    # Global exception handlers — ensure stack traces never reach the caller
  
    @app.exception_handler(AIServiceError)
    async def ai_service_error_handler(
        request: Request, exc: AIServiceError
    ) -> JSONResponse:
        """
        Convert an :class:`AIServiceError` into a clean 502 response.

        The AI service is a downstream dependency; its failure should surface
        as a 502 (Bad Gateway) rather than a 500, making it easier to
        distinguish provider outages from application bugs.
        """
        logger.error("AI service error: %s", exc, exc_info=True)
        return JSONResponse(
            status_code=502,
            content=ErrorResponse(
                error=ErrorDetail(
                    code="AI_SERVICE_ERROR",
                    message="The AI service failed to process the request. Please try again.",
                )
            ).model_dump(),
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(
        request: Request, exc: Exception
    ) -> JSONResponse:
        """
        Catch-all handler for any unexpected exception.

        Logs the full traceback server-side and returns a generic 500 to the
        caller so internal details are never leaked.
        """
        logger.exception("Unhandled exception on %s %s", request.method, request.url)
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                error=ErrorDetail(
                    code="INTERNAL_ERROR",
                    message="An unexpected error occurred. Please try again later.",
                )
            ).model_dump(),
        )

    # ------------------------------------------------------------------
    # Routes
    # ------------------------------------------------------------------

    FRONTEND_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TutorOn AI</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --surface-color: #1e293b;
            --border-color: #334155;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --primary: #3b82f6;
            --primary-hover: #2563eb;
            --error-color: #ef4444;
            --font-family: 'Inter', system-ui, -apple-system, sans-serif;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: var(--font-family);
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding: 2rem 1rem;
        }

        .container {
            background-color: var(--surface-color);
            max-width: 800px;
            width: 100%;
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            border: 1px solid var(--border-color);
            animation: fadeIn 0.5s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 {
            font-size: 2.2rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            font-weight: 800;
        }

        p.subtitle {
            text-align: center;
            color: var(--text-muted);
            margin-bottom: 2rem;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: var(--text-main);
        }

        textarea {
            width: 100%;
            background-color: #0f172a;
            border: 1px solid var(--border-color);
            color: var(--text-main);
            border-radius: 8px;
            padding: 1rem;
            font-family: inherit;
            font-size: 1rem;
            resize: vertical;
            transition: border-color 0.2s, box-shadow 0.2s;
        }

        textarea:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
        }

        button {
            width: 100%;
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 1rem;
            font-size: 1.125rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.2s, transform 0.1s;
        }

        button:hover {
            background-color: var(--primary-hover);
        }

        button:active {
            transform: scale(0.98);
        }

        button:disabled {
            background-color: var(--border-color);
            color: var(--text-muted);
            cursor: not-allowed;
            transform: none;
        }

        #result-container {
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid var(--border-color);
            display: none;
            animation: fadeIn 0.4s ease-out;
        }

        .answer-box {
            background-color: rgba(59, 130, 246, 0.05);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-radius: 8px;
            padding: 1.5rem;
            white-space: pre-wrap;
            line-height: 1.7;
        }

        .source-tag {
            margin-top: 1rem;
            font-size: 0.8rem;
            color: var(--text-muted);
            text-align: right;
            font-style: italic;
        }

        .error-message {
            background-color: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.3);
            color: var(--error-color);
            border-radius: 8px;
            padding: 1rem;
            margin-top: 1rem;
            display: none;
        }

        .spinner {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255,255,255,.3);
            border-radius: 50%;
            border-top-color: white;
            animation: spin 1s ease-in-out infinite;
            margin-right: 8px;
            vertical-align: middle;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>TutorOn AI</h1>
        <p class="subtitle">Seu assistente acadêmico disponível 24 horas por dia</p>
        
        <form id="qa-form">
            <div class="form-group">
                <label for="question">Sua dúvida:</label>
                <textarea id="question" rows="4" placeholder="Ex: O que é recursão e como evitar que ela rode para sempre?" required></textarea>
            </div>
            
            <div class="form-group">
                <label for="context">Código ou contexto adicional (opcional):</label>
                <textarea id="context" rows="6" placeholder="Cole seu código ou mensagens de erro aqui..."></textarea>
            </div>
            
            <button type="submit" id="submit-btn">Perguntar</button>
        </form>

        <div id="error-box" class="error-message"></div>

        <div id="result-container">
            <h3 style="margin-bottom: 1rem; color: #60a5fa; font-weight: 600;">Resposta do Tutor:</h3>
            <div id="answer" class="answer-box"></div>
            <div id="source" class="source-tag"></div>
        </div>
    </div>

    <script>
        document.getElementById('qa-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const questionInput = document.getElementById('question').value.trim();
            const contextInput = document.getElementById('context').value.trim();
            
            const submitBtn = document.getElementById('submit-btn');
            const resultContainer = document.getElementById('result-container');
            const answerBox = document.getElementById('answer');
            const sourceBox = document.getElementById('source');
            const errorBox = document.getElementById('error-box');
            
            if (!questionInput) return;
            
            // Estado de carregamento
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="spinner"></span>Processando...';
            errorBox.style.display = 'none';
            resultContainer.style.display = 'none';
            
            const payload = {
                question: questionInput,
                context: contextInput || null
            };
            
            try {
                const response = await fetch('/api/v1/questions', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                
                const data = await response.json();
                
                if (!response.ok) {
                    let errMsg = 'Ocorreu um erro ao processar a requisição.';
                    if (data.error && data.error.message) {
                        errMsg = data.error.message;
                    } else if (data.detail) {
                        if (Array.isArray(data.detail) && data.detail.length > 0) {
                            errMsg = data.detail[0].msg || JSON.stringify(data.detail);
                        } else {
                            errMsg = JSON.stringify(data.detail);
                        }
                    }
                    throw new Error(errMsg);
                }
                
                // Sucesso
                answerBox.textContent = data.answer;
                sourceBox.textContent = `Respondido por: ${data.source}`;
                resultContainer.style.display = 'block';
                
            } catch (err) {
                errorBox.textContent = err.message;
                errorBox.style.display = 'block';
            } finally {
                // Reseta os estados visuais
                submitBtn.disabled = false;
                submitBtn.textContent = 'Perguntar';
            }
        });
    </script>
</body>
</html>"""

    @app.get("/", tags=["frontend"], response_class=HTMLResponse)
    async def serve_frontend() -> HTMLResponse:
        """
        Rota principal servindo a interface web de MVP do TutorOn.
        Retorna o HTML/CSS/JS estático numa única string.
        """
        return HTMLResponse(content=FRONTEND_HTML, status_code=200)

    @app.get("/health", tags=["health"])
    async def health_check() -> dict[str, str]:
        """
        Liveness probe.  Returns ``{"status": "ok"}`` when the service is up.
        """
        return {"status": "ok"}

    @app.post(
        "/api/v1/questions",
        response_model=QuestionResponse,
        status_code=200,
        tags=["questions"],
        responses={
            422: {"model": ErrorResponse, "description": "Validation error"},
            502: {"model": ErrorResponse, "description": "AI service failure"},
            500: {"model": ErrorResponse, "description": "Unexpected server error"},
        },
    )
    async def ask_question(
        payload: QuestionRequest,
        ai_service: AIService = Depends(get_ai_service),
    ) -> QuestionResponse:
        """
        Accept a student question, route it through the AI service, and return
        a normalised answer.

        Args:
            payload:    Validated request body containing ``question`` and
                        optional ``context``.
            ai_service: Injected :class:`AIService` implementation.  Swappable
                        via FastAPI's dependency-override mechanism.

        Returns:
            A :class:`QuestionResponse` with the answer, source tag, and
            provider metadata.

        Raises:
            AIServiceError: Propagated from the service; caught by the global
                            exception handler and returned as a 502.
        """
        ai_request = AIRequest(
            question=payload.question,
            context=payload.context,
        )

        # AIServiceError bubbles up to the registered exception handler above.
        ai_response: AIResponse = ai_service.ask(ai_request)

        return QuestionResponse(
            answer=ai_response.answer,
            source=ai_response.source,
            metadata=ai_response.metadata,
        )

    return app

app = create_app()