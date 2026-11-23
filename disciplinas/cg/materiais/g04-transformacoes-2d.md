---
id: cg-transformacoes-2d-coordenadas-homogeneas-translacao-rotacao-escala-espelhamento-composicao-de-matrizes
titulo: Transformações geométricas 2D em coordenadas homogêneas: translação, rotação, escala, espelhamento e cisalhamento; composição de matrizes e rotação em torno de um ponto qualquer; AB1 de 2021.2
assunto: cg-02-transformacoes-projecao-e-recorte
tipo: prova
questao: AB1 de 2021.2, questão 1, e exercício de composição de matrizes
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
Computação Gráfica (IC-UFAL), AB1 de 2021.2, questão 1, e exercício de composição de matrizes (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Coordenadas homogêneas:** o ponto $(x, y)$ vira $(x, y, 1)$, e toda transformação afim vira uma matriz $3 \times 3$; assim a translação também é um produto.

$$T(d_x,d_y)=\begin{bmatrix}1&0&d_x\\0&1&d_y\\0&0&1\end{bmatrix},\quad R(\theta)=\begin{bmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{bmatrix},\quad S(s_x,s_y)=\begin{bmatrix}s_x&0&0\\0&s_y&0\\0&0&1\end{bmatrix}$$

Espelhamento no eixo $y$: $S(-1, 1)$; no eixo $x$: $S(1, -1)$.

**Composição:** a primeira transformação aplicada fica **mais à direita**: aplicar $A$ e depois $B$ é $M = B \cdot A$. A ordem importa: rotação e translação não comutam.

**Em torno de um ponto $P$:** $M = T(P)\,R(\theta)\,T(-P)$ (leva $P$ à origem, gira, volta).

**AB1 de 2021.2:**
- a) translação de 4 para a direita e 2 para baixo, depois rotação de 45° na origem: $M = R(45°)\,T(4,-2)$;
- b) rotação de 30° em torno de $P(4,5)$, depois escala 2 em $x$ e 4 em $y$: $M = S(2,4)\,T(4,5)\,R(30°)\,T(-4,-5)$;
- c) espelhamento na reta por $A(1,3)$ e $B(1,0)$, que é $x = 1$, depois ampliação de 3: $M = S(3,3)\,T(1,0)\,S(-1,1)\,T(-1,0)$, ou seja, $x' = 3(2 - x)$ e $y' = 3y$.

Confira sempre aplicando $M$ a um ponto conhecido: em (c), $A(1,3)$ fica na reta e vai para $(3, 9)$.

**Verificação:** `test_composicao_2d` monta as três matrizes com NumPy e confere a ordem, o ponto fixo da rotação em torno de $P$ e a imagem de $A$ em (c).
