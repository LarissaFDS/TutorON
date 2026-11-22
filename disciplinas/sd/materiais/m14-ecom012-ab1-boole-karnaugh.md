---
id: sd-ecom012-ab1
titulo: Circuitos Digitais (ECOM012), AB1 de 2015 — expressão de circuito, Boole, mapas, bases e NAND
assunto: sd-02-algebra-booleana-portas
tipo: prova
resolucao: sim
questao: 1-6
fonte: fotos de duas versões da AB1 de Circuitos Digitais (UFAL, 2015) | enunciados parafraseados
fontes_catalogo: ufal-ecom012-provas-2015-2016
autoria: Enunciados: prova da disciplina Circuitos Digitais (UFAL), professor não identificado. Resoluções: equipe TutorON com apoio de IA, conferidas por código
licenca: Não declarada (prova da disciplina; fotos de aluno, não versionadas)
publicacao_transcricao: não autorizada; enunciados parafraseados a partir das fotos, sem nomes, notas ou imagens
curadoria: aprovado
natureza: material_da_disciplina
revisao_humana: pendente
verificacao: conferida_por_codigo
---
Circuitos Digitais (ECOM012, antecessora de SD) — AB1, duas versões (2015)

1. Circuito: AND de A com B' dá AB'; OR de A' com C dá A'+C; uma OR junta os dois; um NOT gera (A'+C)'; uma AND final dá F. (a) Expressão; (b) simplifique e redesenhe.
Resolução: F = [AB' + (A'+C)]·(A'+C)'. Por De Morgan, (A'+C)' = AC'. F = AC'·AB' + AC'·A' + AC'·C = AB'C' + 0 + 0 = **AB'C'** (uma AND de 3 entradas com B e C negados).

2. Desenhe os circuitos de X = AB + CDE; X = (A+B)(C+D)E; Y = AB(C+D) + E. Método: cada produto vira AND, cada soma vira OR, na ordem dos parênteses.

3. Mapa de 4 variáveis (linhas xy, colunas zw, ordem Gray 00, 01, 11, 10): as colunas zw = 00 e 10 são todas 1; na coluna 01 há 1 só nas linhas xy = 00 e 10; a coluna 11 é toda 0.
Resolução: grupo de 8 (colunas com w = 0) → w'; grupo de 4 (z = 0, y = 0, cantos da coluna 01 com a 00) → y'z'. **F = w' + y'z'**.

4. 1001101001₂ em octal e hexadecimal. Agrupe de 3 em 3 e de 4 em 4 a partir da direita: 1|001|101|001 = **1151₈**; 10|0110|1001 = **269₁₆** (= 617₁₀).

5. Monte AND com duas NAND: a primeira dá (AB)', a segunda, com as duas entradas ligadas nessa saída, inverte: ((AB)')' = AB. Variante: mostre NOT, AND e OR só com NAND e depois só com NOR (NOT = NAND(A,A); OR = NAND(A',B'); com NOR: OR = NOR(NOR(A,B)), AND = NOR(A',B')).

6. Mapa de 3 variáveis (linha x, colunas yz): x = 0 → 0 1 0 1; x = 1 → 1 1 0 1. Mintermos 1, 2, 4, 5, 6.
Resolução: F = y'z + yz' + xz' (ou + xy', também mínima).

**Verificação:** todas as expressões conferidas contra a tabela-verdade completa em tests_acervo/test_sd_ecom012.py.
