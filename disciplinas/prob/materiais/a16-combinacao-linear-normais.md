---
id: prob-anot-combinacao-linear-normais
titulo: Combinação linear de normais independentes: soma, diferença (2X − Y), múltiplo aX e soma de n cópias; peso líquido
assunto: prob-08-combinacao-linear
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Distribuição Exponencial e Combinação Linear _251011_140915.pdf" (2025.2), págs. 4–5
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
Resumo digitado do aluno (2025.2), parafraseado. Status da resolução: corrigida (múltiplo de uma normal e notação do exemplo 1). Conferido com `scipy.stats.norm` e simulação.

**Teorema:** se $X_1, \dots, X_n$ são normais **independentes**, $W = a_1X_1 + \dots + a_nX_n$ é normal com
$$E(W) = \sum a_i\mu_i, \qquad \operatorname{Var}(W) = \sum a_i^2\sigma_i^2.$$
- Soma: médias somam, **variâncias** somam; $\sigma_W = \sqrt{\sigma_1^2 + \dots + \sigma_n^2}$ (não some desvios).
- Diferença $X_1 - X_2$: média $\mu_1 - \mu_2$, variância $\sigma_1^2 + \sigma_2^2$ (soma sempre).
- **2X − Y:** $N(2\mu_X - \mu_Y,\ 4\sigma_X^2 + \sigma_Y^2)$.
- **Correção:** o resumo diz que $W = nX$ tem variância $n\sigma^2$ e desvio $\sqrt n\,\sigma$. Isso vale para a **soma de n cópias independentes** $X_1 + \dots + X_n$. Para o múltiplo $nX$ (uma variável vezes n), $\operatorname{Var}(nX) = n^2\sigma^2$ e desvio $n\sigma$.

**Exemplo 1 (montagem em 2 etapas):** o resumo escreve $N(75, 16{,}81^2)$ e $N(129, 106{,}09^2)$, mas soma 16,81 + 106,09 como variâncias. **Correção de notação:** as contas só fecham lendo 16,81 e 106,09 como **variâncias** (desvios 4,1 e 10,3). Então $T \sim N(204,\ 122{,}90)$, $\sigma_T \approx 11{,}09$, $P(T < 200) = \Phi(-0{,}361) \approx 0{,}3591$.

**Exemplo 2 (peso líquido):** bruto $\sim N(1000, 20^2)$, lata $\sim N(90, 10^2)$, independentes. Líquido = bruto − lata $\sim N(910,\ 400 + 100 = 500)$, $\sigma \approx 22{,}36$.
a) $P(L < 850) \approx 0{,}0036$; b) $P(L > 870) \approx 0{,}9632$; c) $P(860 < L < 920) \approx 0{,}6600$.

**Verificação:** simulação de 200 mil pares dá desvio do líquido ≈ 22,4 (com variâncias subtraídas seria $\sqrt{300} \approx 17{,}3$); `norm(910, 500**0.5).cdf(850)` = 0,0036.
