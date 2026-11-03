---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não se aplica: o bloco descreve o conteúdo didático do quadro; a foto original fica fora do repositório
revisao_humana: pendente
id: oac-aula-operando-memoria
titulo: Aula — operando em memória: A[12] = h + A[8] com lw/sw e endereçamento por byte
assunto: oac-05-isa-registradores-memoria
tipo: material_estudo
questao: 1
fonte: Foto do quadro em aula (slide "Memory Operand Example", cap. 2 — 13), transcrita; a foto não está no repositório porque mostra uma pessoa
autoria: Exemplo do slide de aula (Patterson & Hennessy, seção 2.3) com anotações do professor no quadro; transcrição e explicação da equipe TutorON
fontes_catalogo: ufal-oac-aula-foto
verificacao: conferida_por_codigo
status_resolucao: validada
---
Exemplo de aula: operando em memória (transcrição do quadro). Status: validada (conferida por simulação pela equipe TutorON).

Código C: A[12] = h + A[8]; com h em x21 e o endereço base de A em x22.

```asm
lw  x9, 32(x22)    # x9 = A[8]: índice 8 × 4 bytes = deslocamento 32
add x9, x21, x9    # x9 = h + A[8]
sw  x9, 48(x22)    # A[12] = x9: índice 12 × 4 = 48
```

Por que 32 acessa A[8]: a memória é endereçada por **byte**, e cada inteiro (palavra) ocupa **4 bytes**. A[0] ocupa os endereços base+0 a base+3, A[1] ocupa base+4 a base+7, e assim por diante; A[i] começa em base + 4i. Logo A[8] começa em base + 32. O deslocamento do lw/sw é em bytes, não em posições do vetor.

Anotações do quadro: à esquerda, o banco de registradores (x0 a x31, cada um com 4 bytes); à direita, a memória com uma célula de 1 byte por endereço (0x0, 0x1, 0x2…). A[0] ocupa as células 0x0–0x3 e A[1] as células 0x4–0x7. O lw copia uma palavra da memória para o registrador; o sw copia do registrador para a memória. No quadro, com x22 = 4, o endereço efetivo de 32(x22) é 4 + 32 = **36**.

Verificação: endereço efetivo = valor de rs1 + imediato. Para sw, 4 + 48 = 52 = 4 + 12 × 4.
