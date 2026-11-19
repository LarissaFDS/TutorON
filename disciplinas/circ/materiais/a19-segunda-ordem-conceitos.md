---
id: circ-anot-segunda-ordem-conceitos
titulo: Circuitos RLC de segunda ordem: equação característica, α, ω₀, amortecimento supercrítico, crítico e subamortecido, condições iniciais
assunto: circ-08-segunda-ordem
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Circuitos de Segunda Ordem" (18 jun. 2026), lista de revisão
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

**Ideia:** um circuito com um indutor e um capacitor (que não se reduzem a um só) dá uma equação diferencial de segunda ordem. Na forma padrão,
$$\frac{d^2x}{dt^2} + 2\alpha\frac{dx}{dt} + \omega_0^2 x = f(t),$$
a derivada segunda, mais duas vezes alfa vezes a derivada, mais ômega zero ao quadrado vezes a variável, é igual à excitação.

**Parâmetros:** RLC série: $\alpha = \dfrac{R}{2L}$; RLC paralelo: $\alpha = \dfrac{1}{2RC}$; nos dois, $\omega_0 = \dfrac{1}{\sqrt{LC}}$. As raízes são $s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$.

**Três casos (resposta natural):**
- $\alpha > \omega_0$ (superamortecido): $x = A_1e^{s_1t} + A_2e^{s_2t}$;
- $\alpha = \omega_0$ (crítico): $x = (A_1 + A_2t)e^{-\alpha t}$;
- $\alpha < \omega_0$ (subamortecido): $x = e^{-\alpha t}(B_1\cos\omega_d t + B_2\sin\omega_d t)$, com $\omega_d = \sqrt{\omega_0^2 - \alpha^2}$.

**Correção das anotações:** a expressão $e^{at}(A\cos bt + B\sin bt)$ para raízes $a \pm bj$ é a solução **homogênea** (natural), não a particular. A particular, para fonte constante, é o valor final $x(\infty)$.

**Condições iniciais:** a tensão no capacitor e a corrente no indutor não saltam: $v_C(0^+) = v_C(0^-)$ e $i_L(0^+) = i_L(0^-)$. Calcule-as em regime CC antes da chave (capacitor = aberto, indutor = curto). A derivada sai de $C\,dv_C/dt = i_C(0^+)$ ou $L\,di_L/dt = v_L(0^+)$.

**Verificação:** os exemplos deste acervo (AB2, revisão) foram resolvidos com `dsolve` do SymPy e conferem com as condições iniciais.
