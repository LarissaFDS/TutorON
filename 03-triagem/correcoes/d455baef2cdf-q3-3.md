Computar a^n para inteiro n>=0 por divisão e conquista.
potencia(a,0)=1. Para n>0, calcule uma única vez r=potencia(a,floor(n/2)); se n for par, retorne r*r; se for ímpar, retorne r*r*a.
A identidade a^(2k)=(a^k)^2 e a^(2k+1)=(a^k)^2*a prova a recorrência por indução. Há O(log n) multiplicações e profundidade O(log n), no modelo de operações aritméticas de custo unitário. O custo em bits depende do tamanho de a^n e das multiplicações. Um limite O(n log n) pedido no enunciado também é atendido por essa solução mais eficiente. Não confundir r*r com r+r; esses símbolos estão corrompidos no OCR.
