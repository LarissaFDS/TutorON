---
id: prob-petrucio-soma-media-normais-r
titulo: Soma e média de normais: pacotes de queijo (média de 16 pacotes), elevador com 7 adultos e 3 lutadores de sumô até 850 kg; cirurgia ACL e quantil
assunto: prob-08-combinacao-linear
tipo: lista
questao: Lista de distribuições contínuas, Q7, Q9, Q14
semestre: 2025.2
resolucao: sim
fonte: Lista "Distribuições Contínuas – Normal e Exponencial" do Prof. Petrucio A. Medeiros Barros (UFAL) | Q7, Q9, Q14
curso: Engenharia de Computação (UFAL), ECOM020
autoria: Enunciados: lista do Prof. Petrucio A. Medeiros Barros, parafraseados pela equipe TutorON; as dicas de comando R são da lista; resolução da equipe TutorON, redigida com auxílio de IA e conferida com scipy.stats
licenca: Não declarada (material da disciplina); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia os enunciados e não reproduz a lista
fontes_catalogo: ufal-prob-petrucio-listas-r
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista de distribuições contínuas do Prof. Petrucio (enunciados parafraseados). Status da resolução: validada (a lista só traz as dicas de comando; os valores são da equipe TutorON, conferidos com `scipy.stats`).

Regra: numa soma de normais independentes, **somam-se as médias e as variâncias** (nunca os desvios padrão). A média de n valores tem desvio σ/√n.

**Q9.** Pacotes N(100; 10): P(95 < X < 105) ≈ 0,3829. A média de 16 pacotes tem desvio 10/√16 = 2,5: P(95 < X̄ < 105) ≈ 0,9545. A média varia bem menos que um pacote.

**Q14.** 7 adultos N(75; 8) e 3 lutadores N(110; 5). Total: média 7·75 + 3·110 = 855 kg; variância 7·64 + 3·25 = 523 (desvio ≈ 22,87). P(T > 850) ≈ 0,5865. A média do grupo já passa do limite, por isso a chance é maior que 50%.

**Q7.** Cirurgia ACL, N(129; 14): (a) P(X > 129 + 28) ≈ 0,0228; (b) P(X < 100) ≈ 0,0192; (c) `qnorm(0.95, 129, 14)` ≈ 152 min; (d) 199 min está 5 desvios acima da média: muito improvável nesse modelo, o que sugere um caso fora do padrão.

**Verificação:** valores refeitos com `scipy.stats` em `tests_acervo/test_disciplina_prob.py`.
