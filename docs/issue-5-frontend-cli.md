# Issue #4 — Frontend CLI

## Overview

The frontend CLI has been implemented, and the HTTP client follows the backend API contract. The end-to-end integration with the backend is prepared but remains pending validation by the integration/testing task.

The TutorOn CLI provides the initial human interaction layer for the Mini MVP, allowing a student to submit an academic question and optional context through the terminal. The frontend implementation is complete for its current scope. The API client is structured according to the existing backend contract, while end-to-end integration is a separate project responsibility and has not yet been marked as complete.

The CLI is completely decoupled from the AI implementation. It prepares data according to the API contract and is unaware of internal backend services such as `MockAIService`.

## Project structure

The frontend implementation is deliberately kept minimal and divided by responsibility:

```text
frontend/
├── cli.py            # Terminal user interface, input validation, and interaction flow
└── api_client.py     # HTTP communication layer, payload construction, and error parsing
```

## CLI architecture

The architecture enforces a strict separation of concerns between the user interface and backend communication:

```text
┌──────────────┐
│     User     │
└──────┬───────┘
       │ Terminal I/O
       ▼
┌──────────────┐
│   CLI Layer  │  cli.py
└──────┬───────┘
       │ Function calls
       ▼
┌──────────────┐
│  API Client  │  api_client.py
└──────┬───────┘
       │ HTTP POST /api/v1/questions
       ▼
┌──────────────┐
│   Backend    │  FastAPI
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  AI Service  │  MockAIService
└──────────────┘
```

* The frontend knows the API contract.
* The frontend does not know about `AIService`, `MockAIService`, or the internal AI model.

## User flow

The designed and prepared flow for the application is:

1. **Student** starts the application.
2. **CLI** displays the TutorOn header and asks for the student's question.
3. **CLI** asks for optional context or code.
4. **API Client** prepares the payload and sends an HTTP request.
5. **Backend API** receives the request and routes it to the AI Service.
6. **Response** is returned to the API Client and displayed by the CLI.

> **Note:** The frontend implements the CLI and API client portions of this flow. End-to-end execution is pending integration validation.

## API integration

The frontend includes a dedicated HTTP communication layer in `api_client.py`.

The API client is implemented according to the existing TutorOn backend contract and is responsible for preparing requests, sending HTTP calls, parsing responses, and translating communication errors.

The end-to-end integration with the backend is not considered complete in this issue. Final validation of the complete Frontend → Backend → AI Service flow is handled separately by the project's integration/testing task.

* **Library:** `httpx` for synchronous HTTP communication.
* **Base URL:** Read from the `TUTORON_BACKEND_URL` environment variable.
* **Default URL:** `http://localhost:8000`.
* **Endpoint:** `POST /api/v1/questions`.
* **Timeout:** 30 seconds.

## API contract

The API client follows the existing backend contract.

### Request

`POST /api/v1/questions`

| Field      | Type   | Required | Description                                    |
| ---------- | ------ | -------- | ---------------------------------------------- |
| `question` | string | Yes      | Academic question. Must not be empty or blank. |
| `context`  | string | No       | Optional code snippet or additional context.   |

Example:

```json
{
  "question": "Why does my binary search return -1 for a value that exists?",
  "context": "def binary_search(arr, target):\n    lo, hi = 0, len(arr)"
}
```

### Success response

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

* **`answer`:** Text to be displayed to the student.
* **`source`:** Identifies the backend provider that produced the response.
* **`metadata`:** Informational provider data. The frontend does not depend on specific metadata fields.

### Errors handled

* **422 Unprocessable Entity:** Validation error, such as a missing or blank question.
* **502 Bad Gateway:** AI service failure.
* **500 Internal Server Error:** Unexpected backend failure.

## Configuration

The backend URL can be configured through the `TUTORON_BACKEND_URL` environment variable.

Default:

```text
http://localhost:8000
```

Linux/macOS:

```bash
export TUTORON_BACKEND_URL="http://127.0.0.1:8080"
```

Windows PowerShell:

```powershell
$env:TUTORON_BACKEND_URL="http://127.0.0.1:8080"
```

## Error handling

The frontend handles HTTP and network errors by displaying user-friendly messages instead of raw tracebacks.

