# TutorON x IA genérica: relatório das Fases 0 e 1

Situação em 13/10/2026: o harness está pronto e testado. Os diagnósticos de roteamento, recuperação e prompt foram medidos. **A matriz de modelos ainda não rodou**: esta máquina não tem `GEMINI_API_KEY` nem o `bge-m3` no Ollama. Por isso este relatório **ainda não diz qual alavanca explica mais a diferença**; ele diz o que os logs já provam e o que só a matriz pode decidir.

## Números já medidos

### H1 — Roteamento: confirmada nos logs

Fontes: `perguntas.jsonl` (8 respostas do modo Tutor, 12/10) e `06-avaliacao/resultados-mvp.json` (8 respostas TutorON+Gemini). Detalhes em [`results/diagnostico-roteamento.md`](results/diagnostico-roteamento.md).

| Quem respondeu | Logs do site | Avaliação MVP | Total |
|---|---:|---:|---:|
| gemini-3.1-flash-lite | 6 de 8 (75%) | 5 de 8 | **11 de 16 (69%)** |
| modelos melhores (3.6 a 3.8, flash-latest) | 2 de 8 | 3 de 8 | 5 de 16 |
| ollama:tutoron-paa (local) | 0 | 0 | 0 |

- O pedido citava "5 de 7"; o arquivo tem 8 respostas, das quais 6 vieram do lite.
- Os cinco modelos melhores receberam **HTTP 429 em sequência, em menos de 3 s no total**, cada um com a própria pausa. A pausa por modelo já existe (`Breaker` em `backend/llm.py`); o problema é que **todos** esgotam a cota juntos. Depois de um 429, ficaram em pausa **pelo menos 30 min** (19:13 → 19:43), compatível com o `retryDelay` do Google (o código aceita até 1 h).
- O log não guarda o `retryDelay` nem se o 429 foi por minuto ou por dia. Sem isso, não dá para saber se "esperar e tentar de novo o modelo forte" resolveria.
- O modelo local nunca respondeu: apareceu 1 vez e foi cancelado. Hoje ele quase não participa da corrida.
- O lite só falhou uma vez (503). Ele é o "chão" da cascata e responde sempre, sem nenhum aviso ao aluno.

### H2 — Prompt e estrutura: confirmada nos logs

| Métrica (respostas do Gemini) | TutorON (16) | Genérico, mesmo modelo (8) |
|---|---:|---:|
| Termina com "**Verificação:**" | **16 (100%)** | 0 |
| Tem tabela | 0 | 1 |
| Tem bloco de código ou pseudocódigo | 1 | 0 |
| Citações [P]/[L] por resposta | 4,2 (site) / 2,1 (MVP) | 0 |
| Palavras (média) | ~330 | ~350 |

O que no `SISTEMA_TUTOR` (`backend/prompts.py`) causa isso:

1. **"Termine respostas com cálculo com uma linha "**Verificação:**"…"**: causa direta dos 16 de 16. Vira um bloco genérico mesmo quando não confere nada ("O cálculo segue a lógica de acumulação…", na resposta do robô).
2. **Não há roteiro por tipo de questão.** Nada pede subproblema → recorrência → pseudocódigo → rastreio → complexidade, nem o significado de i-1/j-1. É exatamente o que o aluno sentiu falta.
3. **"Pseudocódigo e código em blocos ``` com a linguagem"**: convida a usar uma linguagem e não prefere pseudocódigo. Na prática quase não houve nem um nem outro.
4. **Limite de ~400 palavras** para tudo: aperta uma resposta de PD completa (6 partes).
5. **Nenhuma regra sobre pedidos de formato**: "faça um esqueminha" gerou o mesmo texto corrido, sem tabela nem diagrama. "De forma mais fácil" (robô) gerou 336 palavras sem pseudocódigo nem exemplo numérico.
6. **"Ao usar um trecho, cite o rótulo"**, somado ao RAG que sempre devolve 4 trechos (H3), produz citações que só enfeitam a frase ("Como visto em [L2]…" na resposta do troco), mesmo quando o trecho não foi usado de fato.

### H3 — Recuperação: confirmada, mas com uma nuance

Detalhes em [`results/diagnostico-recuperacao.md`](results/diagnostico-recuperacao.md). Esta execução foi **só léxica** (sem bge-m3 aqui); a produção usa a busca híbrida.

