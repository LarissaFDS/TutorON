---
id: grafos-coloracao-vertices-delta-mais-um-petersen
titulo: Coloração de vértices — número cromático, coloração gulosa com no máximo Δ+1 cores, grades e árvores bicoloríveis (sem ciclo ímpar), grafo de Petersen tem número cromático 3
assunto: grafos-05-coloracao
tipo: lista
questao: 3.7, 3.10 (lista); 2 (prova)
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
Lista 2020.1, questões 3.7 e 3.10, e 2ª avaliação de 2016.2, questão 2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Coloração própria:** vizinhos com cores diferentes; $\chi(G)$ (qui de G, número cromático) é o menor número de cores. Sempre $\chi(G) \ge \omega(G)$, o tamanho da maior clique.

**$\Delta + 1$ cores (3.7):** pinte os vértices em qualquer ordem com a menor cor não usada pelos vizinhos já pintados. Cada vértice tem no máximo $\Delta$ vizinhos, então uma das cores $1, \dots, \Delta+1$ está livre. (Brooks melhora para $\Delta$, exceto grafos completos e ciclos ímpares.)

**Grades (3.10):** pinte $(i,j)$ pela paridade de $i+j$; vizinhos mudam uma coordenada em 1 e trocam de paridade. Um grafo é 2-colorível se e só se **não tem ciclo ímpar**.

**Petersen (prova, Q2c):** tem ciclos de 5 vértices, então $\chi \ge 3$; uma 3-coloração existe (pinte o ciclo externo com 1, 2, 1, 2, 3 e dê a cada vértice interno uma cor livre). Logo $\chi = 3$.

A questão 4.4 (mapa do Brasil) não tem resolução aqui: o argumento depende da lista de fronteiras entre estados, que não foi conferida.

**Verificação:** `test_coloracao_vertices` calcula por força bruta o número cromático do Petersen (3), confere o guloso com no máximo $\Delta+1$ cores em grafos aleatórios e a bicoloração de grades com NetworkX.
