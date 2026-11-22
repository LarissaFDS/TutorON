---
id: lfa-cc-ab2-2017-anbn-pilha-maquina-de-turing
titulo: AB2 de 2017.2 (Ciência da Computação) — gramática e autômato com pilha para aⁿbⁿ (aaabbb), o que faz a máquina de Turing da figura (a e b alternados), MT para 0*
assunto: lfa-06-maquinas-de-turing
tipo: prova
questao: 1 a 4
resolucao: sim
fonte: AB2 de Teoria da Computação 2017.2, turma de Ciência da Computação da UFAL (foto da prova; professor não identificado), questões 1 a 4
curso: Ciência da Computação (UFAL), turma de Teoria da Computação (COMP376), 2017.2
fontes_catalogo: ufal-cc-tc-provas-2017-2
autoria: Questões da prova (professor não identificado na foto); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, foto não versionada
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
AB2 de 2017.2 da turma de Ciência da Computação, questões 1 a 4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Q1 — gramática de $\{a^nb^n \mid n \ge 0\}$:** $S \to aSb \mid \varepsilon$. Derivação de aaabbb: $S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aaaSbbb \Rightarrow aaabbb$. A árvore tem S em cada nível interno, com filhos a, S, b, e a última S com filho ε. Com essa gramática, toda palavra tem **uma só** árvore: a gramática não é ambígua. (Já $S \to aSb \mid ab \mid \varepsilon$ dá duas árvores para ab e é ambígua.)

**Q2 — autômato com pilha:** empilhe um X para cada a; ao ler b, desempilhe um X; aceite se a entrada acabou e a pilha voltou ao fundo. Para aaabbb a pilha vai a X, XX, XXX e volta a XX, X, vazia: aceita. aab termina com X na pilha: rejeita.

**Q3 — máquina da figura:** $q_0$ inicial; $\delta(q_0,a)=(q_1,a,D)$, $\delta(q_1,b)=(q_0,b,D)$, $\delta(q_0,\square)=(q_2,\square,D)$, $\delta(q_1,\square)=(q_2,\square,D)$, $q_2$ final. A máquina só lê, sem mudar a fita, e aceita as palavras em que a e b se **alternam começando por a**: $(ab)^*(a+\varepsilon)$, como ε, a, ab, aba, abab. Computação de aba: $q_0$ lê a → $q_1$; lê b → $q_0$; lê a → $q_1$; lê □ → $q_2$, aceita; a fita continua aba. Em abb a máquina para em $q_0$ lendo o segundo b, sem transição: rejeita.

**Q4 — MT para $L = 0^*$ sobre $\{0,1\}$:** $\delta(q_0,0)=(q_0,0,D)$ e $\delta(q_0,\square)=(q_a,\square,D)$; com 1 não há transição (rejeita). Exemplo: 000 passa três vezes por $q_0$ e aceita no branco.

Erros comuns: dizer que a máquina da Q3 reconhece só $(ab)^*$ (ela também aceita palavras que terminam em a, porque $q_1$ vai ao final no branco); esquecer a palavra vazia em $a^nb^n$ e em $0^*$.

**Verificação:** `test_prova_cc_2017_ab2` gera as palavras da gramática com `gera`, conta as árvores e roda as duas máquinas de Turing com `mt` em todas as palavras até comprimento 8.
