---
id: eletronica-anot-projeto-rb-rc
titulo: Projeto de polarização fixa (exercício 41): achar RB e RC para VCC = 12 V, β = 80, ICQ = 2,5 mA e VCEQ = 6 V; RB ≈ 361,6 kΩ e RC = 2,4 kΩ
assunto: eletronica-07-tbj-polarizacao
tipo: resolucao
resolucao: sim
fonte: Anotações "Exercício parte 2" (22 out. 2026), p. 8–9 (exercício de livro, parafraseado)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Eletrônica 2026.2, IC/UFAL; docente indicado no cabeçalho: Prof. João Raphael Souza Martins); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de slides parafraseados; fotos de quadro, de slides e figuras de livro não foram copiadas
fontes_catalogo: ufal-eletronica-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Pedido:** polarização fixa com $V_{CC} = 12$ V, $\beta = 80$, ponto Q com $I_{CQ} = 2{,}5$ mA e $V_{CEQ} = 6$ V; achar $R_B$ e $R_C$.

- Corrente de base: $I_B = I_C/\beta = 2{,}5\ \mathrm{mA}/80 = 31{,}25\ \mu$A.
- Malha da base: $R_B = \frac{V_{CC} - V_{BE}}{I_B} = \frac{11{,}3}{31{,}25\ \mu\mathrm{A}} = 361{,}6$ kΩ (a anotação arredondou $I_B$ para 31,2 μA e chegou a 361,4 kΩ).
- Malha do coletor: $R_C = \frac{V_{CC} - V_{CEQ}}{I_C} = \frac{6}{2{,}5\ \mathrm{mA}} = 2{,}4$ kΩ.

Na prática, escolha o valor comercial mais próximo (por exemplo, 360 kΩ e 2,4 kΩ) e recalcule o ponto Q.

**Verificação:** com $R_B = 361{,}6$ kΩ e $R_C = 2{,}4$ kΩ, a análise direta dá $I_C = 2{,}5$ mA e $V_{CE} = 6{,}0$ V; como $V_{CE} > 0{,}2$ V, a hipótese de região ativa vale.
