---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-prova1-b-q5
titulo: Prova 1, versão B, Q5 (numerada 4 por engano) — laços aninhados com beq: o que fica em x10
assunto: oac-09-desvios-lacos-vetores
tipo: gabarito
questao: 5
fonte: Prova 1 -_2025.1_-_GABARITO.pdf | p. 6 (versão B)
autoria: Enunciado: Prof. Erick de Andrade Barboza (Prova 1 de OAC, UFAL, 2025.1), parafraseado pela equipe TutorON; gabarito original da prova; resolução revisada pela equipe TutorON
fontes_catalogo: ufal-oac-prova1-2025-1
verificacao: conferida_por_codigo
status_resolucao: validada
---
Prova 1 de OAC (2025.1), versão B, última questão (impressa como "4)", mas é a quinta). Dois vetores de 2500 palavras; bases em x12 e x13; tamanhos (2500) em x14 e x15. Comentar o código e dizer o que retorna em x10. A única diferença para a versão A é o desvio: beq no lugar de bne. Status da resolução: validada (resposta do gabarito conferida por simulação pela equipe TutorON).

```asm
       slli x14, x14, 2     # x14 = 2500*4: tamanho de array1 em bytes
       slli x15, x15, 2     # x15 = tamanho de array2 em bytes
       add  x10, x0, x0     # x10 (a0) = contador = 0
       add  x5, x0, x0      # x5 (t0) = i*4 = 0
outer: add  x29, x12, x5    # x29 = &array1[i]
       lw   x29, 0(x29)     # x29 = array1[i]
       add  x6, x0, x0      # x6 (t1) = j*4 = 0
inner: add  x28, x13, x6    # x28 = &array2[j]
       lw   x28, 0(x28)     # x28 = array2[j]
       beq  x28, x29, skip  # iguais: não conta
       addi x10, x10, 1     # conta o par (i, j)
skip:  addi x6, x6, 4       # j++
       bne  x6, x15, inner  # ainda há elementos em array2
       addi x5, x5, 4       # i++
       bne  x5, x14, outer  # ainda há elementos em array1
```

Resposta (gabarito): x10 = quantidade de **pares (i, j) com valores diferentes**, entre todos os pares formados pelos dois vetores. Equivale a 2500 × 2500 − (pares iguais).

Verificação: com array1 = {1, 2, 3} e array2 = {3, 1, 1}, há 9 pares e 3 iguais, então x10 = 6.
