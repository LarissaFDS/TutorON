# f38bb8142136-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L7.pdf | página(s): 8

6. O PROBLEMA DA ´ARVORE GERADORA COM RESTRIC¸ ˜AO DE GRAU
´e o seguinte.
Entrada: Um grafo n˜ao-direcionado G(V,E).
Sa´ıda: Uma ´arvore geradora de G na qual cada n´o tem grau ≤k, se uma
´arvore desse tipo existe. Mostre que para todo k ≥2 o problema ´e NP-dif´ıcil.

Solu¸c˜ao: Considerando o problema da ´arvore geradora com restri¸c˜ao de grau 2, n´os
devemos encontrar uma ´arvore cujos v´ertices possuam no m´aximo grau 2. No entanto,
uma ´arvore desse modo deve ser um caminho, j´a que criar uma ramifica¸c˜ao em todos
os v´ertices faria com que o grau daquele v´ertice fosse 3. Al´em disso, se a ´arvore
estende o grafo, ela deve ser um caminho hamiltoniano. Portanto, esse problema ´e o
mesmo que o problema do caminho hamiltoniano, que ´e NP-completo.

Dando continuidade, devemos reduzir a ´arvore geradora. Dado um grafo G(V,E),
no qual cada v´ertice v ∈V, n´os adicionaremos k - 1 v´ertices que se conectam somente
a v. Al´em disso, adicionamos um outro conjunto de v´ertices para cara v´ertice original
no grafo. Esse novo grafo pode ser denominado G’. Com isso, podemos perceber que
uma ´arvore geradora com grau k deve conter todas os v´ertices rec´em adicionados
como folhas, visto que eles possuem grau 1. Os removendo, possu´ımos uma ´arvore
geradora de grau 2. Da mesma forma, ao adicionarmos k - 2 folhas para cada v´ertice
em uma ´arvore geradora de grau 2 de G, n´os teremos uma ´arvore geradora de grau k
de G’. Portanto, podemos concluir que o problema da ´arvore geradora com restri¸c˜ao
de grau ´e NP-completo para todo k ≥2.

Tendo em vista pela hierarquia das classes que se um problema ´e NP-completo,
ele tamb´em ´e NP-dificil, visto que esse ´ultimo abrange os problemas dessa classe e
outros. Com isso, conclu´ımos a nossa prova.

■
