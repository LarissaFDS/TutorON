---
id: sd-ecom012-listas-6-7
titulo: Circuitos Digitais (ECOM012), listas das aulas 6 e 7 — tanque com eletroválvulas, chave seletora, paridade, codificador, Gray para binário e decodificadores
assunto: sd-04-blocos-combinacionais
tipo: lista
resolucao: sim
questao: aulas 6-7
fonte: Listas de exercícios das aulas 6 e 7 de Circuitos Digitais (UFAL) | enunciados parafraseados
fontes_catalogo: ufal-ecom012-listas
autoria: Enunciados: listas da disciplina Circuitos Digitais (UFAL), professor não identificado. Resoluções: equipe TutorON com apoio de IA
licenca: Não declarada (lista da disciplina; original não versionado)
publicacao_transcricao: não autorizada; enunciados parafraseados, figuras descritas em texto
curadoria: aprovado
natureza: material_da_disciplina
revisao_humana: pendente
verificacao: conferida_por_codigo
---
Circuitos Digitais (ECOM012) — listas das aulas 6 e 7

Aula 6.
1. Tanque com sensor de nível máximo N (1 = cheio), botão B (1 = encher) e válvulas de entrada VE e de saída VS. Suposição: o tanque esvazia por completo enquanto B = 0. **VE = B·N'** e **VS = B'**.
2. Chave seletora digital de 2 entradas é um MUX 2:1: **Y = S'·I0 + S·I1**.
3. Três chaves A, B e C, ligadas ao terra, com saída S; detectar um número par de chaves ligadas. Se "ligada" vale 1, **S = (A ⊕ B ⊕ C)'**. Se a chave fechada leva a entrada a 0 (resistor de pull-up), "par de ligadas" equivale a "ímpar de 1s", e **S = A ⊕ B ⊕ C**. Diga qual convenção usou.

Aula 7.
1. Codificador 4 para 2, com exatamente uma entrada I0–I3 alta: **Y1 = I2 + I3** e **Y0 = I1 + I3**.
2. Decodificador do código Gray para o sistema binário comum (n bits): o bit mais significativo é copiado, Bₙ₋₁ = Gₙ₋₁; para os demais, Bᵢ = Bᵢ₊₁ ⊕ Gᵢ. Em 4 bits: B3 = G3, B2 = G3⊕G2, B1 = G3⊕G2⊕G1, B0 = G3⊕G2⊕G1⊕G0.
3. Quatro fios com nível 0 em apenas um, escolhido por 2 bits S1 S0: é um decodificador 2 para 4 com saídas ativas em baixo. Yᵢ = NAND do mintermo i (Y0 = (S1'S0')', …).
4. Decodificador 3 para 8: três NOT e oito AND de 3 entradas, uma por mintermo (veja o bloco das provas de ECOM012).

**Verificação:** tanque, MUX, paridade, codificador, Gray e decodificador ativo em baixo conferidos por enumeração em tests_acervo/test_sd_ecom012.py.
