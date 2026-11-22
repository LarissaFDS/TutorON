---
id: grafos-arvore-geradora-minima-caminho-minimo
titulo: Árvore geradora mínima (Kruskal e Prim) e caminho mínimo (Dijkstra) — ideia, exemplo pequeno conferido e por que Dijkstra exige pesos não negativos
assunto: grafos-02-arvores-conectividade
tipo: lista
questao: 2.8 (lista) e aulas de árvores e de busca
resolucao: sim
fonte: Lista de exercícios de Teoria dos Grafos 2020.1, Prof. Rian Gabriel Pinheiro (IC-UFAL); Aulas de Teoria dos Grafos da Profa. Patrícia D. L. Machado (DSC-UFCG, 2012), usadas pela turma
curso: Ciência da Computação (UFAL), Teoria dos Grafos (COMP369), 2020.1
fontes_catalogo: ufal-rian-lista-2020-1,ufcg-machado-slides-grafos
autoria: Questões do Prof. Rian Gabriel Pinheiro (UFAL); resolução da equipe TutorON; Tópicos das aulas da Profa. Patrícia Machado (UFCG); exemplo da equipe TutorON
licenca: Não declarada (lista, prova e slides); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Tópicos das aulas de árvores e de algoritmos de busca da Profa. Patrícia Machado (UFCG), usadas pela turma, e da questão 2.8 da lista 2020.1, que usa a árvore geradora mínima. O exemplo é da equipe TutorON. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Árvore geradora mínima (AGM):** árvore que liga todos os vértices com a menor soma de pesos.
- **Kruskal:** ordene as arestas por peso e aceite cada uma que não forme ciclo com as já aceitas.
- **Prim:** comece num vértice e acrescente sempre a aresta mais leve que sai da árvore atual.

**Caminho mínimo (Dijkstra):** a partir de $s$, fixe repetidamente o vértice ainda não fixado com menor distância provisória e atualize os vizinhos: $d(v) \leftarrow \min(d(v),\ d(u) + w(uv))$. Exige pesos **não negativos**: com peso negativo, um vértice fixado cedo pode ganhar depois um caminho menor (use Bellman-Ford).

**Exemplo:** vértices A, B, C, D com pesos AB = 1, BC = 2, AC = 4, CD = 1, BD = 5. Kruskal aceita AB (1), CD (1) e BC (2) e rejeita AC e BD: AGM de peso 4. Dijkstra a partir de A: B = 1, C = 3 (por B), D = 4 (por B e C).

**Verificação:** `test_agm_e_dijkstra` confere o exemplo com `minimum_spanning_tree` e `dijkstra_path_length` do NetworkX e mostra um grafo com peso negativo em que fixar o vértice cedo dá distância errada.
