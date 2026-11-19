---
id: circ-anot-thevenin-dependentes-ex6-ex11
titulo: Thévenin com fonte de tensão dependente 160iΔ (exercício 6) e com 3vx que se anula em aberto (exercício 11)
assunto: circ-04-thevenin-norton
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Teorema de Thévenin e Norton" (28 abr. 2026), exercícios 6 e 11
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

**Exercício 6 (descrito):** fonte de 4 A em paralelo com 60 Ω; 20 Ω; fonte de tensão dependente $160 i_\Delta$ (+ à esquerda) até o nó a; de a ao terra, 80 Ω e 40 Ω, com $i_\Delta$ no 40 Ω. Transformando 4 A ∥ 60 Ω em 240 V com 60 Ω, a resistência em série fica 80 Ω.

Em aberto: $i_\Delta = v_a/40$ e a corrente no ramo série é $i = v_a/80 + v_a/40$; LKT:
$$240 - 80i - 160 i_\Delta = v_a \Rightarrow V_{Th} = 30\text{ V}\quad (i_\Delta = 0{,}75\text{ A}).$$
As anotações deixam $R_{Th}$ "na própria lista"; com fonte de teste (equipe): $R_{Th} = 10$ Ω.

**Exercício 11 (descrito):** 4 V; 5 Ω até o nó n; 15 Ω de n ao terra; 5 Ω de n até a; fonte dependente $3v_x$ de n para a; b ligado ao terra por 6 Ω, com $v_x$ nesse 6 Ω. Em aberto, o 6 Ω não conduz: $v_x = 0$, então $3v_x = 0$ e o 5 Ω de saída também não conduz:
$$V_{ab} = 4\cdot\frac{15}{20} = 3\text{ V}.$$
A dependente não foi "desligada": ela vale zero porque a variável de controle é zero. Isso só vale em aberto; para $R_{Th}$ ela volta a atuar e é preciso fonte de teste (as anotações não fizeram essa parte).

**Verificação:** SymPy: exercício 6, $V_{Th} = 30$ V e $R_{Th} = 10$ Ω (fonte de teste); exercício 11, $V_{ab} = 3$ V.
