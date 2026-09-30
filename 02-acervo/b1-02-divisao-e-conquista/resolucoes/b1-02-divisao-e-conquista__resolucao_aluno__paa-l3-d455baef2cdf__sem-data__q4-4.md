# d455baef2cdf-q4-4

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 4

4. S˜ao dadas duas listas ordenadas de tamanho m e n.
Dˆe um algoritmo de
tempo O(log m + log n) para computar o k-´esimo menor elemento da uni˜ao
das duas listas.

Solu¸c˜ao:


[OCR parcial do recorte p4-fig2.png; conferir símbolos na imagem]
if (lista_A ==fim_lista_A)
return lista_B[k];
if(lista_B ==fim_lista_B)
return lista_A[k];
int meioA =(fim_lista_A -lista_A) / 2;
int meioB=(fim_lista_B-lista_B)/ 2;
if(meioA+meioB<k)
if(lista_A[meioA]>lista_B[meioB])
return k_esimo_menor(lista_A,lista_B + meioB +1,fim_lista_A,fim_lista_B,
k-meioB -1);
else
return R_esimo_menor(lista_A + meioA +1,lista_B,fim_lista_A,fim_lista_B,
k-meioA-1);
else
if(lista_A[meioA]>lista_B[meioB])
return k_esimo_menor(lista_A,lista_B, lista_A + meioA, fim_lista_B, k);
[incerto] 351a
return k_esimo_menor(lista_A,lista_B,fim_lista_A,lista_B + meioB,k);


Page iv
