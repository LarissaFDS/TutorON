---
id: grafos-pratica1-robo-grid-dijkstra
titulo: Prática 1, cenário 3 — robô de armazém em grid 10 × 15 com obstáculos e piso difícil: montar o grafo do mapa e usar Dijkstra; custo mínimo 26 de S a G
assunto: grafos-03-percursos-caminhos
tipo: lista
questao: cenário 3
resolucao: sim
fonte: Prática 1 - Grafos (caminho mínimo), Teoria dos Grafos ECOM033, IC-UFAL, com os arquivos de entrada graph1.txt, graph2.txt e grid_example.txt
curso: Engenharia de Computação (UFAL), Teoria dos Grafos (ECOM033)
fontes_catalogo: ufal-ecom033-pratica1-caminho-minimo
autoria: Enunciado e arquivos de entrada: Prática 1 da disciplina ECOM033 (IC-UFAL; professor não identificado no arquivo), parafraseados pela equipe TutorON; resolução da equipe TutorON
licenca: Não declarada (atividade da disciplina); paráfrase, PDF e arquivos de entrada não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Prática 1 de Teoria dos Grafos (ECOM033, IC-UFAL), cenário 3. Enunciado parafraseado. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor; a prática pede que o aluno implemente e compare com o pseudocódigo da aula, então aqui ficam a escolha do algoritmo, o raciocínio e os números para conferir.

**Problema.** Um robô vai de S (recarga) a G (coleta) num grid. Célula livre custa 1, piso difícil (`~`) custa 3, obstáculo (`#`) não pode ser atravessado; movimento em 4 direções. A primeira linha do arquivo traz linhas e colunas. (O enunciado diz `=` para célula livre, mas o arquivo de exemplo usa `.`.)

**Montar o grafo.** Cada célula que não é obstáculo vira vértice; há arco de uma célula para cada vizinha livre (norte, sul, leste, oeste) com o **custo de entrar** na vizinha. Assim o grafo é direcionado (entrar em `~` custa 3, sair dele para `.` custa 1).

**Algoritmo: Dijkstra.** Pesos positivos e uma única origem: Dijkstra com fila de prioridade, O((V + E) log V), é o mais eficiente. Bellman-Ford e Floyd-Warshall resolveriam, mas são bem mais lentos num grid grande e resolvem outros problemas (pesos negativos, todos os pares). Com custo uniforme, BFS bastaria; com `~`, não.

**Com o arquivo de exemplo** (10 × 15, S na linha 3 coluna 0 e G na linha 3 coluna 8, contando de 0): custo mínimo **26**, com 22 movimentos. O robô desce pela coluna 0, segue pela última linha e sobe pelas colunas 7 a 9, entrando em duas células `~` (22 movimentos + 2 × 2 extras = 26); o caminho direto para a direita é bloqueado pela parede da coluna 2. Pode haver mais de um caminho com custo 26; o custo é o que se confere.

**Verificação:** `test_pratica1_robo_grid_dijkstra` monta o grafo do grid e confere com `networkx.dijkstra_path_length` e com um Dijkstra próprio com `heapq`.
