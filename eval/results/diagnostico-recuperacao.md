# Diagnóstico de recuperação

Índice `04-rag/indice.json`: 53 blocos, modo hibrido. Consulta desta execução: SÓ LÉXICA (bge-m3 indisponível nesta máquina).

Relevância por assunto: o bloco é do mesmo assunto da pergunta (b2-04 para PD etc.). É um critério grosseiro: um bloco do assunto certo ainda pode tratar de outro problema.

### A1-mochila-01 (pd)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L6.pdf | p. 5, 6 — Oito damas por programação de restrições. | b2-05-transformacao-de-problemas | 0.0180 | 3.49 | – | NÃO |
| 2 | c05_lista2_q9_asterisco_resolucao.md | p. não informada na transcrição — Quantos asteriscos ASTERISCO(n) imprime? | b1-01-corretude-complexidade | 0.0177 | 3.39 | – | NÃO |
| 3 | PAA_L6.pdf | p. 3, 4 — Programação linear de duas rações. | b2-05-transformacao-de-problemas | 0.0175 | 3.06 | – | NÃO |
| 4 | PAA_L5.pdf | p. 4, 5 — Maior substring comum de x e y. | b2-04-programacao-dinamica | 0.0172 | 2.54 | – | sim |

### A2-subset-sum (pd)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L5.pdf | p. 7, 8 — SUBSET SUM para inteiros positivos e alvo t>=0. | b2-04-programacao-dinamica | 0.0180 | 20.23 | – | sim |
| 2 | PAA_L7.pdf | p. 6, 7, 8 — TRI-PARTIÇÃO em três grupos de mesma soma: interpretação do  | b2-06-np-completude | 0.0177 | 12.28 | – | NÃO |
| 3 | PAA_L7.pdf | p. 9, 10 — CONJUNTO INCIDENTE (Hitting Set). | b2-06-np-completude | 0.0175 | 11.46 | – | NÃO |
| 4 | PAA_L6.pdf | p. 4, 5 — Troco mínimo como programa linear inteiro. | b2-05-transformacao-de-problemas | 0.0172 | 10.55 | – | NÃO |

### A3-substring-comum (pd)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L5.pdf | p. 4, 5 — Maior substring comum de x e y. | b2-04-programacao-dinamica | 0.0180 | 20.40 | – | sim |
| 2 | PAA_L5.pdf | p. 5, 6 — Custo mínimo de cortar uma string de comprimento n nas posiç | b2-04-programacao-dinamica | 0.0177 | 8.70 | – | sim |
| 3 | PAA_L2.pdf | p. 7 — Encontrar dois elementos distintos de S cuja soma é x em tem | b1-01-corretude-complexidade | 0.0175 | 6.30 | – | NÃO |
| 4 | PAA_L3.pdf | p. 6, 7 — Hanoi com quatro pinos: analisar a estratégia apresentada, n | b1-02-divisao-e-conquista | 0.0172 | 5.65 | – | NÃO |

### P1-robo-matriz-facil (pd)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L5.pdf | p. 2 — Robô coletor de moedas em matriz de r linhas e c colunas, mo | b2-04-programacao-dinamica | 0.0180 | 7.33 | – | sim |
| 2 | PAA_L6.pdf | p. 7 — Clique máxima como programa linear inteiro binário. | b2-05-transformacao-de-problemas | 0.0177 | 5.21 | – | NÃO |
| 3 | PAA_L1.pdf | p. 9, 10 — Corretude de Horner para P(x)=sum(A[j]x^j,j=0..n). | b1-01-corretude-complexidade | 0.0175 | 4.19 | – | NÃO |
| 4 | PAA_L5.pdf | p. 2, 3 — Caminho mais longo em um DAG, medido em número de arestas. | b2-04-programacao-dinamica | 0.0172 | 2.16 | – | sim |

