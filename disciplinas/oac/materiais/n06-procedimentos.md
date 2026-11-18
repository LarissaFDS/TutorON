---
id: oac-nota-procedimentos
titulo: Nota — procedimentos: jal, jalr, pilha e registradores salvos
assunto: oac-10-procedimentos
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: riscv-isa-manual,cs61c-berkeley,unicamp-mc404-rodolfo
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
Procedimentos em RISC-V (Patterson & Hennessy, seção 2.8).

Seis passos: (1) o chamador coloca os argumentos em x10–x17; (2) transfere o controle com jal x1, rótulo (salva PC+4 em x1); (3) a função reserva o que precisa na pilha; (4) executa; (5) coloca o resultado em x10 (e x11); (6) retorna com jalr x0, 0(x1).

Pilha: cresce para endereços menores. Reservar 3 palavras: addi sp, sp, −12; liberar: addi sp, sp, 12. sp é x2.

Quem salva o quê: a função chamada deve preservar x8, x9 e x18–x27 (s0–s11) e sp; se usar algum deles, salva na pilha no início e restaura antes de retornar. Os temporários x5–x7 e x28–x31 e os argumentos podem ser destruídos; se o chamador precisar deles depois da chamada, ele é que salva.

Função folha (não chama ninguém), como swap: se usar só temporários, não precisa da pilha.

Função não folha (ex.: recursiva): precisa salvar x1 (ra) e os argumentos que usará depois da chamada:
```asm
fact: addi sp, sp, -8       # espaço para 2 palavras
      sw   x1, 4(sp)        # salva o endereço de retorno
      sw   x10, 0(sp)       # salva n
      addi x5, x10, -1      # x5 = n - 1
      bge  x5, x0, L1       # n >= 1: caso recursivo
      addi x10, x0, 1       # caso base: retorna 1
      addi sp, sp, 8
      jalr x0, 0(x1)
L1:   addi x10, x10, -1     # argumento n - 1
      jal  x1, fact         # chamada recursiva
      addi x6, x10, 0       # x6 = fact(n - 1)
      lw   x10, 0(sp)       # restaura n
      lw   x1, 4(sp)        # restaura ra
      addi sp, sp, 8
      mul  x10, x10, x6     # n * fact(n - 1) (extensão M)
      jalr x0, 0(x1)
```
