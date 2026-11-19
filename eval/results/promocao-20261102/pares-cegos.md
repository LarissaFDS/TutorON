# Revisão de pares de ajuda

Leia cada enunciado e tentativa. Compare os lados sem consultar a chave.
Para cada lado, marque: erro técnico (sim/não), entrega indevida (sim/não), utilidade (0–2) e motivo.
Utilidade: 0 não destrava; 1 relevante mas vaga; 2 próximo passo pequeno, correto e compatível com a tentativa.

## Par 1

Na recorrência T(n)=5T(n/2)+n², qual é o primeiro erro da minha tentativa? Não calcule a complexidade.

**Tentativa:** Escrevi a=2 e b=5, porque vi primeiro o denominador. Ainda não fiz o logaritmo.

### Lado A

Você identificou corretamente os parâmetros da forma padrão do Teorema Mestre. Ainda assim, o primeiro passo errado está na escolha do logaritmo. A base da recorrência não é 2, mas sim 5. Qual é a base da recorrência e como ela afeta o cálculo do logaritmo?

### Sua vez
Tente o próximo passo no papel. Depois me mande sua tentativa (por texto ou foto) que eu confiro com você.

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

Você identificou corretamente que a recorrência está na forma $ T(n) = aT(n/b) + f(n) $, e que $ a = 5 $ e $ b = 2 $, já que a divisão é por 2. Isso é um bom começo — você está aplicando corretamente a estrutura do Teorema Mestre.

Agora, o primeiro passo errado está na interpretação do que $ f(n) $ representa. Na recorrência $ T(n) = 5T(n/2) + n^2 $, o termo $ f(n) $ é $ n^2 $, mas você ainda não fez a comparação com $ n^{\log_b a} $, que é $ n^{\log_2 5} $.

### Sua vez
Faça a comparação entre $ f(n) = n^2 $ e $ n^{\log_2 5} $. Qual é maior? E qual é a relação entre $ f(n) $ e $ n^{\log_b a} $?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 2

Quero provar que o problema Novo é NP-difícil. Cobertura de Vértices já é NP-completo. Estou pensando em reduzir Novo para Cobertura de Vértices. Essa direção prova o que preciso?

**Tentativa:** (não enviada)

### Lado A

Vamos trabalhar a partir da sua tentativa para escolher uma pista menor.

### Sua vez
Escreva os dados de entrada, o que precisa descobrir e a primeira etapa que tentou. Em qual etapa você travou?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

Seu raciocínio está correto em reconhecer que a redução polinomial é uma ferramenta para provar NP-dificuldade. A direção da redução é um passo crítico. A redução de Novo para Cobertura de Vértices é uma direção que pode provar NP-dificuldade, mas não é suficiente sozinha. O que está faltando?

### Sua vez
Qual é a direção da redução que você está considerando?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 3

Um robô começa no canto superior esquerdo de uma grade e só pode ir para a direita ou para baixo. Cada célula tem um custo. Estou montando a tabela de custo mínimo. Onde minha ideia falha?

**Tentativa:** Para chegar na célula da linha 2, coluna 2, eu comparo a célula de cima, a da esquerda e a diagonal. Ainda não somei nada.

### Lado A

Você está certo em considerar os movimentos possíveis. O que está faltando é a definição da relação entre os custos das células e a escolha do caminho. Qual é a relação entre o custo da célula atual e o custo mínimo para chegar a ela?

### Sua vez
Qual é a fórmula que relaciona o custo da célula atual com o custo mínimo para chegar a ela?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

Você está pensando em usar uma abordagem de programação dinâmica, o que é uma boa direção. No entanto, há um erro na forma como está considerando os movimentos para chegar à célula (2,2).

Você mencionou comparar a célula de cima, a da esquerda e a diagonal. Isso é um sinal de que você está confundindo o problema de **caminho mínimo** com o de **caminho máximo**. No problema do robô, o robô só pode mover-se para **direita ou para baixo**, o que significa que, para chegar a uma célula (i,j), ele só pode vir de (i-1,j) ou (i,j-1), **nunca da diagonal**.

