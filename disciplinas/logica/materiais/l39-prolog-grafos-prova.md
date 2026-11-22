---
id: logica-prolog-grafos-prova
titulo: Prova de Prolog com grafos: laço, grau e caminho
assunto: logica-14-programacao-logica-prolog
tipo: prova
resolucao: sim
fonte: Prova de Prolog sobre grafos, Profa. Roberta Lopes, aplicada em 21/03/2019 (Ciência da Computação, UFAL); enunciado parafraseado
curso: Ciência da Computação (UFAL), turma da Profa. Roberta Lopes, COMP360
semestre: nao_informado (prova aplicada em 21/03/2019)
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
Questão de prova (paráfrase do enunciado) com resolução. Prova é atividade avaliativa: o tutor guia, não entrega. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; código executado no SWI-Prolog 11).

Enunciado (paráfrase): um grafo é dado por fatos `aresta(X,Y)`. Escreva predicados para **laço** (aresta de um vértice nele mesmo), **grau** de um vértice, **caminho** entre dois vértices e, depois, para testar se um caminho é **elementar** (sem vértice repetido), **simples** (sem aresta repetida), **fechado** (começa e termina no mesmo vértice) e se é um **circuito**.

Resolução de amostra (só as três primeiras partes), com um grafo de teste próprio:

```prolog
aresta(a,b). aresta(b,c). aresta(c,a). aresta(c,c). aresta(c,d).
laco(V) :- aresta(V,V).
grau(V,G) :- findall(x, (aresta(V,_) ; aresta(_,V)), L), length(L,G).
caminho(X,Y,[X,Y]) :- aresta(X,Y).
caminho(X,Y,[X|P]) :- aresta(X,Z), X \= Z, caminho(Z,Y,P).
```

`laco(V)` dá `V = c`. `grau(c,G)` dá `G = 5`: as arestas b–c, c–a e c–d contam 1 cada e o laço c–c conta 2 (aparece como saída e como entrada), a convenção usual. `caminho(a,d,P)` dá primeiro `P = [a,b,c,d]`. Atenção: em grafo com ciclo, `caminho` pode gerar caminhos cada vez mais longos ao pedir mais soluções; guardar os vértices visitados resolve.

Para as partes restantes, o tutor guia: elementar é "a lista do caminho não tem repetidos" (pense em `pertence/2` ou em `sort/2` e comprimento); fechado compara o primeiro e o último elemento.

**Verificação:** laco/1, grau/2 e a primeira solução de caminho/3 rodaram no SWI-Prolog 11 com as respostas citadas.
