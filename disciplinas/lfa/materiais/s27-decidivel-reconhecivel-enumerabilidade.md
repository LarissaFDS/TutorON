---
id: lfa-decidivel-vs-reconhecivel-diagonalizacao
titulo: Linguagem decidível (recursiva) × reconhecível (recursivamente enumerável), co-reconhecível, contagem e enumerabilidade, diagonalização de Cantor e existência de linguagens não reconhecíveis
assunto: lfa-08-decidibilidade-parada
tipo: lista
questao: 1
resolucao: sim
fonte: Lista de Teoria da Computação 2016.2 (UFAL), questão 1; aula 8 das notas de Sipser (MIT), linguagens e diagonalização
fontes_catalogo: ufal-lista-decidibilidade-2016-2,lee-sipser-notas-2012
autoria: Lista de Teoria da Computação da UFAL (2016.2, professor não identificado no arquivo); resolução da equipe TutorON
licenca: Não declarada (lista); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
status_resolucao: validada
revisao_humana: pendente
---
Lista de 2016.2, questão 1: distinguir linguagens decidíveis das reconhecidas por máquina de Turing. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Reconhecível** (Turing-reconhecível, recursivamente enumerável): existe uma MT $M$ que **aceita** toda $w \in L$. Para $w \notin L$, $M$ rejeita **ou nunca para**.

**Decidível** (recursiva): existe uma MT que **sempre para**, aceitando $w \in L$ e rejeitando $w \notin L$. É o **decisor** de $L$.

Toda decidível é reconhecível. A recíproca é falsa: $A_{TM}$ é reconhecível (simule $M$ sobre $w$ e aceite se ela aceitar), mas não é decidível. A diferença prática é que, com um reconhecedor, ao esperar uma resposta você não sabe se ela ainda vem ou se nunca virá.

**Teorema:** $L$ é decidível se, e só se, $L$ e $\overline{L}$ são reconhecíveis. Rode os dois reconhecedores **alternando passos**: um deles aceita em tempo finito, e isso decide. Consequência: $\overline{A_{TM}}$ **não** é reconhecível.

**Contagem e enumerabilidade** (ementa: "contagem e enumerabilidade"):
- Um conjunto é **enumerável** se pode ser posto em correspondência com $\mathbb{N}$.
- $\Sigma^*$ é enumerável: liste por comprimento e, dentro do mesmo comprimento, em ordem alfabética.
- Toda MT é uma cadeia finita (sua descrição $\langle M \rangle$), então há uma quantidade **enumerável** de MTs.
- O conjunto de **todas** as linguagens, $2^{\Sigma^*}$, não é enumerável (diagonal de Cantor). Se $L_1, L_2, \dots$ fosse uma lista de todas, $D = \{s_i \mid s_i \notin L_i\}$ seria diferente de cada $L_i$ na palavra $s_i$.
- Logo, existem linguagens que **nenhuma** MT reconhece.

**Verificação:** a enumeração de $\{0,1\}^*$ por comprimento é conferida por código (posição $2^n - 1$ para a primeira palavra de comprimento $n$), e a diagonal construída sobre as 8 primeiras linguagens de uma lista finita difere de cada uma delas.
