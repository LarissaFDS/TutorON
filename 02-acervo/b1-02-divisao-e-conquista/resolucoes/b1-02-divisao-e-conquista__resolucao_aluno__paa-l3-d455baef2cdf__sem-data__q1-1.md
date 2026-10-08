# d455baef2cdf-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 1, 2, 3

Versão derivada corrigida por agente; original SHA-256: 69c88c88f2d77f2b6db273fe6dba878f11dd30e66c8ab1f1532d17f0d896f2f7. Não é aprovação do professor.

Ordenação da pilha de panquecas distintas com a maior na base.
Para o prefixo ativo de tamanho m, de n até 2, localize sua maior panqueca na posição p. Se já estiver na base m, não faça nada. Caso contrário, se p não for o topo, inverta o prefixo p para trazê-la ao topo; depois inverta o prefixo m para levá-la à base. Continue com m-1. Por indução, o sufixo já fixado contém as maiores panquecas nas posições corretas e não é tocado novamente.
Há no máximo 2(n-1) inversões de prefixo, portanto O(n) inversões. Essa contagem não é o tempo total: localizar a maior e movimentar um prefixo custam O(m), dando O(n^2) de tempo e O(1) de espaço auxiliar com inversão in-place. O código OCR usa limites duvidosos; esta é uma reconstrução derivada.
