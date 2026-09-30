# 1a81ca283132-q8-8

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 7, 8

8. Forne¸ca um algoritmo de programa¸c˜ao dinˆamica (note que ser´a pseudo-polinomial)
para o problema SUBSET SUM.

Page viiEntrada: Um conjunto A com valores inteiros positivos, e um inteiro t.
Quest˜ao: Existe um subconjunto A ⊆A cuja soma dos valores seja exatamente
t?

Solu¸c˜ao:


[OCR parcial do recorte p8-fig1.png; conferir símbolos na imagem]
boot isSubsetSum(int A[], int t,int k)
bool subset[k+1][t+1];
for(int i=1;i<=t;i++)
subset[o][i]=false;
for（inti=0；i<=k;i++)
subset[i][o]=true;
for(inti=1i<=k;i++)
for（intj=1;j<=t;j++)
if(j<A[i-1])
subset[i][j]=subset[i -1][j];
if(j>=A[i-1])
subset[ij[j] =subset[i -1]tj] l| subset[i-1][j-A[i -1]];
for（int i=0;i<=ki++)
for(intj=0j<=t;j++)
printf("%4d",subset[i][i]);
cout<<"\n";
return subset[k][t];
int main()
intA[]={3,344,12,5,2}
intt=9；
intk=sizeof(A)/ sizeof(A[o]);
if (isSubsetSum(A,t,k) == true)
cout << "Foi encontrado um subconjunto cuja soma dos valores é exatamente igual a “t'.";
else
cout << "Nao ha subconjunto com soma
return 0;


Page viii
