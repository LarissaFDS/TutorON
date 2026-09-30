# 70d6475b28bf-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 1, 2

1. Um quadrado m´agico de ordem 3 ´e uma tabela 3 × 3 preenchida com nove
n´umeros inteiros distintos de 1 a 9, de modo que a soma dos n´umeros em cada
linha, coluna e duas diagonais de ponta a ponta seja a mesma. Implemente
um algoritmo backtracking e encontre todos os quadrados m´agicos de ordem
3.

Solu¸c˜ao:[OCR parcial do recorte p2-fig1.png; conferir símbolos na imagem]
intis_solution(int*matriz){
int sum_1[3]={0},sum_c[3]={θ};sum_pd=0,sum_sd=θ;
for(inti≈0;i< 9;i++)
int j = i%3;
if(i==j） sum_pd += matriz[i];
if(i+j==2） sum_sd+=matriz[i];
sum_l[i] += matriz[i];
sum_c[j] += matriz[i];
if(sum_1[0]==sum_1[1] && sum_1{1]==sum_1[2] && sum_c[0]==sum_c[1]
&& sum_c[1]==sum_c[2] && sum_c[2]== sum_pd && sum_pd == sum_sd)
return 1;
return 0;
void generate(int matriz[9],int i,int element){
if(i==9) return;
if(element==9） return;
for(int j =1; j<=9;j++)
matriz[i]=j
if(is_solution(matriz)){
print_mat(matriz);
generate(matriz,i+1,j);
int main(){
int matriz[9]={1};
int element=1;
generate(matriz,0,element);
