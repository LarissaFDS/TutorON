# Auditoria por HTTP

Servidor: http://127.0.0.1:8001. Completa: True.

Aprovação pelo revisor não prova utilidade nem correção.

| Caso | Disciplina | Status | Modelo | Tempo (s) | Reserva |
|---|---|---|---|---:|---|
| p01-mestre-pista | paa | pronta | tutoron-paa | 17.0 | False |
| p02-mestre-erro | paa | pronta | tutoron-paa | 20.6 | False |
| p03-mestre-certo | paa | pronta | tutoron-paa | 37.5 | False |
| p04-mestre-naoaplica | paa | pronta | tutoron-paa | 34.4 | False |
| p05-arvore | paa | pronta | tutoron-paa | 43.7 | False |
| p06-laco | paa | pronta | tutoron-paa | 18.0 | False |
| p07-assintotica | paa | pronta | tutoron-paa | 28.3 | False |
| p08-mochila | paa | pronta | tutoron-paa | 15.4 | False |

## p01-mestre-pista

**Pedido:** Estou travado em T(n)=3T(n/2)+n. Não sei por onde começar.

**Tentativa:** (não enviada)

**Critério do avaliador (não enviado ao modelo):** Identificar parâmetros sem complexidade final; caso 1 ficaria apenas na referência do avaliador.

**Primeira versão bruta:**

A recorrência está na forma padrão $ T(n) = aT(n/b) + f(n) $. Identifique os valores de $ a $, $ b $ e $ f(n) $, e compare $ f(n) $ com $ n^{\log_b a} $. Qual é o caso do Teorema Mestre que se aplica aqui?

### Sua vez
Calcule $ \log_2 3 $ e compare com o grau de $ f(n) = n $. Qual caso do Teorema Mestre se aplica?

**Publicada:**

A recorrência está na forma padrão $ T(n) = aT(n/b) + f(n) $. Identifique os valores de $ a $, $ b $ e $ f(n) $, e compare $ f(n) $ com $ n^{\log_b a} $. Qual é o caso do Teorema Mestre que se aplica aqui?

### Sua vez
Calcule $ \log_2 3 $ e compare com o grau de $ f(n) = n $. Qual caso do Teorema Mestre se aplica?

**Revisões:**

[{"aprovada": true, "motivo": "A ajuda fornece uma pista adequada para iniciar a resolução da recorrência, sem entregar a solução completa ou a resposta final.", "modelo": "ollama:tutoron-paa", "segundos": 2.09}]


## p02-mestre-erro

**Pedido:** Onde está meu primeiro erro em T(n)=4T(n/2)+n^2?

**Tentativa:** Escrevi a=2 porque n é dividido por 2; escrevi b=4 porque há 4 chamadas. Depois calculei log_4(2).

**Critério do avaliador (não enviado ao modelo):** Apontar a troca entre número de chamadas e divisor, sem validar a troca nem fornecer conclusão assintótica.

**Primeira versão bruta:**

O que está correto: você identificou $ a = 4 $ (4 subproblemas) e $ b = 2 $ (divisão por 2). O erro está no cálculo do logaritmo. O Teorema Mestre exige comparar $ f(n) = n^2 $ com $ n^{\log_b a} = n^{\log_2 4} $. Qual é o valor de $ \log_2 4 $?

### Sua vez
Calcule $ \log_2 4 $ e compare $ n^2 $ com $ n^{\log_2 4} $. Qual caso do Teorema Mestre se aplica?

**Publicada:**

O que está correto: você identificou $ a = 4 $ (4 subproblemas) e $ b = 2 $ (divisão por 2). O erro está no cálculo do logaritmo. O Teorema Mestre exige comparar $ f(n) = n^2 $ com $ n^{\log_b a} = n^{\log_2 4} $. Qual é o valor de $ \log_2 4 $?

### Sua vez
Calcule $ \log_2 4 $ e compare $ n^2 $ com $ n^{\log_2 4} $. Qual caso do Teorema Mestre se aplica?

**Revisões:**

