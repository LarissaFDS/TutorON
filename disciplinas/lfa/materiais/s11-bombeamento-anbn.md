---
id: lfa-lema-do-bombeamento-anbn
titulo: Como usar o lema do bombeamento para provar que aⁿbⁿ não é regular — enunciado, jogo contra o adversário, para toda decomposição xyz com |xy| ≤ p e |y| ≥ 1
assunto: lfa-04-nao-regularidade
tipo: material_estudo
resolucao: nao
fonte: Apostila 02 (Profa. Simone Prado, UNESP), lema do bombeamento; aula 3 das notas de Sipser (MIT), linguagens não regulares
fontes_catalogo: unesp-prado-apostilas-tc,lee-sipser-notas-2012
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
**Lema do bombeamento (regulares).** Se $L$ é regular, existe $p \ge 1$ (o número de estados de um AFD para $L$) tal que toda $w \in L$ com $|w| \ge p$ pode ser escrita $w = xyz$ com
(1) $|xy| \le p$, (2) $|y| \ge 1$, (3) $xy^iz \in L$ para **todo** $i \ge 0$.

O lema só serve para provar que uma linguagem **não** é regular, por contradição. A prova é um jogo em que os quantificadores decidem quem escolhe:

| Quem escolhe | O quê |
|---|---|
| adversário | o $p$ (você não sabe o valor) |
| **você** | uma palavra $w \in L$ com $|w| \ge p$, escrita em função de $p$ |
| adversário | **qualquer** decomposição $xyz$ com $|xy| \le p$ e $|y| \ge 1$ |
| **você** | um $i$ com $xy^iz \notin L$ |

**Prova de que $L = \{a^n b^n \mid n \ge 0\}$ não é regular.**
1. Suponha $L$ regular, com constante $p$.
2. Escolha $w = a^p b^p \in L$, com $|w| = 2p \ge p$.
3. Seja $w = xyz$ **qualquer** decomposição com $|xy| \le p$ e $|y| \ge 1$. Como os $p$ primeiros símbolos de $w$ são a, $y = a^k$ com $k \ge 1$.
4. Tome $i = 2$: $xy^2z = a^{p+k}b^p$, com mais a do que b, então $xy^2z \notin L$. ($i = 0$ também serve: $a^{p-k}b^p$.)
5. Isso contradiz o lema, então $L$ não é regular.

Erros comuns:
- escolher a decomposição (o "1º caso, 2º caso" com $y$ escolhido por você), em vez de cobrir **toda** decomposição;
- usar um $p$ numérico ($p = 4$) em vez de um $p$ arbitrário;
- escolher $w$ curta demais, como $w = ab$;
- concluir que $L$ **é** regular porque uma palavra pode ser bombeada (o lema não tem recíproca).

**Verificação:** para cada $p$ de 1 a 8, `tests_acervo/test_disciplina_lfa.py` percorre **todas** as decomposições de $a^pb^p$ com $|xy| \le p$ e $|y| \ge 1$ e confirma que $xy^2z$ e $xz$ estão fora de $L$.
