# 7b4da6a8adf7-q2-8

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 12, 13

2. Dando prosseguimento com a atualiza¸c˜ao do valor de tk ao ser dividido por 2,
o que permite que haja o algoritmo continue para que a convers˜ao pare quando
o n´umero for menor ou igual a zero. Dessa forma, precisamos mostrar que se o
invariante de la¸co  ´e v´alido para k, ele ser´a v´alido para k+1. Supomos, ent˜ao,
que n(k) ´e v´alido, ent˜ao sabemos que n(k) = tk.2k + mk e a partir do corpo do
loop deduzimos que:

                                     k’ = k + 1
                                    b[k’] = tk mod 2
                                               tk′ = tk ÷ 2

Assim, temos dois casos a provar:

• Quando tk ´e par, ent˜ao b[k’] = 0 e b[1...k’] ainda representa mk.

                     ∴   mk′ = mk

             Logo  n(k) = mk + tk.2k ⇒n(k′) = mk′ + tk′.2k′
            = mk + (tk/2).2k′ = mk + tk.2k = n

, temos ent˜ao que n(k + 1) ´e v´alido ∀tk par   ( I )
  • Quando tk  ´e ´ımpar, isso nos d´a ent˜ao que b[k’] = 1 e b[1...k’] representa
2k + mk.

                       i=k                     i=k+1              i=k′
        Pois, mk = X b[i] 2i−1 ⇒mk+1 = X  b[i] 2i−1 = X b[i] 2i−1

                        i=1                        i=1              i=1

                             i=k′                        i=k
            = X b[i] 2i−1 = b[k′].2k + X b[i] 2i−1

                          i=1                        i=1
                    ∴mk′ = 2k + mk
Sabendo disso e que, quando tk ´e ´ımpar tk′ = tk−12   , segue-se que:

                 n(k) = mk + tk.2k ⇒n(k′) = mk′ + tk′.2k′

                                                   tk −1
               = (mk + 2k) +         .2k′
                                       2
               = (mk + 2k) + (tk −1).2k
           = mk + 2k + tk.2k −2k = mk + tk.2k = n



                            Page xiiTemos ent˜ao que n(k + 1) ´e v´alido ∀tk ´ımpar.  ( II )

      Logo, de (I) e (II), temos que o invariante ´e v´alido ∀tk

      T´ermino: Sabemos que o la¸co de repeti¸c˜ao executa enquanto o nosso inteiro t
            ´e maior do que zero, no entanto, isso acontece considerando que t inicializa com
      n e ´e decrementado dividindo seu valor por dois a cada intera¸c˜ao. Desse modo,
      na ´ultima itera¸c˜ao, quando “t ≤0”e “k = n”, o valor de n ´e:

                             n = tn.2n + mn

       Portanto, conclui-se que o algoritmo Conversor D-B est´a correto e, de fato, con-
       verte para bin´ario um n´umero natural dado.
                                                ■
