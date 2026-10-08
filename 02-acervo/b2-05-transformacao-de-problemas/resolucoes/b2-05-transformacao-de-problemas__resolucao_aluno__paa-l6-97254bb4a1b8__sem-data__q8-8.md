# 97254bb4a1b8-q8-8

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 5, 6

Versão derivada corrigida por agente; original SHA-256: 2aead388f0beafe11646843ae981f580e0a1ae281ee8dc2a0ae12f9304f00a7f. Não é aprovação do professor.

Oito damas por programação de restrições.
Variável A[i] em {1,...,8} é a coluna da dama na linha i, para i=1,...,8. Para cada par 1<=i<j<=8, imponha A[i]!=A[j] e abs(A[i]−A[j])!=j−i.
Equivalentemente, imponha AllDifferent(A[i]), AllDifferent(A[i]+i) e AllDifferent(A[i]−i). Uma dama por variável garante uma por linha; as demais restrições impedem coluna e diagonais compartilhadas.
O quantificador original para todos i,j inclui i=j e exigiria A[i]!=A[i], o que torna o modelo impossível. A restrição correta é para índices distintos. Uma solução é [1,5,8,6,3,7,2,4]; com linhas rotuladas há 92 soluções quando rotações/reflexões são contadas separadamente.
