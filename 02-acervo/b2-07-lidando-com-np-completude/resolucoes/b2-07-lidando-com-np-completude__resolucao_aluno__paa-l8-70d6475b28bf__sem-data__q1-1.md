# 70d6475b28bf-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 1, 2

Versão derivada corrigida por agente; original SHA-256: 38bfcad4509fc4e2a4491de87c4693338d17c8c63d361da646bce1fca541dcfb. Não é aprovação do professor.

Todos os quadrados mágicos normais de ordem 3.
A soma de 1 até 9 é 45; três linhas iguais dão soma mágica 15. Preencha nove posições por backtracking, mantendo um conjunto dos números ainda não usados. A cada escolha, não repita número; se uma linha, coluna ou diagonal estiver completa, exija soma 15. Se uma linha parcial já tiver soma >=15 com posições restantes, descarte, pois os números são positivos.
Uma poda mais forte soma os menores e maiores números disponíveis para limitar o que ainda pode completar cada linha. Ao preencher as nove posições, confira as três linhas, três colunas e duas diagonais. Há oito soluções ao contar rotações e reflexões separadamente; por exemplo [[8,1,6],[3,5,7],[4,9,2]]. O centro é 5.
Um limite simples é O(9!) para permutar os números, com memória O(9). Não confundir igualdade entre diagonais com a exigência de que todas as oito somas sejam 15. O código da imagem foi substituído por descrição derivada.
