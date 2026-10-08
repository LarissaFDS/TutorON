# Revisão d455baef2cdf-q10-10

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 8, 9
SHA-256: 221250d42a50d64d8e45671f4bb24f30bda44e121719841de591cfc332a67146

Confiabilidade: media

Motivo: Correção derivada por agente com fonte e hash; revisão do professor pendente.

## Enunciado e resolução — transcrição sem alteração

Dias de compra e venda para maximizar p[venda]−p[compra], com compra<venda.
Divida os dias em duas metades. A melhor operação está inteiramente à esquerda, inteiramente à direita ou compra à esquerda e vende à direita. Resolva recursivamente as duas primeiras opções. Para a terceira, encontre preço mínimo e seu dia na metade esquerda e preço máximo e seu dia na metade direita. Compare os três lucros, guardando os índices.
Base de um único dia: nenhuma operação válida, com valor -infinito quando a compra/venda for obrigatória. Para n>=2, T(n)=2T(n/2)+O(n)=O(n log n), memória O(log n) de pilha. Se puder não operar, compare também com lucro zero.
Para preços [9,1,5], compre no dia 2 e venda no dia 3, lucro 4 por ação ou 4000 por 1000 ações. Há também solução linear mantendo o menor preço anterior, mas essa nota apresenta a divisão e conquista solicitada.

## Parecer local

nao_executado

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
