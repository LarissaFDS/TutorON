---
id: sinais-anot-laplace
titulo: Transformada de Laplace unilateral: definição, região de convergência, tabela (degrau, exponencial, seno, cosseno, tⁿ) e propriedades
assunto: sinais-09-laplace
tipo: resumo
resolucao: nao
fonte: Anotações manuscritas "Transformada de Laplace" (10 jun. 2026)
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

Convenção das anotações: **unilateral**, $F(s) = \int_{0^-}^{\infty}f(t)e^{-st}dt$, para sinais nulos em $t < 0$ (multiplicados pelo degrau). A integral só converge numa **região de convergência** (RC) $\mathrm{Re}\,s > \sigma_0$. Na bilateral a RC é indispensável para inverter; na unilateral, as condições iniciais entram pela regra da derivada.

**Tabela:**
- $Ae^{at} \to \frac{A}{s - a}$, RC: $\mathrm{Re}\,s > a$. Degrau: $\frac1s$ ($\mathrm{Re}\,s > 0$).
- $\delta(t) \to 1$; $t^n \to \frac{n!}{s^{n+1}}$; $\frac{t^{n-1}}{(n-1)!}e^{at} \to \frac{1}{(s - a)^n}$.
- $\cos\omega t \to \frac{s}{s^2 + \omega^2}$; $\mathrm{sen}\,\omega t \to \frac{\omega}{s^2 + \omega^2}$.

**Propriedades:** derivada $f' \to sF(s) - f(0^-)$ e $f'' \to s^2F - sf(0^-) - f'(0^-)$; integral $\int_0^t f \to F(s)/s$; deslocamento no tempo $f(t - t_0)u(t - t_0) \to e^{-st_0}F(s)$; deslocamento em $s$: $e^{-at}f(t) \to F(s + a)$; convolução $f * g \to F(s)G(s)$; $t^nf(t) \to (-1)^n\frac{d^nF}{ds^n}$.

**Exemplo (RL série com degrau $V$):** $V/s = RI(s) + LsI(s)$ com $i(0) = 0$, logo $I(s) = \frac{V}{s(R + Ls)}$ e
$$i(t) = \frac VR\left(1 - e^{-Rt/L}\right),\quad t \ge 0.$$

**Verificação:** `laplace_transform` do SymPy confere cada linha da tabela; $i(0) = 0$ e $i(\infty) = V/R$ (teorema do valor final: $\lim_{s\to0}sI(s) = V/R$).
