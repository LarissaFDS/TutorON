# Estrutura do repositório

| Pasta | O que tem |
|---|---|
| `backend/` | Servidor FastAPI (`main.py`), IA (`llm.py`), tutor (`tarefas.py`, `tutoria.py`, `prompts.py`), cota, RAG. |
| `backend/web/` | Front-end. **Todas as páginas usam o layout do chat** (`chat.css` + `shell.js`). |
| `backend/tests/` | Testes do servidor. |
| `acervo/` | Código do pipeline do acervo (extração, curadoria, busca). |
| `pipeline/` | Dados do pipeline, em ordem: `00-originais` (local) → `01-extraido` → `02-acervo` → `03-triagem` → `04-rag` (índice usado pelo servidor) → `05-modelo` (treino) → `06-avaliacao` → `07-validacao-alunos` (local). |
| `disciplinas/` | Cadastro e curadoria de cada disciplina. |
| `materiais/`, `ocr/` | Material das disciplinas e OCR. |
| `eval/` | Avaliações e auditorias do tutor. |
| `scripts/` | Scripts de apoio (treino, avaliação, `limpar.ps1`). |
| `docs/` | Documentação. Comece por `AGENTS.md` na raiz. |
| `legado/`, `demo-offline/` | Código antigo e demo offline; não use em código novo. |
| `dados/` | **Local, fora do Git.** Dados de alunos até a migração para o banco. |
| `*.bat` na raiz | Atalhos de um clique para a equipe (iniciar, validar, treinar, reiniciar, desligar). |

## Comandos

```
python -m pytest -q                 # todos os testes
ruff check .                        # lint
powershell -File scripts/limpar.ps1 # ver caches/temporários que podem ser apagados
```
