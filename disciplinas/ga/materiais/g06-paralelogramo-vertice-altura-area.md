---
id: ga-paralelogramo-area
titulo: Paralelogramo com três vértices A(−2, −3), B(5, 2), C(−1, 3): quarto vértice, altura por projeção e área; área do paralelogramo de (1, 2) e (1, 1)
assunto: ga-01-vetores-operacoes
tipo: prova
questao: 1; 2b
semestre: nao_informado e 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Prova sem cabeçalho (foto), Q1; 1ª Avaliação (11.02.2017), Q2b
fontes_catalogo: ufal-ga-provas-sem-cabecalho,ufal-ga-provas-2017
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

**a) Quarto vértice.** Há três paralelogramos possíveis, conforme qual vértice é oposto a qual: $D = B + C - A = (6, 8)$, $D = A + C - B = (-8, -2)$ ou $D = A + B - C = (4, -4)$. A seguir, $D = (6, 8)$, com lados $\overrightarrow{AB} = (7, 5)$ e $\overrightarrow{AC} = (1, 6)$.

**b) Altura por projeção.** A altura relativa ao lado AB é a parte de $\overrightarrow{AC}$ perpendicular a AB.
- Projeção: $\dfrac{\overrightarrow{AC}\cdot\overrightarrow{AB}}{\|\overrightarrow{AB}\|^2}\overrightarrow{AB} = \tfrac{37}{74}(7,5) = (\tfrac72, \tfrac52)$.
- $\mathbf{h} = \overrightarrow{AC} - (\tfrac72, \tfrac52) = (-\tfrac52, \tfrac72)$, $\|\mathbf{h}\| = \tfrac{\sqrt{74}}{2}$.

**c) Área.** Base vezes altura: $\sqrt{74}\cdot\tfrac{\sqrt{74}}{2} = 37$. No plano, a área também é $\left|\det\begin{pmatrix}7 & 5\\ 1 & 6\end{pmatrix}\right| = |42 - 5| = 37$.

**1ª Avaliação de 2017, Q2b.** Paralelogramo de $\mathbf{v} = (1, 2)$ e $\mathbf{u} = (1, 1)$: área $|1\cdot1 - 2\cdot1| = 1$.

**Verificação:** $\mathbf{h}\cdot\overrightarrow{AB} = -\tfrac{35}{2} + \tfrac{35}{2} = 0$; o produto vetorial de (7, 5, 0) e (1, 6, 0) é (0, 0, 37), de norma 37.
