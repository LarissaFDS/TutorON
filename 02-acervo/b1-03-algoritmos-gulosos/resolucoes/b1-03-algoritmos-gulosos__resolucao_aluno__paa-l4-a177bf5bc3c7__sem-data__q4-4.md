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
candicoes = [1
for à in range(m):
condicoes .appendCinput ())

igualdades, desigualdades= ter. condicoes(condicoes) tê ese

subset=[]

sor v in range(s)+
sunset -append(Subset(u,2)) * Constrói list

for igualdade in igualdades:

union(subset, jgualdade[?), igualdade(1}) sé

f1ag=1

for desigualdade in desigualdades» Para © igual ica os pais 0

parent = find(subset, desigualdade[@]) é Se todos Os ert componente conexa Pé ma mesma

parent2 ind(subset, desigualdade[3]) ter p E à i p proxi!

1% parent == parent2: é Se poss eco pai, são iguais e, portanto ® de álida é consequentemente à

flag = 8
print("N válido")
=

44 Flag: peint(" 55 tã og!
