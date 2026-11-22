---
id: redes-roteamento-link-state-vetor-de-distancia
titulo: Algoritmos de roteamento: objetivo, Link State (Dijkstra, OSPF) × Vetor de Distância (Bellman-Ford, RIP), mensagens, convergência, contagem ao infinito
assunto: redes-07-roteamento
tipo: prova
questao: AB2 2017 Q4; AB2 2020.1 Q5; prova 2020.1; reposição AB2 2020.1 Q1; final 2020.1 Q6
resolucao: sim
fonte: Provas de 2017 e 2020.1 de Redes de Computadores 1, Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Redes de Computadores 1 (COMP — Prof. Leandro Melo de Sales); provas de 2017 e 2020.1
fontes_catalogo: ufal-leandro-provas-redes
autoria: Questões do Prof. Leandro Melo de Sales (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), AB2 2017 Q4; AB2 2020.1 Q5; prova 2020.1; reposição AB2 2020.1 Q1; final 2020.1 Q6 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Objetivo:** achar, para cada destino, um **bom caminho** (de menor custo) pela rede de roteadores, um grafo com custos nos enlaces. O resultado preenche a **tabela de repasse** de cada roteador.

**Link State (estado de enlace), ex.: OSPF.** Cada roteador anuncia por **inundação** o custo dos seus enlaces a **todos** os roteadores. Assim, todos conhecem a topologia inteira e cada um roda **Dijkstra** sozinho. É algoritmo **global**: com $n$ roteadores, Dijkstra simples custa $O(n^2)$ e a inundação gera muitas mensagens. Converge rápido, e um erro de um roteador afeta só o cálculo dele (até certo ponto).

**Vetor de Distância, ex.: RIP.** Cada roteador conhece só os vizinhos e o custo até eles. Periodicamente (ou quando algo muda), manda aos **vizinhos** o seu vetor de distâncias e atualiza pela equação de **Bellman-Ford**: $D_x(y) = \min_v \{ c(x,v) + D_v(y) \}$ (o custo de x a y é o menor, entre os vizinhos v, de ir até v e depois de v a y). É **distribuído, iterativo e assíncrono**, e troca poucas mensagens. Converge mais devagar. Uma boa notícia (custo que cai) se espalha rápido; uma má (enlace que piora ou cai) pode causar **contagem ao infinito**, com dois roteadores apontando um para o outro. O *poisoned reverse* (rota envenenada) resolve laços entre dois nós, mas não os maiores.

**Ponderações:** LS troca mais mensagens e exige mais memória e processamento, mas converge melhor. DV é mais leve, mas sofre com laços temporários e propaga erros (um roteador que anuncia custo errado contamina os outros).

**Verificação:** `test_link_state_e_vetor_de_distancia` roda Dijkstra e Bellman-Ford distribuído (rodadas de troca de vetores) num grafo de 6 roteadores, obtém as mesmas distâncias e mostra a contagem ao infinito num caminho de 3 nós quando um enlace cai.
