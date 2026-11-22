---
id: cd-naive-bayes-quando-usar-classificacao-de-texto-what-do-you-mean
titulo: Naive Bayes: em que tipos de problemas é preferível; exercício de classificar o texto "what do you mean" como pergunta ou afirmação (stmt × question) com Laplace
assunto: cd-03-metodos
tipo: prova
questao: AB2 2020.1 Q1; Lista 2 Q2 e Q7
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
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB2 2020.1 Q1; Lista 2 Q2 e Q7 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Naive Bayes:** escolhe a classe $c$ que maximiza
$$P(c \mid x_1, \ldots, x_n) \propto P(c) \prod_{i} P(x_i \mid c)$$
Em palavras: a probabilidade da classe vezes o produto das probabilidades de cada atributo dado a classe, supondo **atributos independentes dada a classe** (a suposição "ingênua").

**Quando é preferível:** **texto** (spam, sentimento, tema), muitos atributos e **poucos dados**, necessidade de **treino e predição rápidos** e modelo simples de atualizar; bom ponto de partida (*baseline*). Menos indicado quando atributos são muito dependentes e se precisa de **probabilidades bem calibradas**.

**Comparação com redes neurais (Lista 2 Q2):** redes captam interações e fronteiras não lineares e costumam ser mais precisas com muitos dados; mas precisam de muito mais dados, tempo e ajuste de parâmetros, e são menos interpretáveis.

**Exercício (Lista 2 Q7):** treino com 4 frases *stmt* e 4 *question*; classificar "what do you mean". Modelo **multinomial** com **suavização de Laplace**, contando palavras em minúsculas:
- *stmt*: 17 palavras; *question*: 18; vocabulário: 22 palavras distintas;
- "what" aparece 2 vezes em *question* e 0 em *stmt*; "you", 1 e 0; "do" e "mean" não aparecem no treino (ignoradas, ou com o mesmo fator nas duas classes).
- $P(\text{question}) = P(\text{stmt}) = 1/2$.
$$\text{question}: \tfrac{2+1}{18+22} \cdot \tfrac{1+1}{18+22} = \tfrac{6}{1600} = 0{,}00375 \qquad \text{stmt}: \tfrac{0+1}{17+22} \cdot \tfrac{0+1}{17+22} = \tfrac{1}{1521} \approx 0{,}00066$$
Classe: **question**. Sem Laplace, a palavra "what" zeraria a probabilidade de *stmt* e qualquer palavra nova zeraria as duas: por isso se suaviza.

**Verificação:** `test_naive_bayes_texto` refaz as contagens (17, 18 e 22), as duas probabilidades e a classe à mão, e confere com `CountVectorizer` e `MultinomialNB` do scikit-learn, que também dão **question**.
