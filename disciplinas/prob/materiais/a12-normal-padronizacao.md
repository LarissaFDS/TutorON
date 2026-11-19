---
id: prob-anot-normal-padronizacao
titulo: Distribuição normal: padronização z = (x − μ)/σ, tabela acumulada e pnorm/qnorm em cinco tipos de problema
assunto: prob-06-uniforme-normal
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Distribuições Normais e Uniformes_251011_135256.pdf" (2025.2), págs. 1–2
autoria: Otávio Joshua Costa Brandão Menezes (aluno, equipe TutorON), anotações de estudo; paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações pessoais do aluno); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia as anotações e não reproduz imagens
fontes_catalogo: ufal-prob-anotacoes-2025-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Anotações de aluno (2025.2), parafraseadas. Status da resolução: validada. Conferido com `scipy.stats.norm`.

**Normal** $X \sim N(\mu, \sigma^2)$: curva gaussiana, simétrica em torno da média μ, definida pela média e pelo desvio-padrão σ ($\sigma = \sqrt{\text{variância}}$). Probabilidade = área sob a curva.

**Padronização:** $Z = \dfrac{X - \mu}{\sigma} \sim N(0, 1)$. Então $P(X \le a) = \Phi\!\left(\frac{a - \mu}{\sigma}\right)$, onde Φ é a acumulada da normal padrão. Tabela de **área acumulada** (de −∞ a z) dá Φ(z) direto; tabela de **área entre 0 e z** dá $\Phi(z) - 0{,}5$, e é preciso somar 0,5. Simetria: $\Phi(-z) = 1 - \Phi(z)$.

**Cinco tipos**, com $X \sim N(40, 10^2)$ (média 40, desvio 10):
1. $P(X \le 50)$: $z = (50-40)/10 = 1$, $\Phi(1) \approx 0{,}8413$. R: `pnorm(50, mean = 40, sd = 10)`.
2. $P(X \ge 35)$: $z = -0{,}5$, $1 - \Phi(-0{,}5) \approx 0{,}6915$. R: `pnorm(35, 40, 10, lower.tail = FALSE)`.
3. $P(25 < X < 60)$: $\Phi(2) - \Phi(-1{,}5) \approx 0{,}9104$.
4. $P(X \le 30 \text{ ou } X \ge 55)$: $\Phi(-1) + 1 - \Phi(1{,}5) \approx 0{,}2255$.
5. x com $P(X \le x) = 0{,}95$: `qnorm(0.95, 40, 10)` $\approx 56{,}45$ ($z \approx 1{,}645$); x com $P(X > x) = 0{,}10$: `qnorm(0.10, 40, 10, lower.tail = FALSE)` = `qnorm(0.90, 40, 10)` $\approx 52{,}82$.

No R, `sd` é o **desvio-padrão**, não a variância. `dnorm` dá a densidade num ponto (não é probabilidade); `rnorm(n, mean, sd)` gera valores.

**Verificação:** tipos 1 e 2 conferidos com `norm.cdf(1)` = 0,8413 e `norm.sf(-0.5)` = 0,6915; no tipo 5, `norm.cdf(56.45, 40, 10)` ≈ 0,95.
