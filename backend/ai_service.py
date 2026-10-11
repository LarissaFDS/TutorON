from __future__ import annotations

import os
import time

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from dotenv import load_dotenv
from google import genai
from google.genai import errors as genai_errors

from .rag import search_context


load_dotenv()


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
# Errors
# =========================================================

class AIServiceError(Exception):
    pass


# =========================================================
# Gemini + RAG
# =========================================================

GEMINI_MODELS = [
    "gemini-3.8-flash",
    "gemini-flash-latest",
    "gemini-3.7-flash",
    "gemini-flash-lite-latest",
]


class GeminiAIService(AIService):

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def ask(
        self,
        request: AIRequest
    ) -> AIResponse:

        start = time.perf_counter()

        try:

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
"""

            # ---------------------------------------------
            # 4. Gemini (com fallback entre modelos)
            # ---------------------------------------------

            response = None
            used_model = None
            errors_by_model: dict[str, str] = {}

            for model in GEMINI_MODELS:

                try:

                    response = self.client.models.generate_content(
                        model=model,
                        contents=prompt,
                    )

                    if response.text is None:
                        raise AIServiceError(
                            f"{model} returned an empty response"
                        )

                    used_model = model
                    break

                except (genai_errors.APIError, AIServiceError) as exc:

                    errors_by_model[model] = str(exc)
                    continue

            if response is None or used_model is None:

                raise AIServiceError(
                    "Nenhum modelo Gemini disponível no momento "
                    f"(tentados: {list(errors_by_model.keys())}). "
                    f"Erros: {errors_by_model}"
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
                    "latency_ms": elapsed_ms,
                    "model_used": used_model,
                    "fallback_errors": errors_by_model or None,
                },
            )

        except AIServiceError:

            raise

        except Exception as exc:

            raise AIServiceError(
                f"Gemini/RAG error: {exc}"
            ) from exc