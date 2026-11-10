---
id: sd-nota-blocos-combinacionais
titulo: Nota — multiplexador, demultiplexador, decodificador, codificador e deslocador
assunto: sd-04-blocos-combinacionais
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: wikibooks-digital-circuits,kuphaldt-lec-vol4,wikilivros-eletronica-digital
autoria: Equipe TutorON, redigida com auxílio de IA; revisada pela responsável pela curadoria em 21/10/2026
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Blocos combinacionais

Multiplexador (MUX) 2ⁿ:1: escolhe uma de 2ⁿ entradas pelas n linhas de seleção.
- MUX 2:1: Y = s'·I0 + s·I1.
- MUX 4:1: Y = s1's0'·I0 + s1's0·I1 + s1s0'·I2 + s1s0·I3.
- Barramento de k bits: k MUX em paralelo com a mesma seleção ("MUX 2:1 de 4 bits").
- Implementar uma função F com MUX (expansão de Shannon): F = x'·F(x = 0) + x·F(x = 1). Com um MUX 4:1, use duas variáveis como seleção; cada entrada recebe 0, 1, a terceira variável ou o complemento dela.

Demultiplexador: leva uma entrada para uma de 2ⁿ saídas, escolhida pela seleção.

Decodificador n:2ⁿ: ativa exatamente a saída cujo índice é o valor da entrada; cada saída é um mintermo (decodificador 2:4: D0 = x1'x0', D1 = x1'x0, D2 = x1x0', D3 = x1x0). Uma função qualquer é a OR das saídas dos seus mintermos. Com enable E, todas as saídas ficam em 0 quando E = 0.

Codificador 2ⁿ:n faz o contrário. O codificador com prioridade resolve várias entradas ativas ao mesmo tempo, devolvendo o índice da mais prioritária e um bit de "entrada válida".

Display de 7 segmentos (a no topo, sentido horário a–f, g no meio): para cada segmento, monte a tabela "dígito → segmento aceso" e simplifique por Karnaugh. Para 0–3: b sempre aceso; a = d = x1 + x0'; c = x1' + x0; e = x0'; f = x1'x0'; g = x1.

Deslocador (shifter): MUX que escolhem entre o bit da própria posição e o do vizinho. Deslocar uma quantidade variável usa estágios de 1, 2, 4… posições, cada um controlado por um bit da quantidade (barrel shifter). Deslocar à direita k posições divide por 2ᵏ; à esquerda, multiplica.
