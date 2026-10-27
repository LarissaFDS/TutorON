---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-prova1-q4-swap
titulo: Prova 1, Q4 (duas versões) — sub-rotina swap em RISC-V
assunto: oac-10-procedimentos
tipo: gabarito
questao: 4
fonte: Prova 1 -_2025.1_-_GABARITO.pdf | p. 2 (versão A) e pp. 5–6 (versão B)
autoria: Enunciado: Prof. Erick de Andrade Barboza (Prova 1 de OAC, UFAL, 2025.1), parafraseado pela equipe TutorON; gabarito original da prova; resolução revisada pela equipe TutorON
fontes_catalogo: ufal-oac-prova1-2025-1
verificacao: conferida_por_codigo
status_resolucao: corrigida
---
Prova 1 de OAC (2025.1), Questão 4, igual nas duas versões. Escrever em RISC-V a função C abaixo; base de v em x10, k em x11, endereço de retorno em x1. Status da resolução: corrigida (o código do gabarito está certo e foi simulado; só os comentários foram corrigidos, porque usavam nomes de registradores do MIPS que não correspondem aos registradores usados).

```c
void swap(int v[], int k) {
    int temp;
    temp = v[k];
    v[k] = v[k+1];
    v[k+1] = temp;
}
```

```asm
swap: slli x5, x11, 2      # x5 (t0) = k * 4  (int tem 4 bytes)
      add  x5, x10, x5     # x5 = v + k*4 = endereço de v[k]
      lw   x6, 0(x5)       # x6 (t1) = temp = v[k]
      lw   x7, 4(x5)       # x7 (t2) = v[k+1]  (próxima palavra)
      sw   x7, 0(x5)       # v[k]   = x7
      sw   x6, 4(x5)       # v[k+1] = x6 (temp)
      jalr x0, 0(x1)       # retorna ao chamador
```

Correção dos comentários: o gabarito chamava x5 de "$t1", x6 de "$t0" e x7 de "$t2" (nomes do exemplo MIPS do livro). No RISC-V, x5 = t0, x6 = t1 e x7 = t2. Como swap é folha e só usa temporários (x5–x7), não precisa salvar nada na pilha.

Verificação: com v = {10, 20, 30} e k = 1, depois da chamada v = {10, 30, 20}.
