---
id: circ-anot-malhas-fonte-dependente
titulo: Análise de malhas (LKT) com fonte de corrente de 4 A e fonte de tensão dependente Vx: correntes de malha e potências (questão 3,5-2)
assunto: circ-02-kirchhoff-nodal-malhas
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Questões circuitos" (1 maio 2026), págs. 4–5 (enunciado de lista colado, parafraseado)
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

**Circuito (descrito), três malhas no sentido horário:**
- malha 1 (esquerda): fonte de 40 V (+ em cima), 2 Ω em cima, 4 Ω vertical no meio, 5 Ω embaixo;
- malha 2 (direita): 1 Ω em cima, fonte de 4 A no ramo direito (seta para cima), 4 Ω embaixo, cuja tensão é $V_x$;
- malha 3 (topo): fonte de tensão dependente de valor $V_x$ (− à esquerda, + à direita) e 13 Ω, sobre os resistores de 2 Ω e 1 Ω.

**Montagem:** a fonte de 4 A está só na malha 2 e a corrente de malha desce por ela: $i_2 = -4$ A (não precisa de supermalha). $V_x = 4 i_2 = -16$ V.
- Malha 1: $-40 + 2(i_1-i_3) + 4(i_1-i_2) + 5i_1 = 0 \Rightarrow 11i_1 - 4i_2 - 2i_3 = 40$.
- Malha 3: $2(i_3-i_1) + 1(i_3-i_2) - V_x + 13 i_3 = 0$.

**Resultado:** $i_1 = 2$ A (horário), $i_2 = -4$ A (4 A anti-horário), $i_3 = -1$ A (1 A anti-horário). Tensão na fonte de 4 A: 43 V.

Potências: a fonte de 4 A fornece $43\cdot 4 = 172$ W; a de 40 V fornece 80 W; a dependente fornece $16\cdot1 = 16$ W. Resistores: 5 Ω 20 W, 4 Ω vertical $(i_1-i_2)^2\cdot4 = 144$ W, 4 Ω de baixo 64 W, 2 Ω $(i_1-i_3)^2\cdot 2 = 18$ W, 1 Ω 9 W, 13 Ω 13 W.

**Verificação:** 172 + 80 + 16 = 268 W = 20 + 144 + 64 + 18 + 9 + 13. Conferido com análise nodal modificada no SymPy.
