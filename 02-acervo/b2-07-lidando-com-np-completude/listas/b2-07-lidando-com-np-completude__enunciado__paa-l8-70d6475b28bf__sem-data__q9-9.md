# 70d6475b28bf-q9-9

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 12, 13, 14

9.  Escolha 5 meta-heur´ıstias do livro “Handbook of Metaheuristics”


                                  Page xii( https:// www.springer.com/gp/book/9783319910857, cada cap´ıtulo fala de
uma meta-heur´ıstica ). Para cada uma das 5, descreva o algoritmo e explique
quais os mecanismos de intensifica¸c˜ao e diversifica¸c˜ao da busca.


  Solu¸c˜ao:

     • Tˆempera Simulada (Simulated Annealing):
       Importante ressaltar a analogia do comportamento do algoritmo ao seu nome,
      que reprenta uma forma de ”abaixar a temperatura”gradualmente at´e que um
         l´ıquido se solidifique. No nosso caso, a temperatura serve como m´etrica para
         intensifica¸c˜ao e diversifica¸c˜ao, e representa uma probabilidade de escolher alea-
       toriamente que varia com o tempo, em outras palavras, ´e uma forma de deixar
       a escolha da probabilidade de forma dinˆamica e gradual.  ´E no contexto ini-
         cial desse algoritmo que ocorre a maior quantidade de diversifica¸c˜ao, isto  ´e,
         explora¸c˜ao a fim de conhecer as possibilidades e evitar cen´arios como m´aximos
         locais, plan´ıcies e encostas. Em seguida, ocorre a intensifica¸c˜ao, passo que busca
       otimizar certo resultado.

     • Busca Tabu (Tabu Search):
          ´E um algoritmo de busca por vizinhan¸ca que implementa o conceito de mem´oria
       para o seu funcionamento. Com a mem´oria, ele permite que haja maior diver-
          sifica¸c˜ao das solu¸c˜oes no espa¸co de busca ao evitar que haja repeti¸c˜ao `a curto
       prazo de movimentos realizados recentemente e obrigando a procura de novas
         solu¸c˜ao ao sair do espa¸co de vizinhan¸ca. Esse algoritmo foi criado pois apesar
      do fator de aleatoriedade ser crucial para fugir de cen´arios como m´aximos lo-
         cais, plan´ıcies e encostas, isso pode fazer com que haja uma taxa significativa
       de visita em solu¸c˜oes repetivas. Ele funciona partindo de uma solu¸c˜ao inicial e
        se movendo, a cada itera¸c˜ao, para a melhor solu¸c˜ao na vizinhan¸ca sem ir para
         solu¸c˜oes que est˜ao na lista tabu, dessa forma, intensificando e diversificando as
          solu¸c˜oes.

     • Variable Neighborhood Search:
          ´E um algoritmo que possui mais de uma vizinhan¸ca auxiliando na fuga de um
       m´aximo local. Inicialmente, uma solu¸c˜ao ´e gerada automaticamente. Ap´os isso,
        ela ´e intensificada atrav´es do VND e verificada se ´e a melhor solu¸c˜ao que j´a foi
       encontrada. Caso seja, ela explora a vizinhan¸ca em quest˜ao, caso n˜ao seja, ela
       explora outra (realizando uma visita aleat´oria tamb´em). Isso garante que haja
         diversifica¸c˜ao e intensifica¸c˜ao da busca. Uma caracter´ıstica importante ´e que
       deve haver diferen¸ca significativa entre as vizinhan¸cas.

     • Algoritmo Gen´etico (Genetic Algorithms):
          ´E um algoritmo de otimiza¸c˜ao baseado em evolu¸c˜ao natural. Para que a solu¸c˜ao
        ”´otima”seja encontrada,  ´e necess´ario que se tenha v´arias ”gera¸c˜oes”, assim
      como ocorre na vida real. H´a dois processos important´ıssimos nesse algoritmo,




                               Page xiiisendo eles: cross-over e muta¸c˜ao. O primeiro ´e respons´avel por misturar as in-
             forma¸c˜oes de maneira aleat´oria a fim de criar novas solu¸c˜oes que s˜ao a mistura
          de solu¸c˜oes j´a existentes, essa seria a etapa de diversifica¸c˜ao.  J´a a muta¸c˜ao ´e
            respons´avel por adicionar variedade `as solu¸c˜oes existentes, adicionando peque-
           nas mudan¸cas, essa sendo a intensifica¸c˜ao. A muta¸c˜ao tamb´em ´e respons´avel
          por casos onde s˜ao criadas caracter´ısticas que caracterizam um melhor usu´ario.

        • Colˆonia de formigas (Ant Colony Optimization):
           Esse algoritmo inspirado na comunica¸c˜ao baseada em feromˆoneos realizada pe-
             las formigas ´e geralmente utilizado para encontrar o melhor caminho, visto que
          a analogia procede da grande habilidade do inseto em se guiar em busca de co-
         mida atrav´es da coopera¸c˜ao entre a colˆonia. O algoritmo funciona baseado na
            comunica¸c˜ao dentro de uma colˆonia de formingas artificiais, usando o caminho
              artificial de feromˆoneos deixados por elas. Esse caminho ´e usado de maneira
            num´erica para probabilisticamente construir solu¸c˜oes e, em seguida, adaptar
           as solu¸c˜oes existentes de acordo com a experiˆencia adquirida. Inicialmente sem
          muita experiˆencia, as formigas procuram diversificar seus caminhos, explorando
           as possibilidades e `a medida que a experiˆencia de formigas anteriores ´e adqui-
             rida, a colˆonia recebe conhecimento e consegue se guiar para, baseada nele,
             intensificar e encontrar a melhor solu¸c˜ao poss´ıvel.
