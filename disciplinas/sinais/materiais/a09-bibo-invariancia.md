---
id: sinais-anot-bibo-invariancia
titulo: Estabilidade BIBO e invariância no tempo: indutor (integrador) não é BIBO estável; teste de invariância com dois caminhos; y(t) = x(2t) é variante
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

**BIBO:** toda entrada limitada ($|u(t)| \le M$) gera saída limitada ($|y(t)| \le P$). Para negar basta **uma** entrada limitada com saída ilimitada.

**Indutor** ($u = v$, $y = i = \frac1L\int_{-\infty}^t v$): o degrau dá a rampa $t/L$, ilimitada, logo **não é BIBO estável**. Com $v = e^{-at}u_{-1}(t)$ a saída $\frac{1}{aL}(1 - e^{-at})$ é limitada, mas isso não salva a propriedade. (Correção: as anotações chamam isso de "marginalmente estável" pelo fato de algumas entradas darem saída limitada; "marginalmente estável" é a classificação pelos polos, aqui um polo simples em $s = 0$; em termos BIBO o sistema é instável.)

**Invariância no tempo:** compare os dois caminhos: (1) atrasar a saída, $y(t - T)$; (2) atrasar a entrada e passar pelo sistema, $y_2(t) = T[u(t - T)]$. Invariante se forem iguais para todo $u$ e $T$.
- $y = e^{-t}u(t)$: $y(t - T) = e^{-(t-T)}u(t - T)$, mas $y_2 = e^{-t}u(t - T)$. **Variante** (coeficiente que muda com $t$).
- Indutor: com $\beta' = \beta - T$, $y_2(t) = \frac1L\int_{-\infty}^{t-T}u(\beta')d\beta' = y(t - T)$. **Invariante**.
- $y(t) = x(2t)$ (complemento da equipe): $y_2(t) = x(2t - T)$, mas $y(t - T) = x(2t - 2T)$. **Variante**. Contraexemplo: $x$ = pulso em $[0, 1]$ e $T = 1$: $y_2$ ocupa $[\tfrac12, 1]$ e $y(t - 1)$ ocupa $[1, \tfrac32]$.

**Verificação:** os dois caminhos de $x(2t)$ com o pulso e $T = 1$ foram calculados nos testes (diferem em $t = 0{,}75$); a rampa $t/L$ passa de qualquer $P$ para $t > PL$.
