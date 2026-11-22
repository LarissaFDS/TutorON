---
id: logica-prolog-unificacao-aritmetica
titulo: Prolog: unificação (=), avaliação (is) e comparação aritmética (=:=)
assunto: logica-14-programacao-logica-prolog
tipo: material_estudo
resolucao: sim
fonte: Fichas práticas 3 e 4 (operadores, unificação e aritmética), usadas pela turma de Ciência da Computação (UFAL)
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

Em Prolog há três "iguais" diferentes:
- `X = Y` **unifica**: acha substituições que tornam os dois termos idênticos, sem calcular nada. `f(X,b) = f(a,Y)` dá `X = a, Y = b`; `2+3 = 5` **falha**, porque o termo `+(2,3)` não é o número 5.
- `X is E` **avalia** a expressão aritmética `E` (que não pode ter variável livre) e unifica o resultado com `X`: `X is 2+3` dá `X = 5`.
- `E1 =:= E2` **compara** os valores de duas expressões: `2+3 =:= 5` sucede. Também há `<`, `>`, `=<` (menor ou igual, escrito assim em Prolog) e `>=`.

A unificação do Prolog é a mesma da resolução de primeira ordem, mas por padrão **sem teste de ocorrência**: `X = f(X)` sucede criando um termo cíclico; `unify_with_occurs_check(X, f(X))` falha, como no algoritmo de Robinson.

A ficha 3 mostra também a declaração de operadores, por exemplo `:- op(700, xfy, impl).`, que permite escrever `p impl q` em vez de `impl(p,q)`: o número é a precedência e `xfy` diz que o operador é infixo e associa à direita.

**Verificação:** as consultas `f(X,b) = f(a,Y)`, `2+3 = 5`, `X is 2+3`, `2+3 =:= 5`, `unify_with_occurs_check(X,f(X))` e `(p impl q) == impl(p,q)` rodaram no SWI-Prolog 11 com os resultados citados.
