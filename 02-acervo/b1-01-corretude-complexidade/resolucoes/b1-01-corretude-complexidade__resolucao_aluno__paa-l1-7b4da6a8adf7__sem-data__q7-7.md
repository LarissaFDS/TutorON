# 7b4da6a8adf7-q7-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 11, 12, 13

Versão derivada corrigida por agente; original SHA-256: 9f52bb82b32d00353fd7e7fb031fba8138ee4f3b673a06a541586700cee20db3. Não é aprovação do professor.

Conversor decimal-binário de n inteiro não negativo.
Faça t=n e k=0. Enquanto t>0, guarde b[k]=t mod 2, atualize t=floor(t/2) e incremente k. Os bits são armazenados do menos significativo para o mais significativo; inverta a ordem para exibir. Para n=0, exiba 0.
Invariante após k iterações: n=sum(b[j]2^j,j=0..k-1)+t*2^k. A divisão euclidiana t=2*floor(t/2)+(t mod 2) preserva a igualdade ao acrescentar um bit. Como t diminui estritamente quando positivo, termina; em t=0 os bits representam n.
A linha extraída como t=t+2 está errada: a fonte usa divisão inteira. São O(log(n+1)) iterações; armazenar a saída exige O(log(n+1)) bits.
