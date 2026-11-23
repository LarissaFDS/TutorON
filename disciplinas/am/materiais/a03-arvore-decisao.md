---
id: am-arvore-de-decisao-id3-entropia-ganho-de-informacao-taxa-de-erro
titulo: Árvore de decisão: algoritmo ID3, entropia e ganho de informação para escolher o atributo, regras de classificação e taxa de erro do modelo pela média ponderada
assunto: am-02-classificacao
tipo: prova
questao: slides 03 e resumo da AB1
resolucao: sim
fonte: Provas de Aprendizagem de Máquina do Prof. Aydano Machado (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Aprendizagem de Máquina (COMP390); provas AB1 e AB2 (uma delas de 2021.1)
fontes_catalogo: ufal-aydano-provas-am, ufal-aydano-slides-am
autoria: Questões do Prof. Aydano Machado (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), slides 03 e resumo da AB1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Árvore de decisão:** cada nó interno testa um atributo, cada ramo é um valor, cada folha é uma classe. Cada caminho da raiz a uma folha vira uma **regra** "se ... então classe".

**ID3 (entrada: base de treino, atributos de entrada e atributo classe):**
1. se todos os exemplos do nó têm a mesma classe, crie uma folha;
2. senão, escolha o atributo de **maior ganho de informação**, crie um ramo por valor e repita em cada subconjunto;
3. pare também quando acabarem os atributos (folha com a classe majoritária).

**Entropia** de um conjunto $S$ com proporções $p_i$ de cada classe:
$$H(S) = -\sum_i p_i \log_2 p_i$$
Em palavras: menos a soma de cada proporção vezes o logaritmo na base 2 dela. É 0 se o conjunto é puro e 1 com duas classes meio a meio.

**Ganho de informação** do atributo $A$: $G(S, A) = H(S) - \sum_v \frac{|S_v|}{|S|} H(S_v)$, a entropia antes menos a média ponderada das entropias depois da divisão.

Exemplo: 14 exemplos, 9 "sim" e 5 "não": $H = 0{,}940$. Um atributo que divide em (6 sim, 2 não) e (3 sim, 3 não) dá $H$ de 0,811 e 1, média ponderada $\tfrac{8}{14}0{,}811 + \tfrac{6}{14}1 = 0{,}892$, e ganho $0{,}048$.

**Taxa de erro do modelo:** média das taxas de erro das folhas (regras) **ponderada** pela fração de exemplos de cada uma. No resumo da turma: folhas com 3, 1, 4, 3 e 2 de 13 exemplos e erros 0, 0, 1/4, 1/3 e 0 dão
$$0{,}25 \cdot \tfrac{4}{13} + \tfrac{1}{3} \cdot \tfrac{3}{13} = \tfrac{2}{13} \approx 0{,}15$$
A acurácia é $1 - 0{,}15 = 0{,}85$.

**Verificação:** `test_entropia_ganho_e_erro_ponderado` refaz 0,940, 0,892 e 0,048, confere $2/13$ e compara com o `DecisionTreeClassifier(criterion="entropy")` do scikit-learn, que escolhe na raiz o atributo de maior ganho.
