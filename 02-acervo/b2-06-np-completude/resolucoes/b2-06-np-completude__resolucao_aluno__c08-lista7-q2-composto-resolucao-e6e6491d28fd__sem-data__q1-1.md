# c08

Fonte: materiais\c08_lista7_q2_composto_resolucao.md | página(s): não informada na transcrição

2. Considere o seguinte algoritmo força bruta para resolver o problema do número COMPOSTO:
Verifique inteiros sucessivos de 2 a ⌊n/2⌋ como possíveis divisores de n. Se um deles divide n,
retorna SIM; se nenhum deles o fizer, retorne NÃO. Por que esse algoritmo não coloca o
problema na classe P?

Solução: Este algoritmo não é polinomial e sim pseudo-polinomial, uma vez que a complexidade
de tempo depende do valor inserido na entrada e não do tamanho da mesma. Sendo assim, dada
uma entrada n qualquer e considerando-a um vetor binário de b bits, tem-se que:
  b = log2(n)
  2^b = 2^(log2 n)
  n = 2^b
Logo, é possível notar que a complexidade não pode ser polinomial, pois depende da quantidade
de bits do valor informado na entrada; sendo assim, a complexidade aumenta exponencialmente
com o número de bits da entrada e portanto o algoritmo é pseudo-polinomial.
