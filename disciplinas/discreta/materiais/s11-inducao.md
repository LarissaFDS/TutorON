---
id: discreta-inducao
titulo: Indução matemática — como provar que 1 + 2 + … + n = n(n+1)/2 e que 6 divide n³ − n
assunto: discreta-06-inducao-peano
tipo: resolucao
resolucao: sim
questao: lista 6 (2011.1), Q2 e Q3; revisão UFCG, Q1
fonte: Notas de aula do Prof. Pablo Sampaio (UFRPE), Indução Matemática, 8ª lista e respostas da 6ª lista (2011.1); slides do Prof. Leandro Balby Marinho (UFCG), Indução e Recursividade; exercício de revisão do 2º estágio (UFCG), questão 1
fontes_catalogo: ufrpe-discreta-pablo,ufcg-discreta-leandro
autoria: Prof. Pablo Sampaio (UFRPE) e Prof. Leandro Balby Marinho (UFCG), parafraseados pela equipe TutorON com auxílio de IA; resolução da Q1 da UFCG pela equipe
licenca: Não declarada (material dos professores)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Para provar "P(n) para todo inteiro n ≥ $n_0$" pelo **primeiro princípio da indução**:
1. **Caso base**: prove $P(n_0)$.
2. **Passo indutivo**: para k ≥ $n_0$ arbitrário, suponha P(k) (**hipótese de indução**) e prove P(k + 1).
Analogia da aula: o robô que chega ao primeiro degrau e sabe subir de qualquer degrau para o seguinte sobe a escada toda. Sem o caso base, o passo sozinho não prova nada.

Exemplo: $1 + 2 + \dots + n = \dfrac{n(n+1)}{2}$ para n ≥ 1 (soma dos n primeiros inteiros é n vezes n mais 1, sobre 2).
- Base, n = 1: o lado esquerdo é 1; o direito, 1 · 2 / 2 = 1.
- Passo: suponha $1 + \dots + k = \dfrac{k(k+1)}{2}$. Somando k + 1 dos dois lados: $1 + \dots + k + (k+1) = \dfrac{k(k+1)}{2} + (k+1) = \dfrac{k(k+1) + 2(k+1)}{2} = \dfrac{(k+1)(k+2)}{2}$, que é P(k + 1). ∎

Exemplo com divisibilidade (revisão da UFCG): 6 divide $n^3 - n$ para todo n ≥ 0.
- Base: $0^3 - 0 = 0$ e 6 | 0.
- Passo: $(k+1)^3 - (k+1) = (k^3 - k) + 3k(k+1)$. Pela hipótese, 6 | $(k^3 - k)$. E k(k + 1) é par (produto de consecutivos), então 3k(k + 1) é múltiplo de 6. A soma de dois múltiplos de 6 é múltiplo de 6. ∎

**Indução forte** (segundo princípio): no passo, suponha P(j) para **todos** os j de $n_0$ a k e prove P(k + 1). Útil quando P(k + 1) depende de casos anteriores ao k, como "todo inteiro n ≥ 2 é primo ou produto de primos".

Erros comuns: esquecer o caso base; usar no passo exatamente o que se quer provar (P(k + 1)); fazer só exemplos ("vale para 1, 2, 3, então vale sempre"); começar a base no valor errado.

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** para n = 4: 1 + 2 + 3 + 4 = 10 = 4 · 5 / 2. Por código, as duas fórmulas foram checadas para n de 0 a 2000.