- **O acervo indexado tem só 53 blocos**, 10 de PD, todos "resolução de aluno" com mediana de ~650 caracteres. Mochila 0/1, troco por PD e LIS **não existem**.
- **SUBSET SUM e substring comum existem** (Lista 5, q. 8 e q. 5), mas são telegráficos. O de SUBSET SUM traz só a versão compactada em 1D (`possivel[s]`), sem `dp[i][s]` nem recorrência com casos base. O de substring comum usa `x[i-1]=y[j-1]` sem explicar o deslocamento entre a string (base 0) e a tabela (base 1). **É exatamente a confusão do aluno com "i-1" e "j-1".** Então o problema não é só falta de cobertura: os blocos de PD que existem ensinam mal.
- **Sem corte de relevância.** A fusão por ranking (RRF) dá a todos scores entre 0,017 e 0,018, e qualquer palavra em comum (BM25 > 0) passa o filtro. A busca **sempre** devolve 4 blocos: só **28 de 60** são do mesmo assunto da pergunta. Mochila 0/1 recebeu "Oito damas", "ASTERISCO" e "duas rações"; troco por PD recebeu 4 blocos de outros assuntos.
- **Por que PAA_L3 p. 4 domina:** os dois blocos dessa página (a^n e k-ésimo menor) são **hubs do embedding**. O de a^n está entre os 4 vizinhos mais próximos de 12 dos outros 52 blocos, 3 vezes o esperado. Na busca híbrida, o filtro semântico (cosseno ≥ 0,55) é baixo para o bge-m3, e o RRF dá pontos pela posição no ranking, não pela similaridade. Um hub entra no top 4 de perguntas sem relação (robô, laços). O chunking é por questão, não por página; a "página 4" aparece duas vezes porque tem duas questões curtas.
- **Os curados c01, c02 e c09 funcionam onde existem.** O Algoritmo X recupera c01 e c02 em 1º e 2º, e NP recupera c09 em 2º.

### H4 — O RAG piora a resposta? Ainda sem resposta

Os logs só mostram sintomas (citações a material irrelevante). A diferença com e sem RAG, no mesmo modelo e com o mesmo prompt, só aparece na matriz.

## O que a matriz vai decidir

`python eval/matriz.py gerar && python eval/matriz.py julgar && python eval/matriz.py relatorio`. São 15 perguntas × 2 modelos × 5 braços (genérico, atual sem/com RAG, novo sem/com RAG), julgadas pela rubrica [`rubrica.md`](rubrica.md).

| Pergunta | Comparação no relatório |
|---|---|
| O modelo explica a diferença? | `modelo (forte - lite)` em cada braço |
| O prompt explica? | `prompt (novo - atual)`, com e sem RAG |
| O RAG ajuda ou atrapalha (H4)? | `RAG (com - sem)` com o prompt atual |
| Reproduz a queixa do aluno? | `TutorON atual - genérico` (deve dar negativo) |
| Critério de sucesso | `novo_rag` ≥ `generico`, e a, b e d ≥ 4 nas 3 perguntas originais |

Custo: cerca de 300 chamadas ao Gemini. **Rode com uma chave separada ou fora do horário de uso**: a cota compartilhada com o site é exatamente o que derruba o roteamento (H1).

## Plano da Fase 2 (só depois da matriz)

Cada item vira um PR separado. A ordem depende da matriz:

1. **Prompt**: levar `eval/prompt_candidato.py` para `backend/prompts.py` se `prompt (novo - atual)` for positivo.
2. **Roteamento**: registrar a degradação e o `retryDelay` no log; aviso ao aluno quando cair no lite; para perguntas de raciocínio, esperar curto pelo modelo forte antes do lite. Este PR só vem se `modelo (forte - lite)` for relevante.
3. **Recuperação**: corte por similaridade absoluta (e não só RRF), penalidade a hubs, e não citar nada quando nada for relevante.
4. **Curadoria**: .md revisados para mochila 0/1, SUBSET SUM, LCS/substring, troco e robô, no padrão dos c01/c02/c09.

## Riscos e limites desta fase

- As três perguntas do aluno foram **reconstruídas** a partir do relato (as respostas originais da validação cega não estavam nos arquivos enviados). As duas de lista usam o enunciado real da Lista 5.
- O juiz é um Gemini: mesma família dos modelos avaliados. Confira à mão as 3 perguntas originais.
- O diagnóstico de recuperação desta máquina foi só léxico. O de hubness usa os vetores salvos no índice e vale para a produção.
