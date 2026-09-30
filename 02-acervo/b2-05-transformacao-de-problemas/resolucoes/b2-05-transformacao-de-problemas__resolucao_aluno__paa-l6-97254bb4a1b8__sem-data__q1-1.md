# 97254bb4a1b8-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 1

1. Maria aposta com Jo˜ao que ela pode fazer o seguinte truque. Jo˜ao recitar´a
n −1 n´umeros diferentes de 1 a n em uma ordem aleat´oria e ela ser´a capaz
de nomear o ´unico n´umero nesse intervalo que ele ter´a perdido. Claro, ela
ter´a que realizar a tarefa em sua cabe¸ca, sem fazer anota¸c˜oes. Como ela deve
fazer esse truque? Em outras palavras, projete um algoritmo que descubra o
n´umero faltante utilizando O(1) de espa¸co em mem´oria.

Solu¸c˜ao:


[OCR parcial do recorte p1-fig3.png; conferir símbolos na imagem]
lint main(){
int n,x,sum;
cin >> n;
sum=n
(n+1)/2;
for(int i=1;i<n;i++)
cin >> x；
sum-=x；
cout<<sum;
