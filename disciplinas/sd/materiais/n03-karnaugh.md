---
id: sd-nota-karnaugh
titulo: Nota — simplificação por mapa de Karnaugh (Veitch-Karnaugh) com irrelevâncias
assunto: sd-03-simplificacao-karnaugh
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: wikibooks-digital-circuits,wikilivros-eletronica-digital,kuphaldt-lec-vol4
autoria: Equipe TutorON, redigida com auxílio de IA; exemplo conferido por código; revisada pela responsável pela curadoria em 21/10/2026
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Mapa de Karnaugh (diagrama de Veitch-Karnaugh)

Para que serve: achar a expressão SOP mínima de uma função de até 4 (ou 5) variáveis sem manipular a álgebra.

Procedimento:
1. Monte o mapa com linhas e colunas na ordem de Gray (00, 01, 11, 10). Com 4 variáveis: AB nas linhas, CD nas colunas; a célula de AB = 01 e CD = 11 é o mintermo 0111 = m7.
2. Coloque 1 nos mintermos da função, 0 no resto e x nas irrelevâncias (combinações que nunca ocorrem ou cuja saída não importa).
3. Agrupe os 1 em retângulos de 1, 2, 4, 8 ou 16 células, os maiores possíveis. As bordas são vizinhas (o mapa "dá a volta"), e os quatro cantos formam um grupo.
4. Use x só quando ele aumentar um grupo; não é obrigatório cobrir x.
5. Escolha o menor número de grupos que cubra todos os 1 (primeiro os implicantes primos essenciais, que cobrem um 1 que nenhum outro grupo cobre).
6. Cada grupo vira um produto com as variáveis que não mudam dentro dele: a variável que vale 1 entra direta e a que vale 0 entra negada.

Exemplo: F(A,B,C,D) = Σm(0,2,5,7,8,10,13,15).
- Os quatro cantos (m0, m2, m8, m10) têm B = 0 e D = 0 → B'D'.
- O bloco central (m5, m7, m13, m15) tem B = 1 e D = 1 → BD.
- F = B'D' + BD = (B ⊕ D)'. **Verificação:** em m5 = 0101, B = 1 e D = 1 → F = 1; em m1 = 0001, B = 0 e D = 1 → F = 0, e de fato m1 não está na lista.

Forma POS: agrupe os 0 do mesmo jeito; cada grupo vira uma soma com as variáveis negadas ao contrário (a que vale 0 entra direta).

Erros comuns: grupos de 3 ou 6 células; esquecer a vizinhança das bordas; ler a coluna 10 como se viesse depois de 01; usar x como 1 obrigatório.
