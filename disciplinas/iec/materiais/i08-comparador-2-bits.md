---
id: iec-comparador-2-bits
titulo: Comparador de igualdade de 2 bits (S = 1 só se A0 = B0 e A1 = B1)
assunto: iec-09-circuitos-combinacionais
tipo: prova
questao: 5
semestre: 2016.1
resolucao: sim
fonte: Fotos da Reavaliação AB1 de Introdução à Engenharia de Computação (ECOM006), UFAL, 2016.1, Q5
fontes_catalogo: ufal-iec-reav-ab1-2016
autoria: Enunciados: reavaliação da disciplina (professor não identificado na prova), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Enunciado (Reavaliação AB1, Q5):** desenhar o circuito de um comparador de 2 bits cuja saída $S$ vale 1 somente quando $A_0=B_0$ **e** $A_1=B_1$, e 0 nos demais casos.

**Ideia:** igualdade de 1 bit é a **XNOR** (sai 1 quando as entradas são iguais). Para 2 bits, as duas igualdades precisam valer ao mesmo tempo: uma **AND**.

$S=\overline{A_0\oplus B_0}\cdot\overline{A_1\oplus B_1}$

Circuito (em palavras): uma porta XNOR com entradas $A_0$ e $B_0$; outra XNOR com $A_1$ e $B_1$; as duas saídas entram numa AND de 2 entradas, cuja saída é $S$.

A tabela-verdade tem 16 linhas (4 entradas); $S=1$ só nas 4 em que $A_1A_0=B_1B_0$: 00/00, 01/01, 10/10 e 11/11. Em soma de mintermos seriam 4 produtos de 4 variáveis; a forma com XNOR é bem menor. Sem porta XNOR: $\overline{A\oplus B}=AB+\overline{A}\,\overline{B}$.

Comparar qual número é **maior** (a partir do bit mais significativo) é aprofundado em Sistemas Digitais.

**Verificação:** a expressão foi testada nas 16 combinações (Python): vale 1 exatamente quando os números de 2 bits são iguais.
