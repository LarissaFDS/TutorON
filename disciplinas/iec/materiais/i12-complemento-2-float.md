---
id: iec-complemento-de-2-e-float
titulo: Inteiros de 8 bits em complemento de 2 e soma convertida para float: x = 67, y = −3, z = x + y
assunto: iec-06-representacao-dados
tipo: prova
questao: 2
semestre: 2016.1
resolucao: sim
fonte: Fotos da Reavaliação AB1 de Introdução à Engenharia de Computação (ECOM006), UFAL, 2016.1, Q2
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

**Enunciado (Reavaliação AB1, Q2):** num programa com `int x, y; float z;` e `x = 67; y = -3; z = x + y;`, dar os valores binários de x, y e z, com inteiro de 8 bits em complemento de 2 e float no padrão IEEE 754.

**Complemento de 2 (8 bits, de −128 a 127):** positivo é o binário comum; negativo: escreva o módulo, **inverta todos os bits** e **some 1**.
- $x=67=64+2+1$: **01000011**.
- $y=-3$: $3=00000011$, invertido 11111100, mais 1 = **11111101**.

**Soma inteira** coluna a coluna: 01000011 + 11111101 = 1 01000000; o carry que sai do bit 7 é descartado em 8 bits e não há overflow (somar números de sinais opostos nunca estoura). Resultado 01000000 = 64.

**z = 64.0 em IEEE 754 simples:** $64=1{,}0\times2^{6}$; sinal 0; expoente $6+127=133=10000101$; fração toda zero. z = 0 10000101 00000000000000000000000 = **0x42800000**.

Sistemas de números negativos citados por Tanenbaum: sinal-magnitude, complemento de 1, complemento de 2 e excesso $2^{m-1}$; os computadores atuais usam complemento de 2 para inteiros.

**Verificação:** 11111101 lido em complemento de 2 vale $-128+125=-3$; $67+(-3)=64$; e o float 64.0 empacotado pelo Python dá 42800000 em hexadecimal.
