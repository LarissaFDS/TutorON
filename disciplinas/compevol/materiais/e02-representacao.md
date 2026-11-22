---
id: compevol-representacao-binaria-decodificacao-numero-de-bits-precisao
titulo: Representação binária de um parâmetro real: quantos bits para uma precisão dada, como decodificar o cromossomo em x, representação real e outras codificações
assunto: compevol-01-fundamentos
tipo: exercicio_resolvido
questao: Lacerda e Carvalho, seções 3.1-3.2; apostila de Lucas, seção 3.1
resolucao: sim
fonte: Apostilas e textos da pasta da turma (Lucas, UFRGS 2002; Lacerda e Carvalho; Dianati, Song e Treiber)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: lacerda-carvalho-ag,lucas-apostila-ag
autoria: Exercício clássico dos textos da pasta da turma; resolução da equipe TutorON
licenca: Textos sem licença aberta declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Lacerda e Carvalho, seções 3.1-3.2; apostila de Lucas, seção 3.1 (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Codificação binária:** o cromossomo é uma cadeia de $L$ bits; cada parâmetro real $x \in [x_{\min}, x_{\max}]$ ocupa um trecho. Para decodificar, lê-se o trecho como inteiro $k$ (de $0$ a $2^L - 1$) e mapeia-se linearmente:
$$x = x_{\min} + \frac{x_{\max} - x_{\min}}{2^L - 1}\, k$$
Em palavras: o inteiro vira uma fração do intervalo.

**Quantos bits?** Para precisão de $p$ casas decimais, o intervalo precisa de pelo menos $(x_{\max} - x_{\min}) \cdot 10^p$ valores distintos:
$$2^{L-1} < (x_{\max} - x_{\min}) \cdot 10^p \le 2^L$$

**Exemplo:** $x \in [-1, 2]$ com 6 casas: $3 \cdot 10^6$ valores; $2^{21} = 2\,097\,152 < 3\,000\,000 \le 2^{22} = 4\,194\,304$, logo **$L = 22$ bits**. O cromossomo de 22 bits todos iguais a 1 decodifica em $x = 2$; todos 0, em $x = -1$.

Com dois parâmetros (como $x$ e $y$ em $[-100, 100]$), concatena-se um trecho por parâmetro e decodifica-se cada um separadamente.

**Outras representações:**
- **real** (vetor de números): mais natural para parâmetros contínuos, sem perda de precisão; pede operadores próprios (cruzamento aritmético, mutação gaussiana);
- **permutação:** para ordem (caixeiro-viajante, escalonamento);
- **árvore:** em programação genética, o indivíduo é um programa.

A escolha da representação define quais operadores fazem sentido e quanto vizinhos no cromossomo são vizinhos na solução (no binário, $0111$ e $1000$ diferem em 4 bits, mas são inteiros vizinhos; o **código de Gray** evita isso).

**Verificação:** `test_bits_e_decodificacao` confere $L = 22$ pela desigualdade, a decodificação dos extremos e de um ponto do meio, e que vizinhos em código de Gray diferem em um bit só.
