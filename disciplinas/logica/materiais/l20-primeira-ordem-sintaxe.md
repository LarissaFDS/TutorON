---
id: logica-primeira-ordem-sintaxe
titulo: Lógica de primeira ordem: termos, predicados, quantificadores, variáveis livres e ligadas, e como traduzir
assunto: logica-09-primeira-ordem-formalizacao
tipo: material_estudo
resolucao: sim
fonte: Slides Linguagens de Primeira Ordem (Baldoino Fonseca, UFAL); slides Lógica de predicados (Tiago Massoni, UFCG)
fontes_catalogo: ufal-baldoino-slides-primeira-ordem, ufcg-massoni-slides
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL) e Prof. Tiago Massoni (UFCG), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: corrigida (resolução da equipe TutorON, não é gabarito do professor; conferida com Python; o original tem erro apontado abaixo).

A lógica proposicional não exprime "todo", "existe", "apenas". A de primeira ordem acrescenta variáveis, **quantificadores** $\forall$ ("para todo") e $\exists$ ("existe"), constantes, símbolos funcionais e predicativos e, opcionalmente, igualdade.

**Termos:** variáveis, constantes e $f(t_1,\dots,t_n)$. **Fórmulas atômicas:** $P(t_1,\dots,t_n)$ e $t_1=t_2$; as demais com conectivos e $\forall x\,\varphi$, $\exists x\,\varphi$. O **escopo** de $\forall x$ em $\forall x(Q)$ é $Q$; uma ocorrência de $x$ é **ligada** se está no escopo de um quantificador em $x$, senão é **livre**. **Sentença** é fórmula sem variável livre.

**Padrões de tradução:**
- "Todo $A$ é $B$": $\forall x(A(x)\to B(x))$ (não use $\land$).
- "Algum $A$ é $B$": $\exists x(A(x)\land B(x))$ (não use $\to$).
- "Nenhum $A$ é $B$": $\neg\exists x(A(x)\land B(x))\equiv\forall x(A(x)\to\neg B(x))$.
- Ex.: "nenhum conjunto é elemento de si mesmo": $\neg\exists x(x\in x)$; "$x\subseteq y$ se e somente se todo elemento de $x$ está em $y$": $\forall x\forall y(x\subseteq y\leftrightarrow\forall z(z\in x\to z\in y))$.

**Correções nos slides de Baldoino:** "$-1\le\mathrm{sen}(x)\ge1$" deve ser $-1\le\mathrm{sen}(x)\le1$; o exemplo do ancestral deve ser "se $x$ é ancestral de $y$ e $y$ é ancestral de $z$, então $x$ é ancestral de $z$".

**Verificação:** os padrões "nenhum" foram conferidos como equivalentes em todos os modelos com universo de até 3 elementos (busca exaustiva em Python).
