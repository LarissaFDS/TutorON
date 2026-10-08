# Revisão 7b4da6a8adf7-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 9, 10
SHA-256: b8422278ca4a9bf2da0b7ed06994935e8af58c0bf8fceb7e4a56d17c5623b7e6

Confiabilidade: media

Motivo: Correção derivada por agente com fonte e hash; revisão do professor pendente.

## Enunciado e resolução — transcrição sem alteração

Corretude de Horner para P(x)=sum(A[j]x^j,j=0..n).
Inicialize p=A[n]. Para i=n-1,n-2,...,0, faça p=p*x+A[i]. Antes da iteração i, o invariante é p=sum(A[j]x^(j-i-1),j=i+1..n). Vale inicialmente para i=n-1, pois p=A[n]. Após o corpo, p=sum(A[j]x^(j-i),j=i..n), que é o invariante antes da próxima iteração i-1. Ao terminar i=0, p=P(x).
O número de multiplicações e adições é n, portanto O(n) operações aritméticas e O(1) memória auxiliar. Isso não limita o custo em bits para coeficientes inteiros arbitrariamente grandes. A formulação considera aritmética exata; erros de ponto flutuante são outra questão.

## Parecer local

nao_executado

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
