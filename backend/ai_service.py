from __future__ import annotations

import logging
import time

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from .config import generation_models
from .errors import AIServiceError, GeminiUnavailableError
from .gemini import call_gemini, get_gemini_client

from .rag import search_context


logger = logging.getLogger("tutoron.backend")


# =========================================================
# Request / Response
# =========================================================

@dataclass
class AIRequest:

    question: str

    context: str | None = None


@dataclass
class AIResponse:

    answer: str

    source: str

    metadata: dict = field(default_factory=dict)


# =========================================================
# Interface
# =========================================================

class AIService(ABC):

    @abstractmethod
    def ask(
        self,
        request: AIRequest
    ) -> AIResponse:

        raise NotImplementedError


# =========================================================
# Gemini + RAG
# =========================================================

class GeminiAIService(AIService):

    def __init__(self):

        self.models = generation_models()
        self.client = get_gemini_client()

    def ask(
        self,
        request: AIRequest
    ) -> AIResponse:

        start = time.perf_counter()

        # ---------------------------------------------
        # 1. Buscar contexto no Supabase
        # ---------------------------------------------

        chunks = search_context(
            request.question,
            limit=3
        )

        # ---------------------------------------------
        # 2. Montar contexto
        # ---------------------------------------------

        context_parts = []

        for chunk in chunks:

            page = chunk.get(
                "page_number"
            )

            content = chunk.get(
                "content",
                ""
            )

            context_parts.append(
                f"[Página {page}]\n{content}"
            )

        context = "\n\n".join(
            context_parts
        )

        # ---------------------------------------------
        # 3. Prompt
        # ---------------------------------------------

        prompt = f"""
Você é um tutor universitário.

Sua função é ajudar o aluno a compreender
o conteúdo da disciplina.

Use prioritariamente o material fornecido
abaixo para responder.

Não invente informações que não estejam
no material.

Se a pergunta não puder ser respondida
com base no material fornecido, diga
claramente:

"Não encontrei essa informação no
material da disciplina."

Material da disciplina:

-------------------------
{context}
-------------------------

Pergunta do aluno:

{request.question}

Contexto adicional do aluno (não substitui o material da disciplina):
{request.context or "Não fornecido."}
"""

        # ---------------------------------------------
        # 4. Gemini
        # ---------------------------------------------

        for index, model in enumerate(self.models):
            try:
                response = call_gemini(
                    lambda: self.client.models.generate_content(
                        model=model, contents=prompt,
                    ),
                    stage="generation", model=model,
                )
                break
            except GeminiUnavailableError:
                if index == len(self.models) - 1:
                    raise
                logger.warning("Gemini generation exhausted retries; switching from %s to %s",
                               model, self.models[index + 1])

        if not response.text or not response.text.strip():
            raise AIServiceError(
                "Gemini returned an empty response"
            )

        elapsed_ms = round(
            (time.perf_counter() - start) * 1000,
            2
        )

        # ---------------------------------------------
        # 5. Resposta
        # ---------------------------------------------

        return AIResponse(
            answer=response.text,
            source="gemini-rag",
            metadata={
                "chunks_used": len(chunks),
                "model": model,
                "fallback_used": index > 0,
                "latency_ms": elapsed_ms,
            },
        )
