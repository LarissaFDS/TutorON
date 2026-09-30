# ef6d051e4b8c-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L2.pdf | página(s): 1, 2

1. Encontre o n´umero de maneiras diferentes de subir uma escada com n degraus
se cada passo pode ter um ou dois degraus. Por exemplo, uma escada de trˆes
degraus pode ser escalada de trˆes maneiras: 1–1–1, 1–2 e 2–1.

Solu¸c˜ao: Considerando n o n´umero de degraus da escada, temos que:

Para n=1:

´E necess´ario dar apenas um passo, logo:
- 1 degrau
⇒Degrau(1) = 1 maneira.

Para n=2:
Podemos subir a escada de duas maneiras:
- 1 degrau
- 2 degraus
⇒Degrau(2) = 2 maneiras.

Para n=3:
Podemos subir a escada de trˆes maneiras:
- 1 + 1 + 1 degraus
- 1 + 2 degraus
- 2 + 1 degraus
⇒Degrau(3) = 3 maneiras.

Para n=4:
Podemos subir a escada de cinco maneiras:
- 1 + 1 + 1 + 1 degraus- 1 + 1 + 2 degraus
- 2 + 2 degraus
- 2 + 1 + 1 degraus
- 2 + 2 + 1 degraus
⇒Degrau(4) = 5 maneiras.

Para n=5
Podemos subir a escada de cinco maneiras:
- 1 + 1 + 1 + 1 +1 degraus
- 1 + 1 + 1 + 2 degraus
- 1 + 1 + 2 + 1 degraus
- 1 + 2 + 1 + 1 degraus
- 1 + 2 + 2 degraus
- 2 + 1 + 1 + 1 degraus
- 2 + 1 + 2 degraus
- 2 + 2 + 1 degraus
- 2 + 2 + 1 degraus
⇒Degrau(5) = 8 maneiras.

Em resumo, obtemos as seguintes rela¸c˜oes:

Degrau(1) = 1
Degrau(2) = 2
Degrau(3) = 3
Degrau(4) = 5
Degrau(5) = 8

Portanto, ´e poss´ıvel notar que a fun¸c˜ao Degrau se assimila `a sequˆencia de Fibonacci





⇒Desse modo, a fun¸c˜ao Degrau(n) =

1,
se
n = 1
2,
se
n = 2
Degrau(n −1) + Degrau(n −2), se
n ≥3



