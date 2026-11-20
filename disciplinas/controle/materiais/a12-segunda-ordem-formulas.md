---
id: controle-anot-segunda-ordem
titulo: Segunda ordem padrão ωn²/(s² + 2ζωn s + ωn²): polos, ωd, θ = arccos ζ, sobressinal Mp = e^{−ζπ/√(1−ζ²)}, tempo de pico π/ωd, acomodação 4/(ζωn) e tempo de subida
assunto: controle-05-resposta-temporal
tipo: resolucao
resolucao: sim
fonte: Anotações "Análise de Resposta Temporal" (1º out. 2026), p. 3–9
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

**Forma padrão:** $G(s) = \frac{C\omega_n^2}{s^2 + 2\zeta\omega_ns + \omega_n^2}$ (fator de amortecimento $\zeta$, frequência natural $\omega_n$). Polos: $p = -\zeta\omega_n \pm \omega_n\sqrt{\zeta^2 - 1}$.
- $0 < \zeta < 1$ (subamortecido): $p = -\zeta\omega_n \pm j\omega_d$, com $\omega_d = \omega_n\sqrt{1 - \zeta^2}$; $|p| = \omega_n$; $\theta = \arccos\zeta$ é o ângulo do polo com o eixo real negativo.
- Degrau: $y(t) = C\Big[1 - \frac{e^{-\zeta\omega_nt}}{\sqrt{1 - \zeta^2}}\mathrm{sen}(\omega_dt + \theta)\Big]$; $\zeta = 0$: $1 - \cos\omega_nt$.

**Especificações (subamortecido):**
- sobressinal: $M_p = e^{-\zeta\pi/\sqrt{1 - \zeta^2}}$ (e elevado a menos zeta pi sobre raiz de um menos zeta ao quadrado). Valores: $\zeta = 0{,}5 \to 16{,}3\%$; $0{,}6 \to 9{,}5\%$; $0{,}7 \to 4{,}6\%$;
- tempo de pico: $t_p = \pi/\omega_d$;
- tempo de subida (0 a 100%): $t_r = (\pi - \theta)/\omega_d$; de 10 a 90%: $t_r \approx 1{,}8/\omega_n$ (aproximação boa perto de $\zeta = 0{,}5$);
- acomodação: $t_s \approx 4/(\zeta\omega_n)$ (2%) ou $3/(\zeta\omega_n)$ (5%).

**Correções:** nas anotações os polos aparecem sem $\omega_n$ e $\omega_d$ como $\omega_n\sqrt{\zeta^2 - 1}$; o certo está acima. Também se afirma que $(\pi - \theta)/\sqrt{1 - \zeta^2}$ "fica em torno de 2" para $0{,}4 \le \zeta \le 0{,}8$: na verdade vai de $2{,}16$ a $4{,}16$.

Essas fórmulas valem para o sistema de 2ª ordem **padrão** (sem zeros, sem terceiro polo); com polo ou zero adicional, simule.

**Verificação:** `scipy.signal.step` com $\omega_n = 1$, $\zeta = 0{,}5$ dá pico $1{,}163$ em $t = 3{,}63 = \pi/\omega_d$ e $t_r$ (10–90%) $= 1{,}64$.
