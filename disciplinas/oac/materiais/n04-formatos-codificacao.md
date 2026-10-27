---
id: oac-nota-formatos-codificacao
titulo: Nota — formatos R, I, S, B, U e J e codificação de instruções em binário
assunto: oac-07-formatos-codificacao
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: riscv-isa-manual,riscv-card-jameslzhu
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Formatos de instrução do RISC-V (Patterson & Hennessy, seções 2.5 e 2.10). Todas as instruções têm 32 bits; rs1, rs2 e rd ficam sempre nas mesmas posições para simplificar a decodificação ("bom projeto exige bons compromissos").

R  (registrador): funct7[31:25] | rs2[24:20] | rs1[19:15] | funct3[14:12] | rd[11:7] | opcode[6:0] — 7+5+5+3+5+7 = 32
I  (imediato, loads, jalr): imm[11:0] | rs1 | funct3 | rd | opcode — imediato de 12 bits em complemento de 2, com extensão de sinal
S  (stores): imm[11:5] | rs2 | rs1 | funct3 | imm[4:0] | opcode — o imediato é dividido para rs1 e rs2 não mudarem de lugar
B  (desvios condicionais, antes "SB"): como S, mas o imediato codifica o deslocamento em múltiplos de 2 bytes
U  (lui, auipc): imm[31:12] | rd | opcode
J  (jal, antes "UJ"): imm[20|10:1|11|19:12] | rd | opcode

Opcodes e funct3 usados nos exemplos: add/sub opcode 0110011, funct3 000 (funct7 0000000 para add, 0100000 para sub); addi opcode 0010011, funct3 000; lw opcode 0000011, funct3 010; sw opcode 0100011, funct3 010.

Exemplos (conferidos pela equipe):
- add x9, x21, x9 → 0000000 01001 10101 000 01001 0110011 = 0x009A84B3
- sub x19, x20, x21 → 0100000 10101 10100 000 10011 0110011 = 0x415A09B3
- addi x22, x22, 1 → 000000000001 10110 000 10110 0010011 = 0x001B0B13
- lw x9, 32(x22) → 000000100000 10110 010 01001 0000011 = 0x020B2483
- sw x9, 48(x22): 48 = 0000001 10000 → 0000001 01001 10110 010 10000 0100011 = 0x029B2823

Procedimento: (1) identifique o formato pelo tipo de instrução; (2) escreva opcode, funct3 e funct7; (3) converta os números dos registradores para 5 bits; (4) converta o imediato para binário de 12 bits em complemento de 2 e divida-o, se for S ou B; (5) junte os campos e confira 32 bits; (6) agrupe de 4 em 4 para o hexadecimal.
