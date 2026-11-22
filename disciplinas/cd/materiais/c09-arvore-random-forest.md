---
id: cd-arvore-de-decisao-vantagens-interpretacao-regras-random-forest-importancia
titulo: Árvores de decisão: vantagens (comparadas ao k-NN), importância para a interpretação dos dados, criar um conjunto com 2 classes e uma regra com 2 atributos; Random Forest para extrair informação (importância das variáveis)
assunto: cd-03-metodos
tipo: prova
questao: AB2 2020.1 Q2; Final e REAV 2 2020.1; AB2 2020.2 Q1-Q2; REAV AB2 2020.2 Q1; AB2 2021.1 Q1-Q2
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
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB2 2020.1 Q2; Final e REAV 2 2020.1; AB2 2020.2 Q1-Q2; REAV AB2 2020.2 Q1; AB2 2021.1 Q1-Q2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Vantagens da árvore de decisão (inclusive sobre o k-NN):**
1. **interpretável**: cada caminho é uma regra "se ... então" que um especialista entende e confere;
2. **predição rápida**: percorre a altura da árvore, sem comparar com toda a base (o k-NN compara com todos);
3. **seleciona atributos** sozinha (os mais informativos ficam perto da raiz) e ignora irrelevantes;
4. aceita atributos **numéricos e categóricos** e **não exige normalização**.
Desvantagens: instável e propensa a **overfitting** sem poda.

**Importância para a interpretação:** a árvore **mostra quais variáveis e limiares** separam as classes; isso gera conhecimento, não só previsão.

**Exemplo com 2 classes (AB2 Q2):** pacientes com `idade` e `pressão`; classe `risco` ou `normal`:

| idade | pressão | classe |
|---|---|---|
| 25 | 110 | normal |
| 35 | 120 | normal |
| 45 | 150 | risco |
| 60 | 145 | risco |
| 65 | 115 | normal |
| 50 | 160 | risco |

Uma árvore separa primeiro por pressão e gera a regra: **se pressão > 132,5 então risco; senão normal**. Com dois atributos: se pressão $> 132{,}5$ **e** idade $> 40$, então risco.

**Random Forest:** **conjunto** (*ensemble*) de muitas árvores, cada uma treinada numa **amostra com reposição** (*bootstrap*) e escolhendo atributos num **subconjunto aleatório** a cada divisão; a classe final é a **votação**. Reduz a variância de uma árvore só. Para **extrair informação**: a **importância das variáveis** (quanto cada uma reduz a impureza, em média, ou quanto o desempenho cai ao embaralhá-la) e o erro *out-of-bag* como estimativa sem conjunto de teste separado.

**Verificação:** `test_arvore_e_random_forest` treina a árvore na tabela acima (acerto de 100% e raiz em pressão, limiar 132,5) e mostra que a importância do Random Forest põe em primeiro lugar a variável que de fato define a classe numa base sintética com ruído.
