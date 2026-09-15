"""
AI Service interface and concrete implementations.

This module defines the provider-agnostic contract (AIService) that every
AI backend must satisfy. The route layer only ever depends on this interface,
so swapping in a real model later requires adding a new class here and
updating the dependency-injection wiring in main.py — nothing else changes.
"""

from __future__ import annotations

import os
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import httpx


@dataclass
class AIRequest:
    """
    Normalised input passed to any AIService implementation.

    Attributes:
        question: The academic question the student needs help with.
        context:  Optional code snippet or surrounding context that may help
                  the model produce a more accurate answer.
    """

    question: str
    context: str | None = None


@dataclass
class AIResponse:
    """
    Normalised output returned by any AIService implementation.

    Attributes:
        answer:    The textual answer produced by the service.
        source:    Identifier for which backend produced the answer
                   (e.g. ``"mock"``, ``"openai"``, ``"gemini"``).
        metadata:  Arbitrary key/value bag for provider-specific extras
                   (latency, token counts, model version, …).  Consumers
                   should treat unknown keys as informational only.
    """

    answer: str
    source: str
    metadata: dict = field(default_factory=dict)


class AIService(ABC):
    """
    Abstract base class defining the contract every AI backend must implement.

    Implementing classes must override :meth:`ask` and return an
    :class:`AIResponse`.  They must *not* raise generic exceptions — any
    provider-specific error should be wrapped in a :class:`AIServiceError`
    so the route layer can catch a single, predictable exception type.
    """

    @abstractmethod
    def ask(self, request: AIRequest) -> AIResponse:
        """
        Submit a question to the AI backend and return a normalised response.

        Args:
            request: The normalised input containing the question and optional
                     context.

        Returns:
            An :class:`AIResponse` with the answer, source tag, and metadata.

        Raises:
            AIServiceError: If the underlying provider call fails for any reason.
        """


class AIServiceError(Exception):
    """
    Raised by :class:`AIService` implementations when the provider call fails.

    Wrapping provider-specific exceptions in this type lets the route layer
    catch a single, predictable error instead of every possible SDK exception.
    """


class MockAIService(AIService):
    """
    Deterministic stub implementation of :class:`AIService` for development
    and testing.

    Returns a clearly-labelled placeholder answer so it is always obvious
    when a response comes from the mock rather than a real AI provider.
    No network calls are made; the response is instantaneous and predictable.
    """

    # Prefix added to every answer so callers can tell at a glance this is a real model response.
    MOCK_ANSWER_PREFIX = "[MOCK RESPONSE — real AI provider not yet connected]"

    def ask(self, request: AIRequest) -> AIResponse:
        """
        Return a deterministic placeholder answer without calling any external
        service.

        Args:
            request: The normalised input (question text and optional context).

        Returns:
            An :class:`AIResponse` whose ``source`` is ``"mock"`` and whose
            ``answer`` echoes the question so it is easy to verify round-trips
            in tests and demos.
        """
        start = time.perf_counter()

        context_note = (
            f" (context provided: {len(request.context)} chars)"
            if request.context
            else ""
        )
        answer = (
            f"{self.MOCK_ANSWER_PREFIX}\n\n"
            f"You asked: \"{request.question}\"{context_note}\n\n"
            "This is a placeholder. Once the AI strategy (Issue #1) is "
            "finalised, a real provider implementation will replace this mock "
            "without any changes to the route layer."
        )

        elapsed_ms = round((time.perf_counter() - start) * 1000, 2)

        return AIResponse(
            answer=answer,
            source="mock",
            metadata={
                "provider": "MockAIService",
                "latency_ms": elapsed_ms,
            },
        )


class RealAIService(AIService):
    """
    Implementação real de :class:`AIService` que se comunica com a API do Google Gemini
    via HTTP puro, utilizando a biblioteca httpx.
    """

    def __init__(self, api_key: str | None = None, model: str | None = None):
        """
        Inicializa o serviço de LLM real (Gemini).

        Args:
            api_key: A chave de API. Se omitida, será lida da variável de
                     ambiente ``TUTORON_LLM_API_KEY``.
            model:   O modelo a ser utilizado. Se omitido, será lido da
                     variável ``TUTORON_LLM_MODEL`` (com fallback para um padrão).

        Raises:
            ValueError: Se a chave de API não for fornecida e a variável de
                        ambiente não estiver definida.
        """
        self.api_key = api_key or os.environ.get("TUTORON_LLM_API_KEY")
        if not self.api_key:
            raise ValueError("A chave de API TUTORON_LLM_API_KEY deve ser configurada nas variáveis de ambiente.")
        self.model = model or os.environ.get("TUTORON_LLM_MODEL") or "gemini-3.1-flash-lite"
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"

    def ask(self, request: AIRequest) -> AIResponse:
        """
        Envia a pergunta do aluno para a API do Google Gemini e retorna a resposta formatada.

        Args:
            request: O objeto contendo a pergunta e o contexto opcional.

        Returns:
            Um :class:`AIResponse` com a resposta do modelo, a fonte
            e metadados da requisição (latência e modelo utilizado).

        Raises:
            AIServiceError: Se houver falha de rede (Timeout/ConnectError),
                            a API retornar um erro (HTTP não-2xx) ou formato inesperado.
        """
        start = time.perf_counter()

        system_prompt = (
            "Você deve agir como um tutor acadêmico para estudantes universitários, "
            "focado nas áreas de programação, lógica, matemática e exatas. "
            "Sua tarefa é explicar os conceitos de forma didática e passo a passo, "
            "em vez de apenas entregar a resposta pronta. Seja conciso, mas completo."
        )
        
        user_prompt = request.question
        if request.context:
            user_prompt += f"\n\nContexto fornecido:\n{request.context}"

        payload = {
            "system_instruction": {
                "parts": [{"text": system_prompt}]
            },
            "contents": [
                {
                    "parts": [{"text": user_prompt}]
                }
            ]
        }

        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.post(
                    self.url,
                    headers={"x-goog-api-key": self.api_key},
                    json=payload
                )
                response.raise_for_status()
                data = response.json()

                answer = data["candidates"][0]["content"]["parts"][0]["text"]

                elapsed_ms = round((time.perf_counter() - start) * 1000, 2)

                return AIResponse(
                    answer=answer,
                    source=self.model,
                    metadata={
                        "model": self.model,
                        "latency_ms": elapsed_ms,
                    }
                )
        except httpx.TimeoutException as e:
            raise AIServiceError("Tempo de requisição esgotado ao contatar a API do LLM.") from e
        except httpx.ConnectError as e:
            raise AIServiceError("Falha de conexão ao tentar contatar a API do LLM.") from e
        except httpx.HTTPStatusError as e:
            raise AIServiceError(f"A API do LLM retornou erro HTTP {e.response.status_code}.") from e
        except (KeyError, IndexError, TypeError) as e:
            raise AIServiceError("Resposta inesperada ou campo de texto ausente no JSON da API do LLM.") from e

