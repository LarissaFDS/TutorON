---
id: comp-analisador-descendente-preditivo-tabular-e-recursivo-tabela-ll1-pilha-movimentos
titulo: Analisador descendente preditivo: tabela LL(1), pilha e movimentos; versão recursiva; condições para usar
assunto: comp-02-analise-sintatica
tipo: exercicio_resolvido
questao: tabela preditiva dos trabalhos e questões de análise descendente de 2009 e 2015.2
resolucao: sim
fonte: Provas de Compiladores do IC-UFAL (2013 a 2017.1)
curso: Ciência da Computação (UFAL), COMP263 Compiladores; provas de 2013 a 2017.1 e trabalhos de 2017.1 (o código ECOM045 aparece no cabeçalho da AB1 de 2017.1)
fontes_catalogo: ufal-compiladores-provas,ramos-provas-compiladores
autoria: Questões das provas de Compiladores do IC-UFAL; resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Compiladores (Ciência da Computação), tabela preditiva dos trabalhos e questões de análise descendente de 2009 e 2015.2 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Descendentes:** recursivo com retrocesso (tentativa e erro, não determinístico), **preditivo recursivo** e **preditivo tabular**. Os preditivos exigem gramática sem recursão à esquerda, fatorada e com FIRST que identifique a produção (LL(1)).

**Tabela:** $M[A, a]$ recebe $A \to \alpha$ para cada $a \in$ FIRST$(\alpha)$; se $\alpha \Rightarrow^* \varepsilon$, também para cada $a \in$ FOLLOW$(A)$. Duas produções na mesma célula = conflito.

**Gramática de expressões:**
- $E \to T E'$; $E' \to + T E' \mid \varepsilon$;
- $T \to F T'$; $T' \to * F T' \mid \varepsilon$;
- $F \to (E) \mid id$.

| | id | + | * | ( | ) | \$ |
|---|---|---|---|---|---|---|
| $E$ | $TE'$ | | | $TE'$ | | |
| $E'$ | | $+TE'$ | | | $\varepsilon$ | $\varepsilon$ |
| $T$ | $FT'$ | | | $FT'$ | | |
| $T'$ | | $\varepsilon$ | $*FT'$ | | $\varepsilon$ | $\varepsilon$ |
| $F$ | id | | | $(E)$ | | |

**Algoritmo:** pilha começa com `$ E`. Se o topo é terminal igual ao token, desempilha e avança; se é não-terminal, troca pela produção $M[\text{topo}, \text{token}]$ (empilhada ao contrário); célula vazia é erro. Para `id + id * id` são 11 expansões, na ordem da derivação mais à esquerda: $E \to TE'$, $T \to FT'$, $F \to id$, $T' \to \varepsilon$, $E' \to +TE'$, $T \to FT'$, $F \to id$, $T' \to *FT'$, $F \to id$, $T' \to \varepsilon$, $E' \to \varepsilon$.

**Versão recursiva:** uma função por não-terminal que olha o token atual e escolhe a alternativa, por exemplo `E() { T(); E'(); }`, `E'() { if (tk == '+') { aceita('+'); T(); E'(); } }`. A recursão faz o papel da pilha.

**Verificação:** `test_preditivo_tabular` monta a tabela, confere que não há conflito e reconhece e rejeita cadeias.
