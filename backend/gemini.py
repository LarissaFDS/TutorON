"""Bounded retry policy shared by query embeddings and answer generation."""

import logging
import random
import time
from functools import lru_cache

import httpx
from google import genai
from google.genai import errors, types

from .config import required_env
from .errors import GeminiRequestError, GeminiUnavailableError

logger = logging.getLogger("tutoron.backend")
TRANSIENT_CODES = {429, 500, 502, 503, 504}
MAX_ATTEMPTS = 3


@lru_cache(maxsize=1)
def get_gemini_client():
    return genai.Client(
        api_key=required_env("GEMINI_API_KEY"),
        vertexai=False,
        http_options=types.HttpOptions(
            api_version="v1beta",
            timeout=10_000,
            # Retries are controlled here so SDK retries cannot multiply them.
            retry_options=types.HttpRetryOptions(attempts=1),
        ),
    )


def call_gemini(operation, *, stage: str, model: str):
    for attempt in range(MAX_ATTEMPTS):
        try:
            return operation()
        except errors.APIError as exc:
            if exc.code not in TRANSIENT_CODES:
                raise GeminiRequestError(
                    f"Gemini {stage} rejected model={model}, HTTP {exc.code}"
                ) from exc
            failure = exc
            reason = f"HTTP {exc.code}"
        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            failure = exc
            reason = type(exc).__name__

        logger.warning(
            "Gemini %s model=%s attempt=%s/%s failed: %s",
            stage, model, attempt + 1, MAX_ATTEMPTS, reason,
        )
        if attempt == MAX_ATTEMPTS - 1:
            raise GeminiUnavailableError(
                f"Gemini {stage} unavailable for model={model} after {MAX_ATTEMPTS} attempts"
            ) from failure
        time.sleep(0.5 * 2**attempt + random.uniform(0, 0.25))