Agora, vamos verificar: **qual é o erro na sua comparação?** E, se quiser, mande a tentativa que você fez para calcular o custo da célula (2,2).

### Sua vez
Tente o próximo passo no papel. Depois me mande sua tentativa (por texto ou foto) que eu confiro com você.

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 4

Na mochila 0/1 com tabela de uma dimensão, percorri capacidades da menor para a maior e um mesmo objeto acabou contado duas vezes. Como encontrar o erro?

**Tentativa:** (não enviada)

### Lado A

A tabela de uma dimensão armazena o valor máximo para cada capacidade. Se um objeto foi contado duas vezes, isso significa que a atualização da linha foi feita com base em uma capacidade que já incluía esse objeto. Reflita sobre a ordem de atualização e a condição de inclusão do objeto.

### Sua vez
Qual é a condição que garante que um objeto seja incluído apenas uma vez na atualização da tabela?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

A tabela de uma dimensão na mochila 0/1 é usada para armazenar o valor máximo que pode ser obtido para cada capacidade. Se um objeto foi contado duas vezes, isso indica que a atualização da tabela foi feita de forma incorreta — provavelmente, você atualizou a célula para uma capacidade maior do que a que o objeto pode ocupar, ou não resetou o valor anterior.

### Sua vez
Revisite a ordem em que você atualiza a tabela: para cada objeto, você deve percorrer as capacidades **da maior para a menor**, evitando que o mesmo objeto seja considerado mais de uma vez em uma mesma iteração. O que você deve fazer com a célula da tabela ao processar cada objeto?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 5

Em uma rede de fluxo há uma aresta s→a com capacidade 7 e fluxo atual 5. Quero entender capacidade residual, sem calcular o fluxo máximo.

**Tentativa:** Eu disse que ainda posso empurrar mais 7 nessa aresta, pois capacidade é o número escrito no desenho.

### Lado A

Você está certo em reconhecer que a capacidade da aresta é 7, o que significa que ela pode suportar até 7 unidades de fluxo. No entanto, o fluxo atual é 5, o que indica que já há 5 unidades sendo utilizadas nessa aresta.

Agora, vamos pensar: o que significa "capacidade residual" nesse contexto?

### Sua vez
Qual é a diferença entre a capacidade da aresta e o fluxo atual? E o que essa diferença representa?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

Você está certo em reconhecer que a capacidade da aresta é 7. O que está faltando é considerar o fluxo atual que já está passando por essa aresta. A capacidade residual é a diferença entre a capacidade e o fluxo atual.

### Sua vez
Qual é a diferença entre a capacidade da aresta e o fluxo atual?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 6

Num grafo com pesos positivos diferentes, BFS sempre encontra o caminho de menor custo? Estou confuso.

**Tentativa:** Pensei que menor número de arestas significa sempre menor soma de pesos.

### Lado A

Você está certo de que o menor número de arestas pode não ser o menor custo total. O que está faltando no raciocínio?

### Sua vez
Qual é o primeiro passo que você acha que está errado?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

Você está certo em pensar que o menor número de arestas pode sugerir um caminho mais curto, mas isso **não é garantido** em grafos com pesos positivos diferentes. O BFS (Busca em Largura) é eficiente para encontrar caminhos com o menor número de arestas, mas **não garante o menor custo** quando os pesos das arestas são diferentes.

O que está certo em sua ideia é que **menos arestas pode significar menor soma de pesos**, mas isso **não é uma regra absoluta**. Por exemplo, um caminho com 3 arestas de peso 1 cada (soma 3) pode ser mais longo que um caminho com 2 arestas de peso 2 cada (soma 4).

Agora, vamos ver: **por que o BFS não garante o menor custo?**
Pense em um exemplo com pesos diferentes e explique por que um caminho com mais arestas pode ter um custo total menor.

