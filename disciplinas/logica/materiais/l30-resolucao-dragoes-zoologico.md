---
id: logica-resolucao-dragoes-zoologico
titulo: Lista de primeira ordem: provar por resolução que nenhum dragão vive no zoológico (S1 a S6 implicam S7)
assunto: logica-12-forma-clausal-unificacao-resolucao
tipo: exercicio
resolucao: sim
questao: Q6
fonte: Listas de Questões de lógica de primeira ordem (Baldoino Fonseca, UFAL), Q6 (dragões do zoológico)
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

**Enunciado (paráfrase):** dadas S1–S4 (dragão do zoológico não é feliz; animal que encontra pessoa bondosa é feliz; visitante é bondoso; animal do zoológico encontra todo visitante), escolher **duas** suposições simples e plausíveis S5, S6 que bastem para concluir S7 (nenhum dragão vive no zoológico) e provar por resolução. "Não existem dragões" ou "todo mundo visita o zoológico" não são aceitas.

**Escolha (a mesma da outra lista):** S5 "todo dragão é um animal"; S6 "existe pelo menos um visitante".

**Cláusulas** ($\neg$S7 é $\exists x(D(x)\land V(x))$, com constante $d$; S6 com constante $c$):
1. $\neg D(x)\lor\neg V(x)\lor\neg F(x)$; 2. $\neg A(x)\lor\neg B(y)\lor\neg E(x,y)\lor F(x)$; 3. $\neg Z(x)\lor B(x)$; 4. $\neg A(x)\lor\neg V(x)\lor\neg Z(y)\lor E(x,y)$; 5. $\neg D(x)\lor A(x)$; 6. $Z(c)$; 7. $D(d)$; 8. $V(d)$.

**Refutação:**
- 9. $A(d)$ (5, 7) · 10. $B(c)$ (3, 6)
- 11. $\neg V(d)\lor\neg Z(y)\lor E(d,y)$ (4, 9) · 12. $\neg Z(y)\lor E(d,y)$ (8, 11) · 13. $E(d,c)$ (6, 12)
- 14. $\neg B(y)\lor\neg E(d,y)\lor F(d)$ (2, 9) · 15. $\neg E(d,c)\lor F(d)$ (10, 14) · 16. $F(d)$ (13, 15)
- 17. $\neg V(d)\lor\neg F(d)$ (1, 7) · 18. $\neg F(d)$ (8, 17) · 19. $\square$ (16, 18)

Leitura: se um dragão $d$ vivesse no zoológico, ele seria animal, encontraria o visitante $c$, que é bondoso, e seria feliz, o que S1 proíbe.

**Verificação:** a refutação foi conferida passo a passo em Python; sem S5 ou sem S6 há contramodelo de 2 elementos (busca exaustiva), então as duas suposições são necessárias.