### P2-troco-guloso-esquema (guloso)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L6.pdf | p. 4, 5 — Troco mínimo como programa linear inteiro. | b2-05-transformacao-de-problemas | 0.0180 | 11.10 | – | NÃO |
| 2 | PAA_L5.pdf | p. 7, 8 — SUBSET SUM para inteiros positivos e alvo t>=0. | b2-04-programacao-dinamica | 0.0177 | 3.87 | – | NÃO |
| 3 | PAA_L3.pdf | p. 7, 8 — Pico de vetor unimodal de valores distintos. | b1-02-divisao-e-conquista | 0.0175 | 3.61 | – | NÃO |
| 4 | PAA_L5.pdf | p. 2 — Robô coletor de moedas em matriz de r linhas e c colunas, mo | b2-04-programacao-dinamica | 0.0172 | 3.14 | – | NÃO |

### P3-troco-pd (pd)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L6.pdf | p. 4, 5 — Troco mínimo como programa linear inteiro. | b2-05-transformacao-de-problemas | 0.0180 | 5.75 | – | NÃO |
| 2 | PAA_L6.pdf | p. 3, 4 — Programação linear de duas rações. | b2-05-transformacao-de-problemas | 0.0177 | 4.69 | – | NÃO |
| 3 | PAA_L4.pdf | p. 3 — Agendamento do maior número de intervalos compatíveis. | b1-03-algoritmos-gulosos | 0.0175 | 3.82 | – | NÃO |
| 4 | PAA_L6.pdf | p. 5, 6 — Oito damas por programação de restrições. | b2-05-transformacao-de-problemas | 0.0172 | 3.49 | – | NÃO |

### P4-lis (pd)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L5.pdf | p. 4 — Subsequência contígua de soma máxima com subsequência vazia  | b2-04-programacao-dinamica | 0.0180 | 6.66 | – | sim |
| 2 | PAA_L3.pdf | p. 7, 8 — Pico de vetor unimodal de valores distintos. | b1-02-divisao-e-conquista | 0.0177 | 5.62 | – | NÃO |
| 3 | PAA_L2.pdf | p. 7 — Encontrar dois elementos distintos de S cuja soma é x em tem | b1-01-corretude-complexidade | 0.0175 | 5.44 | – | NÃO |
| 4 | PAA_L4.pdf | p. 3 — Agendamento do maior número de intervalos compatíveis. | b1-03-algoritmos-gulosos | 0.0172 | 5.34 | – | NÃO |

### R1-mestre-nlogn (recorrencia)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L3.pdf | p. 5 — Comparação de três recorrências, com casos base constantes. | b1-02-divisao-e-conquista | 0.0180 | 15.30 | – | sim |
| 2 | PAA_L3.pdf | p. 8, 9 — Dias de compra e venda para maximizar p[venda]−p[compra], co | b1-02-divisao-e-conquista | 0.0177 | 7.32 | – | sim |
| 3 | c02_gabarito_algoritmo_x_nota_2.md | p. não informada na transcrição — Prova de corretude do Algoritmo X que retorna o maior elemen | b1-02-divisao-e-conquista | 0.0175 | 3.99 | – | sim |
| 4 | PAA_L5.pdf | p. 9 — Quantidade de caminhos simples distintos entre s e t. | b2-04-programacao-dinamica | 0.0172 | 3.42 | – | NÃO |

### R2-lacos-dependentes (lacos)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L2.pdf | p. 1, 2 — Subir n degraus em passos de tamanho 1 ou 2. | b1-01-corretude-complexidade | 0.0180 | 7.48 | – | sim |
| 2 | PAA_L2.pdf | p. 7 — Encontrar dois elementos distintos de S cuja soma é x em tem | b1-01-corretude-complexidade | 0.0177 | 7.39 | – | sim |
| 3 | PAA_L5.pdf | p. 2, 3 — Caminho mais longo em um DAG, medido em número de arestas. | b2-04-programacao-dinamica | 0.0175 | 3.20 | – | NÃO |
| 4 | PAA_L3.pdf | p. 4 — Computar a^n para inteiro n>=0 por divisão e conquista. | b1-02-divisao-e-conquista | 0.0172 | 3.06 | – | NÃO |

