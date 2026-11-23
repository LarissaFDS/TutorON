---
id: grafos-isomorfismo-onze-grafos-quatro-vertices
titulo: Isomorfismo — por que há exatamente 11 grafos simples não isomorfos com 4 vértices, invariantes (número de arestas, sequência de graus) e como não contar o mesmo grafo duas vezes
assunto: grafos-01-conceitos
tipo: lista
questao: 1.3
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
Lista 2020.1, questão 1.3 (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Isomorfismo:** $G \cong H$ se existe uma bijeção $f: V(G) \to V(H)$ que preserva adjacência ($uv \in E(G) \iff f(u)f(v) \in E(H)$). Para mostrar que dois grafos **não** são isomorfos basta um **invariante** diferente: número de arestas, sequência de graus, número de componentes, presença de triângulo.

**Os 11 grafos com 4 vértices, por número de arestas $m$:**

| $m$ | grafos | quantos |
|---|---|---|
| 0 | vazio | 1 |
| 1 | uma aresta | 1 |
| 2 | duas arestas com ponta comum; duas arestas disjuntas | 2 |
| 3 | triângulo e vértice isolado; caminho $P_4$; estrela $K_{1,3}$ | 3 |
| 4 | ciclo $C_4$; triângulo com uma aresta pendurada | 2 |
| 5 | $K_4$ menos uma aresta | 1 |
| 6 | $K_4$ | 1 |

Total: $1+1+2+3+2+1+1 = 11$. A tabela é simétrica porque o complemento de um grafo com $m$ arestas tem $6-m$.

Erro comum (visto em resoluções da turma): listar como diferentes dois desenhos do mesmo grafo. Antes de contar um grafo novo, compare número de arestas e sequência de graus; com 4 vértices esses dois invariantes já separam todos os casos.

**Verificação:** `test_onze_grafos_de_quatro_vertices` gera os $2^6 = 64$ grafos rotulados, agrupa por isomorfismo com NetworkX e obtém 11 classes, com 1, 1, 2, 3, 2, 1, 1 por número de arestas.
