# a177bf5bc3c7-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 1, 2

1. Considere um grafo n˜ao-direcionado G = (V, E) com pesos de aresta n˜ao-
negativos we ≥0. Suponha que vocˆe computou uma ´arvore geradora m´ınima
de G e que tamb´em computou os caminhos m´ınimos para todos os n´os par-
tindo de um particular n´o s ∈V . Agora suponha que cada peso de aresta seja
aumentado em uma unidade: os novos pesos s˜ao w

′
e = we + 1.

a) Ser´a que a ´arvore geradora m´ınima muda? Dˆe um exemplo para o qual ela
muda ou prove que ela n˜ao pode mudar.

b)Ser´a que os caminhos m´ınimos mudam? Dˆe um exemplo para o qual eles
mudam ou prove que isso n˜ao pode ocorrer.

Solu¸c˜ao:

(a) N˜ao, a ´arvore geradora m´ınima permanece a mesma. Por exemplo, se G tem n

v´ertices, ent˜ao qualquer ´arvore geradora tem n - 1 arestas. Portanto, ao incre-
mentar cada peso de aresta em uma unidade, aumenta-se o custo de cada ´arvore
gerada tamb´em por uma unidade. Dessa forma, todas as ´arvores geradoras que
possu´ıam custo m´ınimo no grafo original continuam a possuir custo m´ınimo com
essa altera¸c˜ao, visto que a altera¸c˜ao foi igual para todas e, com isso, podemos
concluir que a ´arvore geradora m´ınima n˜ao ´e alterada.

(b) Sim, os caminhos m´ınimos podem mudar. Um exemplo com intuito de demons-

tra¸c˜ao se d´a a seguir:Ao supormos um grafo G, que originalmente possui arestas indo de s at´e x, de x
at´e y e de y at´e t com custo 0, e uma aresta de s at´e t com custo 1, assim como
ilustrado na figura 1, podemos notar que o melhor caminho se d´a por s →x →
y →t, totalizando um custo 0.


[OCR parcial do recorte p2-fig1.png; conferir símbolos na imagem]
X
[incerto] S


Figura 1. Grafo original.


[OCR parcial do recorte p2-fig2.png; conferir símbolos na imagem]
[incerto] X
S
2


Figura 2. Grafo incrementado.

No entanto, ap´os as altera¸c˜oes feitas no grafo G, como ilustra a figura 2, o
caminho s →x →y →t passa a ser mais custoso, com um valor de 3. Por sua
vez, o caminho s →t que antes possu´ıa desvantagem agora possui custo 2 e ´e
mais ben´efico e, portanto, se torna o novo melhor caminho, provando assim que
os camihos m´ınimos podem mudar.

Page ii