[{"aprovada": true, "motivo": "A ajuda não entrega a resposta, mas orienta o aluno a refletir sobre o cálculo do logaritmo e a aplicação do Teorema Mestre, conforme solicitado.", "modelo": "ollama:tutoron-paa", "segundos": 2.08}]


## p03-mestre-certo

**Pedido:** Pode conferir só o meu início em T(n)=4T(n/2)+n^2?

**Tentativa:** Identifiquei a=4, b=2 e f(n)=n^2. Ainda não calculei a comparação.

**Critério do avaliador (não enviado ao modelo):** Reconhecer parâmetros corretos e pedir comparação; não inventar erro nem completar caso e complexidade.

**Primeira versão bruta:**

Você identificou corretamente os parâmetros $ a = 4 $, $ b = 2 $ e $ f(n) = n^2 $. A próxima etapa é comparar $ f(n) $ com $ n^{\log_b a} $. Como $ \log_2 4 = 2 $, temos que $ n^{\log_b a} = n^2 $, o que significa que $ f(n) $ é exatamente igual a $ n^{\log_b a} $.

### Pergunta-chave:
O que acontece quando $ f(n) $ é **igual** a $ n^{\log_b a} $ no Teorema Mestre? Qual é a forma da complexidade final nesse caso?

### Sua vez
Verifique se $ f(n) = n^2 $ é de fato $ \Theta(n^{\log_b a}) $ e, se sim, qual é a complexidade final do algoritmo. Não esqueça de justificar a comparação.

**Publicada:**

Você identificou corretamente os parâmetros $ a = 4 $, $ b = 2 $ e $ f(n) = n^2 $. A próxima etapa é comparar $ f(n) $ com $ n^{\log_b a} $. Como $ \log_2 4 = 2 $, temos que $ n^{\log_b a} = n^2 $, o que significa que $ f(n) $ é exatamente igual a $ n^{\log_b a} $.

### Pergunta-chave:
O que acontece quando $ f(n) $ é **igual** a $ n^{\log_b a} $ no Teorema Mestre? Qual é a forma da complexidade final nesse caso?

### Sua vez
Verifique se $ f(n) = n^2 $ é de fato $ \Theta(n^{\log_b a}) $ e, se sim, qual é a complexidade final do algoritmo. Não esqueça de justificar a comparação.

**Revisões:**

[{"aprovada": true, "motivo": "A ajuda fornece uma explicação correta dos parâmetros e orienta o aluno sobre a próxima etapa do Teorema Mestre, sem entregar a resposta final ou resolver completamente o problema.", "modelo": "ollama:tutoron-paa", "segundos": 2.0}]


## p04-mestre-naoaplica

**Pedido:** T(n)=T(n/2)+T(n/3)+n parece divisão e conquista. Posso aplicar diretamente o Mestre clássico?

**Tentativa:** (não enviada)

**Critério do avaliador (não enviado ao modelo):** Mestre clássico não se aplica diretamente a tamanhos desiguais; sugerir analisar árvore ou outro método sem resolver.

**Primeira versão bruta:**

A recorrência $ T(n) = T(n/2) + T(n/3) + n $ **não se enquadra diretamente no Teorema Mestre** por uma razão crucial: o Teorema Mestre assume que a divisão dos subproblemas é uniforme, ou seja, todos os termos recursivos têm a mesma estrutura $ T(n/b) $. Na forma padrão do teorema, a recorrência é $ T(n) = a \cdot T(n/b) + f(n) $, onde $ a $ é o número de subproblemas e $ b $ é o fator de divisão.

No entanto, na recorrência do aluno, há **dois termos recursivos diferentes**: $ T(n/2) $ e $ T(n/3) $. Isso viola a hipótese de uniformidade dos subproblemas. O Teorema Mestre não pode ser aplicado diretamente a casos onde os subproblemas têm divisões diferentes (como $ n/2 $ e $ n/3 $), pois a comparação entre $ f(n) $ e $ n^{\log_b a} $ (onde $ a $ e $ b $ são constantes) perde sentido quando $ b $ varia entre os termos.

### Sua vez
**Explique por que a hipótese de divisão uniforme é essencial para o Teorema Mestre.** Dê um exemplo de recorrência que pode ser resolvida pelo Teorema Mestre e outro que não pode, justificando a diferença.

