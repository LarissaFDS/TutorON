---
id: logica-roberta-prova1-complexidade-negacao
titulo: Prova de lógica proposicional: tabela-verdade, grau de complexidade, negação nos átomos e fórmula mais simples
assunto: logica-02-proposicional-sintaxe-semantica
tipo: prova
resolucao: sim
fonte: 1ª avaliação de lógica proposicional, Profa. Roberta Lopes, aplicada em 22/01/2019 (Ciência da Computação, UFAL); enunciado parafraseado com fórmula própria
curso: Ciência da Computação (UFAL), turma da Profa. Roberta Lopes, COMP360
semestre: nao_informado (prova aplicada em 22/01/2019)
fontes_catalogo: roberta-provas-2019
autoria: Profa. Roberta Lopes (IC-UFAL), Ciência da Computação; enunciado parafraseado pela equipe TutorON com auxílio de IA, sem nada da resposta do aluno
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Questão de prova (paráfrase do enunciado) com resolução. Prova é atividade avaliativa: o tutor guia, não entrega. Status da resolução: pendente_professor (resolução da equipe TutorON, não é gabarito do professor; conferida com Python, mas a resposta esperada depende de uma premissa que o enunciado não traz).

Enunciado (paráfrase): na prova, cada aluno montava a própria fórmula trocando letras por conectivos segundo uma tabela. Para uma fórmula $A$: (1) faça a tabela-verdade e diga se é tautologia, contradição ou contingência; (2) confira um valor pela definição de valoração; (3) dê o grau de complexidade; (4) escreva $\neg A$ com a negação só nos átomos; (5) ache a fórmula equivalente mais simples.

Amostra com fórmula própria: $A = (p\to q)\land\neg(q\lor r)$ (em palavras: "se p então q, e não é o caso que q ou r").

1. $A$ é verdadeira só quando $p$, $q$ e $r$ são todos falsos: das 8 linhas, 1 verdadeira e 7 falsas, então é **contingência**.
2. Com $v(p)=v(q)=v(r)=F$: $v(p\to q)=V$, $v(q\lor r)=F$, $v(\neg(q\lor r))=V$, logo $v(A)=V$.
3. Contando ocorrências de conectivos ($\to$, $\land$, $\neg$, $\lor$), o grau é **4**. Atenção: há livros que contam símbolos (comprimento) ou a altura da árvore; confira a definição usada em aula.
4. $\neg A\equiv\neg(p\to q)\lor(q\lor r)\equiv(p\land\neg q)\lor q\lor r\equiv p\lor q\lor r$.
5. $A\equiv(p\to q)\land\neg q\land\neg r\equiv\neg p\land\neg q\land\neg r$.

A pendência é só o item 3: o enunciado não define "grau de complexidade".

**Verificação:** a tabela-verdade, a valoração e as equivalências dos itens 4 e 5 foram conferidas em Python (tests_acervo/logica_verif.py).
