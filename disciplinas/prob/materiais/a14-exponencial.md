---
id: prob-anot-exponencial
titulo: Distribuição exponencial: densidade, acumulada, média 1/λ, falta de memória, taxa x média e pexp no R
assunto: prob-07-exponencial
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Distribuição Exponencial e Combinação Linear _251011_140915.pdf" (2025.2), págs. 1–3
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
Resumo digitado do aluno (2025.2), parafraseado. Status da resolução: validada. Conferido com `scipy.stats.expon` e simulação.

**Exponencial com taxa λ** (λ eventos por unidade de tempo): tempo ou distância **entre eventos** de um processo de Poisson; contínua e não negativa.
$$f(x) = \lambda e^{-\lambda x},\ x \ge 0; \quad F(x) = 1 - e^{-\lambda x}; \quad P(X > x) = e^{-\lambda x}; \quad E(X) = \tfrac{1}{\lambda},\ \operatorname{Var}(X) = \tfrac{1}{\lambda^2},\ \sigma = \tfrac{1}{\lambda}.$$

**Taxa ou média?** Se o enunciado dá a **média** (100 horas), $\lambda = 1/100 = 0{,}01$ por hora. Se dá a **taxa** (3 eventos por minuto), λ = 3. O R usa a taxa: `pexp(x, rate = λ)`; a scipy usa a média: `expon(scale = 1/λ)`.

**Falta de memória:** $P(X > s + t \mid X > s) = P(X > t)$. Ex.: P(durar mais 10 h | já durou 100 h) = P(durar mais de 10 h desde o início). A "idade" não muda a chance de falha futura (taxa de falha constante). Prova: $e^{-\lambda(s+t)}/e^{-\lambda s} = e^{-\lambda t}$.

**Verificação:** $\int_0^\infty \lambda e^{-\lambda x}dx = 1$; numa simulação de 100 mil valores com λ = 0,2, a fração acima de 10 é ≈ 0,135 e, entre os que passaram de 5, a fração que passa de 15 também é ≈ 0,135 (falta de memória).
