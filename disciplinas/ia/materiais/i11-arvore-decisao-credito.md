---
id: ia-aprendizado-arvore-de-decisao-id3-risco-de-credito-entropia-ganho-renda-c45-prism
titulo: Aprendizado simbólico: árvore de decisão ID3 na base de risco de crédito (histórico, dívida, garantia, renda), entropia e ganho de cada atributo, comparação com C4.5 (J48) e Prism no Weka
assunto: ia-04-incerteza-e-aprendizado
tipo: lista
questao: Lista 1 (2020.2), questão de árvore de decisão com a base de risco de crédito
resolucao: sim
fonte: Listas 1 e 2 de Inteligência Artificial (IC-UFAL), 2020.2, Prof. Evandro de Barros Costa
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufal-ia-listas-2020-2
autoria: Questões do Prof. Evandro de Barros Costa (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), Lista 1 (2020.2), questão de árvore de decisão com a base de risco de crédito (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Base:** 14 clientes com histórico de crédito (ruim, desconhecido, bom), dívida (alta, baixa), garantia (nenhuma, adequada) e renda (0 a 15 mil, 15 a 35 mil, acima de 35 mil); classe risco (alto 6, moderado 3, baixo 5).

**Entropia da raiz:**
$$H = -\tfrac{6}{14}\log_2\tfrac{6}{14} - \tfrac{3}{14}\log_2\tfrac{3}{14} - \tfrac{5}{14}\log_2\tfrac{5}{14} \approx 1{,}531$$

**Ganho de informação** $G(A) = H(S) - \sum_v \frac{|S_v|}{|S|} H(S_v)$:
- renda: **0,966**;
- histórico: 0,266;
- garantia: 0,206;
- dívida: 0,063.

O ID3 põe **renda** na raiz. Ramos:
- 0 a 15 mil: todos de risco **alto** (folha);
- 15 a 35 mil: divide por histórico (ruim → alto; bom → moderado; desconhecido → divide por dívida: alta → alto, baixa → moderado);
- acima de 35 mil: divide por histórico (ruim → moderado; desconhecido e bom → baixo).

**C4.5 (J48 no Weka)** poda a árvore e fica com 3 folhas, só pela renda; **Prism** gera regras de cobertura. Com 14 exemplos e validação cruzada de 10 partes, as taxas de acerto (cerca de 50 a 65 %) são instáveis: compare os modelos pela matriz de confusão, não por um número só.

Árvores de decisão em profundidade (poda, atributos contínuos, avaliação) são de Aprendizagem de Máquina.

**Verificação:** `test_id3_credito` recalcula a entropia 1,531 e os quatro ganhos e confere que renda é a raiz e que o ramo de 0 a 15 mil é puro.
