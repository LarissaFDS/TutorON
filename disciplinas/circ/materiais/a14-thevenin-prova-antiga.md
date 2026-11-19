---
id: circ-anot-thevenin-prova-antiga
titulo: Questão de prova antiga: Thévenin com fonte de tensão controlada por corrente 6i₀ e fonte de teste (Vth = −4 V, Rth = 6 Ω)
assunto: circ-04-thevenin-norton
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Questões para a prova 2" (17 maio 2026), questão de prova antiga; repetida em "Questões circuitos", págs. 12–13
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

**Circuito (descrito):** fonte de 2 A (para cima) em paralelo com 4 Ω (corrente $i_0$ para baixo) no nó 1; do nó 1, fonte de tensão dependente $6i_0$ (+ do lado do nó 1) e 8 Ω até o terminal a; b no terra.

**Tensão em aberto:** sem corrente no 8 Ω, os 2 A passam todos pelo 4 Ω: $i_0 = 2$ A, $v_1 = 8$ V, e a dependente vale $6i_0 = 12$ V, com queda de 12 V no sentido de a:
$$V_{Th} = v_1 - 12 = -4\text{ V}.$$

**Resistência com fonte de teste:** desligue a fonte de 2 A (aberta) e mantenha $6i_0$. Injetando $I_T$ em a, a corrente percorre 8 Ω e a dependente e desce pelo 4 Ω: $i_0 = I_T$.
$$V_T = 8I_T - 6i_0 + 4i_0 = 8I_T - 6I_T + 4I_T = 6I_T \Rightarrow R_{Th} = 6\ \Omega .$$

**Resultado:** fonte de 4 V com o + voltado para b, em série com 6 Ω.

**Verificação:** curto em a–b: LKT na malha, $4i_0 - 6i_0 - 8(2 - i_0) = 0$ dá $i_0 = \tfrac{8}{3}$ A e $I_{cc} = 2 - i_0 = -\tfrac{2}{3}$ A; $V_{Th}/I_{cc} = 6$ Ω. Conferido no SymPy. Nas anotações há, logo depois, um circuito de 8 V, 16 Ω e fonte de 40 V sem enunciado; ele não entrou no acervo.
