---
id: ga-plano-tres-pontos
titulo: Como achar a equação do plano por três pontos com o produto vetorial e a distância de um ponto ao plano: A(1, 2, 2), B(0, −1, 3), C(3, −1, 1), P(4, 2, 3); A(2, 0, 1), B(0, 1, 0), C(1, 1, 1), P(1, 2, 3)
assunto: ga-05-distancias-angulos-espaco
tipo: prova
questao: vários
semestre: 2016.2 e 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Final (14.11.2016), Q7; P2 (15.10.2016), Q3b; Reavaliação AB2 (24.05.2017), Q4a; P2 Adventistas, Q5; Reposição 2, Q1c
fontes_catalogo: ufal-ga-provas-2016,ufal-ga-provas-2017
autoria: Enunciados: provas de Geometria Analítica do Instituto de Matemática da UFAL (ver fontes_catalogo), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

**Plano por três pontos não colineares.** Vetores no plano: $\overrightarrow{AB}$ e $\overrightarrow{AC}$. Vetor normal: $\mathbf{n} = \overrightarrow{AB}\times\overrightarrow{AC}$ (se der $\mathbf{0}$, os pontos são colineares e não definem um plano). Forma geral: $\mathbf{n}\cdot(X - A) = 0$.

**Final 2016, Q7.** $\overrightarrow{AB} = (-1,-3,1)$, $\overrightarrow{AC} = (2,-3,-1)$, $\mathbf{n} = (6, 1, 9)$; forma geral $6x + y + 9z = 26$.
- a) Distância a P(4, 2, 3): $\dfrac{|24 + 2 + 27 - 26|}{\sqrt{118}} = \dfrac{27}{\sqrt{118}} \approx 2{,}49$.
- b) Reta $x = 1 - t$, $y = 2 + 3t$, $z = 2 + t$: $6(1 - t) + (2 + 3t) + 9(2 + t) = 26 + 6t = 26$, $t = 0$, ponto (1, 2, 2) = A.

**Reavaliação AB2, Q4a.** $\overrightarrow{AB} = (-2,1,-1)$, $\overrightarrow{AC} = (-1,1,0)$, $\mathbf{n} = (1, 1, -1)$, plano $x + y - z = 1$; distância de P(1, 2, 3): $\dfrac{|1 + 2 - 3 - 1|}{\sqrt3} = \dfrac{1}{\sqrt3}$.

**Outros dados de prova:** P(1, 4, −1) ao plano $3x - 2y + z = 2$: $\dfrac{8}{\sqrt{14}}$. D(4, 2, 2) ao plano de A(1,2,2), B(1,−1,3), C(−3,0,3): $\dfrac{3}{\sqrt{161}}$.

Erro comum: esquecer de dividir pela norma do vetor normal.

**Verificação:** A, B e C satisfazem $6x + y + 9z = 26$ (6 + 2 + 18; 0 − 1 + 27; 18 − 1 + 9); o ponto $P - \tfrac{27}{118}(6,1,9)$ cai no plano.
