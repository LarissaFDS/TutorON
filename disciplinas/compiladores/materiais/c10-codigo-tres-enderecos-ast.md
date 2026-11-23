---
id: comp-codigo-de-tres-enderecos-quadruplas-arvore-de-sintaxe-abstrata-ast-grafo-de-sintaxe-dag-temporarios
titulo: Código de três endereços (quádruplas e triplas), árvore de sintaxe abstrata e grafo de sintaxe (DAG) para x = a * b + c - (b + c) / d
assunto: comp-03-semantica-e-codigo-intermediario
tipo: exercicio_resolvido
questao: questão 2 da prova de 2015.2
resolucao: sim
fonte: Provas de Compiladores do IC-UFAL (2013 a 2017.1)
curso: Ciência da Computação (UFAL), COMP263 Compiladores; provas de 2013 a 2017.1 e trabalhos de 2017.1 (o código ECOM045 aparece no cabeçalho da AB1 de 2017.1)
fontes_catalogo: ufal-compiladores-provas
autoria: Questões das provas de Compiladores do IC-UFAL; resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Compiladores (Ciência da Computação), questão 2 da prova de 2015.2 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Árvore de sintaxe abstrata (AST):** só operadores e operandos, sem os não-terminais da derivação. **Grafo de sintaxe (DAG):** a AST com subexpressões iguais compartilhadas, para não avaliar duas vezes.

**x = a * b + c - (b + c) / d** (precedência e associatividade usuais): a raiz é `-`; à esquerda `+(*(a, b), c)`, à direita `/(+(b, c), d)`.

**Código de três endereços** (quádruplas: operador, arg1, arg2, resultado):

| # | op | arg1 | arg2 | res |
|---|---|---|---|---|
| 0 | * | a | b | T1 |
| 1 | + | T1 | c | T2 |
| 2 | + | b | c | T3 |
| 3 | / | T3 | d | T4 |
| 4 | - | T2 | T4 | T5 |
| 5 | = | T5 | | x |

Em **triplas** o resultado é a posição: `(0) * a b`, `(1) + (0) c`, `(2) + b c`, `(3) / (2) d`, `(4) - (1) (3)`, `(5) = x (4)`.

**AST × DAG aqui:** `b + c` aparece uma vez e `a * b + c` não é a mesma subexpressão que `b + c`, então o DAG não compartilha nada e o código é o mesmo. Num caso como `(b + c) * (b + c)`, o DAG avalia `b + c` uma vez só.

**Verificação:** `test_tres_enderecos` executa as quádruplas e compara com a expressão para valores aleatórios.
