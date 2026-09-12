# Issue #3 — Backend core and AI Service adapter

## Overview

Implements the minimal backend capable of receiving a student question, validating it, routing it through a pluggable AI Service adapter, and returning a normalised response.

The AI service is currently backed by `MockAIService` — a deterministic placeholder that returns a clearly-labelled stub answer. No changes to the route layer are needed once the real provider is decided in Issue #1; only a new class needs to be added.

---

## Project structure

```
backend/
├── ai_service.py      # AIService ABC, AIRequest/AIResponse, AIServiceError, MockAIService
├── main.py            # FastAPI app factory, Pydantic schemas, DI wiring, routes, error handlers
├── requirements.txt   # Pinned direct dependencies
└── tests/
    └── test_api.py    # 11 integration tests
```

---

## API contract

### `POST /api/v1/questions`

Accepts a student question, forwards it to the AI service, and returns a normalised answer.

**Request body**

| Field     | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `question` | string | ✅ Yes  | The academic question. Must be non-empty and non-blank. |
| `context`  | string | No       | Optional code snippet or surrounding context. |

```json
{
  "question": "Why does my binary search return -1 for a value that exists?",
  "context": "def binary_search(arr, target):\n    lo, hi = 0, len(arr)"
}
```

**200 OK — success**

```json
{
  "answer": "[MOCK RESPONSE — real AI provider not yet connected]\n\nYou asked: ...",
  "source": "mock",
  "metadata": {
    "provider": "MockAIService",
    "latency_ms": 0.05
  }
}
```

| Field | Description |
|-------|-------------|
| `answer` | Textual answer from the AI service. |
| `source` | Which backend produced the answer (`"mock"`, or a real provider tag later). |
| `metadata` | Provider-specific extras (latency, token counts, model version, etc.). |

**422 Unprocessable Entity — validation failure**

Returned when `question` is missing, empty, or whitespace-only.

```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "question"],
      "msg": "Value error, question must not be blank",
      "input": ""
    }
  ]
}
```

**502 Bad Gateway — AI service failure**

Returned when the AI service raises an `AIServiceError` (e.g. provider outage). Stack traces are never exposed to the caller.

```json
{
  "error": {
    "code": "AI_SERVICE_ERROR",
    "message": "The AI service failed to process the request. Please try again."
  }
}
```

**500 Internal Server Error — unexpected failure**

Returned for any unhandled exception. Full traceback is logged server-side only.

```json
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "An unexpected error occurred. Please try again later."
  }
}
```

---

### `GET /health`

Liveness probe. Returns `200 {"status": "ok"}` when the service is up.

---

## Architecture decisions

### AI Service as an abstract adapter

`AIService` is an abstract base class (ABC) in `backend/ai_service.py`. The route handler depends only on this interface — it never imports `MockAIService` directly. FastAPI's dependency injection system (`Depends`) wires the concrete implementation at startup.

```
Route handler
     │
     │  Depends(get_ai_service)
     ▼
  AIService  ◄──── MockAIService   (today)
  (ABC)      ◄──── RealAIService   (future, Issue #1)
```

**To plug in a real provider:**
1. Add a new class in `backend/ai_service.py` that extends `AIService` and implements `ask()`.
2. In `backend/main.py`, update `get_ai_service()` to return your new class.
3. That's it — the route handler, validation, and error handling are unchanged.

### Error taxonomy

| Scenario | HTTP code | Rationale |
|----------|-----------|-----------|
| Invalid request payload | 422 | Standard FastAPI/Pydantic validation response. |
| AI provider call fails | 502 | The AI service is a downstream dependency; 502 (Bad Gateway) distinguishes provider outages from application bugs. |
| Unexpected exception | 500 | Catch-all; full traceback logged server-side, never exposed to the caller. |

### Judgment calls

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Field name | `context` (not `code_or_context`) | Shorter, more general, reads naturally in JSON. |
| Whitespace stripping | Validator trims `question` before forwarding | Prevents `"   "` from passing validation but arriving at the model as empty-ish input. |
| Endpoint versioning | `/api/v1/questions` | `v1` prefix lets the team evolve the contract without breaking existing clients. |

---

## Smoke-test commands

```bash
# Liveness
curl http://localhost:8000/health

# Valid question only
curl -s -X POST http://localhost:8000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"What is a binary search tree?\"}" | python -m json.tool

# Valid question + context
curl -s -X POST http://localhost:8000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"Why does this loop run forever?\", \"context\": \"while True:\\n    pass\"}" \
  | python -m json.tool

# Validation error (empty question → 422)
curl -s -X POST http://localhost:8000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"\"}" | python -m json.tool
```

---

## Acceptance criteria

| Criterion | Status | How it is satisfied |
|-----------|--------|---------------------|
| Backend starts and listens | ✅ | `uvicorn backend.main:app --port 8000` |
| Payload received and validated | ✅ | Pydantic v2 schema + `@field_validator` for blank strings |
| AI Service processes the input | ✅ | `MockAIService` injected via `Depends(get_ai_service)` |
| Errors handled with clear responses | ✅ | `AIServiceError` → 502, unhandled → 500; no stack traces in responses |
| Extensible to plug in real model | ✅ | Add class in `ai_service.py`, change one line in `get_ai_service()` |
