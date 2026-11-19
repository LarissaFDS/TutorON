---
id: prob-anot-poisson
titulo: Distribuição de Poisson: número de ocorrências num intervalo; ajuste da média ao intervalo; P(X > k) com ppois
assunto: prob-05-distribuicoes-discretas
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Principais Distribuições Discretas_251011_130200.pdf" (2025.2), pág. 4; e "Distribuição Exponencial e Combinação Linear _251011_140915.pdf", págs. 3 e 5
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
Anotações de aluno (2025.2), parafraseadas. Status da resolução: validada. Conferido com `scipy.stats.poisson`.

**Poisson** $X \sim \text{Poisson}(\lambda)$: número de ocorrências num intervalo contínuo (tempo, área, comprimento), com ocorrências independentes e taxa constante. λ é o **número médio de ocorrências no intervalo da pergunta**.
$$P(X = x) = \frac{e^{-\lambda}\lambda^x}{x!},\quad x = 0, 1, 2, \dots; \qquad E(X) = \operatorname{Var}(X) = \lambda.$$

**Ajuste do intervalo:** se a taxa é 15 chamadas por hora e a pergunta é sobre 40 minutos, $\lambda = 15 \cdot 40/60 = 10$. Exatamente 10 chamadas em 40 min: `dpois(10, lambda = 10)` $= e^{-10}10^{10}/10! \approx 0{,}1251$. Usar λ = 15 (o intervalo errado) é um erro comum.

**Cauda superior com média 3:** uma fábrica tem em média 3 falhas por dia; mais de 4 falhas num dia:
$$P(X > 4) = 1 - P(X \le 4) = 1 - e^{-3}\left(1 + 3 + \tfrac{9}{2} + \tfrac{27}{6} + \tfrac{81}{24}\right) \approx 0{,}1847,$$
em R `ppois(4, lambda = 3, lower.tail = FALSE)`. Do mesmo modo, P(X > 2) numa Poisson de média 3 é $1 - P(0) - P(1) - P(2)$, ou `ppois(2, 3, lower.tail = FALSE)`.

**Verificação:** `poisson.sf(4, 3)` = 0,1847 e `poisson.pmf(10, 10)` = 0,1251; a soma de P(X = x) para x de 0 a 50 com λ = 3 dá 1.
