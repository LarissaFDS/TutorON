---
id: sd-ecom012-mux-demux
titulo: Circuitos Digitais (ECOM012) — MUX de paridade, demultiplexador e decodificador 3 para 8, comparador, hexadecimal e contagem em base R
assunto: sd-04-blocos-combinacionais
tipo: prova
resolucao: sim
questao: varias
fonte: fotos da AB2 de 2015 e da prova final de Circuitos Digitais (UFAL) | enunciados parafraseados
fontes_catalogo: ufal-ecom012-provas-2015-2016
autoria: Enunciados: provas da disciplina Circuitos Digitais (UFAL), professor não identificado. Resoluções: equipe TutorON com apoio de IA, conferidas por código
licenca: Não declarada (prova da disciplina; fotos de aluno, não versionadas)
publicacao_transcricao: não autorizada; enunciados parafraseados a partir das fotos, sem nomes, notas ou imagens
curadoria: aprovado
natureza: material_da_disciplina
revisao_humana: pendente
verificacao: conferida_por_codigo
---
Circuitos Digitais (ECOM012) — blocos combinacionais e numeração

1. Com um MUX 8:1 (seleção A, B, C; entradas D0–D7), faça F = 1 se e só se houver um número par de entradas em 1.
Resolução: Dᵢ = 1 quando i (ABC) tem quantidade par de 1s: **D0 = D3 = D5 = D6 = 1** e D1 = D2 = D4 = D7 = 0.

2. Demultiplexador de 2 bits (1 entrada E, controles S1 S0, 4 saídas): Y0 = E·S1'S0', Y1 = E·S1'S0, Y2 = E·S1S0', Y3 = E·S1S0. Versão de 3 bits (8 saídas, 3 linhas de controle — o enunciado diz "duas", mas 8 saídas exigem 3): Yᵢ = E·(mintermo i de S2S1S0).

3. Decodificador 3 para 8 com portas: é o mesmo circuito do demux de 3 bits com E = 1 (ou E como habilitação). Três NOT geram S2', S1', S0'; oito AND de 3 entradas geram os mintermos m0 = S2'S1'S0' … m7 = S2S1S0; exatamente uma saída vale 1.

4. Comparador de palavras de 8 bits: igualdade A = B é o AND das 8 XNOR (Aᵢ ⊙ Bᵢ); para A > B, compare do bit mais significativo para o menos, como no comparador de 2 bits.

5. Quais são hexadecimais válidos: BED, CAB, DEAD, DECADE, ACCEDED, BAG, DAD? Todos menos **BAG** (G não é dígito hexadecimal).

6. Quantos inteiros diferentes cabem em K dígitos de base R? Rᴷ valores (0 a Rᴷ − 1); **positivos: Rᴷ − 1**.

7. Mostre pela tabela-verdade que X = XY + XY': nas 4 linhas a soma vale X (Boole: X(Y + Y') = X·1 = X).

**Verificação:** MUX, decodificador, demux, comparador e identidade conferidos por enumeração em tests_acervo/test_sd_ecom012.py.
