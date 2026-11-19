---
id: circ-anot-rlc-revisao-q1
titulo: Capacitor carregado e chave que abre (revisão, questão 1): vc(0⁻) = 24 V, RLC criticamente amortecido, i = −9,6t e^(−20t)
assunto: circ-08-segunda-ordem
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Circuitos de Segunda Ordem" (18 jun. 2026), lista de revisão, revisão questão 1
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Circuitos Elétricos 2026.1, Prof. Jobson de Araújo Nascimento, IC/UFAL); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-circ-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Condições iniciais depois que a chave abre:** antes, em regime CC, o capacitor estava carregado pelo divisor da fonte: $v_C(0^-) = 24$ V; o indutor não conduzia, $i_L(0^-) = 0$. A chave abre em $t = 0$ e, como $v_C$ e $i_L$ não saltam, $v_C(0^+) = 24$ V e $i(0^+) = 0$.

**Circuito depois:** fica só a malha RLC série sem fonte (resposta natural), com $\alpha = \omega_0 = 20$: **amortecimento crítico**, $i(t) = (A_1 + A_2t)e^{-20t}$.

**Constantes:** $i(0) = 0 \Rightarrow A_1 = 0$. A derivada vem da LKT em $0^+$: $L\,\dfrac{di}{dt}(0^+) = -v_C(0^+) - Ri(0^+) = -24$ V, o que dá $A_2 = -9{,}6$ A/s para o $L$ da questão.

$$i(t) = -9{,}6\,t\,e^{-20t}\ \text{A}.$$
O sinal negativo indica que a corrente circula no sentido oposto ao arbitrado: o capacitor descarrega.

**Correção:** as anotações param antes de determinar a segunda constante; a equipe completou a conta.

**Verificação:** `dsolve` com $i(0) = 0$ e $i'(0) = -24/L$ devolve $-9{,}6te^{-20t}$.
