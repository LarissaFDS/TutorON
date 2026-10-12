# 23950cced864-q5-5

Fonte: materiais\Disponiveis\RAG PAA\prova_2(1).pdf | página(s): 1

Questão 5 [2 ponto):
Considere o seguinte algoritmo gulosos para o CAIXEIRO VIAJANTE. Mostre que ele não é exato, isto é, não garante
retornar a solução ótima. Para isso use um contra-exemplo.
Algoritmo 1 (Algoritmo do vizinho mais próximo)
1. Inicialize todos os vértices como não visitados.
2. Selecione um vértice arbitrário, defina-o como o vértice atual u. Marque u como visitado.
3. Descubra a aresta mais curta conectando o vértice atual u e um vértice não visitado v.
4. Defina v como o vértice atual u. Marque v como visitado.
5. Se todos os vértices do domínio forem visitados, então termine. Caso contrário, vá para o passo 3.
