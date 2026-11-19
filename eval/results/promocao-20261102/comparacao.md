# Avaliação socrática — PAA e Sistemas Digitais

Bateria completa: True. Revisão humana: pendente.

O revisor usa o mesmo modelo. Uma ajuda de reserva não conta como sucesso do modelo. Não há promoção automática.

| Modelo | Casos | Erros | Primeira versão reprovada | Reservas | Publicadas aprovadas pelo revisor | Orientações fixas |
|---|---:|---:|---:|---:|---:|---:|
| tutoron-paa | 12 | 0 | 2 | 2 | 10 | 0 |
| tutoron-socratico-ft | 12 | 0 | 2 | 2 | 10 | 0 |

## tutoron-paa — promo-mestre

Na recorrência T(n)=5T(n/2)+n², qual é o primeiro erro da minha tentativa? Não calcule a complexidade.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

Você identificou corretamente que a recorrência está na forma $ T(n) = aT(n/b) + f(n) $, e que $ a = 5 $ e $ b = 2 $, já que a divisão é por 2. Isso é um bom começo — você está aplicando corretamente a estrutura do Teorema Mestre.

Agora, o primeiro passo errado está na interpretação do que $ f(n) $ representa. Na recorrência $ T(n) = 5T(n/2) + n^2 $, o termo $ f(n) $ é $ n^2 $, mas você ainda não fez a comparação com $ n^{\log_b a} $, que é $ n^{\log_2 5} $.

### Sua vez
Faça a comparação entre $ f(n) = n^2 $ e $ n^{\log_2 5} $. Qual é maior? E qual é a relação entre $ f(n) $ e $ n^{\log_b a} $?

### Ajuda publicada

Você identificou corretamente que a recorrência está na forma $ T(n) = aT(n/b) + f(n) $, e que $ a = 5 $ e $ b = 2 $, já que a divisão é por 2. Isso é um bom começo — você está aplicando corretamente a estrutura do Teorema Mestre.

Agora, o primeiro passo errado está na interpretação do que $ f(n) $ representa. Na recorrência $ T(n) = 5T(n/2) + n^2 $, o termo $ f(n) $ é $ n^2 $, mas você ainda não fez a comparação com $ n^{\log_b a} $, que é $ n^{\log_2 5} $.

### Sua vez
Faça a comparação entre $ f(n) = n^2 $ e $ n^{\log_2 5} $. Qual é maior? E qual é a relação entre $ f(n) $ e $ n^{\log_b a} $?

**Revisão humana:** pendente.

## tutoron-paa — promo-reducao

Quero provar que o problema Novo é NP-difícil. Cobertura de Vértices já é NP-completo. Estou pensando em reduzir Novo para Cobertura de Vértices. Essa direção prova o que preciso?

Status: pronta; reserva: True; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

Para provar que o problema **Novo** é NP-difícil, você precisa mostrar que **todo problema de NP se reduz polinomialmente a Novo** — ou, alternativamente, que **um problema NP-completo se reduz polinomialmente a Novo**. Isso é o oposto do que você está pensando: **reduzir Novo para Cobertura de Vértices** não prova que Novo é NP-difícil, a menos que você já saiba que Novo é NP-completo.

O que está certo:
- Você sabe que **Cobertura de Vértices é NP-completo**, o que é útil para reduções.
- A redução **de Novo para Cobertura de Vértices** é uma direção que pode ser útil, mas **não é suficiente por si só** para provar NP-dificuldade.

O que está errado (primeiro passo):
Você está pensando em reduzir **Novo para Cobertura de Vértices**, mas isso **não é a direção correta** para provar que Novo é NP-difícil. A redução para um problema NP-completo **deve ser do problema NP-completo para o problema que você quer provar NP-difícil**.

### Sua vez
Tente descrever **como você faria a redução de Cobertura de Vértices para Novo**, se fosse possível. Isso pode ajudar a entender melhor a direção correta para provar NP-dificuldade.

