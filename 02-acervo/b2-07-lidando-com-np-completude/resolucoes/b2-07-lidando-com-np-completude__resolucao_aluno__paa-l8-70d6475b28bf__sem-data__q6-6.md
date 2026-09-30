# 70d6475b28bf-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 9, 10, 11

6. Implemente um algoritmo backtracking para o PROBLEMA DO PASSEIO
DO CAVALO, iniciando de uma das quinas. Informe o tempo em segundos e
apresente a solu¸c˜ao.

Solu¸c˜ao:

Page ix[OCR parcial do recorte p10-fig1.png; conferir símbolos na imagem]
defprint_solution_kt(board):
for i in range(8):
for j in range(8):
print(board[ij[j], end=′')
print()
def is_valid_move(board, x, y):
# verifica se a posicao eh valida de acordo com as limitacoes
if(x >=θ and y >= θ and x< 8 and y < 8 and board[xJ[y] ==-1):
return true
return False
defsolve_kt_bt(board,curr_x,curr_y;next_x,next_y,pos):
if pos x= 64:
return True
# tenta todas as coordenadas atraves de backtracking
for i in range(8):
x=curr_x+next_x[i]
y=curr_y+next_y[i]
iF(is_valid_move(board,x,y)):
board[x][y]=pos
if(solve_kt_bt(board，x,y,next_x,next_y,pos+1)):
return True
board[x][y]=-1
return False
def knights_tour_bt():
board = [[-1 for i in range(8)] for i in range(8)]
board[e][e] =θ #inicializa 0 cavala na quina do primeiro bloco
#prox coordenadas
next_x=[2，1，~1,
nexty=[1,2,2,1,-1,~2,-2-1}
-2
-2-2,1,2}
pos = 1
#chama afuncao que vai executar o backtracking
if solve_kt_bt(board,0,θ,next_x, next_y, pos):
print_solution_kt(board)
elsey
print("There's no solution for this problem.")
knights_tour_bt()



[OCR parcial do recorte p10-fig2.png; conferir símbolos na imagem]
Considerandoacoordenadadoprimeiromoyimento,asolucaosedaaseguir:
037583542475651
593414857504346
383136412455255
336039264954344
3093261402522.53
176227102320134
82918156112421
63167281914512


O tempo em segundos decorrido para encontrar a solu¸c˜ao foi: 41.19298219680786s.
Importante observar que o tempo decorrido varia de acordo com o caminho que se
percorre, caso invertˆessemos a ordem entre next x e next y ter´ıamos encontrado uma

Page xsolu¸c˜ao em 37.05153942108154s. Al´em disso, a complexidade para esse algoritmo ´e
O(8N2).
