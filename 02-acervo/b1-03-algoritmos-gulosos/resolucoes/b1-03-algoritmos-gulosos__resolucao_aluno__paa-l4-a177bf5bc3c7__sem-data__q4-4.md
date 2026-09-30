# a177bf5bc3c7-q4-4

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 4

4. Este ´e um problema que ocorre em an´alise autom´atica de programas. Para
um conjunto de vari´aveis x1, ..., xn, s˜ao dadas algumas restri¸c˜oes de igualdade,
da forma “xi = xj”e algumas restri¸c˜oes de desigualdade, da forma xi̸ = xj.
Ser´a que ´e poss´ıvel satisfazer todas elas? Por exemplo, as restri¸c˜oes

x1 = x2, x2 = x3, x3 = x4, x1̸ = x4

n˜ao podem ser satisfeitas.
Forne¸ca um algoritmo eficiente que tome como
entrada m restri¸c˜oes sobre n vari´aveis e decida se as restri¸c˜oes podem ser
satisfeitas.

Solu¸c˜ao:


[OCR parcial do recorte p4-fig1.png; conferir símbolos na imagem]
def main():
m =int(input())
n=int(input(）)
condicoes = []
for i in range(m):
condicoes.append(input())
igualdades,desigualdades= ler_condicoes(condicoes) # Le e separa as condicoes de igualdade e desigualdade D(m)
subset=[]
for u in range(n):
subset.append(Subset(u,0)) # Constroi lista de dependencia do Grafo,
#com as componentes conexas D（n)
#Para cada igualdade,constroi as componentes conexas
for igualdadein igualdades:
union(subset, igualdade[0], igualdade[1]) # Em formato de estrutura de conjuntos disjuntos (unian-find)
flag=1
#Para cada desigualdade, verifica os pais das componentes conexas
for desigualdadein desiguaidades:
parent1 = find(subset, desigualdade[O]) #Se todos os vertices na componente conexa representam a mesma igualdade
parent2 = find(subset, desiguaidade[1]) # e portanto tem o mesmo pai. Entao basta achar  pai da componente conexa que é aproximadamente O(1)
if parent1 == parent2: # Se possuem Q mesmo pai, sao iguais e, portanto a desigualdade é invalida e consequentemente a lista de condicoes、
flag=0
print("Nao évalido")
break
if flag:print("E valido") #5e todas as desigualdades sao validas, entao o programa é valido
