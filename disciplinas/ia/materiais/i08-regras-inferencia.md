---
id: ia-regras-de-inferencia-modus-ponens-modus-tollens-silogismo-hipotetico-dilema-construtivo-absorcao-simplificacao-conjuncao-adicao
titulo: Regras de inferência da lógica proposicional: modus ponens, modus tollens, silogismo hipotético e disjuntivo, dilema construtivo, absorção, simplificação, conjunção e adição; prova passo a passo
assunto: ia-03-conhecimento-e-raciocinio
tipo: lista
questao: slide de regras de inferência e Lista 1 (2020.2), questão de prova formal
resolucao: sim
fonte: Slide de regras de inferência da turma e Lista 1 de Inteligência Artificial (IC-UFAL), 2020.2, Prof. Evandro de Barros Costa
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufal-ia-listas-2020-2
autoria: Questões do Prof. Evandro de Barros Costa (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), slide de regras de inferência e Lista 1 (2020.2), questão de prova formal (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Regras** (todas corretas: a conclusão é consequência lógica das premissas):
1. **Modus ponens:** $P \to Q$, $P$ ⊢ $Q$;
2. **Modus tollens:** $P \to Q$, $\lnot Q$ ⊢ $\lnot P$;
3. **Silogismo hipotético:** $P \to Q$, $Q \to R$ ⊢ $P \to R$;
4. **Silogismo disjuntivo:** $P \lor Q$, $\lnot P$ ⊢ $Q$;
5. **Dilema construtivo:** $(P \to Q) \land (R \to S)$, $P \lor R$ ⊢ $Q \lor S$;
6. **Absorção:** $P \to Q$ ⊢ $P \to (P \land Q)$;
7. **Simplificação:** $P \land Q$ ⊢ $P$;
8. **Conjunção:** $P$, $Q$ ⊢ $P \land Q$;
9. **Adição:** $P$ ⊢ $P \lor Q$.

**Exercício da Lista 1 (forma da prova):** com as premissas (1) $S$, (2) $S \to T$, (3) $T \to P$, (4) $S \to V$, (5) $V \to Q$ e (6) $P \land Q \to R$, prove $R$:
- (7) $S \to P$, de 2 e 3 por silogismo hipotético;
- (8) $P$, de 7 e 1 por modus ponens;
- (9) $S \to Q$, de 4 e 5 por silogismo hipotético;
- (10) $Q$, de 9 e 1 por modus ponens;
- (11) $P \land Q$, de 8 e 10 por conjunção;
- (12) $R$, de 6 e 11 por modus ponens.

Numere cada linha e diga a regra e as linhas usadas. Não pule a conjunção antes de usar a regra com $P \land Q$.

**Verificação:** `test_regras_de_inferencia_corretas` confere por tabela-verdade que as 9 regras são corretas e que a prova chega a $R$.
