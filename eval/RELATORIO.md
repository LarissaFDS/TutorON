# TutorON x IA genérica: relatório das Fases 0, 1 e 2

Situação em 13/10/2026:
- O harness (`eval/`) está pronto e testado.
- Os diagnósticos de roteamento, recuperação e prompt foram medidos.
- As correções que **não dependem da matriz** estão em PRs separados (tabela abaixo).
- **A matriz de modelos ainda não rodou**: esta máquina não tem `GEMINI_API_KEY` nem o `bge-m3`. Ela vai rodar no servidor.

Por isso este relatório **ainda não diz qual alavanca (modelo, prompt ou recuperação) explica mais a diferença**. Diz o que os logs e o índice já provam, o que foi corrigido e o que só a matriz decide.

## Status dos PRs (todos para `dev`, nenhum mesclado)

| PR | Tema | Depende da matriz? | Situação |
|---|---|---|---|
| [#21](https://github.com/LarissaFDS/TutorON/pull/21) | Harness `eval/`: conjunto dourado, rubrica, matriz, juiz, folha cega, diagnósticos | Não | Pronto para revisão |
| [#22](https://github.com/LarissaFDS/TutorON/pull/22) | Roteamento: registrar `retry_delay_s`, cota por dia/minuto e `degradado` | Não (só registra) | Pronto para revisão |
| [#23](https://github.com/LarissaFDS/TutorON/pull/23) | Recuperação: corte absoluto de similaridade, penalidade de hub, lista vazia | O **limiar** depende da calibração | Pronto; limiar padrão conservador (0,5) |
| [#24](https://github.com/LarissaFDS/TutorON/pull/24) | Curadoria: 5 materiais de PD da equipe (`revisado: false`) | Não | Precisa de revisão humana do conteúdo e de reindexar no servidor |
| [#25](https://github.com/LarissaFDS/TutorON/pull/25) | Prompt novo + citações legíveis | **Sim** | **Rascunho**: só entra se a matriz aprovar |

Os PRs #22 a #25 foram mesclados juntos numa cópia local, sem conflito, e os 75 testes passaram.

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
- **Correção em relação à versão anterior deste relatório:** medi o cosseno do bge-m3 **entre blocos diferentes** do acervo: mediana **0,556**, p90 0,634. O filtro semântico antigo (0,55) fica praticamente na mediana, então deixa entrar metade do acervo em qualquer pergunta. Isso pesa tanto quanto o RRF.
- **Por que PAA_L3 p. 4 domina:** os dois blocos dessa página (a^n e k-ésimo menor) são **hubs do embedding**. O de a^n está entre os 4 vizinhos mais próximos de 12 dos outros 52 blocos, 3 vezes o esperado. Na busca híbrida, o filtro semântico (cosseno ≥ 0,55) é baixo para o bge-m3, e o RRF dá pontos pela posição no ranking, não pela similaridade. Um hub entra no top 4 de perguntas sem relação (robô, laços). O chunking é por questão, não por página; a "página 4" aparece duas vezes porque tem duas questões curtas.
- **Os curados c01, c02 e c09 funcionam onde existem.** O Algoritmo X recupera c01 e c02 em 1º e 2º, e NP recupera c09 em 2º.

### H4 — O RAG piora a resposta? Ainda sem resposta

Os logs só mostram sintomas (citações a material irrelevante). A diferença com e sem RAG, no mesmo modelo e com o mesmo prompt, só aparece na matriz.

## Fase 2: o que já foi feito sem depender da matriz

### #22 Roteamento (só observabilidade)
Cada 429 passa a gravar `retry_delay_s` (o valor real; a pausa continua limitada a 1 h), `quota_ids` e `cota` (`por_dia`/`por_minuto`). Cada resposta grava `degradado: true` quando vem do último Gemini depois de falha ou pausa dos melhores. A lógica da cascata e a interface não mudaram. Com um dia de log novo, `python eval/diagnostico.py roteamento --logs dados/perguntas.jsonl` mostra se a cota que acaba é a diária (esperar não adianta) ou a por minuto (esperar adianta).

### #23 Recuperação

| Medida (vetores do índice, bloco como consulta) | Antes | Depois |
|---|---:|---:|
| k-ocorrência do PAA_L3 p. 4 (a^n / k-ésimo) | 12 / 9 | **7 / 3** |
| Maior k-ocorrência do acervo (esperado: 4) | 12 | 8 |
| Vizinhos do mesmo assunto | 42% | 44% |

A penalidade de hub resolve o PAA_L3 p. 4, mas melhora pouco a precisão por assunto. O ganho maior deve vir do **corte absoluto**, e o limiar dele **não foi inventado**: o padrão de 0,5 é o mesmo do livro (mesmo bge-m3) e é conservador, porque corta pouco, dado que a mediana entre blocos é 0,556. O valor certo sai de `python eval/diagnostico.py calibrar` no servidor. O comando recomenda o maior limiar que não perde nenhum acerto conhecido (c01/c02 no Algoritmo X, c09 em NP, os novos e01–e05).

### #24 Curadoria de PD
Cinco materiais (mochila 0/1, SUBSET SUM com `S[i][s]` antes da versão 1D, substring comum com a explicação base 0/base 1, troco, robô). Cada rastreio é conferido por um teste que implementa a recorrência. Na busca léxica (índice refeito numa cópia temporária), o material novo ficou em **1º lugar** nas três perguntas do aluno; antes, a mochila recebia "Oito damas", "ASTERISCO" e "duas rações". Rotulados como material da equipe, `revisado: false`.

### #25 Prompt (rascunho)
Leva `eval/prompt_candidato.py` para produção e troca os rótulos [P1]/[L1] por nomes legíveis ("Lista 5, p. 7-8"), também na lista "Material consultado" do site. A matriz mede o prompt antigo congelado em `eval/prompt_anterior.py`, então o resultado não muda se o #25 entrar antes, mas o ideal é rodar a matriz primeiro.

## O que o usuário roda no servidor

O roteiro exato está em [`rodar_servidor.md`](rodar_servidor.md). Ele roda numa worktree separada da pasta do site, em duas rodadas com pastas de resultado próprias:

1. **Rodada 1, baseline (só o #21).**
   - `preflight.py --rodada 1` confere chave, `bge-m3`, índice com vetores, e que o #23/#24 **não** estão no checkout. Também estima chamadas e tempo.
   - Depois: `gerar` nas 3 perguntas do aluno, `julgar` com dois juízes, `relatorio` e `folha_cega`, tudo em `eval/results/rodada1`.
2. **Rodada 2, integração (#21 + #23 + #24).**
   - Preflight, depois **backup do índice** com data, `python -m acervo indexar --embeddings` e `preflight --pos-indexacao`.
   - `diagnostico.py calibrar`, com o limiar passado por variável de ambiente para não mexer no site.
   - `gerar` só de `atual_rag` e `novo_rag`, com `--incluir-nao-revisados`, depois `julgar` com os mesmos dois juízes e `relatorio`, em `eval/results/rodada2`.
3. **Decisão.** `python eval/decidir.py --rodada1 ... --rodada2 ...` imprime as decisões (a)–(d) da tabela abaixo e grava `eval/results/decisao.md`.

## O que depende da matriz, e o que muda conforme o resultado

| Resultado da matriz | O que fazer |
|---|---|
| `prompt (novo - atual)` > 0 e critério de sucesso atingido (`novo_rag` ≥ genérico; a, b, d ≥ 4 nas 3 originais) | Tirar o **#25** de rascunho e mesclar. |
| `prompt (novo - atual)` ≈ 0 ou < 0 | Não mesclar o #25. Olhar as notas por critério (a–f) e as justificativas do juiz para ajustar o prompt candidato e rodar de novo só as 3 originais. |
| `modelo (forte - lite)` grande, sobretudo em PD | Abrir o PR de roteamento que ficou de fora: esperar o modelo forte antes do lite em perguntas de raciocínio e avisar o aluno quando houver degradação. A decisão entre esperar e trocar de chave/plano depende da coluna de cota do #22. |
| `modelo (forte - lite)` ≈ 0 | Não mexer no roteamento; o lite basta e é mais rápido. O #22 continua útil para monitorar. |
| `RAG (com - sem)` < 0 com o prompt atual (H4 confirmada) | Priorizar o #23 com o limiar calibrado, e rodar a matriz de novo **depois** do #23 e do #24. Se continuar negativo, reduzir `ACERVO_K` ou usar o RAG só em PD/listas. |
| `RAG (com - sem)` > 0 | O #23 continua recomendado (limpeza), mas sem urgência. |
| Juiz com autopreferência alta | Usar como juiz principal o que não é avaliado (o relatório já escolhe sozinho) e dar mais peso à folha cega do aluno. |

Em todos os casos, **a nota do aluno na folha cega é a validação final**; o juiz Gemini é só triagem.

## O que não resolvi / riscos

- As três perguntas do aluno foram **reconstruídas** a partir do relato (as respostas originais da validação cega não estavam nos arquivos enviados). As duas de lista usam o enunciado real da Lista 5.
- O juiz é um Gemini: mesma família dos modelos avaliados. Confira à mão as 3 perguntas originais.
- O diagnóstico de recuperação desta máquina foi só léxico. O de hubness usa os vetores salvos no índice e vale para a produção.
- Os 5 materiais de PD foram escritos por agente e conferidos por teste (contas e rastreios), **não por um professor**. Precisam de revisão humana antes de uso amplo.
- O corte de relevância, com o limiar padrão, corta pouco. Sem a calibração no servidor, o ganho do #23 em produção vem quase só da penalidade de hub.
- A matriz não mede citações nem latência. O prompt novo é ~35% mais longo; vale olhar o tempo de resposta e o modelo local (janela de 8k).
- O roteamento continua descendo para o lite sem aviso até a matriz justificar a mudança. O #22 só passa a medir isso.
