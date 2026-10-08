# c05

Fonte: materiais\c05_lista2_q9_asterisco_resolucao.md | página(s): não informada na transcrição

Versão derivada corrigida por agente; original SHA-256: 00cd438ca3bb7f5699fd7d3d51f5882a260b658b3f173e3945bf367adef813c6. Não é aprovação do professor.

Quantos asteriscos ASTERISCO(n) imprime?
Para n inteiro não negativo: A(0)=0. Para n>=1, duas chamadas imprimem A(n-1) cada e o laço imprime n, logo A(n)=2A(n-1)+n.
A solução é A(n)=2^(n+1)-n-2. A substituição na recorrência e o caso base comprovam a fórmula. Valores: A(1)=1, A(2)=4, A(3)=11, A(4)=26. Portanto a contagem é Theta(2^n). A contagem de asteriscos não é o número de chamadas; há 2^(n+1)-1 chamadas, incluindo n=0. A variante com uma chamada em floor(n/2) tem outra recorrência e não usa esta fórmula.
