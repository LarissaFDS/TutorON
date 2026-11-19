---
id: prob-anot-binomial
titulo: Distribuição binomial: k sucessos em n ensaios de Bernoulli independentes; dbinom e pbinom no R
assunto: prob-05-distribuicoes-discretas
tipo: material_estudo
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Principais Distribuições Discretas_251011_130200.pdf" (2025.2), págs. 2–3
autoria: Otávio Joshua Costa Brandão Menezes (aluno, equipe TutorON), anotações de estudo; paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações pessoais do aluno); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia as anotações e não reproduz imagens
fontes_catalogo: ufal-prob-anotacoes-2025-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Anotações de aluno (2025.2), parafraseadas. Status da resolução: corrigida (a soma de dbinom para P(X ≤ 3) começava em 1 e ia até 4). Conferido com `scipy.stats.binom`.

**Binomial** $X \sim \text{Bin}(n, p)$: número de sucessos em n repetições **independentes** de um ensaio de Bernoulli com a mesma probabilidade de sucesso p ($q = 1-p$).
$$P(X = k) = \binom{n}{k} p^k q^{n-k},\quad k = 0, 1, \dots, n; \qquad E(X) = np,\ \operatorname{Var}(X) = npq.$$

**No R:**
- `dbinom(k, size = n, prob = p)` = $P(X = k)$ ("exatamente k");
- `pbinom(k, size = n, prob = p)` = $P(X \le k)$ ("até k", cauda inferior, `lower.tail = TRUE` é o padrão);
- `pbinom(k, size = n, prob = p, lower.tail = FALSE)` = $P(X > k)$ ("mais que k"). Para $P(X \ge k)$ use `pbinom(k - 1, …, lower.tail = FALSE)`.

$P(X \le 3)$ (0, 1, 2 ou 3 sucessos) é `pbinom(3, n, p)` ou a soma de quatro pontos:
$$P(X \le 3) = \texttt{dbinom(0)} + \texttt{dbinom(1)} + \texttt{dbinom(2)} + \texttt{dbinom(3)}.$$
- **Correção:** as anotações somam `dbinom(1)` a `dbinom(4)`: esquecem o zero e incluem o 4, o que dá $P(1 \le X \le 4)$.

Ex.: n = 10, p = 0,3: $P(X \le 3) \approx 0{,}6496$.

**Verificação:** `binom.cdf(3, 10, 0.3)` = 0,6496 = soma de `binom.pmf(k)` para k = 0..3; $\sum_{k=0}^{10} P(X = k) = 1$.
