---
id: pcom-anot-portadora-fase-instantanea
titulo: Portadora, mensagem e sinal modulado; Hz e rad/s; fase instantânea θ(t) e frequência instantânea ωi = dθ/dt
assunto: pcom-01-sinais-espectro
tipo: material_estudo
resolucao: sim
fonte: Anotações "conceitos iniciais" (22 ago. 2026), p. 1
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Princípios de Comunicação 2026.2; docente Jobson de Araújo Nascimento, conforme os cabeçalhos das simulações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de listas e de provas parafraseados; fotos de slide, capturas de tela e figuras coladas não foram copiadas
fontes_catalogo: ufal-pcom-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Portadora:** onda senoidal de alta frequência que transporta a informação, $c(t) = A_c\cos(2\pi f_c t + \phi_c)$ ($A_c$ amplitude da portadora, $f_c$ frequência da portadora em Hz, $\phi_c$ fase inicial). **Mensagem** ou sinal modulante, em banda básica: $m(t)$. **Sinal modulado:** $s(t)$.

Modular é adequar o sinal ao canal: uma característica da portadora varia de acordo com a mensagem. No AM a informação vai na **envoltória** (amplitude); no PM e no FM vai no **ângulo** da portadora.

**Unidades:** $T = 1/f$ e $\omega = 2\pi f$; $f$ em hertz (Hz), $\omega$ em radianos por segundo (rad/s). De rad/s para Hz divide-se por $2\pi$: $6000\pi$ rad/s são 3 kHz. Diga sempre a unidade; trocar uma pela outra é o erro mais comum das listas.

**Fase instantânea** $\theta(t)$: o argumento inteiro do cosseno. **Frequência angular instantânea:**
$$\omega_i(t) = \frac{d\theta(t)}{dt}$$ (ômega i é a derivada da fase), em rad/s; em Hz, $f_i = \frac{1}{2\pi}\frac{d\theta}{dt}$. Essa distinção é o que separa PM (mexe na fase) de FM (mexe na frequência instantânea).

**Verificação:** em $\cos(6000\pi t)$, $\theta = 6000\pi t$, $\omega_i = 6000\pi$ rad/s e $f_i = 3000$ Hz, conferido por derivação numérica da fase.
