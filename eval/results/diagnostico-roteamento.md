# Diagnóstico de roteamento

Fontes: `perguntas.jsonl`, `resultados-mvp.json`. 16 respostas.

## Modelo que respondeu: perguntas.jsonl

| Modelo | Respostas | % |
|---|---:|---:|
| gemini-3.1-flash-lite | 6 | 75% |
| gemini-3.8-flash | 1 | 12% |
| gemini-flash-latest | 1 | 12% |

## Modelo que respondeu: resultados-mvp.json

| Modelo | Respostas | % |
|---|---:|---:|
| gemini-3.1-flash-lite | 5 | 62% |
| gemini-3.7-flash | 2 | 25% |
| gemini-3.6-flash | 1 | 12% |

## Modelo que respondeu: (todas)

| Modelo | Respostas | % |
|---|---:|---:|
| gemini-3.1-flash-lite | 11 | 69% |
| gemini-3.7-flash | 2 | 12% |
| gemini-3.8-flash | 1 | 6% |
| gemini-flash-latest | 1 | 6% |
| gemini-3.6-flash | 1 | 6% |

## Resultado de cada modelo nas tentativas

| Modelo | HTTP 429 | HTTP 503 | cancelado (outro respondeu antes) | pulado (em pausa) | respondeu | tempo esgotado |
|---|---:|---:|---:|---:|---:|---:|
| gemini:gemini-3.8-flash | 5 | 2 | 3 | 5 | 1 | 0 |
| gemini:gemini-3.7-flash | 2 | 4 | 2 | 5 | 2 | 1 |
| gemini:gemini-3.6-flash | 6 | 1 | 3 | 5 | 1 | 0 |
| gemini:gemini-3.5-flash | 6 | 1 | 1 | 5 | 0 | 0 |
| gemini:gemini-flash-latest | 6 | 0 | 0 | 5 | 1 | 0 |
| gemini:gemini-3.1-flash-lite | 0 | 1 | 0 | 0 | 11 | 0 |
| ollama:tutoron-paa | 0 | 0 | 1 | 0 | 0 | 0 |

## Tempo em pausa observado (limite inferior)

Do último erro de cada modelo até a última pergunta em que ele foi pulado por estar em pausa. Pelo código (`backend/llm.py`), um 429 pausa por max(60 s, retryDelay do Google), até 1 h; 503 pausa 20 s; tempo esgotado, 30 s.

| Modelo | Erro que causou a pausa | Pausa observada (min) |
|---|---|---:|
| gemini:gemini-3.8-flash | HTTP 429 | ≥ 30 |
| gemini:gemini-3.7-flash | HTTP 429 | ≥ 30 |
| gemini:gemini-3.6-flash | HTTP 429 | ≥ 30 |
| gemini:gemini-3.5-flash | HTTP 429 | ≥ 30 |
| gemini:gemini-flash-latest | HTTP 429 | ≥ 30 |

## Papel do modelo local na corrida

Tentativas do `ollama:*` nestes logs: {'cancelado (outro respondeu antes)': 1}. Respostas servidas pelo local: 0.
