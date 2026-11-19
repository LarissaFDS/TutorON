---
id: circ-anot-rlc-ab2-q2
titulo: RLC superamortecido com fonte (AB2, questão 2): condições iniciais vc(0⁻) = 3 V e iL(0⁻) = 1 A, iL = 2 − 2e^(−2t) + e^(−4t)
assunto: circ-08-segunda-ordem
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Lista para AB 2" (16 jun. 2026), lista do Prof. Jobson de Araújo Nascimento, questão 2
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

**Condições iniciais:** em regime CC antes da chave, o capacitor é um circuito aberto e o indutor um curto. Das anotações: $v_C(0^-) = 3$ V e $i_L(0^-) = 1$ A; como não saltam, valem o mesmo em $0^+$.

**Equação (depois da chave):** escrevendo LKC e LKT com a corrente $i_L$ como variável, as anotações chegam a
$$\frac{d^2 i_L}{dt^2} + 6\frac{di_L}{dt} + 8 i_L = 16 .$$
Daí $2\alpha = 6$, $\alpha = 3$ e $\omega_0 = \sqrt8 \approx 2{,}83$: $\alpha > \omega_0$, **superamortecido**, raízes $s = -2$ e $s = -4$.

**Solução:** particular $i_L(\infty) = 16/8 = 2$ A; natural $A_1e^{-2t} + A_2e^{-4t}$. Com $i_L(0) = 1$ e $i_L'(0) = 0$ (da tensão inicial no indutor):
$$i_L(t) = 2 - 2e^{-2t} + e^{-4t}\ \text{A}, \qquad v_s = 3\,i_L .$$

**Verificação:** $i_L(0) = 2 - 2 + 1 = 1$ ✓; $i_L'(0) = 4 - 4 = 0$ ✓; $i_L(\infty) = 2$ ✓. `dsolve` confirma.
