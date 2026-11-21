---
id: iec-fracoes-binarias-ieee754
titulo: Frações em binário (multiplicações por 2) e ponto flutuante IEEE 754 de 32 bits: 37,21875 e 0,3125
assunto: iec-06-representacao-dados
tipo: prova
questao: 3
semestre: 2016.1
resolucao: sim
fonte: Fotos da Reavaliação AB1 de Introdução à Engenharia de Computação (ECOM006), UFAL, 2016.1, Q3
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

**Enunciado (Reavaliação AB1, Q3):** converter 37,21875 e 0,3125 para binário (no máximo 5 bits de fração) e escrever em ponto flutuante IEEE 754.

**Parte fracionária: multiplicações sucessivas por 2**; a parte inteira de cada produto é o próximo bit.
- 0,21875: ×2 = 0,4375 (0); 0,875 (0); 1,75 (1); 1,5 (1); 1,0 (1). Fração 0,00111 (= 7/32, exata em 5 bits).
- 37 = 100101. Logo 37,21875 = 100101,00111.
- 0,3125: 0,625 (0); 1,25 (1); 0,5 (0); 1,0 (1). Logo 0,0101.

**IEEE 754, precisão simples (32 bits):** 1 bit de sinal, 8 de expoente com **excesso 127** e 23 de fração (sem o 1 implícito). Normalize para $1{,}f\times2^e$.
- $100101{,}00111=1{,}0010100111\times2^{5}$; expoente $5+127=132=10000100$; fração 0010100111 seguida de zeros. Resultado 0 10000100 00101001110000000000000 = **0x4214E000**.
- $0{,}0101=1{,}01\times2^{-2}$; expoente $-2+127=125=01111101$; fração 01 e zeros. Resultado 0 01111101 01000000000000000000000 = **0x3EA00000**.

**Verificação:** $(1+2^{-3}+2^{-5}+2^{-8}+2^{-9}+2^{-10})\cdot2^5=37{,}21875$ e $1{,}25\cdot2^{-2}=0{,}3125$; os padrões de bits conferem com o módulo struct do Python.
