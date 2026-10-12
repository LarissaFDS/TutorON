# 1a81ca283132-q9-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 9

9. Dado um grafo simples G(V, E ) e dois v´ertices s, t ∈V , projete um algoritmo
de programa¸c˜ao dinˆamica que encontre a quantidade de caminhos simples
distintos entre s e t

Solu¸c˜ao:


[OCR parcial do recorte p9-fig1.png; conferir símbolos na imagem]
vector<int> topo_sort(int freq[], int graph_size)
queue<int> fila;
for (int i = 0;i< n; i++){
if (!freq[i]) fila.push(i);
vector<int> grafo_ordenado;
while (!fila.empty()){
int u = fila.front();
fila.pop();
grafo_ordenado.push_back(u);
for(int i =0; i< grafo_inicial[u].size(); i++) {
freq[grafo_inicial[u][i]]--;
if (freq[grafo_inicial[u][i]]==0)
fila.push(grafo_inicial[u][i]);
return grafo_ordenado;
int caminhos_distintos(int destino, int n, int freq[])
vector<int> grafo_ordenado = topo_sort(freq, n);
int estados_anteriores[n]={ θ };
estados_anteriores[destino] =1;
for (int i = grafo_ordenado.size() -1;i >= 0; i--){
pos = grafo_ordenado[i];
for(intj=0;j<grafo_inicial[pos].size();j++){
estados_anteriores[pos] += estados_anteriores[grafo_inicial[pos][j]];
return estados_anteriores[o];


Page ix
