"""Read-only live checks. Run after starting Uvicorn; never prints credentials."""

import argparse

import httpx

from .ai_service import AIRequest, GeminiAIService
from .config import ENV_PATH, generation_models, required_env
from .gemini import call_gemini, get_gemini_client
from .rag import EMBEDDING_MODEL, generate_embedding, get_supabase_client


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    parser.add_argument("--question", default="Qual é o assunto principal do material da disciplina? Cite a página usada.")
    args = parser.parse_args()
    stage = "environment"
    try:
        for name in ("GEMINI_API_KEY", "SUPABASE_URL", "SUPABASE_KEY"):
            required_env(name)
        print(f"PASS environment: {ENV_PATH} (deployment variables take precedence)", flush=True)

        stage = "Gemini authentication / model listing"
        client = get_gemini_client()
        models = call_gemini(lambda: list(client.models.list()), stage="model listing", model="catalog")
        available = {m.name.removeprefix("models/"): m.supported_actions or [] for m in models}
        for model in generation_models():
            if "generateContent" not in available.get(model.removeprefix("models/"), []):
                raise RuntimeError(f"Configured generation model not available: {model}")
        if "embedContent" not in available.get(EMBEDDING_MODEL, []):
            raise RuntimeError("Required embedding model not available")
        print("PASS authentication; available generation models:", flush=True)
        print(", ".join(name for name, actions in available.items() if "generateContent" in actions), flush=True)

        stage = "embedding"
        embedding = generate_embedding(args.question, "RETRIEVAL_QUERY")
        print(f"PASS embedding: {len(embedding)} dimensions", flush=True)

        stage = "Supabase match_chunks"
        chunks = get_supabase_client().rpc("match_chunks", {
            "query_embedding": embedding, "match_count": 3,
        }).execute().data
        if not chunks or any(not chunk.get("content", "").strip() for chunk in chunks):
            raise RuntimeError("No usable indexed course material")
        print(f"PASS match_chunks: {len(chunks)} chunks, pages {[c.get('page_number') for c in chunks]}", flush=True)

        stage = "grounded Gemini generation"
        result = GeminiAIService().ask(AIRequest(args.question))
        print(f"PASS generation: {result.metadata}", flush=True)
        print(result.answer, flush=True)

        stage = "HTTP /api/v1/questions"
        response = httpx.post(args.base_url.rstrip("/") + "/api/v1/questions",
                              json={"question": args.question}, timeout=120)
        response.raise_for_status()
        body = response.json()
        if not body.get("answer") or body.get("source") != "gemini-rag" or body["metadata"]["chunks_used"] < 1:
            raise RuntimeError("Endpoint did not return a grounded answer")
        print(f"PASS HTTP {response.status_code}: {body['metadata']}", flush=True)
    except Exception as exc:
        # No raw provider payloads/URLs: they can contain account information.
        code = getattr(exc, "code", None)
        status = getattr(getattr(exc, "response", None), "status_code", None)
        print(f"FAIL {stage}: {type(exc).__name__}; code={code}; HTTP={status}", flush=True)
        print("Check the failing stage's configuration and backend logs.", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
