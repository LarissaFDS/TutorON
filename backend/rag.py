from functools import lru_cache

import httpx
from google.genai import types
from postgrest.exceptions import APIError
from supabase import ClientOptions, create_client

from .config import required_env
from .errors import RAGError
from .gemini import call_gemini, get_gemini_client

# Must match the existing ingested vectors; changing this requires reindexing.
EMBEDDING_MODEL = "gemini-embedding-001"
EMBEDDING_DIMENSIONS = 1536


@lru_cache(maxsize=1)
def get_supabase_client():
    return create_client(
        required_env("SUPABASE_URL"),
        required_env("SUPABASE_KEY"),
        options=ClientOptions(postgrest_client_timeout=10),
    )


def generate_embedding(text: str, task_type: str) -> list[float]:
    gemini = get_gemini_client()
    response = call_gemini(
        lambda: gemini.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=text,
            config=types.EmbedContentConfig(
                task_type=task_type,
                output_dimensionality=EMBEDDING_DIMENSIONS,
            ),
        ),
        stage="embedding",
        model=EMBEDDING_MODEL,
    )
    if not response.embeddings or not response.embeddings[0].values:
        raise RAGError("Gemini returned an empty embedding")
    values = response.embeddings[0].values
    if len(values) != EMBEDDING_DIMENSIONS:
        raise RAGError(f"Expected {EMBEDDING_DIMENSIONS} embedding dimensions, got {len(values)}")
    return values


def search_context(question: str, limit: int = 3) -> list[dict]:
    supabase = get_supabase_client()
    embedding = generate_embedding(question, "RETRIEVAL_QUERY")
    try:
        response = supabase.rpc(
            "match_chunks",
            {"query_embedding": embedding, "match_count": limit},
        ).execute()
    except (APIError, httpx.HTTPError) as exc:
        raise RAGError("Supabase match_chunks retrieval failed") from exc

    chunks = response.data
    if not isinstance(chunks, list) or not chunks:
        raise RAGError("Supabase match_chunks returned no course material")
    if any(not isinstance(chunk, dict) or not isinstance(chunk.get("content"), str)
           or not chunk["content"].strip() for chunk in chunks):
        raise RAGError("Supabase match_chunks returned invalid or empty content")
    return chunks
