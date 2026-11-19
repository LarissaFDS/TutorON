---
id: prob-anot-esperanca-variancia
titulo: Valor esperado, variância e desvio-padrão: definições e propriedades (variância da soma e da diferença)
assunto: prob-04-esperanca-variancia
tipo: material_estudo
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Variáveis Aleatórias_251008_230428.pdf" (2025.2), págs. 5–6
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
Anotações de aluno (2025.2), parafraseadas. Status da resolução: corrigida (variância da diferença com sinal errado). Conferido com SymPy e simulação.

**Valor esperado (esperança, média):** discreta $\mu = E(X) = \sum_i x_i\,P(X = x_i)$; contínua $E(X) = \int_{-\infty}^{\infty} x\,f(x)\,dx$ (na prática, no intervalo onde f não é zero).

Propriedades: $E(k) = k$; $E(kX) = k\,E(X)$; $E(X + Y) = E(X) + E(Y)$ e $E(X - Y) = E(X) - E(Y)$ **sempre**; $E(XY) = E(X)E(Y)$ se X e Y são independentes.

**Variância** (dispersão em torno da média): $\operatorname{Var}(X) = \sigma^2 = E[(X-\mu)^2] = E(X^2) - [E(X)]^2$, com $E(X^2) = \sum x_i^2 p(x_i)$ ou $\int x^2 f(x)\,dx$. **Desvio-padrão:** $\sigma = \sqrt{\operatorname{Var}(X)}$, na unidade de X.

Propriedades: $\operatorname{Var}(k) = 0$; $\operatorname{Var}(kX) = k^2\operatorname{Var}(X)$; se X e Y são independentes, $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$ e
$$\operatorname{Var}(X - Y) = \operatorname{Var}(X) + \operatorname{Var}(Y).$$
- **Correção:** as anotações escrevem $\sigma^2(X - Y) = \sigma^2(X) - \sigma^2(Y)$. Está errado: $X - Y = X + (-1)Y$ e $\operatorname{Var}(-Y) = (-1)^2\operatorname{Var}(Y)$; as variâncias **somam**. Com o sinal de menos a variância poderia dar negativa.
- Sem independência: $\operatorname{Var}(X \pm Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) \pm 2\operatorname{Cov}(X, Y)$.
- Some variâncias, não desvios-padrão: $\sigma_{X+Y} = \sqrt{\sigma_X^2 + \sigma_Y^2}$.

**Verificação:** dado honesto: $E(X) = 3{,}5$, $E(X^2) = 91/6$, $\operatorname{Var}(X) = 91/6 - 12{,}25 = 35/12 \approx 2{,}9167$. Para dois dados independentes, $\operatorname{Var}(X - Y) = 35/6$ (simulação confirma), não 0.
