---
id: sinais-anot-integral-janela
titulo: Exemplo: y(t) = ∫ de t a t+1 de u(τ − α) dτ: para quais α é causal; memória, BIBO, invariância e linearidade
assunto: sinais-04-propriedades-sistemas
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Propriedades de Sistemas" (8 abr. 2026), exemplo 2
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

**Sistema:** $y(t) = \int_t^{t+1} u(\tau - \alpha)\,d\tau$.

**Mudança de variável** $w = \tau - \alpha$: $y(t) = \int_{t-\alpha}^{t+1-\alpha} u(w)\,dw$ (a saída integra a entrada numa janela de largura 1).

**(a) Causalidade:** em $t_0$ a janela vai até $t_0 + 1 - \alpha$. Para não usar entrada futura: $t_0 + 1 - \alpha \le t_0 \iff \alpha \ge 1$. Em palavras: o sistema é causal se e só se alfa é maior ou igual a 1.

**(b) Demais propriedades:**
- Com memória: com $\alpha = 1$, $y(t_0)$ depende de $u$ em $[t_0 - 1, t_0]$.
- BIBO estável: $|y| \le \int_{t-\alpha}^{t+1-\alpha}|u(w)|\,dw \le M\cdot 1$.
- Invariante: com $u(t - t_0)$ e $z = w - t_0$, sai $\int_{t-t_0-\alpha}^{t-t_0+1-\alpha}u(z)\,dz = y(t - t_0)$.
- Linear: a integral da combinação é a combinação das integrais.

As conclusões das anotações conferem.

**Verificação:** com $u = $ degrau e $\alpha = 1$, $y(t) = \int_{t-1}^{t}u = $ rampa de 0 a 1 em $[0, 1]$, que começa só quando a entrada começa; com $\alpha = 0{,}5$, $y(-0{,}2) = 0{,}3 \ne 0$ antes da entrada (não causal). Conferido nos testes.
