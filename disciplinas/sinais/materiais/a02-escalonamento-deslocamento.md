---
id: sinais-anot-escalonamento-deslocamento
titulo: Reflexão, escalonamento e deslocamento no tempo: como esboçar y(t) = x(at − b) pelo mapeamento τ = at − b
assunto: sinais-02-operacoes-tempo
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Escalonamento e Deslocamento de tempo" (13 mar. 2026)
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

**Operações (variável independente $t$):**
- Reflexão: $y(t) = x(-t)$; o valor de $x$ em $t_0$ aparece em $-t_0$.
- Escalonamento: $y(t) = x(at)$, $a \ne 0$: comprime se $|a| > 1$, expande se $|a| < 1$. Ex.: triângulo de $-1$ a $1$ vira, em $x(2t)$, triângulo de $-\tfrac12$ a $\tfrac12$; em $x(t/2)$, de $-2$ a $2$.
- Deslocamento: $y(t) = x(t - T)$: atraso (para a direita) se $T > 0$, avanço se $T < 0$. Ex.: pulso em $[-\tfrac12, \tfrac12]$: $x(t-2)$ ocupa $[\tfrac32, \tfrac52]$ e $x(t+1)$ ocupa $[-\tfrac32, -\tfrac12]$.
- Amplitude: $Ax(t) + B$ (ganho e soma de constante, ex. $-3x(t) - 1$).

**Método para $x(at - b)$:** chame o argumento de $\tau = at - b$ e isole $t = \frac{\tau + b}{a}$. Cada ponto notável $\tau_i$ de $x$ vai para $t_i = (\tau_i + b)/a$. Erro típico: deslocar por $b$ em vez de $b/a$, pois $x(at - b) = x\big(a(t - b/a)\big)$.

**Exemplo das anotações:** $x(\tau) = 1$ em $[-1, 0)$, rampa de 0 a 1 em $[0, 1]$, $1$ em $[1, 2]$, zero fora. Para $y(t) = x(-\tfrac12 t + 1)$: $t = 2 - 2\tau$. Então $\tau = 2 \to t = -2$; $\tau = 1 \to t = 0$; $\tau = 0 \to t = 2$; $\tau = -1 \to t = 4$. Resultado: $y = 1$ em $[-2, 0]$, rampa descendo de 1 a 0 em $[0, 2]$, $y = 1$ em $(2, 4]$, zero fora (o sinal foi refletido e esticado 2 vezes).

**Verificação:** substituindo pontos: $y(1) = x(\tfrac12) = \tfrac12$ (meio da rampa), $y(3) = x(-\tfrac12) = 1$ e $y(5) = x(-\tfrac32) = 0$, conferidos numericamente nos testes.
