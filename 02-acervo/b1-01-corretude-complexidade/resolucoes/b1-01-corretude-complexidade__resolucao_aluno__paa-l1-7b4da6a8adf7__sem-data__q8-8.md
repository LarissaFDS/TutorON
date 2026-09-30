# 7b4da6a8adf7-q8-8

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 13, 14

8. A sequˆencia de Fibonacci ´e definida da seguinte forma: f0 = 0; f1 = 1 e
fi+2 = fi+1 + fi, ∀i ≥0. Prove que para todo n ≥1 temos:


[OCR parcial do recorte p13-fig1.png; conferir símbolos na imagem]
n
1
1
fn+1
fn
1
0
fn
fn-1


em que o lado esquerdo representa n-´esima potˆencia de uma matriz 2 x 2.

Solu¸c˜ao:

A prova pode ser feita por indu¸c˜ao:

Passo Base: (n = 1)

1





An =

=

=

1
1
1
0

f1+1
f1
f1
f0

f2
f1
f1
f0

Considerando a sequˆencia de Fibonacci at´e os 3 primeiros termos, temos que:

f0 = 0
f1 = 1
f2 = f0 + f1 = 1

1



e, portanto, a matriz A =

=

, associa direta e corretamente a

1
1
1
0

f2
f1
f1
f0

sequˆencia de Fibonacci para os seus 3 primeiros elementos elementos.

Hip´otese de Indu¸c˜ao: (n ≤k)

k



Suponha que a hip´otese de indu¸c˜ao Ak =

=

,
∀n ≤k.

1
1
1
0

fk+1
fk
fk
fk−1

Page xiiiPasso Indutivo: (n = k + 1)

Deseja-se saber se a hip´otese ´e v´alida ∀n > k. Portanto, sabendo que

k

Ak+1 = Ak · A1
, por defini¸c˜ao, e
Ak =

, por hip´otese.

1
1
1
0

Segue-se que:







Ak · A =

=

·
1
1
1
0

fk+1
fk
fk
fk−1

fk+1 + fk
fk+1
fk + fk−1
fk





∴
Ak · A =

⇒
Ak+1 =

fk+2
fk+1
fk+1
fk

fk+2
fk+1
fk+1
fk

Portanto, por indu¸c˜ao, se a hip´otese ´e v´alida para n = k ent˜ao ´e v´alida para n = k+1,

n

logo a matriz An =

provˆe os {n + 1, n, n −1} -´esimos termos da

1
1
1
0

sequˆencia de Fibonacci, ∀n ≥1.

■
