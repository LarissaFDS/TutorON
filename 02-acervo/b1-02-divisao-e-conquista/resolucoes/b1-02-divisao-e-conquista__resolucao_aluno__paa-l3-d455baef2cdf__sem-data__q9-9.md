# d455baef2cdf-q9-9

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 7, 8

9. Dado um vetor A com n entradas, com cada entrada um n´umero distinto.
Sabe-se que a sequˆencia de valores A[1], A[2], . . . , A[n] ´e unimodal: ou
seja, existe ´ındice p entre 1 e n, os valores nas entradas do vetor aumentam
at´e a posi¸c˜ao p e, em seguida, reduzem, o resto do caminho, at´e que a posi¸c˜ao

Page viin. Deseja-se encontrar o “ponto de m´aximo” p. Mostre como encontrar p
atrav´es de um algoritmo O(log n).

Solu¸c˜ao:


[OCR parcial do recorte p8-fig1.png; conferir símbolos na imagem]
#include<vector>
#include<iostream>
using namespace std;
intfind_num(int*arr,intb,inte){//Arrayindexadoθa n-1
if(b==e)returnb;//Umelemento
elseif(b==e-1) returnarr[b]>arr[e]？b:e;//2Elementos
elsef/fMaisde 2elementos
int m=(b+e)>>1;//Elemento doMeio
if(arr[mj>arr[m-1]&&arr[m]>arr[m+1]) returnm;//Condicaoparamaximo
etse if(arr[m]>arr[m+1]) return find_num(arr,b,m-1);//Segue para metade esquerda
else if(arr[m]>arr[m-1]) return find_num(arr,m+1,e);//Segue para metade direita
}//ComplexidadeO(Logn)
return-1;//Erro
