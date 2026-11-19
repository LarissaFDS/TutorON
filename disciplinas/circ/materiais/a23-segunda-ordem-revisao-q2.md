---
id: circ-anot-rlc-revisao-q2
titulo: RLC subamortecido (revisão, questão 2): vc(0⁻) = −8 V, α = 3, ωd = 4, vc = e^(−3t)(4 cos 4t + 3 sen 4t) − 12
assunto: circ-08-segunda-ordem
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Circuitos de Segunda Ordem" (18 jun. 2026), lista de revisão, revisão questão 2
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

**Condições iniciais:** antes da comutação, regime CC: $v_C(0^-) = -8$ V (o + do capacitor fica no terminal de baixo) e $dv_C/dt(0^+) = 0$, pois a corrente no indutor era nula. Depois da chave, o valor final é $v_C(\infty) = -12$ V.

**Equação:** $\dfrac{d^2 v_C}{dt^2} + 6\dfrac{dv_C}{dt} + 25 v_C = -300$. Logo $\alpha = 3$ e $\omega_0 = 5$; como $\alpha < \omega_0$, é **subamortecido**, com
$$\omega_d = \sqrt{\omega_0^2 - \alpha^2} = \sqrt{25 - 9} = 4\ \text{rad/s}.$$

**Solução:** natural mais final,
$$v_C(t) = e^{-3t}(B_1\cos4t + B_2\sin4t) - 12 .$$
De $v_C(0) = -8$: $B_1 = 4$. De $v_C'(0) = -3B_1 + 4B_2 = 0$: $B_2 = 3$.
$$v_C(t) = e^{-3t}(4\cos4t + 3\sin4t) - 12\ \text{V}.$$
Oscila em 4 rad/s, com envoltória $e^{-3t}$, em torno de −12 V.

**Verificação:** $v_C(0) = 4 - 12 = -8$ ✓; $v_C'(0) = -12 + 12 = 0$ ✓; `dsolve` confirma.
