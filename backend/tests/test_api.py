"""
Integration tests for the TutorOn backend API.

Each test uses the FastAPI TestClient (backed by httpx) so the full
request/response cycle — validation, dependency injection, exception
handlers — is exercised without starting a real server.

Test scenarios covered:
- Valid request with question only → 200 with mock answer.
- Valid request with question + context → 200 with context reflected in answer.
- Missing ``question`` field → 422 validation error.
- Empty ``question`` string → 422 validation error.
- Blank (whitespace-only) ``question`` → 422 validation error.
- AI service raising :class:`AIServiceError` → 502 clean error response.
- AI service raising an unexpected exception → 500 clean error response.
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from backend.ai_service import AIRequest, AIResponse, AIService, AIServiceError
from backend.main import create_app


# ---------------------------------------------------------------------------
# Helpers / stubs
# ---------------------------------------------------------------------------


class AlwaysFailAIService(AIService):
    """
    Stub that always raises :class:`AIServiceError`.

    Used to verify that the route layer handles downstream failures gracefully
    and never leaks internal details to the caller.
    """

    def ask(self, request: AIRequest) -> AIResponse:
        """Unconditionally simulate a provider failure."""
        raise AIServiceError("Simulated provider outage")


class AlwaysCrashAIService(AIService):
    """
    Stub that raises a generic :class:`RuntimeError`.

    Used to verify that the global catch-all exception handler returns a
    clean 500 response even for completely unexpected errors.
    """

    def ask(self, request: AIRequest) -> AIResponse:
        """Unconditionally simulate an unexpected crash."""
        raise RuntimeError("Unexpected internal error")


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def client() -> TestClient:
    """
    Return a test client wired to the default MockAIService.

    Using ``create_app()`` (the factory) rather than importing the module-level
    ``app`` instance ensures each test starts with a clean application state.
    """
    return TestClient(create_app(), raise_server_exceptions=False)


@pytest.fixture()
def failing_client() -> TestClient:
    """Return a test client whose AI service always raises AIServiceError."""
    return TestClient(create_app(ai_service_override=AlwaysFailAIService()), raise_server_exceptions=False)


@pytest.fixture()
def crashing_client() -> TestClient:
    """Return a test client whose AI service always raises RuntimeError."""
    return TestClient(create_app(ai_service_override=AlwaysCrashAIService()), raise_server_exceptions=False)


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------


class TestAskQuestion:
    """Tests for the POST /api/v1/questions happy path."""

    def test_valid_question_returns_200_with_mock_answer(self, client: TestClient) -> None:
        """A well-formed request returns HTTP 200 and a clearly labelled mock answer."""
        response = client.post(
            "/api/v1/questions",
            json={"question": "What is a binary search tree?"},
        )

        assert response.status_code == 200
        body = response.json()
        assert "answer" in body
        assert "source" in body
        assert "metadata" in body
        # The mock must self-identify so it is never confused with a real response.
        assert body["source"] == "mock"
        assert "[MOCK RESPONSE" in body["answer"]

    def test_valid_question_with_context_returns_200(self, client: TestClient) -> None:
        """A request with both question and context is accepted and processed."""
        response = client.post(
            "/api/v1/questions",
            json={
                "question": "Why does this loop run forever?",
                "context": "while True:\n    pass",
            },
        )

        assert response.status_code == 200
        body = response.json()
        assert body["source"] == "mock"
        # The mock echoes context length — verify context was forwarded.
        assert "context provided" in body["answer"]

    def test_response_schema_contains_expected_fields(self, client: TestClient) -> None:
        """The response always contains answer, source, and metadata fields."""
        response = client.post(
            "/api/v1/questions",
            json={"question": "What is recursion?"},
        )

        body = response.json()
        assert set(body.keys()) >= {"answer", "source", "metadata"}
        assert isinstance(body["metadata"], dict)


# ---------------------------------------------------------------------------
# Validation errors
# ---------------------------------------------------------------------------


class TestValidation:
    """Tests for input validation — all should return 422."""

    def test_missing_question_field_returns_422(self, client: TestClient) -> None:
        """A payload with no 'question' key must be rejected with 422."""
        response = client.post("/api/v1/questions", json={})
        assert response.status_code == 422

    def test_empty_question_string_returns_422(self, client: TestClient) -> None:
        """An empty string for 'question' must be rejected with 422."""
        response = client.post(
            "/api/v1/questions",
            json={"question": ""},
        )
        assert response.status_code == 422

    def test_whitespace_only_question_returns_422(self, client: TestClient) -> None:
        """A whitespace-only 'question' must be rejected with 422."""
        response = client.post(
            "/api/v1/questions",
            json={"question": "   "},
        )
        assert response.status_code == 422

    def test_null_question_returns_422(self, client: TestClient) -> None:
        """A null 'question' must be rejected with 422."""
        response = client.post(
            "/api/v1/questions",
            json={"question": None},
        )
        assert response.status_code == 422

    def test_context_is_truly_optional(self, client: TestClient) -> None:
        """A request without 'context' must succeed — it is always optional."""
        response = client.post(
            "/api/v1/questions",
            json={"question": "What is polymorphism?"},
        )
        assert response.status_code == 200


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------


class TestErrorHandling:
    """Tests for downstream error scenarios."""

    def test_ai_service_error_returns_502(self, failing_client: TestClient) -> None:
        """An AIServiceError from the provider must surface as a clean 502."""
        response = failing_client.post(
            "/api/v1/questions",
            json={"question": "What is a deadlock?"},
        )

        assert response.status_code == 502
        body = response.json()
        assert "error" in body
        assert body["error"]["code"] == "AI_SERVICE_ERROR"
        # Stack traces must never reach the caller.
        assert "Traceback" not in body["error"]["message"]

    def test_unexpected_exception_returns_500(self, crashing_client: TestClient) -> None:
        """An unexpected RuntimeError must surface as a clean 500, not a raw traceback."""
        response = crashing_client.post(
            "/api/v1/questions",
            json={"question": "What is a stack overflow?"},
        )

        assert response.status_code == 500
        body = response.json()
        assert "error" in body
        assert body["error"]["code"] == "INTERNAL_ERROR"
        assert "Traceback" not in body["error"]["message"]


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------


class TestHealthCheck:
    """Tests for the /health liveness probe."""

    def test_health_returns_200_ok(self, client: TestClient) -> None:
        """The health endpoint must return 200 {"status": "ok"} when the service is up."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
