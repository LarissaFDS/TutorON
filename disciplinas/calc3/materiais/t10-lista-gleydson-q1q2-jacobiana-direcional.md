---
id: calc3-lista-gleydson-q1q2-jacobiana-direcional
titulo: Lista de Cálculo III (Prof. Gleydson), Q1 e Q2 — matriz jacobiana de (sen(xyz), z^(x+y)) e J·u para a função vetorial (tg x, sec y, arctg z) no ponto (π/4, π/4, 0) com u unitário de (−1, 4, 0)
assunto: calc3-09-derivada-direcional-gradiente
tipo: lista
questao: 1 e 2
resolucao: sim
fonte: Lista de Cálculo III (Instituto de Computação, UFAL; Prof. Gleydson Santos da Silva; arquivo P3C3, atividade para nota extra), questões 1 e 2 | enunciado parafraseado
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
Lista de Cálculo III do Prof. Gleydson Santos da Silva (IC/UFAL, ECOM017), questões 1 e 2, parafraseadas. Status da resolução: validada (contas conferidas com SymPy em `tests_acervo/test_disciplina_calc3.py`). A resolução é da equipe TutorON e não é gabarito do professor.

**Q1.** Matriz jacobiana de $f(x,y,z) = (\text{sen}(xyz),\ z^{x+y})$, de $\mathbb R^3$ em $\mathbb R^2$: uma linha por componente, uma coluna por variável (matriz $2\times3$).
$$J_f = \begin{pmatrix} yz\cos(xyz) & xz\cos(xyz) & xy\cos(xyz) \\ z^{x+y}\ln z & z^{x+y}\ln z & (x+y)\,z^{x+y-1}\end{pmatrix}.$$
Cuidado na segunda linha: em $x$ e $y$ o expoente varia ($z^{x+y} = e^{(x+y)\ln z}$, vale para $z > 0$), então aparece $\ln z$; em $z$ é regra da potência.

**Q2.** Para a função vetorial $f(x,y,z) = (\text{tg}\,x,\ \sec y,\ \text{arctg}\,z)$, a taxa de variação ao longo de um vetor unitário $\mathbf u$ é o produto matricial $J_f\,\mathbf u$. A jacobiana é diagonal: $\text{diag}(\sec^2 x,\ \sec y\,\text{tg}\,y,\ \frac{1}{1+z^2})$, e em $(\frac\pi4, \frac\pi4, 0)$ vale $\text{diag}(2,\ \sqrt2,\ 1)$.

Normalize o vetor dado: $\|(-1,4,0)\| = \sqrt{17}$, $\mathbf u = \frac{1}{\sqrt{17}}(-1, 4, 0)$. Então
$$D_{\mathbf u}f\left(\tfrac\pi4, \tfrac\pi4, 0\right) = \left(-\tfrac{2}{\sqrt{17}},\ \tfrac{4\sqrt2}{\sqrt{17}},\ 0\right).$$
Dúvida comum: usar $\mathbf v$ sem normalizar dá $(-2, 4\sqrt2, 0)$, que é a taxa por unidade de parâmetro ao longo de $\mathbf v$, não por unidade de distância; a definição pede vetor unitário.

**Verificação:** `test_lista_gleydson_q1q2` refaz a jacobiana com SymPy e o produto $J\mathbf u$ no ponto.
