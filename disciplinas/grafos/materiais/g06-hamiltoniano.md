---
id: grafos-hamiltoniano-petersen-kij-caixeiro
titulo: Ciclos hamiltonianos — grafo de Petersen não é hamiltoniano, K(i,j) só tem ciclo hamiltoniano se i = j, caixeiro-viajante com desigualdade triangular e a árvore geradora mínima (2·w(T))
assunto: grafos-03-percursos-caminhos
tipo: lista
questao: 2.4, 2.5, 2.8
resolucao: sim
fonte: Lista de exercícios de Teoria dos Grafos 2020.1, Prof. Rian Gabriel Pinheiro (IC-UFAL)
curso: Ciência da Computação (UFAL), Teoria dos Grafos (COMP369), 2020.1
fontes_catalogo: ufal-rian-lista-2020-1
autoria: Questões do Prof. Rian Gabriel Pinheiro (UFAL); resolução da equipe TutorON
licenca: Não declarada (lista, prova e slides); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista 2020.1, questões 2.4, 2.5 e 2.8 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Ciclo hamiltoniano:** passa por todo **vértice** uma vez (no euleriano é por toda aresta). Não há condição simples de "se e só se"; decidir se existe é NP-completo.

**$K_{i,j}$ (2.5):** um ciclo num bipartido alterna os lados e usa tantos vértices de um lado quanto do outro. Para passar por todos, precisa $i = j \ge 2$; nesse caso $a_1 b_1 a_2 b_2 \dots a_i b_i a_1$ serve.

**Petersen (2.4):** 10 vértices, 3-regular: ciclo externo $u_0 \dots u_4$, estrela interna ($v_i$ ligado a $v_{i+2}$) e raios $u_i v_i$. Um ciclo hamiltoniano cruza entre as partes por um número par de raios. Com 2 raios, cada parte seria percorrida por um caminho hamiltoniano entre as pontas dos raios, e as distâncias no ciclo e na estrela não combinam; com 4 raios, a parte externa se quebra em pedaços que obrigam algum vértice a usar 3 arestas. Em todos os casos há contradição.

**Caixeiro e AGM (2.8):** tirando uma aresta do ciclo ótimo $C^*$ obtém-se uma árvore geradora, então $w(T) \le w(C^*)$. Percorrer $T$ em profundidade usa cada aresta duas vezes (custo $2w(T)$); pulando vértices repetidos, a desigualdade triangular só diminui o custo. Assim há ciclo hamiltoniano de custo $\le 2w(T)$, e $w(C^*) \le 2w(T)$.

**Verificação:** `test_hamiltoniano` procura por força bruta ciclo hamiltoniano no Petersen (não há), em $K_{3,3}$ (há) e $K_{2,3}$ (não há), e confere o atalho pela árvore em grafos com pesos euclidianos.
