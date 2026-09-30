# a177bf5bc3c7-q3-3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 3

3. Considere o problema de agendamento de intervalos. N´os temos um conjunto
de atividades 1, 2, ..., n; cada atividade i possui um intervalo de tempo a partir
de si e termina em fi .
Um agendamento — conjunto de atividades — ´e
dito compat´ıvel, se nenhuma atividade se sobrep˜oem no tempo. O objetivo
´e determinar um agendamento compat´ıvel com o maior n´umero poss´ıvel de
atividades. Projete um algoritmo para este problema.

Solu¸c˜ao:


[OCR parcial do recorte p3-fig1.png; conferir símbolos na imagem]
def endEventTime(task):
return task.end
def scheduler(tasks):
tasks.sort(key = endEventTime) # Ordena a lista pelo tempo de termino das atividades
schedule=[]
prevEndTime =-inf #Inicializa o tempo de término parao algoritmoguloso
foriin range(1,len(tasks)):
iftasks[i].begin>prevEndTime:#Encaixa as atividades de acordo com a disponibilidade,
#ou seja,como as atividades estao ordenadas pelo tempo
schedule.append(tasks[i])
prevEndTime =tasks[i].end # de termino,a preferencia sera pelas que comecam logo
#aposoterminodamenoratividadeateomomento
return schedule
foriin scheduler(tasks):
print(i)


Page iii
