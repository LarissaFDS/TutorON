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
| `diagnostico.py` | Roteamento (pelos logs), recuperação do acervo e calibração do corte |
| `preflight.py` | Confere chave, `bge-m3`, índice, branch e PRs no checkout antes de gastar cota; estima chamadas e tempo |
| `decidir.py` | Lê o `resumo.json` das rodadas e imprime a decisão da Fase 2 (limiares heurísticos no topo) |
| `rodar_servidor.md` | **Roteiro exato das duas rodadas no servidor** (baseline e integração #23 + #24) |
| `results/` | Saídas; cada rodada na sua pasta (`--saida eval/results/rodada1`) |
| `test_eval.py` | Testes sem rede (rodam no `python -m pytest`) |

## Para quem vai rodar (no servidor)

Siga [`rodar_servidor.md`](rodar_servidor.md): preflight, rodada 1 (só o #21), backup do índice, rodada 2 (#21 + #23 + #24) e `decidir.py`. Todos os comandos da matriz, da folha cega e do diagnóstico aceitam `--saida <pasta>`; sem ela, gravam em `eval/results/`.

Regras que valem para qualquer rodada:
- A matriz divide a cota do Gemini com o site: use outra chave ou rode fora do horário de uso.
- A chave fica só no `.env`; o preflight diz se ela existe sem mostrá-la.
- Se aparecer "indisponível" (cota), rode o mesmo comando mais tarde: tudo retoma de onde parou e nunca troca de modelo em silêncio.
- A matriz completa (15 perguntas) é o mesmo `gerar` sem `--perguntas`: 150 gerações + 150 julgamentos por juiz. Só vale depois que a rodada rápida der resultado legível.

## Comandos de diagnóstico

```bash
python eval/diagnostico.py roteamento --logs dados/perguntas.jsonl 06-avaliacao/resultados-mvp.json
python eval/diagnostico.py recuperacao
python eval/diagnostico.py --saida eval/results/rodada2 calibrar   # limiar ACERVO_SIMILARIDADE_MINIMA (PR #23), precisa do bge-m3
```

`--perguntas` aceita prefixos de id separados por vírgula (`A1,A2,A3`, `P1`, `N2`…).

## Relevância da busca e bateria do tutor (19/10/2026)

```bash
python eval/relevancia.py             # 52 perguntas rotuladas (PAA e SD): bloco certo ou nenhum bloco
python eval/relevancia.py --vetores   # grava os embeddings das perguntas novas (precisa do bge-m3)
python eval/bateria_tutor.py --modelo tutoron-paa --saida eval/results/bateria-tutor-tutoron-paa.json
```

A bateria do tutor passa pelo fluxo real do site e grava fontes, resposta, rótulos citados e ajustes; a correção é avaliada à mão com os gabaritos de `tests_acervo/test_casos_sd.py`. Resultados: `06-avaliacao/correcoes-2026-10-19.md`.
