---
id: grafos-fluxo-maximo-corte-minimo-ford-fulkerson
titulo: Fluxo em redes — fluxo máximo igual ao corte mínimo, algoritmo de Ford-Fulkerson com caminhos aumentantes e grafo residual (de folgas), exemplo das 1000 iterações, caminhos disjuntos (Menger)
assunto: grafos-07-digrafos-fluxos
tipo: lista
questao: 4.6, 4.7, 4.8 (lista); 3 (prova)
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
Lista 2020.1, questões 4.6, 4.7 e 4.8, e o método pedido na 2ª avaliação de 2016.2, questão 3 (enunciados parafraseados; a rede da prova está numa figura e não foi reproduzida). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Rede:** dígrafo com capacidades $c(e) \ge 0$, fonte $s$ e sumidouro $t$. Um fluxo respeita $0 \le f(e) \le c(e)$ e conserva, em cada vértice interno, o que entra e o que sai. Um **corte** $(S, \bar S)$ com $s \in S$ e $t \notin S$ tem capacidade igual à soma das capacidades dos arcos de $S$ para $\bar S$.

**Teorema:** valor do fluxo máximo = capacidade do corte mínimo.

**Ford-Fulkerson:** enquanto houver caminho de $s$ a $t$ no **grafo residual** (de folgas: arco para frente com folga $c - f$ e arco para trás com $f$), aumente o fluxo pelo gargalo do caminho. Quando parar, os vértices alcançáveis a partir de $s$ no residual formam o lado $S$ de um corte mínimo.

**1000 iterações (4.7):** $s \to A$, $s \to B$, $A \to t$ e $B \to t$ com capacidade 1000 e $A \to B$ com 1. Alternando caminhos que usam $A \to B$ e a volta $B \to A$ do residual, cada aumento vale 1: são 2000 aumentos até o máximo de 2000. Com caminhos mais curtos (Edmonds-Karp, busca em largura) bastam 2.

**Menger (4.8):** com capacidades 1, um fluxo de valor $k$ dá $k$ caminhos de $a$ a $b$ sem arestas em comum, e todo conjunto de arestas que separa $a$ de $b$ tem pelo menos $k$ arestas.

**Verificação:** `test_fluxo` confere o fluxo máximo de 2000 do exemplo, o número de aumentos com a escolha ruim e a igualdade com o corte mínimo em redes aleatórias, com NetworkX.
