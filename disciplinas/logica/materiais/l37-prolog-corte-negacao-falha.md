---
id: logica-prolog-corte-negacao-falha
titulo: Prolog: corte (!), fail e negação por falha (\+)
assunto: logica-14-programacao-logica-prolog
tipo: material_estudo
resolucao: sim
fonte: Fichas práticas 7 e 9 (árvores de prova, cut e fail), usadas pela turma de Ciência da Computação (UFAL)
curso: Ciência da Computação (UFAL), turma da Profa. Roberta Lopes, COMP360
fontes_catalogo: fichas-praticas-prolog
autoria: Fichas práticas de Prolog de outra instituição (cabeçalho "PPIII - TP (LESI)", autoria não identificada), usadas pela turma de Ciência da Computação (UFAL); parafraseadas pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; código executado no SWI-Prolog 11).

**Árvore de prova:** a execução de uma consulta é uma busca em profundidade, da esquerda para a direita, nas cláusulas na ordem em que aparecem; quando um objetivo falha, o Prolog volta (**backtracking**) para a última escolha em aberto. O `trace` mostra as portas Call, Exit, Redo e Fail de cada objetivo.

**Corte `!`:** sucede uma vez e elimina as escolhas pendentes da cláusula atual e do predicado. Cuidado com o corte "vermelho":

```prolog
max(X,Y,X) :- X >= Y, !.
max(_,Y,Y).
```

`max(3,5,M)` e `max(5,3,M)` dão `M = 5`, mas `max(5,3,3)` **sucede** (a primeira cláusula não casa com o terceiro argumento 3, e a segunda aceita). Versão segura: `max(X,Y,Z) :- X >= Y, !, Z = X.` e `max(_,Y,Y).`

**Negação por falha:** `\+ G` sucede quando `G` não pode ser provado. Não é a negação lógica $\neg$: vale a hipótese do mundo fechado (o que não está na base é falso).

```prolog
ave(piupiu). ave(pingu). pinguim(pingu).
voa(X) :- ave(X), \+ pinguim(X).
```

`voa(X)` dá só `X = piupiu`. Se a regra fosse `\+ pinguim(X), ave(X)`, a consulta `voa(X)` falharia: `\+` com variável ainda livre pergunta "não existe pinguim nenhum?".

**Verificação:** max/3 (inclusive o caso errado max(5,3,3)), a versão segura e voa/1 nas duas ordens rodaram no SWI-Prolog 11 com os resultados citados.
