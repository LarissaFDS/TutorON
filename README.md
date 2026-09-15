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

### Configuração da IA

Para usar o serviço de IA real (Google Gemini):
1. Copie o arquivo `.env.example` para `.env`.
2. Preencha a variável `TUTORON_LLM_API_KEY` com a sua chave. Você pode obter uma chave gratuita acessando o [Google AI Studio](https://aistudio.google.com/) (basta fazer login com sua conta Google, sem necessidade de cartão de crédito). (**Aviso:** a chave real nunca deve ser commitada no repositório).
3. Para rodar a aplicação ou a suíte de testes sem uma chave de API (útil para desenvolvimento local e CI), configure a variável `TUTORON_AI_PROVIDER=mock`.

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