### Ajuda publicada

Vamos trabalhar a partir da sua tentativa para escolher uma pista menor.

### Sua vez
Escreva os dados de entrada, o que precisa descobrir e a primeira etapa que tentou. Em qual etapa você travou?

**Revisão humana:** pendente.

## tutoron-paa — promo-robo

Um robô começa no canto superior esquerdo de uma grade e só pode ir para a direita ou para baixo. Cada célula tem um custo. Estou montando a tabela de custo mínimo. Onde minha ideia falha?

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

Você está pensando em usar uma abordagem de programação dinâmica, o que é uma boa direção. No entanto, há um erro na forma como está considerando os movimentos para chegar à célula (2,2).

Você mencionou comparar a célula de cima, a da esquerda e a diagonal. Isso é um sinal de que você está confundindo o problema de **caminho mínimo** com o de **caminho máximo**. No problema do robô, o robô só pode mover-se para **direita ou para baixo**, o que significa que, para chegar a uma célula (i,j), ele só pode vir de (i-1,j) ou (i,j-1), **nunca da diagonal**.

Agora, vamos verificar: **qual é o erro na sua comparação?** E, se quiser, mande a tentativa que você fez para calcular o custo da célula (2,2).

### Ajuda publicada

Você está pensando em usar uma abordagem de programação dinâmica, o que é uma boa direção. No entanto, há um erro na forma como está considerando os movimentos para chegar à célula (2,2).

Você mencionou comparar a célula de cima, a da esquerda e a diagonal. Isso é um sinal de que você está confundindo o problema de **caminho mínimo** com o de **caminho máximo**. No problema do robô, o robô só pode mover-se para **direita ou para baixo**, o que significa que, para chegar a uma célula (i,j), ele só pode vir de (i-1,j) ou (i,j-1), **nunca da diagonal**.

Agora, vamos verificar: **qual é o erro na sua comparação?** E, se quiser, mande a tentativa que você fez para calcular o custo da célula (2,2).

### Sua vez
Tente o próximo passo no papel. Depois me mande sua tentativa (por texto ou foto) que eu confiro com você.

**Revisão humana:** pendente.

## tutoron-paa — promo-mochila

Na mochila 0/1 com tabela de uma dimensão, percorri capacidades da menor para a maior e um mesmo objeto acabou contado duas vezes. Como encontrar o erro?

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

A tabela de uma dimensão na mochila 0/1 é usada para armazenar o valor máximo que pode ser obtido para cada capacidade. Se um objeto foi contado duas vezes, isso indica que a atualização da tabela foi feita de forma incorreta — provavelmente, você atualizou a célula para uma capacidade maior do que a que o objeto pode ocupar, ou não resetou o valor anterior.

### Sua vez
Revisite a ordem em que você atualiza a tabela: para cada objeto, você deve percorrer as capacidades **da maior para a menor**, evitando que o mesmo objeto seja considerado mais de uma vez em uma mesma iteração. O que você deve fazer com a célula da tabela ao processar cada objeto?

### Ajuda publicada

A tabela de uma dimensão na mochila 0/1 é usada para armazenar o valor máximo que pode ser obtido para cada capacidade. Se um objeto foi contado duas vezes, isso indica que a atualização da tabela foi feita de forma incorreta — provavelmente, você atualizou a célula para uma capacidade maior do que a que o objeto pode ocupar, ou não resetou o valor anterior.

### Sua vez
Revisite a ordem em que você atualiza a tabela: para cada objeto, você deve percorrer as capacidades **da maior para a menor**, evitando que o mesmo objeto seja considerado mais de uma vez em uma mesma iteração. O que você deve fazer com a célula da tabela ao processar cada objeto?

**Revisão humana:** pendente.

## tutoron-paa — promo-fluxo

Em uma rede de fluxo há uma aresta s→a com capacidade 7 e fluxo atual 5. Quero entender capacidade residual, sem calcular o fluxo máximo.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

