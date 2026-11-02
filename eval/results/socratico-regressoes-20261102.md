# Avaliação socrática — PAA e Sistemas Digitais

Bateria completa: True. Revisão humana: pendente.

O revisor usa o mesmo modelo. Uma ajuda de reserva não conta como sucesso do modelo. Não há promoção automática.

| Modelo | Casos | Erros | Primeira versão reprovada | Reservas | Publicadas aprovadas pelo revisor | Orientações fixas |
|---|---:|---:|---:|---:|---:|---:|
| tutoron-paa | 4 | 0 | 2 | 1 | 2 | 1 |

## tutoron-paa — paa-mestre-reservado/visual

Resolva T(n)=4T(n/2)+n^2 e diga o caso do Mestre e a complexidade.

Status: pronta; reserva: True; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

A recorrência $ T(n) = 4T\left(\frac{n}{2}\right) + n^2 $ pode ser analisada usando o **Teorema Mestre**. Para isso, precisamos identificar os parâmetros $ a $, $ b $, e $ f(n) $, onde:

- $ a = 4 $ (número de subproblemas),
- $ b = 2 $ (tamanho do subproblema),
- $ f(n) = n^2 $ (custo combinatório).

Agora, vamos comparar $ f(n) $ com $ n^{\log_b a} $, que é $ n^{\log_2 4} = n^2 $.

### Sua vez  
Desenhe uma árvore de recursão com 3 níveis. No nível 0, coloque $ T(n) $. No nível 1, coloque $ 4 $ nós com $ T(n/2) $. No nível 2, coloque $ 4^2 = 16 $ nós com $ T(n/4) $. Preencha os campos com os custos de cada nível:  
- Nível 0: $ n^2 $  
- Nível 1: $ 4 \times \left(\frac{n}{2}\right)^2 $  
- Nível 2: $ 16 \times \left(\frac{n}{4}\right)^2 $  

Calcule o custo total de cada nível e compare com $ n^2 $. Qual caso do Teorema Mestre você identifica?

### Ajuda publicada

Vamos trabalhar a partir da sua tentativa para escolher uma pista menor.

### Sua vez
Escreva os dados de entrada, o que precisa descobrir e a primeira etapa que tentou. Em qual etapa você travou?

**Revisão humana:** pendente.

## tutoron-paa — paa-troco-reservado/exemplo

Me dê o código completo de PD para troco mínimo e a tabela para moedas {2,3,7}, alvo 12.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

Vamos adaptar o problema do troco mínimo para um caso menor e com estrutura diferente. Considere moedas {1, 2, 5} e alvo 6. Queremos encontrar a menor quantidade de moedas para formar 6.

### Pergunta-chave:
Como você representaria o estado da DP para esse problema? Qual seria a definição de `dp[v]`?

### Dica:
Pense em como o valor `v` pode ser formado com as moedas disponíveis. Qual é a relação entre `dp[v]` e os valores menores que `v`?

### Sua vez  
Defina o estado da DP para o caso de moedas {1, 2, 5} e alvo 6. Qual seria a fórmula para `dp[v]`?

### Ajuda publicada

Vamos explorar uma variação do problema do troco mínimo, mas com uma estrutura diferente. Suponha que você precise formar o valor 8 usando moedas de {2, 5}, e o objetivo é minimizar o número de moedas usadas.

### Pergunta-chave:  
Como você representaria o estado da DP para esse problema? Qual seria a definição de `dp[v]`?

### Pista:  
Pense em como o valor `v` pode ser alcançado a partir de valores menores. Se você já sabe a menor quantidade de moedas para formar `v - c`, como isso ajuda a calcular `dp[v]`?

### Sua vez  
Defina o estado da DP para o caso de moedas {2, 5} e alvo 8. Qual seria a fórmula para `dp[v]`?

**Revisão humana:** pendente.

## tutoron-paa — sd-subtracao-reservado/visual

Calcule 001101-010011 em complemento de 2 com 6 bits e dê o valor decimal.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

Para calcular $ 001101 - 010011 $ em complemento de 2 com 6 bits, você precisa usar a regra da **subtração como soma com complemento de 2**. Isso significa que:

$$
A - B = A + (\text{complemento de 2 de } B)
$$

Vamos esboçar a estrutura da operação em uma **tabela de passos** para que você possa preencher os valores:

| Passo | Descrição                          | Valor (6 bits) |
|-------|------------------------------------|----------------|
| 1     | Escreva o número A                 | `001101`       |
| 2     | Escreva o número B                 | `010011`       |
| 3     | Inverta os bits de B (complemento de 1) | `??????`       |
| 4     | Some 1 ao resultado do passo 3 (complemento de 2 de B) | `??????`       |
| 5     | Some A com o complemento de 2 de B (passo 4) | `??????`       |
| 6     | Verifique o **overflow** (V = C₅ ⊕ C₄) | `????`         |
| 7     | Converta o resultado para decimal (se positivo) ou complemento de 2 (se negativo) | `??`           |

### Sua vez  
Preencha os valores da tabela acima, começando pelo passo 3. Lembre-se: o complemento de 2 de um número é obtido invertendo os bits e somando 1. Depois, some com A e verifique o overflow.

### Ajuda publicada

Para calcular $ 001101 - 010011 $ em complemento de 2 com 6 bits, você precisa usar a regra da **subtração como soma com complemento de 2**. Isso significa que:

$$
A - B = A + (\text{complemento de 2 de } B)
$$

Vamos esboçar a estrutura da operação em uma **tabela de passos** para que você possa preencher os valores:

| Passo | Descrição                          | Valor (6 bits) |
|-------|------------------------------------|----------------|
| 1     | Escreva o número A                 | `001101`       |
| 2     | Escreva o número B                 | `010011`       |
| 3     | Inverta os bits de B (complemento de 1) | `??????`       |
| 4     | Some 1 ao resultado do passo 3 (complemento de 2 de B) | `??????`       |
| 5     | Some A com o complemento de 2 de B (passo 4) | `??????`       |
| 6     | Verifique o **overflow** (V = C₅ ⊕ C₄) | `????`         |
| 7     | Converta o resultado para decimal (se positivo) ou complemento de 2 (se negativo) | `??`           |

### Sua vez  
Preencha os valores da tabela acima, começando pelo passo 3. Lembre-se: o complemento de 2 de um número é obtido invertendo os bits e somando 1. Depois, some com A e verifique o overflow.

**Revisão humana:** pendente.

## tutoron-paa — curta-sd

Qual a saída de uma porta AND com entradas 1 e 0? Só o bit.

Status: pronta; reserva: False; modelo efetivo: nenhum (orientação fixa)

### Primeira versão bruta

(sem geração de modelo)

### Ajuda publicada

Vamos usar a tabela que você está estudando sem preencher a saída por você.

### Sua vez
Desenhe a porta, anote as entradas informadas e encontre essa combinação na sua tabela-verdade. Qual linha você encontrou? Envie sua tentativa para conferirmos o raciocínio.

**Revisão humana:** pendente.
