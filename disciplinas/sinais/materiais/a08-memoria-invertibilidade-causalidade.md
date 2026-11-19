---
id: sinais-anot-memoria-causalidade
titulo: Propriedades de sistemas: memória, invertibilidade e causalidade, com exemplos (RC, y = u², y = u(t − 2) e u(t + 2))
assunto: sinais-04-propriedades-sistemas
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Propriedades de Sistemas" (8 abr. 2026)
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

**Sem memória (estático):** $y(t_0)$ só depende de $u(t_0)$. Ex.: ganho $y = \beta u$, resistor $v = Ri$. **Com memória (dinâmico):** depende de valores passados (ou futuros).

**Exemplo com memória:** fonte de corrente $u(t)$ num R em série com C; $y = v_R + v_C$:
$$y(t) = Ru(t) + \frac1C\int_{-\infty}^t u(\tau)\,d\tau = Ru(t) + \frac1C\int_0^t u(\tau)\,d\tau + v_C(0),\quad t \ge 0.$$
(Correção: as anotações escrevem "$t \le 0$"; a forma com $v_C(0)$ vale para $t \ge 0$.)

**Invertível:** entradas diferentes dão saídas diferentes. Contraexemplo: $y = u^2$, pois $y = 4$ vem de $u = 2$ ou $u = -2$.

**Causal:** $y(t_0)$ não depende de $u(t)$ para $t > t_0$. Teste com um pulso em $[0, 1]$: $y = u(t - 2)$ responde em $[2, 3]$, depois da entrada (causal, é um atraso); $y = u(t + 2)$ responde em $[-2, -1]$, antes da entrada (**não causal**).

**Aplicação (instrumentação):** ohmímetro com galvanômetro, $\alpha = KI$, fundo de escala $90^\circ$ com $1$ mA, logo $K = 90000^\circ$/A. Com $V_0 = 0{,}1$ V e $R_0 = 100$ Ω em série, $\alpha = KV_0/(R_0 + R_x)$ e o indicador implementa $R_x = 9000/\alpha - 100$: $0^\circ \to \infty$, $15^\circ \to 500$ Ω, $30^\circ \to 200$ Ω, $90^\circ \to 0$.

**Verificação:** $9000/15 - 100 = 500$ e $9000/90 - 100 = 0$; derivando $y$ do RC, $\dot y = R\dot u + u/C$, independente de $v_C(0)$.