Você está certo em reconhecer que a capacidade da aresta é 7, o que significa que ela pode suportar até 7 unidades de fluxo. No entanto, o fluxo atual é 5, o que indica que já há 5 unidades sendo utilizadas nessa aresta.

Agora, vamos pensar: o que significa "capacidade residual" nesse contexto?

### Sua vez
Qual é a diferença entre a capacidade da aresta e o fluxo atual? E o que essa diferença representa?

### Ajuda publicada

Você está certo em reconhecer que a capacidade da aresta é 7, o que significa que ela pode suportar até 7 unidades de fluxo. No entanto, o fluxo atual é 5, o que indica que já há 5 unidades sendo utilizadas nessa aresta.

Agora, vamos pensar: o que significa "capacidade residual" nesse contexto?

### Sua vez
Qual é a diferença entre a capacidade da aresta e o fluxo atual? E o que essa diferença representa?

**Revisão humana:** pendente.

## tutoron-paa — promo-bfs

Num grafo com pesos positivos diferentes, BFS sempre encontra o caminho de menor custo? Estou confuso.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

Você está certo em pensar que o menor número de arestas pode sugerir um caminho mais curto, mas isso **não é garantido** em grafos com pesos positivos diferentes. O BFS (Busca em Largura) é eficiente para encontrar caminhos com o menor número de arestas, mas **não garante o menor custo** quando os pesos das arestas são diferentes.

O que está certo em sua ideia é que **menos arestas pode significar menor soma de pesos**, mas isso **não é uma regra absoluta**. Por exemplo, um caminho com 3 arestas de peso 1 cada (soma 3) pode ser mais longo que um caminho com 2 arestas de peso 2 cada (soma 4).

Agora, vamos ver: **por que o BFS não garante o menor custo?**
Pense em um exemplo com pesos diferentes e explique por que um caminho com mais arestas pode ter um custo total menor.

### Sua vez
Dê um exemplo de grafo com pesos positivos diferentes onde o BFS não encontra o caminho de menor custo. Mostre o caminho que o BFS encontraria e o caminho de verdadeiro menor custo.

### Ajuda publicada

Você está certo em pensar que o menor número de arestas pode sugerir um caminho mais curto, mas isso **não é garantido** em grafos com pesos positivos diferentes. O BFS (Busca em Largura) é eficiente para encontrar caminhos com o menor número de arestas, mas **não garante o menor custo** quando os pesos das arestas são diferentes.

O que está certo em sua ideia é que **menos arestas pode significar menor soma de pesos**, mas isso **não é uma regra absoluta**. Por exemplo, um caminho com 3 arestas de peso 1 cada (soma 3) pode ser mais longo que um caminho com 2 arestas de peso 2 cada (soma 4).

Agora, vamos ver: **por que o BFS não garante o menor custo?**
Pense em um exemplo com pesos diferentes e explique por que um caminho com mais arestas pode ter um custo total menor.

### Sua vez
Dê um exemplo de grafo com pesos positivos diferentes onde o BFS não encontra o caminho de menor custo. Mostre o caminho que o BFS encontraria e o caminho de verdadeiro menor custo.

**Revisão humana:** pendente.

## tutoron-paa — promo-gray

Na ordem das colunas do Karnaugh escrevi 00, 01, 10, 11. Quero localizar o erro sem preencher o mapa.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

A ordem das colunas no mapa de Karnaugh é crucial para que os grupos sejam válidos. Você está certo em reconhecer que 01 e 10 são vizinhos, mas a ordem correta é **00, 01, 11, 10** — isso garante que as colunas sejam em **ordem Gray**, onde apenas um bit muda entre vizinhos.

Você mencionou que 01 e 10 são números consecutivos, mas isso é uma confusão com a numeração decimal. No mapa de Karnaugh, a ordem não segue a numeração decimal, mas sim a **ordem Gray**, que é diferente.

