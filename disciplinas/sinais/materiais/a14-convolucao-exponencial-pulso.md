---
id: sinais-anot-convolucao-exponencial
titulo: Convolução de 3e^{−0,5t}u(t) com g(t) = 1 em [0, 2): resposta por intervalos 6(1 − e^{−0,5t}) e 6(e − 1)e^{−0,5t}
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

**Dados:** entrada $x(t) = 3e^{-0{,}5t}u_{-1}(t)$; resposta ao impulso $g(t) = 1$ para $0 \le t < 2$ e zero fora.

**Montagem:** $y(t) = \int x(\tau)g(t - \tau)d\tau$; $g(t - \tau) = 1$ para $t - 2 < \tau \le t$, e $x(\tau) \ne 0$ só para $\tau \ge 0$.

**Intervalos:**
- $t < 0$: sem sobreposição, $y = 0$.
- $0 \le t < 2$: $\tau \in [0, t]$: $y = \int_0^t 3e^{-0{,}5\tau}d\tau = 6(1 - e^{-0{,}5t})$.
- $t \ge 2$: $\tau \in [t - 2, t]$: $y = 6(e^{-0{,}5(t-2)} - e^{-0{,}5t}) = 6(e - 1)e^{-0{,}5t} \approx 10{,}31\,e^{-0{,}5t}$.

**Interpretação:** $g$ é uma média móvel de janela 2 (integra os últimos 2 s da entrada).

O item seguinte das anotações (pulso de largura 2 num sistema com resposta ao degrau $1 - e^{-t}$, logo $g = e^{-t}u_{-1}(t)$) ficou incompleto e não entrou.

**Verificação:** em $t = 2$ os dois pedaços valem $6(1 - e^{-1}) \approx 3{,}79$ (continuidade); `scipy` com convolução numérica (passo 1 ms) coincide com a fórmula até $10^{-3}$.
