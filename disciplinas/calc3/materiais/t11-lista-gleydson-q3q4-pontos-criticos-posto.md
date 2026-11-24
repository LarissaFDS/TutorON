---
id: calc3-lista-gleydson-q3q4-pontos-criticos-posto
titulo: Lista de Cálculo III (Prof. Gleydson), Q3 e Q4 — pontos críticos de f(x, y) = (x², y³ + xy²) pelo determinante da jacobiana; jacobiana 3 × 2 de posto 2 não dá ponto crítico
assunto: calc3-11-maximos-minimos-lagrange
tipo: lista
questao: 3 e 4
resolucao: sim
fonte: Lista de Cálculo III (Instituto de Computação, UFAL; Prof. Gleydson Santos da Silva; arquivo P3C3, atividade para nota extra), questões 3 e 4 | enunciado parafraseado
autoria: Enunciado: Prof. Gleydson Santos da Silva (IC-UFAL); resolução da equipe TutorON, conferida com SymPy
licenca: Não declarada (lista da disciplina); o PDF não está no repositório
publicacao_transcricao: não autorizada até agora; enunciado parafraseado
fontes_catalogo: ufal-calc3-lista-gleydson-p3
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista de Cálculo III do Prof. Gleydson Santos da Silva (IC/UFAL, ECOM017), questões 3 e 4, parafraseadas. Status da resolução: validada (contas conferidas com SymPy em `tests_acervo/test_disciplina_calc3.py`). A resolução é da equipe TutorON e não é gabarito do professor.

**Ideia.** Para $f:\mathbb R^n\to\mathbb R^m$, um ponto é **crítico** quando a jacobiana não tem posto máximo, $\text{posto}\,J_f < \min(n, m)$. Com $n = m$, isso é $\det J_f = 0$.

**Q3.** $f(x,y) = (x^2,\ y^3 + xy^2)$:
$$J_f = \begin{pmatrix} 2x & 0 \\ y^2 & 3y^2 + 2xy\end{pmatrix},\qquad \det J_f = 2x(3y^2 + 2xy) = 2xy\,(3y + 2x).$$
Zera em três retas: $x = 0$, $y = 0$ e $y = -\frac{2x}{3}$. Todos os pontos dessas retas são críticos (não são pontos isolados).

**Q4.** Uma função $f:\mathbb R^2\to\mathbb R^3$ tem jacobiana $3\times2$ em $(1,2,3)$ com colunas $(1, -3, 5)$ e $(2, 5, -1)$. O posto máximo é $\min(2,3) = 2$. As colunas não são proporcionais: se $(2,5,-1) = k(1,-3,5)$, a primeira entrada dá $k = 2$ e a segunda daria $5 = -6$. Também basta um menor $2\times2$ não nulo: $1\cdot5 - 2\cdot(-3) = 11 \ne 0$. Posto 2, então **não** é ponto crítico.

Observação: o enunciado chama o ponto de $(1,2,3)$, com três coordenadas, embora o domínio seja $\mathbb R^2$; a conclusão depende só da matriz dada.

**Verificação:** `test_lista_gleydson_q3q4` confere o determinante, as três retas e o posto da matriz.