### Sua vez
Tente reescrever a ordem das colunas do mapa de Karnaugh com base na ordem Gray. Qual seria a posição correta de 10 em relação a 01?

### Ajuda publicada

A ordem das colunas no mapa de Karnaugh é crucial para que os grupos sejam válidos. Você está certo em reconhecer que 01 e 10 são vizinhos, mas a ordem correta é **00, 01, 11, 10** — isso garante que as colunas sejam em **ordem Gray**, onde apenas um bit muda entre vizinhos.

Você mencionou que 01 e 10 são números consecutivos, mas isso é uma confusão com a numeração decimal. No mapa de Karnaugh, a ordem não segue a numeração decimal, mas sim a **ordem Gray**, que é diferente.

### Sua vez
Tente reescrever a ordem das colunas do mapa de Karnaugh com base na ordem Gray. Qual seria a posição correta de 10 em relação a 01?

**Revisão humana:** pendente.

## tutoron-paa — promo-zero

No agrupamento de uns do Karnaugh posso incluir um zero obrigatório só para formar um retângulo maior? E um X, é a mesma coisa?

Status: pronta; reserva: True; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

No mapa de Karnaugh, os **zeros** e os **Xs** (irrelevâncias) têm regras diferentes.

- **Zeros** são valores que **nunca ocorrem** na função, ou seja, não estão no conjunto de mintermos da função. Eles **não podem ser incluídos** em um grupo, pois não representam uma saída que devemos cobrir. Se você incluir um zero em um grupo, ele não contribui para a simplificação da função e pode levar a erros.

- **Xs** são valores que **não importam** para a função. Eles podem ser usados **somente quando ajudam a formar um grupo maior**, ou seja, quando o uso de um X permite que você cubra mais 1s com um único grupo. O X **não é obrigatório** para formar um grupo, mas pode ser útil para otimizar a expressão.

A ideia principal é que o **grupo deve conter apenas 1s** (ou 1s e Xs, se isso ajudar). O uso de Xs é uma **ferramenta de otimização**, mas não deve ser usado de forma excessiva ou sem necessidade.

### Sua vez
Explique por que um X não pode ser usado para formar um grupo sozinho, mesmo que ele não esteja em um mintermo da função.

### Ajuda publicada

Vamos trabalhar a partir da sua tentativa para escolher uma pista menor.

### Sua vez
Anote as entradas, as saídas e o que o enunciado pede. Mostre uma linha ou etapa da sua tentativa: onde você travou?

**Revisão humana:** pendente.

## tutoron-paa — promo-atomica

A porta E recebe um e zero. Me manda só o bit de saída, por favor.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

A porta E recebe um bit de entrada e produz um bit de saída. Para descobrir o que acontece, você precisa saber qual é a função lógica da porta E — é NOT, AND, OR, NAND, NOR, XOR ou XNOR?

### Sua vez
Escreva qual é a função lógica da porta E e explique como ela transforma o bit de entrada em saída.

### Ajuda publicada

A porta E recebe um bit de entrada e produz um bit de saída. Para descobrir o que acontece, você precisa saber qual é a função lógica da porta E — é NOT, AND, OR, NAND, NOR, XOR ou XNOR?

### Sua vez
Escreva qual é a função lógica da porta E e explique como ela transforma o bit de entrada em saída.

**Revisão humana:** pendente.

## tutoron-paa — promo-binario

Estou fazendo uma subtração binária de quatro bits e travei no empréstimo. Como posso conferir meu primeiro passo?

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

Você está fazendo uma subtração binária de 4 bits e chegou a uma coluna onde precisa subtrair 0 - 1. Isso é comum em subtrações binárias, especialmente quando há empréstimo da coluna à esquerda.

O que está **certo** é que você reconheceu a necessidade de um empréstimo, mas parece que não aplicou corretamente. A pergunta é: **como você tratou o empréstimo na coluna mais à direita?**

