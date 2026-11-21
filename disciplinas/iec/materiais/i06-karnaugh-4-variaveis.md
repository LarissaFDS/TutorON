---
id: iec-karnaugh-4-variaveis
titulo: Mapa de Karnaugh de 4 variáveis: quadras, pares, cantos e termos isolados
assunto: iec-08-simplificacao-karnaugh
tipo: material_estudo
resolucao: sim
fonte: Slides Álgebra de Boole e Simplificação de Circuitos Lógicos, Prof. José Augusto Baranauskas (FFCLRP-USP), slides 71 a 94 (soluções dos slides 90 e 94)
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

Com 4 variáveis o mapa tem 16 células: linhas $AB$ e colunas $CD$, ambas em ordem Gray (00, 01, 11, 10). Bordas opostas são vizinhas, e os **quatro cantos** formam uma quadra. Procure oitavas, depois quadras, pares e isolados.

**Exemplo A:** $S=\sum m(1,3,4,5,6,7,10,15)$ (ordem ABCD; m10 = 1010 = $A\overline{B}C\overline{D}$).
- Quadra $\overline{A}B$ (m4, m5, m6, m7).
- Quadra $\overline{A}D$ (m1, m3, m5, m7).
- Par $BCD$ (m7, m15).
- Isolado $A\overline{B}C\overline{D}$ (m10).
$S=\overline{A}D+\overline{A}B+BCD+A\overline{B}C\overline{D}$.

**Exemplo B:** $S=\sum m(0,1,2,5,8,9,10,13,15)$.
- Quadra $\overline{C}D$ (m1, m5, m9, m13, coluna inteira).
- Quadra dos cantos $\overline{B}\,\overline{D}$ (m0, m2, m8, m10).
- Par $ABD$ (m13, m15).
$S=\overline{C}D+\overline{B}\,\overline{D}+ABD$.

Irrelevâncias (x, "don't care") entram num grupo só se ajudarem a aumentá-lo.

**Verificação:** as duas expressões foram comparadas com a lista de mintermos nas 16 combinações (Python): batem em todas.