* **HTTP 422:** Displays a validation warning.
* **HTTP 502:** Displays a friendly AI service failure message.
* **HTTP 500:** Displays a generic internal server error.
* **Connection refused:** Informs the user that the backend could not be reached.
* **Timeout:** Informs the user that the backend took too long to respond.
* **Invalid JSON:** Reports an invalid response from the server.

## How to run locally

The project dependencies should be installed according to the global project documentation.

### Terminal 1 — Backend

```bash
uvicorn backend.main:app --reload --port 8000
```

### Terminal 2 — Frontend CLI

```bash
python frontend/cli.py
```

> The commands above describe the expected local execution flow for the frontend/backend pair. End-to-end integration remains pending formal validation by the integration/testing task.

## Usage example

The following example represents the expected CLI behavior using the backend's current `MockAIService`. It is not evidence that end-to-end integration has already been validated.

### Example with multi-line context

```text
========================================
              TutorOn AI
         Seu tutor acadêmico
========================================

Digite sua dúvida:
> Por que meu código não funciona?

Digite código ou contexto adicional (opcional, pressione Enter para pular):
> def soma(a, b):
>     return a - b
>

Processando sua dúvida...

========================================
          Resposta do TutorOn
========================================

[MOCK RESPONSE — real AI provider not yet connected]

You asked: "Por que meu código não funciona?" (context provided: 27 chars)

========================================
[Fonte da resposta: mock]
========================================
```

### Example skipping context

```text
Digite sua dúvida:
> quanto é 5 * 8

Digite código ou contexto adicional (opcional, pressione Enter para pular):
>

Processando sua dúvida...
```

## Testing

The frontend implementation has been validated at the CLI/client level for the scenarios currently covered by the implementation.

The following scenarios should be validated during the integration stage:

* Sending a question without context.
* Sending a question with multi-line context.
* Submitting an empty question.
* Handling a stopped backend.
* Handling HTTP 422 responses.
* Handling HTTP 502 responses.
* Handling HTTP 500 responses.

End-to-end validation against the running FastAPI backend is part of the project's integration/testing task and is not considered complete by this issue alone.

## Architecture decisions

| Decision                   | Choice                                  | Rationale                                                                     |
| -------------------------- | --------------------------------------- | ----------------------------------------------------------------------------- |
| Interface type             | CLI                                     | Keeps the 4-day MVP focused on the core interaction.                          |
| Communication              | HTTP                                    | Matches the existing FastAPI backend contract.                                |
| HTTP client                | `httpx`                                 | Lightweight and appropriate for the CLI.                                      |
| Separation                 | CLI + API client                        | Keeps user interaction separate from HTTP communication.                      |
| Backend URL                | Environment variable with local default | Avoids hardcoding the backend address throughout the code.                    |
| Web frontend               | Out of MVP                              | Avoids unnecessary implementation effort.                                     |
| Integration responsibility | Separate integration task               | Keeps frontend implementation independent from end-to-end project validation. |

## Acceptance criteria

| Criterion                                    | Status     | How it is satisfied                                                                 |
| -------------------------------------------- | ---------- | ----------------------------------------------------------------------------------- |
| CLI starts                                   | ✅          | Frontend CLI implementation is available.                                           |
| Student can enter a question                 | ✅          | CLI provides question input and local validation.                                   |
| Context is optional                          | ✅          | CLI supports skipping context and multi-line context input.                         |
| API client is implemented                    | ✅          | HTTP communication is isolated in `api_client.py`.                                  |
| API contract is respected                    | ✅          | Client follows `POST /api/v1/questions` and the documented request/response schema. |
| Error handling is implemented                | ✅          | Client handles the expected HTTP and communication errors.                          |
| Frontend is prepared for backend integration | ✅          | API communication is isolated behind the client layer.                              |
| End-to-end backend integration               | ⚠️ Pending | Final validation belongs to the integration/testing task.                           |
| Real backend response validated in the CLI   | ⚠️ Pending | Requires end-to-end integration validation.                                         |
| Code is documented                           | ✅          | Explicit names, parameters, type hints, and docstrings are used.                    |

## Future improvements

The following features are intentionally outside the Mini MVP:

* Web frontend.
* Authentication and user management.
* Conversation history and persistence.
* Streaming responses.
* Advanced terminal formatting.
* File upload support.

> **Note:** End-to-end integration validation is not a future feature. It is a pending step required to close the Mini MVP and is handled by the integration/testing task.
