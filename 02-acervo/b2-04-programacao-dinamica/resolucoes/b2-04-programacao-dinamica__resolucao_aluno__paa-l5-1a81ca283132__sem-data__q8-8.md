# 1a81ca283132-q8-8

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 7, 8

Versão derivada corrigida por agente; original SHA-256: 6b1d27d5b3e65143f2eb8964a47b2229591f1dfcda2b6b9fd6e41b1b5ddb9870. Não é aprovação do professor.

SUBSET SUM para inteiros positivos e alvo t>=0.
Inicialize possivel[0]=True e demais posições até t em False. Para cada valor a, percorra s de t até a em ordem decrescente e faça possivel[s]=possivel[s] or possivel[s-a]. Retorne possivel[t]. O sentido decrescente impede usar o mesmo elemento mais de uma vez.
Tempo O(nt), memória O(t), pseudo-polinomial porque t pode ser exponencial no comprimento de sua representação binária. Para [3,34,4,12,5,2] e t=9, existe subconjunto [4,5]. A versão de decisão tem certificado verificável; esta DP não prova P=NP.
