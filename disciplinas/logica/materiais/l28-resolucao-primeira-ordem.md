---
id: logica-resolucao-primeira-ordem
titulo: Resolução de primeira ordem (Robinson): resolvente com u.m.g., fatores, refutação e o exemplo "depende"
assunto: logica-12-forma-clausal-unificacao-resolucao
tipo: material_estudo
resolucao: sim
fonte: Slides de Resolução (Baldoino Fonseca, UFAL)
fontes_catalogo: ufal-baldoino-slides-primeira-ordem
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

A resolução de Robinson (início dos anos 1960) vem do teorema de Herbrand, mas não gera instâncias básicas: usa o **u.m.g.** para igualar dois literais de sinais opostos no próprio passo.

**Resolvente binário:** de $A'$ e $A''$ (com variáveis renomeadas para não coincidirem), escolha $L'\in A'$ e $L''\in A''$ de sinais opostos cujos átomos tenham u.m.g. $\theta$; o resolvente é $(A'\theta-L'\theta)\cup(A''\theta-L''\theta)$. **Fator:** aplicar o u.m.g. de dois literais da mesma cláusula, que se fundem. A regra geral resolve fatores. **Refutação:** derivar $\square$; um conjunto é insatisfazível se e somente se tem refutação.

**Exemplo dos slides** (chama, usa, depende): 1. $chama(a,b)$; 2. $usa(b,e)$; 3. $\neg chama(x,y)\lor depende(x,y)$; 4. $\neg usa(x,y)\lor depende(x,y)$; 5. $\neg depende(x,z)\lor\neg depende(z,y)\lor depende(x,y)$ (transitividade); 6. $\neg depende(a,e)$ (negação do que se quer provar).
- 7. $depende(a,b)$, de 1 e 3 com $\{x/a,\;y/b\}$;
- 8. $depende(b,e)$, de 2 e 4 com $\{x/b,\;y/e\}$;
- 9. $\neg depende(b,y)\lor depende(a,y)$, de 5 e 7 com $\{x/a,\;z/b\}$;
- 10. $depende(a,e)$, de 8 e 9 com $\{y/e\}$;
- 11. $\square$, de 6 e 10.

Logo $a$ depende de $e$ (por transitividade: $a$ chama $b$, que usa $e$).

**Literal de resposta (Lista, Q9):** de $\{\neg P(x,y)\lor R(x)\lor Q(a),\;\neg R(x)\lor Q(f(x)),\;P(a,b)\}$ segue $\exists x\,Q(x)$: com $\neg Q(z)$ chega-se a $\square$ via $R(a)\lor Q(a)$, $R(a)$, $Q(f(a))$. Trocando $\neg Q(z)$ por $\neg Q(z)\lor r(z)$, a mesma refutação termina em $r(f(a))\lor r(a)$: a resposta é "$x=a$ ou $x=f(a)$" (não dá para saber qual).

**Verificação:** cada resolvente foi recalculado em Python (renomeação, u.m.g. e resolvente), inclusive a versão com literal de resposta.
