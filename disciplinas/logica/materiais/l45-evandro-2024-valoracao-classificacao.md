---
id: logica-evandro-2024-valoracao-classificacao
titulo: Valor de uma fórmula em duas interpretações e classificação em tautologia, contradição ou contingência; bicondicional como duas condicionais
assunto: logica-02-proposicional-sintaxe-semantica
tipo: prova
resolucao: sim
fonte: Lista 1 e prova 1 de Lógica Aplicada à Computação, Prof. Evandro Costa, 2024.1 (Engenharia de Computação, UFAL); enunciado parafraseado
curso: Engenharia de Computação (UFAL), turma do Prof. Evandro Costa, ECOM007, 2024.1
semestre: 2024.1
fontes_catalogo: ufal-evandro-2024-lista-prova
autoria: Prof. Evandro Costa (IC-UFAL); enunciado parafraseado pela equipe TutorON com auxílio de IA, sem nada das respostas do aluno
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio; as fotos e imagens originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de lista e de prova (paráfrase) com resolução. Prova é atividade avaliativa: o tutor guia, não entrega. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**1. Valor numa interpretação.** Fórmula $(p\land(\neg q\to p))\land\neg((p\leftrightarrow\neg q)\to(q\lor\neg p))$.
- $p$ V, $q$ F: $\neg q\to p$ é V, então a primeira parte é V. $p\leftrightarrow\neg q$ é V; $q\lor\neg p$ é F; V implica F dá F; invertendo, V. **Valor: V.**
- $p$ F, $q$ F: a primeira parte já é F. **Valor: F.**
Erro comum: errar a segunda parte por esquecer que o "não" de fora vale para a implicação inteira.

**2. Classificação** (tabela-verdade):
- $(P\to Q)\land(\neg P\to R)$: contingência (satisfatível, não tautologia).
- $P\land\neg P\land Q$: contradição.
- $(\neg(P\lor Q)\lor\neg P)\land P$: contradição (com $P$ V, as duas partes do "ou" são F).
- $Q\to(P\land\neg Q)$: contingência (V só quando $Q$ é F).
- $(P\land Q)\leftrightarrow(\neg P\lor Q)$: contingência (F quando $P$ é F).

**3. "Se e somente se".** "Um inteiro é par se e somente se o quadrado é par" ($P\leftrightarrow Q$) equivale a "se é par, o quadrado é par; e se não é par, o quadrado não é par" ($(P\to Q)\land(\neg P\to\neg Q)$): a segunda condicional é a contrapositiva de $Q\to P$.

**4. Questão de concurso** (lista): "a inflação não baixa ou os juros aumentam" ($\neg B\lor J$) equivale a "**se a inflação baixa, os juros aumentam**" ($B\to J$), pela lei $p\to q\equiv\neg p\lor q$.

**Verificação:** valores, classificações e equivalências conferidos por tabela-verdade completa em Python.
