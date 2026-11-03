---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações de alunos no Notion da turma); imagens e arquivos anexos não estão no repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações; trechos de código curtos foram conferidos
revisao_humana: pendente
fontes_catalogo: ufal-oac-notion
id: oac-notion-cap2-procedimentos
titulo: Anotações da turma (Notion) — cap. 2: chamada de procedimento, pilha, procedimento não folha e fatorial recursivo
assunto: oac-10-procedimentos
tipo: material_estudo
fonte: Notion da turma, página "Capítulo 2", seções de procedimento, laço e fatorial
autoria: Alunos da turma de OAC (UFAL); código do fatorial do livro (seção 2.8); revisão da equipe TutorON
status_resolucao: validada
---
Anotações dos alunos sobre procedimentos. Status da resolução: validada (código conferido por simulação).

Convenção: argumentos em x10–x17, resultado em x10, endereço de retorno em x1 (ra), ponteiro de pilha em x2 (sp). Temporários x5–x7 e x28–x31 (o chamado não precisa preservar); salvos x8–x9 e x18–x27 (o chamado preserva).
jal x1, rotulo chama (salva PC + 4 em x1); jalr x0, 0(x1) retorna. jalr com registrador também implementa tabelas de desvio (switch).
Procedimento não folha (chama outro, como na recursão): precisa empilhar x1 e os argumentos que usará depois.

Laço "while (save[i] == k)" das anotações:
```asm
Loop: lw x9, 0(x10)
      bne x9, x11, Exit
      addi x10, x10, 4
      jal x0, Loop
Exit:
```

Fatorial recursivo (n em x10):
```asm
fact: addi sp, sp, -8
      sw x1, 4(sp)
      sw x10, 0(sp)
      addi x5, x10, -1
      bge x5, x0, L1
      addi x10, x0, 1
      addi sp, sp, 8
      jalr x0, 0(x1)
L1:   addi x10, x10, -1
      jal x1, fact
      add x6, x10, x0
      lw x10, 0(sp)
      lw x1, 4(sp)
      addi sp, sp, 8
      mul x10, x10, x6
      jalr x0, 0(x1)
```
Se n − 1 ≥ 0, vai para L1 e calcula n × fact(n − 1); senão devolve 1.

Dicas da turma para a lista: no Ex. 5, multiplicar por somas repetidas tratando o sinal; no Ex. 6 (Fibonacci), tratar n = 0 e n = 1 antes da recursão.
