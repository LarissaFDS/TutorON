---
id: sinais-anot-convolucao-pulsos
titulo: Convolução de um pulso retangular com uma rampa por intervalos de sobreposição; caso de dois pulsos retangulares (triângulo)
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

**Como calcular a convolução de dois sinais de duração finita:** reflita e desloque um deles ($g(t - \tau)$), deslize e, para cada faixa de $t$, integre só onde os dois se sobrepõem.

**Exemplo das anotações:** $x(\tau) = 1$ em $[-1, 1]$ (pulso retangular) e $g(t) = t/3$ em $[0, 3]$ (rampa). $g(t - \tau) \ne 0$ para $t - 3 \le \tau \le t$.
- $t < -1$: sem sobreposição, $y = 0$.
- $-1 \le t < 1$: sobreposição $[-1, t]$: $y = \int_{-1}^t \frac{t - \tau}{3}d\tau = \frac{(t+1)^2}{6}$.
- $1 \le t < 2$: $[-1, 1]$ inteiro: $y = \int_{-1}^{1}\frac{t - \tau}{3}d\tau = \frac{2t}{3}$.
- $2 \le t < 4$: $[t - 3, 1]$: $y = -\frac{t^2 - 2t - 8}{6}$.
- $t \ge 4$: $y = 0$.

**Dois pulsos retangulares (complemento da equipe):** $p(t) = 1$ em $[0, T]$. $p * p$: para $0 \le t < T$ a sobreposição é $[0, t]$, $y = t$; para $T \le t < 2T$ é $[t - T, T]$, $y = 2T - t$. Resultado: **triângulo** de base $[0, 2T]$ e pico $T$ em $t = T$. Pulsos de larguras diferentes dão um trapézio.

**Verificação:** a convolução começa na soma dos inícios ($-1 + 0$) e termina na soma dos fins ($1 + 3 = 4$); a área de $y$ é o produto das áreas (pulso: 2; rampa: $\int_0^3 t/3\,dt = 1{,}5$; logo 3), conferida numericamente com `numpy.convolve`; os pedaços se emendam em $t = 1$ ($2/3$), $t = 2$ ($4/3$) e $t = 4$ (0).
