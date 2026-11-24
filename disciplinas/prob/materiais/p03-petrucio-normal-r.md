---
id: prob-petrucio-normal-r
titulo: Normal no R com pnorm e qnorm: cartas por quinzena, enchedora de refrigerante (com binomial), discos fora de 3 desvios, garantia de TV, baterias e motores
assunto: prob-06-uniforme-normal
tipo: lista
questao: Lista de distribuições contínuas, Q1 a Q5, Q8, Q13
semestre: 2025.2
resolucao: sim
fonte: Lista "Distribuições Contínuas – Normal e Exponencial" do Prof. Petrucio A. Medeiros Barros (UFAL) | Q1 a Q5, Q8, Q13
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

No R: `pnorm(x, media, dp)` = P(X ≤ x); `1 - pnorm(...)` = P(X > x); `qnorm(prob, media, dp)` dá o valor com aquela probabilidade acumulada (usado para "qual garantia").

**Q1.** N(4000; 200): P(3600 < X < 4250) ≈ 0,8716; P(X < 3400) ≈ 0,0013; P(X > 4636) ≈ 0,0007.

**Q2.** N(1000; 10): P(X < 990) ≈ 0,1587; P(|X − 1000| ≤ 20) ≈ 0,9545. (c) Primeiro p = P(X > 1002) ≈ 0,4207; depois, em 10 garrafas, Y ~ Bin(10; p) e P(Y ≤ 4) ≈ 0,5803. A normal dá o p e a binomial conta as garrafas.

**Q3.** N(45; 20): p = P(X > 50) + P(X < 30) ≈ 0,6279; em 50 candidatos, cerca de 50p ≈ 31.

**Q4.** Defeito além de 0,03 cm = além de 3 desvios: 2 · `pnorm(-3)` ≈ 0,27%.

**Q5.** Vida N(8; 1,8), no máximo 5% de trocas: g = `qnorm(0.05, 8, 1.8)` ≈ 5,04 anos.

**Q8.** Baterias N(600; 100), garantia de 312 dias: P(X < 312) ≈ 0,0020; em 10.000 baterias, cerca de 20 trocas por mês.

**Q13.** Motores N(150000; 5000): P(X < 170000) ≈ 0,99997 (4 desvios acima); P(140000 < X < 165000) ≈ 0,9759; garantia com menos de 0,2% de trocas: `qnorm(0.002, 150000, 5000)` ≈ 135.609 km.

**Verificação:** valores refeitos com `scipy.stats` em `tests_acervo/test_disciplina_prob.py`.
