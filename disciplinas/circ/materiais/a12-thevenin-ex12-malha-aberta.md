---
id: circ-anot-thevenin-ex12
titulo: Thévenin com fonte de corrente e fonte de tensão: LKT na malha aberta (corrente zero) e Norton (exercício 12)
assunto: circ-04-thevenin-norton
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Teorema de Thévenin e Norton" (28 abr. 2026), exercício 12
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

**Circuito (descrito):** fonte de 2 A (para cima) e 2 Ω até o nó x; de x, dois resistores de 1 Ω em série até o terra, com uma fonte de 5 V em paralelo com o de cima (+ em x); de x, 1 Ω até o terminal A; do terra, 1 Ω até o terminal B.

**Tensão em aberto:** os 2 A descem pelo ramo de x: a fonte de 5 V fixa a tensão do 1 Ω de cima, então o 1 Ω de baixo leva os 2 A ($v = 2$ V). Na malha que passa por A e B não circula corrente ("malha aberta", $i = 0$), e os resistores de 1 Ω dos terminais não têm queda:
$$V_{AB} = 5 + 1\cdot 2 = 7\text{ V}.$$

**Resistência:** desligando as fontes (5 V em curto, 2 A aberta), o 1 Ω de cima some; sobram 1 Ω (A) + 1 Ω (de baixo) + 1 Ω (B) em série: $R_{Th} = 3$ Ω. Norton: $I_N = 7/3 \approx 2{,}33$ A.

**Verificação:** análise nodal com fonte de teste no SymPy: $V_{Th} = 7$ V, $R_{Th} = 3$ Ω.
