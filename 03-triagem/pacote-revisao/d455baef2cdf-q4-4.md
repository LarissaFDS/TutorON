# Revisão d455baef2cdf-q4-4

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 4
SHA-256: 0c7508bfd7192803550aa9881ecd9bc2ee6418860f8e45154eba80f924fb3b90

Confiabilidade: media

Motivo: Correção derivada por agente com fonte e hash; revisão do professor pendente.

## Enunciado e resolução — transcrição sem alteração

K-ésimo menor elemento da união de duas listas ordenadas A e B de tamanhos m e n, contando duplicatas.
Exija 1<=k<=m+n e coloque a lista menor em A. Procure i entre max(0,k-n) e min(k,m), com j=k-i. Use -infinito quando a partição não tiver elemento à esquerda e +infinito quando não tiver elemento à direita.
Se A[i-1]<=B[j] e B[j-1]<=A[i], retorne max(A[i-1],B[j-1]). Se A[i-1]>B[j], diminua i; caso contrário, aumente i. A busca binária encontra a partição em que exatamente k elementos ficam à esquerda, todos menores ou iguais aos da direita.
Tempo O(log(min(m,n)+1)) e memória O(1), inclusive quando uma lista é vazia, caso em que basta acessar a outra. Isso atende ao limite O(log m+log n) quando as listas são não vazias. Esta nota é reconstrução derivada; não é transcrição do código rotacionado.

## Parecer local

nao_executado

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
