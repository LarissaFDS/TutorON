---
id: ed-notion-structs
titulo: Anotações da turma (Notion) — structs, vetor de structs e leitura com scanf
assunto: ed-02-structs-funcoes
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Structs"
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
`struct` agrupa campos de tipos diferentes; `typedef` dá um nome curto. Acesso: `x.campo` para a struct, `p->campo` para um ponteiro (é o mesmo que `(*p).campo`). Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

Vetor de structs com tamanho lido do usuário: leia n primeiro e só então aloque.

```c
int n;
struct personagem *p;
if (scanf("%d", &n) != 1 || n <= 0) return 1;
p = malloc((size_t)n * sizeof *p);
if (p == NULL) return 1;
/* ... scanf("%49s", p[i].nome) para char nome[50] ... */
free(p);
```

Correções da equipe
- Divergência: a anotação fazia `int n; struct personagem p[n];` antes do `scanf` de n. O tamanho do VLA vinha de uma variável não inicializada (comportamento indefinido). VLA também é opcional desde C11; com malloc o código vale em qualquer padrão.
- `scanf("%s")` sem largura pode estourar o vetor; use a largura do vetor menos 1 (`%49s`).
