---
id: logica-prolog-findall-assert
titulo: Prolog: findall, bagof, setof, assert e retract
assunto: logica-14-programacao-logica-prolog
tipo: material_estudo
resolucao: sim
fonte: Fichas práticas 8, 10, 11 e 12 (meta-predicados, base dinâmica, leitura e programas interativos), usadas pela turma de Ciência da Computação (UFAL)
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

**Todas as soluções de uma consulta:**

```prolog
pai(ana,joao). pai(beto,joao). pai(caio,maria).
```

- `findall(F, pai(F,P), L)` junta todas as soluções numa lista e ignora `P`: `L = [ana,beto,caio]`. Sem solução, devolve `[]`.
- `bagof(F, pai(F,P), L)` agrupa por cada valor da variável livre `P`: primeiro `P = joao, L = [ana,beto]`, depois `P = maria, L = [caio]`; sem solução, **falha**. Com `P^pai(F,P)` a variável `P` passa a ser existencial e sai uma lista só.
- `setof` é como `bagof`, mas ordena e tira repetições.

**Base dinâmica:** `:- dynamic contador/1.` permite mudar fatos durante a execução. `assertz(F)` acrescenta no fim, `asserta(F)` no começo e `retract(F)` remove o primeiro fato que unifica:

```prolog
:- dynamic contador/1.
contador(0).
incrementa :- retract(contador(N)), N1 is N+1, assertz(contador(N1)).
```

Após duas chamadas de `incrementa`, `contador(X)` dá `X = 2`. As fichas 11 e 12 usam isso com `read/1`, `write/1` e um laço `repeat ... fail` para menus interativos; o sistema especialista da turma guarda as respostas do usuário do mesmo jeito.

**Verificação:** as três consultas de findall/bagof, a versão com `P^`, setof e o contador rodaram no SWI-Prolog 11 com as respostas citadas.
