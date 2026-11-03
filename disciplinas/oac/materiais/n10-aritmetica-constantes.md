---
id: oac-nota-aritmetica-constantes
titulo: Nota — constantes de 32 bits (lui/addi), extensão de sinal, overflow e ponto flutuante IEEE 754
assunto: oac-12-aritmetica
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: riscv-isa-manual,pattersonhennessy-cod-riscv
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Aritmética e constantes no RISC-V (Patterson & Hennessy, seções 2.4, 2.10, 3.2 e 3.5). Complemento de 2 e somadores em si são de Sistemas Digitais; aqui o foco é o que a ISA faz com eles.

Extensão de sinal: o imediato de 12 bits do formato I é estendido para 32 bits repetindo o bit 11. Ex.: imediato 0xFFF = −1, então addi x5, x0, −1 deixa x5 = 0xFFFFFFFF. lb estende o sinal do byte; lbu completa com zeros.

Constante de 32 bits: lui rd, imm20 carrega os 20 bits superiores (rd = imm20 << 12); addi completa os 12 inferiores. Como o addi estende o sinal, se o bit 11 da parte baixa for 1, some 1 à parte alta. Ex.: 0x12345678 → lui x5, 0x12345; addi x5, x5, 0x678. Ex.: 0x00001800 → a parte baixa 0x800 vale −2048 no addi, então lui x5, 0x2; addi x5, x5, −2048.

Overflow: o RISC-V não gera exceção de overflow em add/sub; o software testa quando precisa. Em soma com sinal, há overflow quando os dois operandos têm o mesmo sinal e o resultado tem sinal diferente; sem sinal, quando o resultado é menor que um dos operandos (teste com bltu).

Multiplicação e divisão (extensão M): mul (32 bits baixos), mulh/mulhu (32 bits altos), div, divu, rem, remu.

IEEE 754 precisão simples: sinal (1) | expoente (8, viés 127) | fração (23). Valor = (−1)ˢ × (1 + fração) × 2^(expoente − 127). Ex.: −0,75 = −1,1₂ × 2⁻¹ → s = 1, expoente = 126 = 01111110, fração = 100…0 → 0xBF400000. Precisão dupla: expoente de 11 bits (viés 1023) e fração de 52.
