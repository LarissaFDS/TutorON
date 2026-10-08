# 1a81ca283132-q5-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 4, 5

Versão derivada corrigida por agente; original SHA-256: 5310fdae7cf8c08f22b6e41813d62271a7d4dea532f78ef3b988aa3ae3d5fc24. Não é aprovação do professor.

Maior substring comum de x e y.
Se x[i-1]=y[j-1], L[i][j]=L[i-1][j-1]+1; caso contrário, L[i][j]=0. A primeira linha e coluna são zero. A resposta é o maior valor de qualquer célula, não somente L[n][m]. A zeragem em desencontros impõe contiguidade.
Tempo O(nm), memória O(nm) ou O(m) com duas linhas. Para x=ABABC e y=BABCA, a maior substring comum é BABC, tamanho 4. Esta recorrência reconstrói a solução; o OCR do código contém índices e símbolos incertos.
