---
id: ed-notion-ponteiros-funcao
titulo: Anotações da turma (Notion) — ponteiros para funções, map, filter e integral numérica
assunto: ed-02-structs-funcoes
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Ponteiros para Funções / Map e Filter / Integral"
fontes_catalogo: ufal-ed-notion
autoria: Anotações de alunos da turma de Estrutura de Dados (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código revisado; o original não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
Ponteiro para função: `int (*op)(int, int) = soma;` e depois `op(2, 3)`. Com `typedef void (*Ordena)(int[], int);` um vetor de funções pode guardar vários métodos de ordenação e testar todos com o mesmo laço. Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

`map` em C: aplicar f a cada elemento, gravando num vetor de saída do mesmo tamanho. `filter`: copiar só os que passam no teste e devolver quantos foram copiados.

```c
int filter(const int v[], int n, int (*ok)(int), int saida[])
{
    int i, k = 0;
    for (i = 0; i < n; i++) if (ok(v[i])) saida[k++] = v[i];
    return k; /* 0 se nenhum passou */
}
```

Integral numérica (soma de Riemann): $\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1} f(x_i)\,\Delta x$, com $\Delta x = (b - a)/n$ e $x_i = a + i\,\Delta x$. O exemplo da aula usa o ponto da esquerda e n = 100; o erro diminui quando n cresce.

Correções da equipe
- Divergência: as funções da anotação devolviam um único valor (o último), não a lista transformada; `filter` devolvia `result` não inicializado quando nada passava.
- O exemplo "Map e Filter" estava em Haskell, não em C; aqui fica a versão em C.
- `volume_circulo` calcula o volume da esfera (4/3·π·r³); o nome certo é `volume_esfera`.
- Erro de digitação "decçara" (declara).
