# 70d6475b28bf-q2-2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 2, 3

2. Projete um algoritmo para o PROBLEMA DO CAMINHO HAMILTONI-
 ANO de um v´ertice fixo s.


     Solu¸c˜ao: O problema do caminho hamiltoniano pode ser resolvido atrav´es de back-
     tracking, que divide o problema total em subproblemas a fim de facilitar a sua re-
      solu¸c˜ao - pois solucionaremos pequenos problemas que resultar˜ao na resolu¸c˜ao de
    nosso principal objetivo.
   Com a divis˜ao do problema do caminho hamiltoniano em subproblemas teremos uma
    nova instˆancia dele, no qual teremos um subgrafo do original que come¸ca em um dado
      v´ertice v ∈V. Esse subgrafo nos permitir´a construir progressivamente um caminho
    ao removermos v´ertices que j´a foram visitados.
    Devemos definir os sub problemas nos pequenos grafos e, atrav´es deles, escolher
     os v´ertices que ser˜ao avaliados primeiro. Isso reduzir´a a complexidade de espa¸co do
     algoritmo, visto que um ´unico caminho ativo deve ser mantido na ´arvore dos poss´ıveis



                                   Page iicaminhos hamiltonianos. Para expandir o sub problema do caminho hamiltoniano
    come¸cando em ’s’ em um grafo G, devemos quebr´a-lo em subproblemas onde o i-´esimo
    subproblema ser´a uma instˆancia desse problema come¸cando no i-´esimo vizinho de ’s’
   em G.
