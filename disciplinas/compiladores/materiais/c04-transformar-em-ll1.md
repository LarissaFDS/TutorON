---
id: comp-transformar-gramatica-em-ll1-fatoracao-a-esquerda-eliminar-recursao-a-esquerda-conflito-first-follow
titulo: Transformar uma gramática em LL(1): fatoração à esquerda, eliminação da recursão à esquerda e conflito FIRST/FOLLOW (prova de 2009)
assunto: comp-02-analise-sintatica
tipo: exercicio_resolvido
questao: questão 5 da prova de 2009
resolucao: sim
fonte: Provas de Compiladores do Prof. Marcus Ramos (2009 e 2010), cópias da pasta da turma
curso: Ciência da Computação (UFAL), COMP263 Compiladores; provas de 2013 a 2017.1 e trabalhos de 2017.1 (o código ECOM045 aparece no cabeçalho da AB1 de 2017.1)
fontes_catalogo: ramos-provas-compiladores
autoria: Questões e respostas das provas do Prof. Marcus Ramos; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Compiladores (Ciência da Computação), questão 5 da prova de 2009 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Para usar um analisador descendente preditivo, a gramática precisa ser LL(1): é preciso eliminar a recursão à esquerda, fatorar à esquerda e tirar os conflitos com a vazia.

**Transformações:**
- **fatoração à esquerda:** $A \to \alpha\beta_1 \mid \alpha\beta_2$ vira $A \to \alpha A'$, $A' \to \beta_1 \mid \beta_2$;
- **recursão à esquerda:** $A \to A\alpha \mid \beta$ vira $A \to \beta A'$, $A' \to \alpha A' \mid \varepsilon$. Exemplo: $E \to E + T \mid T$ vira $E \to T E'$, $E' \to + T E' \mid \varepsilon$;
- **conflito com a vazia:** se FIRST de uma alternativa cruza o FOLLOW, reescreva a linguagem daquele trecho.

**Gramática da prova:** $S \to aXb \mid aYc \mid aaZd$, $X \to bX \mid bc$, $Y \to cY \mid cb$, $Z \to dZ \mid \varepsilon$.

**Não é LL(1):** as três alternativas de $S$ começam com $a$; $X$ tem duas alternativas com $b$; $Y$, duas com $c$; e FIRST$(dZ) = \{d\}$ cruza FOLLOW$(Z) = \{d\}$.

**Gramática equivalente LL(1):**
- $S \to a\,S'$; $S' \to X b \mid Y c \mid a\,d\,Z$;
- $X \to b\,X'$; $X' \to X \mid c$;
- $Y \to c\,Y'$; $Y' \to Y \mid b$;
- $Z \to d\,Z \mid \varepsilon$.

Por que $a\,d\,Z$: $aZd$ gera $a\,d^n d$, isto é, $a$ seguido de **pelo menos um** $d$; escrever $a\,d\,Z$ põe o $d$ obrigatório antes, e agora FOLLOW$(Z) = \{\$\}$ não cruza $\{d\}$.

**Prova de que é LL(1):** $S'$: $\{b\}, \{c\}, \{a\}$; $X'$: $\{b\}, \{c\}$; $Y'$: $\{c\}, \{b\}$; $Z$: $\{d\}$ e FOLLOW $\{\$\}$. Todos disjuntos.

**Verificação:** `test_transformacao_ll1` confere que a nova gramática não tem conflitos e gera as mesmas cadeias (até um tamanho) que a original.
