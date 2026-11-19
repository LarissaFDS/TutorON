---
id: sinais-anot-convolucao-definicao
titulo: Integral de convolução: y = u * g, propriedades e exemplo e^{−t}u(t) * e^{−2t}u(t); propriedades do sistema pela resposta ao impulso
assunto: sinais-05-convolucao
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Descrição matemática de sistemas de tempo contínuo" (29 abr. 2026)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sinais e Sistemas 2026.1; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-sinais-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: validada.

Notação das anotações: $u(t)$ é a entrada e $g(t)$ a **resposta ao impulso** do SLIT.

**Dedução:** a entrada é aproximada por pulsos estreitos de área $u(\tau)\Delta\tau$; cada um gera $u(\tau)g(t - \tau)\Delta\tau$ (linearidade e invariância); somando e fazendo $\Delta\tau \to 0$:
$$y(t) = (u * g)(t) = \int_{-\infty}^{\infty} u(\tau)\,g(t - \tau)\,d\tau.$$
Em palavras: a saída é a integral de u de tau vezes g de t menos tau.

**Propriedades:** comutativa, associativa, distributiva; $u(t - t_0) * g(t) = y(t - t_0)$; $u * \delta = u$.

**Propriedades do sistema por $g$:** sem memória $\iff g = K\delta(t)$; causal $\iff g(t) = 0$ para $t < 0$; BIBO estável $\iff \int_{-\infty}^{\infty}|g(t)|\,dt < \infty$. Ex.: $g = e^{-3t}u_{-1}(t)$: $\int_0^\infty e^{-3t}dt = 1/3$, estável.

**Resposta ao degrau:** $s(t) = \int_0^t g(\tau)d\tau$ e $g = ds/dt$. Para $g = e^{-3t}u_{-1}(t)$: $s(t) = \tfrac13(1 - e^{-3t})u_{-1}(t)$. (As anotações chamam $g$ de "$y(t)$" nesse passo; é a resposta ao impulso.)

**Exemplo:** $e^{-t}u_{-1}(t) * e^{-2t}u_{-1}(t)$: os dois são zero para tempo negativo, então os limites são de 0 a $t$:
$$\int_0^t e^{-\tau}e^{-2(t-\tau)}d\tau = e^{-2t}(e^t - 1) = (e^{-t} - e^{-2t})u_{-1}(t).$$

**Verificação:** SymPy refaz a integral; pela Laplace, $\frac{1}{s+1}\cdot\frac{1}{s+2} = \frac{1}{s+1} - \frac{1}{s+2}$, o mesmo resultado.
