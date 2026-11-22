---
id: grafos-graus-aperto-de-maos-kn-bipartido
titulo: Graus e número de arestas — soma dos graus é 2|E| (aperto de mãos), vértices de grau ímpar são em número par, arestas de Kn e de Km,n, bipartido simples tem no máximo n²/4 arestas
assunto: grafos-01-conceitos
tipo: lista
questao: 1.2, 1.4, 1.5, 1.6
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
Lista 2020.1, questões 1.2, 1.4, 1.5 e 1.6 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Soma dos graus:** $\sum_{v \in V} d(v) = 2|E|$ (em palavras: somando os graus de todos os vértices, cada aresta é contada duas vezes, uma em cada ponta; um laço conta 2 no seu vértice).

**Vértices de grau ímpar:** separe a soma em graus pares e ímpares. A parte dos pares é par e o total $2|E|$ é par, então a soma dos graus ímpares também é par; uma soma de números ímpares só é par com uma quantidade **par** de parcelas.

**Grafo completo:** em $K_n$ cada vértice tem grau $n-1$, então $|E(K_n)| = \dfrac{n(n-1)}{2} = \binom{n}{2}$ (uma aresta para cada par de vértices). $K_5$ tem 10 arestas.

**Bipartido completo:** em $K_{m,n}$ cada um dos $m$ vértices de um lado liga-se aos $n$ do outro: $|E| = mn$.

**Bipartido simples com $n$ vértices:** com partes de tamanhos $a$ e $n-a$ há no máximo $a(n-a)$ arestas, e $a(n-a) \le n^2/4$ porque $n^2/4 - a(n-a) = (a - n/2)^2 \ge 0$.

Erros comuns: justificar o máximo em $a = n/2$ só dizendo que valores extremos dão produto pequeno (falta o argumento do quadrado); esquecer que a soma dos graus vale também para multigrafos.

**Verificação:** `test_graus_e_arestas` confere a soma dos graus e a paridade em grafos aleatórios, $|E(K_n)|$ e $|E(K_{m,n})|$ com NetworkX e o máximo de arestas de bipartidos até $n = 12$.
