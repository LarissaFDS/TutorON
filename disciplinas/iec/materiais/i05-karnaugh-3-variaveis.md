---
id: iec-karnaugh-3-variaveis
titulo: Mapa de Karnaugh (Veitch-Karnaugh) de 3 variáveis: exercícios resolvidos
assunto: iec-08-simplificacao-karnaugh
tipo: material_estudo
resolucao: sim
fonte: Slides Álgebra de Boole e Simplificação de Circuitos Lógicos, Prof. José Augusto Baranauskas (FFCLRP-USP), slides 28 a 70 (exercícios dos slides 62 a 70)
fontes_catalogo: usp-baranauskas-boole
autoria: Prof. José Augusto Baranauskas (USP), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

Mapa de 3 variáveis: linhas $A=0$ e $A=1$; colunas $BC$ na ordem **Gray** 00, 01, 11, 10 (vizinhas diferem num bit; as bordas também são vizinhas). Agrupe os 1s em **quadras** (4), depois **pares** (2), depois isolados, com o menor número de grupos e grupos os maiores possíveis. Cada grupo vira o produto das variáveis que **não mudam** dentro dele.

**Exercício 1:** $S=\sum m(1,3,4,5,6)$.
Mapa (colunas BC = 00 01 11 10): linha $A=0$: 0 1 1 0; linha $A=1$: 1 1 0 1.
Pares: $\overline{A}C$ (m1, m3), $A\overline{B}$ (m4, m5), $A\overline{C}$ (m4, m6, pela borda). $S=\overline{A}C+A\overline{B}+A\overline{C}$. Outra cobertura igualmente mínima: $S=\overline{A}C+\overline{B}C+A\overline{C}$: expressões diferentes, mesma tabela.

**Exercício 2:** $S=\sum m(0,1,3,5,7)$: quadra $C$ (m1, m3, m5, m7) e par $\overline{A}\,\overline{B}$ (m0, m1). $S=C+\overline{A}\,\overline{B}$.

**Exercício 3:** $S=\sum m(0,2,3,7)$: par $\overline{A}\,\overline{C}$ (m0, m2) e par $BC$ (m3, m7). $S=\overline{A}\,\overline{C}+BC$.

Quando nenhum 1 tem vizinho (ex.: $\overline{A}B+A\overline{B}$, o XOR), não há simplificação.

**Verificação:** cada expressão final foi testada nas 8 combinações de A, B, C contra a lista de mintermos (Python): vale 1 só nos mintermos listados.
