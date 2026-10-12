# materiais\c04_prova_asterisco_enunciados.md

SHA-256: 269a6e57f68c60201e1569a8b7ccff51b3f6fe0cf40412f40e44aae0be34168c

## Página não informada (arquivo textual)

Fonte: materiais\c04_prova_asterisco_enunciados.md

Qualidade: boa; método: texto_original

---
id: c04
fonte: "Reavaliação 28/03/2024 (Q2, 1 ponto) e 1ª Prova 2023 (Q7, 1 ponto) — Prof. Rian Gabriel Pinheiro; também Lista geral, exercício 2.8"
tipo: prova
topico: recorrências, contagem
---
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

