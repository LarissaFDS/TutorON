---
id: pln-traducao-seq2seq-codificador-decodificador-lstm-nivel-de-caractere-teacher-forcing
titulo: Tradução com modelo sequência a sequência (seq2seq) em nível de caractere: codificador e decodificador LSTM, teacher forcing, inferência passo a passo, versão em nível de palavra
assunto: pln-04-redes-neurais-e-spacy
tipo: lista
questao: Lista 6, questão 4
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
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 6, questão 4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Arquitetura** (tutorial *Character-level recurrent sequence-to-sequence model* da documentação do Keras):
- **codificador:** uma LSTM lê a frase de origem caractere a caractere (cada um em *one-hot*) e devolve só os **estados finais** $(h, c)$, um resumo da frase;
- **decodificador:** outra LSTM começa com esses estados e gera a frase de destino caractere a caractere, com uma camada densa *softmax* sobre o alfabeto de destino.

**Dados:** pares de frases (os arquivos do site manythings.org/anki têm um par por linha, separado por tabulação). Cada frase de destino ganha um caractere de **início** (`\t`) e um de **fim** (`\n`). Tensores *one-hot*:
- entrada do codificador: (amostras, maior frase de origem, tamanho do alfabeto de origem);
- entrada do decodificador: (amostras, maior frase de destino, alfabeto de destino);
- alvo do decodificador: a entrada do decodificador **deslocada um passo** para a esquerda.

**Teacher forcing:** no treino, o decodificador recebe o caractere **correto** anterior, não o que ele previu; aprende mais rápido.

**Inferência:** codifica a frase, começa com `\t` e, a cada passo, prevê o próximo caractere, realimenta-o e atualiza os estados, até gerar `\n` ou atingir o tamanho máximo.

**Nível de palavra (bônus):** troque o *one-hot* de caracteres por índices de palavras com uma camada **Embedding** em cada lado; o vocabulário cresce, as sequências encurtam e palavras desconhecidas precisam de um token especial.

**Verificação:** `test_dados_seq2seq` monta os tensores *one-hot* de dois pares de brinquedo em NumPy e confere as formas, os caracteres de início e fim e que o alvo é a entrada do decodificador deslocada um passo.
