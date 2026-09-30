# f38bb8142136-q3-3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L7.pdf | página(s): 2, 3, 4

3. Responda cada um dos itens abaixo e dˆe uma justificativa para as respostas

Page ii• Se um problema Π pode ser polinomialmente reduzido a um problema Π′ e Π′ est´a
em P ent˜ao Π est´a em P?

• Se um problema Π pode ser polinomialmente reduzido a Π′ e Π′ ´e NP-completo
ent˜ao Π ´e NP-completo?

• H´a problemas em NP que n˜ao s˜ao NP-completos?

• Existem problemas NP-completos em P?

Solu¸c˜ao:

• Se um problema Π pode ser polinomialmente reduzido a um problema Π′ e Π′

est´a em P ent˜ao Π est´a em P?
Sim, em termos formais podemos dizer que se Π̸ ∈Π′ e Π ´e polinomialmente
redut´ıvel a Π′, ent˜ao Π′̸ ∈P. Isso acontece pois a classe de todos os polinˆomios ´e
fechada sob composi¸c˜ao, o que permite a combina¸c˜ao de algoritmos polinomais
de diversos jeitos sem que altere seu custo de tempo.

• Se um problema Π pode ser polinomialmente reduzido a Π′ e Π′ ´e NP-completo
ent˜ao Π ´e NP-completo?
N˜ao ´e poss´ıvel dar essa garantia. No entanto, se tivermos o cen´ario no qual
Π pode ser polinomialmente reduzido a Π′ e Π ´e NP-completo ent˜ao podemos
garantir que Π′ tamb´em ´e NP-completo.

• H´a problemas em NP que n˜ao s˜ao NP-completos?
Sim. Os problemas NP-completos consistem em apenas uma parcela da classe
NP que abrange os problemas mais dif´ıceis dela. Al´em disso, um problema em
NP s´o est´a tamb´em em NP-Completo se e somente se todos os outros problemas
em NP puderem ser transformados em tempo polinomial.

• Existem problemas NP-completos em P?
Ainda n˜ao se sabe pois isso implicaria que problemas que podem ser verificados
em tempo polinomial tamb´em podem ser resolvidos em tempo polinomial. Al´em
disso, devemos considerar que se um problema NPC puder ser resolvido por um
algoritmo polinomial, ent˜ao todos os outros problemas NPC tamb´em poder˜ao,
o que implicaria que P = NP.
Uma imagem que facilita a compreens˜ao das classes est´a a seguir:

Page iii[OCR parcial do recorte p4-fig1.png; conferir símbolos na imagem]
NP-Hard
NP-Hard
NP-Complete
P =NP
NP
NP-Complete
Complexity
P
P ≠ NP
P = NP
