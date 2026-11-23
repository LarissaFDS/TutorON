---
id: cg-transformacoes-3d-rotacao-em-torno-dos-eixos-projecao-ortografica-e-perspectiva-anomalias-pontos-de-fuga
titulo: Transformações 3D (translação, escala e rotação em torno de x, y e z, matrizes 4×4); projeções ortográfica e perspectiva; anomalias perspectivas: encurtamento, pontos de fuga, confusão visual, distorção topológica
assunto: cg-02-transformacoes-projecao-e-recorte
tipo: prova
questao: prova bimestral I.2 (questão 1), AB2 de 2021.2 (questão 1) e aulas de Transformações 3D e Observação de Cenas 3D
resolucao: sim
fonte: Exercícios e provas de Computação Gráfica do Prof. Marcelo Costa Oliveira (IC-UFAL)
curso: Ciência da Computação (UFAL), COMP381 Computação Gráfica; aulas de 2012 a 2017 e provas de 2014 e 2021.2 (Prof. Marcelo Costa Oliveira)
fontes_catalogo: ufal-marcelo-aulas-cg,ufal-cg-provas-exercicios
autoria: Questões do Prof. Marcelo Costa Oliveira (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Gráfica (IC-UFAL), prova bimestral I.2 (questão 1), AB2 de 2021.2 (questão 1) e aulas de Transformações 3D e Observação de Cenas 3D (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**3D em coordenadas homogêneas:** matrizes $4 \times 4$. Rotações (ângulo $\theta$, regra da mão direita):
$$R_x=\begin{bmatrix}1&0&0&0\\0&\cos\theta&-\sin\theta&0\\0&\sin\theta&\cos\theta&0\\0&0&0&1\end{bmatrix},\ R_y=\begin{bmatrix}\cos\theta&0&\sin\theta&0\\0&1&0&0\\-\sin\theta&0&\cos\theta&0\\0&0&0&1\end{bmatrix},\ R_z=\begin{bmatrix}\cos\theta&-\sin\theta&0&0\\\sin\theta&\cos\theta&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}$$
Atenção ao sinal de $R_y$: o $-\sin\theta$ fica embaixo.

**Achar eixo e ângulo de uma rotação dada** (reavaliação de 2014.2): o eixo é a coordenada que fica fixa (linha e coluna com 1); o ângulo sai de $\cos\theta$ e $\sin\theta$ na matriz.

**Projeção:** leva a cena 3D ao plano de projeção (2D).
- **Ortográfica (paralela):** projetores paralelos entre si e perpendiculares ao plano; preserva medidas e paralelismo; usada em engenharia (vistas frontal, lateral, superior).
- **Perspectiva:** projetores convergem para o **centro de projeção**; o tamanho projetado cai com a distância, o que dá realismo. Com o centro na origem e o plano em $z = d$: $x_p = \dfrac{d\,x}{z}$, $y_p = \dfrac{d\,y}{z}$.

**Anomalias perspectivas:**
- **encurtamento perspectivo:** quanto mais longe, menor;
- **pontos de fuga:** retas paralelas não paralelas ao plano parecem se encontrar num ponto;
- **confusão visual:** objetos atrás do centro de projeção aparecem invertidos;
- **distorção topológica:** pontos no plano que contém o centro de projeção vão para o infinito; paralelismo, ângulos e distâncias não se preservam.

**Verificação:** `test_rotacoes_e_perspectiva` confere com NumPy que as rotações são ortogonais com determinante 1, que $R_x(90°)$ leva $y$ em $z$ e que a perspectiva reduz à metade um objeto com o dobro da distância.
