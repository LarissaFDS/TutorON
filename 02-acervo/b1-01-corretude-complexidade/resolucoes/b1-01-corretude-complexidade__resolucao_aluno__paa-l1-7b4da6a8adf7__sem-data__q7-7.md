# 7b4da6a8adf7-q7-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 11, 12, 13

7. Prove a corretude do algoritmo Conversor Decimal-Bin´ario.


[OCR parcial do recorte p11-fig1.png; conferir símbolos na imagem]
1:procedure CoNVERsORD-B(inteiro n)
2:
u→1
3:
k←0
4:
zeretodososbitsdeb
5:
whilet>0do
6:
k←k+1
7:
b[k]←tmod2
8:
t←t÷2
9:
endwhile
10:
return b
11:endprocedure


Solu¸c˜ao:

Teorema: O algoritmo Conversor Decimal-Bin´ario est´a correto, ou seja, retorna
corretamente a convers˜ao em bin´ario para um n´umero natural dado.

Prova:

Sendo:
- mk ´e o inteiro que representa o estado atual do vetor b, ap´os k itera¸c˜oes, tal que:

0,
se k = 0





mk =

i=k
P

b[i] 2i−1,
se k ≥1




i=1

- tk representa o valor de t ao final do k-´esimo loop.

Considere o seguinte invariante de la¸co, onde na itera¸c˜ao k, o vetor b[1...k] re-
presenta um inteiro mk tal que:

n(k) = mk + tk.2k, ∀k

Inicializa¸c˜ao: Neste caso, a vari´avel t ´e inicializada com o n´umero natural a
ser convertido n, o contador k = 0 e o vetor b est´a vazio. Al´em disso, a itera¸c˜ao
na inicializa¸c˜ao ´e:

para k = 0:
n(0) = t0.20 + m0 = n.1 + 0 ∴n(0) = n

Page xiDessa forma, a defini¸c˜ao de invariante na inicializa¸c˜ao est´a satisfeita.

Manuten¸c˜ao: Prosseguimos ent˜ao para a execu¸c˜ao do la¸co nos passos seguintes,
onde k ´e incrementado uma unidade a cada itera¸c˜ao e, dessa forma, o vetor b na
posi¸c˜ao k ´e atualizado com o valor da opera¸c˜ao modular com 2, isto ´e, tk mod
2. Dando prosseguimento com a atualiza¸c˜ao do valor de tk ao ser dividido por 2,
o que permite que haja o algoritmo continue para que a convers˜ao pare quando
o n´umero for menor ou igual a zero. Dessa forma, precisamos mostrar que se o
invariante de la¸co ´e v´alido para k, ele ser´a v´alido para k+1. Supomos, ent˜ao,
que n(k) ´e v´alido, ent˜ao sabemos que n(k) = tk.2k + mk e a partir do corpo do
loop deduzimos que:

k’ = k + 1
b[k’] = tk mod 2

tk′ = tk ÷ 2

Assim, temos dois casos a provar:

• Quando tk ´e par, ent˜ao b[k’] = 0 e b[1...k’] ainda representa mk.

∴
mk′ = mk

Logo
n(k) = mk + tk.2k ⇒n(k′) = mk′ + tk′.2k′

= mk + (tk/2).2k′ = mk + tk.2k = n

, temos ent˜ao que n(k + 1) ´e v´alido ∀tk par
( I )

• Quando tk ´e ´ımpar, isso nos d´a ent˜ao que b[k’] = 1 e b[1...k’] representa
2k + mk.

i=k
X

i=k+1
X

i=k′
X

b[i] 2i−1 =

b[i] 2i−1

Pois, mk =

b[i] 2i−1 ⇒mk+1 =

i=1

i=1

i=1

i=k′
X

i=k
X

=

b[i] 2i−1 = b[k′].2k +

b[i] 2i−1

i=1

i=1

∴mk′ = 2k + mk

Sabendo disso e que, quando tk ´e ´ımpar tk′ = tk−1

2 , segue-se que:

n(k) = mk + tk.2k ⇒n(k′) = mk′ + tk′.2k′

= (mk + 2k) + tk −1

2
.2k′

= (mk + 2k) + (tk −1).2k

= mk + 2k + tk.2k −2k = mk + tk.2k = n

Page xiiTemos ent˜ao que n(k + 1) ´e v´alido ∀tk ´ımpar.
( II )

Logo, de (I) e (II), temos que o invariante ´e v´alido ∀tk

T´ermino: Sabemos que o la¸co de repeti¸c˜ao executa enquanto o nosso inteiro t
´e maior do que zero, no entanto, isso acontece considerando que t inicializa com
n e ´e decrementado dividindo seu valor por dois a cada intera¸c˜ao. Desse modo,
na ´ultima itera¸c˜ao, quando “t ≤0”e “k = n”, o valor de n ´e:

n = tn.2n + mn

Portanto, conclui-se que o algoritmo Conversor D-B est´a correto e, de fato, con-
verte para bin´ario um n´umero natural dado.

■
