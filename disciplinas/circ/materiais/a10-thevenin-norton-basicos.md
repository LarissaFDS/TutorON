---
id: circ-anot-thevenin-norton-basicos
titulo: Equivalente de Thévenin e de Norton sem fonte dependente: tensão em aberto, resistência com as fontes desligadas, In = Vth/Rth
assunto: circ-04-thevenin-norton
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Teorema de Thévenin e Norton" (28 abr. 2026), exercícios 1, 7 e 9
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

**Método:** (1) tire a carga e calcule a tensão em aberto $V_{Th} = v_{ab}$; (2) desligue as fontes **independentes** (tensão → curto, corrente → aberto) e calcule a resistência vista de a–b, $R_{Th}$; (3) Norton: $I_N = V_{Th}/R_{Th}$ em paralelo com $R_N = R_{Th}$, com a seta de $I_N$ apontando para o terminal +.

**Ex. 1:** 10 V em série com 1 kΩ até o nó x; fonte de 2 mA do terra para x; 4 kΩ de x até a; b no terra. Em aberto, o 4 kΩ não conduz: $\dfrac{v_x - 10}{1000} - 0{,}002 = 0 \Rightarrow V_{Th} = 12$ V. Desligando as fontes, $R_{Th} = 1 + 4 = 5$ kΩ.

**Ex. 7:** 12 V; 12 Ω até o nó m; 6 Ω de m ao terra; 2 Ω de m até a; fonte de 8 A do nó da fonte de 12 V até a (por cima, em paralelo com 12 Ω + 2 Ω). Em aberto, os 8 A voltam por 2 Ω: $v_m = 36$ V e $V_{Th} = 36 + 2\cdot8 = 52$ V. $R_{Th} = 12\parallel 6 + 2 = 6$ Ω. Norton: $I_N = 52/6 = \tfrac{26}{3}$ A.

**Ex. 9 (depois de transformar as fontes):** nó a ligado por 15 kΩ a um nó fixo em 30 V e por 30 kΩ a um nó fixo em −300 V: $V_{Th} = 30 + (-300-30)\tfrac{15}{45} = -80$ V; $R_{Th} = 15\parallel30 = 10$ kΩ; $I_N = -8$ mA, isto é, 8 mA com a seta para b.

Nas anotações, o passo 2 é chamado de "superposição"; é só desligar as fontes independentes.

**Verificação:** os três equivalentes foram refeitos por análise nodal com fonte de teste no SymPy (12 V e 5 kΩ; 52 V e 6 Ω; −80 V e 10 kΩ).
