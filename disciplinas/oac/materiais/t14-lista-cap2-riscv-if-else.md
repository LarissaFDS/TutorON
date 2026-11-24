---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-lista-cap2-ex1-ex2
titulo: Lista RISC-V do capítulo 2, Ex. 1 e 2 — if/else com menor valor e condição composta (a >= 0 && a < b) em RISC-V
assunto: oac-09-desvios-lacos-vetores
tipo: exercicio
questao: 1-2
fonte: OAC - RISC-V - Exercícios 2.pdf | p. 1
autoria: Enunciado: lista da turma (cap. 2), parafraseado pela equipe TutorON; resolução da equipe TutorON com auxílio de IA, simulada
fontes_catalogo: ufal-oac-lista-cap2
verificacao: conferida_por_codigo
status_resolucao: validada
---
Lista RISC-V do capítulo 2, Exercícios 1 e 2 (a lista não traz resposta). Status da resolução: validada (resolução da equipe TutorON, simulada no teste).

**Ex. 1.** a = 2, b = 1, m = a; se b < m, m = b; senão m = 0. O RISC-V desvia na condição contrária: "se b >= m, vá para o else".

```asm
       addi x5, x0, 2       # a = 2
       addi x6, x0, 1       # b = 1
       add  x7, x5, x0      # m = a
       bge  x6, x7, senao   # b >= m: condição falsa
       add  x7, x6, x0      # m = b
       jal  x0, fim
senao: addi x7, x0, 0       # m = 0
fim:
```

Com a = 2 e b = 1, termina com m = 1.

**Ex. 2.** x = 1 se a >= 0 e a < b; x = 2 se a < 0 e a > b; senão x = 3. Cada && vira dois desvios seguidos: qualquer parte falsa pula para o caso seguinte. Aqui a em x11, b em x12 e x em x10.

```asm
        bge  x11, x0, naoneg   # a >= 0: testa o primeiro caso
        bge  x12, x11, padrao  # a < 0, mas b >= a: não vale a > b
        addi x10, x0, 2
        jal  x0, fim
naoneg: bge  x11, x12, padrao  # a >= b: não vale a < b
        addi x10, x0, 1
        jal  x0, fim
padrao: addi x10, x0, 3
fim:
```

Exemplos: (a, b) = (1, 5) → 1; (−1, −4) → 2; (5, 1) → 3; (−3, 2) → 3.
