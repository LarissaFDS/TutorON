---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações de alunos no Notion da turma); imagens e arquivos anexos não estão no repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações; trechos de código curtos foram conferidos
revisao_humana: pendente
fontes_catalogo: ufal-oac-notion
id: oac-notion-cap2-instrucoes
titulo: Anotações da turma (Notion) — cap. 2: instruções RISC-V, memória, lógicas, desvios e formatos (com correções)
assunto: oac-05-isa-registradores-memoria
tipo: material_estudo
fonte: Notion da turma, página "Capítulo 2" (texto e código; fotos e capturas de slides não foram lidas)
autoria: Alunos da turma de OAC (UFAL); revisão da equipe TutorON
status_resolucao: corrigida
---
Resumo das anotações dos alunos (aula de 21/07/2025 e revisão). Status da resolução: corrigida (cinco itens; ver "Correções").

Registradores são mais rápidos que a memória; só loads e stores acessam a memória. Aritméticas têm 3 operandos: add x5, x20, x21 (x5 = x20 + x21); sub; addi com constante.
Vetor A[i] de words: slli x6, x11, 2 (i × 4); add x6, x10, x6; lw x7, 0(x6).
Lógicas: and/andi, or/ori, xor/xori. Deslocamentos: slli multiplica por potência de 2; srli completa com zeros. Bytes: lb (com sinal), lbu (sem sinal), sb. Trocar maiúscula/minúscula ASCII: xori com 0x20 (bit 5).
Desvios: beq, bne, blt, bge (com sinal); bltu, bgeu (sem sinal). Bloco básico: sequência sem desvio no meio e sem entrada no meio.
Formatos (nomes do livro): R (add), I (addi, lw), S (sw), SB (beq), U (lui), UJ (jal).

Correções da equipe:
1. "sw x9, 48(x22) → x9 = A[12]" está invertido: sw grava na memória, A[12] = x9.
2. O imediato do beq não tem 16 bits: tem 12 bits, em múltiplos de 2 bytes (alcance de ±4 KiB).
3. Não existe lli no RISC-V. Para constantes há a pseudo-instrução li (vira addi, ou lui + addi); lui carrega os 20 bits altos.
4. Os exemplos "beq $s1, $s2, L1" usam sintaxe MIPS; no RISC-V os registradores são x0–x31 (s1 = x9).
5. srli divide por potência de 2 só números sem sinal; para inteiros com sinal use srai.
