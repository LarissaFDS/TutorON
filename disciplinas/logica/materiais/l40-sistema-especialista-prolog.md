---
id: logica-sistema-especialista-prolog
titulo: Sistema especialista em Prolog: base de regras, perguntas ao usuário e pontuação
assunto: logica-14-programacao-logica-prolog
tipo: material_estudo
resolucao: sim
fonte: Projeto ExpertSystem-GUI (dados.pl e main.pl) da pasta da turma de Ciência da Computação (UFAL); estrutura descrita, exemplo próprio da equipe
curso: Ciência da Computação (UFAL), turma da Profa. Roberta Lopes, COMP360
fontes_catalogo: cc-expertsystem-gui
autoria: Material de Prolog da turma de Ciência da Computação (UFAL), autoria dos arquivos não identificada; exemplos próprios da equipe TutorON escritos com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; código executado no SWI-Prolog 11).

Um **sistema especialista** guarda conhecimento de um domínio como fatos e regras e faz perguntas ao usuário até chegar a uma conclusão. O projeto da turma tem três partes, que servem de modelo:
1. **base de conhecimento** (`dados.pl`): hipóteses, perguntas e, para cada pergunta, a lista das hipóteses que ela apoia;
2. **memória de trabalho** dinâmica (`:- dynamic`): uma pontuação por hipótese, alterada com `retract` e `asserta` a cada resposta "sim";
3. **interface** (`main.pl`): janelas da biblioteca gráfica XPCE (`new/2`, `send/2`, `dialog`, `button`) para perguntar e mostrar o resultado em porcentagem.

Exemplo próprio, mínimo e sem interface gráfica (identificar um animal):

```prolog
:- dynamic pontos/2.
pontos(gato,0). pontos(pato,0).
pergunta(p1,'Tem penas?',[pato]).
pergunta(p2,'Mia?',[gato]).
sim([]).
sim([H|T]) :- retract(pontos(H,N)), N1 is N+1, asserta(pontos(H,N1)), sim(T).
responde(Q,s) :- pergunta(Q,_,Hs), sim(Hs).
responde(_,n).
melhor(H) :- findall(N-X, pontos(X,N), L), max_member(_-H, L).
```

Respondendo `responde(p1,s)` e `responde(p2,n)`, `melhor(H)` dá `H = pato`. Isso é **encadeamento por pontuação**; um sistema por regras usaria `diagnostico(X) :- sintoma(a), sintoma(b).`, provado para trás (backward chaining) pelo próprio Prolog.

Projeto avaliado: o tutor explica a arquitetura e ajuda a depurar, sem escrever o sistema.

**Verificação:** o exemplo rodou no SWI-Prolog 11 e respondeu H = pato.
