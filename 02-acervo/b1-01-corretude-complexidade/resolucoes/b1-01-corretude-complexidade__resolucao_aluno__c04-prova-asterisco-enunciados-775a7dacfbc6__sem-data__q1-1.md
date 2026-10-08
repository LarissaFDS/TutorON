# c04

Fonte: materiais\c04_prova_asterisco_enunciados.md | página(s): não informada na transcrição

Considere o seguinte algoritmo recursivo, cujo argumento n é um inteiro positivo.

1: procedure ASTERISCO(n)
2:   if n > 0 then
3:     ASTERISCO(n − 1)
4:     for i ← 1 → n do
5:       imprima "*"
6:     end for
7:     ASTERISCO(n − 1)
8:   end if
9: end procedure

Para um dado valor de n, quantos asteriscos serão impressos em uma chamada de
ASTERISCO(n)? Mostre a recorrência.

(Variante em outra prova, Q8: ASTERISCO com um laço de 1 a n seguido de uma única chamada
ASTERISCO(⌊n/2⌋) — "Mostre a recorrência e escreva a solução usando notação assintótica.")
