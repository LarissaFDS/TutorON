---
id: prob-petrucio-binomial-r
titulo: Binomial no R com dbinom e pbinom: componentes cerâmicos com 12% de defeito em lote de 40, carteira de 15 ações, tubulações e moeda
assunto: prob-05-distribuicoes-discretas
tipo: lista
questao: Lista de VA discretas, Q1, Q2, Q4 a Q7
semestre: 2025.2
resolucao: sim
fonte: Lista "Variáveis Aleatórias Discretas" do Prof. Petrucio A. Medeiros Barros (UFAL) | Q1, Q2, Q4 a Q7
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
Lista de VA discretas do Prof. Petrucio (enunciados parafraseados). Status da resolução: validada (a lista só traz as dicas de comando; os valores são da equipe TutorON, conferidos com `scipy.stats`).

Molde da lista no R: `dbinom(k, n, p)` = P(X = k); `pbinom(c, n, p)` = P(X ≤ c); `1 - pbinom(c, n, p)` = P(X > c); `pbinom(b, n, p) - pbinom(a - 1, n, p)` = P(a ≤ X ≤ b). O cuidado é o "a − 1": X é inteira, então P(X ≥ 2) = 1 − P(X ≤ 1).

**Q1.** Falha na rede em 60% dos dias, 3 dias: X ~ Bin(3; 0,6). P(0), ..., P(3) = 0,064; 0,288; 0,432; 0,216. E(X) = np = 1,8 dia.

**Q2.** Defeito 12%, lote de 40: X ~ Bin(40; 0,12).
- (a) P(3 ≤ X ≤ 5) = `pbinom(5,40,.12) - pbinom(2,40,.12)` ≈ 0,5275.
- (b) P(X ≥ 2) = `1 - pbinom(1,40,.12)` ≈ 0,9612.
- (c) P(X ≤ 3) ≈ 0,2768.
- (d) Pelo menos 39 boas = no máximo 1 defeituosa: P(X ≤ 1) ≈ 0,0388.
- (e) No máximo 39 boas = pelo menos 1 defeituosa: 1 − P(X = 0) ≈ 0,9940.

**Q4.** 15 ações, cada uma cai com p = 0,75: E(X) = 11,25; σ = √(15 · 0,75 · 0,25) ≈ 1,677; P(X = 15) ≈ 0,0134; P(X = 10) ≈ 0,1651; P(X ≥ 13) = `1 - pbinom(12,15,.75)` ≈ 0,2361.

**Q5.** Moeda 6 vezes: P(4 coroas) ≈ 0,2344; P(≥ 2) ≈ 0,8906; P(≤ 3) ≈ 0,6562.

**Q6.** 15% defeituosas, amostra de 10: P(X ≤ 1) ≈ 0,5443. **Q7.** 70% favoráveis, 5 pessoas: P(X = 3) ≈ 0,3087.

**Verificação:** valores refeitos com `scipy.stats` em `tests_acervo/test_disciplina_prob.py`.
