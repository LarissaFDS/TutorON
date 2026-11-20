---
id: pcom-prova-am-potencia-88w
titulo: Exercício de prova AM: mensagem 8 cos(2π 500 t), portadora 12 cos(2π 5000 t), φAM = [A + m(t)]cos(ωc t): A = 12, μ = 2/3, potência 88 W
assunto: pcom-02-am-dsb
tipo: prova
resolucao: sim
fonte: Anotações "fórmulas fundamentais para a prova 1" (7 set. 2026), p. 7 (questão 2 de prova, enunciado parafraseado)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Princípios de Comunicação 2026.2; docente Jobson de Araújo Nascimento, conforme os cabeçalhos das simulações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de listas e de provas parafraseados; fotos de slide, capturas de tela e figuras coladas não foram copiadas
fontes_catalogo: ufal-pcom-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Enunciado (parafraseado):** a mensagem $m(t) = 8\cos(2\pi\,500t)$ V modula uma portadora $12\cos(2\pi\,5000t)$ V no esquema $\phi_{AM}(t) = [A + m(t)]\cos(\omega_c t)$. Pede-se $A$, o índice de modulação e a potência do sinal modulado.

**Montagem:** comparando com $[A + B\cos(\omega_m t)]\cos(\omega_c t)$: $A = 12$ V (amplitude da **portadora**), $B = 8$ V (amplitude da **mensagem**), $f_m = 500$ Hz, $f_c = 5$ kHz.

**Cálculo:** $\mu = B/A = 8/12 = 2/3$. Cada banda lateral (4,5 kHz e 5,5 kHz) tem amplitude $B/2 = 4$ V. Em carga de 1 Ω:
$$P_T = \frac{12^2}{2} + \frac{4^2}{2} + \frac{4^2}{2} = 72 + 8 + 8 = 88\ \text{W}.$$

Correção: a anotação troca os rótulos ("A: amplitude da mensagem", "B: amplitude da portadora"); os valores usados estão certos.

**Verificação:** pela fórmula fechada, $\frac{A^2}{2}(1 + \mu^2/2) = 72(1 + 2/9) = 88$ W; a média de $s^2(t)$ simulada também dá 88.
