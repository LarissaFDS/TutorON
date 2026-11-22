---
id: sd-ecom012-listas-4-5
titulo: Circuitos Digitais (ECOM012), listas das aulas 4 e 5 — expressão de circuitos, XNOR/XOR e simplificação por mapa de Karnaugh
assunto: sd-03-simplificacao-karnaugh
tipo: lista
resolucao: sim
questao: aulas 4-5
fonte: Listas de exercícios das aulas 4 e 5 de Circuitos Digitais (UFAL) | figuras descritas pela equipe
fontes_catalogo: ufal-ecom012-listas
autoria: Enunciados: listas da disciplina Circuitos Digitais (UFAL), professor não identificado. Resoluções: equipe TutorON com apoio de IA
licenca: Não declarada (lista da disciplina; original não versionado)
publicacao_transcricao: não autorizada; enunciados parafraseados, figuras descritas em texto
curadoria: aprovado
natureza: material_da_disciplina
revisao_humana: pendente
verificacao: parcial
---
Circuitos Digitais (ECOM012) — listas das aulas 4 e 5

Aula 4. (1) A partir de S = (A ⊙ B)', chegue a A ⊕ B: (A ⊙ B)' = (AB + A'B')' = (A' + B')(A + B) = A'B + AB' = A ⊕ B. (2) Circuito 1: o mesmo da AB1, F = [AB' + (A'+C)]·(A'+C)' = **AB'C'**. (3) Circuito 2: uma NAND de A e B, uma XOR dessa saída com C, uma OR de D' com E e uma AND final: **X = ((AB)' ⊕ C)·(D' + E)**. (4) Circuitos de X = AB + CDE e X = A + (BC + DE) + H. (5) Tabela-verdade com X = 1 nas linhas 000, 100 e 111: **X = B'C' + ABC**.

Aula 5. Forma mínima em soma de produtos:
1. Mapa com linha x e colunas yz (Gray). x = 0: 1 0 0 1; x = 1: 1 0 1 1. **F = z' + xy**.
2. Mapa 4×4 com linhas xy e colunas zw, o mesmo da AB1: **F = w' + y'z'**.
3. Mapa com linhas gh e colunas ij. As linhas com h = 0 são 0 1 1 0; as linhas com h = 1 são 1 0 0 1. **F = h'j + hj' = h ⊕ j**. Nenhum grupo maior que 2 é possível, porque os 1s se alternam.
4. Tabela-verdade com S = 1 em 000, 001, 011, 101 e 111: **S = C + Ā·B̄** (C ou nem A nem B).
5. S = ABC + … com quatro termos: as barras de negação se perderam no arquivo, e o enunciado não foi transcrito.

**Verificação:** todas as expressões conferidas contra a tabela-verdade completa em tests_acervo/test_sd_ecom012.py.
