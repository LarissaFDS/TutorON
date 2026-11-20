Hanoi com quatro pinos: analisar a estratégia apresentada, não afirmar que ela é ótima.
Para n>=2, mova n−2 discos para um pino auxiliar usando quatro pinos; mova o penúltimo para o outro auxiliar, o maior para o destino e o penúltimo para o destino; por fim mova os n−2 discos para o destino. Bases T(0)=0, T(1)=1. Assim T(n)=2T(n−2)+3.
Para n=2k, T(n)=3*2^k−3. Para n=2k+1, T(n)=4*2^k−3. Em particular T(2)=3, T(3)=5 e T(4)=9. O crescimento dessa estratégia é Theta(2^(n/2)).
A expressão 3*2^(n/2)−3 não serve para n ímpar. A recorrência conta movimentos desse algoritmo; não demonstra o mínimo possível para quatro pinos. Por exemplo existem estratégias melhores para tamanhos maiores, então não se deve chamar essa contagem de ótimo geral.
