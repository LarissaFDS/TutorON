Pico de vetor unimodal de valores distintos.
Mantenha l=1,r=n. Enquanto l<r, faça m=floor((l+r)/2). Se A[m]<A[m+1], faça l=m+1; caso contrário, faça r=m. Retorne l.
O intervalo sempre contém o pico. Se a sequência cresce entre m e m+1, o pico fica à direita; se decresce, fica em m ou à esquerda. Enquanto l<r, m<r e portanto m+1 está no vetor. Tempo O(log n), memória O(1). Não é busca pelo máximo de vetor arbitrário; a hipótese de unimodalidade permite descartar uma metade.
