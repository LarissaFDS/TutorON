---
id: discreta-cc-relacoes-fecho-ordem
titulo: Que pares inserir para virar relação de equivalência; construir ordem parcial; composição de relações (provas de CC)
assunto: discreta-04-relacoes
tipo: resolucao
resolucao: sim
questao: Prova 1 2020.2 e 2021.1 (Q2, Q3); Reavaliação 1 2020.2 (Q2, Q3); Prova 1 de 2017 (Q4, Q5)
fonte: Provas do Prof. Bruno Pimentel (2020.2 e 2021.1) e Prova Escrita 01 do Prof. Lucas Amorim (2017)
curso: Ciência da Computação (UFAL), turmas de 2017 (Prof. Lucas Amorim) e 2020.2/2021.1 (Prof. Bruno Pimentel)
fontes_catalogo: ufal-cc-discreta-provas-bruno,ufal-cc-discreta-prova-lucas-2017
autoria: Profs. Bruno Pimentel e Lucas Amorim (IC-UFAL), enunciados parafraseados; resolução da equipe TutorON com auxílio de IA
licenca: Não declarada (provas do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia os enunciados e traz resolução própria; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Resolução da equipe TutorON, não é gabarito do professor. Status da resolução: validada.

**Quais pares inserir para virar equivalência?** Calcule o **fecho**: some os pares reflexivos $(a,a)$, depois os simétricos, depois os que a transitividade exige, e repita até nada mudar. É mais fácil pensar nas **classes**: quem está ligado a quem.

Em $\{0,1,2,3\}$, $R=\{(0,0),(1,1),(1,3),(3,0)\}$: 1–3 e 3–0 ligam {0,1,3}; 2 fica sozinho. Faltam $(0,1),(0,3),(1,0),(3,1),(3,3),(2,2)$; o fecho tem 10 pares. Com $R=\{(0,1),(1,2),(3,3)\}$, as classes são {0,1,2} e {3}: também 10 pares no fim.

Quando a relação liga os quatro elementos numa só classe (caso da prova de 2020.2), o fecho é $A\times A$, com 16 pares.

**Ordem parcial** = reflexiva, antissimétrica e transitiva. Em $\{1,2,3,4\}$ servem $\le$ ou "divide". Se a ordem precisa conter $(3,2)$ e $(2,4)$, a transitividade obriga $(3,4)$: a menor é $\{(1,1),(2,2),(3,3),(4,4),(3,2),(2,4),(3,4)\}$. Esquecer os pares $(a,a)$ é o erro mais comum.

**Relação dada por grafo** (prova de 2017: laço em 1, setas 1→2, 1→3, 1→4, 1→5, 2→5, 3→4): não é reflexiva (falta o laço em 2), não é simétrica (há 1→2 sem 2→1) e é transitiva (todo caminho de duas setas tem atalho: 1→2→5 e 1→5; 1→3→4 e 1→4).

**Composição** $S\circ R$: primeiro R, depois S; $(a,c)\in S\circ R$ se há b com $(a,b)\in R$ e $(b,c)\in S$. Com $R=\{(1,a),(2,a),(1,b),(3,b)\}$ e $S=\{(a,j),(b,w)\}$: $S\circ R=\{(1,j),(2,j),(1,w),(3,w)\}$. Se S começa em elementos que R nunca atinge, como $\{(1,j),(2,w)\}$, a composição é vazia.

**Verificação:** fechos, propriedades e composições foram calculados em Python, que também confirmou que a ordem parcial proposta é reflexiva, antissimétrica e transitiva.