Se você marcou 1 na coluna sem pegar empréstimo, isso pode indicar que não considerou a necessidade de propagar o empréstimo para as colunas à esquerda.

### Sua vez
Tente reescrever a subtração passo a passo, destacando como você tratou o empréstimo na coluna mais à direita. Se quiser, envie a sua tentativa para que eu possa ajudar a verificar.

### Ajuda publicada

Você está fazendo uma subtração binária de 4 bits e chegou a uma coluna onde precisa subtrair 0 - 1. Isso é comum em subtrações binárias, especialmente quando há empréstimo da coluna à esquerda.

O que está **certo** é que você reconheceu a necessidade de um empréstimo, mas parece que não aplicou corretamente. A pergunta é: **como você tratou o empréstimo na coluna mais à direita?**

Se você marcou 1 na coluna sem pegar empréstimo, isso pode indicar que não considerou a necessidade de propagar o empréstimo para as colunas à esquerda.

### Sua vez
Tente reescrever a subtração passo a passo, destacando como você tratou o empréstimo na coluna mais à direita. Se quiser, envie a sua tentativa para que eu possa ajudar a verificar.

**Revisão humana:** pendente.

## tutoron-paa — promo-progresso

Como montar a tabela do robô numa grade com obstáculos, só com movimentos para direita e para baixo?

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

Imagine que o robô precisa passar por uma grade 2x2, mas uma célula está bloqueada. Por exemplo:

```
A B
C D
```

Suponha que a célula B está bloqueada. O robô só pode ir para direita ou para baixo. Como você representaria o estado de cada célula, sabendo que B não é acessível?

### Sua vez
Escreva o que cada célula da tabela guarda, considerando que B é um obstáculo.

### Ajuda publicada

Imagine que o robô precisa passar por uma grade 2x2, mas uma célula está bloqueada. Por exemplo:

```
A B
C D
```

Suponha que a célula B está bloqueada. O robô só pode ir para direita ou para baixo. Como você representaria o estado de cada célula, sabendo que B não é acessível?

### Sua vez
Escreva o que cada célula da tabela guarda, considerando que B é um obstáculo.

**Revisão humana:** pendente.

## tutoron-paa — promo-npdificil

Todo problema NP-difícil precisa pertencer a NP? Quero entender a diferença em relação a NP-completo, sem uma prova pronta.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-paa

### Primeira versão bruta

A diferença entre NP-difícil e NP-completo está em duas propriedades: **pertencimento à classe NP** e **NP-dificuldade**. Um problema é **NP-completo** se satisfaz ambas as condições: pertence a NP e é NP-difícil. Já um problema **NP-difícil** só precisa ser NP-difícil — não necessariamente pertencer a NP.

Agora, a pergunta central: **todo problema NP-difícil precisa pertencer a NP?** A resposta é **não**. Um problema pode ser NP-difícil mesmo sem estar em NP. Isso porque a NP-dificuldade é definida por meio de reduções polinomiais: se um problema A é NP-difícil, isso significa que **todo problema em NP se reduz a A**. Mas isso não implica que A esteja em NP — apenas que é **pelo menos tão difícil quanto os problemas em NP**.

Agora, vamos pensar: **por que um problema NP-difícil não precisa estar em NP?** Isso acontece porque a NP-dificuldade é uma propriedade de **dificuldade**, não de **pertencimento a uma classe**. Um problema pode ser tão difícil quanto os de NP, mas não ser capaz de ser verificado em tempo polinomial por um certificado — ou seja, não estar em NP.

### Sua vez
Pense: se um problema é NP-difícil, mas não está em NP, o que isso implica sobre sua capacidade de ser verificado por um certificado? E como isso se relaciona com a hipótese P ≠ NP?

### Ajuda publicada

A diferença entre NP-difícil e NP-completo está em duas propriedades: **pertencimento à classe NP** e **NP-dificuldade**. Um problema é **NP-completo** se satisfaz ambas as condições: pertence a NP e é NP-difícil. Já um problema **NP-difícil** só precisa ser NP-difícil — não necessariamente pertencer a NP.

