---
id: pcom-revisao-am-envoltoria
titulo: AM a partir do gráfico da envoltória: máximo 3 e mínimo 1 dão A = 2, B = 1, μ = 1/2; máximo 8 com B = 2 dá A = 6, μ = 1/3 e potência 19 W
assunto: pcom-02-am-dsb
tipo: resolucao
resolucao: sim
fonte: Anotações "Revisão prova 1" (30 ago. 2026), p. 2–3 (questões 2 e 3)
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

Os gráficos dos enunciados não estão nas anotações; os valores abaixo são os lidos pelo aluno.

**Questão 2:** a envoltória vai de 1 a 3. Com $\phi_{AM} = A[1 + \frac{B}{A}\cos\omega_m t]\cos\omega_c t$: $A + B = 3$ e $A - B = 1$, logo $A = 2$, $B = 1$, $\mu = 1/2$. Períodos lidos: mensagem $T_m = 5{,}5$ ms, então $f_m = 1/5{,}5\ \text{ms} = \frac{2}{11}$ kHz $\approx 181{,}8$ Hz; portadora $T_c = 0{,}5$ ms, então $f_c = 2$ kHz. Resulta $m(t) = \cos(2\pi\cdot 181{,}8\,t)$ e portadora $2\cos(2\pi\,2000t)$.

**Questão 3:** $B = 2$ e o máximo da envoltória é 8: $A + 2 = 8$, $A = 6$, $\mu = 2/6 = 1/3$, portadora $6\cos(\omega_c t)$. Expandindo, $6\cos\omega_c t + \cos(\omega_c + \omega_m)t + \cos(\omega_c - \omega_m)t$, e
$$P = \frac{6^2}{2} + 2\cdot\frac{1^2}{2} = 18 + 1 = 19\ \text{W}.$$

Correção: a identidade escrita ao lado tem o sinal trocado ($\cos a\cos b = \frac{1}{2}[\cos(a + b) - \cos(a - b)]$); o certo é **mais**, e é o que o desenvolvimento usa.

**Verificação:** $\mu$ pela envoltória, $(3 - 1)/(3 + 1) = 0{,}5$ e $(8 - 4)/(8 + 4) = 1/3$; a potência simulada da questão 3 dá 19,0 W.
