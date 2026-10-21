---
id: sd-av1-q08-13
titulo: Lista AV1 — circuitos combinacionais, multiplexadores e deslocador (Q8–Q13)
assunto: sd-04-blocos-combinacionais
tipo: lista
resolucao: sim
questao: 8-13
fonte: Lista de SD AV1.pdf | páginas 2–3 | questões 8 a 13
fontes_catalogo: ufal-sd-lista-av1
autoria: Enunciados: lista de exercícios da disciplina (UFAL). Resoluções: equipe TutorON
licenca: Não declarada (material original da disciplina)
publicacao_transcricao: autorizada pela responsável pela curadoria em 2026-10-21, só para esta transcrição Markdown; não é licença aberta; arquivo original fora do repositório; aprovação do professor ou monitor não declarada
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Lista de SD AV1 — Circuitos Combinacionais

8. Um circuito tem entradas x1 (mais significativo) e x0 (menos significativo), que representam inteiros de 0 a 3, e uma saída que é 0 para todos os valores, exceto 2. Qual expressão representa o circuito? (As alternativas estão em figura no original.)
Resolução: 2 = 10₂ → x1 = 1 e x0 = 0. **S = x1·x0'**.

9. Faça o circuito da figura com multiplexadores 2:1. (Figura não transcrita.) Ideia geral: um MUX 2:1 faz S = s'·I0 + s·I1; escolhendo uma variável como seleção (expansão de Shannon), F = x'·F(x=0) + x·F(x=1), e cada cofator vira entrada do MUX ou de outro MUX.

10. Usando MUX 2:1 e, se preciso, portas lógicas, desenhe um deslocador programável de 4 bits E que desloca para a direita i ∈ {0,1,2,3} bits, conforme op1 op0: 00 → S = E; 01 → S = E >> 1; 10 → S = E >> 2; 11 → S = E >> 3.
Resolução: deslocador em dois estágios (barrel shifter). Estágio 1, controlado por op0: desloca 0 ou 1 bit. Estágio 2, controlado por op1: desloca 0 ou 2 bits. Cada estágio tem 4 MUX 2:1; na posição em que o bit "sai" pela esquerda entra 0. Total: 8 MUX 2:1.

11. Faça um circuito que calcule S = A / 2^B, com 0 ≤ B ≤ 3 e 0 ≤ A ≤ 8, arredondando para baixo (ex.: 3/2 = 1).
Resolução: dividir por 2^B é deslocar A para a direita B posições. A precisa de 4 bits (8 = 1000), B de 2 bits; usa-se o deslocador da Q10 com op = B.

12. Implemente S = |A − B| com A e B de 4 bits. Ideia: calcular A − B e B − A (ou usar um comparador A ≥ B) e escolher por MUX o resultado não negativo.

13. Implemente S = (A + B)/2 com A e B de 4 bits.
Resolução: somador de 4 bits gera 5 bits (Cout S3 S2 S1 S0); dividir por 2 é descartar S0: **resultado = Cout S3 S2 S1** (4 bits, sem perder o vai-um).
