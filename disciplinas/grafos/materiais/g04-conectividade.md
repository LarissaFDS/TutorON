---
id: grafos-conectividade-kappa-lambda-delta-pontes
titulo: Conectividade — κ(G) ≤ λ(G) ≤ δ(G) (conexidade de vértices, de arestas e grau mínimo), pontes e vértices de corte (articulações), exemplos em que as desigualdades são estritas
assunto: grafos-02-arvores-conectividade
tipo: lista
questao: 1.9
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
Lista 2020.1, questão 1.9 (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Definições:** $\kappa(G)$ (kappa, conexidade) é o menor número de vértices cuja remoção desconecta $G$ ou deixa um só vértice; $\lambda(G)$ (lambda, conexidade por arestas) é o menor número de arestas cuja remoção desconecta $G$; $\delta(G)$ é o grau mínimo. **Ponte** é uma aresta que desconecta sozinha; **vértice de corte** (articulação) é um vértice que desconecta sozinho.

**$\lambda \le \delta$:** remova as $\delta$ arestas de um vértice de grau mínimo; ele fica isolado.

**$\kappa \le \lambda$:** seja $F$ um corte mínimo de arestas, $|F| = \lambda$. Remova, para cada aresta de $F$, uma de suas pontas, escolhida de modo a não apagar todo um lado do corte. São no máximo $\lambda$ vértices, as arestas de $F$ somem e o grafo se desconecta (ou sobra um só vértice). Logo $\kappa \le \lambda$.

**Desigualdades estritas:** dois $K_4$ que compartilham um vértice: $\delta = 3$, $\lambda = 3$ e $\kappa = 1$ (o vértice comum é articulação). Dois $K_4$ disjuntos ligados por uma aresta: $\kappa = \lambda = 1 < \delta = 3$ (a aresta é ponte).

Erros comuns: confundir corte de vértices com corte de arestas; achar que grau mínimo alto garante conexidade alta.

**Verificação:** `test_conectividade` calcula $\kappa$, $\lambda$ e $\delta$ com NetworkX nos exemplos e em grafos aleatórios e confere $\kappa \le \lambda \le \delta$.
