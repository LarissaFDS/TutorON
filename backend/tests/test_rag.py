"""Exercise the real RAG pipeline and route; mock only external service I/O."""

from types import SimpleNamespace
from unittest.mock import Mock, call

import httpx
import pytest
from fastapi.testclient import TestClient
from google.genai import errors, types
from postgrest.exceptions import APIError as SupabaseAPIError

from backend import ai_service, gemini, rag
from backend.errors import ConfigurationError
from backend.main import create_app


def api_error(code):
    return errors.APIError(code, {"error": {"code": code, "message": "simulated failure"}})


@pytest.fixture
def pipeline(monkeypatch):
    monkeypatch.setenv("GEMINI_MODEL", "primary")
    monkeypatch.setenv("GEMINI_FALLBACK_MODEL", "fallback")
    sleep = Mock()
    monkeypatch.setattr(gemini.time, "sleep", sleep)
    monkeypatch.setattr(gemini.random, "uniform", lambda *_: 0)
    google = Mock()
    google.models.embed_content.return_value = types.EmbedContentResponse(
        embeddings=[types.ContentEmbedding(values=[0.1] * 1536)]
    )
    google.models.generate_content.return_value = SimpleNamespace(text="Grounded answer")
    database = Mock()
    database.rpc.return_value.execute.return_value = SimpleNamespace(
        data=[{"page_number": 7, "content": "Unique course material about recursion."}]
    )
    monkeypatch.setattr(ai_service, "get_gemini_client", lambda: google)
    monkeypatch.setattr(rag, "get_gemini_client", lambda: google)
    monkeypatch.setattr(rag, "get_supabase_client", lambda: database)
    return SimpleNamespace(google=google, database=database, sleep=sleep,
                           client=TestClient(create_app(), raise_server_exceptions=False))


def ask(pipeline):
    return pipeline.client.post("/api/v1/questions", json={
        "question": "Explain recursion", "context": "student's code",
    })


def test_full_rag_endpoint_uses_embedding_rpc_and_context(pipeline):
    response = ask(pipeline)
    assert response.status_code == 200
    assert response.json()["source"] == "gemini-rag"
    assert response.json()["metadata"]["chunks_used"] == 1
    embedding = pipeline.google.models.embed_content.call_args.kwargs
    assert embedding["model"] == "gemini-embedding-001"
    assert embedding["config"].task_type == "RETRIEVAL_QUERY"
    assert embedding["config"].output_dimensionality == 1536
    pipeline.database.rpc.assert_called_once_with(
        "match_chunks", {"query_embedding": [0.1] * 1536, "match_count": 3}
    )
    prompt = pipeline.google.models.generate_content.call_args.kwargs["contents"]
    assert "Unique course material" in prompt
    assert "[Página 7]" in prompt
    assert "Explain recursion" in prompt
    assert "student's code" in prompt


@pytest.mark.parametrize("code", [429, 500, 502, 503, 504])
def test_transient_generation_recovers_on_same_model(pipeline, code):
    generate = pipeline.google.models.generate_content
    generate.side_effect = [api_error(code), api_error(code), SimpleNamespace(text="Recovered")]
    response = ask(pipeline)
    assert response.status_code == 200
    assert response.json()["metadata"]["fallback_used"] is False
    assert [c.kwargs["model"] for c in generate.call_args_list] == ["primary"] * 3
    assert pipeline.sleep.call_args_list == [call(0.5), call(1.0)]


def test_fallback_preserves_retrieved_context_without_repeating_retrieval(pipeline):
    generate = pipeline.google.models.generate_content
    generate.side_effect = [api_error(503)] * 3 + [SimpleNamespace(text="Fallback answer")]
    response = ask(pipeline)
    assert response.status_code == 200
    assert response.json()["metadata"]["model"] == "fallback"
    assert response.json()["metadata"]["fallback_used"] is True
    assert [c.kwargs["model"] for c in generate.call_args_list] == ["primary"] * 3 + ["fallback"]
    prompts = [c.kwargs["contents"] for c in generate.call_args_list]
    assert len(set(prompts)) == 1 and "Unique course material" in prompts[0]
    pipeline.database.rpc.assert_called_once()
    pipeline.google.models.embed_content.assert_called_once()


def test_exhausted_models_return_temporary_503(pipeline):
    pipeline.google.models.generate_content.side_effect = api_error(503)
    response = ask(pipeline)
    assert response.status_code == 503
    assert response.json()["error"]["code"] == "AI_TEMPORARILY_UNAVAILABLE"
    assert response.headers["Retry-After"] == "5"
    assert pipeline.google.models.generate_content.call_count == 6


