---
id: ed-notion-hash
titulo: Anotações da turma (Notion) — tabela hash com endereçamento aberto e com encadeamento
assunto: ed-09-hash
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Hash"
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
Função hash h(k) = k mod M. Colisão: duas chaves com o mesmo h (com M = 7, as chaves 3, 10, 17 e −4 caem em 3). Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

Endereçamento aberto (sondagem linear): procura em h, h+1, ... Remover marca a posição como REMOVIDO, não como LIVRE; a busca passa pelo REMOVIDO e só para no LIVRE.

```c
static int h(int chave)
{
    int r = chave % M;
    return r < 0 ? r + M : r; /* em C, -3 % 7 == -3 */
}

int put_aberta(Aberta *t, int chave, int valor)
{
    int i, pos, livre = -1;
    pos = procurar(t, chave);
    if (pos >= 0) {
        t->valor[pos] = valor; /* chave já existe: atualiza */
        return 1;
    }
    for (i = 0; i < M && livre < 0; i++) {
        pos = (h(chave) + i) % M;
        if (t->estado[pos] != OCUPADO) {
            livre = pos; /* reaproveita REMOVIDO */
        }
    }
    if (livre < 0) {
        return 0; /* cheia: o chamador fica sabendo */
    }
    t->estado[livre] = OCUPADO;
    t->chave[livre] = chave;
    t->valor[livre] = valor;
    return 1;
}
```

Encadeamento: cada posição é uma lista; `put` primeiro procura a chave na lista e atualiza o valor se ela já existe.

Custo médio O(1 + α), com α = n/M o fator de carga; o pior caso é O(n). Mantenha α baixo (redimensionando a tabela).

Correções da equipe
- Divergência: em C, `-3 % 7` vale −3, então chave negativa dava índice negativo (escrita fora do vetor). Corrigido em `h`.
- `put` parava na primeira marca de removido sem ver se a chave existia mais adiante, o que duplicava a chave. O encadeamento também duplicava.
- A chave −1 era a marca de removido, então `get(-1)` achava lixo. Agora o estado é separado da chave.
- `remove` fazia `malloc` de um elemento novo só para marcar; tabela cheia falhava em silêncio; nada era liberado.
