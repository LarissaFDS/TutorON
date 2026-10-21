---
id: sd-reav-q2-q4
titulo: Reavaliação — FSM de baixo nível da média de 16 posições de memória e RTL do MDC (Q2 e Q4)
assunto: sd-10-projeto-rtl
tipo: prova
resolucao: sim
questao: 2,4
fonte: REAV.pdf | páginas 1–3 | questões 2 e 4 (prova fotografada; figura do bloco operacional descrita pela equipe)
fontes_catalogo: ufal-sd-reav
autoria: Enunciados: reavaliação da disciplina (UFAL). Descrição da figura e esboços: equipe TutorON
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: candidato
natureza: material_da_disciplina
verificacao: nao_verificada
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Reavaliação (REAV) — continuação

2. (2,0) Exiba a FSM de baixo nível que controla o bloco operacional da figura. O bloco calcula a média de um array de 16 elementos guardado na memória a partir do endereço 26. M_end é o endereço acessado e M_dados é o dado nesse endereço.
Figura: registradores i (i_ld, i_clr), soma (s_ld, s_clr), a (a_ld, a_clr, carregado de M_dados) e média (média_ld, média_clr); somador i + constante gerando M_end (a figura parece mostrar 25; o enunciado diz endereço 26, então confira se i começa em 0 ou 1); incrementador i + 1; comparador i < 16 gerando o status i_lt16; somador soma + a; deslocador >> 4 (divide por 16) na entrada de média.
Esboço: Início: i_clr, s_clr. Ler: a_ld (a ← M[M_end]). Acumular: s_ld (soma ← soma + a), i_ld (i ← i + 1). Testar: com i_lt16 volta a Ler; senão Fim: média_ld (média ← soma >> 4). Ajuste a condição de parada ao valor inicial de i para somar exatamente 16 elementos.

4. (3,0) Apresente a FSM de alto nível, o bloco operacional e a FSM de baixo nível para o algoritmo: Entradas: byte a, byte b, bit comece. Saídas: byte mdc, bit terminado.
MDC: while (1) { while (!comece); terminado = 0; while (a != b) { if (a > b) a = a - b; else b = b - a; } mdc = a; terminado = 1; }
Esboço (MDC de Euclides por subtrações):
- FSM de alto nível: Espera (até comece) → Inicia (terminado = 0; carrega a e b) → Compara (a ≠ b? a > b?) → SubA (a = a − b) ou SubB (b = b − a), voltando a Compara → Fim (mdc = a; terminado = 1) → Espera.
- Bloco operacional: registradores a, b, mdc (8 bits) e terminado; subtratores a − b e b − a; MUX na entrada de a e de b (valor de entrada ou diferença); comparadores a ≠ b e a > b como sinais de status.
- FSM de baixo nível: cada estado ativa a_ld/a_sel, b_ld/b_sel, mdc_ld e terminado; as transições usam os status a_ne_b e a_gt_b.
