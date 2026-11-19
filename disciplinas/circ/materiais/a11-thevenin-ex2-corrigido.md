---
id: circ-anot-thevenin-ex2
titulo: Equivalente de Thévenin com duas fontes de tensão (50 V e 54 V): resistência de Thévenin corrigida para 25 Ω
assunto: circ-04-thevenin-norton
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Teorema de Thévenin e Norton" (28 abr. 2026), exercício 2
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Circuitos Elétricos 2026.1, Prof. Jobson de Araújo Nascimento, IC/UFAL); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-circ-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Circuito (descrito):** fonte de 50 V e 50 Ω em série até o terminal 1. Entre o terminal 1 e o terminal 2 (terra), um ramo vertical: 20 Ω, fonte de 54 V (− em cima, + embaixo) e 30 Ω.

**Tensão em aberto:** uma malha só, horária: $-50 + 50i + 20i - 54 + 30i = 0 \Rightarrow i = \tfrac{104}{100} = \tfrac{26}{25}$ A. Descendo pelo ramo vertical:
$$V_{12} = 20i - 54 + 30i = 50\cdot1{,}04 - 54 = -2\text{ V} = V_{Th}.$$

**Resistência de Thévenin:** com as fontes desligadas, o 50 Ω fica em paralelo com o ramo de $20 + 30 = 50$ Ω:
$$R_{Th} = 50 \parallel 50 = 25\ \Omega .$$

**Correções:** as anotações separam o ramo vertical em 30 Ω e "15 Ω" e chegam a $R_{Th} = 40$ Ω. O 20 Ω e o 30 Ω estão em série no mesmo ramo; o certo é 25 Ω. $V_{Th} = -2$ V está certo.

**Resultado:** fonte de 2 V com o + voltado para o terminal 2, em série com 25 Ω.

**Verificação:** curto entre 1 e 2: $I_{cc} = 50/50 + (-54)/50 = -0{,}08$ A, e $V_{Th}/I_{cc} = -2/(-0{,}08) = 25$ Ω. Conferido com fonte de teste no SymPy.
