---
id: prog1-aula12-matrizes
titulo: Aula 12 — matrizes (arrays de duas dimensões): ler, percorrer, somar e transpor
assunto: prog1-08-matrizes
tipo: material_estudo
resolucao: sim
curso: Engenharia de Computação (UFAL), Programação 1 (ECOM002); slides do Prof. Rodrigo de Barros Paes; semestre não identificado
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 12 (Arrays com duas dimensões; livro, seção 10.7)
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
`float notas[5][4];` tem 5 linhas (alunos) e 4 colunas (notas); `notas[4][1] = 8.0;` é a segunda nota do quinto aluno. Ler do teclado: `scanf("%f", &notas[i][j]);`. Percorrer linha por linha: laço de fora nas linhas (i), de dentro nas colunas (j). Coluna por coluna: troque a ordem dos laços. De baixo para cima ou da direita para a esquerda: faça o índice descer de n − 1 até 0.

Para passar uma matriz a uma função, o número de colunas tem que aparecer no parâmetro (`int a[][MAX]`), porque o compilador precisa dele para achar `a[i][j]`.

```c
void transpor(int lin, int col, int a[][MAX], int t[][MAX])
{
    int i, j;
    for (i = 0; i < lin; i++) {
        for (j = 0; j < col; j++) {
            t[j][i] = a[i][j];
        }
    }
}

void somar(int lin, int col, int a[][MAX], int b[][MAX], int c[][MAX])
{
    int i, j;
    for (i = 0; i < lin; i++) {
        for (j = 0; j < col; j++) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
}
```

O padrão da transposta, achado na aula escrevendo as atribuições uma a uma: `t[j][i]` sempre recebe `a[i][j]`, e uma matriz 2 × 3 vira 3 × 2. Soma: as duas matrizes têm as mesmas dimensões N × M (1 ≤ N, M ≤ 100, com `#define MAX 100`). Matrizes de 100 × 100 inteiros cabem como variáveis locais, mas matrizes muito maiores devem ser globais ou `static` para não estourar a pilha. Status da resolução: validada (conferida por código pela equipe TutorON).
