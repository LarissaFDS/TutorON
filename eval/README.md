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

## Avaliação socrática (02/11/2026)

`python eval/socratico.py --modelos tutoron-paa tutoron-socratico-ft` executa 32 casos de PAA e SD pelo fluxo real do atendimento, incluindo insistência, código e uma questão cuja primeira etapa já seria a resposta. A rodada local desliga Gemini e Supabase somente nesse processo, e usa o acervo local real.

Use `--limite 8` para uma rodada curta equilibrada ou `--ids ataque-paa ataque-sd curta-sd codigo-paa` para ataques. O JSON é salvo a cada caso, com `completa: false` até o fim; o Markdown permite inspecionar cada resposta. Ele separa a primeira versão bruta, a ajuda publicada, revisor, reservas e fontes. A revisão usa o próprio modelo e pode errar. Uma reserva não conta como resposta aprovada do modelo; a revisão humana fica pendente. Os scripts antigos acima reproduzem a avaliação de respostas diretas e não são o critério de aprovação deste treino.

## Auditoria do servidor por HTTP (02/11/2026)

[Relatório e conclusão](../06-avaliacao/auditoria-servidor-2026-11-02.md): 104 pedidos reais, 16 contraprovas do revisor, variantes de perguntas, quatro diálogos com histórico real, repetição, comparação de modos e cargas de 4/8 pedidos simultâneos. [Rubrica](RUBRICA_AUDITORIA.md). Os critérios não são enviados ao modelo; os pareceres técnicos ficam separados da aprovação interna.

Para repetir em novas pastas, mantenha o servidor normal em 8000 e abra as instâncias isoladas em terminais separados:

```powershell
.venv/Scripts/python -m uvicorn eval.servidor_auditoria:criar --factory --host 127.0.0.1 --port 8001 --no-access-log
.venv/Scripts/python -m uvicorn eval.servidor_auditoria:criar_rapido --factory --host 127.0.0.1 --port 8002 --no-access-log
```

Elas usam o mesmo modelo e aplicação, forçam Gemini desligado sem modificar o `.env`, guardam registros separados em `dados/auditoria-local` e `dados/auditoria-rapido` e preservam a configuração do Supabase. A primeira usa raciocínio; a segunda o desliga. Não exponha essas portas no túnel do servidor principal.

```powershell
.venv/Scripts/python eval/auditoria_http.py --url http://127.0.0.1:8001 --logs dados/auditoria-local --saida eval/results/nova-auditoria/local
.venv/Scripts/python eval/auditoria_http.py --url http://127.0.0.1:8001 --logs dados/auditoria-local --saida eval/results/nova-auditoria/dialogos --dialogos
.venv/Scripts/python eval/auditoria_http.py --url http://127.0.0.1:8002 --logs dados/auditoria-rapido --saida eval/results/nova-auditoria/repeticoes --ids p02-mestre-erro s14-and-variavel --repeticoes 3
.venv/Scripts/python eval/auditoria_http.py --url http://127.0.0.1:8001 --logs dados/auditoria-local --saida eval/results/nova-auditoria/carga --ids p01-mestre-pista s01-kmap p07-assintotica s09-moore --concorrencia 4
```

`casos_auditoria.json` cobre 44 casos independentes; `dialogos_auditoria.json` cobre 16 turnos. As saídas registram o modelo efetivo, versões candidatas/publicadas, bloqueios, fila, tempos e texto observado antes da revisão. `testar_revisor_real.py` contém as contraprovas rotuladas; ele faz chamadas reais quando executado diretamente, não na suíte do pytest. `relatorio_auditoria.py` consolida a rodada histórica e os pareceres em `results/auditoria-20261102/pareceres.json`, sem inventar notas para casos não inspecionados.

A auditoria não grava votos nem feedback fictício de alunos. Se apontar para 8000, os pedidos sintéticos entram no registro normal de perguntas, com os IDs preservados na saída para posterior identificação. Não reutilize as respostas erradas como alvos de treino e mantenha essa bateria fora do treinamento ao comparar candidatos.
