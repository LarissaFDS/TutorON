---
id: discreta-absurdo-contraexemplo
titulo: Redução ao absurdo, contraexemplo e prova existencial (raiz de 2 irracional, infinitos primos)
assunto: discreta-02-demonstracoes
tipo: material_estudo
resolucao: sim
fonte: Notas de aula do Prof. Pablo Sampaio (UFRPE), Demonstrações Matemáticas partes 2 e 4, lista 4 e "Considerações adicionais sobre demonstrações"; slides do Prof. Leandro Balby Marinho (UFCG), Técnicas de Demonstração
fontes_catalogo: ufrpe-discreta-pablo,ufcg-discreta-leandro
autoria: Prof. Pablo Sampaio (UFRPE) e Prof. Leandro Balby Marinho (UFCG), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material dos professores)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
**Redução ao absurdo (contradição)**: para provar Q, suponha ¬Q e deduza algo impossível (por exemplo, "x é par e ímpar"). Para P → Q, suponha P e ¬Q.

Exemplo clássico: $\sqrt{2}$ é irracional. Suponha $\sqrt{2} = a/b$ com a, b inteiros, b ≠ 0 e a fração irredutível. Então $a^2 = 2b^2$; logo $a^2$ é par e, pela contrapositiva já provada, a é par: a = 2k. Daí $4k^2 = 2b^2$, $b^2 = 2k^2$, e b também é par. Então a e b têm o fator 2, o que contradiz "irredutível". ∎

Existem infinitos primos. Suponha que só existam $p_1, \dots, p_k$. O número $N = p_1 p_2 \cdots p_k + 1$ deixa resto 1 na divisão por cada $p_i$; então nenhum deles divide N. Mas N > 1 tem um fator primo, que não está na lista. Contradição. ∎ Cuidado: N não precisa ser primo. Com 2, 3, 5, 7, 11 e 13, N = 30031 = 59 · 509.

**Contraexemplo** refuta um "para todo". Lista 4 do Prof. Pablo: "se $a \mid b$, então $(a+m) \mid (b+m)$" é falsa: a = 2, b = 4, m = 3 dá 5 ∤ 7. E "se $ac \equiv bc \pmod{m}$, então $a \equiv b \pmod{m}$" é falsa: a = 2, b = 7, c = 3, m = 3 (6 ≡ 21, mas 2 ≢ 7 mod 3). Um contraexemplo precisa satisfazer **todas** as hipóteses e falhar a conclusão.

**Prova existencial**: exibir um exemplo basta ("existe primo par": 2). Já "para todo" nunca se prova com exemplos, a não ser que o universo seja finito e todos os casos sejam testados (exaustão).

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** 30031 = 59 · 509 e os dois contraexemplos foram conferidos por código.