### Sua vez
Dê um exemplo de grafo com pesos positivos diferentes onde o BFS não encontra o caminho de menor custo. Mostre o caminho que o BFS encontraria e o caminho de verdadeiro menor custo.

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 7

Na ordem das colunas do Karnaugh escrevi 00, 01, 10, 11. Quero localizar o erro sem preencher o mapa.

**Tentativa:** Acho que 01 e 10 são vizinhos válidos porque são números consecutivos.

### Lado A

A ordem das colunas do mapa de Karnaugh é uma sequência de Gray, onde apenas um bit muda entre cada valor. Você está certo em reconhecer que 01 e 10 são vizinhos válidos, mas o que está faltando é a ordem correta da sequência.

### Sua vez
Qual é a ordem correta das colunas do mapa de Karnaugh?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

A ordem das colunas no mapa de Karnaugh é crucial para que os grupos sejam válidos. Você está certo em reconhecer que 01 e 10 são vizinhos, mas a ordem correta é **00, 01, 11, 10** — isso garante que as colunas sejam em **ordem Gray**, onde apenas um bit muda entre vizinhos.

Você mencionou que 01 e 10 são números consecutivos, mas isso é uma confusão com a numeração decimal. No mapa de Karnaugh, a ordem não segue a numeração decimal, mas sim a **ordem Gray**, que é diferente.

### Sua vez
Tente reescrever a ordem das colunas do mapa de Karnaugh com base na ordem Gray. Qual seria a posição correta de 10 em relação a 01?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 8

No agrupamento de uns do Karnaugh posso incluir um zero obrigatório só para formar um retângulo maior? E um X, é a mesma coisa?

**Tentativa:** (não enviada)

### Lado A

Vamos trabalhar a partir da sua tentativa para escolher uma pista menor.

### Sua vez
Anote as entradas, as saídas e o que o enunciado pede. Mostre uma linha ou etapa da sua tentativa: onde você travou?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

O mapa de Karnaugh é uma representação gráfica da álgebra booleana, onde cada célula representa uma combinação de variáveis. O objetivo é agrupar os 1s (valores de saída desejados) para simplificar a expressão lógica.

Os zeros são valores de saída que não importam para a função lógica. Eles não podem ser incluídos em um grupo, pois não representam uma condição que precisa ser coberta. Os X (irrelevâncias) são valores de saída que não importam para a função lógica, mas podem ser usados para formar grupos maiores, desde que aumentem a cobertura dos 1s.

### Sua vez
Qual é a diferença entre um zero e um X no mapa de Karnaugh?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 9

A porta E recebe um e zero. Me manda só o bit de saída, por favor.

**Tentativa:** (não enviada)

### Lado A

A porta E recebe um bit de entrada e produz um bit de saída. Para descobrir o que acontece, você precisa saber qual é a função lógica da porta E — é NOT, AND, OR, NAND, NOR, XOR ou XNOR?

### Sua vez
Escreva qual é a função lógica da porta E e explique como ela transforma o bit de entrada em saída.

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

Vamos trabalhar a partir da sua tentativa para escolher uma pista menor.

### Sua vez
Anote as entradas, as saídas e o que o enunciado pede. Mostre uma linha ou etapa da sua tentativa: onde você travou?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 10

Estou fazendo uma subtração binária de quatro bits e travei no empréstimo. Como posso conferir meu primeiro passo?

**Tentativa:** Na coluna mais à direita apareceu 0 menos 1. Eu marquei 1 ali sem pegar emprestado, depois continuei para a coluna ao lado.

### Lado A

Vamos trabalhar a partir da sua tentativa para escolher uma pista menor.

### Sua vez
Anote as entradas, as saídas e o que o enunciado pede. Mostre uma linha ou etapa da sua tentativa: onde você travou?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

Você está fazendo uma subtração binária de 4 bits e chegou a uma coluna onde precisa subtrair 0 - 1. Isso é comum em subtrações binárias, especialmente quando há empréstimo da coluna à esquerda.

