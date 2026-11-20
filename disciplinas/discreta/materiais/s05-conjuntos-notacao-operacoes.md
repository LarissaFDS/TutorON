---
id: discreta-conjuntos-operacoes
titulo: Aula 02 — conjuntos: notação, pertinência, subconjunto, potência e operações
assunto: discreta-03-conjuntos
tipo: material_estudo
fonte: Slides do Prof. Lucas Amorim (UFAL), Aula 02 — Teoria dos conjuntos (adaptação de materiais dos Profs. Pablo Sampaio, Diego Matos e Rafael Mello); notas do Prof. Pablo Sampaio (UFRPE), Teoria dos Conjuntos
fontes_catalogo: ufal-discreta-slides-lucas,ufrpe-discreta-pablo
autoria: Prof. Lucas Amorim (IC/UFAL) e Prof. Pablo Sampaio (UFRPE), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Conjunto é uma coleção **não ordenada** de objetos **distintos**: {3, 2, 1} = {1, 2, 3} e {1, 1, 3, 2, 2} = {1, 2, 3}. $x \in A$: x pertence a A; $x \notin A$ é o mesmo que $\neg(x \in A)$.

Representações: por extensão ({água, terra, fogo, ar}); por padrão ({2, 4, 6, …}); por diagrama de Venn (universo U como retângulo); por compreensão, de dois tipos:
- $\{x \in U \mid P(x)\}$: os elementos de U que satisfazem P. Ex.: $\{x \in \mathbb{Z} \mid x \text{ é par e } 0 < x < 10\} = \{2, 4, 6, 8\}$.
- $\{f(x) \mid x \in U \text{ e } P(x)\}$: aplica f a cada x que satisfaz P. Ex.: $\{k^2 \mid k \in \mathbb{Z},\ -5 < k < 5\} = \{0, 1, 4, 9, 16\}$.

Na notação da aula, $\mathbb{N} = \{0, 1, 2, \dots\}$ (com o zero).

**Pertinência × inclusão**: $\in$ relaciona elemento e conjunto; $\subseteq$ relaciona dois conjuntos. $A \subseteq B$ se todo elemento de A está em B; $A \subset B$ (subconjunto próprio) se $A \subseteq B$ e $A \neq B$. Ex.: $4 \in \{2, 3, 4\}$, mas $\{4\} \notin \{2, 3, 4\}$; já $\{4\} \in \{2, 3, \{4\}\}$.

**Conjunto potência** $\mathcal{P}(A)$: todos os subconjuntos de A; se |A| = n, então $|\mathcal{P}(A)| = 2^n$. Ex.: $\mathcal{P}(\{0, 3, 6\})$ tem 8 elementos: ∅, {0}, {3}, {6}, {0,3}, {0,6}, {3,6}, {0,3,6}.

Operações: união $A \cup B$; interseção $A \cap B$; diferença $A - B$ (está em A e não em B); complemento $A^C = U - A$. **Cardinalidade** |A|: número de elementos distintos (|{a, a}| = 1, |∅| = 0). **Produto cartesiano** $A \times B$: pares ordenados (a, b); em geral $A \times B \neq B \times A$, e $|A \times B| = |A| \cdot |B|$.

Divergência com o slide: o slide de propriedades do subconjunto diz "∅ ⊂ A para qualquer A" com o símbolo de subconjunto **próprio**. O correto é $\emptyset \subseteq A$ para todo A; $\emptyset \subset A$ só vale se A ≠ ∅. O slide do tipo 2 também escreve "1 < k < 4" onde a definição era $1 \le k \le 4$. Correções da equipe TutorON; não é gabarito do professor. Status da resolução: corrigida.

**Verificação:** potência de {0, 3, 6} e os exemplos por compreensão conferidos por código.
