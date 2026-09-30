---
id: c09
fonte: "Lista de Exercícios 7 (Cap. 7 — NP-Completude), questão 1 — resolução de alunos (NÃO revisada pelo professor)"
tipo: resolucao_lista
topico: classes P, NP, NP-completo, redução polinomial
---
• O que significa dizer que um problema Π pode ser polinomialmente reduzido a um problema Π′?
Estamos afirmando que existe um algoritmo polinomial X que transforma qualquer instância Y de Π
em uma instância X(Y) de Π′ de tal forma que X(Y) tem solução se e somente se Y tem solução.

• Defina as classes P, NP e problema NP-completo:
Inicialmente podemos definir um problema computacional como polinomial se há um algoritmo cujo
consumo de tempo, em seu pior caso, limita o problema em uma função polinomial. Esse tipo de
problema é o que caracteriza a classe P.
Já a classe NP é caracterizada pelos problemas de decisões nos quais a sua solução é dada por um
algoritmo não determinístico. Essa classe abrange todos os problemas P mas também alguns outros
que se comportam de maneira diferenciada. Em outras palavras, a classe NP inclui os problemas em
que ninguém conseguiu até hoje comprovar se são polinomiais ou intratáveis. Também é dito que,
para os problemas em NP, o certificado para o SIM pode ser dito em tempo polinomial.
Exemplos de NP são: Bin packing e Knapsack.
Os problemas NP-completos são definidos como uma subclasse da classe NP que inclui os problemas
mais difíceis da classe NP. Se for encontrado um algoritmo polinomial que resolva qualquer um dos
problemas NP-completos, então é possível encontrar um algoritmo polinomial para todos os outros
problemas e poderíamos comprovar a igualdade P = NP.

• P ∩ NP = ∅? Não. Na verdade P ⊆ NP, pois qualquer algoritmo polinomial que soluciona problemas
de decisão em P pode ser considerado um algoritmo não-determinístico com fase inicial vazia.
