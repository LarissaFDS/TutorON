# Revisão 7b4da6a8adf7-q7-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 11, 12, 13
SHA-256: 13b572ccab20134134399ade260887a44a6925ee473aee6babc614dc52b11f11

Confiabilidade: media

Motivo: Correção derivada por agente com fonte e hash; revisão do professor pendente.

## Enunciado e resolução — transcrição sem alteração

Conversor decimal-binário de n inteiro não negativo.
Faça t=n e k=0. Enquanto t>0, guarde b[k]=t mod 2, atualize t=floor(t/2) e incremente k. Os bits são armazenados do menos significativo para o mais significativo; inverta a ordem para exibir. Para n=0, exiba 0.
Invariante após k iterações: n=sum(b[j]2^j,j=0..k-1)+t*2^k. A divisão euclidiana t=2*floor(t/2)+(t mod 2) preserva a igualdade ao acrescentar um bit. Como t diminui estritamente quando positivo, termina; em t=0 os bits representam n.
A linha extraída como t=t+2 está errada: a fonte usa divisão inteira. São O(log(n+1)) iterações; armazenar a saída exige O(log(n+1)) bits.

## Parecer local

nao_executado

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
