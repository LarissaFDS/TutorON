---
id: logica-lista-q5-q6-argumentos
titulo: Lista proposicional Q5 e Q6: argumentos de João e Maria (prêmios) e do catálogo de sementes
assunto: logica-03-consequencia-equivalencia
tipo: exercicio
resolucao: sim
questao: Q5-Q6
fonte: Lista de Questões de lógica proposicional (Baldoino Fonseca, UFAL), Q5 e Q6
fontes_catalogo: ufal-baldoino-lista-proposicional
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

**Q5 (paráfrase):** se João ganha o primeiro prêmio, Maria ganha o segundo ou José fica desapontado. Maria não ganha o segundo. Portanto, se José está desapontado, João não ganha o primeiro.
- $j$: João ganha o 1º; $m$: Maria ganha o 2º; $z$: José desapontado. Premissas $j\to(m\lor z)$ e $\neg m$; conclusão $z\to\neg j$.
- **Inválido.** Contraexemplo: $j$=V, $m$=F, $z$=V. As premissas ficam V ($m\lor z$ é V) e a conclusão fica V$\to$F = F. O que segue das premissas é $j\to z$ ("se João ganha, José fica desapontado"), não a recíproca.

**Q6 (paráfrase):** se o catálogo de sementes está correto, então, se as sementes são plantadas em abril, as flores brotam em julho. As flores não brotam em julho. Portanto, se as sementes são plantadas em abril, o catálogo não está correto.
- $c$: catálogo correto; $a$: plantadas em abril; $f$: flores brotam em julho. Premissas $c\to(a\to f)$ e $\neg f$; conclusão $a\to\neg c$.
- **Válido.** Por T2: premissas com $\neg(a\to\neg c)\equiv a\land c$ são insatisfazíveis: de $c$ e $a$ sai $f$, que contradiz $\neg f$. Em resolução: 1. $\{\neg c, \neg a, f\}$; 2. $\{\neg f\}$; 3. $\{a\}$; 4. $\{c\}$; 5. $\{\neg c, \neg a\}$ (1, 2); 6. $\{\neg a\}$ (4, 5); 7. $\square$ (3, 6).

**Verificação:** tabela-verdade em Python das 8 valorações de cada argumento; a refutação de Q6 foi conferida passo a passo.
