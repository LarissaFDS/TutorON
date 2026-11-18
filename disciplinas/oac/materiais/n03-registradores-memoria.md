---
id: oac-nota-registradores-memoria
titulo: Nota — RISC-V RV32: registradores, convenção de uso, memória por byte, alinhamento e endianness
assunto: oac-05-isa-registradores-memoria
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: riscv-isa-manual,riscv-card-jameslzhu
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
Registradores e memória no RISC-V RV32 (Patterson & Hennessy, seções 2.2 e 2.3; slides "RISC-V Registers").

Banco de registradores: 32 registradores de 32 bits (x0 a x31). Dado de 32 bits = "word" (palavra); de 64 bits = "doubleword". Registradores são usados para os dados acessados com frequência, porque são muito mais rápidos que a memória.

Convenção de uso (nome ABI entre parênteses):
- x0 (zero): sempre vale 0; escrever nele não tem efeito.
- x1 (ra): endereço de retorno. x2 (sp): ponteiro de pilha. x3 (gp): ponteiro global. x4 (tp): ponteiro de thread.
- x5–x7 (t0–t2) e x28–x31 (t3–t6): temporários, não preservados entre chamadas.
- x8 (s0/fp): frame pointer; x9 (s1) e x18–x27 (s2–s11): salvos, preservados pela função chamada.
- x10–x11 (a0–a1): argumentos e resultados; x12–x17 (a2–a7): argumentos.

Memória: endereçada por **byte**. Uma palavra ocupa 4 endereços consecutivos, então o elemento i de um vetor de int fica em base + 4i. Só lw/sw (e variantes lb, lh, lbu, lhu, sb, sh) acessam a memória; as operações aritméticas trabalham só com registradores (arquitetura load/store).

Endianness: o RISC-V é **little-endian**: o byte menos significativo da palavra fica no menor endereço. Ex.: a palavra 0x01234567 guardada no endereço 0 deixa 0x67 em 0, 0x45 em 1, 0x23 em 2 e 0x01 em 3 (como desenhado no quadro da aula, com A[0] ocupando 0x0–0x3).

Alinhamento: o RISC-V permite acesso desalinhado, mas ele pode ser lento ou gerar exceção conforme a implementação; o compilador alinha palavras em endereços múltiplos de 4.

MIPS × RISC-V: no MIPS do livro antigo, $t0–$t7 são os registradores 8–15 e $s0–$s7 são 16–23; no RISC-V os números e os nomes são outros.
