# 1a81ca283132-q3-3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 2, 3

3. Projete um algoritmo eficiente para encontrar o comprimento do caminho
mais longo em um DAG. (Este problema ´e importante como um prot´otipo de
muitos outros aplicativos de programa¸c˜ao dinˆamica, pois determina o tempo
m´ınimo necess´ario para concluir um projeto que compreende tarefas de pre-
cedˆencia restrita.)

Solu¸c˜ao:

Page ii[OCR parcial do recorte p3-fig1.png; conferir símbolos na imagem]
def addEdge(adj,u，v):
adj[u].append(v)
def dfs(node,adj，arr,visited):
visitedfnode]=True
for i in range(0,len(adj{node])):
if not visited[adj[node][i]]:
dfs(adj[node][i],adj,arr,visited)
arr[node] = max(arr[node], 1 + arr[adj[node][i]])



[OCR parcial do recorte p3-fig2.png; conferir símbolos na imagem]
def lengthLongestPath(adj，k):
arr=[0] *(k+1)
visited =[False] *(k + 1)
for i in range(1,k + 1):
if not visited[i];
dfs(i,adj，arr,visited)
maxLength = θ
for i in range(1, k + 1):
maxlength = max(maxlength, arr[i])
return maxLength
# Main Code
k=5
adj = [[] for i in range(k + 1)]
#Exempl0
addEdge(adj,2,3)
addEdge(adj,2，4)
addEdge(adj,4,3)
addEdge(adj,3,5)
addEdge(adj,4，5)
print(lengthlongestPath(adj, k))


Page iii
