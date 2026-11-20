---
id: controle-anot-revisao-segunda-ordem
titulo: Revisão prova 1: segunda ordem 6/(s²+2s+8) (tp, tr, Mp) e malha fechada de 20/(s²+6s+16) com realimentação unitária (ζ = 0,5, Mp = 16,3%); faixa de α em 9/(s²+(1+α)s+9)
assunto: controle-05-resposta-temporal
tipo: resolucao
resolucao: sim
fonte: Anotações "Revisão prova 1" (2 out. 2026), exercícios 4.4 a 4.6
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**4.4:** $G = \frac{6}{s^2 + 2s + 8}$ (malha aberta, degrau). $\omega_n = \sqrt8 = 2{,}83$, $\zeta = \frac{2}{2\sqrt8} = 0{,}354$, ganho $C = 6/8 = 0{,}75$, $\omega_d = 2{,}65$; $t_p = \pi/\omega_d = 1{,}19$ s; $\theta = \arccos\zeta = 1{,}209$ rad; $t_r = (\pi - \theta)/\omega_d = 0{,}73$ s; $M_p = 30{,}5\%$; $y_{max} = 0{,}75\cdot1{,}305 = 0{,}979$.

**4.5:** $G = \frac{20}{s^2 + 6s + 16}$ com realimentação **unitária negativa**: $G_{mf} = \frac{20}{s^2 + 6s + 36}$. $\omega_n = 6$, $\zeta = 0{,}5$, $C = 20/36 = 0{,}556$, $\omega_d = 5{,}196$, $t_p = 0{,}605$ s.
$$M_p = e^{-\zeta\pi/\sqrt{1 - \zeta^2}} = e^{-1{,}814} = 16{,}3\%,\qquad y_{max} = 0{,}556\cdot1{,}163 = 0{,}646.$$
**Correção:** as anotações usam $e^{-\zeta\pi\sqrt{1 - \zeta^2}}$ (multiplicando pela raiz) e chegam a $25{,}65\%$ e $y_{max} = 0{,}691$.

**4.6 (paráfrase):** $\frac{9}{s^2 + (1 + \alpha)s + 9}$: $\omega_n = 3$, $\zeta = \frac{1 + \alpha}{6}$. Superamortecido: $\alpha > 5$; subamortecido e estável: $-1 < \alpha < 5$; constante de tempo da envoltória $1/(\zeta\omega_n) = 1$ s: $\alpha = 1$.

**Verificação:** `scipy.signal.step`: pico $0{,}979$ em $t = 1{,}19$ s (4.4) e $0{,}646$ em $t = 0{,}605$ s (4.5).
