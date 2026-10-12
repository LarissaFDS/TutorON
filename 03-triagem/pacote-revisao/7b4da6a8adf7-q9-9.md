# Revisão 7b4da6a8adf7-q9-9

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 14, 15
SHA-256: 96a2de681b534ca0f5da7031e9be8f702c9a599a3e835e325ca5c4ea01ea61f7

Confiabilidade: nao_verificada

Motivo: Revisão de fonte e conteúdo pendente.

## Enunciado e resolução — transcrição sem alteração

9. O BIN PACKING ´e um problema cuja entrada consiste em: n itens com
tamanhos s1, s2, ..., sn em que si ∈[0, 1]. O objetivo ´e encontrar o menor n´umero
de “bins” (caixas) unit´arias para armazenar os n itens. Dado os algoritmos
a seguir, mostre que eles n˜ao encontram a solu¸c˜ao ´otima do problema, ou
seja, encontre contraexemplos para cada um dos seguinte algoritmos para o
problema.

• (A) Coloque na bins os elementos em ordem da esquerda para a direita,
se ele couber, caso contr´ario tente na pr´oxima bin;

• (B) Coloque na bin mais livre o maior elemento;

• (C) Coloque o menor elemento na bin mais livre.

Page xivSolu¸c˜ao: Supondo que cada bin consiga armazenar o equivalente a um item de
tamanho 1, temos que:

(a) Caso de Entrada:
(0.2, 0.8, 0.5, 0.5, 0.7, 1, 0.3)
Sa´ıda do Algoritmo A:
[0.2, 0.8], [0.5, 0.5], [0.7], [1], [0.3]
Sa´ıda Otimizada:
[0.2, 0.8], [0.5, 0.5], [0.7, 0.3], [1]

(b) Caso de Entrada:
(0.2, 0.8, 0.5, 0.5, 0.7, 1, 0.3)
Sa´ıda do Algoritmo B:
[1], [0.8], [0.7], [0.5, 0.5], [0.3, 0.2]
Sa´ıda Otimizada:
[0.2, 0.8], [0.5, 0.5], [0.7, 0.3], [1]

(c) Caso de Entrada:
(0.2, 0.8, 0.5, 0.5, 0.7, 1, 0.3)
Sa´ıda do Algoritmo C:
[0.2, 0.3, 0.5], [0.5], [0.7], [0.8], [1]
Sa´ıda Otimizada:
[0.2, 0.8], [0.5, 0.5], [0.7, 0.3], [1]

Page xv

## Parecer local

A resolução apresenta contraexemplos corretos para cada algoritmo, mostrando que eles não encontram a solução ótima. Os casos de entrada e as saídas são claramente definidos e os resultados otimizados são apresentados de forma lógica.

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