Agora, a pergunta central: **todo problema NP-difícil precisa pertencer a NP?** A resposta é **não**. Um problema pode ser NP-difícil mesmo sem estar em NP. Isso porque a NP-dificuldade é definida por meio de reduções polinomiais: se um problema A é NP-difícil, isso significa que **todo problema em NP se reduz a A**. Mas isso não implica que A esteja em NP — apenas que é **pelo menos tão difícil quanto os problemas em NP**.

Agora, vamos pensar: **por que um problema NP-difícil não precisa estar em NP?** Isso acontece porque a NP-dificuldade é uma propriedade de **dificuldade**, não de **pertencimento a uma classe**. Um problema pode ser tão difícil quanto os de NP, mas não ser capaz de ser verificado em tempo polinomial por um certificado — ou seja, não estar em NP.

### Sua vez
Pense: se um problema é NP-difícil, mas não está em NP, o que isso implica sobre sua capacidade de ser verificado por um certificado? E como isso se relaciona com a hipótese P ≠ NP?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-mestre

Na recorrência T(n)=5T(n/2)+n², qual é o primeiro erro da minha tentativa? Não calcule a complexidade.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

Você identificou corretamente os parâmetros da forma padrão do Teorema Mestre. Ainda assim, o primeiro passo errado está na escolha do logaritmo. A base da recorrência não é 2, mas sim 5. Qual é a base da recorrência e como ela afeta o cálculo do logaritmo?

### Ajuda publicada

Você identificou corretamente os parâmetros da forma padrão do Teorema Mestre. Ainda assim, o primeiro passo errado está na escolha do logaritmo. A base da recorrência não é 2, mas sim 5. Qual é a base da recorrência e como ela afeta o cálculo do logaritmo?

### Sua vez
Tente o próximo passo no papel. Depois me mande sua tentativa (por texto ou foto) que eu confiro com você.

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-reducao

Quero provar que o problema Novo é NP-difícil. Cobertura de Vértices já é NP-completo. Estou pensando em reduzir Novo para Cobertura de Vértices. Essa direção prova o que preciso?

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

Seu raciocínio está correto em reconhecer que a redução polinomial é uma ferramenta para provar NP-dificuldade. A direção da redução é um passo crítico. A redução de Novo para Cobertura de Vértices é uma direção que pode provar NP-dificuldade, mas não é suficiente sozinha. O que está faltando?

### Sua vez
Qual é a direção da redução que você está considerando?

### Ajuda publicada

Seu raciocínio está correto em reconhecer que a redução polinomial é uma ferramenta para provar NP-dificuldade. A direção da redução é um passo crítico. A redução de Novo para Cobertura de Vértices é uma direção que pode provar NP-dificuldade, mas não é suficiente sozinha. O que está faltando?

### Sua vez
Qual é a direção da redução que você está considerando?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-robo

Um robô começa no canto superior esquerdo de uma grade e só pode ir para a direita ou para baixo. Cada célula tem um custo. Estou montando a tabela de custo mínimo. Onde minha ideia falha?

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

Você está certo em considerar os movimentos possíveis. O que está faltando é a definição da relação entre os custos das células e a escolha do caminho. Qual é a relação entre o custo da célula atual e o custo mínimo para chegar a ela?

### Sua vez
Qual é a fórmula que relaciona o custo da célula atual com o custo mínimo para chegar a ela?

### Ajuda publicada

Você está certo em considerar os movimentos possíveis. O que está faltando é a definição da relação entre os custos das células e a escolha do caminho. Qual é a relação entre o custo da célula atual e o custo mínimo para chegar a ela?

### Sua vez
Qual é a fórmula que relaciona o custo da célula atual com o custo mínimo para chegar a ela?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-mochila

