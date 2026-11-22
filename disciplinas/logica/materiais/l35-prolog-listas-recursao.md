---
id: logica-prolog-listas-recursao
titulo: Prolog: listas e recursão (comprimento, soma, pertence, concatena, remove)
assunto: logica-14-programacao-logica-prolog
tipo: material_estudo
resolucao: sim
fonte: Arquivo questoes_prolog.txt da pasta Prolog e fichas práticas 5 e 6 (turma de Ciência da Computação, UFAL)
curso: Ciência da Computação (UFAL), turma da Profa. Roberta Lopes, COMP360
fontes_catalogo: cc-prolog-turma, fichas-praticas-prolog
autoria: Fichas práticas de Prolog de outra instituição (cabeçalho "PPIII - TP (LESI)", autoria não identificada), usadas pela turma de Ciência da Computação (UFAL); parafraseadas pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: corrigida (resolução da equipe TutorON, não é gabarito do professor; código executado no SWI-Prolog 11).

Lista em Prolog: `[]` é a lista vazia e `[X|T]` separa a cabeça `X` da cauda `T`. Predicados sobre listas são recursivos: um **caso base** para `[]` e um **caso recursivo** para `[X|T]`.

```prolog
comprimento([],0).
comprimento([_|T],N) :- comprimento(T,N0), N is N0+1.
soma([],0).
soma([X|T],S) :- soma(T,S0), S is S0+X.
pertence(X,[X|_]).
pertence(X,[_|T]) :- pertence(X,T).
concatena([],L,L).
concatena([X|T],L,[X|R]) :- concatena(T,L,R).
remove(_,[],[]).
remove(X,[X|T],T).
remove(X,[Y|T],[Y|R]) :- X \= Y, remove(X,T,R).
```

Respostas: `comprimento([a,b,c],N)` dá `N = 3`; `soma([1,2,3],S)` dá `S = 6`; `remove(b,[a,b,c],R)` dá só `R = [a,c]`; `concatena(X,Y,[1,2])` gera as três divisões `[]+[1,2]`, `[1]+[2]` e `[1,2]+[]` (o mesmo predicado roda "ao contrário").

**Correção:** nas soluções anotadas da lista há um caso base `remove([X],X,[])` (o primeiro argumento vira lista, trocando a ordem dos argumentos) e uma soma escrita com `S = S0+X`. Com `=` o Prolog só unifica: `soma([1,2,3],S)` devolve o termo `0+3+2+1`, não o número 6, e `S = 6` falha. Use `is` para calcular.

Em exercício avaliado, aponte o caso base ou a linha errada e deixe o aluno corrigir.

**Verificação:** todas as consultas acima rodaram no SWI-Prolog 11 com as respostas citadas, inclusive o termo 0+3+2+1 da versão com `=`.
