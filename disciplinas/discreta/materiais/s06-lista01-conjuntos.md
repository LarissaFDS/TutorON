---
id: discreta-lista01-conjuntos
titulo: Lista 01 (Prof. Lucas Amorim) — conjuntos: operações, extensão, pertinência e inclusão-exclusão
assunto: discreta-03-conjuntos
tipo: resolucao
resolucao: sim
questao: 1, 6, 7, 8, 9, 10
fonte: Lista de Exercícios 01 — Conjuntos, Prof. Lucas Amorim (UFAL); exercícios finais da Aula 02; respostas da 3ª lista do Prof. Pablo Sampaio (mesma questão 1)
fontes_catalogo: ufal-discreta-lista01,ufal-discreta-slides-lucas,ufrpe-discreta-pablo
autoria: Enunciados do Prof. Lucas Amorim (IC/UFAL); resolução da equipe TutorON com auxílio de IA, conferida por código
licenca: Não declarada (lista do professor)
publicacao_transcricao: não se aplica: os enunciados aparecem resumidos; a lista não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
**Q1.** A = {1, 2, 3, 4, 5}, B = {0, 3, 6}, U = {0, 1, …, 9}. $A \cap B = \{3\}$; $A \cup B = \{0, 1, 2, 3, 4, 5, 6\}$; $A - B = \{1, 2, 4, 5\}$; $B^C = \{1, 2, 4, 5, 7, 8, 9\}$; $B^C - A = \{7, 8, 9\}$. (Bate com as respostas da lista do Prof. Pablo, que também dá $|A^C| = |\{0, 6, 7, 8, 9\}| = 5$.)

**Q6.** Por extensão: $\{x \in \mathbb{Z} \mid 0 < x < 5\} = \{1, 2, 3, 4\}$; $\{x \mid x \in \mathbb{Z}^+ \land x < 12\} = \{1, \dots, 11\}$ (lendo $\mathbb{Z}^+$ como inteiros positivos; se a turma incluir o 0, acrescente-o); $\{x^2 \mid x \in \mathbb{Z},\ -10 < x < 10\} = \{0, 1, 4, 9, 16, 25, 36, 49, 64, 81\}$; $\{x + y \mid x, y \text{ ímpares},\ 0 < x < y < 10\} = \{4, 6, 8, 10, 12, 14, 16\}$; $\{x \in \mathbb{Z} \mid x^2 = 2\} = \emptyset$.

**Q7.** 400 pessoas, 30% homens: 280 mulheres. 65% delas têm mais de 20 anos, então 35% não: 0,35 · 280 = **98**.

**Q8.** 30% são de Humanas e 20% destes escolhem Direito: 0,30 · 0,20 = **6%** do total.

**Q9.** Inclusão-exclusão com 95% consumindo alguma marca: $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|$, ou seja, 95 = 48 + 45 + 50 − 18 − 25 − 15 + x = 85 + x, logo **x = 10%**.

**Q10.** (a) $0 \in \emptyset$: F. (b) $\{0\} \subset \emptyset$: F. (c) $\{0\} \in \{0\}$: F (o único elemento é 0). (d) $\{\emptyset\} \subseteq \{\emptyset\}$: V. (e) $\emptyset \in \{0\}$: F. (f) $\emptyset \subset \{0\}$: V. (g) $\{0\} \subset \{0\}$: F (não é próprio).

Exercícios da aula: se 80% leem x, 60% leem y e todos leem algum, 80 + 60 − 100 = **40%** leem os dois. Com 10 estudantes, 6 de óculos e 8 de relógio, ao menos **4** usam os dois (6 + 8 − 10). As questões 2, 3 e 13 dependem de diagramas de Venn (imagens), que não foram transcritas.

Status da resolução: validada (conferida por código pela equipe TutorON; a lista do Prof. Lucas não traz gabarito).

**Verificação:** todos os conjuntos e porcentagens acima foram recalculados por código com conjuntos do Python.
