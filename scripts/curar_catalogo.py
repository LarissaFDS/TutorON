"""Correções editoriais explícitas. Não executa código extraído dos documentos."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from acervo.common import ROOT, read_json, write_json, caminho_guardado

# Texto novo, derivado da análise da fonte; nunca apresentado como transcrição.
CORRECTIONS = {
 '97254bb4a1b8-q1-1': ('Reconstruir código da imagem; memória em palavras e overflow.', '''Número faltante entre 1 e n, ouvindo n-1 inteiros distintos válidos.
Inicialize faltante=n(n+1)/2 e subtraia cada número ouvido. Ao final, resta exatamente o omitido. São O(n) operações e O(1) palavras de memória no modelo RAM; representar os acumuladores exige O(log n) bits. Valide as hipóteses de intervalo e distinção se a entrada não for garantida.
Em tipos inteiros de tamanho fixo, a multiplicação n(n+1) pode transbordar mesmo quando a soma final cabe: divida um dos fatores pares por 2 antes de multiplicar e use um tipo suficientemente largo. Uma alternativa é XOR de 1..n combinado com XOR dos números recebidos; todos os presentes cancelam, deixando o faltante. XOR evita a soma intermediária, mas ainda exige um tipo capaz de representar n.'''),
 'd455baef2cdf-q1-1': ('Reconstruir panquecas e distinguir inversões do custo de movimentação.', '''Ordenação da pilha de panquecas distintas com a maior na base.
Para o prefixo ativo de tamanho m, de n até 2, localize sua maior panqueca na posição p. Se já estiver na base m, não faça nada. Caso contrário, se p não for o topo, inverta o prefixo p para trazê-la ao topo; depois inverta o prefixo m para levá-la à base. Continue com m-1. Por indução, o sufixo já fixado contém as maiores panquecas nas posições corretas e não é tocado novamente.
Há no máximo 2(n-1) inversões de prefixo, portanto O(n) inversões. Essa contagem não é o tempo total: localizar a maior e movimentar um prefixo custam O(m), dando O(n^2) de tempo e O(1) de espaço auxiliar com inversão in-place. O código OCR usa limites duvidosos; esta é uma reconstrução derivada.'''),
 '7b4da6a8adf7-q2-2': ('Corrigir direção da implicação indutiva e tornar fórmulas legíveis.', '''Provas das somas por indução, para n>=1.
S1(n)=n(n+1)/2; S2(n)=n(n+1)(2n+1)/6; S3(n)=n^2(n+1)^2/4, onde Sr(n)=sum(i^r,i=1..n).
Caso base n=1: todas as fórmulas dão 1. Hipótese: a fórmula vale em k. Para provar k+1, some o próximo termo, e não suponha antecipadamente o resultado:
S1(k+1)=k(k+1)/2+(k+1)=(k+1)(k+2)/2.
S2(k+1)=k(k+1)(2k+1)/6+(k+1)^2=(k+1)(k+2)(2k+3)/6.
S3(k+1)=k^2(k+1)^2/4+(k+1)^3=(k+1)^2(k+2)^2/4.
Assim P(k) implica P(k+1). A frase inversa na resolução original não é o passo necessário da indução.'''),
 '7b4da6a8adf7-q3-3': ('Corrigir a hipótese circular da prova direta e o rótulo do caso base.', '''Três provas de divisibilidade.
(a) Para n>=0, 3 divide n^3+2n. Base n=0: o resultado é 0. Se 3 divide k^3+2k, então (k+1)^3+2(k+1)=(k^3+2k)+3(k^2+k+1), soma de dois múltiplos de 3. Portanto a propriedade vale em k+1.
(b) Contrapositiva: se m é ímpar, escreva m=2r+1. Então 3m=6r+3=2(3r+1)+1 também é ímpar. Logo, se 2 divide 3m, 2 divide m.
(c) Para qualquer inteiro a, a+(a+1)+(a+2)=3(a+1), logo a soma de três consecutivos é múltipla de 3. A hipótese é a ser inteiro, não a conclusão de divisibilidade.'''),
 '7b4da6a8adf7-q6-6': ('Distinguir o invariante antes e depois de cada iteração de Horner.', '''Corretude de Horner para P(x)=sum(A[j]x^j,j=0..n).
Inicialize p=A[n]. Para i=n-1,n-2,...,0, faça p=p*x+A[i]. Antes da iteração i, o invariante é p=sum(A[j]x^(j-i-1),j=i+1..n). Vale inicialmente para i=n-1, pois p=A[n]. Após o corpo, p=sum(A[j]x^(j-i),j=i..n), que é o invariante antes da próxima iteração i-1. Ao terminar i=0, p=P(x).
O número de multiplicações e adições é n, portanto O(n) operações aritméticas e O(1) memória auxiliar. Isso não limita o custo em bits para coeficientes inteiros arbitrariamente grandes. A formulação considera aritmética exata; erros de ponto flutuante são outra questão.'''),
 '7b4da6a8adf7-q7-7': ('O OCR troca divisão inteira por adição na atualização de t.', '''Conversor decimal-binário de n inteiro não negativo.
Faça t=n e k=0. Enquanto t>0, guarde b[k]=t mod 2, atualize t=floor(t/2) e incremente k. Os bits são armazenados do menos significativo para o mais significativo; inverta a ordem para exibir. Para n=0, exiba 0.
Invariante após k iterações: n=sum(b[j]2^j,j=0..k-1)+t*2^k. A divisão euclidiana t=2*floor(t/2)+(t mod 2) preserva a igualdade ao acrescentar um bit. Como t diminui estritamente quando positivo, termina; em t=0 os bits representam n.
A linha extraída como t=t+2 está errada: a fonte usa divisão inteira. São O(log(n+1)) iterações; armazenar a saída exige O(log(n+1)) bits.'''),
 'ef6d051e4b8c-q1-1': ('Corrigir enumerações de escada, com casos base explícitos.', '''Subir n degraus em passos de tamanho 1 ou 2.
Defina E(0)=1 (sequência vazia) e E(1)=1. Para n>=2, E(n)=E(n-1)+E(n-2), separando pelo último passo. Logo os valores para n=0..5 são 1,1,2,3,5,8.
Para n=4, as cinco sequências são 1111,112,121,211,22. Para n=5, as oito são 11111,1112,1121,1211,2111,122,212,221. A sequência 221 não pode representar quatro degraus, e não deve ser duplicada na lista de cinco.
É possível calcular em O(n) adições e O(1) palavras auxiliares com duas variáveis. A contagem pode exigir inteiros grandes; a complexidade em bits deve considerar seu crescimento.'''),
 'ef6d051e4b8c-q6-6': ('Índices corretos do algoritmo de dois ponteiros.', '''Encontrar dois elementos distintos de S cuja soma é x em tempo Theta(n log n).
Ordene S com um algoritmo de pior caso Theta(n log n), como merge sort. Use i=0 e j=n-1. Enquanto i<j, compare S[i]+S[j] com x. Se igual, encontrou o par; se menor, incremente i; se maior, decremente j. Quando i>=j sem igualdade, não há par.
Se a soma é pequena, nenhum parceiro na posição atual de i com índice <=j a torna maior que S[i]+S[j]; descartar i é seguro. O argumento dual vale para descartar j quando a soma é grande. A varredura é O(n), dominada pela ordenação. i<j impede reutilizar o mesmo elemento. A memória depende da ordenação; merge sort usual requer O(n).'''),
 'ef6d051e4b8c-q8-8': ('Corrigir a direção da indução no limite da contagem de OI.', '''Contagem da palavra OI em Prog1(n), n>=1.
T(1)=1; para n>1, T(n)=n+T(n-1). A solução exata é n(n+1)/2.
Indução do limite T(n)<=n^2: base T(1)=1. Suponha T(k)<=k^2 para k>=1. Então T(k+1)=k+1+T(k)<=k^2+k+1<=(k+1)^2, pois a diferença é k>=1. Isso prova P(k)->P(k+1); não se deve inverter a implicação. Portanto o limite vale para todo n>=1.'''),
 'c01': ('Índices inteiros e domínio do algoritmo.', '''Explique o que o Algoritmo X faz e prove sua corretude.
O domínio é um intervalo não vazio A[inicio..fim], com índices inteiros. Interprete a divisão do índice como piso: meio = inicio + floor((fim-inicio)/2). Se inicio=fim, retorne A[inicio]. Caso contrário, calcule a=X(A,inicio,meio), b=X(A,meio+1,fim) e retorne max(a,b). Esta versão retorna o máximo, não a soma. Sem o piso, a notação do enunciado pode produzir índices não inteiros; a interpretação foi explicitada nesta versão derivada.'''),
 'c02': ('Corrigir a variável da hipótese de indução e os limites dos subvetores.', '''Prova de corretude do Algoritmo X que retorna o maior elemento.
Teorema: para qualquer intervalo não vazio A[inicio..fim] de tamanho m=fim-inicio+1, X retorna seu máximo.
Caso base: m=1 implica inicio=fim; o retorno A[inicio] é o único elemento.
Hipótese de indução forte: para todo tamanho k com 1<=k<m, X devolve o máximo de qualquer intervalo desse tamanho.
Passo indutivo: para m>1, meio=inicio+floor((fim-inicio)/2). Os intervalos A[inicio..meio] e A[meio+1..fim] são não vazios, disjuntos, cobrem o intervalo original e têm tamanhos menores que m. Pela hipótese, as chamadas retornam os máximos a e b. Compará-los e retornar o maior produz o máximo do intervalo inteiro. Os tamanhos diminuem, provando também a terminação.
São m-1 comparações de combinação e tempo Theta(m); a pilha tem profundidade O(log m). Esta é uma correção editorial da prova transcrita, sem atribuir ao professor a nova redação.'''),
 'c05': ('Acrescentar a recorrência exigida e distinguir contagem de tempo.', '''Quantos asteriscos ASTERISCO(n) imprime?
Para n inteiro não negativo: A(0)=0. Para n>=1, duas chamadas imprimem A(n-1) cada e o laço imprime n, logo A(n)=2A(n-1)+n.
A solução é A(n)=2^(n+1)-n-2. A substituição na recorrência e o caso base comprovam a fórmula. Valores: A(1)=1, A(2)=4, A(3)=11, A(4)=26. Portanto a contagem é Theta(2^n). A contagem de asteriscos não é o número de chamadas; há 2^(n+1)-1 chamadas, incluindo n=0. A variante com uma chamada em floor(n/2) tem outra recorrência e não usa esta fórmula.'''),
 'c06': ('Eliminar referência a uma equação inexistente e fechar a soma.', '''Método da iteração: T(n)=T(n-1)+n, T(1)=1.
Iterando k vezes, T(n)=T(n-k)+sum(j,n-k+1,n). Para k=n-1 resulta T(n)=1+2+...+n=n(n+1)/2. Assim T(n)=Theta(n^2), e em particular O(n^2). Para n>=1, T(n)<=n^2. Não há necessidade de uma quarta equação não apresentada na transcrição.'''),
 'c08': ('Usar o tamanho exato da entrada binária e analisar o pior caso.', '''Por que o algoritmo força bruta de COMPOSTO não demonstra que o problema está em P?
Para n>=2, a representação binária tem b=floor(log2(n))+1 bits. Portanto 2^(b-1)<=n<2^b; não se deve escrever b=log2(n) como igualdade exata para todo inteiro.
Testar sucessivamente os divisores de 2 até floor(n/2) pode exigir Theta(n) testes no pior caso, por exemplo em entradas primas. A divisão também tem custo em bits, polinomial em b. O número de testes já cresce exponencialmente em b, apesar de ser polinomial no valor numérico n: daí a descrição pseudo-polinomial.
Isso classifica este algoritmo, não prova que COMPOSTO esteja fora de P nem que seja NP-completo. Encontrar um divisor é um certificado de composição verificável em tempo polinomial em b.'''),
 'c09': ('Substituir a definição incorreta de NP e explicitar redução e decisão.', '''Defina P, NP, NP-completo e redução polinomial.
P é a classe dos problemas de decisão resolvidos por algoritmo determinístico em tempo polinomial no comprimento da entrada.
NP é a classe dos problemas de decisão cujas instâncias SIM possuem certificados de tamanho polinomial verificáveis em tempo polinomial. Equivalentemente, são decididos em tempo polinomial por máquina não determinística. NP não é definida como problemas que ninguém conseguiu provar polinomiais ou intratáveis. P está contida em NP; não se sabe se P=NP.
Uma redução many-one A<=p B é uma função f computável em tempo polinomial tal que x pertence a A se e somente se f(x) pertence a B.
B é NP-completo se B pertence a NP e todo problema de NP se reduz polinomialmente a B. Para demonstrar NP-dificuldade, reduza um problema já NP-difícil para o problema novo. A direção contrária não basta.
Exemplos apropriados de decisão: SAT, CLIQUE (existe clique de tamanho pelo menos k?) e MOCHILA com limite de peso e alvo de valor. Distinguir essas versões das versões de otimização. Se algum NP-completo estiver em P, então P=NP. Esta redação corrige a resolução de alunos.'''),
 'a177bf5bc3c7-q1-1': ('Uma AGM aumenta n-1 unidades; preservar o contraexemplo da fonte.', '''Ao somar 1 ao peso de cada aresta, a árvore geradora mínima continua mínima? E os caminhos mínimos?
Em um grafo conexo com n vértices, toda árvore geradora tem exatamente n-1 arestas. Logo w'(T)=w(T)+(n-1) para toda árvore T. A ordem dos custos e o conjunto de árvores mínimas permanecem iguais. A afirmação da resolução original de que o aumento seria uma unidade está errada.
Para caminhos, w'(P)=w(P)+|E(P)|, e diferentes caminhos podem usar quantidades diferentes de arestas. Contraexemplo da fonte: s-x, x-y, y-t têm custo 0; s-t tem custo 1. Antes, o caminho de três arestas custa 0 e é melhor. Depois, custa 3, enquanto s-t custa 2; o caminho mínimo muda.'''),
 'a177bf5bc3c7-q2-2': ('Corrigir o argumento de troca e exigir pesos distintos.', '''Prove a unicidade da árvore geradora mínima quando os pesos das arestas são distintos.
Assuma duas AGMs diferentes T e U. Seja e a aresta de menor peso na diferença simétrica T xor U; troque seus nomes se necessário para que e esteja em T. Inserir e em U cria um ciclo. Esse ciclo contém uma aresta f de U que não está em T, pois T não contém ciclos. Como os pesos são distintos e e é a menor aresta na diferença simétrica, w(e)<w(f). Logo U+e-f é uma árvore geradora de custo menor que U, contradição. É a distinção entre pesos que interessa; arestas serem objetos distintos por si só não garante unicidade.'''),
 'a177bf5bc3c7-q3-3': ('Reconstruir o pseudocódigo ilegível e explicitar a convenção de intervalos.', '''Agendamento do maior número de intervalos compatíveis.
Para intervalos semiabertos [s_i,f_i), ordene por término crescente. Comece com ultimo_fim=-infinito. Para cada atividade nessa ordem, aceite-a se s_i>=ultimo_fim e atualize ultimo_fim=f_i. A convenção semiaberta permite uma atividade começar quando outra termina.
A escolha do menor término pode substituir a primeira atividade de uma solução ótima sem reduzir o espaço para as seguintes; repetindo o argumento, o algoritmo é ótimo. Custo O(n log n) para ordenar e O(n) para selecionar. Este pseudocódigo derivado substitui OCR de imagem; não é transcrição literal.'''),
 '1a81ca283132-q1-1': ('Reconstrução correta de DP triangular; código OCR não é executável.', '''Menor soma de um caminho do ápice à base de um triângulo.
Seja tri[i][j] a entrada. Para triângulo não vazio, inicialize dp=[tri[0][0]]. Para cada linha i>0, crie new de tamanho i+1: new[0]=tri[i][0]+dp[0]; new[i]=tri[i][i]+dp[i-1]; para 0<j<i, new[j]=tri[i][j]+min(dp[j-1],dp[j]). Substitua dp por new. A resposta é min(dp).
A recorrência considera exatamente os pais adjacentes de cada célula. Para n linhas, o tempo é O(n^2) e a memória auxiliar O(n). Para [[2],[3,4],[6,5,7],[4,1,8,3]], a soma mínima é 11. O código desta nota é uma reconstrução editorial, e não certifica a transcrição de índices da imagem.'''),
 '1a81ca283132-q2-2': ('O exercício pede o caminho, além da contagem de moedas.', '''Robô coletor de moedas em matriz de r linhas e c colunas, movendo para direita ou baixo.
Defina dp[i][j]=moeda[i][j]+max(dp[i-1][j],dp[i][j-1]), considerando apenas predecessores válidos. A origem tem dp[0][0]=moeda[0][0]. Grave o predecessor escolhido em cada célula. A contagem máxima é dp[r-1][c-1]; reconstrua o caminho seguindo predecessores até a origem e invertendo a ordem.
Em empates, qualquer predecessor ótimo produz um caminho ótimo. Tempo O(rc); memória O(rc) com reconstrução. Se somente a soma for pedida, a memória pode cair para O(c). O OCR do código não deve ser usado como programa executável.'''),
 '1a81ca283132-q3-3': ('Reconstruir recorrência e restringir corretamente ao DAG.', '''Caminho mais longo em um DAG, medido em número de arestas.
Faça uma ordenação topológica. Inicialize d[v]=0 para todos os vértices se o início puder ser qualquer vértice. Processe u nessa ordem e relaxe cada aresta u->v: d[v]=max(d[v],d[u]+1). O resultado é max(d). Para origem fixa s, inicialize d[s]=0 e os demais em -infinito.
A ordem topológica assegura que todos os predecessores já tenham sido processados. Tempo O(|V|+|E|), memória O(|V|). O método depende da ausência de ciclos.'''),
 '1a81ca283132-q4-4': ('Garantir subsequência vazia e corrigir Kadane.', '''Subsequência contígua de soma máxima com subsequência vazia permitida (Lista 5).
Defina fim[0]=0 e fim[j]=max(0,fim[j-1]+a_j). Defina melhor[0]=0 e melhor[j]=max(melhor[j-1],fim[j]). O resultado é melhor[n]. É possível manter apenas fim e melhor em O(1) de memória; o tempo é O(n). Guarde índices de início/fim se for necessário retornar a subsequência.
Para [5,15,-30,10,-5,40,10], a resposta é [10,-5,40,10] com soma 55. Para [-5,-2,-8], a resposta é a subsequência vazia, soma 0. Inicializar o melhor valor em -infinito e exigir um elemento muda a convenção da fonte e é inadequado aqui.'''),
 '1a81ca283132-q5-5': ('Distinguir substring contígua de subsequência.', '''Maior substring comum de x e y.
Se x[i-1]=y[j-1], L[i][j]=L[i-1][j-1]+1; caso contrário, L[i][j]=0. A primeira linha e coluna são zero. A resposta é o maior valor de qualquer célula, não somente L[n][m]. A zeragem em desencontros impõe contiguidade.
Tempo O(nm), memória O(nm) ou O(m) com duas linhas. Para x=ABABC e y=BABCA, a maior substring comum é BABC, tamanho 4. Esta recorrência reconstrói a solução; o OCR do código contém índices e símbolos incertos.'''),
 '1a81ca283132-q6-6': ('Reconstruir DP dos cortes e preservar o exemplo 37 versus 30.', '''Custo mínimo de cortar uma string de comprimento n nas posições dadas.
Ordene os m cortes distintos e internos e acrescente p[0]=0 e p[m+1]=n. Para j=i+1, C[i][j]=0. Para intervalos com cortes internos, C[i][j]=(p[j]-p[i])+min(C[i][k]+C[k][j]) sobre i<k<j. Calcule por tamanho crescente do intervalo e retorne C[0][m+1].
Cada primeiro corte custa o comprimento do segmento atual e divide o problema em dois segmentos independentes. Tempo O(m^3), memória O(m^2). Para n=20 e cortes 3 e 10, cortar em 3 primeiro custa 37; cortar em 10 primeiro custa 30, que é o ótimo.'''),
 '1a81ca283132-q7-7': ('Cobertura é subconjunto de V, não superconjunto; DP em árvore.', '''Cobertura mínima de vértices de uma árvore.
Uma cobertura S satisfaz S subseteq V e contém uma extremidade de cada aresta. Enraíze a árvore. Para cada v, incl[v]=1+sum(min(incl[u],excl[u])) sobre seus filhos u; excl[v]=sum(incl[u]). Para folhas, incl=1 e excl=0. A resposta é min(incl[raiz],excl[raiz]).
Se v não for escolhido, todos os filhos precisam ser escolhidos; se v for escolhido, cada filho pode usar sua melhor opção. Tempo O(|V|), memória O(|V|). A figura com vértices nomeados ainda exige conferência; esta nota não inventa suas arestas.'''),
 '1a81ca283132-q8-8': ('Reconstruir Subset Sum 0/1 e explicar pseudopolinomial.', '''SUBSET SUM para inteiros positivos e alvo t>=0.
Inicialize possivel[0]=True e demais posições até t em False. Para cada valor a, percorra s de t até a em ordem decrescente e faça possivel[s]=possivel[s] or possivel[s-a]. Retorne possivel[t]. O sentido decrescente impede usar o mesmo elemento mais de uma vez.
Tempo O(nt), memória O(t), pseudo-polinomial porque t pode ser exponencial no comprimento de sua representação binária. Para [3,34,4,12,5,2] e t=9, existe subconjunto [4,5]. A versão de decisão tem certificado verificável; esta DP não prova P=NP.'''),
 '1a81ca283132-q9-9': ('A contagem por ordenação topológica só é válida em DAG.', '''Quantidade de caminhos simples distintos entre s e t.
Em um DAG, inicialize count[t]=1 e processe os vértices em ordem topológica inversa: count[u]=sum(count[v]) para sucessores v de u. A resposta é count[s]. O tempo é O(|V|+|E|) operações aritméticas, com inteiros potencialmente grandes.
O enunciado fala em grafo simples geral, que pode ter ciclos. Nesse caso, ordenação topológica não se aplica. Uma solução exata usa DP por subconjuntos: D[S,v] conta caminhos iniciados em s que visitam exatamente S e terminam em v. Base D[{s},s]=1; para aresta v->w com w fora de S, acrescente D[S,v] a D[S union {w},w]. Some D[S,t] sobre S. Tempo O(2^n n^2) em implementação densa e memória O(2^n n). Em grafo não dirigido, trate cada aresta em ambos os sentidos. Não confundir contagem de caminhos simples com caminhadas que repetem vértices.'''),
 '1a81ca283132-q10-10': ('Substituir maximização inválida de Floyd por DP exponencial.', '''Caminho simples máximo entre s e t em grafo geral.
Use DP por subconjuntos: D[S,v] é o maior comprimento/peso de um caminho iniciado em s, com conjunto de vértices visitados exatamente S, terminado em v. Inicialize D[{s},s]=0 e os demais em -infinito. Para cada aresta v->w com w fora de S, atualize D[S union {w},w]=max(D[S union {w},w],D[S,v]+peso(v,w)). A resposta é max(D[S,t]) sobre S; se todos forem -infinito, não existe caminho.
Tempo O(2^n n^2) em representação densa e memória O(2^n n). Trocar min por max no algoritmo de Floyd não impõe a condição de caminho simples: pode combinar trechos que repetem vértices. Em DAG existe uma solução linear por ordenação topológica, mas essa hipótese não está no enunciado geral. Esta nota substitui a alegação polinomial incorreta da resolução.'''),
 'f38bb8142136-q1-1': ('Mesma definição de NP incorreta encontrada no PDF original.', None),
 'f38bb8142136-q2-2': ('Corrigir tamanho binário exato no PDF original.', None),
 'f38bb8142136-q3-3': ('NP-dificuldade não dispensa pertinência a NP.', '''Implicações de reduções polinomiais entre problemas de decisão A e B.
Se A<=p B e B pertence a P, então A pertence a P: componha a transformação com o algoritmo de B.
Se A<=p B e B é NP-completo, isso não torna A NP-completo. Para provar que B é NP-completo a partir de A NP-completo e A<=p B, ainda é necessário mostrar B pertence a NP; a redução prova somente NP-dificuldade.
Há linguagens em NP que não são NP-completas, como a linguagem vazia e a linguagem universal sob reduções many-one usuais. Não atribua isso à hipótese não demonstrada P diferente de NP.
Não se sabe se existe problema NP-completo em P: isso é equivalente a P=NP.'''),
 'f38bb8142136-q5-5': ('Não confundir três partes iguais com 3-PARTITION; redução não pode usar solução desconhecida.', '''TRI-PARTIÇÃO em três grupos de mesma soma: interpretação do enunciado.
Os três grupos são I, J e o complemento de I union J, disjuntos. A expressão da transcrição envolvendo complemento de I intersection J é inconsistente com essa interpretação e precisa ser conferida na página original.
Sob a interpretação de três grupos iguais, o problema está em NP: o certificado atribui cada elemento a um dos três grupos e as somas são verificadas em tempo polinomial em bits.
Redução de PARTIÇÃO: seja S a soma dos inteiros positivos. Se S é ímpar, envie uma instância NÃO fixa como [1,1,2]. Se S é par, acrescente o inteiro S/2. A soma nova é 3S/2; cada grupo deve somar S/2. Por positividade, o novo elemento ocupa sozinho seu grupo. Os dois grupos restantes particionam a entrada original em somas iguais, e vice-versa.
A transformação usa somente a entrada, sem conhecer uma partição prévia. NP mais essa redução prova NP-completude; uma redução inversa não é necessária. Não confundir este problema com 3-PARTITION, que particiona 3m números em m trios e tem outra definição.'''),
 'f38bb8142136-q6-6': ('Adicionar k-2 folhas, não k-1; separar decisão e busca.', '''Árvore geradora com grau máximo k, para cada constante k>=2.
A versão de decisão pergunta se tal árvore existe. Ela pertence a NP: verificar conectividade, ausência de ciclos, cobertura dos vértices e os graus é polinomial.
Para k=2, uma árvore de grau máximo 2 é um caminho, logo o problema equivale a CAMINHO HAMILTONIANO.
Para k>2, a partir de G adicione exatamente k-2 folhas privadas a cada vértice original. Todas as arestas dessas folhas são obrigatórias em qualquer árvore geradora. Se a árvore nova tiver grau máximo k, removê-las deixa uma árvore geradora de G com grau máximo 2, isto é, um caminho hamiltoniano. Reciprocamente, um caminho hamiltoniano de G mais todas essas folhas tem grau máximo k. A construção é polinomial para k fixo.
Portanto a decisão é NP-completa e a tarefa de encontrar tal árvore é NP-difícil. A resolução original alternava k-1 e k-2 folhas; o valor correto é k-2.'''),
 'f38bb8142136-q8-8': ('Interseção não vazia não significa inclusão do certificado em cada conjunto.', '''CONJUNTO INCIDENTE (Hitting Set).
Entrada: universo U, conjuntos S_i subseteq U e limite b. Certificado: H subseteq U com |H|<=b. Verifique H intersection S_i não vazio para todo i. Não é necessário H subseteq S_i. Essa verificação é polinomial na representação explícita da entrada.
Redução de COBERTURA DE VÉRTICES: para G=(V,E) e limite k, use U=V, S_e={u,v} para cada aresta e={u,v}, e b=k. Um H que intersecta todos os S_e é exatamente uma cobertura de vértices de tamanho no máximo k. A transformação é polinomial e preserva SIM/NÃO.
Logo CONJUNTO INCIDENTE é NP-completo. Se P=NP, passa a haver algoritmo polinomial de decisão; se P diferente de NP, não existe tal algoritmo. O enunciado transcrito menciona afirmativas sem enumerá-las, então não se devem inventar itens ausentes.'''),
 'f38bb8142136-q9-9': ('Isomorfismo de subgrafo não é o problema de isomorfismo de grafos.', '''ISOMORFISMO DE SUBGRAFO: dados o padrão G e o grafo alvo H, existe um mapeamento injetivo f:V(G)->V(H) que preserva todas as arestas do padrão?
O certificado é esse mapeamento. Verificar injetividade e que cada aresta {u,v} de G mapeia para uma aresta {f(u),f(v)} de H leva tempo polinomial. Para subgrafo não induzido, não é necessário preservar não arestas.
Redução de CLIQUE: para instância (H,k), construa o padrão G=K_k e mantenha H como alvo. Há uma clique de tamanho k em H se e somente se K_k é isomorfo a um subgrafo de H. Se k>|V(H)|, a resposta é imediatamente NÃO e pode ser enviada a uma instância NÃO fixa; a construção restante é polinomial.
Logo ISOMORFISMO DE SUBGRAFO é NP-completo. A resolução trocava padrão e alvo e concluía incorretamente NP-completude de ISOMORFISMO DE GRAFOS, que é outro problema; essa conclusão não foi preservada.'''),
 '70d6475b28bf-q1-1': ('Reconstruir backtracking legível, com verificação das oito somas.', '''Todos os quadrados mágicos normais de ordem 3.
A soma de 1 até 9 é 45; três linhas iguais dão soma mágica 15. Preencha nove posições por backtracking, mantendo um conjunto dos números ainda não usados. A cada escolha, não repita número; se uma linha, coluna ou diagonal estiver completa, exija soma 15. Se uma linha parcial já tiver soma >=15 com posições restantes, descarte, pois os números são positivos.
Uma poda mais forte soma os menores e maiores números disponíveis para limitar o que ainda pode completar cada linha. Ao preencher as nove posições, confira as três linhas, três colunas e duas diagonais. Há oito soluções ao contar rotações e reflexões separadamente; por exemplo [[8,1,6],[3,5,7],[4,9,2]]. O centro é 5.
Um limite simples é O(9!) para permutar os números, com memória O(9). Não confundir igualdade entre diagonais com a exigência de que todas as oito somas sejam 15. O código da imagem foi substituído por descrição derivada.'''),
 '70d6475b28bf-q4-4': ('A fonte responde cobertura de vértices a um enunciado de cobertura de conjuntos.', '''Branch-and-bound para COBERTURA DE CONJUNTOS.
Entrada: universo U e coleção S_1,...,S_m; minimizar o número de conjuntos escolhidos cuja união é U. Uma solução gulosa viável fornece um limitante superior UB.
Estado: conjuntos escolhidos C, elementos descobertos R e conjuntos candidatos. Se R for vazio, atualize UB com |C|. Se algum elemento de R não tiver candidato que o cubra, descarte. Um limitante inferior válido é ceil(|R|/max_i |S_i intersection R|), quando o denominador é positivo; sobreposição só pode aumentar a necessidade real.
Se |C|+LB>=UB, pode podar ao buscar uma solução ótima (se quiser enumerar todas as ótimas, ajuste o empate). Escolha um elemento descoberto e ramifique escolhendo cada conjunto candidato que o contém. A busca exata é exponencial no pior caso. A formulação em grafo e os limitantes de cobertura de vértices presentes na resolução original não respondem diretamente a este enunciado.'''),
 '70d6475b28bf-q7-7': ('Descrever 2-opt; o original descreve árvore duplicada.', '''Busca local 2-opt para TSP.
Em um ciclo de visita, escolha duas arestas não adjacentes (a,b) e (c,d). Substitua-as por (a,c) e (b,d), invertendo o segmento entre b e c. Em TSP simétrico, a variação de custo é d(a,c)+d(b,d)-d(a,b)-d(c,d). Aceite uma troca se ela reduzir o custo e repita até não haver melhora nessa vizinhança.
Há O(n^2) pares por varredura, com avaliação O(1) da diferença se as distâncias forem acessíveis; inverter o segmento pode custar O(n). Exemplo geométrico: desfazer duas arestas cruzadas pode encurtar o tour.
O término em ótimo local não garante ótimo global. Percorrer duas vezes uma AGM e atalhar vértices é outra heurística, com garantia de 2-aproximação em TSP métrico; isso não é a operação 2-opt. O exemplo numérico da figura original não foi usado para certificar esta busca local.'''),
 '70d6475b28bf-q9-9': ('Corrigir a atribuição fixa de diversificação/intensificação nos algoritmos genéticos.', '''Mecanismos usuais em cinco meta-heurísticas.
Têmpera simulada: aceita melhorias e pode aceitar pioras com probabilidade exp(-delta/T). Temperatura alta favorece exploração; o resfriamento tende a concentrar a busca. Não garante ótimo em um orçamento finito.
Busca tabu: usa memória de movimentos/atributos proibidos e critério de aspiração. A memória reduz ciclos; intensificação explora regiões promissoras e diversificação desloca a busca para regiões pouco visitadas.
Variable Neighborhood Search: alterna vizinhanças e combina perturbação com busca local. A busca local intensifica; mudanças de vizinhança e perturbações ajudam a diversificar.
Algoritmos genéticos: seleção favorece candidatos de melhor aptidão e pode intensificar; cruzamento recombina estruturas; mutação introduz variação e frequentemente contribui à diversificação. Não é correto atribuir universalmente cruzamento à diversificação e mutação à intensificação: os efeitos dependem dos operadores e da seleção.
Colônia de formigas: candidatos são construídos probabilisticamente a partir de feromônio e heurística. Reforçar boas soluções intensifica; evaporação e amostragem mantêm exploração. Nenhum desses mecanismos, isoladamente, certifica ótima global. Esta síntese é editorial e não é reprodução de capítulos do livro citado pela lista.'''),
}


CORRECTIONS.update({
 'd455baef2cdf-q2-2': ('Listar pares de partidas não constrói uma ordem hamiltoniana.', '''Ordenar times de um torneio sem empates de modo que cada time vença o próximo.
Represente cada time por um vértice; para cada par existe exatamente uma aresta dirigida do vencedor ao perdedor. Construa uma lista por inserção: para um novo time x, percorra a lista até o primeiro time y que x venceu; insira x imediatamente antes de y. Se x perdeu para todos os times da lista, insira no fim.
Invariante: cada elemento da lista vence o seguinte. Antes da posição de inserção, todos venceram x; o primeiro time encontrado perdeu para x. Essas são as únicas duas adjacências novas, logo o invariante é preservado. Obtém-se um caminho hamiltoniano do torneio em O(n^2) consultas aos resultados e O(n) memória para a lista, além da representação dos resultados. Listar os pares vencedor/perdedor das partidas não satisfaz a tarefa.'''),
 'd455baef2cdf-q3-3': ('Reconstruir símbolos de exponenciação por quadratura.', '''Computar a^n para inteiro n>=0 por divisão e conquista.
potencia(a,0)=1. Para n>0, calcule uma única vez r=potencia(a,floor(n/2)); se n for par, retorne r*r; se for ímpar, retorne r*r*a.
A identidade a^(2k)=(a^k)^2 e a^(2k+1)=(a^k)^2*a prova a recorrência por indução. Há O(log n) multiplicações e profundidade O(log n), no modelo de operações aritméticas de custo unitário. O custo em bits depende do tamanho de a^n e das multiplicações. Um limite O(n log n) pedido no enunciado também é atendido por essa solução mais eficiente. Não confundir r*r com r+r; esses símbolos estão corrompidos no OCR.'''),
 'd455baef2cdf-q4-4': ('Código rotacionado e índices ilegíveis: substituir por seleção por partição.', '''K-ésimo menor elemento da união de duas listas ordenadas A e B de tamanhos m e n, contando duplicatas.
Exija 1<=k<=m+n e coloque a lista menor em A. Procure i entre max(0,k-n) e min(k,m), com j=k-i. Use -infinito quando a partição não tiver elemento à esquerda e +infinito quando não tiver elemento à direita.
Se A[i-1]<=B[j] e B[j-1]<=A[i], retorne max(A[i-1],B[j-1]). Se A[i-1]>B[j], diminua i; caso contrário, aumente i. A busca binária encontra a partição em que exatamente k elementos ficam à esquerda, todos menores ou iguais aos da direita.
Tempo O(log(min(m,n)+1)) e memória O(1), inclusive quando uma lista é vazia, caso em que basta acessar a outra. Isso atende ao limite O(log m+log n) quando as listas são não vazias. Esta nota é reconstrução derivada; não é transcrição do código rotacionado.'''),
 'd455baef2cdf-q5-5': ('O OCR apagou n−1 e expoentes nas recorrências.', '''Comparação de três recorrências, com casos base constantes.
A: T_A(n)=5T_A(n/2)+Theta(n), logo Theta(n^(log_2 5)), aproximadamente n^2,322, pelo primeiro caso do Teorema Mestre.
B: T_B(n)=2T_B(n-1)+Theta(1), logo Theta(2^n). O tamanho do subproblema é n−1; a transcrição que perdeu o sinal de menos não é a recorrência pretendida.
C: T_C(n)=9T_C(n/3)+Theta(n^2), logo Theta(n^2 log n), pelo caso de equilíbrio do Teorema Mestre.
Escolha C assintoticamente: n^2 log n cresce menos que n^2,322 e que 2^n. Arredondamentos de n/2 e n/3 não mudam essas ordens sob hipóteses usuais. Não se afirma superioridade para todo n pequeno ou todas as constantes de implementação.'''),
 'd455baef2cdf-q6-6': ('Explicitar desigualdades e hipótese de inteiros distintos.', '''Ponto fixo A[i]=i em vetor ordenado de inteiros distintos, índices de 1 a n.
Faça busca binária: m=floor((l+r)/2). Se A[m]=m, retorne m. Se A[m]<m, procure somente à direita; se A[m]>m, procure somente à esquerda. Se o intervalo ficar vazio, não há ponto fixo.
Como os valores são inteiros estritamente crescentes, para i<m temos A[i]<=A[m]-(m-i), e para i>m temos A[i]>=A[m]+(i-m). Portanto A[m]<m elimina todos os índices à esquerda; A[m]>m elimina todos à direita. Tempo O(log n), memória O(1) na versão iterativa. Valores repetidos ou números reais eliminam essa justificativa.'''),
 'd455baef2cdf-q7-7': ('Fórmula da resolução só vale para n par; não prova optimalidade.', '''Hanoi com quatro pinos: analisar a estratégia apresentada, não afirmar que ela é ótima.
Para n>=2, mova n−2 discos para um pino auxiliar usando quatro pinos; mova o penúltimo para o outro auxiliar, o maior para o destino e o penúltimo para o destino; por fim mova os n−2 discos para o destino. Bases T(0)=0, T(1)=1. Assim T(n)=2T(n−2)+3.
Para n=2k, T(n)=3*2^k−3. Para n=2k+1, T(n)=4*2^k−3. Em particular T(2)=3, T(3)=5 e T(4)=9. O crescimento dessa estratégia é Theta(2^(n/2)).
A expressão 3*2^(n/2)−3 não serve para n ímpar. A recorrência conta movimentos desse algoritmo; não demonstra o mínimo possível para quatro pinos. Por exemplo existem estratégias melhores para tamanhos maiores, então não se deve chamar essa contagem de ótimo geral.'''),
 'd455baef2cdf-q9-9': ('Reconstruir busca no pico sem acesso fora do vetor.', '''Pico de vetor unimodal de valores distintos.
Mantenha l=1,r=n. Enquanto l<r, faça m=floor((l+r)/2). Se A[m]<A[m+1], faça l=m+1; caso contrário, faça r=m. Retorne l.
O intervalo sempre contém o pico. Se a sequência cresce entre m e m+1, o pico fica à direita; se decresce, fica em m ou à esquerda. Enquanto l<r, m<r e portanto m+1 está no vetor. Tempo O(log n), memória O(1). Não é busca pelo máximo de vetor arbitrário; a hipótese de unimodalidade permite descartar uma metade.'''),
 'd455baef2cdf-q10-10': ('Código rotacionado: reconstruir lucro por divisão e conquista.', '''Dias de compra e venda para maximizar p[venda]−p[compra], com compra<venda.
Divida os dias em duas metades. A melhor operação está inteiramente à esquerda, inteiramente à direita ou compra à esquerda e vende à direita. Resolva recursivamente as duas primeiras opções. Para a terceira, encontre preço mínimo e seu dia na metade esquerda e preço máximo e seu dia na metade direita. Compare os três lucros, guardando os índices.
Base de um único dia: nenhuma operação válida, com valor -infinito quando a compra/venda for obrigatória. Para n>=2, T(n)=2T(n/2)+O(n)=O(n log n), memória O(log n) de pilha. Se puder não operar, compare também com lucro zero.
Para preços [9,1,5], compre no dia 2 e venda no dia 3, lucro 4 por ação ou 4000 por 1000 ações. Há também solução linear mantendo o menor preço anterior, mas essa nota apresenta a divisão e conquista solicitada.'''),
 '97254bb4a1b8-q2-2': ('Modelagem em Hamiltoniano não basta para provar NP-dificuldade.', '''Mesa circular de cavaleiros: grafo de compatibilidade.
Cada cavaleiro é um vértice; existe aresta entre dois cavaleiros se eles podem sentar juntos. Uma disposição circular válida corresponde a um ciclo hamiltoniano nesse grafo, incluindo a compatibilidade entre último e primeiro. Um caminho hamiltoniano sozinho não garante a mesa circular.
Para a versão de decisão com número variável de cavaleiros, o certificado é a ordem circular, verificável em tempo polinomial. Para provar NP-dificuldade, reduza CICLO HAMILTONIANO à disposição: para qualquer grafo simples G com pelo menos três vértices, crie um cavaleiro por vértice e declare briguentos exatamente os pares sem aresta de G. Há disposição válida se e somente se G tem ciclo hamiltoniano. Isso fornece a direção de redução necessária; a decisão é NP-completa.'''),
 '97254bb4a1b8-q3-3': ('Corrigir índices do grafo e testar atendimento de todas as famílias.', '''Famílias em mesas via fluxo máximo.
Crie fonte s, vértices F_i para famílias e M_j para mesas, e sorvedouro t. Arestas s->F_i têm capacidade a_i; F_i->M_j têm capacidade 1 para todos os pares; M_j->t têm capacidade b_j. Capacidades inteiras permitem obter um fluxo máximo integral.
Existe disposição para todos se e somente se o fluxo máximo vale sum_i a_i. Uma unidade em F_i->M_j significa colocar um membro da família i na mesa j; capacidade 1 impede dois membros da mesma família na mesma mesa. As capacidades de origem e destino asseguram tamanhos das famílias e mesas. Se o fluxo for menor, a disposição completa é impossível. O desenho original trocava nomes de índices; esta reconstrução define todas as arestas.'''),
 '97254bb4a1b8-q5-5': ('Objetivo não é equação igual a zero; corrigir V/S no lucro final.', '''Programação linear de duas rações.
V e S são quantidades de pacotes de Viralata e Sucesso, não negativas. Lucro unitário V: 7−1−3−1,40=1,60. Lucro unitário S: 6−2−2−0,60=1,40. Maximize 1,6V+1,4S, sem impor que esse valor seja zero.
Restrições: V<=110000; V+2S<=240000 (cereal); 1,5V+S<=180000 (carne); V,S>=0.
Vértices viáveis: (0,0), (0,120000), (60000,90000), (110000,15000), (110000,0). Lucros respectivos: 0,168000,222000,197000,176000. O ótimo é V=60000,S=90000, lucro 222000. A expressão com S=110000 na resolução é erro; 1,4*90000=126000. Esses valores inteiros também são viáveis se os pacotes exigirem integralidade.'''),
 '97254bb4a1b8-q6-6': ('Quantidades de moedas podem ser zero; separar limite k e minimização.', '''Troco mínimo como programa linear inteiro.
Para valores de moedas c_1,...,c_n positivos e alvo v>=0, use x_i inteiro não negativo, quantidade de moedas do tipo i. Minimize sum_i x_i sujeito a sum_i c_i*x_i=v.
Permitir x_i=0 é necessário: nem todos os tipos precisam aparecer. Para a versão de decisão com no máximo k moedas, acrescente sum_i x_i<=k e verifique viabilidade, sem necessidade de objetivo. Estoque ilimitado não requer limites superiores para x_i. Se não houver solução inteira, o troco exato é impossível. A relaxação para reais pode dar frações de moedas e não resolve o problema inteiro.'''),
 '97254bb4a1b8-q8-8': ('As restrições precisam excluir i=j para não tornar o modelo inviável.', '''Oito damas por programação de restrições.
Variável A[i] em {1,...,8} é a coluna da dama na linha i, para i=1,...,8. Para cada par 1<=i<j<=8, imponha A[i]!=A[j] e abs(A[i]−A[j])!=j−i.
Equivalentemente, imponha AllDifferent(A[i]), AllDifferent(A[i]+i) e AllDifferent(A[i]−i). Uma dama por variável garante uma por linha; as demais restrições impedem coluna e diagonais compartilhadas.
O quantificador original para todos i,j inclui i=j e exigiria A[i]!=A[i], o que torna o modelo impossível. A restrição correta é para índices distintos. Uma solução é [1,5,8,6,3,7,2,4]; com linhas rotuladas há 92 soluções quando rotações/reflexões são contadas separadamente.'''),
 '97254bb4a1b8-q10-10': ('Corrigir limite da restrição agregada que proíbe cliques válidas.', '''Clique máxima como programa linear inteiro binário.
Para cada vértice i, variável x_i em {0,1} indica participação na clique. Maximize sum_i x_i. Para cada par distinto não adjacente {i,j}, imponha x_i+x_j<=1. Não há restrição desse tipo para pares adjacentes. Todo conjunto escolhido é clique e qualquer clique satisfaz o modelo.
A restrição original h_j*x_j+sum_{i não vizinho de j}x_i<=1 é incorreta quando h_j>1: impede escolher o próprio j. Uma forma agregada equivalente válida é h_j*x_j+sum_{i não vizinho de j}x_i<=h_j, com h_j igual à quantidade de não vizinhos distintos e sem autoarestas; para h_j=0 a restrição é dispensável.
O modelo por pares é mais simples e tem O(n^2) restrições. Clique de G corresponde a conjunto independente no grafo complementar, não necessariamente no próprio G.'''),
})


def main():
    items = {i['id']: i for i in read_json(ROOT / '02-acervo/itens.json', [])}
    manifest = read_json(ROOT / '03-triagem/correcoes.json', {})
    sources = {d['id']: d['sha256'] for d in read_json(ROOT / '03-triagem/inventario.json', [])}
    for identifier, (reason, text) in CORRECTIONS.items():
        if text is None:
            text = CORRECTIONS['c09' if identifier.endswith('q1-1') else 'c08'][1]
        item = items[identifier]
        original = item.get('sha256_original', item['sha256'])
        source_hash = sources[item['documento_id']]
        if identifier in manifest and manifest[identifier]['sha256_original'] != original:
            raise RuntimeError(f'Fonte mudou: {identifier}; revise a correção antes de atualizar o hash.')
        if identifier in manifest and manifest[identifier].get('sha256_fonte', source_hash) != source_hash:
            raise RuntimeError(f'Arquivo-fonte mudou: {identifier}; não basta o OCR continuar igual.')
        path = ROOT / '03-triagem/correcoes' / (identifier + '.md')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text.strip() + '\n', encoding='utf-8')
        manifest[identifier] = {'sha256_original': original, 'sha256_fonte': source_hash, 'arquivo': caminho_guardado(path),
                                'motivo': reason, 'revisor': 'Codex (agente; não é revisão humana)',
                                'documento_id': item['documento_id']}
    write_json(ROOT / '03-triagem/correcoes.json', manifest)
    print(f'{len(manifest)} correções derivadas registradas.')


if __name__ == '__main__':
    main()
