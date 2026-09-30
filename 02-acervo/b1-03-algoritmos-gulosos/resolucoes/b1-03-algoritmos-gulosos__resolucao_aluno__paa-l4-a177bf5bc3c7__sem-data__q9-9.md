# a177bf5bc3c7-q9-9

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 8, 9

9. Forne¸ca um algoritmo de tempo linear que tome como entrada uma ´arvore e
determine se ela tem um emparelhamento perfeito: um conjunto de arestas
que tocam cada v´ertice exatamente uma vez.

Solu¸c˜ao:

Page viii[OCR parcial do recorte p9-fig1.png; conferir símbolos na imagem]
def perf_match_tree(V,E):
if len(V)%2==1:return False
else:
while Ien(V);
if not len(E):
return False
leaf=select_leaf(v,E)
parent=get_parent(leaf,E)
foredge in get_edges(parent,V,E):
E.remove(edge)
V.remove(leaf)
V.remove(parent)
returnTrue
