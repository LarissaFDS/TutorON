# 7b4da6a8adf7-q2-2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 2, 3

Versão derivada corrigida por agente; original SHA-256: b2c9f1f8cc87a3d74a1c80c0f7a09791c3dce1925c13ee553b4dec75f0651938. Não é aprovação do professor.

Provas das somas por indução, para n>=1.
S1(n)=n(n+1)/2; S2(n)=n(n+1)(2n+1)/6; S3(n)=n^2(n+1)^2/4, onde Sr(n)=sum(i^r,i=1..n).
Caso base n=1: todas as fórmulas dão 1. Hipótese: a fórmula vale em k. Para provar k+1, some o próximo termo, e não suponha antecipadamente o resultado:
S1(k+1)=k(k+1)/2+(k+1)=(k+1)(k+2)/2.
S2(k+1)=k(k+1)(2k+1)/6+(k+1)^2=(k+1)(k+2)(2k+3)/6.
S3(k+1)=k^2(k+1)^2/4+(k+1)^3=(k+1)^2(k+2)^2/4.
Assim P(k) implica P(k+1). A frase inversa na resolução original não é o passo necessário da indução.
