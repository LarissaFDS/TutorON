# TutorON

TutorOn AI is an automated micro-tutoring platform focused on unblocking university students who are stuck on bugs or practical problems, replacing the wait for a human tutor with an intelligent assistant available 24/7.

---

## Backend — Issue #3

Minimal FastAPI backend that accepts a student question, routes it through a pluggable AI service adapter, and returns a normalised answer.

> **Note:** The AI service is currently backed by `MockAIService` (a deterministic placeholder). The real provider will be wired in once Issue #1 (AI strategy) is resolved — no backend changes needed beyond adding the new class.

### Project structure

```
backend/
├── ai_service.py      # AIService ABC, AIRequest/AIResponse, MockAIService
├── main.py            # FastAPI app factory, schemas, DI wiring, routes
├── requirements.txt   # Direct dependencies only
└── tests/
    └── test_api.py    # Integration tests (pytest + httpx)
```

### Prerequisites

- Python 3.11 or newer
- `pip` (or any venv manager you prefer)

### Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

# 2. Install dependencies
pip install -r backend/requirements.txt
```

### Run the server

```bash
# From the repository root, with the venv active:
uvicorn backend.main:app --reload --port 8000
```

The server starts at <http://localhost:8000>.  
Interactive API docs (Swagger UI) are at <http://localhost:8000/docs>.

### Smoke test (curl)

**Liveness probe:**
```bash
curl http://localhost:8000/health
# → {"status":"ok"}
```

**Valid question (question only):**
```bash
curl -s -X POST http://localhost:8000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d '{"question": "What is a binary search tree?"}' | python -m json.tool
```

**Valid question with context:**
```bash
curl -s -X POST http://localhost:8000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d '{"question": "Why does this loop run forever?", "context": "while True:\n    pass"}' \
  | python -m json.tool
```

**Validation error (empty question → 422):**
```bash
curl -s -X POST http://localhost:8000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d '{"question": ""}' | python -m json.tool
```

### Run the tests

```bash
# From the repository root, with the venv active:
pytest backend/tests/ -v
```

Expected output: all tests pass (green).

### API contract

#### `POST /api/v1/questions`

**Request body**

| Field      | Type   | Required | Description                                      |
|------------|--------|----------|--------------------------------------------------|
| `question` | string | ✅ Yes   | The academic question. Must be non-empty.        |
| `context`  | string | No       | Optional code snippet or surrounding context.    |

**Success response — 200**

```json
{
  "answer": "...",
  "source": "mock",
  "metadata": {
    "provider": "MockAIService",
    "latency_ms": 0.05
  }
}
```

**Error response — 422 (validation)**

```json
{
  "detail": [...]
}
```

**Error response — 502 (AI service failure)**

```json
{
  "error": {
    "code": "AI_SERVICE_ERROR",
    "message": "The AI service failed to process the request. Please try again."
  }
}
```

**Error response — 500 (unexpected)**

```json
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "An unexpected error occurred. Please try again later."
  }
}
```

#### `GET /health`

Returns `{"status": "ok"}` when the service is up.

---

### Plugging in a real AI provider (future work)

1. Add a new class in `backend/ai_service.py` that extends `AIService` and implements `ask()`.
2. In `backend/main.py`, update `get_ai_service()` to return your new class.
3. That's it — the route handler, validation, and error handling are unchanged.
