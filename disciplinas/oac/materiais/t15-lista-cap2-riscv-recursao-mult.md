---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-lista-cap2-ex4-ex5
titulo: Lista RISC-V do capítulo 2, Ex. 4 e 5 — soma recursiva do intervalo [a, b] com pilha e multiplicação sem mul (com sinal)
assunto: oac-10-procedimentos
tipo: exercicio
questao: 4-5
fonte: OAC - RISC-V - Exercícios 2.pdf | p. 2
autoria: Enunciado: lista da turma (cap. 2), parafraseado pela equipe TutorON; resolução da equipe TutorON com auxílio de IA, simulada
fontes_catalogo: ufal-oac-lista-cap2
verificacao: conferida_por_codigo
status_resolucao: validada
---
Lista RISC-V do capítulo 2, Exercícios 4 e 5 (a lista não traz resposta). Status da resolução: validada (resolução da equipe TutorON, simulada no teste). Os Ex. 3 (inverter string trocando maiúsculas e minúsculas) e 6 (Fibonacci recursivo) não têm resolução aqui; o Ex. 6 segue o mesmo molde do fatorial recursivo (salvar x1 e o argumento na pilha).

**Ex. 4.** soma(a, b) = a se b = a; senão b + soma(a, b − 1). Se a > b, x10 = 1 e fim. a em x10, b em x11, resultado em x10. Como soma chama a si mesma, salva x1 e b na pilha.

```asm
main: bge  x11, x10, chama   # b >= a: intervalo válido
      addi x10, x0, 1        # a > b: erro
      jal  x0, fim
chama: jal x1, soma
      jal  x0, fim
soma: bne  x10, x11, rec
      jalr x0, 0(x1)         # caso base: devolve a
rec:  addi sp, sp, -8
      sw   x1, 4(sp)
      sw   x11, 0(sp)
      addi x11, x11, -1
      jal  x1, soma          # x10 = soma(a, b - 1)
      lw   x11, 0(sp)
      lw   x1, 4(sp)
      addi sp, sp, 8
      add  x10, x10, x11     # + b
      jalr x0, 0(x1)
fim:
```

Com a = 3 e b = 6: 3 + 4 + 5 + 6 = 18. Cuidado: com a = b = 1 o resultado também é 1, igual ao código de erro pedido na lista.

**Ex. 5.** a e b na memória (endereços 0 e 4), produto no endereço 8, sem mul. Somar a, |b| vezes, e trocar o sinal no fim se b < 0.

```asm
        lw   x5, 0(x0)      # a
        lw   x6, 4(x0)      # b
        addi x7, x0, 0      # produto
        addi x28, x0, 0     # 1 se b era negativo
        bge  x6, x0, laco
        sub  x6, x0, x6     # b = -b
        addi x28, x0, 1
laco:   beq  x6, x0, sinal
        add  x7, x7, x5
        addi x6, x6, -1
        jal  x0, laco
sinal:  beq  x28, x0, guarda
        sub  x7, x0, x7
guarda: sw   x7, 8(x0)
```

Exemplos: 7 × (−3) = −21; (−4) × (−5) = 20. O laço faz |b| voltas; somar e deslocar (shift-and-add) faz no máximo 32.
