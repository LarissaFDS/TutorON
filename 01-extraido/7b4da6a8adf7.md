# materiais\Disponiveis\RAG PAA\PAA_L1.pdf

SHA-256: 254b99147d1a9f46643b4e618ea2d04980afdb0797876f9a1bb4e8d6dafd7e97

## Página 1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: texto_pdf

Lista de Exerc´ıcios 1

8 de abril de 2022

Engenharia de Computa¸c˜ao

Lilian Giselly Pereira Santos
Pedro Henrique de Brito Nascimento
Projeto e An´alise de Algoritmos - Rian Gabriel Pinheiro

Cap´ıtulo 1 - Corretude de Algoritmos

1. Fa¸ca uma pesquisa (escreva pelo menos 10 linhas) sobre al-Khorezmi (tamb´em
al-Khwarizmi), o homem de cujo nome deriva a palavra “algoritmo”. Mostre
o que as origens das palavras “algoritmo” e “´algebra” tˆem em comum.

Solu¸c˜ao:

Mohamed ibn Musa al-Khwarizmi, nascido por volta do ano 780, viveu em Bagd´a,
localizada no Iraque. Ele trabalhou na Casa da Sabedoria, um lugar de pesquisas
cient´ıficas, e l´a estudou as obras de s´abios ´arabes, gregos e indianos.

Al-Khwarizmi ficou conhecido por criar novas maneiras de solucionar problemas
matem´aticos. Dentre os livros escritos por ele, um explicava o m´etodo de sistemas de
solu¸c˜oes que hoje ´e conhecido por ”´algebra”, palavra cuja origem vem da express˜ao
´arabe al-jabr, que aparece no t´ıtulo do livro. Este livro foi mais utilizado nas univer-
sidades europ´eias no ensino da matem´atica.

A palavra algoritmo se origina do ´arabe “al-khwarizmi” influˆencia do nome do
matem´atico ´arabe do s´eculo IX. J´a o termo ´algebra, deriva do termo al-jabr, como
j´a citado anteriormente, este termo nomeou o livro produzido pelo matem´atico onde
estava descrito um m´etodo para solu¸c˜ao de equa¸c˜oes do segundo grau, utilizando
m´etodos que somente com o que conhecemos hoje por ´algebra e a sua simbologia ´e
poss´ıvel visualizar, como a representa¸c˜ao de inc´ognitas e ra´ızes de uma equa¸c˜ao, bem
como a solu¸c˜ao de sistemas de equa¸c˜oes.

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p1.png](../01-extraido\figuras\7b4da6a8adf7\p1.png)

## Página 2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: texto_pdf

2. Prove por indu¸c˜ao que:

•
Pn

2
, para n ≥1

i=1 i = n(n+1)

•
Pn

6
, para n ≥1

i=1 i2 = n(n+1)(2n+1)

•
Pn

4
, para n ≥1

i=1 i3 = n2(n+1)2

Solu¸c˜ao:

(a) Desejamos provar que:

1 + 2 + 3 + ... + n = n(n+1)
2
Para isto, utilizaremos a prova por indu¸c˜ao e, neste caso:

Passo base (k = 1):

Neste caso,
Pi=k

2
= 1
∴
P(1) ´e verdadeiro

i=1 i = 1(1+1)

Hip´otese de Indu¸c˜ao (k ≤n):

2
, ∀k ≤n

i=1 i = k(k+1)

Supondo por hip´otese de indu¸c˜ao que: Pi=k

Passo indutivo:

Segue-se para o passo da indu¸c˜ao onde, aceitando a hip´otese de indu¸c˜ao P(k),
k ≤n, provaremos que se P(k+1) ´e verdadeiro, ent˜ao P(k) tamb´em ´e, por
indu¸c˜ao. Logo:

Pi=k+1

i=1
i = 1 + 2 + 3 + ... + k + (k + 1) = k(k+1)

2
+ (k + 1)

