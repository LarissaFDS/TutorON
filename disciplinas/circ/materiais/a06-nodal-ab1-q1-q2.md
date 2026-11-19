---
id: circ-anot-nodal-ab1-q1-q2
titulo: Lista AB1, questões 1 e 2: análise nodal com fonte de corrente controlada por corrente (2i₀)
assunto: circ-02-kirchhoff-nodal-malhas
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Lista para AB1" (1 maio 2026), lista do Prof. Jobson de Araújo Nascimento, págs. 1–3
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Circuitos Elétricos 2026.1, Prof. Jobson de Araújo Nascimento, IC/UFAL); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-circ-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Questão 1 (descrita):** fonte de 27 V (+ em cima) entre o nó direito e o terra, então esse nó está a 27 V. Nó $v_1$ à esquerda: 3 Ω até o nó de 27 V (por cima), 1 Ω até o nó $v_0$, 2 Ω ao terra com corrente $i_0$ para baixo. Nó $v_0$: 2 Ω até o nó de 27 V e fonte dependente $2i_0$ do terra para $v_0$.
$$\frac{v_1-27}{3} + \frac{v_1}{2} + (v_1 - v_0) = 0 \Rightarrow 11v_1 - 6v_0 = 54$$
$$\frac{v_0-27}{2} - 2i_0 + (v_0 - v_1) = 0,\quad i_0 = \frac{v_1}{2} \Rightarrow v_0 = \frac{27 + 4v_1}{3}$$
$v_1 = 36$ V, $v_0 = 57$ V, $i_0 = 18$ A. A fonte dependente (36 A) fornece $57\cdot 36 = 2052$ W e a de 27 V **absorve** 486 W.

**Questão 2 (descrita):** nós $v_0$ (esquerda), $v_1$ (meio) e $v_2$ (direita). 1 Ω entre $v_0$ e $v_2$ (por cima); fonte de 4 A de $v_0$ para $v_1$; fonte dependente $2i_0$ de $v_1$ para $v_2$; 8 Ω de $v_0$ ao terra ($i_0$ para baixo), 2 Ω de $v_1$ e 4 Ω de $v_2$ ao terra.
Nó $v_0$: $\dfrac{v_0}{8} + (v_0 - v_2) + 4 = 0$; nó $v_2$: $(v_2 - v_0) - 2\dfrac{v_0}{8} + \dfrac{v_2}{4} = 0 \Rightarrow v_2 = v_0$.
$v_0 = v_2 = -32$ V, $i_0 = -4$ A, $v_1 = 24$ V.

**Verificação:** Q1: a soma das potências é zero. Q2: o 1 Ω não conduz ($v_0 = v_2$); LKC em $v_1$: chegam 4 A, saem 12 A pelo 2 Ω e $2i_0 = -8$ A pela dependente. Conferido no SymPy.
