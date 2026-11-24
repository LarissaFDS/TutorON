---
id: alglin-lista2-base-dimensao
titulo: Lista 2 — base de um espaço de funções, base de um subespaço de R4 e dimensões de soma e interseção de subespaços
assunto: alglin-02-base-dimensao-posto
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
Álgebra Linear, Lista 2 (base e dimensão). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Base = gera e é LI.** Se já se sabe a dimensão $n$, basta mostrar $n$ vetores LI.

**1. Funções.** $V = [1, t, \cos 2t, e^{3t}]$ tem dimensão 4. Nas coordenadas dessa base: $f_1 = 2t - 1 \to (-1, 2, 0, 0)$, $f_2 = t + \cos 2t \to (0, 1, 1, 0)$, $f_3 = 3 - e^{3t} \to (3, 0, 0, -1)$, $f_4 = -t + e^{3t} \to (0, -1, 0, 1)$. O determinante da matriz é $5 \ne 0$: são LI, logo base.

**2. $W = \{x_1 + x_2 + x_3 + x_4 = 0\}$** tem dimensão 3 (uma equação em $\mathbb R^4$). Os vetores $(2, 0, 0, -2)$, $(2, 0, -2, 0)$, $(8, -2, -4, -2)$ estão em $W$ (a soma das coordenadas é 0) e têm posto 3: base. (No PDF os sinais de menos sumiram na extração; com eles, as somas dão 0.)

**3. $\dim(S_1 + S_2)$** com $S_1: x_1 - 2x_2 + 3x_3 = 0$ e $S_2: x_1 - x_2 + x_3 = 0$: dois planos distintos, a interseção é a reta de direção $(1, 2, 1)$. $\dim(S_1 + S_2) = 2 + 2 - 1 = 3$, ou seja, $S_1 + S_2 = \mathbb R^3$.

**4. Em $\mathbb R^4$**, $V: x - y + z - t = 0$ e $U: 2x + y + 2z + t = 0$ (dimensão 3 cada). As duas equações são independentes, então $\dim(U \cap V) = 4 - 2 = 2$ e $\dim(U + V) = 3 + 3 - 2 = 4$; o quociente $(U + V)/(U \cap V)$ tem dimensão $4 - 2 = 2$.

**Verificação:** determinante, postos e dimensões conferidos com SymPy em `test_lista2_base_dimensao`.
