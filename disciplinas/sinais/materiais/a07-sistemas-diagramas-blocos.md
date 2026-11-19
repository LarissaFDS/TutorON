---
id: sinais-anot-sistemas-blocos
titulo: Sistemas de tempo contínuo: y = T[u], modelo de um circuito RL, diagramas de blocos, paralelo, cascata e realimentação
assunto: sinais-04-propriedades-sistemas
tipo: resumo
resolucao: nao
fonte: Anotações manuscritas "Sistemas de Tempo Contínuo" (20 mar. 2026)
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

**Sistema:** processa uma entrada $u(t)$ e gera uma saída $y(t) = T[u(t)]$; com uma entrada e uma saída é **SISO**. O **modelo matemático** é o conjunto de equações que liga $u$ e $y$.

**Exemplo RL série:** entrada $v(t)$, saída $v_L(t)$: $v(t) = Ri(t) + L\frac{di}{dt}$ e $v_L = L\frac{di}{dt}$, uma EDO linear de 1ª ordem com coeficientes constantes.

**Blocos básicos:** bloco ($y = T[u]$), junção de soma (cada entrada com seu sinal, ex. $y = u_1 - u_2 + u_3$).
- **Paralelo:** $y = T_1[u] + T_2[u]$.
- **Cascata:** $y = T_2[T_1[u]]$.
- **Realimentação:** referência $r(t)$ menos a medida do sensor dá o erro, que vai ao controlador, ao atuador e à planta (ex. controle do nível de um reservatório).

**Hipótese da interconexão:** ligar um sistema ao outro não muda nenhum deles. Em circuitos isso só vale se o segundo não carregar o primeiro; por isso se usa um **amplificador isolador** (impedância de entrada muito alta) entre dois circuitos RL.

**Verificação:** para $T_1[u] = 2u$ e $T_2[u] = u + 1$, a cascata dá $2u + 1$ e a ordem inversa dá $2u + 2$: com sistema não linear (o $+1$) a ordem da cascata importa; para dois SLIT, não.
