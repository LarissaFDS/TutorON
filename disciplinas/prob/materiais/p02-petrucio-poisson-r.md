---
id: prob-petrucio-poisson-r
titulo: Poisson no R com dpois e ppois: bombeiros com 3 chamadas por dia, 20 chamadas na semana, clientes no posto, pedidos por hora e por dia de 8 horas
assunto: prob-05-distribuicoes-discretas
tipo: lista
questao: Lista de VA discretas, Q3, Q8 a Q10
semestre: 2025.2
resolucao: sim
fonte: Lista "Variáveis Aleatórias Discretas" do Prof. Petrucio A. Medeiros Barros (UFAL) | Q3, Q8 a Q10
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

Contagem de eventos no tempo com taxa média constante → Poisson. No R: `dpois(k, lambda)` = P(X = k) e `ppois(c, lambda)` = P(X ≤ c). O passo que mais erra: **ajustar λ ao intervalo pedido** antes de calcular (λ por dia × 7 para a semana; λ por hora × 8 para o dia de trabalho).

**Q3.** Bombeiros, λ = 3 por dia.
- (a) P(X = 4) = `dpois(4, 3)` ≈ 0,1680.
- (b) P(X = 0) = e^(−3) ≈ 0,0498.
- (c) Na semana, λ = 21: P(X = 20) = `dpois(20, 21)` ≈ 0,0867.

**Q8.** Posto, λ = 6 clientes por hora: P(X = 3) ≈ 0,0892; P(X ≤ 3) = `ppois(3, 6)` ≈ 0,1512. Na Poisson, E(X) = Var(X) = λ: valor esperado 6 e desvio padrão √6 ≈ 2,449.

**Q9.** λ = 10 defeituosos por hora: P(X ≤ 4) = `ppois(4, 10)` ≈ 0,0293.

**Q10.** λ = 5 pedidos por hora.
- (a) Mais de dois pedidos: `1 - ppois(2, 5)` ≈ 0,8753.
- (b) Num dia de 8 horas, λ = 40: P(X = 50) = `dpois(50, 40)` ≈ 0,0177.

**Verificação:** valores refeitos com `scipy.stats` em `tests_acervo/test_disciplina_prob.py`.