@pytest.mark.parametrize("code", [400, 401, 403, 404])
def test_auth_configuration_errors_do_not_retry_or_fallback(pipeline, code):
    pipeline.google.models.generate_content.side_effect = api_error(code)
    response = ask(pipeline)
    assert response.status_code == 502
    assert response.json()["error"]["code"] == "GEMINI_REQUEST_ERROR"
    pipeline.google.models.generate_content.assert_called_once()
    pipeline.sleep.assert_not_called()


def test_embedding_503_recovers_without_changing_embedding_model(pipeline):
    embed = pipeline.google.models.embed_content
    embed.side_effect = [api_error(503), embed.return_value]
    assert ask(pipeline).status_code == 200
    assert [c.kwargs["model"] for c in embed.call_args_list] == ["gemini-embedding-001"] * 2


def test_embedding_exhaustion_never_bypasses_retrieval(pipeline):
    pipeline.google.models.embed_content.side_effect = api_error(503)
    assert ask(pipeline).status_code == 503
    pipeline.database.rpc.assert_not_called()
    pipeline.google.models.generate_content.assert_not_called()


@pytest.mark.parametrize("data", [[], None, [{"content": " "}], [{"page_number": 1}]])
def test_empty_or_invalid_context_never_generates_ungrounded_answer(pipeline, data):
    pipeline.database.rpc.return_value.execute.return_value.data = data
    response = ask(pipeline)
    assert response.status_code == 502
    assert response.json()["error"]["code"] == "RAG_ERROR"
    pipeline.google.models.generate_content.assert_not_called()


def test_supabase_failure_is_not_retried_as_gemini_failure(pipeline):
    pipeline.database.rpc.return_value.execute.side_effect = SupabaseAPIError({
        "message": "match_chunks is missing", "code": "PGRST202", "details": "", "hint": "",
    })
    response = ask(pipeline)
    assert response.status_code == 502
    assert response.json()["error"]["code"] == "RAG_ERROR"
    pipeline.sleep.assert_not_called()
    pipeline.google.models.generate_content.assert_not_called()


@pytest.mark.parametrize("stage", ["embedding", "generation", "retrieval"])
def test_programming_errors_remain_500(pipeline, stage):
    target = {"embedding": pipeline.google.models.embed_content,
              "generation": pipeline.google.models.generate_content,
              "retrieval": pipeline.database.rpc}[stage]
    target.side_effect = TypeError("programming bug")
    response = ask(pipeline)
    assert response.status_code == 500
    assert response.json()["error"]["code"] == "INTERNAL_ERROR"
    pipeline.sleep.assert_not_called()


def test_invalid_embedding_dimensions_stop_before_rpc(pipeline):
    pipeline.google.models.embed_content.return_value = types.EmbedContentResponse(
        embeddings=[types.ContentEmbedding(values=[0.1])]
    )
    assert ask(pipeline).json()["error"]["code"] == "RAG_ERROR"
    pipeline.database.rpc.assert_not_called()


def test_empty_answer_does_not_trigger_fallback(pipeline):
    pipeline.google.models.generate_content.return_value.text = " "
    assert ask(pipeline).status_code == 502
    pipeline.google.models.generate_content.assert_called_once()


def test_network_timeout_retries(pipeline):
    operation = Mock(side_effect=[httpx.ReadTimeout("timeout"), "ok"])
    assert gemini.call_gemini(operation, stage="generation", model="primary") == "ok"
    assert operation.call_count == 2


def test_no_duplicate_or_disabled_fallback(pipeline, monkeypatch):
    for fallback in ["", "primary"]:
        monkeypatch.setenv("GEMINI_FALLBACK_MODEL", fallback)
        pipeline.google.models.generate_content.reset_mock()
        pipeline.google.models.generate_content.side_effect = api_error(503)
        assert ask(pipeline).status_code == 503
        assert pipeline.google.models.generate_content.call_count == 3


def test_missing_configuration_has_distinct_error(pipeline, monkeypatch):
    monkeypatch.setattr(ai_service, "get_gemini_client", Mock(side_effect=ConfigurationError("missing")))
    response = ask(pipeline)
    assert response.status_code == 500
    assert response.json()["error"]["code"] == "CONFIGURATION_ERROR"


def test_sdk_internal_retries_disabled(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-placeholder")
    factory = Mock()
    monkeypatch.setattr(gemini.genai, "Client", factory)
    gemini.get_gemini_client.cache_clear()
    try:
        gemini.get_gemini_client()
        options = factory.call_args.kwargs["http_options"]
        assert options.retry_options.attempts == 1
        assert options.timeout == 10_000
    finally:
        gemini.get_gemini_client.cache_clear()
