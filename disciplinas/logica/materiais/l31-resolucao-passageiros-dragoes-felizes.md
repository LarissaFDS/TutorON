---
id: logica-resolucao-passageiros-dragoes-felizes
titulo: Lista de primeira ordem: policiais desonestos (passageiros, candidatos) e dragões verdes felizes por resolução
assunto: logica-12-forma-clausal-unificacao-resolucao
tipo: exercicio
resolucao: sim
questao: Q3, Q8, Q11
fonte: Listas de Questões de lógica de primeira ordem (Baldoino Fonseca, UFAL), Q3 (dragões felizes), Q8 (candidatos) e Q11 (passageiros)
fontes_catalogo: ufal-baldoino-lista-primeira-ordem
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exercício da turma (paráfrase do enunciado) com resolução. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Q11 (passageiros):** S1–S3 implicam S4 "alguns policiais são desonestos". Cláusulas: 1. $\neg E(x)\lor V(x)\lor vd(x,f(x))$; 2. $\neg E(x)\lor V(x)\lor P(f(x))$ (S1, Skolem $f$); 3. $D(a)$; 4. $E(a)$; 5. $\neg vd(a,y)\lor D(y)$ (S2, constante $a$); 6. $\neg D(x)\lor\neg V(x)$ (S3); 7. $\neg D(x)\lor\neg P(x)$ ($\neg$S4).
- 8. $\neg V(a)$ (3, 6) · 9. $V(a)\lor vd(a,f(a))$ (1, 4) · 10. $vd(a,f(a))$ (8, 9) · 11. $D(f(a))$ (5, 10)
- 12. $V(a)\lor P(f(a))$ (2, 4) · 13. $P(f(a))$ (8, 12) · 14. $\neg P(f(a))$ (7, 11) · 15. $\square$ (13, 14)
O policial desonesto é $f(a)$, quem verificou os documentos de $a$. **Q8 (candidatos)** tem a mesma forma (juiz eleitoral no lugar de policial, juiz federal no lugar de VIP) e S5 "existe juiz eleitoral que não é federal" também segue: $f(a)$ é eleitoral e desonesto, logo não é federal.

**Q3 (dragões felizes):** (a) "feliz se todos os filhos voam": $genitor(x,f(x))\lor feliz(x)$ e $\neg voa(f(x))\lor feliz(x)$; (b) $\neg verde(x)\lor voa(x)$; (c) "verde se algum genitor é verde": $\neg genitor(y,x)\lor\neg verde(y)\lor verde(x)$. Negação de (d) "dragões verdes são felizes": $verde(a)$, $\neg feliz(a)$.
- 7. $genitor(a,f(a))$ (1, 6) · 8. $\neg voa(f(a))$ (2, 6) · 9. $\neg verde(f(a))$ (3, 8)
- 10. $\neg verde(a)\lor verde(f(a))$ (4, 7) · 11. $verde(f(a))$ (5, 10) · 12. $\square$ (9, 11)

**Verificação:** as duas refutações foram conferidas passo a passo em Python; a consequência S5 de Q8 foi testada sem contramodelo em universos de até 2 elementos.
