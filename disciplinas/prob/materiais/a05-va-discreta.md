---
id: prob-anot-va-discreta
titulo: Variável aleatória discreta: função de probabilidade, distribuição acumulada; comissão de 3 pessoas com pelo menos 2 mulheres
assunto: prob-03-variaveis-aleatorias
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Variáveis Aleatórias_251008_230428.pdf" (2025.2), págs. 1–3
autoria: Otávio Joshua Costa Brandão Menezes (aluno, equipe TutorON), anotações de estudo; paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações pessoais do aluno); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia as anotações e não reproduz imagens
fontes_catalogo: ufal-prob-anotacoes-2025-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Anotações de aluno (2025.2), parafraseadas. Status da resolução: validada. Conferido com `scipy.stats.hypergeom` e `fractions`.

**Variável aleatória (VA):** função que associa um número a cada resultado do espaço amostral. Ex.: duas moedas, $\Omega = \{CC, CK, KC, KK\}$, X = número de caras, valores 0, 1, 2. **Discreta:** valores num conjunto finito ou enumerável (contagens: abelhas numa colmeia). **Contínua:** valores num intervalo real (tempo de resposta de uma CPU).

**Função de probabilidade (fp)** de uma VA discreta: $p(x_i) = P(X = x_i)$, com $0 \le P(X=x_i) \le 1$ e $\sum_i P(X = x_i) = 1$. Ex.: dado honesto, $P(X=x) = 1/6$ para x = 1, …, 6.

**Função de distribuição acumulada (FDA):** $F(x) = P(X \le x) = \sum_{x_i \le x} P(X = x_i)$. Nas duas moedas: fp 1/4, 1/2, 1/4 para x = 0, 1, 2; FDA 1/4, 3/4, 1.

**Exemplo (comissão):** de 35 pessoas, 21 homens e 14 mulheres, sorteia-se uma comissão de 3 sem reposição. X = número de mulheres. Probabilidade de pelo menos 2 mulheres:
$$P(X \ge 2) = \frac{\binom{14}{2}\binom{21}{1} + \binom{14}{3}}{\binom{35}{3}} = \frac{1911 + 364}{6545} = \frac{2275}{6545} \approx 0{,}3476.$$
A tabela das anotações (pela árvore HHH, HHM, …) dá $P(X=0..3) \approx 0{,}203;\ 0{,}449;\ 0{,}292;\ 0{,}056$, e $0{,}291 + 0{,}056 = 0{,}347$ com arredondamento. Em R: `(choose(14,2)*choose(21,1) + choose(14,3))/choose(35,3)`.

**Verificação:** as quatro probabilidades somam 1 (6545/6545); X é hipergeométrica (N = 35, K = 14, n = 3), e `hypergeom.sf(1, 35, 14, 3)` dá 0,3476.
