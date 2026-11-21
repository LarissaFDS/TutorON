---
id: logica-sintaxe-proposicional
titulo: Sintaxe da lógica proposicional: alfabeto, fórmulas bem formadas, precedência e tradução do português
assunto: logica-02-proposicional-sintaxe-semantica
tipo: material_estudo
resolucao: sim
fonte: Slides de Lógica Clássica Proposicional (Baldoino Fonseca, UFAL), sintaxe; slides Lógica Proposicional: sintaxe e semântica (Tiago Massoni, UFCG)
fontes_catalogo: ufal-baldoino-slides-proposicional, ufcg-massoni-slides
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

**Alfabeto:** constantes $\top$ (verdadeiro) e $\bot$ (falso), símbolos proposicionais $P, Q, R, \dots$, conectivos $\neg$ (não), $\land$ (e), $\lor$ (ou), $\to$ (se… então), $\leftrightarrow$ (se e somente se) e parênteses.

**Fórmulas bem formadas:** todo átomo é fórmula; se $A$ é fórmula, $\neg A$ é fórmula; se $A$ e $B$ são fórmulas, $(A\land B)$, $(A\lor B)$, $(A\to B)$ e $(A\leftrightarrow B)$ são fórmulas. Exercício dos slides: $\neg\neg\neg R$, $(\neg R)$, $\neg(P\to Q)$ e $\neg(\neg P\land\neg Q)$ são bem formadas; $PQ$ não é (dois átomos sem conectivo).

**Precedência** (convenção da UFCG e do livro de Huth e Ryan): $\neg$, depois $\land$, depois $\lor$, depois $\to$; $\to$ associa à direita. Assim $p\to q\land r$ lê-se $p\to(q\land r)$, e não $(p\to q)\land r$; e $p\to q\to r$ lê-se $p\to(q\to r)$. **Correção:** um slide de Baldoino lista a ordem "$\neg$; $\to,\leftrightarrow$; $\land,\lor$", que contradiz essa convenção; na dúvida, use parênteses.

**Tradução do português:** "mas", "embora", "contudo" são $\land$. "Se $P$ então $Q$", "$P$ implica $Q$", "$Q$ se $P$", "$P$ só se $Q$", "$P$ somente se $Q$" são todos $P\to Q$. "$P$ se e somente se $Q$" é $(P\to Q)\land(Q\to P)$.

**Verificação:** o leitor de fórmulas dos testes lê $p\to q\land r$ como $p\to(q\land r)$, e as duas leituras diferem na tabela-verdade ($p$=F, $r$=F dá V numa e F na outra).
