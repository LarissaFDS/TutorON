# c02

Fonte: materiais\c02_gabarito_algoritmo_x_nota_2.md | página(s): não informada na transcrição

Versão derivada corrigida por agente; original SHA-256: f975aafbe28e28a84aa69a50fb029c1f4aad504d6b2d90ee483ef52b9d5c3a98. Não é aprovação do professor.

Prova de corretude do Algoritmo X que retorna o maior elemento.
Teorema: para qualquer intervalo não vazio A[inicio..fim] de tamanho m=fim-inicio+1, X retorna seu máximo.
Caso base: m=1 implica inicio=fim; o retorno A[inicio] é o único elemento.
Hipótese de indução forte: para todo tamanho k com 1<=k<m, X devolve o máximo de qualquer intervalo desse tamanho.
Passo indutivo: para m>1, meio=inicio+floor((fim-inicio)/2). Os intervalos A[inicio..meio] e A[meio+1..fim] são não vazios, disjuntos, cobrem o intervalo original e têm tamanhos menores que m. Pela hipótese, as chamadas retornam os máximos a e b. Compará-los e retornar o maior produz o máximo do intervalo inteiro. Os tamanhos diminuem, provando também a terminação.
São m-1 comparações de combinação e tempo Theta(m); a pilha tem profundidade O(log m). Esta é uma correção editorial da prova transcrita, sem atribuir ao professor a nova redação.
