---
id: controle-anot-diagrama-circuito
titulo: Exemplo: circuito R1, C, L, R2 modelado por diagrama de blocos e reduzido: Vo/Vi = R2/(R1LCs² + (R1R2C + L)s + R1 + R2)
assunto: controle-03-diagramas-blocos
tipo: resolucao
resolucao: sim
fonte: Anotações "Diagrama de Blocos" (1º out. 2026), p. 4–7
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Circuito (texto):** $V_i$ – $R_1$ – nó $v_C$; capacitor $C$ do nó ao terra; indutor $L$ do nó até a saída; $R_2$ da saída ao terra ($v_o$ sobre $R_2$).

**Blocos:** $I_1 = \frac{1}{R_1}(V_i - V_C)$; $I_C = I_1 - I_2$; $V_C = \frac{1}{Cs}I_C$; $I_2 = \frac{1}{Ls}(V_C - V_o)$; $V_o = R_2I_2$. São três malhas de realimentação negativa.

**Redução:** a malha interna $\frac{R_2/(Ls)}{1 + R_2/(Ls)} = \frac{R_2}{Ls + R_2}$ dá $V_o/V_C$; a malha do capacitor e a de $R_1$ fecham em seguida:
$$\frac{V_o(s)}{V_i(s)} = \frac{R_2}{R_1LCs^2 + (R_1R_2C + L)s + R_1 + R_2}.$$

**Verificação:** `sympy.solve` das cinco equações dá o mesmo resultado; em CC ($s = 0$, $L$ curto, $C$ aberto) é o divisor $R_2/(R_1 + R_2)$.
