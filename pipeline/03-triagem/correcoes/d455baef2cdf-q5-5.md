Comparação de três recorrências, com casos base constantes.
A: T_A(n)=5T_A(n/2)+Theta(n), logo Theta(n^(log_2 5)), aproximadamente n^2,322, pelo primeiro caso do Teorema Mestre.
B: T_B(n)=2T_B(n-1)+Theta(1), logo Theta(2^n). O tamanho do subproblema é n−1; a transcrição que perdeu o sinal de menos não é a recorrência pretendida.
C: T_C(n)=9T_C(n/3)+Theta(n^2), logo Theta(n^2 log n), pelo caso de equilíbrio do Teorema Mestre.
Escolha C assintoticamente: n^2 log n cresce menos que n^2,322 e que 2^n. Arredondamentos de n/2 e n/3 não mudam essas ordens sob hipóteses usuais. Não se afirma superioridade para todo n pequeno ou todas as constantes de implementação.
