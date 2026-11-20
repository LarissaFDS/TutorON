# d455baef2cdf-q10-10

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 8, 9

Versão derivada corrigida por agente; original SHA-256: d0374e5cca7f751d64b16ee7eb581530da6d3a20afa561a37fee90eb9d32d284. Não é aprovação do professor.

Dias de compra e venda para maximizar p[venda]−p[compra], com compra<venda.
Divida os dias em duas metades. A melhor operação está inteiramente à esquerda, inteiramente à direita ou compra à esquerda e vende à direita. Resolva recursivamente as duas primeiras opções. Para a terceira, encontre preço mínimo e seu dia na metade esquerda e preço máximo e seu dia na metade direita. Compare os três lucros, guardando os índices.
Base de um único dia: nenhuma operação válida, com valor -infinito quando a compra/venda for obrigatória. Para n>=2, T(n)=2T(n/2)+O(n)=O(n log n), memória O(log n) de pilha. Se puder não operar, compare também com lucro zero.
Para preços [9,1,5], compre no dia 2 e venda no dia 3, lucro 4 por ação ou 4000 por 1000 ações. Há também solução linear mantendo o menor preço anterior, mas essa nota apresenta a divisão e conquista solicitada.
