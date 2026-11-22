---
id: ed-cc-bfs-distancia-predecessor
titulo: Busca em largura (BFS) com fila: distância em arestas e predecessor de cada vértice, e o caminho de volta até a origem
assunto: ed-11-grafos
tipo: exercicio
resolucao: sim
fonte: Huxley, problema 805 (Busca em Largura), salvo na pasta da turma de CC
curso: Ciência da Computação (UFAL), material de Estrutura de Dados da turma de CC
fontes_catalogo: ufal-cc-ed-huxley
autoria: Enunciado: problema do Huxley (juiz on-line usado no IC-UFAL), parafraseado pela equipe TutorON; código e explicação da equipe TutorON, escritos com auxílio de IA e testados
licenca: Não declarada (página do Huxley salva pela turma); as páginas não estão no repositório
publicacao_transcricao: não se aplica: o bloco reescreve com texto e código próprios
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Como fazer a busca em largura marcando a distância e o predecessor de cada vértice? Use uma **fila**. Status da resolução: validada (código da equipe TutorON, compilado com -Wall -Wextra -Werror e testado em tests_acervo/c_ed/cc_huxley.c; não é gabarito do professor).

A BFS visita a origem, depois todos os vizinhos dela, depois os vizinhos dos vizinhos. Ao descobrir v a partir de u, marque `dist[v] = dist[u] + 1` e `pred[v] = u`. Como a fila respeita a ordem de descoberta, a distância marcada é o **menor número de arestas** da origem até v.

```c
void bfs(int n, int adj[][MAXV], int origem, int dist[], int pred[])
{
    int fila[MAXV], ini = 0, fim = 0, i, u, v;
    for (i = 0; i < n; i++) {
        dist[i] = -1;
        pred[i] = -1;
    }
    dist[origem] = 0;
    fila[fim++] = origem;
    while (ini < fim) {
        u = fila[ini++];
        for (v = 0; v < n; v++)
            if (adj[u][v] && dist[v] < 0) {
                dist[v] = dist[u] + 1;
                pred[v] = u;
                fila[fim++] = v;
            }
    }
}
```

Para reconstruir o caminho até um destino, siga `pred` a partir dele até chegar à origem (−1 marca o fim) e inverta a sequência. Vértice com `dist = -1` não é alcançável. Com a matriz de adjacência o custo é O(V²); com listas de adjacência, O(V + E).

No teste, o grafo tem as arestas 0–1, 0–2, 1–3, 2–3, 3–4 e 5–6. A partir de 0, as distâncias de 1 a 4 são 1, 1, 2 e 3; o predecessor de 3 é 1, porque 1 entra na fila antes de 2. Os vértices 5 e 6 ficam com −1.

A ordem de visita dos vizinhos muda os predecessores, mas não as distâncias: confira no enunciado se os vizinhos devem ser visitados em ordem crescente.

**Verificação:** compilado sem avisos e testado com asserts (distâncias, predecessores e vértices inalcançáveis).
