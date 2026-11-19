---
id: circ-anot-thevenin-fonte-dependente
titulo: Equivalente de Thévenin com fonte dependente: a dependente não é desligada; resistência de Thévenin com fonte de teste, Rth = VT/IT (exercício 5)
assunto: circ-04-thevenin-norton
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Teorema de Thévenin e Norton" (28 abr. 2026), exercício 5
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

**Como calcular o equivalente de Thévenin (ou de Norton) quando o circuito tem fonte dependente, também chamada fonte controlada.**

**Regra:** com fonte **dependente**, desligue só as independentes; a dependente continua no circuito, controlada pela sua variável. Não dá para somar resistências: aplique uma **fonte de teste** nos terminais (tensão $V_T$ ou corrente $I_T$), calcule a outra grandeza e faça
$$R_{Th} = \frac{V_T}{I_T}.$$
Se só houver fontes dependentes, $V_{Th} = 0$ e o equivalente é só $R_{Th}$ (pode até dar negativo).

**Circuito (descrito):** fonte de 24 V (+ em cima) e 2 Ω até o nó a; em paralelo com o 2 Ω, fonte dependente $3i_x$ com a seta de a para a fonte; de a ao terra, fonte de 4 A (para baixo) e 8 Ω com $i_x$ para baixo; b no terra.

**Tensão em aberto (LKC em a, $i_x = v_a/8$):**
$$\frac{v_a - 24}{2} + 3i_x + 4 + i_x = 0 \Rightarrow \frac{v_a}{2} - 12 + \frac{v_a}{2} + 4 = 0 \Rightarrow V_{Th} = 8\text{ V}\ (i_x = 1\text{ A}).$$
As anotações transformam $3i_x \parallel 2$ Ω numa fonte de tensão $6i_x$ em série com 2 Ω (o controle $i_x$ fica fora do trecho) e chegam ao mesmo valor.

**Resistência:** 24 V em curto, 4 A aberta, fonte de teste $V_T$ em a com corrente $I_T$ entrando:
$$I_T = \frac{V_T}{2} + 3\frac{V_T}{8} + \frac{V_T}{8} = V_T \Rightarrow R_{Th} = 1\ \Omega .$$

**Erro típico:** desligar a fonte $3i_x$ daria $2\parallel 8 = 1{,}6$ Ω, errado.

**Verificação:** curto em a–b: $i_x = 0$, a dependente zera e $I_{cc} = 24/2 - 4 = 8$ A; $V_{Th}/I_{cc} = 1$ Ω. Conferido no SymPy.
