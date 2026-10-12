# Revisão d455baef2cdf-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 1, 2, 3
SHA-256: 1826cf5ed77fe2ed6c2e34435ebc78317f847cfccac34c9b3e15410450b2d005

Confiabilidade: media

Motivo: Correção derivada por agente com fonte e hash; revisão do professor pendente.

## Enunciado e resolução — transcrição sem alteração

Ordenação da pilha de panquecas distintas com a maior na base.
Para o prefixo ativo de tamanho m, de n até 2, localize sua maior panqueca na posição p. Se já estiver na base m, não faça nada. Caso contrário, se p não for o topo, inverta o prefixo p para trazê-la ao topo; depois inverta o prefixo m para levá-la à base. Continue com m-1. Por indução, o sufixo já fixado contém as maiores panquecas nas posições corretas e não é tocado novamente.
Há no máximo 2(n-1) inversões de prefixo, portanto O(n) inversões. Essa contagem não é o tempo total: localizar a maior e movimentar um prefixo custam O(m), dando O(n^2) de tempo e O(1) de espaço auxiliar com inversão in-place. O código OCR usa limites duvidosos; esta é uma reconstrução derivada.

## Parecer local

nao_executado

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
