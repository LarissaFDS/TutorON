---
id: pln-word2vec-palavras-mais-parecidas-buscador-de-documentos-distancia-media-doc2vec
titulo: Word2vec: palavras mais parecidas com uma consulta, buscador de documentos pela distância média DM10(w) às 10 palavras mais parecidas de cada documento, e Doc2Vec
assunto: pln-03-topicos-agrupamento-e-embeddings
tipo: lista
questao: Lista 5, questões 1 e 2
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
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 5, questões 1 e 2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Word2vec:** aprende um **vetor denso** (ex.: 100 a 300 dimensões) por palavra, treinando uma rede rasa a prever a palavra pelo contexto (**CBOW**) ou o contexto pela palavra (**skip-gram**). Palavras usadas em contextos parecidos ficam com vetores próximos (similaridade do cosseno). Use um modelo **pré-treinado no idioma dos textos** (para português, os do NILC; para inglês, Google News ou GloVe), já que a base da turma é pequena para treinar do zero. Biblioteca: `gensim` (`KeyedVectors.most_similar`).

**Palavra fora dos textos:** a consulta $w$ precisa existir no **vocabulário do modelo**, não da base. Para achar as 3 palavras **da base** mais parecidas, calcule a similaridade de $w$ com cada palavra da base que o modelo conhece e pegue as 3 maiores.

**Buscador DM10:** para cada documento $d$:
1. $d_{10}(w)$: as 10 palavras de $d$ mais parecidas com $w$;
2. $DM_{10}(w)$: a **distância média** (ex.: $1 - \cos$) entre $w$ e essas 10;
3. retorne os 3 documentos de menor $DM_{10}(w)$.
Documentos com menos de 10 palavras conhecidas usam as que tiverem (registre a decisão).

**Doc2Vec:** estende o word2vec com um vetor **por documento**, treinado junto; dá uma representação de tamanho fixo para classificar e agrupar (refazer listas 3 e 4) e comparar com TF-IDF.

**Verificação:** `test_buscador_dm` implementa o DM10 em NumPy com vetores de brinquedo (consulta "felino" perto de "gato" e "leão") e confere que os documentos sobre animais ficam à frente, que a média usa no máximo 10 palavras e que a distância do cosseno de um vetor com ele mesmo é 0.
