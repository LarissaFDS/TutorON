---
id: sinais-anot-lista-transformacoes
titulo: Lista: esboçar x(−t/3), x(−t), x(3 + t) e x(2 − t) de um sinal com rampas e salto
assunto: sinais-02-operacoes-tempo
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Lista Sinais e Sistemas" (27 abr. 2026), questão 2
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

**Sinal dado (descrito):** $x(t) = 0$ para $t < -6$; rampa de 0 a $-1$ em $[-6, -3]$; salto para $+1$ em $t = -3$; $x = 1$ em $[-3, 0]$; rampa de 1 a 0 em $[0, 3]$; zero depois.

**Método:** para cada caso, $\tau$ = argumento e $t$ isolado; os pontos notáveis $\tau \in \{-6, -3, 0, 3\}$ são levados para o novo eixo.
- $x(-t/3)$: $t = -3\tau$: pontos em $18, 9, 0, -9$. Rampa de 0 a 1 em $[-9, 0]$, $1$ em $[0, 9]$, salto para $-1$ em $t = 9$, rampa até 0 em $t = 18$.
- $x(-t)$: $t = -\tau$: rampa de 0 a 1 em $[-3, 0]$, $1$ em $[0, 3]$, $-1$ em $t = 3$, rampa até 0 em $t = 6$.
- $x(3 + t)$: $t = \tau - 3$ (avanço de 3): rampa de 0 a $-1$ em $[-9, -6]$, salto para 1, $1$ em $[-6, -3]$, rampa até 0 em $t = 0$.
- $x(2 - t)$: $t = 2 - \tau$: rampa de 0 a 1 em $[-1, 2]$, $1$ em $[2, 5]$, $-1$ em $t = 5$, rampa até 0 em $t = 8$.

As anotações chegaram aos quatro esboços com uma tabela de pontos; todos conferem.

**Verificação:** $x(-t/3)$ em $t = 4{,}5$ vale $x(-1{,}5) = 1$; $x(2 - t)$ em $t = 6{,}5$ vale $x(-4{,}5) = -0{,}5$; conferidos numericamente nos testes.
