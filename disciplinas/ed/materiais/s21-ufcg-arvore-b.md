---
id: ed-ufcg-arvore-b
titulo: Árvore B — propriedades, busca, divisão do nó na mediana e remoção, em C (UFCG)
assunto: ed-15-arvores-balanceadas
tipo: material_estudo
resolucao: sim
fonte: Slides de Estrutura de Dados da UFCG (DSC), Prof. Adalberto Cajueiro, 2013, aula "Árvore B"
fontes_catalogo: ufcg-ed-cajueiro-slides
autoria: Conteúdo dos slides do Prof. Adalberto Cajueiro (UFCG), parafraseado e reescrito em C pela equipe TutorON com auxílio de IA
licenca: Não declarada nos slides
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código C novo; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Árvore B de ordem m: cada nó tem no máximo m filhos; um nó com k filhos guarda k − 1 chaves em ordem; todo nó interno que não é a raiz tem pelo menos $\lceil m/2 \rceil$ filhos; a raiz, se não for folha, tem pelo menos 2; todas as folhas ficam no mesmo nível. Status da resolução: validada (conferida pela equipe TutorON com programa C; não é gabarito do professor). Os slides escrevem "m/2 filhos"; para m ímpar vale o teto, $\lceil m/2 \rceil$. Serve para dados em disco: nós largos deixam a árvore baixa, altura O(log n) e poucos acessos.

Busca: dentro do nó, ache a primeira chave maior ou igual a k; se for igual, achou; se não, desça pelo filho daquela posição.

Inserção: sempre numa folha. Se o nó passar a ter m chaves (estouro), divida: as chaves à esquerda da mediana ficam no nó, as da direita vão para um nó novo e a mediana sobe para o pai, que pode estourar também. Se a raiz se dividir, nasce uma raiz nova com só a mediana: é assim que a árvore B cresce, sempre para cima. Exemplo de ordem 3: inserir 10, 20 e 30 dá o nó [10 20 30], que estoura; 20 sobe e vira a raiz, com filhos [10] e [30].

```c
static int dividir(NoB *x, NoB **dir)
{
    int meio = x->n / 2, j;
    NoB *d = novo_no();
    if (d == NULL) exit(1);
    d->n = x->n - meio - 1;
    for (j = 0; j < d->n; j++) d->chave[j] = x->chave[meio + 1 + j];
    for (j = 0; j <= d->n; j++) {
        d->filho[j] = x->filho[meio + 1 + j];
        x->filho[meio + 1 + j] = NULL;
    }
    x->n = meio;
    *dir = d;
    return x->chave[meio];
}
```

O nó tem uma vaga extra (chave[M], filho[M + 1]) para guardar o estouro antes de dividir; quem chama põe a mediana devolvida e o nó *dir no pai.

Remoção: em nó interno, troque a chave pela antecessora ou sucessora (que está numa folha) e remova na folha. Se a folha ficar com menos de $\lceil m/2 \rceil - 1$ chaves, pegue uma chave emprestada de um irmão vizinho que tenha sobra (passando pelo pai) ou funda o nó com um irmão e a chave separadora do pai. A fusão pode se propagar até a raiz e diminuir a altura.
