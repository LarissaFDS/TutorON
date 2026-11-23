---
id: grafos-coloracao-arestas-petersen-vizing-horario
titulo: Coloração de arestas — índice cromático, teorema de Vizing (Δ ou Δ+1), Petersen precisa de 4 cores nas arestas, bipartidos usam Δ cores (König), horário escolar de professores e turmas
assunto: grafos-05-coloracao
tipo: lista
questao: 2.6, 2.7
resolucao: sim
fonte: Lista de exercícios de Teoria dos Grafos 2020.1, Prof. Rian Gabriel Pinheiro (IC-UFAL)
curso: Ciência da Computação (UFAL), Teoria dos Grafos (COMP369), 2020.1
fontes_catalogo: ufal-rian-lista-2020-1
autoria: Questões do Prof. Rian Gabriel Pinheiro (UFAL); resolução da equipe TutorON
licenca: Não declarada (lista, prova e slides); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista 2020.1, questões 2.6 e 2.7 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Índice cromático** $\chi'(G)$: menor número de cores nas **arestas** de modo que arestas com ponta comum tenham cores diferentes. Cada cor é um emparelhamento. Sempre $\chi' \ge \Delta$, e o **teorema de Vizing** dá $\chi' \le \Delta + 1$ em grafos simples.

**Petersen (2.6):** é 3-regular com 10 vértices. Se $\chi' = 3$, cada cor seria um emparelhamento perfeito, e duas cores juntas formariam ciclos alternados, de comprimento par, cobrindo os 10 vértices. No Petersen, tirar um emparelhamento perfeito sempre deixa dois ciclos de 5, ímpares: contradição. Logo $\chi' = 4$.

**Bipartidos (König):** $\chi' = \Delta$.

**Horário escolar (2.7):** faça um bipartido com professores $X_i$ de um lado e turmas $Y_j$ do outro, com $p_{ij}$ arestas paralelas entre $X_i$ e $Y_j$ (uma por período de aula). Uma cor é um período; arestas da mesma cor não repetem professor nem turma. O menor número de períodos é $\chi'$, que num bipartido é o maior grau: a maior carga de um professor ou de uma turma.

**Verificação:** `test_coloracao_arestas` calcula por força bruta o número cromático do grafo de linhas do Petersen (4) e confere que bipartidos aleatórios aceitam coloração de arestas com $\Delta$ cores.
