# a177bf5bc3c7-q5-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 4, 5, 6

5. Alice quer dar uma festa e est´a decidindo quem chamar. Ela tem n pessoas
as quais escolher, e ela fez uma lista de quais pares dessas pessoas conhecem
uma a outra. Ela quer selecionar o maior n´umero de pessoas poss´ıvel, sujeito
a duas restri¸c˜oes: na festa, cada pessoa deve ter pelo menos outras cinco
pessoas que ela conhece e outras cinco pessoas que ela n˜ao conhece. Forne¸ca
um algoritmo eficiente que tome como entrada a lista das n pessoas e a lista
de pares de quem conhece quem e calcule a melhor escolha de convidados
para a festa. Dˆe o tempo de execu¸c˜ao em termos de n.

Solu¸c˜ao:

Page iv[OCR parcial do recorte p5-fig1.png; conferir símbolos na imagem]
void aliceAlgoritm(int n)
GraphG(n);
bool convidados[n];
queue<int>rejeitados;
int entry,aceitos=0；
//Recebe os dados do grafo
for(inti=θ;i<n;i++)
[incerto] do
cout 《<"Person #:";
cin >>entry;
//Adicionar relacaoa matriz
if(entry>θ&&entry<=n&entry!=i+1)
if (G.isEdge(i,entry -1))
[incerto] a>>oxaomnsof>ua>>opepa>>+>>opp>>ao
else
G.addedge(i,entry - 1);
else if (entry ==i + 1)
cout<<"Essaentradanaoévalida!"<<endl;
else if (entry == -1)
[incerto] >>x>>（>>>>+>>>
else
cout<<"Entradainvalida,tentenovamente!“;
}while (entry !=-1);



[OCR parcial do recorte p5-fig2.png; conferir símbolos na imagem]
for(int i=0；i<n;i++)
convidados[i]=1;//convidatodomundo
connections=G.getDegree(i);
if(connections<5lln-connections<5）//verifica os requisitos
rejeitados.push(i);// coloca na lista de rejeitados
convidados[i] = 0; // tira da lista de convidados
//Verifica os requisitos
while(!rejeitados.empty())
intj=rejeitados.front();
rejeitados.pop();
for (int i=θ;i<n;i++)
6.removeEdge(i,j);
[incerto] S   p eti / ( ==sop  (s > sua -u ! s > ()au)) 
rejeitados.push(i);
convidados[i]=0;


Page v[OCR parcial do recorte p6-fig1.png; conferir símbolos na imagem]
//Contagemdeconvidados
cout<<endl;
for（int i=0;i<n;i++)
if (convidados[i]==1)
aceitos++;
I/Resultadodoalgoritmo
if (aceitos == n)
else if (aceitos == 0)
cout <<"Ninguem atende aos requisitos,entao naoé possivel Alice dar uma festa.\n";
else
[incerto] sd od>> sa>>，osad>>u>>s>>
int main()
intn;//numerodepessoas
cin >> n;
cout<< endl;
aliceAlgoritm(n);
cout<<endl;
return 0；


O tempo de execu¸c˜ao em termos de n ´e O(n2). Isso se d´a pois no loop for em que se
recebe e insere as conex˜oes no grafo, ocorre n itera¸c˜oes, a fim de encontrar todas as
conex˜oes de todos os poss´ıveis convidados, onde cada um pode ter no m´aximo n - 1
conex˜oes. Al´em disso, h´a outro loop for que verifica se os requisitos (conhecer mais
de 5 pessoas, e n˜ao conhecer no m´ınimo 5 pessoas) est˜ao sendo cumpridos. Em seu
pior caso, todos os poss´ıveis convidados foram rejeitados, ent˜ao para cada um deles
haver´a n itera¸c˜oes para remover da lista de convidados e de todas as suas conex˜oes.
Sendo assim, justifica-se o tempo polinomial O(n2).
