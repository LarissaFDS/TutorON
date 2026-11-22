---
id: cd-knn-versus-k-means-semelhancas-diferencas-deficiencias-do-knn-quando-usar
titulo: Compare k-vizinhos mais próximos (k-NN) e k-means (semelhanças e diferenças); deficiências do k-NN; problema real em que é preferível k-NN e outro em que é preferível Naive Bayes
assunto: cd-03-metodos
tipo: prova
questao: AB1 2020.1 Q7; REAV 1 Q5; AB1 2020.2 Q5; AB1 2021.1 Q5
resolucao: sim
fonte: Provas e listas de Ciência de Dados do Prof. Bruno Pimentel (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Ciência de Dados (COMP401); turmas 2020.1, 2020.2 e 2021.1
fontes_catalogo: ufal-pimentel-provas-cd
autoria: Questões do Prof. Bruno Pimentel (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB1 2020.1 Q7; REAV 1 Q5; AB1 2020.2 Q5; AB1 2021.1 Q5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Semelhanças:** ambos usam **distância** (em geral euclidiana) entre pontos num espaço de atributos; ambos têm um parâmetro $k$; ambos são sensíveis à **escala** dos atributos (normalizar) e sofrem com muitas dimensões.

**Diferenças:**

| | k-NN | k-means |
|---|---|---|
| tipo | **supervisionado** (classificação ou regressão) | **não supervisionado** (agrupamento) |
| o que é $k$ | número de **vizinhos** consultados | número de **grupos** |
| treino | nenhum (guarda os exemplos, é "preguiçoso") | iterativo: atribui e recalcula centroides |
| saída | rótulo de um novo ponto | partição dos dados e centroides |

**Deficiências do k-NN:**
- **custo de classificação** alto: compara com todos os exemplos (memória e tempo);
- sensível a **escala**, a atributos **irrelevantes** e à **maldição da dimensionalidade**;
- sensível a **ruído** com $k$ pequeno e a **classes desbalanceadas** (a classe maior domina a votação);
- não gera modelo interpretável; exige atributos numéricos ou uma distância adequada;
- escolha de $k$ e da distância por validação.

**Quando usar cada um (problemas reais):**
- **k-NN:** **recomendação** por similaridade ("clientes parecidos compraram"), **localização** em ambiente fechado por intensidade de sinais Wi-Fi, reconhecimento de dígitos: poucos atributos numéricos, fronteiras irregulares e base que cabe na memória.
- **Naive Bayes:** **classificação de texto** (spam, sentimento, tema): milhares de atributos (palavras), poucos exemplos, treino e predição muito rápidos; a suposição de **independência condicional** entre palavras é falsa, mas funciona bem na prática para decidir a classe.

**Verificação:** `test_knn_versus_kmeans` confere no scikit-learn que o k-NN precisa de rótulos e o k-means não, que o k-means devolve 3 centroides na base Iris e que o k-NN piora quando a base de treino é desbalanceada para uma classe.
