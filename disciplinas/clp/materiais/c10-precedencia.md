---
id: clp-precedencia-associatividade-ordem-de-avaliacao-c-maior-b-maior-a
titulo: Precedência e associatividade de operadores; numerar a ordem de avaliação numa tabela dada; r = c > b > a em C com associatividade à esquerda e à direita
assunto: clp-05-expressoes-e-controle
tipo: prova
questao: AB2 2011.2 Q1, Q4 e Q5; final 2012.2 Q7
resolucao: sim
fonte: Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (IC-UFAL)
curso: Ciência da Computação (UFAL), Conceitos de Linguagens de Programação (CCOM027); provas de 2011.2 a 2013.1
fontes_catalogo: ufal-alcino-provas-clp
autoria: Questões do Prof. Alcino Dall'Igna Jr. (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB2 2011.2 Q1, Q4 e Q5; final 2012.2 Q7 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Precedência:** regras que definem a ordem em que operadores de **níveis de prioridade diferentes** são avaliados (em geral, `*` e `/` antes de `+` e `-`). **Associatividade:** ordem em que **operadores adjacentes do mesmo nível** são avaliados (quase sempre da esquerda para a direita; a exponenciação costuma ser da direita para a esquerda).

**Numerar a ordem (AB2, Q4).** A tabela da prova, do maior para o menor nível: `*`, `/`, `not`; depois `+`, `-` (binários), `&`, `mod`; depois `-` unário; depois os relacionais; depois `and`; por fim `or`, `xor`; todos associativos à esquerda. Note que aqui o **menos unário tem prioridade menor que a soma**.
- `- a + b`: a soma vem primeiro (1) e o menos unário depois (2): $-(a + b)$. Resposta: `-`² `a` `+`¹ `b`.
- `a * (b - 1) / c mod d`: o parêntese primeiro (`-` = 1), depois `*` (2) e `/` (3), do mesmo nível, da esquerda para a direita, e por último `mod` (4), que é de nível menor.

Método: coloque parênteses de dentro para fora, primeiro o maior nível; dentro do mesmo nível, siga a associatividade.

**`r = c > b > a` com `a=5, b=6, c=7` (Q5), sabendo que o relacional dá 0 ou 1:**
- associativo à **esquerda** (é o caso de C): `(c > b) > a` = `(7 > 6) > 5` = `1 > 5` = **0**;
- associativo à **direita**: `c > (b > a)` = `7 > (6 > 5)` = `7 > 1` = **1**.
A comparação encadeada não significa "c > b e b > a" em C (em Python significa).

**Verificação:** `test_precedencia_e_associatividade` compila o código com gcc (sai 0), confere em Python que `7 > 6 > 5` é encadeado, e aplica um analisador por precedência com a tabela da prova às expressões (a) e (b), obtendo as ordens 2, 1 e 2, 1, 3, 4.
