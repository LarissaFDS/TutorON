---
id: calc4-impulso-delta-dirac-laplace
titulo: Função impulso (delta de Dirac) — propriedade da peneiração, L{δ(t − a)} = e^(−as) e a EDO y'' + 4y = δ(t − π) − δ(t − 2π) resolvida por Laplace
assunto: calc4-04-laplace-impulso
tipo: notas
questao: anotações de aula sobre a função impulso
resolucao: sim
fonte: Anotações manuscritas da aula de função impulso (delta de Dirac) de Cálculo 4 (arquivo Delta de Dirac.pdf), com os exemplos da aula | paráfrase
curso: Engenharia de Computação (UFAL), ECOM023 Cálculo 4, 4º período
fontes_catalogo: ufal-calc4-anotacoes-impulso
autoria: Anotações de aula (autoria não identificada no arquivo), parafraseadas pela equipe TutorON; resolução completa da equipe, conferida com SymPy
licenca: Não declarada (anotações de turma); PDF não versionado
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Anotações da aula de função impulso de Cálculo 4, parafraseadas. Status da resolução: validada. A resolução completa é da equipe TutorON e não é gabarito do professor.

**Motivação.** Em $ay'' + by' + cy = g(t)$, uma força muito grande que age por pouco tempo (um golpe) é modelada pelo **impulso** $\delta(t - t_0)$: zero fora de $t_0$, com $\int_{-\infty}^{\infty}\delta(t - t_0)\,dt = 1$. A aula constrói $\delta$ como limite de pulsos $d_\tau$ de altura $\frac{1}{2\tau}$ e largura $2\tau$ em volta de $t_0$, com área 1, quando $\tau \to 0$.

**Peneiração.** Para $f$ contínua, $\int_{-\infty}^{\infty} f(t)\,\delta(t - t_0)\,dt = f(t_0)$. Exemplo da aula: $\int_{-\infty}^{\infty}(t^2 + 3t + 5)\,\delta(t - 2)\,dt = 4 + 6 + 5 = 15$.

**Laplace.** Pela peneiração com $f(t) = e^{-st}$: $\mathcal L\{\delta(t - t_0)\} = e^{-st_0}$ ($t_0 \ge 0$); em particular $\mathcal L\{\delta(t)\} = 1$ e $\mathcal L\{\delta(t - 2)\} = e^{-2s}$.

**EDO da aula.** $y'' + 4y = \delta(t - \pi) - \delta(t - 2\pi)$, $y(0) = 0$, $y'(0) = 0$. Transformando: $s^2Y + 4Y = e^{-\pi s} - e^{-2\pi s}$, logo
$$Y(s) = \frac{e^{-\pi s} - e^{-2\pi s}}{s^2 + 4}.$$
Como $\mathcal L^{-1}\{\frac{1}{s^2+4}\} = \frac12\,\text{sen}\,2t$ e $e^{-as}$ desloca com degrau:
$$y(t) = \tfrac12\,\text{sen}\,2(t-\pi)\,u(t-\pi) - \tfrac12\,\text{sen}\,2(t-2\pi)\,u(t-2\pi).$$
Como $\text{sen}\,2(t - \pi) = \text{sen}\,2t$: $y = 0$ para $t < \pi$, $y = \frac12\,\text{sen}\,2t$ para $\pi < t < 2\pi$ e $y = 0$ para $t > 2\pi$. O segundo golpe chega quando a mola está em equilíbrio com velocidade 1, e o golpe $-1$ zera a velocidade, então o sistema para. Em $t = \pi$, $y'$ salta de 0 para 1: o impulso muda a velocidade, não a posição.

**Verificação:** `test_impulso_delta_dirac` confere a peneiração, as transformadas e a solução (inversa de Laplace e salto de $y'$).
