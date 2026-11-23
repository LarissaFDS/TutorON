---
id: pln-stopwords-rotulacao-pos-stemizacao-lematizacao-comparar-frequencias
titulo: Remover stopwords, rotulação de classes gramaticais (POS tagging), stemização e lematização; comparar as palavras mais frequentes antes e depois
assunto: pln-01-regex-e-preprocessamento
tipo: lista
questao: Lista 2, questão 3; Lista 6, questão 3a-b
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
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 2, questão 3; Lista 6, questão 3a-b (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Stopwords:** palavras muito frequentes e pouco informativas (artigos, preposições, pronomes: "o", "de", "que"). Removê-las faz as mais frequentes refletirem o **assunto** da base. Use a lista do idioma certo (NLTK e spaCy têm listas em português) e revise: em análise de sentimento, "não" importa.

**Rotulação de POS** (*part-of-speech*): atribuir a cada token sua classe gramatical (substantivo, verbo, adjetivo...). Um rotulador estatístico usa o **contexto**: "canto" é verbo em "eu canto" e substantivo em "o canto". Ferramentas: `nltk.pos_tag` (com modelo treinado), `spacy` (`token.pos_`, etiquetas universais NOUN, VERB, ADJ). Faça o POS **antes** de stemizar, porque o rotulador precisa das palavras inteiras. A lista 6 pede a frequência de cada classe num gráfico de barras.

**Stemização:** corta sufixos por regras para chegar a um **radical**, que pode não ser palavra: "correr", "correndo", "corrida" → "corr". Para português, o **RSLP** (`nltk.stem.RSLPStemmer`); o Porter é para inglês. **Lematização:** leva à forma de dicionário ("correndo" → "correr", "melhores" → "melhor"); mais precisa, exige dicionário ou modelo (spaCy).

**Efeito nas frequências:** sem stopwords, sobem as palavras de conteúdo; com stemização, variações se juntam ("gato" e "gatos" → "gat"), e a contagem do radical soma as das formas.

Exemplo: tokens `o gato e os gatos correram para o gato` → sem stopwords {o, e, os, para}: `gato gatos correram gato`; com um stemizador que tira o plural: `gato` ×3, `correram` ×1.

**Verificação:** `test_stopwords_e_stem` roda o exemplo com uma lista de stopwords e um stemizador de plural simples em Python e confere que "gato" passa de 2 para 3 ocorrências e que nenhuma stopword sobra.
