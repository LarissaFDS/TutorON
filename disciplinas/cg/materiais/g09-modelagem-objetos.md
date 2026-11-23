---
id: cg-modelagem-de-objetos-representacao-por-vertices-faces-winged-edge-csg-decomposicao-quadtree-octree
titulo: Modelagem e representação de objetos: malhas por vértices e faces, winged-edge, geometria sólida construtiva (CSG), representação por decomposição espacial (quadtree e octree, nós cheio, vazio e parcial)
assunto: cg-03-modelagem-iluminacao-e-textura
tipo: prova
questao: aula de Modelagem de Objetos, AB2 de 2014.1 (questões 2 e 7) e AB2 de 2021.2 (questão 2)
resolucao: sim
fonte: Exercícios e provas de Computação Gráfica do Prof. Marcelo Costa Oliveira (IC-UFAL)
curso: Ciência da Computação (UFAL), COMP381 Computação Gráfica; aulas de 2012 a 2017 e provas de 2014 e 2021.2 (Prof. Marcelo Costa Oliveira)
fontes_catalogo: ufal-marcelo-aulas-cg,ufal-cg-provas-exercicios
autoria: Questões do Prof. Marcelo Costa Oliveira (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Gráfica (IC-UFAL), aula de Modelagem de Objetos, AB2 de 2014.1 (questões 2 e 7) e AB2 de 2021.2 (questão 2) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Para que servem estruturas de dados especiais:** guardar a **geometria** (posições) e a **topologia** (quem é vizinho de quem) do objeto, com consistência e rapidez para desenhar, obter área e volume e detectar colisões.

**Representações:**
- **baseada em vértices:** lista de coordenadas; as faces citam índices de vértices;
- **baseada em faces (malha poligonal):** lista de faces com seus vértices; simples, mas achar vizinhos é caro;
- **winged-edge:** cada aresta guarda seus 2 vértices, as 2 faces e as arestas vizinhas; responde rápido a consultas de adjacência;
- **geometria sólida construtiva (CSG):** árvore de operações booleanas (união, interseção, diferença) sobre primitivas (cubo, esfera, cilindro);
- **por decomposição espacial:** divide o espaço em células e marca as ocupadas; a representação é aproximada, mas consultas de ocupação são diretas.

**Quadtree (2D):** envolve o objeto num quadrado e divide-o em 4 quadrantes iguais. Cada quadrante é **cheio** (todo ocupado), **vazio** ou **parcial** (cheio-vazio). Só os parciais são subdivididos de novo, até a resolução desejada. A **octree** faz o mesmo em 3D com 8 octantes.

**Árvore na prova:** a raiz é o cubo inteiro; cada nó parcial tem 8 filhos na ordem de numeração dos octantes dada pelo cubo de referência; folhas são cheias ou vazias. Indique a profundidade de cada folha.

Uma quadtree de uma imagem $2^n \times 2^n$ tem profundidade máxima $n$.

**Verificação:** `test_quadtree` constrói a quadtree de uma imagem binária $4 \times 4$ e confere a classificação cheio, vazio e parcial e a profundidade máxima 2.
