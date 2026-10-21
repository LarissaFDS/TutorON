---
id: sd-somadores-monitoria
titulo: Somadores — meio somador, somador completo e somador de N bits (material de monitoria)
assunto: sd-05-circuitos-aritmeticos
tipo: material_estudo
resolucao: sim
fonte: Somadores.pdf | páginas 1–6
fontes_catalogo: ufal-sd-somadores
autoria: Material de monitoria da disciplina (UFAL); transcrição da equipe TutorON, com as barras de negação recuperadas e conferidas pela tabela-verdade
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
SOMADOR — Universidade Federal de Alagoas (material de monitoria)

O somador é um circuito combinacional que realiza a soma de bits. Há o meio somador e o somador completo.

1. Meio somador. Soma dois bits A e B sem considerar vai-um anterior. Serve, por exemplo, para os bits menos significativos de um somador de N bits.
Tabela-verdade (A B → S Cout): 00 → 0 0; 01 → 1 0; 10 → 1 0; 11 → 0 1.
Pelos mapas de Karnaugh de cada saída: S = A'B + AB' = **A ⊕ B** e **Cout = A·B**. O circuito é uma porta XOR e uma AND.

2. Somador completo. Forma geral: soma A, B e o vai-um da soma anterior (Cin), e pode ser usado em qualquer posição.
Tabela-verdade (A B Cin → S Cout): 000 → 0 0; 001 → 1 0; 010 → 1 0; 011 → 0 1; 100 → 1 0; 101 → 0 1; 110 → 0 1; 111 → 1 1.
Saída S: S = Cin'·A'·B + Cin'·A·B' + Cin·A'·B' + Cin·A·B = Cin'·(A ⊕ B) + Cin·(A ⊕ B)' = **A ⊕ B ⊕ Cin**.
Saída Cout pelo mapa de Karnaugh: **Cout = A·B + Cin·A + Cin·B** (vale 1 quando pelo menos duas entradas são 1).

3. Somador de N bits. Vários somadores ligados em cascata: o Cout de cada estágio vai para o Cin do seguinte (ripple-carry). O primeiro estágio pode ser um meio somador ou um somador completo com Cin = 0. O atraso cresce com N, porque o vai-um precisa atravessar todos os estágios.
