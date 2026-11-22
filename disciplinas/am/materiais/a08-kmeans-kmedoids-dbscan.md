---
id: am-agrupamento-k-means-k-medoids-dbscan-algoritmo-passo-a-passo
titulo: Descreva um algoritmo não supervisionado: k-means, k-medoids ou DBSCAN (passos, parâmetros, vantagens e limitações)
assunto: am-03-agrupamento-e-associacao
tipo: prova
questao: AB2 Q1
resolucao: sim
fonte: Provas de Aprendizagem de Máquina do Prof. Aydano Machado (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Aprendizagem de Máquina (COMP390); provas AB1 e AB2 (uma delas de 2021.1)
fontes_catalogo: ufal-aydano-provas-am
autoria: Questões do Prof. Aydano Machado (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), AB2 Q1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Agrupamento:** organizar $N$ objetos em grupos de objetos **semelhantes**, sem grupos definidos antes. Usa uma **matriz de dissimilaridade** $d(i, j) \ge 0$, com $d(i, i) = 0$ e $d(i, j) = d(j, i)$.

**k-means** (entrada: $N$ objetos e o número $k$; saída: $k$ grupos):
1. escolha $k$ **centroides** iniciais (aleatórios ou k-means++);
2. **atribua** cada objeto ao centroide mais próximo;
3. **recalcule** cada centroide como a **média** dos objetos do grupo;
4. repita 2 e 3 até as atribuições não mudarem.
Minimiza a soma dos quadrados das distâncias aos centroides, $\sum_k \sum_{x \in C_k} \lVert x - \mu_k \rVert^2$. Converge para um **mínimo local** (rode com várias inicializações); bom desempenho médio; ruim para grupos **não convexos** e sensível a **ruído e outliers** (a média é puxada).

**k-medoids** (PAM): igual, mas o representante é um **medoide**, um **objeto real** do grupo que minimiza a soma das distâncias aos demais. Troca medoides por não medoides enquanto o custo total cai. Mais **robusto a ruído**; mais caro; $k$ ainda é parâmetro.

**DBSCAN** (baseado em **densidade**), parâmetros **raio** $\varepsilon$ e **mínimo de pontos** `minPts`:
- **ponto central:** tem ao menos `minPts` vizinhos no raio $\varepsilon$;
- **ponto de borda:** está no raio de um central sem ser central;
- **ruído:** nem um nem outro.
Grupos são pontos centrais **alcançáveis por densidade** e suas bordas. **Não precisa de $k$**, acha grupos de **forma arbitrária** e marca ruído; sofre com densidades muito diferentes.

**Verificação:** `test_kmeans_passo_a_passo` implementa o k-means em NumPy, confere que a soma dos quadrados nunca sobe entre iterações e que o resultado coincide com o `KMeans` do scikit-learn com os mesmos centroides iniciais; o DBSCAN marca como ruído (-1) um ponto isolado.
