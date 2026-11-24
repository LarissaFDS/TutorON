---
id: prob-petrucio-exponencial-r
titulo: Exponencial no R com pexp e taxa 1/média: caixa de banco, motores com média de 28.500 horas, monitor LCD e falta de memória na reação enzimática
assunto: prob-07-exponencial
tipo: lista
questao: Lista de distribuições contínuas, Q6, Q10 a Q12
semestre: 2025.2
resolucao: sim
fonte: Lista "Distribuições Contínuas – Normal e Exponencial" do Prof. Petrucio A. Medeiros Barros (UFAL) | Q6, Q10 a Q12
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

No R, `pexp(x, rate)` usa a **taxa** λ = 1/média, não a média: com média de 5 minutos, `pexp(4, 1/5)`. P(X > x) = e^(−λx).

**Q6.** Caixa de banco, média 5 min (λ = 1/5): P(X > 5) = e^(−1) ≈ 0,3679; P(X < 4) ≈ 0,5507; P(3 < X < 8) = e^(−0,6) − e^(−1,6) ≈ 0,3469.

**Q10.** Motores, média 28.500 h: P(X ≤ 24.000) = 1 − e^(−24000/28500) ≈ 0,5692. (O enunciado troca "motores" por "ventiladores" no meio; é o mesmo equipamento.)

**Q11.** Monitor, média 5 ms: P(X ≤ 10) = 1 − e^(−2) ≈ 0,8647; P(5 < X < 10) = e^(−1) − e^(−2) ≈ 0,2325.

**Q12.** Reação, média 4.000 s: (a) P(X > 2000) = e^(−0,5) ≈ 0,6065. (b) P(X ≥ 6000 | X ≥ 4000) = P(X ≥ 2000) ≈ 0,6065, pela **falta de memória** da exponencial: o que já durou não muda o que falta. Por isso (a) e (b) dão o mesmo valor.

**Verificação:** valores refeitos com `scipy.stats` em `tests_acervo/test_disciplina_prob.py`.
