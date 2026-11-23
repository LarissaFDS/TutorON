---
id: logica-evandro-2024-governo-inflacao
titulo: Governo bom, desemprego e inflação: há inflação (modus tollens) versus não há inflação (falácia da afirmação do consequente)
assunto: logica-03-consequencia-equivalencia
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
Questão de lista e de prova (paráfrase do enunciado) com resolução. Prova é atividade avaliativa: o tutor guia, não entrega. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

Premissas: "se o governo é bom, não há desemprego" ($G\to\neg D$) e "se não há desemprego, não há inflação" ($\neg D\to\neg I$). As alternativas comparam "o governo não é bom e há desemprego" ($\neg G\land D$), "o governo é bom e há desemprego" ($G\land D$), "o governo é bom e não há desemprego" ($G\land\neg D$) e "nenhuma das anteriores".

**Versão da lista: "há inflação" ($I$).** De $\neg D\to\neg I$ e $I$, por modus tollens, $D$ (há desemprego). De $G\to\neg D$ e $D$, por modus tollens, $\neg G$. Conclusão: **o governo não é bom e há desemprego** ($\neg G\land D$).

**Versão da prova: "não há inflação" ($\neg I$).** Agora nada segue sobre $G$ nem sobre $D$. Concluir $\neg D$ a partir de $\neg D\to\neg I$ e $\neg I$ é a **falácia da afirmação do consequente**. Contramodelos: $G$ V, $D$ F, $I$ F satisfaz as premissas e derruba $\neg G\land D$; $G$ F, $D$ V, $I$ F derruba $G\land\neg D$; $G\land D$ contradiz a primeira premissa. A resposta é **nenhuma das alternativas**.

Erro comum: marcar "o governo é bom e não há desemprego" na versão da prova, lendo a implicação ao contrário. A frase "a inflação não afeta o desemprego" nem é consequência formal: ela fala de causa, e a lógica proposicional não trata disso.

**Verificação:** as duas versões foram conferidas por tabela-verdade em Python: com $I$, só $\neg G\land D$ é consequência; com $\neg I$, nenhuma das três conjunções é.
