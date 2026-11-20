---
id: discreta-divisao-bases
titulo: Divisão euclidiana (div e mod, inclusive com negativos) e sistemas de numeração
assunto: discreta-07-inteiros-numeracao
tipo: material_estudo
resolucao: sim
fonte: Notas de aula do Prof. Pablo Sampaio (UFRPE), Algoritmo da Divisão e suas Aplicações, Números Inteiros — axiomas, e Resultados Diversos (soma na base b); Evaristo e Perdigão, Introdução à Álgebra Abstrata, capítulos 3 e 5
fontes_catalogo: ufrpe-discreta-pablo,ufal-evaristo-algebra
autoria: Prof. Pablo Sampaio (UFRPE) e Jaime Evaristo e Eduardo Perdigão (UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (notas do professor; livro sem licença aberta)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Os inteiros $\mathbb{Z}$ são definidos por axiomas (fechamento de + e ·, associatividade, comutatividade, distributividade, neutros 0 e 1, oposto −a, ordem e boa ordenação). A divisão não está entre as operações: $\mathbb{Z}$ não é fechado para a divisão.

**Divisão euclidiana**: para inteiros a e b ≠ 0, existem q e r **únicos** com $a = bq + r$ e $0 \le r < |b|$. Notação da aula: q = a **div** b e r = a **mod** b. O resto é sempre **não negativo**:
- 17 = 5 · 3 + 2: 17 div 5 = 3, 17 mod 5 = 2.
- −17 = 5 · (−4) + 3: −17 div 5 = −4 e −17 mod 5 = 3 (e não −2). Algumas linguagens (C, Java) dão −2 para `-17 % 5`; o Python dá 3, como a definição.

Aplicações: dia da semana daqui a 100 dias (100 mod 7 = 2 dias à frente), relógio de 24 h, paridade.

**Sistemas de numeração**: na base b ≥ 2, $n = a_k b^k + \dots + a_1 b + a_0$ com $0 \le a_i < b$, e a representação é única. Para converter da base 10 para a base b, divida sucessivamente por b e leia os restos **de baixo para cima**: 37 = 2·18 + 1, 18 = 2·9 + 0, 9 = 2·4 + 1, 4 = 2·2 + 0, 2 = 2·1 + 0, 1 = 2·0 + 1, logo $37 = (100101)_2$. Da base b para a 10, some os dígitos vezes as potências: $(2A)_{16} = 2 \cdot 16 + 10 = 42$. A soma na base b segue o mesmo algoritmo da escola, com "vai um" quando a soma do dígito passa de b − 1: $(1011)_2 + (0110)_2 = (10001)_2$ (11 + 6 = 17).

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** por código, $a = b \cdot (a \text{ div } b) + (a \text{ mod } b)$ com $0 \le r < |b|$ para a de −200 a 200 e b de 1 a 20; 37, 42 e 17 conferidos nas bases 2 e 16.
