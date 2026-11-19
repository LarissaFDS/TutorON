# Três exemplos antes/depois do OCR

As transcrições abaixo são saídas reais. Não foram corrigidas para parecerem melhores.

## Texto nativo preservado

Antes: [materiais\Disponiveis\RAG PAA\PAA_L4.pdf, página 1](../01-extraido/figuras/a177bf5bc3c7/p1.png)
Depois: [Markdown completo](../01-extraido/a177bf5bc3c7.md)
Método: texto_pdf. Qualidade: **parcial**.

```text
Lista de Exerc´ıcios 3

8 de abril de 2022

Engenharia de Computa¸c˜ao

Lilian Giselly Pereira Santos
Pedro Henrique de Brito Nascimento
Projeto e An´alise de Algoritmos - Rian Gabriel Pinheiro

Cap´ıtulo 4 - Algoritmos Gulosos

1. Considere um grafo n˜ao-direcionado G = (V, E) com pesos de aresta n˜ao-
negativos we ≥0. Suponha que vocˆe computou uma ´arvore geradora m´ınima
de G e que tamb´em computou os caminhos m´ınimos para todos os n´os par-
tindo de um particular n´o s ∈V . Agora suponha que cada peso de aresta seja
aumentado em uma unidade: os novos pesos s˜ao w

′
e = we + 1.

a) Ser´a que a ´arvore geradora m´ınima muda? Dˆe um exemplo para o qual ela
muda ou prove que ela n˜ao pode mudar.

b)Ser´a que os caminhos m´ınimos mudam? Dˆe um exemplo para o qual eles
mudam ou prove que isso n˜ao pode ocorrer.

Solu¸c˜ao:

(a) N˜ao, a ´arvore geradora m´ınima permanece a mesma. Por exemplo, se G tem n

v´ertices, ent˜ao qualquer ´arvore geradora tem n - 1 arestas. Portanto, ao incre-
mentar cada peso de aresta em uma unidade, aumenta-se o custo de cada ´arvore
gerada tamb´em por um
```

## Código em recorte de imagem

Antes: [materiais\Disponiveis\RAG PAA\PAA_L5.pdf, página 1](../01-extraido/figuras/1a81ca283132/p1.png)
Depois: [Markdown completo](../01-extraido/1a81ca283132.md)
Método: rapidocr+texto_pdf. Qualidade: **parcial**.

```text
[OCR parcial do recorte p1-fig3.png; conferir símbolos na imagem]
int min_tri_sum(vector<vector<int>>&triang){
int n = triang.size();
vector<int>state(n,θ);
vector<int>new_state(n+1,0);
state[e]=triang[o][o];
for(int i=1;i<n;i++){
for(int j=θ;j<triang[i].size();j++){
if(j==0){
new_state[j]=triang[i][j]+state[i];
else if(j == triang[i].size()-1){
new_state[j]=triang[ij[j]+state[j-1];
else{
new_state[j]=triang[i][j]+ min(state[j-1], state[j]);
state =new_state
int min_path = INT_MAX;
for(int i=0;i<n;i++){
min_path = min(min_path, state[i]);
return min_path;
```

## Manuscrito, revisão necessária

Antes: [materiais\Disponiveis\RAG PAA\gabaritoprova.webp, página 1](../01-extraido/figuras/5ee2f9c93b11/p1.png)
Depois: [Markdown completo](../01-extraido/5ee2f9c93b11.md)
Método: rapidocr. Qualidade: **parcial**.

```text
[incerto] eemertoclum
[incerto] uetor
[incerto] demcotondetamanhaksn
[incerto] Putouncludtieg
[incerto] PanaumaetondedamanhoK+l
algoutmoduaide-Rnduabpastis
[incerto] A+（-）/2]Amo（fmn）/）n],qup
[incerto] menoresdloquKAotimportcnto,gundoqhupolebe demoluceab
[incerto] damadabauiaaxpumunataeoeamenteginha8aleutm
[incerto] netonavamaudntedoualooetoncdeemab
[incerto] Albim,bta poocac@
20
[incerto] QusuL3
[incerto] 3.squnoa demucome,T（n）O（f（n)),endoT（n)f（n）fun
[incerto] domeenexismonticnopenenoao
[incerto] aque
[incerto] O（f（n）)={T（n)<cf（n）1n≥no
quandop/qucllquen
[incerto] Poatanto,Um qunaT(n)portenc aoonuntoO(f(n)
(ouiguae)
```

No código, OCR pode confundir `=`, `-`, `0`, índices e parênteses. Nos manuscritos, também pode trocar palavras e fórmulas. Os candidatos de visão ficam separados e não substituem esta fonte sem revisão.
