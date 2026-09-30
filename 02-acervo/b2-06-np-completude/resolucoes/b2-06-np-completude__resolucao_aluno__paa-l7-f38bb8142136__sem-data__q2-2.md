# f38bb8142136-q2-2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L7.pdf | página(s): 2

2. Considere o seguinte algoritmo for¸ca bruta para resolver o problema do
n´umero COMPOSTO: Verifique inteiros sucessivos de 2 a ⌊n/2⌋como poss´ıveis
divisores de n. Se um deles divide n , retorna SIM (ou seja, o n´umero ´e com-
posto); se nenhum deles o fizer, retorne N˜AO. Por que esse algoritmo n˜ao
coloca o problema na classe P?

Solu¸c˜ao: Este algoritmo n˜ao ´e polinomial e sim pseudo-polinomial, uma vez que
a complexidade de tempo depende do valor inserido na entrada e n˜ao do tamanho
da mesma. Sendo assim, dada uma entrada n qualquer e considerando-a um vetor
bin´ario de b bits, tem-se que:

b = log2(n)

2b = 2log2(n)

n = 2b

Logo, ´e poss´ıvel notar que complexidade n˜ao pode ser polinomial, pois depende da
quantidade de bits do valor informado na entrada, sendo assim a complexidade au-
menta exponencialmente com o n´umero de bits da entrada e portanto o algoritmo ´e
pseudo-polinomial.
