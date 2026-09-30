# ef6d051e4b8c-q2-2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L2.pdf | página(s): 2, 3

2. Na linguagem de sua escolha, implemente dois algoritmos para calcular o
en´esimo n´umero de Fibonacci: (a) o algoritmo baseado na defini¸c˜ao recursiva
e (b) o algoritmo iterativo.
Plote um gr´afico com o tempo de ambos os
algoritmos para cada valor de n = 1, . . . , nmax. Em que nmax ´e o maior valor
de n para o qual ambos programas executam em menos de 1 minuto em seu
computador

Page iiSolu¸c˜ao:

(a) Fibonacci Recursivo:


[OCR parcial do recorte p3-fig1.png; conferir símbolos na imagem]
longfib_recursivo(longn){
if(n==0)
return
0
if(n==1)
return
[incerto] 1;
return
fib_recursivo(n-1)+fib_recursivo(n-2);


(b) Fibonacci Iterativo:


[OCR parcial do recorte p3-fig2.png; conferir símbolos na imagem]
longfib_iterativo(long n){
1ong a=0,b=1,c;
for(inti=1;i<=n;i++)
C=a+b;
a
b;
b
=C；
returna;


Gr´afico Tempo x Entrada


[OCR parcial do recorte p3-fig3.png; conferir símbolos na imagem]
FibonacciRecursivoFibonacciIterativo
60
CustodeTempo(s)
40
20
0?680
EntradaN


Page iii
