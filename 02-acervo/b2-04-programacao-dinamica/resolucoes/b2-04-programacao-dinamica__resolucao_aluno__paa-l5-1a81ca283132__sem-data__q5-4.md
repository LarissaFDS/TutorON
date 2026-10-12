# 1a81ca283132-q5-4

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 4, 5, 6

5. Dadas duas strings x = x1x2xney = y1y2ym, desejamos encontrar o comprimento
da maior substring comum delas, isto ´e, o maior k para o qual existem ´ındices
i e j com xi xi+1 xi+k1 = yj yj+1 yj+k1. Mostre como fazer isso em tempo O(mn)

Solu¸c˜ao:

Page iv[OCR parcial do recorte p5-fig1.png; conferir símbolos na imagem]
int longest_common_substr(char *str1, char *str2, int size1, int size2){
int suff[sizel+1][size2+1];
int max_len=0;
for(int i=0;i<sizel;i++)
for(int j=0;j<size2;j++)
if(i==0l1j==0)suff[i][j]=0；
else if(str1[i-1]== str2[j-1]){
suff[i][j]=suff[i-1][j-1]+ 1;
max_len = max(max_len,suff[ij[j]);
else
suff[i]ti]=0;
return max_len;


6.
Uma certa linguagem de processamento e strings oferece uma opera¸c˜ao pri-
mitiva que divide uma string em dois peda¸cos. Como essa opera¸c˜ao envolve
copiar a string original, ela toma n unidades de tempo para uma string de
tamanho n, n˜ao importa a posi¸c˜ao do corte. Suponha, agora, que vocˆe queira
quebrar a string em muitos peda¸cos. A ordem na qual os cortes s˜ao feitos
pode afetar o tempo de execu¸c˜ao total.
Por exemplo, se vocˆe quiser cor-
tar uma string de 20 caracteres nas posi¸c˜oes 3 e 10, fazer o primeiro corte
na posi¸c˜ao 3 incorrer´a em um custo total de 20+17 = 37, enquanto fazer a
posi¸c˜ao 10 primeiro ter´a um custo melhor de 20 + 10 = 30. Forne¸ca um algo-
ritmo de programa¸c˜ao dinˆamica que, dadas as posi¸c˜oes de m cortes em uma
string de comprimento n, encontre o custo m´ınimo de dividir a string nos m
+ 1 peda¸cos.

Solu¸c˜ao:

Page v[OCR parcial do recorte p6-fig1.png; conferir símbolos na imagem]
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <Iimits.h>
using namespace std;
int main()
int cuts, length, k, split;
while(scanf("%d%d"， &length，&cuts){= EOF)
int arr[length +1][length+1];
int cut[cuts];
int i j
memset(arr,0, sizeof(arr));
for(i=θ;i<cuts; i++)
cin >> cut[i];
for
(split=1;split<=length}split++)
for (i=0,j=i+split; }<=Iength;j++,i++)
if (split ==1)
arr[i][j】] =0;
else
int min = INT_MAX;
for (k =θ; k<cuts; k++)
if (cut[k]<j andcut[k]>i)
int cost=（j -i) +arr[ij[cut[k]] + arr[cut[k]][j];
if(cost<min)
min  costj
if (min >= INT_MAX)
arr[i[j] =θ;
else
[incerto] uw={]t]e
cout<<arr[e][length]<<endl;
return o;
