---
id: ed-notion-big-o
titulo: Anotações da turma (Notion) — notação O (Big-O) e regras de soma e produto
assunto: ed-04-complexidade-recorrencias
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Big-O"
fontes_catalogo: ufal-ed-notion
autoria: Anotações de alunos da turma de Estrutura de Dados (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código revisado; o original não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
$f(n) = O(g(n))$ quando existem $c > 0$ e $n_0$ tais que $f(n) \le c\,g(n)$ para todo $n \ge n_0$. É um limite superior para n grande. Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

Exemplo da aula, conferido: 3n + 2 = O(n) com c = 4 e n₀ = 2 (3n + 2 ≤ 4n quando n ≥ 2). A aula usa c = 3 e n₀ = 2 para outro exemplo do mesmo tipo; o importante é exibir um par (c, n₀) que funcione.

Regras usadas para contar laços em código C:
- Soma: se f₁ = O(g₁) e f₂ = O(g₂), então f₁ + f₂ = O(max(g₁, g₂)). Dois laços seguidos de n passos: O(n).
- Produto: f₁·f₂ = O(g₁·g₂). Laço de n dentro de laço de n: O(n²).
- Constantes somem: 5n² + 100 = O(n²).

Correções da equipe
- Divergência: a anotação definia O "levando em consideração o pior caso". O é um limite para uma função; pior, melhor e caso médio são funções diferentes, e cada uma tem o seu O. Ex.: busca linear tem melhor caso O(1) e pior caso O(n).
- A regra 3 da anotação estava truncada; acima ela está completa (regra da soma).
