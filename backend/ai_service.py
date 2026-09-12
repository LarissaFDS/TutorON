"""
AI Service interface and concrete implementations.

This module defines the provider-agnostic contract (AIService) that every
AI backend must satisfy. The route layer only ever depends on this interface,
so swapping in a real model later requires adding a new class here and
updating the dependency-injection wiring in main.py — nothing else changes.
"""

from __future__ import annotations

import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


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

    # Prefix added to every answer so callers can tell at a glance this is
    # not a real model response.
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