= k(k+1)+2(k+1)

2
= (k+1)(k+2)

2
∴
P(k+1) ´e verdadeiro. ⇒P(k) ´e verdadeiro

■

(b) Desejamos provar que:

1 + 22 + 32 + ... + n2 = n(n+1)(2n+1)
6
Para isto, utilizaremos a prova por indu¸c˜ao e, neste caso:

Passo base (k = 1):

Neste caso,
Pi=k

6
= 6

i=1 i2 = 1(1+1)(2.1+1)

6 = 1
∴
V erdadeiro

Page ii

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p2.png](../01-extraido\figuras\7b4da6a8adf7\p2.png)

## Página 3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: texto_pdf

Hip´otese de Indu¸c˜ao (k ≤n):

6
, ∀k ≤n

i=1 i2 = k(k+1)(2k+1)

Supondo por hip´otese de indu¸c˜ao que: Pi=k

Passo indutivo:

Segue-se para o passo da indu¸c˜ao onde, aceitando a hip´otese de indu¸c˜ao P(k),
k ≤n, provaremos que se P(k+1) ´e verdadeiro, ent˜ao P(k) tamb´em ´e, por
indu¸c˜ao. Logo:

Pi=k+1

i=1
i2 = 1 + 22 + 32... + k2 + (k + 1)2 = k(k+1)(2k+1)

6
+ (k + 1)2

= k(k+1)(2k+1)+6(k+1)2

6
= (k + 1)k(2k+1)+6(k+1)

6

= (k + 1)(2k2+k)+(6k+6)

6

= (k + 1)2k2+7k+6

6

= (k+1)(k+2)(2k+3)

6
= (k+1)((k+1)+1)(2(k+1)+1)

6
∴
P(k+1) ´e verdadeiro. ⇒P(k) ´e verdadeiro

■

(c) Desejamos provar que:

13 + 23 + 33 + ... + n3 = n2(n+1)2

4
Para isto, utilizaremos a prova por indu¸c˜ao e, neste caso:

Passo base (k = 1):

Neste caso,
Pi=k

4
= 4

i=1 i3 = 12(1+1)2

4 = 1
∴
P(1) ´e verdadeiro

Hip´otese de Indu¸c˜ao (k ≤n):

4
, ∀k ≤n

i=1 i3 = k2(k+1)2

Supondo por hip´otese de indu¸c˜ao que: Pi=k

Passo indutivo:

Segue-se para o passo da indu¸c˜ao onde, aceitando a hip´otese de indu¸c˜ao P(k),
k ≤n, provaremos que se P(k+1) ´e verdadeiro, ent˜ao P(k) tamb´em ´e, por
indu¸c˜ao. Logo:

Pi=k+1

i=1
i3 = 1 + 23 + 33... + k3 + (k + 1)3 = k2(k+1)2

4
+ (k + 1)3

= k2(k+1)2+4(k+1)3

4
= (k+1)2[k2+4(k+1)]

4
= (k+1)2(k2+4k+4)

4

= (k+1)2(k+2)2

4
= (k+1)2((k+1)+1)2

4
∴
P(k+1) ´e verdadeiro. ⇒P(k) ´e verdadeiro

■

Page iii

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p3.png](../01-extraido\figuras\7b4da6a8adf7\p3.png)

## Página 4

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: texto_pdf

3. Prove que:

• n3 + 2n ´e divis´ıvel por 3 para todo n ≥0, por indu¸c˜ao.

• Se 2|3m (2 divide 3m) ent˜ao 2|m, por contra-posi¸c˜ao.

• A soma de 3 n´umeros consecutivos ´e m´ultiplo de 3, use prova direta.

Solu¸c˜ao:

(a) Desejamos provar que: n3 + 2n ´e divis´ıvel por 3 para todo n ≥0.

Para isto, utilizaremos a prova por indu¸c˜ao e, neste caso:

Passo base (k = 0):

