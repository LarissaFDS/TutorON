Conversor decimal-binário de n inteiro não negativo.
Faça t=n e k=0. Enquanto t>0, guarde b[k]=t mod 2, atualize t=floor(t/2) e incremente k. Os bits são armazenados do menos significativo para o mais significativo; inverta a ordem para exibir. Para n=0, exiba 0.
Invariante após k iterações: n=sum(b[j]2^j,j=0..k-1)+t*2^k. A divisão euclidiana t=2*floor(t/2)+(t mod 2) preserva a igualdade ao acrescentar um bit. Como t diminui estritamente quando positivo, termina; em t=0 os bits representam n.
A linha extraída como t=t+2 está errada: a fonte usa divisão inteira. São O(log(n+1)) iterações; armazenar a saída exige O(log(n+1)) bits.