Na mochila 0/1 com tabela de uma dimensão, percorri capacidades da menor para a maior e um mesmo objeto acabou contado duas vezes. Como encontrar o erro?

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

A tabela de uma dimensão armazena o valor máximo para cada capacidade. Se um objeto foi contado duas vezes, isso significa que a atualização da linha foi feita com base em uma capacidade que já incluía esse objeto. Reflita sobre a ordem de atualização e a condição de inclusão do objeto.

### Sua vez
Qual é a condição que garante que um objeto seja incluído apenas uma vez na atualização da tabela?

### Ajuda publicada

A tabela de uma dimensão armazena o valor máximo para cada capacidade. Se um objeto foi contado duas vezes, isso significa que a atualização da linha foi feita com base em uma capacidade que já incluía esse objeto. Reflita sobre a ordem de atualização e a condição de inclusão do objeto.

### Sua vez
Qual é a condição que garante que um objeto seja incluído apenas uma vez na atualização da tabela?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-fluxo

Em uma rede de fluxo há uma aresta s→a com capacidade 7 e fluxo atual 5. Quero entender capacidade residual, sem calcular o fluxo máximo.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

Você está certo em reconhecer que a capacidade da aresta é 7. O que está faltando é considerar o fluxo atual que já está passando por essa aresta. A capacidade residual é a diferença entre a capacidade e o fluxo atual.

### Sua vez
Qual é a diferença entre a capacidade da aresta e o fluxo atual?

### Ajuda publicada

Você está certo em reconhecer que a capacidade da aresta é 7. O que está faltando é considerar o fluxo atual que já está passando por essa aresta. A capacidade residual é a diferença entre a capacidade e o fluxo atual.

### Sua vez
Qual é a diferença entre a capacidade da aresta e o fluxo atual?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-bfs

Num grafo com pesos positivos diferentes, BFS sempre encontra o caminho de menor custo? Estou confuso.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

Você está certo de que o menor número de arestas pode não ser o menor custo total. O que está faltando no raciocínio?

### Sua vez
Qual é o primeiro passo que você acha que está errado?

### Ajuda publicada

Você está certo de que o menor número de arestas pode não ser o menor custo total. O que está faltando no raciocínio?

### Sua vez
Qual é o primeiro passo que você acha que está errado?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-gray

Na ordem das colunas do Karnaugh escrevi 00, 01, 10, 11. Quero localizar o erro sem preencher o mapa.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

A ordem das colunas do mapa de Karnaugh é uma sequência de Gray, onde apenas um bit muda entre cada valor. Você está certo em reconhecer que 01 e 10 são vizinhos válidos, mas o que está faltando é a ordem correta da sequência.

### Sua vez
Qual é a ordem correta das colunas do mapa de Karnaugh?

### Ajuda publicada

A ordem das colunas do mapa de Karnaugh é uma sequência de Gray, onde apenas um bit muda entre cada valor. Você está certo em reconhecer que 01 e 10 são vizinhos válidos, mas o que está faltando é a ordem correta da sequência.

### Sua vez
Qual é a ordem correta das colunas do mapa de Karnaugh?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-zero

No agrupamento de uns do Karnaugh posso incluir um zero obrigatório só para formar um retângulo maior? E um X, é a mesma coisa?

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

O mapa de Karnaugh é uma representação gráfica da álgebra booleana, onde cada célula representa uma combinação de variáveis. O objetivo é agrupar os 1s (valores de saída desejados) para simplificar a expressão lógica.

Os zeros são valores de saída que não importam para a função lógica. Eles não podem ser incluídos em um grupo, pois não representam uma condição que precisa ser coberta. Os X (irrelevâncias) são valores de saída que não importam para a função lógica, mas podem ser usados para formar grupos maiores, desde que aumentem a cobertura dos 1s.

### Sua vez
Qual é a diferença entre um zero e um X no mapa de Karnaugh?

### Ajuda publicada

