---
id: sd-nota-numeracao
titulo: Nota — bases numéricas, complemento de 2, overflow e códigos (BCD, Gray)
assunto: sd-01-numeracao-aritmetica
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: kuphaldt-lec-vol4,wikilivros-eletronica-digital,wikibooks-digital-circuits
autoria: Equipe TutorON, redigida com auxílio de IA; exemplos conferidos por código; revisada pela responsável pela curadoria em 21/10/2026
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Sistemas de numeração e aritmética binária

Conversão decimal → binário: divisões sucessivas por 2, lendo os restos de baixo para cima (13 → 1101). Binário → decimal: soma dos pesos 2ⁱ dos bits 1. Hexadecimal e octal: agrupe o binário de 4 em 4 ou de 3 em 3 bits a partir da direita (1011 0110₂ = B6₁₆).

Com n bits: 2ⁿ combinações. Sem sinal: 0 a 2ⁿ − 1.

Complemento de 2 (números com sinal): o bit mais significativo é o sinal. Intervalo: −2ⁿ⁻¹ a 2ⁿ⁻¹ − 1 (4 bits: −8 a 7). Para negar um número, inverta todos os bits e some 1; atalho: copie da direita até o primeiro 1 (inclusive) e inverta o resto. Exemplo, −6 em 4 bits: 0110 → 1001 → 1010. Para estender o sinal a mais bits, repita o bit de sinal à esquerda (1010 → 11111010).

Subtração: A − B = A + (complemento de 2 de B) = A + B' + 1. O mesmo somador faz soma e subtração.

Overflow:
- Sem sinal: o vai-um final (Cout = 1) na soma indica estouro; na subtração A + B' + 1, Cout = 0 indica A < B.
- Com sinal (complemento de 2): somar dois números de mesmo sinal e obter resultado de sinal oposto. Detector: V = Cₙ ⊕ Cₙ₋₁ (vai-um que entra e vai-um que sai do bit de sinal). Exemplo em 4 bits: 0101 + 0100 = 1001 → 5 + 4 dá −7, overflow.

Multiplicação e divisão por 2ᵏ: deslocar k bits à esquerda ou à direita (em números com sinal, o deslocamento aritmético à direita repete o bit de sinal).

Códigos: BCD codifica cada dígito decimal em 4 bits (59 → 0101 1001). O código Gray muda um único bit entre valores vizinhos (00, 01, 11, 10) e é a ordem das linhas e colunas do mapa de Karnaugh.