### R3-laco-multiplicativo (lacos)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L1.pdf | p. 9, 10 — Corretude de Horner para P(x)=sum(A[j]x^j,j=0..n). | b1-01-corretude-complexidade | 0.0180 | 8.98 | – | sim |
| 2 | PAA_L3.pdf | p. 7, 8 — Pico de vetor unimodal de valores distintos. | b1-02-divisao-e-conquista | 0.0177 | 7.61 | – | NÃO |
| 3 | PAA_L1.pdf | p. 11, 12, 13 — Conversor decimal-binário de n inteiro não negativo. | b1-01-corretude-complexidade | 0.0175 | 6.65 | – | sim |
| 4 | PAA_L2.pdf | p. 8, 9 — Contagem da palavra OI em Prog1(n), n>=1. | b1-01-corretude-complexidade | 0.0172 | 5.91 | – | sim |

### D1-algoritmo-x (dc)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | c01_prova1_2023-03_q2_algoritmo_x.md | p. não informada na transcrição — Explique o que o Algoritmo X faz e prove sua corretude. | b1-02-divisao-e-conquista | 0.0180 | 5.26 | – | sim |
| 2 | c02_gabarito_algoritmo_x_nota_2.md | p. não informada na transcrição — Prova de corretude do Algoritmo X que retorna o maior elemen | b1-02-divisao-e-conquista | 0.0177 | 5.19 | – | sim |
| 3 | PAA_L1.pdf | p. 9, 10 — Corretude de Horner para P(x)=sum(A[j]x^j,j=0..n). | b1-01-corretude-complexidade | 0.0175 | 4.37 | – | NÃO |
| 4 | PAA_L6.pdf | p. 4, 5 — Troco mínimo como programa linear inteiro. | b2-05-transformacao-de-problemas | 0.0172 | 4.10 | – | NÃO |

### D2-inversoes (dc)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L3.pdf | p. 4 — Computar a^n para inteiro n>=0 por divisão e conquista. | b1-02-divisao-e-conquista | 0.0180 | 8.55 | – | sim |
| 2 | PAA_L3.pdf | p. 7, 8 — Pico de vetor unimodal de valores distintos. | b1-02-divisao-e-conquista | 0.0177 | 7.45 | – | sim |
| 3 | PAA_L3.pdf | p. 8, 9 — Dias de compra e venda para maximizar p[venda]−p[compra], co | b1-02-divisao-e-conquista | 0.0175 | 6.36 | – | sim |
| 4 | PAA_L1.pdf | p. 11, 12, 13 — Conversor decimal-binário de n inteiro não negativo. | b1-01-corretude-complexidade | 0.0172 | 5.50 | – | NÃO |

### G1-atividades (guloso)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L4.pdf | p. 3 — Agendamento do maior número de intervalos compatíveis. | b1-03-algoritmos-gulosos | 0.0180 | 13.68 | – | sim |
| 2 | PAA_L8.pdf | p. 12, 13, 14 — Mecanismos usuais em cinco meta-heurísticas. | b2-07-lidando-com-np-completude | 0.0177 | 5.76 | – | NÃO |
| 3 | PAA_L5.pdf | p. 5, 6 — Custo mínimo de cortar uma string de comprimento n nas posiç | b2-04-programacao-dinamica | 0.0175 | 4.47 | – | NÃO |
| 4 | PAA_L6.pdf | p. 1, 2 — Mesa circular de cavaleiros: grafo de compatibilidade. | b2-05-transformacao-de-problemas | 0.0172 | 4.31 | – | NÃO |

