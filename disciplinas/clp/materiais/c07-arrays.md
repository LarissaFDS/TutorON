---
id: clp-arrays-armazenamento-por-linha-por-coluna-calculo-de-endereco
titulo: Arrays multidimensionais: armazenamento por linha (row major) e por coluna (column major), linguagens que usam cada um e cálculo do endereço de A[j, k] por coluna
assunto: clp-04-arrays-e-registros
tipo: prova
questao: AB1 2013.1 Q9-Q10; final 2012.2 Q7
resolucao: sim
fonte: Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (IC-UFAL)
curso: Ciência da Computação (UFAL), Conceitos de Linguagens de Programação (CCOM027); provas de 2011.2 a 2013.1
fontes_catalogo: ufal-alcino-provas-clp
autoria: Questões do Prof. Alcino Dall'Igna Jr. (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB1 2013.1 Q9-Q10; final 2012.2 Q7 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Por linha (row major):** guarda primeiro todos os elementos cujo **primeiro índice** está no limite inferior, depois os do segundo valor do primeiro índice, e assim por diante: a matriz vai **linha por linha**. Usam: C, C++, Java, Python (listas e NumPy por padrão), Pascal.

**Por coluna (column major):** guarda primeiro os elementos cujo **último índice** está no limite inferior: a matriz vai **coluna por coluna**. Usam: FORTRAN, MATLAB, R, Julia.

Exemplo da final, com a matriz
$$\begin{pmatrix} 3 & 4 & 7 \\ 6 & 2 & 5 \\ 1 & 3 & 8 \end{pmatrix}$$
- por linha: 3, 4, 7, 6, 2, 5, 1, 3, 8;
- por coluna: 3, 6, 1, 4, 2, 3, 7, 5, 8.

**Endereço de A[j, k] por coluna (AB1 Q10).** Limites: linhas de $i_1$ a $s_1$, colunas de $i_2$ a $s_2$; cada elemento ocupa $t$ bytes; $\text{base}$ é o endereço de $A[i_1, i_2]$. Cada coluna tem $n_l = s_1 - i_1 + 1$ elementos. Antes de $A[j,k]$ vêm $(k - i_2)$ colunas inteiras e mais $(j - i_1)$ elementos da coluna $k$:
$$\text{end}(A[j,k]) = \text{base} + \big[(k - i_2)(s_1 - i_1 + 1) + (j - i_1)\big]\, t$$
Em palavras: base, mais (colunas anteriores vezes elementos por coluna, mais a posição na coluna) vezes o tamanho do elemento.

Por linha, troca-se o papel dos índices: $\text{base} + [(j - i_1)(s_2 - i_2 + 1) + (k - i_2)]\,t$.

**Verificação:** `test_enderecos_por_coluna_e_por_linha` monta arrays com limites inferiores diferentes de zero, guarda por coluna e por linha numa lista plana e confere que a fórmula aponta o elemento certo em todas as posições; confere também as duas sequências da matriz da final.
