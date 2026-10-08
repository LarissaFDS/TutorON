# Revisão d455baef2cdf-q9-9

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 7, 8
SHA-256: f1641b56936dfacbab3389ba7fbf80aaa3c917b3f8bb9d4a8998c074938d574f

Confiabilidade: media

Motivo: Correção derivada por agente com fonte e hash; revisão do professor pendente.

## Enunciado e resolução — transcrição sem alteração

Pico de vetor unimodal de valores distintos.
Mantenha l=1,r=n. Enquanto l<r, faça m=floor((l+r)/2). Se A[m]<A[m+1], faça l=m+1; caso contrário, faça r=m. Retorne l.
O intervalo sempre contém o pico. Se a sequência cresce entre m e m+1, o pico fica à direita; se decresce, fica em m ou à esquerda. Enquanto l<r, m<r e portanto m+1 está no vetor. Tempo O(log n), memória O(1). Não é busca pelo máximo de vetor arbitrário; a hipótese de unimodalidade permite descartar uma metade.

## Parecer local

nao_executado

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
