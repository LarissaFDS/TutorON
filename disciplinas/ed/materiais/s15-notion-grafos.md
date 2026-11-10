---
id: ed-notion-grafos
titulo: Anotações da turma (Notion) — grafos em lista de adjacência, BFS e DFS em C
assunto: ed-11-grafos
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "DFS / BFS"
fontes_catalogo: ufal-ed-notion
autoria: Anotações de alunos da turma de Estrutura de Dados (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código revisado; o original não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Lista de adjacência: um vetor de listas, uma por vértice. BFS (busca em largura) usa fila e dá a distância em arestas a partir da origem; DFS (busca em profundidade) usa recursão (ou pilha). As duas custam O(V + E). Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

```c
int bfs(Grafo *g, int s, int ordem[], int dist[])
{
    int fila[MAXV], ini = 0, fim = 0, k = 0, i;
    Adj *p;
    for (i = 0; i < g->n; i++) {
        g->visitado[i] = 0;
        dist[i] = -1;
    }
    g->visitado[s] = 1;
    dist[s] = 0;
    fila[fim++] = s;
    while (ini < fim) {
        int u = fila[ini++];
        ordem[k++] = u;
        for (p = g->vizinhos[u]; p != NULL; p = p->prox) {
            if (!g->visitado[p->v]) {
                g->visitado[p->v] = 1; /* marca ao enfileirar, não ao sair */
                dist[p->v] = dist[u] + 1;
                fila[fim++] = p->v;
            }
        }
    }
    return k;
}
```

Marque o vértice como visitado ao enfileirar, não ao desenfileirar; senão ele entra na fila mais de uma vez.

Correções da equipe
- Divergência: `create_graph` iniciava os vértices com o laço a partir de i = 1, então `vertices[0]` e `visited[0]` ficavam com lixo. O laço começa em 0.
- O grafo nunca era liberado. A fila do BFS da aula estava correta.
