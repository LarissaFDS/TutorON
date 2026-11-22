---
id: logica-roberta-prova2-modelo-finito
titulo: Prova de primeira ordem: variáveis livres e valor de fórmulas num modelo finito com +, · e ≤
assunto: logica-10-primeira-ordem-semantica
tipo: prova
resolucao: sim
fonte: 2ª avaliação de lógica de primeira ordem, Profa. Roberta Lopes, aplicada em 19/03/2019 (Ciência da Computação, UFAL); enunciado parafraseado com fórmulas próprias
curso: Ciência da Computação (UFAL), turma da Profa. Roberta Lopes, COMP360
semestre: nao_informado (prova aplicada em 19/03/2019)
fontes_catalogo: roberta-provas-2019
autoria: Profa. Roberta Lopes (IC-UFAL), Ciência da Computação; enunciado parafraseado pela equipe TutorON com auxílio de IA, sem nada da resposta do aluno
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questão de prova (paráfrase do enunciado) com resolução. Prova é atividade avaliativa: o tutor guia, não entrega. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

Enunciado (paráfrase): dado um modelo $M$ com domínio $D=\{1,2,3\}$, em que $+$ e $\cdot$ são as operações usuais **limitadas a 3** (todo resultado maior que 3 vira 3) e $\le$ é a ordem usual, e a atribuição $\sigma(x)=1$, $\sigma(y)=2$, $\sigma(z)=3$: (a) diga quais variáveis estão livres em cada fórmula; (b) calcule o valor de cada fórmula em $M$ com $\sigma$; (c) prove alguns teoremas de primeira ordem, como a transitividade da igualdade.

Amostra com fórmulas próprias no mesmo modelo:
- $F_1=\exists x\,(1+y=x)\land\forall y\,(y\le x)$. Livres: $y$ na primeira parte e $x$ na segunda. Valor: $1+2=3$, então existe $x$; mas $\forall y\,(y\le 1)$ é falso ($2\le 1$ falha). **$F_1$ é falsa.**
- $F_2=\exists x\,(x\cdot x=2)\to(x+1=3)$. Livre: o $x$ do consequente. Os quadrados em $D$ são $1$, $3$ e $3$ (4 e 9 viram 3); nenhum é 2, o antecedente é falso e **$F_2$ é verdadeira** (implicação com antecedente falso).
- $F_3=\forall y\,\exists z\,(x+y=z)\to(x=3)$. Livre: $x$ (nas duas partes). O antecedente é verdadeiro (a soma limitada sempre cai em $D$), mas $\sigma(x)=1\neq 3$: **$F_3$ é falsa.**

Erro comum: chamar de "tautologia" uma fórmula só porque ela é verdadeira neste modelo. Tautologia (validade) é ser verdadeira em **todo** modelo e toda atribuição.

**Verificação:** as três fórmulas foram avaliadas em Python no modelo $M$ com $\sigma$, com os valores citados.
