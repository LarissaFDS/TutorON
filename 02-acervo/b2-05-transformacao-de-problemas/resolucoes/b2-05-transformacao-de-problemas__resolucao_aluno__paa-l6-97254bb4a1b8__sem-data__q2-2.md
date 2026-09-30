# 97254bb4a1b8-q2-2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 1, 2

2. O Rei Arthur espera n cavaleiros para um jantar anual em Camelot. Infe-
lizmente, alguns dos cavaleiros brigam entre si, e Arthur sabe quem briga
com quem. Arthur quer sentar seus convidados ao redor de uma mesa paraque dois cavaleiros briguentos n˜ao se sentem pr´oximos um do outro. Qual
problema pode ser usado para modelar a tarefa do Rei Arthur?

Solu¸c˜ao: O problema do Ciclo Hamiltoniano poderia ser utilizado para modelar o
problema do Rei Arthur com grafos, visto que cada cavaleiro poderia ser modelado
como um v´ertice do ciclo hamiltoniano. Assim sendo, o problema seria caracterizado
da seguinte forma:

Dado um grafo G = (V,E) onde V ´e o conjunto de cavaleiros e E o conjunto de arestas
que ditam se os cavaleiros podem se sentar ao lado um do outro, ent˜ao a ausˆencia
de arestas unindo dois v´ertices, por sua vez, determina a impossibilidade de dois
cavaleiros sentarem pr´oximos. Logo, o ciclo hamiltoniano representa uma solu¸c˜ao
para o problema, visto que, um caminho simples ligaria todos os v´ertices uma ´unica
vez, indicando que todos os cavaleiros poderiam se sentar `a mesa naquela disposi¸c˜ao.
Sabendo que o problema do Ciclo Hamiltoniano ´e um problema NP-Completo e que
o problema do Rei Arthur, por sua vez, uma instˆancia do Ciclo Hamiltoniano, o
certificado para o sim de uma disposi¸c˜ao qualquer de cavaleiros poderia ser dita em
tempo polinomial. A redu¸c˜ao do problema nos diz que o problema do Rei Arthur
tamb´em ´e NP-Completo.
