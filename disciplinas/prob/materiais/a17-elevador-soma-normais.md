---
id: prob-anot-elevador
titulo: Soma de n normais iguais: peso total de pessoas num elevador e probabilidade de exceder a capacidade (questão de prova, incompleta)
assunto: prob-08-combinacao-linear
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Distribuição Exponencial e Combinação Linear _251011_140915.pdf" (2025.2), pág. 5
autoria: Otávio Joshua Costa Brandão Menezes (aluno, equipe TutorON), anotações de estudo; paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações pessoais do aluno); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia as anotações e não reproduz imagens
fontes_catalogo: ufal-prob-anotacoes-2025-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Resumo digitado do aluno (2025.2), parafraseado. Status da resolução: pendente de confirmação do professor (o enunciado da prova não está no material e o resumo é inconsistente).

**Situação:** n pessoas entram num elevador; o peso de cada uma é $N(75, 10^2)$ kg, independente das outras. Qual a probabilidade de o peso total exceder a capacidade C?

**Montagem certa (soma de n cópias independentes):** $S = X_1 + \dots + X_n \sim N(75n,\ 100n)$, desvio $10\sqrt n$.
$$P(S > C) = 1 - \Phi\!\left(\frac{C - 75n}{10\sqrt n}\right).$$
- Para n = 8: média 600, desvio $10\sqrt 8 \approx 28{,}28$.
- Para n = 4: média 300, desvio 20.

**O que não fecha no resumo:** o título fala em 4 pessoas e o código usa 8; a capacidade é escrita como "605 + round(xx/10)", com xx dependente de cada aluno, então não há valor numérico para conferir. Pergunte qual é n e qual é a capacidade antes de calcular.

Não use $8X$ (uma pessoa vezes 8): daria desvio 80 em vez de 28,28 (veja a correção sobre múltiplo x soma de cópias).

**Verificação:** com n = 8 e C = 650 (valor só ilustrativo), $z = 50/28{,}28 \approx 1{,}77$ e $P \approx 0{,}0385$; a simulação da soma de 8 normais confirma.
