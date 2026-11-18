---
id: ed-notion-recorrencias
titulo: Anotações da turma (Notion) — equações de recorrência dos algoritmos da aula e método da expansão
assunto: ed-04-complexidade-recorrencias
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Equações de recorrência / Método da expansão"
fontes_catalogo: ufal-ed-notion
autoria: Anotações de alunos da turma de Estrutura de Dados (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código revisado; o original não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: pendente_professor
revisao_humana: pendente
---
Recorrência descreve o custo de uma função recursiva a partir do custo das chamadas menores. Status da resolução: pendente de confirmação do professor. O quadro da aula foi conferido; o motivo do status pendente é a frase sobre os casos-base, explicada abaixo.

Quadro da aula (conferido):
- Selection, Bubble, Insertion: T(n) = T(n − 1) + O(n) → O(n²).
- Merge sort e Quick sort no caso médio: T(n) = 2T(n/2) + O(n) → O(n log n).
- Busca binária: T(n) = T(n/2) + O(1) → O(log n).
- Faltava no quadro: o pior caso do Quick sort (pivô sempre o menor ou o maior) é T(n) = T(n − 1) + O(n) → O(n²).

Expansão do Merge sort, com $T(n) = 2T(n/2) + cn$: depois de k passos, $T(n) = 2^k\,T(n/2^k) + k\,cn$. Para $n/2^k = 1$, $k = \log_2 n$ e $T(n) = n\,T(1) + cn\log_2 n = O(n \log n)$.

Casos-base. A anotação diz que T(0) = 0 "por ser o elemento neutro da soma" e T(1) = 1 "por ser o elemento neutro da multiplicação". Divergência: o caso-base não vem de elemento neutro; ele vem do próprio algoritmo, é o custo de resolver a entrada mínima sem recursão. Ordenar 0 ou 1 elemento custa um teste: T(1) = c, uma constante. Escrever T(1) = 1 é só escolher a unidade de custo. Para a ordem de grandeza, qualquer constante positiva dá o mesmo O. Se T(0) = 0 e T(1) = 1 forem convenção adotada pelo professor, vale como convenção, não como regra; isso aguarda confirmação do professor.
