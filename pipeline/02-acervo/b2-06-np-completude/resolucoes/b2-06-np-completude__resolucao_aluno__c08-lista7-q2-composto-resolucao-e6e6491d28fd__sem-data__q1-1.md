# c08

Fonte: materiais\c08_lista7_q2_composto_resolucao.md | página(s): não informada na transcrição

Versão derivada corrigida por agente; original SHA-256: 98992c34d0d2690c60cf3b160b7143a1bbc3b24e2c2c62cca3eb9c12eea898a1. Não é aprovação do professor.

Por que o algoritmo força bruta de COMPOSTO não demonstra que o problema está em P?
Para n>=2, a representação binária tem b=floor(log2(n))+1 bits. Portanto 2^(b-1)<=n<2^b; não se deve escrever b=log2(n) como igualdade exata para todo inteiro.
Testar sucessivamente os divisores de 2 até floor(n/2) pode exigir Theta(n) testes no pior caso, por exemplo em entradas primas. A divisão também tem custo em bits, polinomial em b. O número de testes já cresce exponencialmente em b, apesar de ser polinomial no valor numérico n: daí a descrição pseudo-polinomial.
Isso classifica este algoritmo, não prova que COMPOSTO esteja fora de P nem que seja NP-completo. Encontrar um divisor é um certificado de composição verificável em tempo polinomial em b.
