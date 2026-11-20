---
id: prog1-aula11-vetores
titulo: Aula 11 — arrays (vetores), inicialização e como passar um vetor para uma função
assunto: prog1-07-vetores
tipo: material_estudo
resolucao: sim
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 11 (Arrays; livro, capítulo 10)
fontes_catalogo: ufal-prog1-slides-paes
autoria: Slides do Prof. Rodrigo de Barros Paes (IC/UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio e código revisado; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
`float valores[1000];` reserva 1000 posições, de `valores[0]` a `valores[999]`. Acessar `valores[1000]` passa do fim: comportamento indefinido, mesmo que "pareça funcionar". `int v[100] = {0};` zera tudo; `{5, 12}` preenche as duas primeiras e zera o resto.

**Como passar um vetor para uma função em C**: passe o vetor **e o tamanho**. O parâmetro `float n[]` recebe o endereço do primeiro elemento (não uma cópia), então a função enxerga e pode alterar o vetor original; use `const` quando ela só lê. Dentro da função, `sizeof n` dá o tamanho de um ponteiro, não do vetor: o tamanho tem que vir como parâmetro. Na chamada, só o nome: `media(notas, tam)`, sem `[]` nem `&`.

```c
float media(const float n[], int tam)
{
    int i;
    float soma = 0;
    for (i = 0; i < tam; i++) {
        soma += n[i];
    }
    return soma / tam;
}

float variancia(const float n[], int tam)
{
    int i;
    float var = 0;
    float m = media(n, tam);
    for (i = 0; i < tam; i++) {
        var += (n[i] - m) * (n[i] - m);
    }
    return var / tam;
}
```

Exemplo da aula: 8, 6, 7, 8, 7, 6, 6, 10 têm média 7,25 e variância populacional 1,6875; o desvio padrão é $\sqrt{1{,}6875} \approx 1{,}299038$ (raiz quadrada da variância). `sqrt` vem de `math.h`; no Linux, compile com `-lm`. Status da resolução: validada (código dos slides conferido por código pela equipe TutorON).