Neste caso, n3 + 2n = 03 + 2 · 0 = 0
∴
P(1) ´e verdadeiro

Hip´otese de Indu¸c˜ao (k ≤n):

Supondo por hip´otese de indu¸c˜ao que: 3 divide k3 + 2k

Passo indutivo:

Segue-se para o passo da indu¸c˜ao onde, aceitando a hip´otese de indu¸c˜ao P(k),
k ≤n, provaremos que se P(k+1) ´e verdadeiro, ent˜ao P(k) tamb´em ´e, por
indu¸c˜ao. Logo:

(k + 1)3 + 2(k + 1) = (k3 + 3k2 + 3k + 1) + 2k + 2 =

(k3 + 2k) + (3k2 + 3k + 1 + 2) = (k3 + 2k) + 3(k2 + k + 1)

Por hip´otese, temos que k3+2k ´e divis´ıvel por 3. Al´em disso, atrav´es da defini¸c˜ao
de divisibilidade: “Um n´umero inteiro n˜ao nulo a divide um inteiro b, se existe
um inteiro c, tal que b = a · c” podemos afirmar, ent˜ao, que 3 · (k2 + k + 1)
tamb´em ´e divis´ıvel por 3.
Logo, como ambas as partes s˜ao divis´ıveis por 3,
podemos afirmar que P(k+1) tamb´em ´e.

∴
P(k+1) ´e verdadeiro.

■

(b) Desejamos provar que se 2|3m (2 divide 3m) ent˜ao 2|m. Para isto, utilizaremos

a prova por contra-posi¸c˜ao, p →q = ¬q →¬p, onde:

•
p: 2 |3m
•
q: 2 |m

Dessa forma, para provarmos ¬q →¬p, temos pela defini¸c˜ao de divisibilidade:

Hip´otese: m = 2k + 1, onde k ´e qualquer n´umero inteiro.
Objetivo: 3m = 2j + 1, onde j ´e qualquer n´umero inteiro.
Desenvolvendo:

m = 2k +1 ⇒3m = 3(2k + 1)

Page iv

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p4.png](../01-extraido\figuras\7b4da6a8adf7\p4.png)

## Página 5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: rapidocr+texto_pdf

= 6k + 3 = 2(3k + 1) + 1

∴
3m = 2j + 1

Portanto, provamos que ¬q →¬p o que implica, pela prova contrapositiva, que
p →q. Dessa forma, est´a provado que se 2|3m ent˜ao 2|m.

■

(c) Desejamos provar que a soma de 3 n´umeros consecutivos ´e m´ultiplo de 3. Para

isto, utilizaremos prova direta:

Hip´otese: 3|a + (a + 1) + (a + 2)
Prova:

a + (a+1) + (a+2) = 3a + 3 = 3(a + 1) = 3k,

onde k ´e qualquer n´umero inteiro.

Pela defini¸c˜ao de divisibilidade, temos que se existe um inteiro k, tal que j = w·k,
ent˜ao, um n´umero inteiro n˜ao nulo w divide um inteiro j, dessa forma, podemos
afirmar, ent˜ao, que a + (a+1) + (a+2) ´e divis´ıvel por 3 e portanto, a + (a+1)
+ (a+2) ´e m´ultiplo de 3.

■

4. Considere um hex´agono regular cujos v´ertices s˜ao v1, v2, ..., v6. Mostre que toda
maneira de colorir os segmentos de retas que unem dois v´ertices, utilizando
as cores azul ou branca, produz pelo menos um triˆangulo cujos lados tem a
mesma cor.

Solu¸c˜ao: Considerando um hex´agono regular e suas propriedades b´asicas, ´e intuitivo
notar que existem in´umeras maneiras de colorir os segmentos de retas que unem dois
v´ertices e na figura abaixo est´a ilustrada uma delas:


[OCR parcial do recorte p5-fig1.png; conferir símbolos na imagem]
[ilegivel]


