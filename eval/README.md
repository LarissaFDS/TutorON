# eval/ — avaliação do TutorON contra uma IA genérica

| Arquivo | O que é |
|---|---|
| `RELATORIO.md` | Conclusões das Fases 0 e 1 (comece por aqui) |
| `perguntas.json` | Conjunto dourado: as 3 perguntas da validação cega do aluno + 12 de PAA, com gabarito curto |
| `rubrica.md` | Critérios a–f do juiz e por que existem |
| `prompt_candidato.py` | "Prompt novo" testado na matriz (ainda não usado em produção) |
| `matriz.py` | Gera respostas, julga e monta o relatório da matriz |
| `diagnostico.py` | Roteamento (pelos logs) e recuperação do acervo |
| `results/` | Saídas: `respostas.jsonl`, `notas.jsonl`, `relatorio.md`, `diagnostico-*.md` |
| `test_eval.py` | Testes sem rede (rodam no `python -m pytest`) |

## Como rodar

Na raiz do repositório, com `GEMINI_API_KEY` no `.env` e o Ollama com `bge-m3` (para a busca híbrida, igual à produção):

```bash
python eval/diagnostico.py roteamento --logs dados/perguntas.jsonl 06-avaliacao/resultados-mvp.json
python eval/diagnostico.py recuperacao
python eval/matriz.py gerar
python eval/matriz.py julgar
python eval/matriz.py relatorio
```

`gerar` e `julgar` retomam de onde pararam. Se a cota acabar no meio, rode de novo mais tarde. Para um teste rápido: `python eval/matriz.py gerar --perguntas A1,A2,A3`.

A matriz faz cerca de 300 chamadas ao Gemini. Use outra chave ou rode fora do horário de uso do site.