**Publicada:**

A recorrência $ T(n) = T(n/2) + T(n/3) + n $ **não se enquadra diretamente no Teorema Mestre** por uma razão crucial: o Teorema Mestre assume que a divisão dos subproblemas é uniforme, ou seja, todos os termos recursivos têm a mesma estrutura $ T(n/b) $. Na forma padrão do teorema, a recorrência é $ T(n) = a \cdot T(n/b) + f(n) $, onde $ a $ é o número de subproblemas e $ b $ é o fator de divisão.

No entanto, na recorrência do aluno, há **dois termos recursivos diferentes**: $ T(n/2) $ e $ T(n/3) $. Isso viola a hipótese de uniformidade dos subproblemas. O Teorema Mestre não pode ser aplicado diretamente a casos onde os subproblemas têm divisões diferentes (como $ n/2 $ e $ n/3 $), pois a comparação entre $ f(n) $ e $ n^{\log_b a} $ (onde $ a $ e $ b $ são constantes) perde sentido quando $ b $ varia entre os termos.

### Sua vez
**Explique por que a hipótese de divisão uniforme é essencial para o Teorema Mestre.** Dê um exemplo de recorrência que pode ser resolvida pelo Teorema Mestre e outro que não pode, justificando a diferença.

**Revisões:**

[{"aprovada": true, "motivo": "A ajuda explica corretamente o porquê da impossibilidade de aplicar diretamente o Teorema Mestre e deixa a pergunta final aberta, sem entregar a solução.", "modelo": "ollama:tutoron-paa", "segundos": 2.13}]


## p05-arvore

**Pedido:** Quero enxergar a estrutura de T(n)=2T(n/2)+n^2 sem resolver. Como desenho?

**Tentativa:** (não enviada)

**Critério do avaliador (não enviado ao modelo):** Estrutura parcial, raiz/filhos, sem somar árvore e sem erro de índice de níveis.

**Primeira versão bruta:**

### Visualize a estrutura da recursão

Desenhe uma **árvore de recursão** com os seguintes elementos:

1. **Raiz**:
   - Custo: $ n^2 $.
   - Filhos: 2 nós (representando $ T(n/2) $).

2. **Nível 1**:
   - Cada nó tem custo $ (n/2)^2 $.
   - Total de nós: 2.

3. **Nível 2**:
   - Cada nó tem custo $ (n/4)^2 $.
   - Total de nós: 4.

4. **...**
   - Em cada nível $ k $, o custo por nó é $ \left(\frac{n}{2^k}\right)^2 $, e o número de nós é $ 2^k $.

### Pergunta:
Qual é a profundidade total da árvore? (Dica: quando o tamanho dos subproblemas se torna 1).

### Sua vez
Desenhe os primeiros 3 níveis da árvore (raiz, nível 1 e nível 2) no papel. Marque o custo de cada nó e o número total de nós em cada nível. Depois, pense: qual é a soma dos custos em cada nível?

**Publicada:**

### Visualize a estrutura da recursão

Desenhe uma **árvore de recursão** com os seguintes elementos:

1. **Raiz**:
   - Custo: $ n^2 $.
   - Filhos: 2 nós (representando $ T(n/2) $).

2. **Nível 1**:
   - Cada nó tem custo $ \_\_\_\_\_ $.
   - Total de nós: $ \_\_\_\_\_ $.

3. **Nível 2**:
   - Cada nó tem custo $ \_\_\_\_\_ $.
   - Total de nós: $ \_\_\_\_\_ $.

4. **...**
   - Em cada nível $ k $, o custo por nó é $ \_\_\_\_\_ $, e o número de nós é $ \_\_\_\_\_ $.

### Pergunta:
Qual é a relação entre o número de nós em cada nível e a profundidade da árvore? (Dica: como o tamanho do subproblema diminui a cada nível?)

### Sua vez
Desenhe os primeiros 2 níveis da árvore no papel. Preencha os campos em branco com expressões em termos de $ n $, não com valores numéricos. Depois, pense: como a soma dos custos em cada nível se relaciona com a complexidade final?

