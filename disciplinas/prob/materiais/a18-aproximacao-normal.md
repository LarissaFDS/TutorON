---
id: prob-anot-aproximacao-normal
titulo: Aproximação normal da binomial e da Poisson com correção de continuidade
assunto: prob-09-aproximacao-normal-tcl
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Distribuição Exponencial e Combinação Linear _251011_140915.pdf" (2025.2), pág. 6
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
Resumo digitado do aluno (2025.2), parafraseado. Status da resolução: validada. Conferido com `scipy.stats` (valor exato e aproximado).

**Binomial → normal:** se n é grande e p não é extremo ($np > 5$ e $nq > 5$), $X \sim \text{Bin}(n, p)$ é aproximada por $N(np,\ npq)$.
**Correção de continuidade:** a binomial é discreta; cada inteiro k vira o intervalo $[k - 0{,}5,\ k + 0{,}5]$. Então $P(X \ge 50)$ vira $P(Y \ge 49{,}5)$ e $P(X \le 50)$ vira $P(Y \le 50{,}5)$.

Ex.: n = 200, p = 0,3: média 60, variância 42, desvio ≈ 6,48.
$$P(X \ge 50) \approx P\!\left(Z \ge \frac{49{,}5 - 60}{\sqrt{42}}\right) = P(Z \ge -1{,}620) \approx 0{,}9474.$$
Valor exato (binomial): 0,9494. Sem a correção ($P(Y \ge 50)$): 0,9386, mais longe.

**Poisson → normal:** para λ grande (o resumo usa λ > 10), $\text{Poisson}(\lambda) \approx N(\lambda, \lambda)$. Ex.: λ = 1000, $P(X \le 950) \approx \Phi\!\left(\frac{950{,}5 - 1000}{\sqrt{1000}}\right) \approx 0{,}0588$ (exato: 0,0578).

Essas aproximações são casos do Teorema Central do Limite (soma de muitos ensaios independentes).

**Verificação:** `binom.sf(49, 200, 0.3)` = 0,9494 e `poisson.cdf(950, 1000)` = 0,0578, próximos das aproximações.
