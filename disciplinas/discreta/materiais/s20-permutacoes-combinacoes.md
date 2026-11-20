---
id: discreta-permutacoes-combinacoes
titulo: Permutações, arranjos, combinações e anagramas com letras repetidas (ex. ARARA)
assunto: discreta-11-combinatoria
tipo: material_estudo
resolucao: sim
fonte: Slides e lista de Contagem do Prof. Leandro Balby Marinho (UFCG), permutações e combinações
fontes_catalogo: ufcg-discreta-leandro
autoria: Prof. Leandro Balby Marinho (UFCG), parafraseado pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Escolha a fórmula pelas duas perguntas: **a ordem importa?** **pode repetir?**

| Ordem importa? | Repete? | Nome | Fórmula |
|---|---|---|---|
| sim | não | arranjo P(n, k) | $\frac{n!}{(n-k)!}$ |
| sim | sim | sequência | $n^k$ |
| não | não | combinação C(n, k) | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ |
| não | sim | combinação com repetição | $\binom{n+k-1}{k}$ |

Em palavras: C(n, k) é "n escolhe k", n fatorial dividido por k fatorial vezes (n − k) fatorial.

Exemplos:
- Ordenar 5 livros distintos na estante: 5! = 120 (permutação).
- Presidente, vice e tesoureiro entre 10 pessoas (cargos diferentes, ordem importa): P(10, 3) = 720.
- Comissão de 3 entre 10 (ordem não importa): C(10, 3) = 120. Note que 720 = 120 · 3!.
- Distribuir 7 bolas **iguais** em 3 caixas: C(9, 2) = 36 ("estrelas e barras").

**Anagramas com letras repetidas**: com n letras, sendo $n_1$ iguais de um tipo, $n_2$ de outro…, o número é $\frac{n!}{n_1!\, n_2! \cdots}$. Divide-se porque trocar entre si letras iguais não gera palavra nova.
- **ARARA**: 5 letras, A três vezes, R duas vezes, então $\frac{5!}{3!\,2!} = \frac{120}{12} = 10$. Interpretação: ordem importa, letras repetidas. Equivale a escolher as 2 posições dos R entre 5: C(5, 2) = 10.
- BANANA: $\frac{6!}{3!\,2!\,1!} = 60$.

**Binômio de Newton**: $(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k$; a soma de uma linha do triângulo de Pascal é $2^n$ (número de subconjuntos de um conjunto de n elementos).

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** os anagramas de ARARA (10) e BANANA (60) foram listados por código com `itertools.permutations`; 120, 720, 120 e 36 conferidos com `math.perm` e `math.comb`.
