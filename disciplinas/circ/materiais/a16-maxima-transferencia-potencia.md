---
id: circ-anot-maxima-transferencia
titulo: Máxima transferência de potência: a carga RL = Rth recebe Pmáx = Vth²/(4 Rth); alto-falantes de 8 Ω e lista AB1 questão 5
assunto: circ-05-maxima-transferencia
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Máxima Transferência de Potência" (28 abr. 2026), lista 4, questão 4; Anotações manuscritas "Lista para AB1" (1 maio 2026), lista do Prof. Jobson de Araújo Nascimento, questão 5
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

**Condição:** substitua o circuito pelo equivalente de Thévenin. A potência na carga é $p = R_L\left(\dfrac{V_{Th}}{R_{Th} + R_L}\right)^2$, máxima quando a derivada em $R_L$ é zero, isto é, quando
$$R_L = R_{Th}, \qquad P_{max} = \frac{V_{Th}^2}{4R_{Th}}.$$
Em palavras: a resistência da carga igual à resistência de Thévenin; a potência máxima é o quadrado da tensão de Thévenin sobre quatro vezes a resistência de Thévenin. Nessa condição a eficiência é 50%: a mesma potência é dissipada em $R_{Th}$.

**Alto-falantes (lista 4, questão 4):** amplificador com $R_i = 8$ Ω que entrega no máximo 200 W: $200 = V_{Th}^2/(4\cdot 8) \Rightarrow V_{Th} = 80$ V. Com alto-falantes de 4 Ω, dois em série dão 8 Ω (casamento); cada um recebe 100 W.

**Lista AB1, questão 5 (descrita):** 18 V; 6 Ω até o nó m; 3 Ω de m ao terra ($v_0$); 2 Ω de m até a, com uma fonte dependente $0{,}25v_0$ em paralelo, seta de a para m. Em aberto: $v_0 = 18\cdot 3/9 = 6$ V; a corrente da dependente (1,5 A) volta pelo 2 Ω de m para a: $V_{Th} = 6 - 2\cdot1{,}5 = 3$ V. Fonte de teste $I_T$ em a: $v_0 = 2I_T$ (6 ∥ 3 = 2 Ω) e $V_T = 2I_T + 2(I_T - 0{,}25 v_0) = 3I_T$, então $R_{Th} = 3$ Ω e
$$P_{max} = \frac{3^2}{4\cdot 3} = 0{,}75\text{ W}.$$

**Verificação:** com $R_L = 3$ Ω, $i = 3/6 = 0{,}5$ A e $p = 3\cdot0{,}25 = 0{,}75$ W; com 2 Ω ou 4 Ω, 0,72 W e 0,73 W, menores. Conferido no SymPy.
