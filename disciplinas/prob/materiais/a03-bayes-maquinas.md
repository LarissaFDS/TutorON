---
id: prob-anot-bayes-maquinas
titulo: Teorema de Bayes e probabilidade total — três máquinas A, B e C com taxas de defeito diferentes
assunto: prob-02-bayes
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Probabilidade _250907_210206.pdf" (2025.2), págs. 3–4
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
Anotações de aluno (2025.2), exemplo de aula parafraseado. Status da resolução: validada (o item b, que as anotações deixam como "análogo", foi completado). Conferido com `fractions` e simulação de Monte Carlo.

**Enunciado:** as máquinas A, B e C produzem 50%, 30% e 20% dos itens, com taxas de defeito de 2%, 3% e 5%. a) Dado que um item é defeituoso, qual a probabilidade de ter vindo de A? b) De C?

**Eventos:** A, B, C = máquina que produziu (uma partição: disjuntos e somam 1); D = item defeituoso. $P(A)=0{,}50$, $P(B)=0{,}30$, $P(C)=0{,}20$; $P(D\mid A)=0{,}02$, $P(D\mid B)=0{,}03$, $P(D\mid C)=0{,}05$.

**1. Probabilidade total** (soma sobre a partição):
$$P(D) = P(D\mid A)P(A) + P(D\mid B)P(B) + P(D\mid C)P(C) = 0{,}010 + 0{,}009 + 0{,}010 = 0{,}029.$$

**2. Teorema de Bayes** (de "defeito dado máquina" para "máquina dado defeito"):
$$P(A\mid D) = \frac{P(D\mid A)\,P(A)}{P(D)} = \frac{0{,}010}{0{,}029} = \frac{10}{29} \approx 0{,}3448.$$
b) $P(C\mid D) = 0{,}010/0{,}029 = 10/29 \approx 0{,}3448$ (e $P(B\mid D) = 9/29 \approx 0{,}3103$).

C produz só 20% dos itens, mas a taxa de defeito maior a deixa tão provável quanto A entre os defeituosos.

**Verificação:** $P(A\mid D)+P(B\mid D)+P(C\mid D) = (10+9+10)/29 = 1$; uma simulação com 200 mil itens dá frequências próximas de 0,345, 0,310 e 0,345.
