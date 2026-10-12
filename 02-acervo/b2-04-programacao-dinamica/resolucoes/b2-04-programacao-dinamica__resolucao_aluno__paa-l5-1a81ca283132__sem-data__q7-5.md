# 1a81ca283132-q7-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 6, 7

7. Uma cobertura de v´ertices de um grafo G = (V, E ) ´e um subconjunto de
v´ertices S ⊇V que inclui ao menos uma extremidade de cada aresta de E .
Forne¸ca um algoritmo de tempo linear para a seguinte tarefa.

Entrada: Uma ´arvore n˜ao-direcionada T = (V, E).
Sa´ıda: O tamanho da menor cobertura de v´ertices de T.
Por exemplo, na ´arvore abaixo, as poss´ıveis coberturas de v´ertice incluem
{A, B, C, D, E, F, G} e {A, C, D, F}, mas n˜ao {C, E, F}. A menor cobertura de
v´ertice tem tamanho 3: B, E, G

Page vi[OCR parcial do recorte p7-fig1.png; conferir símbolos na imagem]
A
D
B
E
G
C
F


Solu¸c˜ao:


[OCR parcial do recorte p7-fig2.png; conferir símbolos na imagem]
class vertex-cover
static int min(int x, int y){
return (x<y)？x：y
class node
public int dataj
public int vertexcover;
public node left,right;
static node createNode(int data)
node el = new nodet);
el.vertexcover=θ;
el.left =el.right =null;
el,data = data}
return el;
statitint vCover(noderoot){
if (root = null)
return θ
if{root.left ==null &&
root.right == nul1)
return B;
if（root.vertexcover=8)
return root.vertexcover!
intsizeWithRoot=1+vCover(root.left)+
vCaver(root.right);
int sizeNoRoot=θ;
if(root,left 1=nul1)
sizeNoRoot+=1+vCover(root.left,left)+
vCover(roat.left.right);
if{root.right =null)
sizeNoRoot+=1+vCover(root.rightleft)+
vCover(root.right.right);
root.vertexcover=Math.Min(sizeWithRoot,sizeNoRoot);
Consale,Write("0 tamanho da menor cobertura de vertice é {0}";root.vertexcover);
return root.vertexcover;