**Revisões:**

[{"aprovada": false, "motivo": "A ajuda entrega a estrutura completa da árvore de recursão e calcula os custos em cada nível, o que não é permitido.", "modelo": "ollama:tutoron-paa", "segundos": 1.94}, {"aprovada": true, "motivo": "A ajuda oferece uma estrutura visual para a árvore de recursão, com campos em branco para o aluno preencher, sem entregar a solução completa ou a resposta final.", "modelo": "ollama:tutoron-paa", "segundos": 1.67}]


## p06-laco

**Pedido:** Como começo a contar for i=1..n: for j=i..n: x++?

**Tentativa:** (não enviada)

**Critério do avaliador (não enviado ao modelo):** Limite interno depende de i; perguntas sobre uma linha; não n(n+1)/2 nem ordem final.

**Primeira versão bruta:**

### Perguntas-guia
1. **Quantas vezes o bloco `x++` é executado para um valor fixo de `i`?** Por exemplo, se `i = 3`, quantos valores de `j` satisfazem `j ≥ i` e `j ≤ n`?

2. **Se você somar o número de iterações do `for j` para todos os valores de `i` de 1 até n, o que isso representa?** Há uma fórmula conhecida para essa soma?

3. **Como o valor final de `x` está relacionado ao número total de iterações do `for j`?**

### Sua vez
Calcule o número total de vezes que `x++` é executado para `n = 5`. Depois, generalize para qualquer `n`.

**Publicada:**

### Perguntas-guia
1. **Quantas vezes o bloco `x++` é executado para um valor fixo de `i`?** Por exemplo, se `i = 3`, quantos valores de `j` satisfazem `j ≥ i` e `j ≤ n`?

2. **Se você somar o número de iterações do `for j` para todos os valores de `i` de 1 até n, o que isso representa?** Há uma fórmula conhecida para essa soma?

3. **Como o valor final de `x` está relacionado ao número total de iterações do `for j`?**

### Sua vez
Calcule o número total de vezes que `x++` é executado para `n = 5`. Depois, generalize para qualquer `n`.

**Revisões:**

[{"aprovada": true, "motivo": "As perguntas-guia são adequadas e levam o aluno ao raciocínio necessário para resolver o problema. A última parte pede cálculo e generalização, mantendo a estrutura aberta para o aluno.", "modelo": "ollama:tutoron-paa", "segundos": 2.05}]


## p07-assintotica

**Pedido:** Qual é a diferença entre O, Omega e Theta? Eu sempre trato O como uma igualdade exata.

**Tentativa:** (não enviada)

**Critério do avaliador (não enviado ao modelo):** Explicar superior, inferior e apertado; corrigir igualdade exata; conceitos não exigem recusa.

**Primeira versão bruta:**

A notação **O** (Big O) descreve um **limitante superior** da taxa de crescimento de uma função. Dizemos que $ f(n) = O(g(n)) $ se, para valores suficientemente grandes de $ n $, $ f(n) $ cresce **não mais rápido** que $ g(n) $, ou seja, $ f(n) \leq c \cdot g(n) $ para alguma constante $ c > 0 $. É uma **cota superior**.

A notação **Ω** (Big Omega) é o oposto: $ f(n) = \Omega(g(n)) $ significa que $ f(n) $ cresce **não mais devagar** que $ g(n) $, ou seja, $ f(n) \geq c \cdot g(n) $ para alguma constante $ c > 0 $. É uma **cota inferior**.

A notação **Θ** (Theta) combina as duas: $ f(n) = \Theta(g(n)) $ se $ f(n) $ cresce **exatamente** na mesma taxa que $ g(n) $, ou seja, $ f(n) = O(g(n)) $ **e** $ f(n) = \Omega(g(n)) $. É uma **cota exata**.

### Armadilhas comuns:
- Tratar **O** como igualdade exata (como o aluno menciona) é um erro: $ O $ é uma **limitação superior**, não uma igualdade. Por exemplo, $ n^2 = O(n^3) $, mas $ n^2 \neq \Theta(n^3) $.
- Misturar notações: um algoritmo pode ter tempo de execução $ O(n^2) $, mas isso não implica que ele seja **exatamente** $ n^2 $, apenas que não ultrapasse esse limite.

