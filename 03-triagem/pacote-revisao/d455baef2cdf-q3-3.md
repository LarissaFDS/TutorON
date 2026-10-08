# Revisão d455baef2cdf-q3-3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 4
SHA-256: 157f0fe26a3e598835f92393a45ed347e8788ce637ebb282db8d6075cc5bfe5f

Confiabilidade: media

Motivo: Correção derivada por agente com fonte e hash; revisão do professor pendente.

## Enunciado e resolução — transcrição sem alteração

Computar a^n para inteiro n>=0 por divisão e conquista.
potencia(a,0)=1. Para n>0, calcule uma única vez r=potencia(a,floor(n/2)); se n for par, retorne r*r; se for ímpar, retorne r*r*a.
A identidade a^(2k)=(a^k)^2 e a^(2k+1)=(a^k)^2*a prova a recorrência por indução. Há O(log n) multiplicações e profundidade O(log n), no modelo de operações aritméticas de custo unitário. O custo em bits depende do tamanho de a^n e das multiplicações. Um limite O(n log n) pedido no enunciado também é atendido por essa solução mais eficiente. Não confundir r*r com r+r; esses símbolos estão corrompidos no OCR.

## Parecer local

nao_executado

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
