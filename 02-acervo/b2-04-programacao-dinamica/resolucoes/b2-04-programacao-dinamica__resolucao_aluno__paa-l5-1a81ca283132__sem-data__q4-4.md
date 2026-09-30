# 1a81ca283132-q4-4

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 4

4.
Uma subsequˆencia cont´ıgua de uma lista S ´e uma subsequˆencia feita de
elementos consecutivos de S. Por exemplo, se S ´e

5, 15, −30, 10, −5, 40, 10,

ent˜ao, 15, -30, 10 ´e uma subsequˆencia cont´ıgua, mas 5, 15, 40 n˜ao ´e. Forne¸ca
um algoritmo de tempo linear para a seguinte tarefa:

Entrada: Uma lista de n´umeros a1, a2, ..., an .

Sa´ıda: A subsequˆencia cont´ıgua de soma m´axima (a subsequˆencia de tamanho
zero tem soma zero).

Para o exemplo anterior, a resposta seria 10, -5, 40, 10, com uma soma de 55.
(Dica: Para cada j ∈1, 2, ..., n considere subsequˆencias cont´ıguas terminando
exatamente na posi¸c˜ao j .

Solu¸c˜ao:


[OCR parcial do recorte p4-fig1.png; conferir símbolos na imagem]
def max_contiguous_sum(S):
cur_max=-inf
max_local =0
start_max =0
end_max = θ
start=θ
for i in len(S):
max_local += S[i]
ifmax_local>cur_max:
cur_max =max_local
start_max = start
end_max = i
if max_local<0:
max_local = 0
start_max = i+1
for i in range(start_max,end_max):print(S[i]+"")
