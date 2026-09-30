# 1a81ca283132-q10-10

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 10

10. Mostre uma algoritmo de programa¸c˜ao dinˆamica para o problema do CAMI-
NHO M´AXIMO entre dois v´ertices s e t (caminho simples). Qual a comple-
xidade do algoritmo (tempo e mem´oria)?

Solu¸c˜ao: Um poss´ıvel algoritmo para resolver tal tarefa ´e o algoritmo de Floyd-
Warshall com uma pequena modifica¸c˜ao (o algoritmo original foi feito para computar
o caminho m´ınimo entre dois v´ertices), assim, o algoritmo ficaria:


[OCR parcial do recorte p10-fig1.png; conferir símbolos na imagem]
def floyd_warshal(adj_dist_matrix):
n=len(adj_dist_matrix[o])
max_dist=adj_dist_matrix
fork in range(1,n+1):
for i in range(1,n+1):
for j in range(1,n+1):
max_dist[i][j] =max(max_dist[i][j],max_dist[i][k]+ max_dist{kj[j])
return max_dist


Complexidade de Tempo: O(n3)
Complexidade de Mem´oria: O(n2)

Outros algoritmos mais eficientes para fontes ´unicas, como o algoritmo de Bellman-
Ford ou Djikstra, tamb´em poderiam funcionar, a abordagem, neste caso, seria a
mesma, maximizar o caminho ao v´ertice destino.

Page x
