---
id: cg-recorte-de-poligonos-sutherland-hodgman-quatro-bordas-casos-dentro-fora-lista-de-vertices
titulo: Recorte de polígonos pelo algoritmo de Sutherland-Hodgman: recorte sucessivo pelas quatro bordas, os quatro casos de cada aresta (dentro-dentro, dentro-fora, fora-fora, fora-dentro) e a lista circular de vértices
assunto: cg-02-transformacoes-projecao-e-recorte
tipo: prova
questao: AB1 de 2021.2 (questão 3) e exercícios de recorte, com a correção do monitor
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
Computação Gráfica (IC-UFAL), AB1 de 2021.2 (questão 3) e exercícios de recorte, com a correção do monitor (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Ideia:** recortar o polígono sucessivamente contra cada borda da janela (esquerda, direita, baixo, topo). A saída de uma etapa é a entrada da seguinte.

Em cada etapa percorre-se a **lista circular** de arestas $(v_1,v_2), (v_2,v_3), \dots, (v_n,v_1)$. Para a aresta de $s$ (início) a $p$ (fim):
1. **dentro → dentro:** emite $p$;
2. **dentro → fora:** emite a interseção $i$;
3. **fora → fora:** não emite nada;
4. **fora → dentro:** emite $i$ e depois $p$.

**Erro corrigido pelo monitor:** as arestas de um triângulo $\{1,2,3\}$ são $\{1,2\}$, $\{2,3\}$ e $\{3,1\}$, nesta ordem. Usar $\{1,2\}$, $\{1,3\}$, $\{2,3\}$ quebra a lista e gera vértices fora de ordem.

**Na prova**, monte uma tabela por borda com: aresta, caso (dentro/fora), vértices emitidos. A lista final é a lista de saída da última borda.

**Exemplo:** triângulo $(-5, 5)$, $(15, 5)$, $(5, 15)$ contra a janela de $(0,0)$ a $(10,10)$. Depois das quatro bordas sobra o polígono de vértices $(0,5)$, $(10,5)$, $(10,10)$, $(0,10)$ : as laterais do triângulo, $y = x + 10$ e $x + y = 20$, só passam por dentro da janela nos cantos $(0,10)$ e $(10,10)$, e o que resta é um retângulo.

O algoritmo pode gerar arestas degeneradas sobre a borda quando o polígono é côncavo e sai e volta à janela.

**Verificação:** `test_sutherland_hodgman` implementa as quatro etapas, roda o exemplo e confere os vértices e que todos ficam dentro da janela.
