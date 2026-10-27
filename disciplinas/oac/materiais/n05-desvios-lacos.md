---
id: oac-nota-desvios-lacos
titulo: Nota — desvios, if/else, laços while e comparação com e sem sinal (blt × bltu)
assunto: oac-09-desvios-lacos-vetores
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: riscv-isa-manual,cs61c-berkeley
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Instruções de decisão (Patterson & Hennessy, seções 2.4 e 2.7; slides "Compiling If Statements", "Compiling Loop Statements" e "Signed vs. Unsigned").

Desvios condicionais: beq, bne, blt, bge (com sinal), bltu, bgeu (sem sinal). O rótulo vira um deslocamento relativo ao PC, calculado pelo montador.

if/else — C: if (i == j) f = g + h; else f = g − h; com f, g, h, i, j em x19 a x23:
```asm
      bne x22, x23, Else    # i != j: vai para o else
      add x19, x20, x21     # f = g + h
      beq x0, x0, Exit      # desvio incondicional (x0 == x0)
Else: sub x19, x20, x21     # f = g - h
Exit: ...
```
Repare que o teste é invertido: o desvio pula o "então" quando a condição é falsa.

while — C: while (save[i] == k) i += 1; com i em x22, k em x24 e o endereço de save em x25:
```asm
Loop: slli x10, x22, 2      # x10 = i * 4
      add  x10, x10, x25    # x10 = &save[i]
      lw   x9, 0(x10)       # x9 = save[i]
      bne  x9, x24, Exit    # sai se save[i] != k
      addi x22, x22, 1      # i += 1
      beq  x0, x0, Loop     # volta ao teste
Exit: ...
```

Com sinal × sem sinal: os mesmos 32 bits podem representar valores diferentes. Com x22 = 0xFFFFFFFF e x23 = 0x00000001: com sinal, x22 = −1 < +1, então blt x22, x23 desvia; sem sinal, x22 = 4.294.967.295 > 1, então bltu x22, x23 não desvia. Truque: bltu x20, x11, ok testa 0 ≤ x20 < x11 de uma vez (índice negativo vira um número grande sem sinal), útil para checar limites de vetor.
