---
id: pln-redes-neurais-para-texto-embedding-convolucional-lstm-geracao-de-texto-proxima-palavra
titulo: Redes neurais para texto: camadas Embedding, convolucionais e LSTM para classificação; LSTM para gerar texto prevendo a próxima palavra a partir de sequências de tamanho 4
assunto: pln-04-redes-neurais-e-spacy
tipo: lista
questao: Lista 6, questões 1 e 2
resolucao: sim
fonte: Listas de exercícios 1 a 6 de Processamento de Linguagem Natural, Prof. Thales Vieira (IC-UFAL), 2021.1
curso: Ciência da Computação (UFAL), eletiva Processamento de Linguagem Natural; turma 2021.1 (listas de out/2021 a fev/2022)
fontes_catalogo: ufal-vieira-listas-pln,scikit-learn-pln
autoria: Questões do Prof. Thales Vieira (IC-UFAL); explicação e exemplo parecido da equipe TutorON
licenca: Não declarada (listas); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 6, questões 1 e 2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Entrada:** cada texto vira uma sequência de **índices** do vocabulário, cortada ou completada (*padding*) até um tamanho fixo.

**Camadas:**
- **Embedding:** tabela que transforma cada índice num vetor denso aprendido (ou iniciado com word2vec);
- **convolucional 1D:** filtros que deslizam sobre janelas de palavras e detectam **n-gramas** relevantes; com *max pooling* global, o resultado não depende da posição;
- **LSTM:** rede recorrente com **portas** (esquecimento, entrada, saída) e uma célula de memória que guarda informação ao longo da sequência e atenua o desaparecimento do gradiente;
- saída: `Dense(1, activation="sigmoid")` na classificação binária.

Duas arquiteturas para comparar: Embedding → Conv1D → GlobalMaxPooling → Dense; Embedding → LSTM → Dense. Use o **mesmo** treino/teste das listas 3 e 5 e validação para a parada antecipada.

**Geração de texto (próxima palavra):** de cada texto tokenizado, crie pares **(4 palavras → a 5ª)** com janela deslizante. Com $m$ tokens, saem $m - 4$ pares. Exemplo: `o gato subiu no telhado de casa` ($m = 7$) gera 3 pares: (o gato subiu no → telhado), (gato subiu no telhado → de), (subiu no telhado de → casa).

Treine Embedding → LSTM → Dense(softmax sobre o vocabulário) com entropia cruzada. Para gerar: dê as palavras iniciais, preveja a próxima, **acrescente** e **deslize a janela**; repita 10 vezes. Escolher sempre a mais provável repete frases; **amostrar** com temperatura dá mais variedade.

**Verificação:** `test_janelas_proxima_palavra` monta os pares do exemplo ($m - 4 = 3$), confere entradas e alvos e simula a geração com um "modelo" de bigramas para checar que a janela desliza e gera 10 palavras.
