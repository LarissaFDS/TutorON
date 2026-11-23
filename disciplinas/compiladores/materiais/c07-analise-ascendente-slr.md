---
id: comp-analise-ascendente-empilha-reduz-handle-lr0-slr1-tabela-action-goto-reducoes-mais-a-esquerda
titulo: Análise ascendente: empilha e reduz, handle, itens LR(0), tabela SLR(1) (ACTION e GOTO) e sequência de reduções
assunto: comp-02-analise-sintatica
tipo: exercicio_resolvido
questao: questões de análise ascendente das provas de 2009 e dos trabalhos de 2017.1
resolucao: sim
fonte: Provas de Compiladores do Prof. Marcus Ramos (2009 e 2010), cópias da pasta da turma
curso: Ciência da Computação (UFAL), COMP263 Compiladores; provas de 2013 a 2017.1 e trabalhos de 2017.1 (o código ECOM045 aparece no cabeçalho da AB1 de 2017.1)
fontes_catalogo: ramos-provas-compiladores,ufal-compiladores-trabalhos
autoria: Questões e respostas das provas do Prof. Marcus Ramos; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Compiladores (Ciência da Computação), questões de análise ascendente das provas de 2009 e dos trabalhos de 2017.1 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Descendente × ascendente:** o descendente parte do símbolo inicial e faz derivações mais à esquerda; o **ascendente** parte da cadeia e faz **reduções**: a ordem inversa de uma derivação mais à direita. **Determinística** = cada movimento sem retrocesso.

**Handle:** a subcadeia que casa com o lado direito de uma produção e cuja redução leva de volta ao símbolo inicial.

**SLR(1):**
1. aumente a gramática com $S' \to S$;
2. monte os conjuntos de **itens LR(0)** ($A \to \alpha \cdot \beta$) com fechamento e transição;
3. ACTION: item $A \to \alpha \cdot a\beta$ dá *empilha*; item completo $A \to \alpha\cdot$ dá *reduz* em cada $a \in$ FOLLOW$(A)$; $S' \to S\cdot$ dá *aceita*; GOTO para os não-terminais;
4. dois movimentos na mesma célula = conflito (a gramática não é SLR(1)).

**Exemplo:** $E \to E + T \mid T$, $T \to T * F \mid F$, $F \to (E) \mid id$ tem **12 estados** LR(0) e nenhum conflito SLR(1). Para `id * id + id` as reduções saem nesta ordem:
$F \to id$, $T \to F$, $F \to id$, $T \to T * F$, $E \to T$, $F \to id$, $T \to F$, $E \to E + T$, e aceita.

O `*` é empilhado com $T$ no topo (não reduz para $E$) porque o item $T \to T \cdot * F$ manda empilhar; o `+` provoca as reduções $T \to T * F$ e $E \to T$ porque $+$ está em FOLLOW$(T)$ e em FOLLOW$(E)$ e nenhum item daqueles estados empilha `+`.

**Verificação:** `test_slr` constrói os itens LR(0) e a tabela SLR(1) e reproduz as reduções.
