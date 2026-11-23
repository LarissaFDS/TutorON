---
id: prog1-ec2-ordenacao-vetor
titulo: Ordenar um vetor em C: ordenação por trocas (i com j) e bolha de verdade (vizinhos, com parada antecipada)
assunto: prog1-07-vetores
tipo: material_estudo
resolucao: sim
curso: Engenharia de Computação (UFAL), 2º período; códigos de exercícios de uma turma de Programação, sem enunciado, professor nem semestre identificados
fonte: Códigos C de exercícios do material do 2º período de Engenharia de Computação (arquivo de "apêndice" com funções de vetor); usados só como evidência do tópico e do erro de nome
fontes_catalogo: ufal-ec2-prog1-codigos-c
autoria: Funções escritas e testadas pela equipe TutorON com auxílio de IA; nenhum código da turma foi copiado
licenca: Não declarada (códigos de aluno); o bloco usa código próprio
publicacao_transcricao: não se aplica: o bloco tem texto e código próprios; os códigos da turma não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo com código conferido. Status da resolução: validada (código da equipe TutorON, não é gabarito do professor; compilado e testado).

Ordenar é deixar o vetor em ordem crescente (ou decrescente, trocando `>` por `<`). O vetor é passado para a função e alterado nela, sem `return`: a função recebe o endereço do primeiro elemento.

**Ordenação por trocas.** Compara a posição `i` com cada posição `j` seguinte e troca quando estão fora de ordem. Ao fim da volta `i`, `v[i]` é o menor do que sobrou.

```c
void ordena_trocas(int v[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (v[i] > v[j]) {
                int aux = v[i];
                v[i] = v[j];
                v[j] = aux;
            }
        }
    }
}
```

**Bolha (bubble sort).** Compara só **vizinhos** (`v[j]` e `v[j + 1]`); a cada passada o maior "sobe" para o fim. Se uma passada não troca nada, o vetor já está ordenado e dá para parar.

```c
void bolha(int v[], int n)
{
    int trocou = 1;
    for (int fim = n - 1; fim > 0 && trocou; fim--) {
        trocou = 0;
        for (int j = 0; j < fim; j++) {
            if (v[j] > v[j + 1]) {
                int aux = v[j];
                v[j] = v[j + 1];
                v[j + 1] = aux;
                trocou = 1;
            }
        }
    }
}
```

Erros comuns: chamar de "bubblesort" a ordenação por trocas (funciona, mas não compara vizinhos); usar `j <= fim`, que lê `v[n]`, fora do vetor; trocar sem a variável `aux`.

Com um vetor de 6 elementos já ordenado, a bolha faz 5 comparações e para; a ordenação por trocas faz sempre 15 ($n(n-1)/2$). Algoritmos melhores (merge sort, quicksort) ficam para Estrutura de Dados.

**Verificação:** as duas funções foram compiladas com `-Wall -Wextra -pedantic -Werror` e AddressSanitizer/UBSan e testadas nas 1024 sequências de 5 valores entre 0 e 3; as contagens de comparações foram medidas.
