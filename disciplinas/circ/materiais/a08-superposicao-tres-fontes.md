---
id: circ-anot-superposicao-tres-fontes
titulo: Princípio da superposição com três fontes independentes (20 V, 1 A e 2 A): contribuição de cada uma para v₀
assunto: circ-03-superposicao-transformacao
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Questões circuitos" (1 maio 2026), pág. 6 (exercício de livro-texto, enunciado parafraseado)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Circuitos Elétricos 2026.1, Prof. Jobson de Araújo Nascimento, IC/UFAL); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-circ-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Circuito (descrito):** fonte de 20 V (+ em cima) no nó L. De L: 4 Ω até o nó 1 e 6 Ω até o nó 2 (por cima). Nó 1: 2 Ω até o nó 2 e fonte de 1 A do terra para o nó 1. Nó 2: 3 Ω ao terra, com $v_0$ (+ em cima). Fonte de 2 A entre os nós 2 e L, com a seta para L. Pede-se $v_0$ pela superposição.

**Uma fonte por vez** (fonte de tensão desligada = curto; fonte de corrente desligada = aberto):
1. Só 20 V: o ramo 4 + 2 = 6 Ω fica em paralelo com o de 6 Ω (3 Ω), em série com 3 Ω: $v_0' = 20\cdot\tfrac{3}{3+3} = 10$ V.
2. Só 2 A (saindo do nó 2): $v_0'' = -3$ V.
3. Só 1 A: LKC nos nós 1 e 2 com L aterrado dá $3v_1 - 2v_0 = 4$ e $6v_0 - 3v_1 = 0$, então $v_0^{(3)} = 1$ V.

$$v_0 = v_0' + v_0'' + v_0^{(3)} = 10 - 3 + 1 = 8\text{ V}.$$

A superposição vale para tensões e correntes (circuito linear), **não** para potências: a potência é quadrática.

**Verificação:** análise nodal direta com as três fontes: $v_1 = \tfrac{40}{3}$ V, $v_0 = 8$ V; soma das potências zero. Conferido no SymPy.
