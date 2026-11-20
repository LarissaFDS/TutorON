---
id: discreta-nocoes-logica
titulo: Noções básicas — proposições, conectivos, tabela-verdade e equivalências
assunto: discreta-01-nocoes-logica
tipo: material_estudo
fonte: Slides do Prof. Lucas Amorim (UFAL), Aula 01; notas de aula do Prof. Pablo Sampaio (UFRPE), aulas 2 a 5, lista 1 e tabela de leis de equivalência; slides do Prof. Leandro Balby Marinho (UFCG), Lógica
fontes_catalogo: ufal-discreta-slides-lucas,ufrpe-discreta-pablo,ufcg-discreta-leandro
autoria: Prof. Lucas Amorim (IC/UFAL), Prof. Pablo Sampaio (UFRPE) e Prof. Leandro Balby Marinho (UFCG), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material dos professores)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Matemática Discreta estuda **estruturas** (conjuntos, inteiros, relações, funções, grafos), **afirmações** sobre elas e **como provar** essas afirmações. A lógica entra como ferramenta; o estudo formal da lógica é assunto de Lógica Aplicada à Computação.

**Proposição** é uma frase declarativa que é verdadeira (V) ou falsa (F). Conectivos: negação $\neg p$ ("não p"), conjunção $p \land q$ ("p e q"), disjunção $p \lor q$ ("p ou q", inclusivo), condicional $p \to q$ ("se p então q") e bicondicional $p \leftrightarrow q$ ("p se e somente se q").

O condicional $p \to q$ só é falso quando p é V e q é F. Exemplo da lista 1 do Prof. Pablo: com p e q verdadeiras e r e s falsas, $q \to (p \lor r)$ vale V → (V ∨ F) = V → V = V.

Equivalências mais usadas (conferidas pela tabela-verdade):
- De Morgan: $\neg(p \land q) \equiv \neg p \lor \neg q$ e $\neg(p \lor q) \equiv \neg p \land \neg q$.
- Condicional: $p \to q \equiv \neg p \lor q$; contrapositiva: $p \to q \equiv \neg q \to \neg p$. A **recíproca** $q \to p$ **não** é equivalente.
- Negação do condicional: $\neg(p \to q) \equiv p \land \neg q$.
- Absorção $p \lor (p \land q) \equiv p$ e dupla negação $\neg\neg p \equiv p$.

Regras de inferência que aparecem nas demonstrações: **modus ponens** (de p e p → q, conclua q), **modus tollens** (de ¬q e p → q, conclua ¬p), silogismo hipotético (de p → q e q → r, conclua p → r) e silogismo disjuntivo (de p ∨ q e ¬p, conclua q).

Tautologia é uma fórmula verdadeira em todas as linhas da tabela; contradição, falsa em todas. Exemplo: $((p \to q) \land p) \to q$ é tautologia (é o modus ponens).

**Verificação:** as equivalências e a tautologia acima foram conferidas por código em todas as atribuições de V/F.
