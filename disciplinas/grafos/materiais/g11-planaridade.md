---
id: grafos-planares-euler-k33-casas
titulo: Grafos planares — problema das três casas (K3,3), fórmula de Euler n − m + f = 2 e com componentes, m ≤ 3n − 6, qual par (n, m) pode ser planar, G ou o complemento não é planar com 11 vértices
assunto: grafos-06-planaridade
tipo: lista
questao: 4.1, 4.2, 4.3, 4.9, 4.10 (lista); 5 (prova)
resolucao: sim
fonte: Lista de exercícios de Teoria dos Grafos 2020.1, Prof. Rian Gabriel Pinheiro (IC-UFAL); 2ª avaliação de Teoria dos Grafos 2016.2, Prof. Leonardo Viana (IC-UFAL)
curso: Ciência da Computação (UFAL), Teoria dos Grafos (COMP369), 2020.1
fontes_catalogo: ufal-rian-lista-2020-1,ufal-viana-prova2-2016-2
autoria: Questões do Prof. Rian Gabriel Pinheiro (UFAL); resolução da equipe TutorON; Questões do Prof. Leonardo Viana (UFAL); resolução da equipe TutorON
licenca: Não declarada (lista, prova e slides); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista 2020.1, questões 4.1, 4.2, 4.3, 4.9 e 4.10, e 2ª avaliação de 2016.2, questão 5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Euler:** num grafo planar **conexo** desenhado sem cruzamentos, $n - m + f = 2$ ($n$ vértices, $m$ arestas, $f$ faces, contando a externa). Com $c$ componentes, $n - m + f - c = 1$ (4.9): a face externa é contada uma vez só.

**Limites:** com $n \ge 3$, cada face tem pelo menos 3 arestas na borda e cada aresta borda no máximo 2 faces: $3f \le 2m$, o que dá $m \le 3n - 6$. Sem triângulos (por exemplo, bipartidos), $m \le 2n - 4$.

**Três casas (4.1):** casas e companhias formam $K_{3,3}$, com $m = 9 > 2 \cdot 6 - 4 = 8$: não é planar, as tubulações têm de se cruzar. $K_5$ também não é ($10 > 9$). **Kuratowski:** planar se e só se não contém subdivisão de $K_5$ nem de $K_{3,3}$.

**Prova, Q5:** entre (8, 12), (5, 10), (6, 15), (7, 21) e (9, 22), só (8, 12) respeita $m \le 3n - 6$ (12 ≤ 18); os outros são $K_5$, $K_6$, $K_7$ e 22 > 21. Resposta: (a). Respeitar o limite não prova planaridade; violá-lo prova que não é planar.

**11 vértices (4.10):** $G$ e $\bar G$ juntos têm $\binom{11}{2} = 55$ arestas; se os dois fossem planares, teriam no máximo $2 \cdot 27 = 54$.

**4.2 e 4.3:** desenhos planares das componentes podem ficar lado a lado; uma ponte liga duas partes que podem ser desenhadas em faces vizinhas, sem cruzar.

**Verificação:** `test_planaridade` usa `check_planarity` do NetworkX em $K_5$, $K_{3,3}$ e no Petersen e confere a alternativa da prova e a fórmula com componentes.
