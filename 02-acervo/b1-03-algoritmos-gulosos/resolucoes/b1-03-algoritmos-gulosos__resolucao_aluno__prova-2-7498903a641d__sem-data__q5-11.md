# 7498903a641d-q5-11

Fonte: materiais\Disponiveis\RAG PAA\prova_2.pdf | página(s): 1

Questao 5 [2 ponto]: 
garantemretornarasolucao6tima.
Algoritmo1(Algoritmo dovizinhomaisproximo)
1.Inicializetodos osvertices comonaovisitados.
2. Selecione um vertice arbitrario, defina-o como o vertice atual u. Marque u como visitado.
3. Descubra a aresta mais curta conectando o vertice atual u e um vertice nao visitado v.
4.Definavcomoovérticeatualu.Marquevcomovisitado.
5. Se todos os vertices do dominio forem visitados, entao termine. Caso contrario, va para o passo 3.
Algoritmo2(Algoritmodainsercaomaisbarata)
1.Crieum ciclo Ccom tresvertices quaisquer.
2. Escolha um vertice k qualquer fora de C.
3.Encontre uma aresta(i,j) ∈ C tal que dik + dkj-dij é minimo.
4.Adicione k a C,remova a aresta (i,j)e adicione as arestas (i,k)e (k,j).
5.Se C contiver todos os nos,pare.Caso contrario,va para 2.
Questao6[2pontos]:
Um ladrao entra em uma loja e ve um conjunto I de n itens, I = {a1,a2....,an}. Cada item tem um peso associado
w; e um valor v. Idealmente, o ladrao gostaria de roubar tudo para obter o maximo beneficio. No entanto, ha muito
que ele pode carrcgar. O ladrao tem uma mochila com capacidade K. O ladrao agora tem que determinar quais itens
alguma parte de um item (por exemplo,0,4 w; de ai)e deixar a parte restante.Issoé chamado de Problema
da Mochila Fracionada.Seja A C I o subeonjunto de itens queoladrao rouba.Elabore um algoritmo guloso
O(n log n) para encontrar o subconjunto A tal que Za;eA w; < K e Za;eA v; é maximo.
2. Suponha que os itens so possam ser retirados como um todo, ou seja, o ladrao so pode pegar ou deixar um item;
Seu algoritmo guloso para a versao fracionaria do problema (pergunta anterior) ainda encontra uma solucao
6tima?Justifiquesuaresposta.


2. Suponha que os itens só possam ser retirados como um todo, ou seja, o ladrão só pode pegar ou deixar um,itcm; 
ele não pode pegar uma fração de um item. Isso é chamado de Problema da Mochila Binária (ou Mochila 0-1 ). 
Seu algoritmo guloso para a versão fracionária do problema (pergunta anterior) ainda encontra uma :,oluçào 
ótima? Justifique sua resposta. 
J
