---
id: prob-anot-contagem
titulo: Contagem: combinação, arranjo, permutação com repetição; dominó e baralho
assunto: prob-01-probabilidade-basica
tipo: material_estudo
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Probabilidade _250907_210206.pdf" (2025.2), págs. 2, 5 e 6
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
Anotações de aluno (2025.2), parafraseadas. Status da resolução: corrigida (a notação do arranjo estava trocada). Conferido com `math.comb` e `math.perm`.

Contagem (princípio fundamental da contagem, análise combinatória) dá os "casos favoráveis" e "casos possíveis" quando há muitas possibilidades.

- **Combinação** (a ordem não importa), n escolhe p: $C_{n,p} = \dbinom{n}{p} = \dfrac{n!}{p!\,(n-p)!}$.
- **Arranjo** (a ordem importa): $A_{n,p} = \dfrac{n!}{(n-p)!}$.
- **Correção:** as anotações escrevem o arranjo como $\binom{n}{p}$, que é o símbolo da combinação. O arranjo é $A_{n,p} = p!\,\binom{n}{p}$; por exemplo, $A_{5,2} = 20$ e $C_{5,2} = 10$.
- **Permutação simples:** $P_n = n!$. **Com repetição** (α, β, γ elementos repetidos): $P_n^{\alpha,\beta,\gamma} = \dfrac{n!}{\alpha!\,\beta!\,\gamma!}$. Ex.: anagramas de ARARA, $5!/(3!\,2!) = 10$.

Casos especiais anotados:
- **Dominó:** 28 peças, das quais 7 "buchas" (as duas metades com o mesmo número, de 0-0 a 6-6). Conta: $\binom{7}{2} + 7 = 21 + 7 = 28$.
- **Baralho:** 52 cartas; 26 vermelhas (copas e ouros) e 26 pretas (paus e espadas); 4 naipes de 13; 12 figuras (J, Q, K de cada naipe) e 4 ases. Ex.: $P(\text{figura}) = 12/52 = 3/13 \approx 0{,}2308$.

**Verificação:** $\sum_{p=0}^{n}\binom{n}{p} = 2^n$ (para n = 5, 32); $A_{5,2}/C_{5,2} = 2! = 2$.
