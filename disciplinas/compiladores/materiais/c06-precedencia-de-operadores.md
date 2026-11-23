---
id: comp-analisador-de-precedencia-de-operadores-gramatica-de-operadores-relacoes-menor-igual-maior-tabela-de-precedencia
titulo: Análise por precedência de operadores: gramática de operadores, relações ⋖ ≐ ⋗, tabela de precedência, empilha e reduz; questão de 2017.1
assunto: comp-02-analise-sintatica
tipo: exercicio_resolvido
questao: questões 8 e 9 da AB1 de 2017.1 e tabela de precedência dos trabalhos
resolucao: sim
fonte: Enunciados dos trabalhos de Compiladores de 2017.1 (IC-UFAL)
curso: Ciência da Computação (UFAL), COMP263 Compiladores; provas de 2013 a 2017.1 e trabalhos de 2017.1 (o código ECOM045 aparece no cabeçalho da AB1 de 2017.1)
fontes_catalogo: ufal-compiladores-provas,ufal-compiladores-trabalhos
autoria: Enunciados do IC-UFAL; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Compiladores (Ciência da Computação), questões 8 e 9 da AB1 de 2017.1 e tabela de precedência dos trabalhos (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Gramática de operadores:** nenhuma produção tem dois não-terminais seguidos nem deriva a vazia; deve estar simplificada. Problema típico: o **mesmo token com aridades diferentes** (o `-` unário e o binário), que o léxico precisa distinguir com tokens diferentes.

**Relações entre terminais:** $a \lessdot b$ ($b$ tem precedência maior: empilha), $a \doteq b$ (mesmo handle, como `(` e `)`), $a \gtrdot b$ ($a$ tem precedência maior: reduz). Associatividade à esquerda: $+ \gtrdot +$; à direita: $\wedge \lessdot \wedge$; operador **não associativo**: célula de erro.

**Algoritmo:** compare o terminal mais alto da pilha com o token; se $\lessdot$ ou $\doteq$, empilha; se $\gtrdot$, desempilha até achar um $\lessdot$ e reduz o handle. Em `id + id * id`: reduz o primeiro `id`, empilha `+`, reduz o segundo `id`, empilha `*` (pois $+ \lessdot *$), reduz o terceiro `id`, reduz `E * E`, reduz `E + E`.

**AB1 de 2017.1, questão 9:** precedência `not` > `opr` > `or`; `opr` não associativo, `not` à direita, `or` à esquerda;
$S = 'if'\ Eb\ 'then'\ S\ 'else'\ S\ 'end'\ ';' \mid 'id'\ '='\ Eb\ ';'$ e
$Eb = Eb\ 'or'\ Eb \mid Eb\ 'opr'\ Eb \mid 'not'\ Eb \mid 'true' \mid 'false' \mid 'id'$.

a) **É** gramática de operadores: não há não-terminais vizinhos nem vazia.

b) **LL(1) equivalente**, um nível por precedência:
- $Eb = Rel\ Or'$; $Or' = 'or'\ Rel\ Or' \mid \varepsilon$ (repetição: associa à esquerda);
- $Rel = Not\ Rel'$; $Rel' = 'opr'\ Not \mid \varepsilon$ (no máximo um `opr`: não associativo);
- $Not = 'not'\ Not \mid 'true' \mid 'false' \mid 'id'$ (recursão à direita).

Juntar tudo num só nível, como em uma resposta da cópia, perde a precedência.

**Verificação:** `test_precedencia_de_operadores` roda o analisador de precedência e confere que a gramática b) é LL(1), respeita a precedência e recusa `id opr id opr id`.
