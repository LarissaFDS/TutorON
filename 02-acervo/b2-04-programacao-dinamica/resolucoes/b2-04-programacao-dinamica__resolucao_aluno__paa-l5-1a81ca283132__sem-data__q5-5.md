# 1a81ca283132-q5-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 4, 5

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
