# Avaliação socrática — PAA e Sistemas Digitais

Bateria completa: True. Revisão humana: pendente.

O revisor usa o mesmo modelo. Uma ajuda de reserva não conta como sucesso do modelo. Não há promoção automática.

| Modelo | Casos | Erros | Primeira versão reprovada | Reservas | Publicadas aprovadas pelo revisor | Orientações fixas |
|---|---:|---:|---:|---:|---:|---:|
| tutoron-socratico-ft | 1 | 0 | 0 | 0 | 1 | 0 |

## tutoron-socratico-ft — paa-mestre-reservado/visual

Resolva T(n)=4T(n/2)+n^2 e diga o caso do Mestre e a complexidade.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

A estrutura da árvore de recursão é formada por níveis. Cada nó representa uma chamada recursiva. O nível 0 tem um nó com custo n². O nível 1 tem 4 nós com custo (n/2)². O nível 2 tem 4² nós com custo (n/4)². O nível k tem 4^k nós com custo (n/2^k)². A soma dos custos dos níveis é a complexidade.

### Sua vez
Quantos níveis tem a árvore de recursão? Qual é o custo total dos níveis?

### Ajuda publicada

A estrutura da árvore de recursão é formada por níveis. Cada nó representa uma chamada recursiva. O nível 0 tem um nó com custo n². O nível 1 tem 4 nós com custo (n/2)². O nível 2 tem 4² nós com custo (n/4)². O nível k tem 4^k nós com custo (n/2^k)². A soma dos custos dos níveis é a complexidade.

### Sua vez
Quantos níveis tem a árvore de recursão? Qual é o custo total dos níveis?

**Revisão humana:** pendente.
