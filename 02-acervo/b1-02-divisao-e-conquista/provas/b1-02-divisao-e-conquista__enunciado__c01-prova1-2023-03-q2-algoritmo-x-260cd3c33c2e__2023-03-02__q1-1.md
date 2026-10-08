# c01

Fonte: materiais\c01_prova1_2023-03_q2_algoritmo_x.md | página(s): não informada na transcrição

Versão derivada corrigida por agente; original SHA-256: 95fff06c742eb5ed38f3af283cc621f7933debf9981a1287b8e6ed670990d590. Não é aprovação do professor.

Explique o que o Algoritmo X faz e prove sua corretude.
O domínio é um intervalo não vazio A[inicio..fim], com índices inteiros. Interprete a divisão do índice como piso: meio = inicio + floor((fim-inicio)/2). Se inicio=fim, retorne A[inicio]. Caso contrário, calcule a=X(A,inicio,meio), b=X(A,meio+1,fim) e retorne max(a,b). Esta versão retorna o máximo, não a soma. Sem o piso, a notação do enunciado pode produzir índices não inteiros; a interpretação foi explicitada nesta versão derivada.
