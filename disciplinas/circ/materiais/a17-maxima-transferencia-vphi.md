---
id: circ-anot-maxima-transferencia-vphi
titulo: Máxima transferência com fonte dependente vφ (lista 4, questão 2): Vth = 120 V, Rth = 3 Ω pela fonte de teste, Pmáx = 1,2 kW
assunto: circ-05-maxima-transferencia
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Máxima Transferência de Potência" (28 abr. 2026), lista 4, questão 2
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

**Circuito (descrito):** fonte de 100 V (+ em cima) no nó L. Ramo de cima: fonte dependente de valor $v_\phi$ (− do lado de L, + do outro) e 4 Ω até a. Ramo do meio: 4 Ω de L até o nó m e 4 Ω de m até a. Do nó m ao terra: 4 Ω (com $v_\phi$, + em m) e fonte de 20 V (+ em cima). A carga $R$ fica entre a e b (terra).

**Tensão em aberto (malhas horárias):** malha de cima $i_1$, malha de baixo $i_2$:
$$-v_\phi + 4i_1 + 4i_1 + 4(i_1 - i_2) = 0, \qquad -100 + 4(i_2 - i_1) + 4i_2 + 20 = 0,\qquad v_\phi = 4i_2.$$
Daí $i_1 = 10$ A, $i_2 = 15$ A, $v_\phi = 60$ V, e por um caminho de a até b: $V_{Th} = 120$ V.

**Resistência com fonte de teste** (100 V e 20 V em curto; a dependente fica): com $V_T$ em a, LKC no nó m dá $v_\phi = V_T/3$, e LKC em a,
$$I_T = \frac{V_T - v_\phi}{4} + \frac{V_T - v_\phi}{4} + \frac{V_T}{4}\cdot 0 \ \Rightarrow\ R_{Th} = \frac{V_T}{I_T} = 3\ \Omega .$$
(As anotações chegam a $4V_T = 12 I_T$.)

$$R = R_{Th} = 3\ \Omega,\qquad P_{max} = \frac{120^2}{4\cdot 3} = 1200\text{ W} = 1{,}2\text{ kW}.$$

**Verificação:** análise nodal com fonte de teste no SymPy: $V_{Th} = 120$ V e $R_{Th} = 3$ Ω.
