---
id: compevol-otimizacao-multiobjetivo-dominancia-de-pareto-frente-soma-ponderada-nsga
titulo: Função de adaptação multiobjetivo em algoritmos evolucionários: dominância de Pareto, frente de Pareto, soma ponderada, ordenação por frentes (NSGA-II) (atividade 2 da ABN2)
assunto: compevol-04-atividades-2021
tipo: exercicio
questao: Atividade 2 da ABN2 (2021.1)
resolucao: sim
fonte: Atividades da turma 2021.1 de Computação Evolucionária (UFAL), página do curso
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: ufal-ce-atividades-2021
autoria: Atividade da turma 2021.1 (UFAL; docente não identificada no material); resolução conceitual da equipe TutorON
licenca: Não declarada (atividade); paráfrase, capturas de tela não versionadas
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Atividade 2 da ABN2 (2021.1) (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

A atividade pede um AE com função de adaptação **multiobjetivo**. É **avaliativa**: aqui vão os conceitos.

**Problema multiobjetivo:** otimizar ao mesmo tempo objetivos em conflito, como **custo** e **qualidade**. Em geral não existe uma solução melhor em todos; existe um conjunto de compromissos.

**Dominância de Pareto** (minimizando todos): $a$ **domina** $b$ se $a$ não é pior que $b$ em nenhum objetivo **e** é estritamente melhor em pelo menos um. Soluções não dominadas por nenhuma outra formam a **frente de Pareto**.

Exemplo (minimizar $f_1$ e $f_2$): $A = (1, 5)$, $B = (2, 3)$, $C = (3, 4)$, $D = (4, 1)$. $B$ domina $C$ ($2 < 3$ e $3 < 4$). $A$, $B$ e $D$ não se dominam: frente = $\{A, B, D\}$.

**Como transformar em aptidão:**
1. **soma ponderada:** $F = w_1 f_1 + w_2 f_2$; simples, mas a resposta depende dos pesos e não acha pontos em partes não convexas da frente;
2. **restrições:** otimiza um objetivo e impõe limites aos outros;
3. **ordenação por frentes** (NSGA-II): a 1ª frente são os não dominados; tirando-os, a 2ª frente, e assim por diante. A aptidão é o número da frente; o desempate usa a **distância de aglomeração** (*crowding distance*), que favorece soluções em regiões menos povoadas, para espalhar a frente.

**Gráficos:** além de melhor e média por geração (para cada objetivo, ou para o hipervolume), mostre a frente final num gráfico $f_1 \times f_2$.

**Verificação:** `test_multiobjetivo` implementa a dominância, confere a frente $\{A, B, D\}$ do exemplo e a ordenação por frentes num conjunto maior, e mostra que a soma ponderada com pesos diferentes escolhe pontos diferentes da frente.
