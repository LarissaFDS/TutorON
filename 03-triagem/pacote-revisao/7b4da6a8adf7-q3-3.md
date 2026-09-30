# Revisão 7b4da6a8adf7-q3-3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 4, 5
SHA-256: dfc8e00ba0a6d1dec35e52b101b3b5b014cd456b050b9884a7fa9ed5b175158b

Confiabilidade: nao_verificada

Motivo: Revisão de fonte e conteúdo pendente.

## Enunciado e resolução — transcrição sem alteração

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

Page iv= 6k + 3 = 2(3k + 1) + 1

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

## Parecer local

A resolução apresenta argumentos lógicos corretos e segue o processo de prova por indução, contra-posição e direta. As notações matemáticas estão claras e as conclusões são válidas.

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
