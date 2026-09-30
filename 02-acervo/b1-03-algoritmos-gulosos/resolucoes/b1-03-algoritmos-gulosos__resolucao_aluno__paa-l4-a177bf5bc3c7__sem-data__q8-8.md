# a177bf5bc3c7-q8-8

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 8

8. Um conjunto feedback de arestas de um grafo n˜ao-direcionado G = (V, E )
´e um subconjunto de arestas E

′ ⊆E que intercepta todos os ciclos do grafo.
Assim, remover as arestas E tornar´a o grafo ac´ıclico. Forne¸ca um algoritmo
eficiente para o seguinte problema:

Entrada: Grafo n˜ao-direcionado G = (V, E) com pesos de aresta positivos
we.
Sa´ıda: Um conjunto feedback de arestas definida E ⊆E de peso total m´ınimo
P

e∈E’ we.

Solu¸c˜ao:


[OCR parcial do recorte p8-fig1.png; conferir símbolos na imagem]
defminimun_weight_feedback_edge_set(V,E):
foredgeinE:
edge.weight=-edge.weight
minSpanTree =kruskal(v,E)#Kruskal vai utilizar as arestas de menor peso que,por serem
#previamente negadas，construirauma MsT cujos pesos das arestas
solution=E
#sao os maiores pesos reais
#Conjuntosolucaoinicializadocomtodasasarestas
for edge in minSpanTree:
solution.remove(edge)#Remove dasolucaoas arestascontidasnaarvoredeexpansao minima
return solution # Retornao conjunto feedback de peso minimo (complemento da MsT,cujos pesos
#das arestas sao os maximos)
