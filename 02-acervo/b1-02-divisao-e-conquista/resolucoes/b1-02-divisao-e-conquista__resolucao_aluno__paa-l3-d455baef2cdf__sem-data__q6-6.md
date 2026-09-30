# d455baef2cdf-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 5

6. Dado A[1, . . . , n], um vetor ordenado de inteiros distintos, vocˆe quer saber
se existe um ´ındice i para o qual A[i] = i.
Dˆe um algoritmo de divis˜ao-e-
conquista que execute em tempo O(log n).

Solu¸c˜ao: Tendo em vista que temos um vetor ordenado e esse ´e o princ´ıpio b´asico
para o uso do algoritmo de busca bin´aria, que de fato utiliza a t´ecnica de dividir e
conquistar, podemos us´a-lo para a resolu¸c˜ao de nosso problema. Com isso:


[OCR parcial do recorte p5-fig1.png; conferir símbolos na imagem]
int binarySearch(int *A,int start,int end){
intmiddle
if（start<=end){
middle=(start+end)/2;//calcula aposicao do meio do array
if（middle ==A[middle]) // cheCa sei=A[i]
return middle;
else if（middle <A[middle})//log(n)
binarySearch(A,start,middle-1);//busca nametade esquerda
else
//log(n)
binarySearch(A,middle+l,end)://busca na metade direita
return-1;//elementonaoencontrado


Page v
