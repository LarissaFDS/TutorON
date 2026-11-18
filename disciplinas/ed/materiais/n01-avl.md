---
id: ed-nota-avl
titulo: Nota da equipe — árvore AVL: fator de balanceamento e rotações simples e duplas
assunto: ed-10-arvores
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: ods-morin,feofiloff-algoritmos-c,usf-galles-visualizacao
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
A página de AVL do Notion está vazia; esta nota é da equipe e aguarda revisão humana.

AVL: ABB em que, em cada nó, as alturas das subárvores diferem no máximo em 1 (fator de balanceamento fb = altura(esq) − altura(dir) ∈ {−1, 0, 1}). A altura fica O(log n) (menor que 1,44·log₂(n + 2)), então busca, inserção e remoção custam O(log n).

Depois de inserir, suba atualizando alturas. No primeiro nó com |fb| = 2:
- LL (inseriu à esquerda da esquerda): rotação simples à direita.
- RR: rotação simples à esquerda.
- LR: rotação à esquerda no filho, depois à direita no nó (dupla).
- RL: à direita no filho, depois à esquerda no nó.

```c
static Arv *rot_dir(Arv *y)
{
    Arv *x = y->esq;
    y->esq = x->dir;
    x->dir = y;
    atualizar(y);
    atualizar(x);
    return x;
}
```

Teste: inserir 3, 2, 1 (LL), 1, 2, 3 (RR), 3, 1, 2 (LR) e 1, 3, 2 (RL); nos quatro casos a raiz final é 2 com altura 2. Erro comum: atualizar a altura do novo topo antes da do nó que desceu.
