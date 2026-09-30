# 1a81ca283132-q2-2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 2

2. Algumas moedas s˜ao espalhadas nas c´elulas de um tabuleiro n × m, uma mo-
eda por c´elula. Um robˆo, localizado na c´elula superior esquerda do tabuleiro,
precisa coletar o m´aximo de moedas poss´ıvel e trazˆe-las para a c´elula inferior
direita. Em cada etapa, o robˆo pode mover uma c´elula para a direita ou uma
c´elula para baixo de sua localiza¸c˜ao atual. Quando o robˆo visita uma c´elula
com uma moeda, ele pega a moeda. Elabore um algoritmo para encontrar o
n´umero m´aximo de moedas que o robˆo pode coletar e um caminho que ele
precisa seguir para fazer isso.

Solu¸c˜ao:


[OCR parcial do recorte p2-fig1.png; conferir símbolos na imagem]
def robotPath(rows,cots,matrix):
# matriz tem rows+1 linhas e cols+1 colunas
robotPath =[[e]*(rows+1) for _in range(cols+1)]
for i in range(1, rows+1):
for j in range(1, cols+1):
# encontra o numero maximo e adc 1 se contem uma moeda
robotPath[i][j]= max(
robotpath[i-1][j],robotPath[i][j-1])+matrix[i-1][j-1]
print('As moedas coletadas pelo robo em cada nivel sao:\n',np.matrix(robotPath))
print('Quantidade maxima de moedas coletadas:',robotPath[rows][cols])
#imprime 0 caminho e o numero maximo
# define uma matriz de exemplo
rows=3
co1s=3
matrix = [{o]*rows for _ in range(cols)]
matrix =[{1,1,1]
[1,0,1],
[1,1,1]]
#envocaafuncaodorobo
robotPath(rows,cols,matrix)
