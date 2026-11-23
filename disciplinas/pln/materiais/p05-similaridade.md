---
id: pln-similaridade-do-cosseno-countvectorizer-tf-idf-documento-mais-parecido
titulo: Documento mais parecido com similaridade do cosseno usando CountVectorizer e TF-IDF; fórmula do TF-IDF e por que muda o resultado
assunto: pln-02-representacao-e-classificacao
tipo: lista
questao: Lista 3, questão 1
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
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 3, questão 1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Similaridade do cosseno** entre vetores $a$ e $b$:
$$\cos(a, b) = \frac{a \cdot b}{\lVert a \rVert\, \lVert b \rVert}$$
Em palavras: produto escalar dividido pelo produto das normas. Vai de 0 (nenhuma palavra em comum, com contagens não negativas) a 1 (mesma proporção de palavras); não depende do tamanho do documento.

**TF-IDF:** pesa cada termo $t$ no documento $d$ por
$$\text{tfidf}(t, d) = \text{tf}(t, d) \cdot \text{idf}(t), \qquad \text{idf}(t) = \ln\frac{1 + N}{1 + \text{df}(t)} + 1$$
(fórmula padrão do scikit-learn, com $N$ documentos e $\text{df}(t)$ documentos que contêm $t$; depois cada vetor é normalizado). Termos que aparecem em **todos** os documentos ganham peso mínimo; termos **raros** e específicos ganham peso alto.

**Por que muda o vizinho:** com contagens, dois textos podem parecer próximos só por compartilhar palavras comuns da base; com TF-IDF, pesa mais compartilhar termos raros.

**Exemplo:** A = "futebol gol time gol", B = "time jogo campeonato", C = "futebol gol goleiro". Com contagens, o mais parecido com A é C (compartilham "futebol" e "gol"). Com TF-IDF continua C ($0{,}71 	o 0{,}63$), e a de A com B cai ($0{,}24 	o 0{,}19$): os termos só de B ("jogo", "campeonato") ganham peso maior, e o "time" compartilhado pesa relativamente menos.

**Procedimento:** vetorize a base; calcule a matriz de similaridades (`sklearn.metrics.pairwise.cosine_similarity`); para cada documento escolhido, **zere a diagonal** (ele mesmo) e pegue o `argmax`. Mostre trechos dos dois documentos que justifiquem a semelhança.

**Verificação:** `test_cosseno_count_tfidf` confere com scikit-learn que o vizinho de A é C nas duas representações, que a diagonal precisa ser excluída, que o idf de um termo presente em todos os documentos é 1 e que o cosseno calculado à mão bate com o da biblioteca.
