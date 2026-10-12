# Revisão 7b4da6a8adf7-q8-9

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 13, 14
SHA-256: 6901f2f802ec768ccf7adfc3d9271bc1dc1f687e0aef594c139fed5427a8520b

Confiabilidade: nao_verificada

Motivo: Revisão de fonte e conteúdo pendente.

## Enunciado e resolução — transcrição sem alteração

8. A sequˆencia de Fibonacci  ´e definida da seguinte forma:  f0 = 0; f1 = 1 e
   fi+2 = fi+1 + fi, ∀i ≥0. Prove que para todo n ≥1 temos:





  em que o lado esquerdo representa n-´esima potˆencia de uma matriz 2 x 2.


     Solu¸c˜ao:

   A prova pode ser feita por indu¸c˜ao:

    Passo Base: (n = 1)

                                                1
                             1  1       f1+1  f1       f2  f1                   An =      =       =
                             1  0         f1   f0       f1  f0

    Considerando a sequˆencia de Fibonacci at´e os 3 primeiros termos, temos que:

                        f0 = 0         f1 = 1         f2 = f0 + f1 = 1


                                                    1
                                    f2  f1       1  1
      e, portanto, a matriz A =       =              , associa direta e corretamente a
                                    f1  f0       1  0
     sequˆencia de Fibonacci para os seus 3 primeiros elementos elementos.

    Hip´otese de Indu¸c˜ao: (n ≤k)

                                                               k
                                          1  1       fk+1   fk    Suponha que a hip´otese de indu¸c˜ao Ak =      =                       ,  ∀n ≤k.
                                          1  0         fk   fk−1



                                  Page xiii
[ilegivel] Visão pendente: HTTPErrorPasso Indutivo: (n = k + 1)

     Deseja-se saber se a hip´otese ´e v´alida ∀n > k. Portanto, sabendo que

                                                                          k
                                                   1  1
           Ak+1 = Ak · A1    , por defini¸c˜ao, e  Ak =                , por hip´otese.
                                                   1  0

     Segue-se que:

                              fk+1   fk      1  1      fk+1 + fk  fk+1               Ak · A =                       ·     =
                                fk   fk−1     1  0       fk + fk−1   fk

                                fk+2  fk+1                   fk+2  fk+1            ∴  Ak · A =       ⇒  Ak+1 =
                                fk+1   fk                    fk+1   fk

     Portanto, por indu¸c˜ao, se a hip´otese ´e v´alida para n = k ent˜ao ´e v´alida para n = k+1,
                                n
                       1  1
     logo a matriz An =           provˆe os {n + 1, n, n −1} -´esimos termos da
                       1  0

     sequˆencia de Fibonacci, ∀n ≥1.

                                                ■

## Parecer local

nao_executado

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
