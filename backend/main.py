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
from typing import Any

from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator

from .ai_service import AIRequest, AIResponse, AIService, AIServiceError, MockAIService

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
    return MockAIService()


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

    # ------------------------------------------------------------------
    # Global exception handlers — ensure stack traces never reach the caller
    # ------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Entry point (uvicorn dev server)
# ---------------------------------------------------------------------------

app = create_app()
