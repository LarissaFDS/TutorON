---
id: sinais-anot-degrau-rampa-impulso
titulo: Degrau, rampa e impulso unitário: pulso por diferença de degraus, impulso como limite, propriedade da amostragem
assunto: sinais-03-sinais-elementares
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Modelos de Sinais" (4 abr. 2026)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sinais e Sistemas 2026.1; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-sinais-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

Notação das anotações: $u_{-1}(t)$ é o degrau (em muitos livros, $u(t)$).

**Degrau:** $u_{-1}(t) = 1$ para $t \ge 0$ e 0 para $t < 0$; $u_{-1}(t - t_0)$ é o degrau atrasado. "Liga" funções: $\cos(\omega t)u_{-1}(t)$ zera a parte $t < 0$. Pulso de 2 a 4: $p(t) = u_{-1}(t - 2) - u_{-1}(t - 4)$.

**Correção (escalonamento do degrau):** as anotações escrevem $u_{-1}(at - t_0) = u_{-1}(t - t_0/a)$ para todo $a \ne 0$. Só vale para $a > 0$. Se $a < 0$, ao dividir $at - t_0 \ge 0$ por $a$ a desigualdade inverte: $u_{-1}(at - t_0) = u_{-1}(t_0/a - t)$. Ex.: $u_{-1}(-2t + 4) = 1$ para $t \le 2$.

**Rampa:** $\int_0^t u_{-1}(\tau - t_0)\,d\tau = (t - t_0)u_{-1}(t - t_0) = r(t - t_0)$; $r(t) = t\,u_{-1}(t)$.

**Impulso:** $\delta(t) = 0$ para $t \ne 0$ e $\int_{-\infty}^{\infty}\delta(t)\,dt = 1$. É o limite, com $\epsilon \to 0$, do pulso de largura $\epsilon$ e altura $1/\epsilon$ (área sempre 1). $K\delta(t)$ tem área $K$.

**Propriedades:** $\phi(t)\delta(t - t_0) = \phi(t_0)\delta(t - t_0)$ se $\phi$ é contínua em $t_0$; **amostragem** $\int_{-\infty}^{\infty}\phi(t)\delta(t - t_0)\,dt = \phi(t_0)$; $\delta(t) = \frac{du_{-1}}{dt}$ e $\int_{-\infty}^t \delta(\tau)\,d\tau = u_{-1}(t)$.

**Verificação:** em $u_{-1}(-2t + 4)$, $t = 0$ dá $u_{-1}(4) = 1$ e $t = 3$ dá $u_{-1}(-2) = 0$, já a fórmula das anotações daria $u_{-1}(t - 2)$, que vale 0 em $t = 0$ e 1 em $t = 3$ (o oposto); conferido nos testes.
