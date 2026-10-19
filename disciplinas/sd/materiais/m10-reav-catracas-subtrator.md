---
id: sd-reav-q1-q3
titulo: Reavaliação — catracas com prioridade A > B > C > D e subtrator sem sinal (Q1 e Q3)
assunto: sd-04-blocos-combinacionais
tipo: prova
resolucao: sim
questao: 1,3
fonte: REAV.pdf | páginas 1 e 3 | questões 1 e 3 (prova fotografada)
fontes_catalogo: ufal-sd-reav
autoria: Enunciados: reavaliação da disciplina (UFAL). Resoluções: equipe TutorON, conferidas por código
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: aprovado
---
Reavaliação (REAV) — Sistemas Digitais

1. (2,0) O restaurante de uma universidade terá catracas eletrônicas com circuitos combinatórios: (i) quatro filas A, B, C e D; (ii) sensores valem 1 quando há cliente na fila e 0 quando está vazia; (iii) fila vazia tem a catraca travada, com prioridade A > B > C > D; (iv) no máximo duas catracas abertas ao mesmo tempo, respeitando a prioridade; (v) as catracas de A, B, C e D são C1, C2, C3 e C4; (vi) saída 1 = catraca aberta, 0 = fechada. Crie o circuito.

Resolução: abrem as duas filas não vazias de maior prioridade.
- C1 = A (A nunca tem ninguém à frente).
- C2 = B (à frente de B só pode haver A: no máximo uma catraca aberta antes).
- C3 = C·(A·B)' (C abre se A e B não estiverem as duas ocupadas).
- C4 = D·(A'B' + A'C' + B'C') (D abre se no máximo uma entre A, B e C estiver ocupada).
**Verificação:** comparando com a regra "abrir as duas primeiras filas ocupadas" nas 16 combinações de A, B, C, D, as equações coincidem (teste automatizado).

3. (3,0) Construa um subtrator de 4 bits que recebe dois números de 4 bits e retorna um número de 4 bits. Os números NÃO têm sinal (não estão em complemento de 2) e o segundo é sempre menor que o primeiro, então o resultado é sempre positivo.
Resolução: S = A + B' + 1 com somador de 4 bits, inversores em B e Cin = 1; o vai-um final é descartado. Mesma questão da Prova 1 (questão 5).
