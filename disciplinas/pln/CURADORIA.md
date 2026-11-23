# Curadoria — Processamento de Linguagem Natural

Situação: **em validação**. Revisão humana pendente em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `Eletivas/Processamento de Linguagem
Natural`). São as listas de exercícios 1 a 6 do Prof. Thales Vieira (IC-UFAL), turma 2021.1, de
outubro de 2021 a fevereiro de 2022.

**Ementa não conferida.** O Projeto Pedagógico de CC disponível (matriz 2011) não traz a eletiva com
ementa própria. A ementa não foi inventada: os tópicos vêm das listas:
- expressões regulares;
- pré-processamento;
- representações vetoriais e similaridade;
- classificação;
- tópicos;
- agrupamento e projeção;
- word2vec e Doc2Vec;
- redes neurais;
- spaCy;
- seq2seq.

## O que entrou
13 blocos (`materiais/p01`–`p13`), um por questão ou grupo de questões das listas.

As listas são **avaliativas** e cada grupo usa a própria base de textos. Por isso os blocos explicam o
método e trazem um **exemplo parecido**, sem o código completo da lista.

Os exemplos foram conferidos com scikit-learn, NumPy e `re`, com semente fixa, em
`tests_acervo/test_disciplina_pln.py`. NLTK, spaCy, gensim, UMAP e Keras não estão instalados nos
testes, e as partes que dependem deles são conferidas por implementações pequenas em Python:
- stemização simples;
- contagem de entidades já anotadas;
- buscador DM10 com vetores de brinquedo;
- janelas de próxima palavra;
- tensores do seq2seq.

## O que não entrou
- PDFs das listas, que não têm licença declarada.
- Resoluções de alunos: não há na pasta.

## Decisões pendentes
- Sem ligação em `disciplinas/cursos.json`. É eletiva, fora da matriz do arquivo.
- Ementa oficial a conferir com a coordenação.
