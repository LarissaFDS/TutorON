---
id: sinais-anot-fracoes-parciais-complexos
titulo: Frações parciais com polos complexos (150/(s² + 12s + 100), degrau) e polos múltiplos (8/(s + 2)³, degrau)
assunto: sinais-10-funcao-transferencia
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Representação por função de transferência" (19 jun. 2026)
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

**Polos complexos** $\alpha \pm j\beta$: $A_2 = A_1^*$ e o par gera $2|A_1|e^{\alpha t}\cos(\beta t + \angle A_1)$.

**Exemplo:** $G = \frac{150}{s^2 + 12s + 100}$, polos $-6 \pm j8$; degrau, $Y = \frac{150}{s(s^2 + 12s + 100)}$. $A_0 = \frac{150}{100} = 1{,}5$. Em $s = -6 + j8$: $A = \frac{150}{(-6 + j8)(j16)}$; $-6 + j8 = 10e^{j\theta}$ com $\theta = \tan^{-1}(8/(-6)) + \pi = 126{,}87^\circ$ (2º quadrante), $j16 = 16e^{j\pi/2}$:
$$A = \tfrac{15}{16}e^{-j(\theta + \pi/2)},\qquad y(t) = 1{,}5 + \tfrac{15}{8}e^{-6t}\cos\!\left(8t - \theta - \tfrac\pi2\right),\ t \ge 0.$$

**Polos múltiplos** $(s - p)^m$: $C_{m-i} = \frac{1}{i!}\frac{d^i}{ds^i}\big[Y(s)(s - p)^m\big]_{s=p}$ e $\frac{1}{(s-p)^n} \to \frac{t^{n-1}}{(n-1)!}e^{pt}$.

**Exemplo:** $G = \frac{8}{(s + 2)^3}$, degrau: $Y = \frac{8}{s(s+2)^3} = \frac1s - \frac{4}{(s+2)^3} - \frac{2}{(s+2)^2} - \frac{1}{s+2}$ e
$$y(t) = 1 - 2t^2e^{-2t} - 2te^{-2t} - e^{-2t},\quad t \ge 0.$$
(Correção: na última página das anotações os rótulos estão trocados: o termo 1 vem da entrada (degrau) e os termos com $e^{-2t}$ vêm dos polos de $G$.)

**Verificação:** nos dois casos $y(0) = 0$ e $y(\infty) = G(0)$: $150/100 = 1{,}5$ e $8/8 = 1$; `inverse_laplace_transform` e `scipy.signal.step` coincidem com as fórmulas.
