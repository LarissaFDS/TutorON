---
id: iec-circuito-para-tabela-verdade
titulo: Do circuito com portas à tabela-verdade e ao circuito simplificado (F de A, B, C)
assunto: iec-07-portas-boole
tipo: prova
questao: 4
semestre: 2016.1
resolucao: sim
fonte: Fotos da Reavaliação AB1 de Introdução à Engenharia de Computação (ECOM006), UFAL, 2016.1, Q4
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

**Enunciado (Reavaliação AB1, Q4):** dado um circuito de entradas A, B, C, achar a tabela-verdade e desenhar, a partir dela, o circuito correspondente.

**Circuito (descrição em texto):**
- G1: porta OR com as três entradas invertidas (bolinhas em A, B, C) e saída invertida: $G_1=\overline{\overline{A}+\overline{B}+\overline{C}}=ABC$ (De Morgan).
- G2: XNOR de A e C. G3: AND de G2 com $\overline{A}$ (bolinha na entrada): $G_3=\overline{A\oplus C}\cdot\overline{A}=\overline{A}\,\overline{C}$.
- G4: AND de A com $\overline{B}$. G5: OR de G4 com B: $A\overline{B}+B=A+B$. G6: AND de G5 com C: $(A+B)C$.
- F: OR de G1, G3 e G6.

**Método:** uma coluna por porta intermediária.

| A B C | G1 | G3 | G6 | F |
|---|---|---|---|---|
| 000 | 0 | 1 | 0 | 1 |
| 001 | 0 | 0 | 0 | 0 |
| 010 | 0 | 1 | 0 | 1 |
| 011 | 0 | 0 | 1 | 1 |
| 100 | 0 | 0 | 0 | 0 |
| 101 | 0 | 0 | 1 | 1 |
| 110 | 0 | 0 | 0 | 0 |
| 111 | 1 | 0 | 1 | 1 |

$F=\sum m(0,2,3,5,7)$. Karnaugh: par $\overline{A}\,\overline{C}$ (m0, m2), par $AC$ (m5, m7), par $BC$ (m3, m7): $F=\overline{A}\,\overline{C}+AC+BC$, ou seja $\overline{A\oplus C}+BC$. Circuito novo: uma XNOR de A e C, uma AND de B e C e uma OR de duas entradas.

**Verificação:** o circuito original, porta a porta, e a expressão simplificada dão a mesma saída nas 8 combinações (Python).
