---
id: logica-resolucao-proposicional
titulo: Resolução proposicional: forma clausal, resolvente, refutação e exemplos dos slides
assunto: logica-06-resolucao-proposicional
tipo: material_estudo
resolucao: sim
fonte: Slides Linguagens Proposicionais (Baldoino Fonseca, UFAL), método da resolução
fontes_catalogo: ufal-baldoino-slides-proposicional
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

**Forma clausal:** conjunto de cláusulas; cláusula é um conjunto de literais (lido como disjunção); $\square$ é a cláusula vazia (falsa).

**Regra da resolução:** de $C_1\cup\{p\}$ e $C_2\cup\{\neg p\}$ infere-se o **resolvente** $C_1\cup C_2$. Ex.: $\{\neg P,Q\}$ e $\{\neg Q,\neg R,P\}$ resolvidos em $Q$ dão $\{\neg P,\neg R,P\}$ (cláusula válida, inútil para refutar).

**Refutação:** sequência de cláusulas, cada uma do conjunto ou resolvente de duas anteriores, terminando em $\square$. **Teorema:** um conjunto de cláusulas é insatisfazível se e somente se tem refutação. Para provar $\Gamma\models\alpha$: ponha $\Gamma\cup\{\neg\alpha\}$ em forma clausal e derive $\square$ (é o T2 da consequência lógica).

**João e Maria** ($\models A$): 1. $\{\neg B, A\}$; 2. $\{\neg A, \neg B\}$; 3. $\{A, B\}$; 4. $\{\neg A\}$ (negação da conclusão); 5. $\{B\}$ (3, 4); 6. $\{A\}$ (1, 5); 7. $\square$ (4, 6).

**Exemplo** $P\leftrightarrow(Q\land R),\;P\to(\neg Q\lor S)\models(Q\land R)\to S$: a negação da conclusão dá $Q$, $R$, $\neg S$. 1. $\{\neg P, Q\}$; 2. $\{\neg P, R\}$; 3. $\{\neg Q, \neg R, P\}$; 4. $\{\neg P, \neg Q, S\}$; 5. $\{Q\}$; 6. $\{R\}$; 7. $\{\neg S\}$; 8. $\{\neg P, \neg Q\}$ (4, 7); 9. $\{\neg P\}$ (5, 8); 10. $\{\neg Q, \neg R\}$ (3, 9); 11. $\{\neg Q\}$ (6, 10); 12. $\square$ (5, 11).

**Verificação:** cada resolvente foi recalculado em Python a partir das duas cláusulas citadas, e os dois conjuntos foram confirmados insatisfazíveis por tabela-verdade.
