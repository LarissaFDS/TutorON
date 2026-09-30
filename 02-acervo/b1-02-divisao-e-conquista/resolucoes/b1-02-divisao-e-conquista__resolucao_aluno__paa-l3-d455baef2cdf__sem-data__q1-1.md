# d455baef2cdf-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 1, 2, 3

1. Existem n panquecas, todas de tamanhos diferentes, empilhadas umas sobre
as outras. Vocˆe pode colocar uma esp´atula sob uma das panquecas e virar
a pilha inteira acima da esp´atula.
O objetivo ´e arranjar as panquecas de
acordo com o tamanho, com a maior na parte inferior. A Figura mostra uma
instˆancia do quebra-cabe¸ca para n = 7. Projete um algoritmo para resolver
este problema e determine o n´umero de opera¸c˜oes feitas pelo algoritmo no
pior caso.


[OCR parcial do recorte p1-fig3.png; conferir símbolos na imagem]
—


Solu¸c˜ao:[OCR parcial do recorte p2-fig1.png; conferir símbolos na imagem]
//considere V a pilha de panquecas c n a quant. de panquecas q ainda nao foran ordenadas
//funcao para imverter a pilha inteira acima da maior
int flipPancakes(int *V, int n)
int start=1,end=n, aux, i;
while(start < end)f // percorre todo o vetor invertendo as posicoes
aux = V[start];
V[start]=V[end];
fxne = [pua]A
1--pua
//funcao para descobrir qual a posicao da maior panqueca da pilha
int biggerpancake(int *V, int n)f
int i = 1,bigger = 1j
for(i=l; i<ng i++}
printf("%d -",V[i]);
/f atualiza a variavel bigger
printf("A maior panqueca esta na pos: %d", bigger);
return bigger)
vaid pancakes(int *v, int m)
if(n == 1)
printf(*nTodas as panquecas foram empilhadas!n");
return,
int posBigger = biggerPancake(V, n);
flippancakes(V, posBigger) : //primeira inversao com tds acima da
//maior panqueca, deixa a mainr no topo
// inverte td a pilha, a maior panqueca
Flippancakes(V, n-1);
// encontrada nessa iteracao fica na posicao n-l
pancakes(V, n-i);
void main()
int V[8] = [0,2, 3, 1,6,4, 5, 7]: // comeca com as panquecas
// empilhadas como na figura
pancakes(V, 7);
int ij
printf("Essa eh a pilha atual de panquecas:\n");
for (i=1; i<=7;i++)
printf("%d-",V[i]]


Page iiNo pior caso, temos que o n´umero de opera¸c˜oes feitas pelo algoritmo ser´a O(n2), uma
vez que, no pior dos casos, o algoritmo executa 2(n −1) opera¸c˜oes de virar a pilha e
cada uma destas custam tempo linear.
