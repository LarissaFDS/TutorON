---
id: compevol-alinhamento-multiplo-de-dna-score-alfa-beta-delta-gaps-algoritmo-evolucionario
titulo: Alinhamento múltiplo de sequências de DNA com computação evolucionária: pontuação αx + βy + δz (pares iguais, diferentes e com gap), representação dos gaps e operadores (segunda atividade da 1ª ABN)
assunto: compevol-04-atividades-2021
tipo: exercicio
questao: Segunda atividade da 1ª ABN (2021.1)
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
Computação Evolucionária (UFAL, turma 2021.1), Segunda atividade da 1ª ABN (2021.1) (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

A atividade pede um programa que alinhe várias sequências de DNA com um AE. É **avaliativa**: aqui vão os conceitos e uma conta pequena, não o programa.

**Problema:** dadas sequências $s_1, \ldots, s_k$ (bases A, C, G, T), inserir **gaps** (`-`) para que todas fiquem com o mesmo tamanho $m$ e a pontuação seja **máxima**; tirando os gaps de cada linha, volta-se à sequência original. Pontuação por **pares de linhas**, coluna a coluna:
$$\text{score} = \alpha x + \beta y + \delta z$$
Em palavras: $x$ pares de bases iguais na mesma coluna, $y$ pares de bases diferentes, $z$ pares base com gap, com pesos $\alpha$, $\beta$, $\delta$ (par gap com gap não conta).

**Exemplo** com $\alpha = 1$, $\beta = 0$, $\delta = -1$:
```
A C G T
A - G T
A C - T
```
Pares de linhas: (1,2): 3 iguais, 1 com gap; (1,3): 3 iguais, 1 com gap; (2,3): colunas A/A igual, -/C gap, G/- gap, T/T igual. Total: $x = 8$, $y = 0$, $z = 4$; score $= 8 - 4 = 4$.

**Modelagem como AE:**
- **indivíduo:** para cada sequência, as **posições dos gaps** (ou a sequência já com gaps); a validade exige que, sem gaps, a linha volte à original;
- **aptidão:** o score acima (o problema exato é NP-difícil para muitas sequências, por isso a heurística);
- **mutação:** mover um gap, inserir um par gap/gap em todas as linhas, remover colunas só de gaps;
- **cruzamento:** cortar as linhas em uma coluna e trocar os lados, ajustando os gaps para manter as bases;
- a preferência por gaps no início, no fim ou no meio pode entrar como **penalidade** na aptidão.

**Verificação:** `test_alinhamento_score` refaz a conta do exemplo ($x = 8$, $z = 4$, score 4) e confere que remover os gaps devolve as sequências.
