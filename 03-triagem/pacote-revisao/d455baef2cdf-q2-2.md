# Revisão d455baef2cdf-q2-2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 3
SHA-256: 5a9597fc4bd615bedd6d1f33da9b5b6a568974e7665e5fd6a91024a282a9a329

Confiabilidade: media

Motivo: Correção derivada por agente com fonte e hash; revisão do professor pendente.

## Enunciado e resolução — transcrição sem alteração

Ordenar times de um torneio sem empates de modo que cada time vença o próximo.
Represente cada time por um vértice; para cada par existe exatamente uma aresta dirigida do vencedor ao perdedor. Construa uma lista por inserção: para um novo time x, percorra a lista até o primeiro time y que x venceu; insira x imediatamente antes de y. Se x perdeu para todos os times da lista, insira no fim.
Invariante: cada elemento da lista vence o seguinte. Antes da posição de inserção, todos venceram x; o primeiro time encontrado perdeu para x. Essas são as únicas duas adjacências novas, logo o invariante é preservado. Obtém-se um caminho hamiltoniano do torneio em O(n^2) consultas aos resultados e O(n) memória para a lista, além da representação dos resultados. Listar os pares vencedor/perdedor das partidas não satisfaz a tarefa.

## Parecer local

nao_executado

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
