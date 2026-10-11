# TutorON

TutorOn AI is an automated micro-tutoring platform focused on unblocking university students who are stuck on bugs or practical problems, replacing the wait for a human tutor with an intelligent assistant available 24/7.

---

## Getting started

### Prerequisites

- Python 3.11 or newer
- [Ollama](https://ollama.com/download) installed and running locally — used to generate
  document/query embeddings with the `bge-m3` model (no API key or internet access needed
  for this step; the generative answers still go through the Gemini API)
- A Gemini API key (for `GEMINI_API_KEY`) and a Supabase project with `pgvector` enabled
  (for `SUPABASE_URL` / `SUPABASE_KEY`)

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

# Pull the embedding model used by ingest.py / rag.py (one-time, ~2.2 GB download)
ollama pull bge-m3
```

Copy `.env.exemple` to `.env` and fill in `GEMINI_API_KEY`, `SUPABASE_URL` and
`SUPABASE_KEY`.

The Supabase `chunks` table must store embeddings as `vector(1024)` (bge-m3's native
dimensionality) — see [backend/ingest.py](backend/ingest.py) and
[backend/rag.py](backend/rag.py) for how embeddings are generated and queried.

### Ingest course material

Before asking questions, ingest the PDF referenced by `PDF_PATH` in
[backend/ingest.py](backend/ingest.py) into Supabase (requires Ollama running locally
with `bge-m3` pulled):

```bash
python backend/ingest.py
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
