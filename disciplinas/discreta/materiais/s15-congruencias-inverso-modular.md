---
id: discreta-congruencias-inverso
titulo: Congruência módulo m e inverso modular — como calcular o inverso de 7 módulo 26
assunto: discreta-09-aritmetica-modular-rsa
tipo: resolucao
resolucao: sim
questao: lista 4, Q6, Q7b, Q9, Q11
fonte: 4ª lista e respostas do Prof. Pablo Sampaio (UFRPE), Algoritmo da Divisão e Aritmética Modular; notas de aula do Prof. Pablo Sampaio, congruência; Evaristo e Perdigão, Introdução à Álgebra Abstrata, capítulo 7 (Os inteiros módulo n)
fontes_catalogo: ufrpe-discreta-pablo,ufal-evaristo-algebra
autoria: Prof. Pablo Sampaio (UFRPE) e Jaime Evaristo e Eduardo Perdigão (UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (notas e lista do professor; livro sem licença aberta)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
**Congruência**: com m > 0, $a \equiv b \pmod{m}$ se $m \mid (a - b)$; equivale a a mod m = b mod m. Ex.: 29 ≡ 8 (mod 3), pois 3 | 21. Lista 4: valores com $x \equiv 7 \pmod 3$ são 1, 4, 7, 10, 13; com $x \equiv 3 \pmod 7$, 3, 10, 17, 24, 31. A congruência é relação de equivalência, e as classes são os elementos de $\mathbb{Z}_m = \{[0], [1], \dots, [m-1]\}$.

Pode-se somar e multiplicar congruências (se $a \equiv b$ e $c \equiv d$, então $a + c \equiv b + d$ e $ac \equiv bd$), mas **não** se pode cancelar à vontade: 2 · 3 ≡ 7 · 3 (mod 3) e 2 ≢ 7 (mod 3). Só se cancela c quando mdc(c, m) = 1.

**Inverso modular**: o inverso de a módulo m é um x com $ax \equiv 1 \pmod{m}$. Ele **existe se e somente se mdc(a, m) = 1**; confira isso antes de procurar. Ex.: 2 não tem inverso módulo 26 (mdc = 2).

**Como calcular o inverso de 7 módulo 26:**
1. mdc(7, 26) = 1 pelo algoritmo de Euclides (26 = 3·7 + 5; 7 = 1·5 + 2; 5 = 2·2 + 1), então o inverso existe.
2. Volte as divisões (Bézout): 1 = 3 · 26 − 11 · 7.
3. Reduza módulo 26: −11 · 7 ≡ 1, e −11 ≡ 15 (mod 26). Logo $7^{-1} \equiv 15 \pmod{26}$.
4. Confira: 7 · 15 = 105 = 4 · 26 + 1.

Para m pequeno, também dá para testar x = 1, 2, …, m − 1 até achar ax mod m = 1. Em $\mathbb{Z}_p$ com p primo, todo elemento não nulo tem inverso (é um corpo).

**Pequeno Teorema de Fermat** e **Euler** (livro, cap. 7): se mdc(a, n) = 1, então $a^{\varphi(n)} \equiv 1 \pmod n$, onde φ(n) conta os inteiros de 1 a n primos com n; para p primo, $a^{p-1} \equiv 1 \pmod p$.

Divergência com a resposta original (Q7b, "n é ímpar sse n ≡ 1 mod 2"): a resposta escreve "2k + 1 = 2m" e não fecha a volta. Prova correta: (⇒) se n = 2k + 1, então n − 1 = 2k e 2 | (n − 1). (⇐) se 2 | (n − 1), n − 1 = 2k e n = 2k + 1 é ímpar. ∎ Correções da equipe TutorON; não é gabarito do professor. Status da resolução: corrigida.

**Verificação:** 7 · 15 mod 26 = 1, conferido também com `pow(7, -1, 26)` do Python.
