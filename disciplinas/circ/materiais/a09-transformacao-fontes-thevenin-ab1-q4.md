---
id: circ-anot-transformacao-fontes-ab1-q4
titulo: Transformação de fontes (corrente em paralelo ↔ tensão em série) para achar o equivalente de Thévenin (lista AB1, questão 4)
assunto: circ-03-superposicao-transformacao
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Lista para AB1" (1 maio 2026), lista do Prof. Jobson de Araújo Nascimento, págs. 5–6
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

**Transformação de fontes:** uma fonte de corrente $I$ em paralelo com $R$ equivale a uma fonte de tensão $V = R I$ em série com o mesmo $R$, e vice-versa. O + da fonte de tensão fica do lado para onde a seta da fonte de corrente aponta. Vale também para fonte dependente, desde que a variável de controle não fique dentro do trecho transformado.

**Circuito (descrito):** fonte de 1 A (para cima) em paralelo com 6 Ω; em seguida, fonte de 14 V (− à esquerda, + à direita) e 14 Ω até o terminal a; entre a e b, fonte de 3 A (para baixo) em paralelo com 5 Ω.

**Montagem:** 1 A ∥ 6 Ω → 6 V (+ em cima) em série com 6 Ω. 3 A ∥ 5 Ω → 15 V em série com 5 Ω, com o + embaixo (a seta aponta para b). Uma malha só, horária:
$$-6 + 6i - 14 + 14i - 15 + 5i = 0 \Rightarrow i = \tfrac{35}{25} = 1{,}4\text{ A}.$$
$$V_{ab} = -15 + 5i = -8\text{ V} = V_{Th}.$$
$R_{Th}$: fontes desligadas, $(6 + 14) \parallel 5 = 4$ Ω.

**Resultado:** equivalente de Thévenin: fonte de 8 V com o + voltado para b, em série com 4 Ω.

**Verificação:** pelo outro caminho, $V_{ab} = 20 - 20i = -8$ V. Análise nodal no circuito original (sem transformação) dá $V_{Th} = -8$ V e $R_{Th} = 4$ Ω (SymPy).
