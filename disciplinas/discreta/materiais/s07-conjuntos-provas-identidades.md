---
id: discreta-conjuntos-provas
titulo: Provar igualdade e inclusão de conjuntos — elemento arbitrário e leis da álgebra dos conjuntos
assunto: discreta-03-conjuntos
tipo: resolucao
resolucao: sim
questao: 4, 6d, 7a
fonte: 3ª lista e respostas do Prof. Pablo Sampaio (UFRPE); tabela de propriedades dos conjuntos; slides do Prof. Leandro Balby Marinho (UFCG), Identidades de Conjuntos; revisão do 2º estágio (UFCG), questão 3
fontes_catalogo: ufrpe-discreta-pablo,ufcg-discreta-leandro
autoria: Prof. Pablo Sampaio (UFRPE) e Prof. Leandro Balby Marinho (UFCG), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material dos professores)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
**Inclusão** $X \subseteq Y$: tome x arbitrário, suponha $x \in X$ e conclua $x \in Y$. **Igualdade** X = Y: prove $X \subseteq Y$ e $Y \subseteq X$ (ou uma cadeia de ↔). Cada passo vem de uma definição ou de uma equivalência lógica.

Exemplo 1: $(A \cap B) \subseteq A$. Seja $x \in A \cap B$. Pela definição, $x \in A \land x \in B$; por simplificação, $x \in A$. ∎ Por absurdo (lista do Prof. Pablo, 7a): suponha $x \in A \cap B$ e $x \notin A$; de $x \in A \cap B$ vem $x \in A$, contradição.

Exemplo 2 (lista, 6d): $(A \cup B)^C = A^C - B$.
$x \in (A \cup B)^C \leftrightarrow \neg(x \in A \lor x \in B) \leftrightarrow x \notin A \land x \notin B$ (De Morgan) $\leftrightarrow x \in A^C \land x \notin B \leftrightarrow x \in A^C - B$. ∎

Exemplo 3 (UFCG): $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$, pela distributiva de ∧ sobre ∨: $x \in A \land (x \in B \lor x \in C) \leftrightarrow (x \in A \land x \in B) \lor (x \in A \land x \in C)$. ∎

Leis da álgebra dos conjuntos (espelham as da lógica): identidade $A \cup \emptyset = A$, $A \cap U = A$; dominação $A \cup U = U$, $A \cap \emptyset = \emptyset$; idempotência; comutativas; associativas; distributivas; absorção $A \cap (A \cup B) = A$ e $A \cup (A \cap B) = A$; De Morgan $(A \cup B)^C = A^C \cap B^C$; involução $(A^C)^C = A$; e $A - B = A \cap B^C$.

Divergência com a resposta original: na passagem de De Morgan da resposta de 6d aparece "x ∈ A ∨ x ∈ A B" (erro de digitação: o certo é "x ∈ A ∨ x ∈ B"). Correções da equipe TutorON; não é gabarito do professor. Status da resolução: corrigida.

Para mostrar que uma igualdade é **falsa**, basta um contraexemplo com conjuntos pequenos: $A - (B - C) \neq (A - B) - C$ com A = B = C = {1}: o lado esquerdo é {1}, o direito é ∅.

**Verificação:** as identidades e o contraexemplo foram testados por código em todos os subconjuntos de um universo com 3 elementos.