### Sua vez
Dado que $ f(n) = 3n^2 + 2n + 1 $, classifique $ f(n) $ em termos de $ O $, $ \Omega $ e $ \Theta $ em relação a $ g(n) = n^2 $. Justifique sua resposta com base nas definições acima.

**Publicada:**

A notação **O** (Big O) descreve um **limitante superior** da taxa de crescimento de uma função. Dizemos que $ f(n) = O(g(n)) $ se, para valores suficientemente grandes de $ n $, $ f(n) $ cresce **não mais rápido** que $ g(n) $, ou seja, $ f(n) \leq c \cdot g(n) $ para alguma constante $ c > 0 $. É uma **cota superior**.

A notação **Ω** (Big Omega) é o oposto: $ f(n) = \Omega(g(n)) $ significa que $ f(n) $ cresce **não mais devagar** que $ g(n) $, ou seja, $ f(n) \geq c \cdot g(n) $ para alguma constante $ c > 0 $. É uma **cota inferior**.

A notação **Θ** (Theta) combina as duas: $ f(n) = \Theta(g(n)) $ se $ f(n) $ cresce **exatamente** na mesma taxa que $ g(n) $, ou seja, $ f(n) = O(g(n)) $ **e** $ f(n) = \Omega(g(n)) $. É uma **cota exata**.

### Armadilhas comuns:
- Tratar **O** como igualdade exata (como o aluno menciona) é um erro: $ O $ é uma **limitação superior**, não uma igualdade. Por exemplo, $ n^2 = O(n^3) $, mas $ n^2 \neq \Theta(n^3) $.
- Misturar notações: um algoritmo pode ter tempo de execução $ O(n^2) $, mas isso não implica que ele seja **exatamente** $ n^2 $, apenas que não ultrapasse esse limite.

### Sua vez
Dado que $ f(n) = 3n^2 + 2n + 1 $, classifique $ f(n) $ em termos de $ O $, $ \Omega $ e $ \Theta $ em relação a $ g(n) = n^2 $. Justifique sua resposta com base nas definições acima.

**Revisões:**

[{"aprovada": true, "motivo": "A ajuda explica corretamente os conceitos de O, Ω e Θ, alerta sobre as armadilhas comuns e deixa a pergunta final aberta para o aluno. Não entrega a resposta final nem a resolução completa.", "modelo": "ollama:tutoron-paa", "segundos": 2.64}]


## p08-mochila

**Pedido:** Não consigo definir o estado da mochila 0/1. O que devo pensar antes de escrever a fórmula?

**Tentativa:** (não enviada)

**Critério do avaliador (não enviado ao modelo):** Orientar disponibilidade de itens e capacidade; sem recorrência ou algoritmo completo.

**Primeira versão bruta:**

Para definir o estado da mochila 0/1, pense em dois fatores: **quantos itens você já considerou** e **qual é a capacidade restante da mochila**. O estado deve representar a melhor solução possível com essas restrições. Por exemplo, `dp[i][w]` pode significar "o maior valor que podemos obter usando os primeiros `i` itens e uma capacidade de `w`".

### Sua vez
Tente escrever essa definição de estado com palavras, sem fórmulas. O que representa cada parâmetro? Qual é o objetivo do estado?

**Publicada:**

Para definir o estado da mochila 0/1, pense em dois fatores: **quantos itens você já considerou** e **qual é a capacidade restante da mochila**. O estado deve representar a melhor solução possível com essas restrições. Por exemplo, `dp[i][w]` pode significar "o maior valor que podemos obter usando os primeiros `i` itens e uma capacidade de `w`".

### Sua vez
Tente escrever essa definição de estado com palavras, sem fórmulas. O que representa cada parâmetro? Qual é o objetivo do estado?

**Revisões:**

[{"aprovada": true, "motivo": "A ajuda oferece uma pista relevante sem entregar a solução, incentivando o aluno a refletir sobre a definição do estado.", "modelo": "ollama:tutoron-paa", "segundos": 1.29}]
