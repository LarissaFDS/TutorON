---
id: so-belady-envelhecimento-localidade-thrashing
titulo: Anomalia de Belady, algoritmo de envelhecimento (aging) com bits de referência, segunda chance, localidade de referência e thrashing
assunto: so-05-memoria
tipo: prova
questao: Prova 2, questões 1 e 3; caderno, cap. 5 (lista 4 da turma, questões 7 e 9 do cap. 17 do livro novo)
resolucao: sim
fonte: Prova 2 do Prof. André Aquino (UFAL), fotos da turma com gabarito; Lista 4 da turma (2021) sobre os exercícios do Prof. Maziero
fontes_catalogo: ufal-aquino-prova2-fotos,turma-listas-2021,maziero-socm-2019,ufal-aquino-slides-so
autoria: Prova do Prof. André Aquino (UFAL) e exercícios do Prof. Maziero; resoluções de alunos conferidas por simulação pela equipe TutorON
licenca: Não declarada (prova); exercícios do Maziero sob CC BY-NC-SA 3.0; paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Prova 2 do Prof. André Aquino e exercícios do Maziero. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Anomalia de Belady (Prova 2, questão 1):** em alguns algoritmos, o número de faltas de página **aumenta** quando aumenta o número de **quadros alocados** (páginas alocadas) ao processo. Resposta: "número de páginas alocadas aumenta". Exemplo clássico com FIFO e a sequência 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5: **9 faltas com 3 quadros e 10 com 4**. O LRU e o ótimo não têm a anomalia (são algoritmos de pilha): com LRU a mesma sequência dá 10 faltas com 3 quadros e 8 com 4.

**Localidade (Prova 2, questão 3):** memória virtual e *cache* funcionam porque um programa, num intervalo curto, acessa poucas regiões (localidade temporal e espacial): manter só elas na memória rápida basta. Resposta: "o princípio da localidade pode ser aplicado". O **conjunto de trabalho** é o conjunto de páginas usadas recentemente; se os quadros não cabem nele, o sistema troca páginas o tempo todo (**thrashing**). Localidade **não** é "o percentual de páginas do processo na RAM" (afirmação falsa do caderno).

**Envelhecimento (aging):** cada página tem um contador de 4 bits; a cada leitura periódica, o contador desloca 1 bit para a direita e o bit de referência R entra pela esquerda: $c \leftarrow (R \ll 3) \mid (c \gg 1)$. Sai a página de **menor** contador.
Exercício (4 quadros A, B, C, D; dez leituras de R): 0101, 0011, 1110, 1100, 1001, 1011, 1010, 0111, 0110, 0111. Valores finais: A = 0001 (**1**), B = 1110 (**14**), C = 1111 (**15**), D = 1010 (**10**). **Substitui-se o quadro A.** A lista da turma chegou aos mesmos valores.

**Segunda chance (relógio):** fila FIFO circular; se a página da vez tem R = 1, zera R e passa adiante; sai a primeira com R = 0.

**Verificação:** as leituras mais recentes pesam mais: A teve R = 1 só nas leituras 3 a 7 e por isso tem o menor contador; os valores finais foram recalculados em `tests_acervo/so_verif.py`, assim como 9 e 10 faltas do FIFO.
