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
python -m pip install -r backend/requirements.txt
```

Create `.env` **in the repository root** by copying `.env.exemple`, then fill:

```dotenv
GEMINI_API_KEY=your-google-ai-studio-key
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-key
GEMINI_MODEL=gemini-3.8-flash
GEMINI_FALLBACK_MODEL=gemini-3.6-flash
```

Never commit `.env` or paste its contents into logs. It is ignored by Git.
The backend resolves `.env` relative to its source, independently of the working
directory; existing process environment variables take precedence. Restart the
backend after editing credentials or model settings.

The Supabase project must already have indexed course material and the
`match_chunks(query_embedding, match_count)` RPC, returning `content` and
`page_number`. The existing ingestion and retrieval use `gemini-embedding-001`
with **1536 dimensions**. Do not change the embedding model/dimensions without
reindexing. If material has not been loaded, place the course PDF at
`materials/disciplina.pdf` and run `python -m backend.ingest` from the root.
Ingestion writes documents/chunks; do not rerun it on an already populated demo
project unless you intend to add duplicate material. No schema migration is
performed by this hotfix.

### Run the server

```bash
python -m uvicorn backend.main:app --reload --port 8000
```

Run from the repository root. From another directory, use
`python -m uvicorn backend.main:app --app-dir /absolute/path/to/TutorON --port 8000`.

- API base URL: http://localhost:8000
- Interactive docs (Swagger UI): http://localhost:8000/docs

### Run the tests

```bash
python -m pytest backend/tests/ -v
```

Tests do not need credentials or make external API calls. They cover the RAG
pipeline with mocked external I/O, transient retries, grounded fallback, and
separate configuration, authentication, Supabase and programming failures.

### Live pre-presentation check

With `.env` filled and the server running, use a second terminal from the root:

```bash
python -m backend.smoke_check
```

This makes real API calls (normal Gemini quota/billing applies). It independently
checks configuration, Gemini authentication and account-visible model actions,
1536-dimensional embeddings, `match_chunks`, grounded generation, and the HTTP
endpoint. It prints no credentials and does not write to Supabase. Use
`--question "Your course question"` or `--base-url http://127.0.0.1:8001` if needed.

PowerShell endpoint test:

```powershell
$body = @{ question = 'Qual é o assunto principal do material da disciplina? Cite a página usada.' } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/v1/questions -ContentType 'application/json; charset=utf-8' -Body ([System.Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 120
```

### Gemini overload handling

Google's [model catalog](https://ai.google.dev/gemini-api/docs/models) lists both
configured models; actual account access is checked by `smoke_check` using the
installed Google GenAI SDK (`google-genai==2.8.0`, Gemini Developer API `v1beta`).
The primary model remains configurable. If it is persistently busy, set
`GEMINI_MODEL` to a model verified by the live check, and choose another available
model as `GEMINI_FALLBACK_MODEL`. Leave the fallback blank to disable it.

Each embedding/generation operation has at most three attempts for HTTP
429/500/502/503/504 and network/timeouts, with 0.5s then 1s exponential delays plus
up to 0.25s jitter. Each Gemini request has a 10s timeout; SDK retries are disabled
to avoid multiplying attempts. After transient generation exhaustion, the fallback
gets the **same prompt and retrieved chunks**. Embeddings never switch models.
Supabase has a 10s request timeout. The CLI allows 120s for the backend's retries.
The synchronous route runs in FastAPI's worker pool so retries do not block the
event loop. These are per-request transport timeouts, not a hard total deadline.

- Exhausted temporary Gemini failures: HTTP **503**, `AI_TEMPORARILY_UNAVAILABLE`,
  `Retry-After: 5`.
- Gemini rejection (including authentication/invalid models): HTTP **502**,
  `GEMINI_REQUEST_ERROR`; no retries or fallback.
- Supabase errors, empty/malformed retrieval or invalid embeddings: HTTP **502**,
  `RAG_ERROR`; never generate without course material.
- Missing local configuration: HTTP **500**, `CONFIGURATION_ERROR`.
- Programming errors: HTTP **500**, `INTERNAL_ERROR`, with a server-side traceback.

Success metadata includes `model`, `fallback_used`, `chunks_used` and `latency_ms`.
No fallback can guarantee availability if Gemini is broadly unavailable or quota
is exhausted. `/health` is a liveness check; use the live smoke check for readiness.

---

## Documentation

Per-issue technical documentation lives in [`docs/`](docs/):

| Issue | Title |
|-------|-------|
| [#3](docs/issue-3-backend-ai-service.md) | Backend core and AI Service adapter |
| [#5](docs/issue-5-frontend-cli.md) | Frontend CLI |
