# TutorON

TutorOn AI is an automated micro-tutoring platform focused on unblocking university students who are stuck on bugs or practical problems, replacing the wait for a human tutor with an intelligent assistant available 24/7.

---

## Getting started

### Prerequisites

- Python 3.11 or newer

### Setup

```bash
# Create and activate a virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

# Install backend dependencies
pip install -r backend/requirements.txt
```

### Run the server

```bash
uvicorn backend.main:app --reload --port 8000
```

- API base URL: http://localhost:8000
- Interactive docs (Swagger UI): http://localhost:8000/docs

### Run the tests

```bash
pytest backend/tests/ -v
```

---

## Documentation

Per-issue technical documentation lives in [`docs/`](docs/):

| Issue | Title |
|-------|-------|
| [#3](docs/issue-3-backend-ai-service.md) | Backend core and AI Service adapter |
| [#5](docs/issue-5-frontend-cli.md) | Frontend CLI |
