# 7b4da6a8adf7-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 9, 10

Versão derivada corrigida por agente; original SHA-256: 117d4ad395c2dbf825a3be75333eb4615f839fdef7b3557d43413a87752fadfc. Não é aprovação do professor.

Corretude de Horner para P(x)=sum(A[j]x^j,j=0..n).
Inicialize p=A[n]. Para i=n-1,n-2,...,0, faça p=p*x+A[i]. Antes da iteração i, o invariante é p=sum(A[j]x^(j-i-1),j=i+1..n). Vale inicialmente para i=n-1, pois p=A[n]. Após o corpo, p=sum(A[j]x^(j-i),j=i..n), que é o invariante antes da próxima iteração i-1. Ao terminar i=0, p=P(x).
O número de multiplicações e adições é n, portanto O(n) operações aritméticas e O(1) memória auxiliar. Isso não limita o custo em bits para coeficientes inteiros arbitrariamente grandes. A formulação considera aritmética exata; erros de ponto flutuante são outra questão.
