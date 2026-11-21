---
id: logica-lista-q3-consequencias
titulo: Lista proposicional Q3 (a–g): provar consequências por equivalências, tableaux e resolução (item d corrigido)
assunto: logica-03-consequencia-equivalencia
tipo: exercicio
resolucao: sim
questao: Q3
fonte: Lista de Questões de lógica proposicional (Baldoino Fonseca, UFAL), Q3
fontes_catalogo: ufal-baldoino-lista-proposicional
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Exercício da turma (paráfrase do enunciado) com resolução. Status da resolução: corrigida (resolução da equipe TutorON, não é gabarito do professor; conferida com Python; o original tem erro apontado abaixo).

A questão pede provar, por equivalências, tableaux e resolução, sete consequências. Resultado de cada uma:
- a) $p\to q,\;q\to r\models(q\to r)\to((p\to\neg r)\to\neg p)$: **válida**.
- b) $q\to(p\land r),\;\neg s\to\neg p,\;(p\land s)\to t\models q\to t$: **válida**. Resolução: 1. $\{\neg q, p\}$; 2. $\{\neg q, r\}$; 3. $\{s, \neg p\}$; 4. $\{\neg p, \neg s, t\}$; 5. $\{q\}$; 6. $\{\neg t\}$; 7. $\{p\}$ (1, 5); 8. $\{s\}$ (3, 7); 9. $\{\neg s, t\}$ (4, 7); 10. $\{t\}$ (8, 9); 11. $\square$ (6, 10).
- c) $(p\to(q\to r))\land\neg r\models q\to\neg p$: **válida**.
- d) $(p\to q)\lor(\neg r\to s)\models(p\land\neg r)\to(p\land s)$: **não vale**, embora o enunciado peça para provar. **Correção:** contraexemplo $p$=V, $q$=V, $r$=F, $s$=F: a premissa é V (porque $p\to q$ é V) e a conclusão é V$\to$F = F. O tableau deixa um ramo aberto e a resolução não chega a $\square$.
- e) $(p\to q)\land(r\to s)\models(p\lor r)\to(q\lor s)$: **válida**.
- f) $\neg((q\to\neg r)\to(p\to(r\to\neg p)))\models\neg((p\to q)\land(\neg r\to\neg q))$: **válida**. A premissa só é V com $p$=V, $q$=F, $r$=V (é preciso $q\to\neg r$ V e $p\to(r\to\neg p)$ F); nessa valoração $p\to q$ é F, então a conclusão é V.
- g) $\models(p\to q)\to((r\to s)\to((p\land s)\to(q\land s)))$: **válida** (tautologia, sem premissas).

**Verificação:** as sete consequências foram testadas por tabela-verdade completa em Python; a refutação de (b) foi conferida passo a passo; o contraexemplo de (d) foi avaliado.
