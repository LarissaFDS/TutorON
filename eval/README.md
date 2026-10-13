# eval/ — avaliação do TutorON contra uma IA genérica

| Arquivo | O que é |
|---|---|
| `RELATORIO.md` | Conclusões das Fases 0 e 1 (comece por aqui) |
| `perguntas.json` | Conjunto dourado: as 3 perguntas da validação cega do aluno + 12 de PAA, com gabarito curto |
| `rubrica.md` | Critérios a–f do juiz e por que existem |
| `prompt_candidato.py` | "Prompt novo" testado na matriz (vai para produção no PR #25, em rascunho) |
| `prompt_anterior.py` | Prompt de produção de 12/10 congelado: o braço "atual" mede sempre a mesma coisa |
| `matriz.py` | Gera respostas, julga (um ou mais juízes) e monta o relatório da matriz |
| `folha_cega.py` | Folha A/B/C anônima das 3 perguntas originais para o aluno reavaliar |
| `diagnostico.py` | Roteamento (pelos logs) e recuperação do acervo |
| `results/` | Saídas: `respostas.jsonl`, `notas.jsonl`, `relatorio.md`, `diagnostico-*.md` |
| `test_eval.py` | Testes sem rede (rodam no `python -m pytest`) |

## Passo a passo para quem vai rodar (no servidor)

1. Use uma chave do Gemini **separada** da do site ou rode **fora do horário de uso**: a matriz divide a cota com os alunos.
2. Coloque a chave no `.env` da raiz (`GEMINI_API_KEY=...`) e confira que o Ollama está ligado com o `bge-m3` (`ollama list`).
3. Rodada rápida, só as 3 perguntas do aluno (30 gerações + 30 julgamentos por juiz): `python eval/matriz.py gerar --perguntas A1,A2,A3`
4. Julgue: `python eval/matriz.py julgar` (juiz padrão: gemini-3.8-flash, que também é o modelo forte avaliado).
5. Julgue de novo com outro juiz, para medir a autopreferência: `python eval/matriz.py julgar --juiz gemini-3.7-flash`
6. Relatório: `python eval/matriz.py relatorio`. Mostra a nota de a–f nas 3 originais, mesmo com resultado parcial.
7. Folha para o aluno reavaliar às cegas: `python eval/folha_cega.py`. Envie só `results/folha_cega.md`; o `folha_cega_mapa.json` diz quem é quem e fica com a equipe.
8. Se a rodada rápida der certo, rode a matriz completa: repita os passos 3 a 6 sem `--perguntas` (150 gerações + 150 julgamentos por juiz).
9. Se aparecer "indisponível" (cota), pare e rode de novo mais tarde: tudo retoma de onde parou e nunca troca de modelo em silêncio.
10. Envie de volta a pasta `eval/results/` inteira (`respostas.jsonl`, `notas.jsonl`, `recuperacao.jsonl`, `relatorio.md`, `resumo.json`).

## Comandos de diagnóstico

```bash
python eval/diagnostico.py roteamento --logs dados/perguntas.jsonl 06-avaliacao/resultados-mvp.json
python eval/diagnostico.py recuperacao
python eval/diagnostico.py calibrar   # limiar ACERVO_SIMILARIDADE_MINIMA (PR #23), precisa do bge-m3
```

`--perguntas` aceita prefixos de id separados por vírgula (`A1,A2,A3`, `P1`, `N2`…).
