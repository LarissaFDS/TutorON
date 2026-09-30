# 70d6475b28bf-q7-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 11, 12

7. Apresente o algoritmo de busca local 2-opt para o TSP, dˆe um exemplo de
execu¸c˜ao e mostre que ele n˜ao ´e exato.

Solu¸c˜ao: Supondo que o DFS escolha arbitrariamente um v´ertice inicial para cons-
truir o caminho em pr´e-ordem e simultaneamente em ordem. Temos o seguinte algo-
ritmo:


[OCR parcial do recorte p11-fig1.png; conferir símbolos na imagem]
deftwo_opt_tsp(complete_graph):
mst_pre_solution=prim(complete_graph)
constructed_solution=dfs(mst_pre_solution)
soIution =delete_duplicate_from_tour（constructed_solution)
returnsolution


O algoritmo ´e 2-OPT pois o custo para achar um caminho que visita todos os v´ertices
exatamente uma vez, no pior dos casos, ´e o custo de executar o DFS em cada v´ertice
da MST. Neste sentido, cada aresta da MST ´e verificada 2 vezes. Assim, o custo ´e
dado por:

OPT >= MST

MSTtrilha ≤2MST

∴
MSTTrilha ≤2 · OPT

Ele n˜ao ´e exato pois depende da escolha e constru¸c˜ao da MST e da elimina¸c˜ao dos
v´ertices duplicados. Nem sempre escolhe o ´otimo global, dado que a troca de v´ertices
constr´oi um ´otimo local favor´avel `a MST.

Exemplo:


[OCR parcial do recorte p11-fig2.png; conferir símbolos na imagem]
a
1
2
3
6
4
S
5
8
10
7
b
d
9


Page xiMST : (s →a), (a →c), (s →d), (a →b)


[OCR parcial do recorte p12-fig1.png; conferir símbolos na imagem]
S
d
a
b


DFS (Pr´e/Em Ordem): s →a →c →a →b →s →d →s

Removendo duplicatas: s →a →c →a →b →s →d →s

Solu¸c˜ao Caixeiro[2-OPT]: s →a →c →b →d →s
CUSTO: 25
Solu¸c˜ao Caixeiro[´Otimo]: s →c →a →b →d →s
CUSTO: 23
