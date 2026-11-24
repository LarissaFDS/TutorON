---
id: alglin-lista1-axiomas-subespaco-gerado
titulo: Lista 1 — operações que não formam espaço vetorial (axioma 1u = u), subespaço gerado por dois vetores e independência linear de matrizes
assunto: alglin-01-espacos-vetoriais-subespacos
tipo: exercicio_resolvido
resolucao: sim
fonte: Lista 1 de Álgebra Linear (Espaços Vetoriais, UFAL), PDF do material do 2º período de Engenharia de Computação | enunciados parafraseados
curso: Engenharia de Computação (UFAL), ECOM011 Álgebra Linear, 2º período (também no 3º período de Ciência da Computação); semestre não identificado
fontes_catalogo: ufal-alglin-listas
autoria: Enunciados da lista da disciplina; resoluções da equipe TutorON com apoio de IA, conferidas com SymPy e NumPy
licenca: Não declarada (lista da disciplina; PDF não versionado)
publicacao_transcricao: não autorizada; enunciados parafraseados
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Álgebra Linear, Lista 1 (espaços vetoriais). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**1. Operação estranha.** Em $\mathbb R^2$, soma usual e $a\,u = (0, a u_2)$. Com $u = (-1, 2)$, $v = (3, 4)$, $a = 3$: $u + v = (2, 6)$ e $a u = (0, 6)$.
- Fechamento: os dois resultados continuam sendo pares de reais.
- Os axiomas que só envolvem a soma (comutatividade, associatividade, vetor nulo, oposto) valem porque a soma é a de $\mathbb R^2$.
- Falha o axioma $1\,u = u$: $1\cdot(-1, 2) = (0, 2) \ne (-1, 2)$. Basta um contraexemplo para $V$ não ser espaço vetorial.

**3. Subespaço gerado.** $S = [v_1, v_2]$ é um plano pela origem; a normal é $v_1 \times v_2$.
- $v_1 = (-1, 3, -1)$, $v_2 = (1, -2, 4)$: normal $(10, 3, -1)$, $S: 10x + 3y - z = 0$. Para $(5, k, 11) \in S$: $50 + 3k - 11 = 0$, $k = -13$.
- $v_1 = (1, -2, 0)$, $v_2 = (2, -2, -1)$: normal $(2, 1, 2)$, $S: 2x + y + 2z = 0$; $(2, k, 2) \in S$ dá $k = -8$.
Outra forma: o vetor está em $S$ quando $\det[v_1; v_2; w] = 0$.

**6. Matrizes LI.** $a = \begin{pmatrix}1&1\\0&0\end{pmatrix}$, $b = I$, $c = \begin{pmatrix}1&1\\1&1\end{pmatrix}$. De $\alpha a + \beta b + \gamma c = 0$: a entrada $(2,1)$ dá $\gamma = 0$; a $(2,2)$ dá $\beta = 0$; a $(1,2)$ dá $\alpha = 0$. Só a solução trivial: LI (posto 3 ao escrever as matrizes como vetores de $\mathbb R^4$).

Erro comum: testar só a soma e esquecer os axiomas do produto por escalar.

**Verificação:** contas, normais, valores de $k$ e posto conferidos com SymPy em `test_lista1_axiomas_gerado_li`.
