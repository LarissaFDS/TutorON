---
id: circ-anot-nodal-duas-fontes
titulo: Análise nodal só com LKC: dois nós, fontes de 120 V e 20 V, correntes, potências fornecidas e dissipadas (questão 3,5-1)
assunto: circ-02-kirchhoff-nodal-malhas
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Questões circuitos" (1 maio 2026), págs. 2–3 (enunciado de lista colado, parafraseado)
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

**Circuito (descrito):** fonte de 120 V (+ em cima) ligada por 10 Ω ao nó 1. Nó 1: 20 Ω até o ponto A e 5 Ω até o nó 2. Nó 2: 5 Ω ao terra e 17,5 Ω até o ponto A. O ponto A está a −20 V: uma fonte de 20 V com o + no terra.

**Montagem (LKC, correntes saindo):**
$$\frac{v_1+20}{20} + \frac{v_1-v_2}{5} + \frac{v_1-120}{10} = 0 \Rightarrow 7v_1 - 4v_2 = 220$$
$$\frac{v_2+20}{17{,}5} + \frac{v_2-v_1}{5} + \frac{v_2}{5} = 0 \Rightarrow 16v_2 - 7v_1 = -40$$

**Resultado:** $v_1 = 40$ V, $v_2 = 15$ V. Correntes: 10 Ω: 8 A da fonte para o nó 1; 20 Ω: 3 A do nó 1 para A; 5 Ω (1→2): 5 A; 5 Ω (2→terra): 3 A; 17,5 Ω: 2 A do nó 2 para A. Os 5 A que chegam em A atravessam a fonte de 20 V de − para +.

Potências: 120 V fornece 960 W; 20 V fornece $20\cdot5 = 100$ W. Resistores: 640 + 180 + 125 + 45 + 70 = 1060 W.

**Verificação:** fornecido 1060 W = absorvido 1060 W; LKC em A: 3 + 2 = 5 A. Conferido no SymPy.
