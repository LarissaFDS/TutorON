# 1a81ca283132-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 1

1. Inteiros positivos s˜ao arranjados em um triˆangulo equil´atero com n n´umeros
em sua base, como o mostrado na figura abaixo para n = 4.
O problema
´e encontrar a menor soma em uma descida do ´apice do triˆangulo at´e sua
base por meio de uma sequˆencia de n´umeros adjacentes (mostrados na figura
pelos c´ırculos).
Projete um algoritmo de programa¸c˜ao dinˆamico para este
problema.

Solu¸c˜ao:


[OCR parcial do recorte p1-fig3.png; conferir símbolos na imagem]
int min_tri_sum(vector<vector<int>>&triang){
int n = triang.size();
vector<int>state(n,θ);
vector<int>new_state(n+1,0);
state[e]=triang[o][o];
for(int i=1;i<n;i++){
for(int j=θ;j<triang[i].size();j++){
if(j==0){
new_state[j]=triang[i][j]+state[i];
else if(j == triang[i].size()-1){
new_state[j]=triang[ij[j]+state[j-1];
else{
new_state[j]=triang[i][j]+ min(state[j-1], state[j]);
state =new_state
int min_path = INT_MAX;
for(int i=0;i<n;i++){
min_path = min(min_path, state[i]);
return min_path;
