---
id: grafos-euleriano-grau-par-ponte-domino
titulo: Grafos eulerianos — teorema de Euler (conexo e todos os graus pares), grafo com todos os graus pares não tem ponte, partição em ciclos, tornar euleriano com um vértice novo, dominó e K7
assunto: grafos-03-percursos-caminhos
tipo: lista
questao: 2.1, 2.3, 2.9, 2.10 (lista); 4 (prova)
resolucao: sim
fonte: Lista de exercícios de Teoria dos Grafos 2020.1, Prof. Rian Gabriel Pinheiro (IC-UFAL); 2ª avaliação de Teoria dos Grafos 2016.2, Prof. Leonardo Viana (IC-UFAL)
curso: Ciência da Computação (UFAL), Teoria dos Grafos (COMP369), 2020.1
fontes_catalogo: ufal-rian-lista-2020-1,ufal-viana-prova2-2016-2
autoria: Questões do Prof. Rian Gabriel Pinheiro (UFAL); resolução da equipe TutorON; Questões do Prof. Leonardo Viana (UFAL); resolução da equipe TutorON
licenca: Não declarada (lista, prova e slides); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista 2020.1, questões 2.1, 2.3, 2.9 e 2.10, e 2ª avaliação de 2016.2, questão 4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Teorema de Euler:** um grafo conexo tem circuito euleriano (passa por toda aresta uma vez e volta ao início) se e só se **todo vértice tem grau par**; tem trilha euleriana aberta se e só se exatamente dois vértices têm grau ímpar.

**Partição em ciclos (2.3):** com todos os graus pares, a parte com arestas tem $\delta \ge 2$ e, portanto, um ciclo; tirando-o, os graus continuam pares. Repita até acabarem as arestas.

**Sem ponte (2.9 e prova, Q4):** toda aresta $e = uv$ está num ciclo da partição; tirar $e$ não desconecta, pois o resto do ciclo liga $u$ a $v$. Outra prova: se $e$ fosse ponte, a componente de $u$ em $G - e$ teria um só vértice de grau ímpar ($u$), contra a paridade.

**Tornar euleriano (2.10):** acrescente um vértice $x$ ligado a todos os vértices de grau ímpar; eles são em número par, então $d(x)$ é par e todos os graus ficam pares. Se $G$ for desconexo, as componentes também precisam ficar ligadas a $x$ mantendo a paridade.

**Dominó (2.1):** as 21 peças que não são bombas são as arestas de $K_7$ (pontos 0 a 6). Cada vértice tem grau 6, par: há circuito euleriano, ou seja, as 21 peças formam uma fila fechada.

**Verificação:** `test_euleriano` confere com NetworkX que $K_7$ é euleriano, que grafos com todos os graus pares não têm ponte e que o vértice extra torna euleriano um grafo conexo.