Observe que tomamos a liberdade de mudar a cor branca sugerida no enunciado para
a cor vermelha, a fim de promover uma melhor visualiza¸c˜ao do problema.

Com isso em mente, queremos provar que utilizando apenas duas cores - em nosso
caso, azul e vermelho - para colorir os segmentos de retas, teremos pelo menos um
triˆangulo com seus trˆes lados possuindo a mesma cor, independente da forma que
escolhermos distribuir as cores.

Page v

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p5.png](../01-extraido\figuras\7b4da6a8adf7\p5.png)

### Visão — candidato incerto, não validado

HTTPError

## Página 6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: rapidocr+texto_pdf

Atrav´es de prova direta, faremos a demonstra¸c˜ao:

Tomando v1 como v´ertice base, sabemos que h´a 5 segmentos de reta em conex˜ao com
ele, assim como mostram as linhas pontilhadas do hex´agono `a esquerda na figura
abaixo. Por termos apenas duas cores, podemos afirmar que pelo menos trˆes destes
segmentos possuir˜ao a mesma cor. Em nosso exemplo, escolheremos a cor vermelha
e diremos que os v´ertices v2, v4 e v6 est˜ao interligados `a v1 atrav´es de um segmento
vermelho, assim como ilustra a figura `a direita.


[OCR parcial do recorte p6-fig1.png; conferir símbolos na imagem]
V2
V2
V6
V3
V6
V3
V5
V4
V5
V4


Prosseguindo com a nossa prova:

• Se entre os segmentos v2v4, v2v6 e v4v6, ao menos um deles ´e vermelho conse-
guimos formar um triˆangulo completamente monocrom´atico, em algum dos formatos
abaixo, o que nos prova a existˆencia de pelo menos um triˆangulo de lados de mesma
cor.


[OCR parcial do recorte p6-fig2.png; conferir símbolos na imagem]
V2
V2
V2
V6
V3
V6
V3
V
V3
V5
V4
V5
V4
V5


•
No entanto, caso a afirmativa anterior seja falsa, s´o podemos assumir ent˜ao
que os trˆes segmentos v2v4, v2v6 e v4v6 s˜ao azuis. Dessa forma, tamb´em provamos a
existˆencia de um triˆangulo monocrom´atico por´em, dessa vez, azul.


[OCR parcial do recorte p6-fig3.png; conferir símbolos na imagem]
V2
V6
V3
V5
V4


■

Page vi

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p6.png](../01-extraido\figuras\7b4da6a8adf7\p6.png)

### Visão — candidato incerto, não validado

HTTPError

### Visão — candidato incerto, não validado

HTTPError

### Visão — candidato incerto, não validado

HTTPError

## Página 7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: rapidocr+texto_pdf

5. Prove a corretude do algoritmo bubblesort:


[OCR parcial do recorte p7-fig1.png; conferir símbolos na imagem]
1: procedure ALGORITMO BUBBLESORT(vetor A[1,...,n])
2:
fori←n-1→1do
3:
for j ← 0 → i - 1 do
4:
if A[j] < A[j +1] then
5:
troca(A[j],A[j+1])]
6:
endif
7:
end for
8:
end for
9: end procedure


Solu¸c˜ao:

Para provar a corretude do algoritmo Bubblesort ´e necess´ario provar os dois invari-
antes das estruturas de repeti¸c˜ao presentes no mesmo. Primeiro, o la¸co interno e,
por fim, a propriedade do primeiro la¸co servir´a de base para a prova do la¸co externo.
Assim, dando continuidade para a prova:

Invariante do la¸co interno:

Teorema: Depois da itera¸c˜ao j do loop interno, o menor elemento do vetor A[0, 1, ..., j]
estar´a na posi¸c˜ao j .

A prova ser´a feita por indu¸c˜ao:

(Inicializa¸c˜ao)

Passo Base (j=0)

Neste caso, o passo base ocorre antes da itera¸c˜ao do loop, pois no caso onde j=0,
temos o vetor A[0, ..., 0], constitu´ıdo apenas pelo elemento a0, desse modo, ele ´e o
menor elemento do vetor e, portanto, P(j=0) ´e verdadeiro.

(Manuten¸c˜ao)

Hip´otese da Indu¸c˜ao:

Como hip´otese indutiva, vamos assumir primeiramente que ap´os a itera¸c˜ao j, o menor
elemento do vetor esteja na posi¸c˜ao j.

Passo Indutivo (j ≥0):

Assim, para concluir, ´e necess´ario mostrar que ap´os a itera¸c˜ao j+1, o menor elemento
do vetor A[0, 1, ..., j, j + 1] estar´a na posi¸c˜ao j+1.

Sabemos pela hip´otese de indu¸c˜ao que ap´os a itera¸c˜ao j, o elemento da posi¸c˜ao j (aj)
´e o menor elemento. Sendo assim, na itera¸c˜ao j+1, ou o menor elemento no vetor
A[0, 1, ..., j, j + 1] ´e aj ou ´e aj+1.

Page vii

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p7.png](../01-extraido\figuras\7b4da6a8adf7\p7.png)

### Visão — candidato incerto, não validado

HTTPError

## Página 8

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: texto_pdf

De todo modo, pela linha (4) o algoritmo verifica e garante que se aj < aj+1, ocorra
a troca dos mesmos, de modo a preservar o menor elemento na posi¸c˜ao j+1 e, assim,
fica assegurado que se h´a j+1 posi¸c˜oes no vetor A[0, 1, ..., j, j + 1], ent˜ao, ap´os j+1
itera¸c˜oes, o menor elemento estar´a na posi¸c˜ao j+1.

(T´ermino)

Portanto, por indu¸c˜ao, ap´os j itera¸c˜oes o menor elemento encontra-se na posi¸c˜ao
j. Em outras palavras, ao final da execu¸c˜ao do la¸co de repeti¸c˜ao, a posi¸c˜ao j ser´a
ocupada pelo menor elemento do vetor A[0, 1, ..., j].

Invariante do la¸co externo:

Teorema: Ap´os a itera¸c˜ao “i” do loop externo, os “n −i” menores elementos do
vetor A[0, 1, ..., n −1] estar˜ao em ordem decrescente nas posi¸c˜oes i at´e n-1, ocupando
portanto, o vetor A[i, ..., n −1].

(Inicializa¸c˜ao)

De fato, na itera¸c˜ao n−1 do loop externo os 1 menores elementos ocupam as posi¸c˜oes
do vetor A[n −1, ..., n −1], que s´o possui um elemento nas posi¸c˜oes previamente
citadas (n −1 at´e n −1) e consequentemente est´a em ordem decrescente. Portanto,
o invariante ´e v´alido.

(Manuten¸c˜ao)

O invariante de la¸co ´e valido para a inicializa¸c˜ao, ou primeira itera¸c˜ao, pois de fato,
s´o h´a um elemento, consequentemente em ordem decrescente, ocupando a posi¸cao
n-1. Logo, resta analisar as pr´oximas “i” itera¸c˜oes.

Sendo assim, sabendo que o la¸co interno garante que o menor elemento do vetor
A[0, ..., i] estar´a na posi¸c˜ao i e que ao fim do la¸co externo o i ´e decrementado para
i −1. Analogamente, na pr´oxima itera¸c˜ao o subvetor A[0, ..., i −1], ter´a seu menor
valor posicionado em A[i −1] e assim sucessivamente. Desse modo, ´e f´acil observar
que ap´os estas itera¸c˜oes, a seguinte proposi¸c˜ao ´e verdadeira:

ai−1 ≥ai

Logo, ´e poss´ıvel concluir tamb´em que os elementos comparados at´e ent˜ao estar˜ao,
com base na linha (4), em ordem decrescente, mantendo a propriedade de ordena¸c˜ao
durante a execu¸c˜ao do la¸co de repeti¸c˜ao.

(T´ermino)

Ap´os o t´ermino do la¸co de repeti¸c˜ao externo, onde i=1, ´e importante lembrar que o
la¸co de repeti¸c˜ao interno foi executado, analisando os elementos do vetor A[0, ..i], logo
A[0, ..., 1], e consequentemente posicionando o elemento de menor valor na posi¸c˜ao
1 do vetor. Portanto, considerando que a inicializa¸c˜ao e manuten¸c˜ao foram v´alidas,
todos os n −i menores elementos do vetor A[0, ..., n −1] est˜ao nas posi¸c˜oes 1 at´e
n −1, consequentemente o elemento a0 ´e o maior elemento do vetor A[0, ..., n −1].

Page viii

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p8.png](../01-extraido\figuras\7b4da6a8adf7\p8.png)

## Página 9

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: rapidocr+texto_pdf

Portanto, a seguinte proposi¸c˜ao est´a correta:

a0 ≥a1 ≥... ≥an−2 ≥an−1

Consequentemente, os elementos do vetor A[0, ..., n −1], est˜ao ordenados de maneira
decrescente.

■

6. Prove a corretude do algoritmo de Horner para a avalia¸c˜ao de polinˆomios.
P(x) = anxn+ an−1xn−1+ ··· +a1x + a0.


[OCR parcial do recorte p9-fig1.png; conferir símbolos na imagem]
1: procedure ALGORITMO DE HoRNER(vetor A[O,...,n], real x)
2:
p ←A[n]
3:
fori←n-1→0do
4:
p←p*x+A[i]
5:
endfor
6:
returnp
7:endprocedure


Solu¸c˜ao:

Teorema: O algoritmo de Horner est´a correto, ou seja, retorna corretamente o
c´alculo do polinˆomio para um valor real dado.

Prova:

Considere o seguinte invariante de la¸co:

n
X

p =

Aj xj−i

j=i

Inicializa¸c˜ao: Neste caso, fica garantido, pela linha (2) que, antes de execu-
tarmos o la¸co de itera¸c˜ao propriamento dito, p resulta no coeficiente do termo
de maior grau do polinˆomio informado, isto ´e: A[n]. Assim, considerando que a
opera¸c˜ao antes do la¸co de repeti¸c˜ao torna i = n (para fins de simplifica¸c˜ao), a
2ª linha de c´odigo mostra que o invariante de la¸co est´a correto antes do loop for.

Manuten¸c˜ao: ´E poss´ıvel ent˜ao prosseguir para a execu¸c˜ao do la¸co nos passos
seguintes, onde “i” ´e decrementado uma unidade em cada itera¸c˜ao e, de mesmo
modo, a linha (4) garante que o valor do pr´oximo termo do invariante ser´a
inclu´ıdo na soma, assim como o valor do termo atual. Sendo que o resultado

Page ix

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p9.png](../01-extraido\figuras\7b4da6a8adf7\p9.png)

### Visão — candidato incerto, não validado

HTTPError

## Página 10

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: texto_pdf

da opera¸c˜ao do termo atual pelo valor real x, informado pelo usu´ario, vai sendo
parcialmente computado em cada la¸co de itera¸c˜ao. Desse modo, para:

n
X

i = n −1 :

Aj xj−i = An−1x0 + Anx1

j= n−1

n
X

i = n −2 :

Aj xj−i = An−2x0 + An−1x1 + Anx2

j= n−2

...
...
...

n
X

i = 1 :

Aj xj−i = A1 x0 + A2 x1 + ... + AN−1 xN−2 + AN xN−1

j=1

Sendo assim, ao longo da execu¸c˜ao dos la¸cos de repeti¸c˜ao

n
X

p =

Aj xj−i

j=1

T´ermino: Sabendo que a vari´avel “i” est´a sendo decrementada e avaliada de
n−1 at´e 0, e considerando que a inicializa¸c˜ao e manuten¸c˜ao do la¸co de repeti¸c˜ao
s˜ao v´alidas. Ap´os a execu¸c˜ao da ´ultima itera¸c˜ao “i = 0”, temos que o valor de p
´e:
n
X

Aj xj−i = A0 x0 + A1 x1−0 + ... + AN−1 x(N−1)−0 + AN xN−0

j=0

= A0 x0 + A1 x1 + ... + AN−1 xN−1 + AN xN

Portanto, conclui-se que o algoritmo de Horner est´a correto e ´e capaz de calcular
o valor do polinˆomio de Grau N dado para um determinado valor de x.

■

Page x

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p10.png](../01-extraido\figuras\7b4da6a8adf7\p10.png)

## Página 11

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: rapidocr+texto_pdf

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

Page xi

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p11.png](../01-extraido\figuras\7b4da6a8adf7\p11.png)

### Visão — candidato incerto, não validado

HTTPError

## Página 12

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: texto_pdf

Dessa forma, a defini¸c˜ao de invariante na inicializa¸c˜ao est´a satisfeita.

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

Page xii

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p12.png](../01-extraido\figuras\7b4da6a8adf7\p12.png)

## Página 13

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: rapidocr+texto_pdf

Temos ent˜ao que n(k + 1) ´e v´alido ∀tk ´ımpar.
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

Page xiii

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p13.png](../01-extraido\figuras\7b4da6a8adf7\p13.png)

### Visão — candidato incerto, não validado

HTTPError

## Página 14

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: texto_pdf

Passo Indutivo: (n = k + 1)

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

9. O BIN PACKING ´e um problema cuja entrada consiste em: n itens com
tamanhos s1, s2, ..., sn em que si ∈[0, 1]. O objetivo ´e encontrar o menor n´umero
de “bins” (caixas) unit´arias para armazenar os n itens. Dado os algoritmos
a seguir, mostre que eles n˜ao encontram a solu¸c˜ao ´otima do problema, ou
seja, encontre contraexemplos para cada um dos seguinte algoritmos para o
problema.

• (A) Coloque na bins os elementos em ordem da esquerda para a direita,
se ele couber, caso contr´ario tente na pr´oxima bin;

• (B) Coloque na bin mais livre o maior elemento;

• (C) Coloque o menor elemento na bin mais livre.

Page xiv

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p14.png](../01-extraido\figuras\7b4da6a8adf7\p14.png)

## Página 15

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: texto_pdf

Solu¸c˜ao: Supondo que cada bin consiga armazenar o equivalente a um item de
tamanho 1, temos que:

(a) Caso de Entrada:
(0.2, 0.8, 0.5, 0.5, 0.7, 1, 0.3)
Sa´ıda do Algoritmo A:
[0.2, 0.8], [0.5, 0.5], [0.7], [1], [0.3]
Sa´ıda Otimizada:
[0.2, 0.8], [0.5, 0.5], [0.7, 0.3], [1]

(b) Caso de Entrada:
(0.2, 0.8, 0.5, 0.5, 0.7, 1, 0.3)
Sa´ıda do Algoritmo B:
[1], [0.8], [0.7], [0.5, 0.5], [0.3, 0.2]
Sa´ıda Otimizada:
[0.2, 0.8], [0.5, 0.5], [0.7, 0.3], [1]

(c) Caso de Entrada:
(0.2, 0.8, 0.5, 0.5, 0.7, 1, 0.3)
Sa´ıda do Algoritmo C:
[0.2, 0.3, 0.5], [0.5], [0.7], [0.8], [1]
Sa´ıda Otimizada:
[0.2, 0.8], [0.5, 0.5], [0.7, 0.3], [1]

Page xv

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p15.png](../01-extraido\figuras\7b4da6a8adf7\p15.png)

## Página 16

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: rapidocr+texto_pdf

10. Considere o algoritmo de Ulam, ele termina?
De fato, conjectura-se que
seguindo o algoritmo, sempre ser´a obtida a sequencia 4, 2, 1 (Conjectura
de Collatz).
Ex:
Para o valor a = 22, ser´a obtida a seguinte sequencia:
22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
Como a prova do
t´ermino do algoritmo consiste em um dif´ıcil problema matem´atico em aberto.
Implemente um teste exaustivo mostrando que para qualquer unsigned shot
int (1 a 65535) de entrada o algoritmo para.
Escreva um pequeno relato
informando o tamanho da maior sequˆencia encontrada, o valor na qual a
maior sequˆencia foi obtida, a m´edia dos tamanhos das sequˆencias e o tempo
de execu¸c˜ao.


[OCR parcial do recorte p16-fig1.png; conferir símbolos na imagem]
1: procedure ALGORITMO DE ULAM(inteiro positivo a)
2:
D→x
3:
whileOstrésultimosvaloresdexnaofor 4,2,1do
4:
if x for par then
5:
x←x/2
6:
else
7:
x←3x+1
:8
end if
9:
endwhile
10:endprocedure


Solu¸c˜ao: Ap´os a implementa¸c˜ao do algoritmo e da execu¸c˜ao de um teste exaustivo
contendo 65535 entradas, ou seja, cobrindo a possibilidade de entrada de qualquer
unsigned short int, pudemos observar que, de fato, o algoritmo para de executar e ´e,
portanto, finito. Al´em disso, assim como ilustra a figura abaixo, algumas informa¸c˜oes
foram coletadas:

• O tamanho da maior sequˆencia equivale a 340 n´umeros;
• O valor de N para a maior sequˆencia ´e 52527;
• A m´edia dos tamanhos das sequˆencias obtidas ´e 104,21 n´umeros;
• O tempo de execu¸c˜ao do algoritmo ´e 0.06200 segundos.

Page xvi

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p16.png](../01-extraido\figuras\7b4da6a8adf7\p16.png)

### Visão — candidato incerto, não validado

HTTPError

## Página 17

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf

Qualidade: parcial; método: rapidocr+texto_pdf

[OCR parcial do recorte p17-fig1.png; conferir símbolos na imagem]
#include<stdio.h>
#include<time.h>
int maior_num=0;
double media_tam=0;
int maior_seq=0;
void ulam(int n){
int x = n;
int a3=0,a2=0,a1=0;
int num_maior_seq=1;
while((a3!=1) ll(a2!=2) 1l (a1!=4)){
if(x%2==0)x=x/2;
else x=3*x +1;
a1 = a2;
a2 = a3;
a3 = x;
num_maior_seq++;
if(num_maior_seq >= maior_seq)
maior_num = n;
maior_seq = num_maior_seq;
media_tam+=num_maior_seq;
int main(){
int n,numeros=0;
clock_t ini = clock();
while(scanf("%d"，&n)!=EOF){
ulam(n);
numeros++;
media_tam/=numeros;
clock_t fim = clock();
double tempo =(double)(fim -ini)/ (double)CLOcKS_PER_SEC;
printf("Tamanho da Maior Sequencia -> %d numeros\n",maior_seq);
printf("valor de Nparaa maior sequencia ->%d\n",maior_num);
printf("Media dos Tamanhos das Sequencias -> %.2lf numeros\n", media_tam);
printf("Tempo de Execucao ->%.51f segundo(s)",tempo);
TamanhodaMaiorSequencia->340numeros
ValordeNparaamaiorsequencia->52527
MediadosTamanhosdasSequencias->104.21r
numeros
Tempo de Execucao ->0.06200 segundo(s)


Page xvii

Imagem para conferência: [01-extraido\figuras\7b4da6a8adf7\p17.png](../01-extraido\figuras\7b4da6a8adf7\p17.png)

### Visão — candidato incerto, não validado

HTTPError
