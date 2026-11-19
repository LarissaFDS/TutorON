---
id: circ-anot-maxima-transferencia-y-delta
titulo: Resistência de Thévenin com transformação estrela-triângulo (Y-Δ) e três nós (lista 4, questão 5)
assunto: circ-05-maxima-transferencia
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Máxima Transferência de Potência" (28 abr. 2026), lista 4, questão 5
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

**Circuito (descrito):** terminal a: fonte de 60 V (+ em a) em série com 20 Ω até o terra; 20 Ω de a até o nó 2. Nó 2: 20 Ω e fonte de 100 V (+ em cima) até o terra. Entre o nó 2 e b: fonte de 1 A (seta para b) em paralelo com dois resistores de 40 Ω. b: 20 Ω até o terra.

**Simplificação:** $40 \parallel 40 = 20$ Ω; 1 A ∥ 20 Ω → fonte de 20 V em série com 20 Ω, com o + do lado de b.

**Tensão (três nós):** LKC em a, 2 e b dá $2v_a - v_2 = 60$ e $2v_b - v_2 = 20$; com a equação do nó 2, $V_{ab} = v_a - v_b = 20$ V.

**Resistência:** desligadas as fontes, sobram cinco resistores de 20 Ω: a–terra, a–2, 2–terra, 2–b, b–terra. Nenhum par está em série ou em paralelo. A estrela de três braços de 20 Ω que sai do nó 2 vira um triângulo:
$$R_\Delta = \frac{R_1R_2 + R_2R_3 + R_3R_1}{R_{oposto}} = \frac{3\cdot 400}{20} = 60\ \Omega .$$
Depois, $60\parallel20 = 15$ Ω de cada lado e $R_{Th} = 60 \parallel (15 + 15) = 20$ Ω.

**Resultado:** $V_{Th} = 20$ V, $R_{Th} = 20$ Ω; para máxima transferência, $R_L = 20$ Ω e $P_{max} = 20^2/(4\cdot20) = 5$ W.

**Verificação:** fonte de teste no SymPy: $V_{Th} = 20$ V, $R_{Th} = 20$ Ω.
