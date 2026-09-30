# d455baef2cdf-q10-10

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 8, 9

10. Vocˆe est´a consultando para uma pequena empresa de investimentos.
Eles
est˜ao fazendo uma simula¸c˜ao em que eles olham para n dias consecutivos de
uma determinada a¸c˜ao, em algum momento no passado. Cara cada dia i = 1,
2, . . . , n; eles tˆem o pre¸co pi da a¸c˜ao neste dia. Suponha que durante este
per´ıodo de tempo, eles queriam comprar 1.000 a¸c˜oes em alguns dias e vender
todas essas a¸c˜oes em algum dia (mais tarde). Eles querem saber: Quando eles
deveriam ter vendido, a fim de maximizar os lucros? Por exemplo, suponha
que n = 3,p1 = 9,p2 = 1,p3 = 5. Veja que deveria retornar “comprar em 2,
vender em 3”(compra no dia 2 e vender no dia 3 significa que eles teria feito 4
por a¸c˜ao, o m´aximo poss´ıvel para esse per´ıodo). Claramente, h´a um algoritmo
simples que leva tempo O(n2): tentar todos os poss´ıveis pares compra/venda
e ver qual deles faz mais dinheiro. Elabore um algoritmo para encontrar os
dias de compra e venda com tempo O(n logn).

Solu¸c˜ao:

Page viii[OCR parcial do recorte p9-fig1.png; conferir símbolos na imagem]
from math importinf
def achar_array_intermed_max(A,comeco,fim，meio):# o(n)
soma_arr_esq = -inf
soma_tot=θ
foriinrange(meio,comeco，-1):
soma_tot= soma_tot+ A[i]
if(soma_tot > soma_arr_esq):
soma_arr_esq= soma_tot
max_ind_esq = i
soma_arr_dir =-inf
soma_tot=θ
fori in range(meio+1,fim):
soma_tot=soma_tot+A[i]
if(soma_tot>soma_arr_dir):
[incerto]  =
max_ind_dir=i
return (max_ind_esq,max_ind_dir，soma_arr_esq+soma_arr_dir)
def achar_array_max_gerat(A, comeco,fim): # O(n Log(n))
if comeco ==fim:
return(comeco,fim,A[comeco])
else:
meio=（comeco+fim)/2
(comeco_esquerdo,fim_esquerdo,soma_esquerdo)= achar_array_max_geral(A,comeco,meio) # T(n/2)
(comeco_direito,fim_direito，5oma_direito)=achar_array_max_geral(A，meio+1，fim)#T(n/2)
(comeco_intemediario,fim_intermediario,soma_intermediario)= achar_array_intermed_max(A,comeco，meio,fim)
#O(n tog(n)),
if soma_esquerdo >= soma_direito and soma_esquerdo>= soma_intermediario:
#n
return(comeco_esquerdo,fim_esquerdo,soma_esquerdo)
elif soma_direito >= soma_esquerdo and soma_direito >= soma_intermediario:
return(comeco_direito,fim_direito,soma_direito)
5
return (comeco_intemediario,fim_intermediario,soma_intermediario)


Page ix
