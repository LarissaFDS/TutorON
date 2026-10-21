---
id: sd-nota-algebra-booleana
titulo: Nota — álgebra booleana, De Morgan, portas lógicas, mintermos e formas SOP/POS
assunto: sd-02-algebra-booleana-portas
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: kuphaldt-lec-vol4,wikilivros-eletronica-digital,wikibooks-digital-circuits
autoria: Equipe TutorON, redigida com auxílio de IA; revisada pela responsável pela curadoria em 21/10/2026
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Álgebra booleana e portas lógicas

Portas: NOT (A'), AND (A·B), OR (A + B), NAND ((A·B)'), NOR ((A + B)'), XOR (A ⊕ B = A'B + AB', vale 1 quando as entradas diferem) e XNOR ((A ⊕ B)', vale 1 quando são iguais; é o comparador de igualdade de 1 bit).

Propriedades úteis:
- Identidade e anulação: A + 0 = A; A·1 = A; A + 1 = 1; A·0 = 0.
- Idempotência e complemento: A + A = A; A·A' = 0; A + A' = 1; (A')' = A.
- Comutativa, associativa e distributiva, inclusive A + B·C = (A + B)(A + C).
- Absorção: A + A·B = A; A·(A + B) = A; A + A'B = A + B.
- Consenso: AB + A'C + BC = AB + A'C.
- De Morgan: (A·B)' = A' + B'; (A + B)' = A'·B'. Na prática: troque AND por OR e negue cada termo.

Da tabela-verdade à expressão: cada linha com saída 1 é um mintermo (produto com todas as variáveis, negando as que valem 0); a soma dos mintermos é a forma canônica SOP, escrita Σm(...). As linhas com saída 0 dão os maxtermos e a forma POS, ΠM(...). Exemplo: S = 1 em ABC = 011 e 110 → S = A'BC + ABC'.

Do circuito à expressão: escreva a saída de cada porta, da entrada para a saída, e substitua até chegar a uma única expressão; depois monte a tabela-verdade.

Portas universais: só com NAND (ou só com NOR) se constrói qualquer função. NOT = NAND com as entradas ligadas; AND = NAND seguida de NOT; OR = NAND das entradas negadas (De Morgan). Uma SOP de dois níveis vira diretamente NAND-NAND.
