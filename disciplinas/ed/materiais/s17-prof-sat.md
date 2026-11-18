---
id: ed-prof-sat
titulo: SAT Solver — CNF, DIMACS e backtracking da aula 21 (sem implementação completa)
assunto: ed-13-sat
tipo: material_estudo
resolucao: sim
fonte: PDF "Aula 21 – SAT Solver" (Márcio Ribeiro) e Notion da turma, página "Casos teste"
fontes_catalogo: ufal-ed-prof-sat,ufal-ed-notion,ufal-ed-prof-preparatorio
autoria: Márcio Ribeiro (UFAL, Instituto de Computação), slides da disciplina; parafraseado pela equipe TutorON
licenca: Não declarada (material do professor); o PDF não está no repositório
publicacao_transcricao: não autorizada: o bloco parafraseia, não transcreve
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
SAT: dada uma fórmula em CNF (E de cláusulas, cada cláusula um OU de literais), existe uma atribuição que a torna verdadeira? Status da resolução: validada (conferida pela equipe TutorON; não é gabarito do professor).

DIMACS: a linha `p cnf V C` diz V variáveis e C cláusulas; cada cláusula é uma linha de inteiros terminada em 0, e o negativo é a negação. Exemplo da aula:

```
p cnf 3 3
-1 -2 0
1 -2 0
-1 -3 0
```

É satisfatível com a interpretação da aula, 1 = 1, 2 = 0, 3 = 0; 1 = 0, 2 = 0, 3 = 0 também serve (conferido por força bruta nos testes). Basta uma atribuição que satisfaça para responder SAT.

Ideia da aula: backtracking recursivo sat(F, I) sobre uma árvore binária de decisões. Escolha uma variável livre, tente verdadeiro e depois falso. Corte o ramo assim que alguma cláusula ficar falsa com a interpretação parcial I. Se todas ficarem verdadeiras, é SAT; se os dois ramos falharem, volta. Pior caso O(2ⁿ). DPLL e propagação unitária não estão nos slides.

Estruturas que o projeto exercita: lista ou vetor de cláusulas, pilha (implícita na recursão) e árvore de decisões. Os casos de teste do Notion incluem um cabeçalho que declara 5 cláusulas mas traz 4: o leitor deve validar o cabeçalho.

O projeto (Entrega 2 da AB2) é avaliado: o TutorON explica e ajuda a depurar, sem entregar o solver completo. A prova de que SAT é NP-completo é assunto de PAA.