### N1-np-reducao (np)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L7.pdf | p. 2, 3, 4 — Implicações de reduções polinomiais entre problemas de decis | b2-06-np-completude | 0.0180 | 11.65 | – | sim |
| 2 | c09_lista7_q1_classes_resolucao.md | p. não informada na transcrição — Defina P, NP, NP-completo e redução polinomial. | b2-06-np-completude | 0.0177 | 10.25 | – | sim |
| 3 | PAA_L7.pdf | p. 9, 10 — CONJUNTO INCIDENTE (Hitting Set). | b2-06-np-completude | 0.0172 | 6.44 | – | sim |
| 4 | PAA_L6.pdf | p. 1, 2 — Mesa circular de cavaleiros: grafo de compatibilidade. | b2-05-transformacao-de-problemas | 0.0169 | 5.90 | – | sim |

### N2-clique-vc (np)

| # | Bloco | Assunto | Score RRF | BM25 | Cosseno | Mesmo assunto? |
|---:|---|---|---:|---:|---:|---|
| 1 | PAA_L7.pdf | p. 9, 10 — CONJUNTO INCIDENTE (Hitting Set). | b2-06-np-completude | 0.0180 | 7.52 | – | sim |
| 2 | PAA_L5.pdf | p. 6, 7 — Cobertura mínima de vértices de uma árvore. | b2-04-programacao-dinamica | 0.0177 | 5.76 | – | NÃO |
| 3 | c09_lista7_q1_classes_resolucao.md | p. não informada na transcrição — Defina P, NP, NP-completo e redução polinomial. | b2-06-np-completude | 0.0175 | 5.28 | – | sim |
| 4 | PAA_L7.pdf | p. 10, 11 — ISOMORFISMO DE SUBGRAFO: dados o padrão G e o grafo alvo H,  | b2-06-np-completude | 0.0169 | 5.26 | – | sim |

## Resumo

- Blocos do mesmo assunto da pergunta: 28/60.
- Blocos que mais aparecem: PAA_L6.pdf | p. 4, 5 (4x), PAA_L3.pdf | p. 7, 8 (4x), PAA_L7.pdf | p. 9, 10 (3x), PAA_L2.pdf | p. 7 (3x), PAA_L1.pdf | p. 9, 10 (3x).

## Hubness do embedding (sem consulta)

k-ocorrência com k=4: quantas vezes o bloco está entre os 4 vizinhos mais próximos dos outros 52 blocos. Média esperada = 4.

| k-ocorrência | Bloco | Assunto | Tamanho (car.) |
|---:|---|---|---:|
| 12 | PAA_L6.pdf | p. 1 — Número faltante entre 1 e n, ouvindo n-1 inteiros  | b2-05-transformacao-de-problemas | 753 |
| 12 | PAA_L3.pdf | p. 4 — Computar a^n para inteiro n>=0 por divisão e conqu | b1-02-divisao-e-conquista | 598 |
| 11 | PAA_L5.pdf | p. 7, 8 — SUBSET SUM para inteiros positivos e alvo t>=0. | b2-04-programacao-dinamica | 556 |
| 10 | PAA_L5.pdf | p. 1 — Menor soma de um caminho do ápice à base de um tri | b2-04-programacao-dinamica | 612 |
| 10 | PAA_L3.pdf | p. 7, 8 — Pico de vetor unimodal de valores distintos. | b1-02-divisao-e-conquista | 477 |
| 9 | c06_lista2_q10_metodo_iteracao.md | p. não informada na transcrição — Método da iteração: T(n)=T(n-1)+n, T(1)=1. | b1-01-corretude-complexidade | 274 |
| 9 | PAA_L1.pdf | p. 11, 12, 13 — Conversor decimal-binário de n inteiro não negativ | b1-01-corretude-complexidade | 636 |
| 9 | PAA_L3.pdf | p. 4 — K-ésimo menor elemento da união de duas listas ord | b1-02-divisao-e-conquista | 805 |
