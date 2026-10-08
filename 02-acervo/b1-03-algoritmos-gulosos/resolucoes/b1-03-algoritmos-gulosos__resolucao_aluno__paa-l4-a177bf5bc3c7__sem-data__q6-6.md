# a177bf5bc3c7-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 6, 7

6. Um servidor tem n usu´arios esperando para serem servidos.
O tempo de
servi¸co requerido por usu´ario ´e conhecido previamente: ´e ti minutos para
o usu´ario i . Portanto se, por exemplo, os usu´arios s˜ao servidos em ordem
crescente de i , ent˜ao o i-´esimo usu´ario tem de esperar a Pi

j=1 tj minutos.
Queremos minimizar o tempo total de espera

n
X

T =

(tempo gasto pelo usu´ario i na espera).

n=1

Forne¸ca um algoritmo eficiente para computar a ordem ´otima na qual pro-
cessar os usu´arios.

Page viSolu¸c˜ao:


[OCR parcial do recorte p7-fig1.png; conferir símbolos na imagem]
8etCPUTime (user):

retur user. CPUTime
~Sched(users array):

users array. sort (key-getCputime)

f server

# pe

user ir users array: # P.

sérver -execute(user.task) #€E
