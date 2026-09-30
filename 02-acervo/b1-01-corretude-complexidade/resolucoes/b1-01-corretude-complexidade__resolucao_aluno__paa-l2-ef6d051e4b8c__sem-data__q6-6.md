# ef6d051e4b8c-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L2.pdf | página(s): 7

6. Descreva um algoritmo de tempo Θ(n lg n) que, dado um conjunto S de n
inteiros e um outro inteiro x, determine se existe ou n˜ao dois elementos em
S cuja soma seja exatamente x.

Solu¸c˜ao:


[OCR parcial do recorte p7-fig1.png; conferir símbolos na imagem]
int verifySum(int x,int *S){
mergeSort(s):
int i=0;
int j =size(S)-1;
while(i<j){
if(s[i]+S[j]>x)
j--;
else
f(S[i]+S[]<x)
i++;
elsereturn1;
return o;


Nesse algoritmo, podemos observar a fun¸c˜ao verifySum, que recebe como parˆametros
o inteiro x e o conjunto S de inteiros. Inicialmente, ordenamos o conjunto S atrav´es
do algoritmo Merge Sort, cuja complexidade ´e Θ(n lg n). Em seguida, presumimos
que size(S) retorna n, visto que ´e o tamanho de S, e percorremos o conjunto em busca
de dois inteiros nele que somando resulte no valor de x. As opera¸c˜oes que sucedem
o Merge Sort tem complexidade Θ(n). Portanto, conclui-se que o algoritmo acima
possui complexidade dominante Θ(n lg n).
