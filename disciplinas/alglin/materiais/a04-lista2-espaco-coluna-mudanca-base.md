---
id: alglin-lista2-espaco-coluna-mudanca-base
titulo: Lista 2 — mesmo espaço coluna, matriz de mudança de base por rotação de 45° e mudança de base nos complexos
assunto: alglin-03-mudanca-de-base
tipo: exercicio_resolvido
resolucao: sim
fonte: Lista 2 de Álgebra Linear (Base, Dimensão, Posto, Mudança de Base, UFAL), PDF do material do 2º período de Engenharia de Computação | enunciados parafraseados
curso: Engenharia de Computação (UFAL), ECOM011 Álgebra Linear, 2º período (também no 3º período de Ciência da Computação); semestre não identificado
fontes_catalogo: ufal-alglin-listas
autoria: Enunciados da lista da disciplina; resoluções da equipe TutorON com apoio de IA, conferidas com SymPy e NumPy
licenca: Não declarada (lista da disciplina; PDF não versionado)
publicacao_transcricao: não autorizada; enunciados parafraseados
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Álgebra Linear, Lista 2 (posto e mudança de base). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**5. Mesmo espaço coluna.** $A = \begin{pmatrix}1&3&5\\1&4&3\\1&1&9\end{pmatrix}$, $B = \begin{pmatrix}1&2&3\\-2&-3&-4\\7&12&17\end{pmatrix}$. Posto de $A$ = posto de $B$ = 2 e posto de $[A \mid B]$ também é 2: as colunas de cada uma estão no espaço da outra, então $\text{col}(A) = \text{col}(B)$.

**Teorema do posto:** $\text{pos}(A) + \text{nul}(A) = $ número de colunas.

**7. Rotação de 45°.** A nova base é $e_1' = \tfrac{1}{\sqrt2}(1, 1)$ (na reta $y = x$) e $e_2' = \tfrac{1}{\sqrt2}(-1, 1)$. A matriz $P$ tem essas colunas, $P = \tfrac{1}{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$. As coordenadas novas são $P^{-1}(5, 6)^T$; como $P$ é ortogonal, $P^{-1} = P^T$: $x' = \tfrac{11}{\sqrt2}$, $y' = \tfrac{1}{\sqrt2}$.

**8. Complexos sobre $\mathbb R$.** $S = \{1, j\}$, $S' = \{1 + j, 1 + 2j\}$. As colunas de $P$ (de $S$ para $S'$) são os vetores de $S'$ escritos em $S$: $P = \begin{pmatrix}1&1\\1&2\end{pmatrix}$. A matriz de $S'$ para $S$ é a inversa: $Q = P^{-1} = \begin{pmatrix}2&-1\\-1&1\end{pmatrix}$.

Erro comum: pôr os vetores da nova base nas linhas em vez das colunas (isso dá $P^T$).

**Verificação:** postos, $P^{-1}(5, 6)^T$ e $PQ = I$ conferidos com SymPy em `test_lista2_coluna_mudanca_base`.
