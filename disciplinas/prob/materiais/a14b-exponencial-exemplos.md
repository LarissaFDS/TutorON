---
id: prob-anot-exponencial-exemplos
titulo: Exemplos de exponencial com pexp: média dada x taxa dada, cauda superior e conversão de unidades (minutos x horas)
assunto: prob-07-exponencial
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Distribuição Exponencial e Combinação Linear _251011_140915.pdf" (2025.2), págs. 2–3
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
Resumo digitado do aluno (2025.2), parafraseado. Status da resolução: validada. Conferido com `scipy.stats.expon`.

Exponencial com taxa λ: $P(X \le x) = 1 - e^{-\lambda x}$ e $P(X > x) = e^{-\lambda x}$; média $1/\lambda$.

**Exemplos** (R: `pexp(x, rate)`, cauda superior com `lower.tail = FALSE`):
- Chamada com média de 5 min ($\lambda = 0{,}2$): $P(X \le 5) = 1 - e^{-1} \approx 0{,}6321$; $P(X > 10) = e^{-2} \approx 0{,}1353$.
- Espera por exame com média de 3 dias: $P(X > 2) = e^{-2/3} \approx 0{,}5134$; $P(2 < X < 4) = e^{-2/3} - e^{-4/3} \approx 0{,}2498$.
- Unidades: taxa de 15 chamadas/hora e pergunta em minutos: $\lambda = 0{,}25$/min, ou converta o tempo (5 min = 5/60 h) e mantenha λ = 15/h. As duas dão $P(X > 5\ \text{min}) = e^{-1{,}25} \approx 0{,}2865$.

**Verificação:** pelo complemento, $0{,}6321 + e^{-1} = 1$; `expon(scale=3).sf(2)` = 0,5134 e `expon(scale=4).sf(5)` (média de 4 min) = 0,2865.
