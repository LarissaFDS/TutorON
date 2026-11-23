---
id: grafos-arvores-conexo-minimo-ciclo-bicoloracao
titulo: Árvores — todo grafo conexo com o mínimo de arestas é árvore (n−1 arestas), grau mínimo pelo menos 2 implica ciclo, passeio contém caminho, toda árvore é 2-colorível
assunto: grafos-02-arvores-conectividade
tipo: lista
questao: 1.1, 1.7, 1.8, 3.6
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
Lista 2020.1, questões 1.1, 1.7, 1.8 e 3.6 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Árvore** = grafo conexo e acíclico; com $n$ vértices tem exatamente $n-1$ arestas.

**1.1 Conexo com o mínimo de arestas é árvore.** Suponha $G$ conexo com o menor número possível de arestas e com um ciclo $C$. Tirando uma aresta $e$ de $C$, as pontas de $e$ continuam ligadas pelo resto do ciclo: $G - e$ é conexo com menos arestas, contradição. (É o "por que não pode haver ciclo" que faltava numa resolução da turma: afirmar $|E| = n-1$ sem provar é circular.)

**1.7 Passeio → caminho.** Pegue um $(u,v)$-passeio de comprimento mínimo. Se repetisse um vértice $w$, o trecho entre as duas visitas a $w$ poderia ser cortado. Logo não repete vértices: é caminho.

**1.8 Grau mínimo $\delta \ge 2$ implica ciclo.** Tome um caminho maximal $v_0 v_1 \dots v_k$. Como $d(v_k) \ge 2$, $v_k$ tem outro vizinho além de $v_{k-1}$; ele está no caminho (senão o caminho cresceria) e fecha um ciclo.

**3.6 Árvores são 2-coloríveis.** Escolha uma raiz e pinte cada vértice pela paridade da distância à raiz; as pontas de uma aresta têm distâncias que diferem de 1. (Árvores não têm ciclos, muito menos ciclos ímpares.)

**Verificação:** `test_arvores` confere com NetworkX que árvores aleatórias têm $n-1$ arestas e são bipartidas, que grafos com $\delta \ge 2$ têm ciclo e que tirar uma aresta de ciclo mantém a conexidade.