O mapa de Karnaugh é uma representação gráfica da álgebra booleana, onde cada célula representa uma combinação de variáveis. O objetivo é agrupar os 1s (valores de saída desejados) para simplificar a expressão lógica.

Os zeros são valores de saída que não importam para a função lógica. Eles não podem ser incluídos em um grupo, pois não representam uma condição que precisa ser coberta. Os X (irrelevâncias) são valores de saída que não importam para a função lógica, mas podem ser usados para formar grupos maiores, desde que aumentem a cobertura dos 1s.

### Sua vez
Qual é a diferença entre um zero e um X no mapa de Karnaugh?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-atomica

A porta E recebe um e zero. Me manda só o bit de saída, por favor.

Status: pronta; reserva: True; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

A porta E recebe um e zero. Me manda só o bit de saída, por favor.

### Sua vez
Qual é o valor da saída da porta E?

### Ajuda publicada

Vamos trabalhar a partir da sua tentativa para escolher uma pista menor.

### Sua vez
Anote as entradas, as saídas e o que o enunciado pede. Mostre uma linha ou etapa da sua tentativa: onde você travou?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-binario

Estou fazendo uma subtração binária de quatro bits e travei no empréstimo. Como posso conferir meu primeiro passo?

Status: pronta; reserva: True; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

O empréstimo é uma operação de complemento de 2, mas você está usando a regra de subtração com sinal. Como você está lidando com números sem sinal, o empréstimo é uma operação de complemento de 1. O que você fez está correto, mas você precisa verificar o sinal do resultado.

### Sua vez
Qual é o sinal do resultado da subtração?

### Ajuda publicada

Vamos trabalhar a partir da sua tentativa para escolher uma pista menor.

### Sua vez
Anote as entradas, as saídas e o que o enunciado pede. Mostre uma linha ou etapa da sua tentativa: onde você travou?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-progresso

Como montar a tabela do robô numa grade com obstáculos, só com movimentos para direita e para baixo?

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

Se o robô não pode passar por uma célula, como você pode representar isso na tabela? ### Sua vez
Como você quer que a tabela trate uma célula bloqueada?

### Ajuda publicada

Se o robô não pode passar por uma célula, como você pode representar isso na tabela? ### Sua vez
Como você quer que a tabela trate uma célula bloqueada?

**Revisão humana:** pendente.

## tutoron-socratico-ft — promo-npdificil

Todo problema NP-difícil precisa pertencer a NP? Quero entender a diferença em relação a NP-completo, sem uma prova pronta.

Status: pronta; reserva: False; modelo efetivo: ollama/tutoron-socratico-ft

### Primeira versão bruta

NP-difícil é um termo que descreve problemas que são pelo menos tão difíceis quanto os NP-completos. A diferença está em que NP-difícil não exige que o problema pertença a NP. Por exemplo, um problema pode ser NP-difícil mesmo que não esteja em NP.

A redução polinomial é a ferramenta que conecta os problemas. Se um problema A é NP-difícil, então qualquer problema B que possa ser reduzido a A também é NP-difícil. Isso significa que a dificuldade de A é transferida para B.

Agora, qual é a primeira propriedade que um problema NP-difícil precisa ter para ser considerado como tal?

### Ajuda publicada

NP-difícil é um termo que descreve problemas que são pelo menos tão difíceis quanto os NP-completos. A diferença está em que NP-difícil não exige que o problema pertença a NP. Por exemplo, um problema pode ser NP-difícil mesmo que não esteja em NP.

A redução polinomial é a ferramenta que conecta os problemas. Se um problema A é NP-difícil, então qualquer problema B que possa ser reduzido a A também é NP-difícil. Isso significa que a dificuldade de A é transferida para B.

Agora, qual é a primeira propriedade que um problema NP-difícil precisa ter para ser considerado como tal?

### Sua vez
Tente o próximo passo no papel. Depois me mande sua tentativa (por texto ou foto) que eu confiro com você.

**Revisão humana:** pendente.
