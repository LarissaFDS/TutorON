---
id: lfa-bombeamento-mesmo-numero-a-b-corrigido
titulo: Lema do bombeamento — prova de que 'mesmo número de a e b' não é regular; correção do exemplo 17 da apostila (n = 4 com aabb e casos escolhidos)
assunto: lfa-04-nao-regularidade
tipo: exercicio_resolvido
questao: exemplo 17
resolucao: sim
fonte: Apostila 02 (Profa. Simone Prado, UNESP), exemplo 17
fontes_catalogo: unesp-prado-apostilas-tc
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Exemplo 17 da apostila: $L = \{w \in \{a,b\}^* \mid w$ tem o mesmo número de a e de b$\}$ não é regular. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Correção:** a ideia da apostila está certa (escolher $w = a^n b^n$ e notar que $uv$ só tem a, na notação $w = uvz$ da apostila), mas o fechamento tem dois erros.
1. Com $n = 4$ ela usa $w = aabb$. Mas $a^4 b^4 = aaaabbbb$, e $aabb$ tem comprimento 4, no limite do lema.
2. Ela examina dois casos **escolhidos** ($u = a, v = a$ e $u = aa, v = b$). O segundo nem respeita a observação anterior de que $uv$ só tem a. A prova tem de valer para **toda** decomposição, com $n$ arbitrário.

**Prova corrigida.**
1. Suponha $L$ regular, com constante $n$.
2. Tome $w = a^n b^n \in L$.
3. Para **qualquer** $w = uvz$ com $|uv| \le n$ e $|v| \ge 1$, temos $v = a^k$ com $1 \le k \le n$, porque os $n$ primeiros símbolos são a.
4. $uv^2z = a^{n+k}b^n$ tem mais a do que b, então não está em $L$. Contradição.

**Outro caminho (fechamento):** $L \cap a^*b^* = \{a^nb^n\}$. Se $L$ fosse regular, a interseção com a regular $a^*b^*$ também seria, mas $a^nb^n$ não é regular.

Cuidado com a escolha de $w$: $w = (ab)^n$ está em $L$, mas não leva à contradição. O adversário pode escolher $v = ab$, e $u(ab)^iz$ continua com o mesmo número de a e b.

**Verificação:** para $n$ de 1 a 7, todas as decomposições de $a^nb^n$ com $|uv| \le n$ e $|v| \ge 1$ dão $uv^2z \notin L$; com $w = (ab)^n$, existe decomposição que bombeia sem sair de $L$ (o teste mostra por que essa escolha não prova nada).
