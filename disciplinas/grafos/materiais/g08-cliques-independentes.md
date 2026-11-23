---
id: grafos-cliques-independentes-ramsey
titulo: Cliques e conjuntos independentes (estáveis) — cliques maximais com tamanhos diferentes, clique de G é independente do complemento, dois vértices de mesmo grau, R(3,3) = 6, C5 sem clique nem independente de tamanho 3
assunto: grafos-04-emparelhamento-estabilidade
tipo: lista
questao: 1.10, 3.1, 3.2, 3.3, 3.4, 3.8
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
Lista 2020.1, questões 1.10, 3.1, 3.2, 3.3, 3.4 e 3.8 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Clique**: vértices dois a dois adjacentes; **independente** (estável): dois a dois não adjacentes. $\omega(G)$ é a maior clique e $\alpha(G)$ o maior independente.

**3.2:** cliques **maximais** (não ampliáveis) podem ter tamanhos diferentes: num triângulo com uma aresta pendurada, a aresta pendurada é clique maximal de tamanho 2 e o triângulo, de tamanho 3.

**3.3:** $S$ é clique em $G$ se e só se é independente no complemento $\bar G$; logo $\omega(G) = \alpha(\bar G)$, e um algoritmo para um problema resolve o outro passando ao complemento.

**3.8:** uma clique e um independente têm no máximo um vértice comum: dois vértices comuns seriam adjacentes e não adjacentes.

**3.1:** num grafo simples com $n \ge 2$ vértices os graus estão em $\{0, \dots, n-1\}$, mas 0 e $n-1$ não aparecem juntos. Sobram $n-1$ valores para $n$ vértices: pela casa dos pombos, dois têm o mesmo grau.

**3.4 e 1.10 (Ramsey):** todo grafo com **pelo menos 6** vértices tem triângulo ou independente de tamanho 3. Um vértice $v$ tem pelo menos 3 vizinhos ou 3 não vizinhos; se tem 3 vizinhos, ou dois deles são adjacentes (triângulo com $v$) ou os três são independentes; o outro caso é simétrico. Com 5 vértices falha: no ciclo $C_5$, $\omega = \alpha = 2$.

**Verificação:** `test_cliques_e_ramsey` confere $\omega(C_5) = \alpha(C_5) = 2$, percorre as $2^{15}$ colorações das arestas de $K_6$ (todas têm triângulo de uma cor só) e testa $\omega(G) = \alpha(\bar G)$ em grafos aleatórios.
