---
id: pcom-lista2-fm-kf-bessel
titulo: Lista 2: FM com kf = 2π e m(t) = 2cos(2π·100t), β = 0,02; espectro de FM por funções de Bessel Jn(β) para β = 0,5 (amplitudes das raias)
assunto: pcom-04-modulacao-angular
tipo: lista
resolucao: sim
fonte: Anotações "Lista 2s" (19 ago. 2026), p. 1–2 (questão 1)
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

**Enunciado (parafraseado):** portadora de amplitude $A = 10$ V e $f_c = 1$ kHz; mensagem $m(t) = 2\cos(2\pi\cdot 100t)$; $k_f = 2\pi$ rad/s/V.

**Sinal FM:** $\phi_{FM}(t) = 10\cos\left[2\pi\cdot 10^3 t + 2\pi\int 2\cos(2\pi\cdot 100\tau)\,d\tau\right]$ e, com $\int\cos(au)\,du = \frac{\sin(au)}{a}$:
$$\phi_{FM}(t) = 10\cos[2\pi\cdot 10^3 t + 0{,}02\sin(2\pi\cdot 100t)].$$ $\Delta\omega = 4\pi$ rad/s, $\Delta f = 2$ Hz, $\beta = 2/100 = 0{,}02$ (banda estreita).

**Espectro por Bessel:** $\phi_{FM} = A\sum_n J_n(\beta)\cos[(\omega_c + n\omega_m)t]$, raias em $f_c + nf_m$ com amplitude $A|J_n(\beta)|$ e $J_{-n} = (-1)^nJ_n$. Para $\beta = 0{,}5$ e $A = 10$:

| $n$ | frequências | amplitude |
|---|---|---|
| 0 | 1 kHz | 9,385 V |
| $\pm 1$ | 1,1 e 0,9 kHz | 2,423 V |
| $\pm 2$ | 1,2 e 0,8 kHz | 0,306 V |
| $\pm 3$ | 1,3 e 0,7 kHz | 0,026 V |
| $\pm 4$ | 1,4 e 0,6 kHz | 0,0016 V |

Correções: a anotação omite o $t$ no termo da portadora ($2\pi\cdot 10^3$ em vez de $2\pi\cdot 10^3t$) e arredonda $n = 3$ para 0,02 V e $n = 4$ para 0,001 V.

**Verificação:** `scipy.special.jv` dá $J_0(0{,}5) = 0{,}9385$, $J_1 = 0{,}2423$, $J_2 = 0{,}0306$, $J_3 = 0{,}00256$, $J_4 = 0{,}00016$; a FFT do sinal FM simulado confere as raias.