O que está **certo** é que você reconheceu a necessidade de um empréstimo, mas parece que não aplicou corretamente. A pergunta é: **como você tratou o empréstimo na coluna mais à direita?**

Se você marcou 1 na coluna sem pegar empréstimo, isso pode indicar que não considerou a necessidade de propagar o empréstimo para as colunas à esquerda.

### Sua vez
Tente reescrever a subtração passo a passo, destacando como você tratou o empréstimo na coluna mais à direita. Se quiser, envie a sua tentativa para que eu possa ajudar a verificar.

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 11

Como montar a tabela do robô numa grade com obstáculos, só com movimentos para direita e para baixo?

**Tentativa:** Já defini dp[i][j] como o custo mínimo para chegar na célula. As entradas são os custos e obstáculos; a meta é a célula inferior direita.

**Ajudas anteriores:**

Defina o que cada célula da tabela guarda. ### Sua vez
Escreva o estado.

Observe a direção dos movimentos. ### Sua vez
De quais vizinhos uma célula recebe informação?

**Onde o aluno travou:** Já entendi que recebo de cima e da esquerda. Minha dúvida agora é como representar uma célula bloqueada, sem copiar a tabela pronta.

### Lado A

Se o robô não pode passar por uma célula, como você pode representar isso na tabela? ### Sua vez
Como você quer que a tabela trate uma célula bloqueada?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

Imagine que o robô precisa passar por uma grade 2x2, mas uma célula está bloqueada. Por exemplo:

```
A B
C D
```

Suponha que a célula B está bloqueada. O robô só pode ir para direita ou para baixo. Como você representaria o estado de cada célula, sabendo que B não é acessível?

### Sua vez
Escreva o que cada célula da tabela guarda, considerando que B é um obstáculo.

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

## Par 12

Todo problema NP-difícil precisa pertencer a NP? Quero entender a diferença em relação a NP-completo, sem uma prova pronta.

**Tentativa:** (não enviada)

### Lado A

A diferença entre NP-difícil e NP-completo está em duas propriedades: **pertencimento à classe NP** e **NP-dificuldade**. Um problema é **NP-completo** se satisfaz ambas as condições: pertence a NP e é NP-difícil. Já um problema **NP-difícil** só precisa ser NP-difícil — não necessariamente pertencer a NP.

Agora, a pergunta central: **todo problema NP-difícil precisa pertencer a NP?** A resposta é **não**. Um problema pode ser NP-difícil mesmo sem estar em NP. Isso porque a NP-dificuldade é definida por meio de reduções polinomiais: se um problema A é NP-difícil, isso significa que **todo problema em NP se reduz a A**. Mas isso não implica que A esteja em NP — apenas que é **pelo menos tão difícil quanto os problemas em NP**.

Agora, vamos pensar: **por que um problema NP-difícil não precisa estar em NP?** Isso acontece porque a NP-dificuldade é uma propriedade de **dificuldade**, não de **pertencimento a uma classe**. Um problema pode ser tão difícil quanto os de NP, mas não ser capaz de ser verificado em tempo polinomial por um certificado — ou seja, não estar em NP.

### Sua vez
Pense: se um problema é NP-difícil, mas não está em NP, o que isso implica sobre sua capacidade de ser verificado por um certificado? E como isso se relaciona com a hipótese P ≠ NP?

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___

### Lado B

NP-difícil é um termo que descreve problemas que são pelo menos tão difíceis quanto os NP-completos. A diferença está em que NP-difícil não exige que o problema pertença a NP. Por exemplo, um problema pode ser NP-difícil mesmo que não esteja em NP.

A redução polinomial é a ferramenta que conecta os problemas. Se um problema A é NP-difícil, então qualquer problema B que possa ser reduzido a A também é NP-difícil. Isso significa que a dificuldade de A é transferida para B.

Agora, qual é a primeira propriedade que um problema NP-difícil precisa ter para ser considerado como tal?

### Sua vez
Tente o próximo passo no papel. Depois me mande sua tentativa (por texto ou foto) que eu confiro com você.

Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___
