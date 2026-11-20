---
id: pcom-revisao-am-espectro-impulsos
titulo: AM a partir do espectro S(f): impulsos 12 em ±1 MHz e 3 em ±0,5 e ±1,5 MHz dão A = 24, B = 12, μ = 0,5; potência de 25 W nas bandas laterais dá B = 10 V
assunto: pcom-02-am-dsb
tipo: resolucao
resolucao: sim
fonte: Anotações "Revisão Final prova 1" (9 set. 2026), p. 4–7 (questões de prova, enunciados parafraseados)
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

**Espectro dado:** $S(f)$ real, com impulsos de peso 12 em $\pm 1$ MHz e de peso 3 em $\pm 0{,}5$ e $\pm 1{,}5$ MHz. Pede-se mensagem, portadora e índice.

Com $s(t) = A\cos(2\pi f_c t) + \frac{B}{2}\cos[2\pi(f_c - f_m)t] + \frac{B}{2}\cos[2\pi(f_c + f_m)t]$:
$$S(f) = \frac{A}{2}[\delta(f - f_c) + \delta(f + f_c)] + \frac{B}{4}[\dots]$$ (impulsos $A/2$ na portadora e $B/4$ nas bandas). Então $A/2 = 12 \Rightarrow A = 24$; $B/4 = 3 \Rightarrow B = 12$; $f_c = 1$ MHz e $f_m = 0{,}5$ MHz. Mensagem $m(t) = 12\cos(2\pi\cdot 0{,}5\cdot 10^6 t)$, portadora $p(t) = 24\cos(2\pi\cdot 10^6 t)$, $\mu = 12/24 = 0{,}5$ (50%).

**Potência nas bandas (outra questão):** $f_c = 100$ kHz, $f_m = 10$ kHz, $\phi_{AM} = A[1 + \frac{B}{A}\cos(2\pi f_m t)]\cos(2\pi f_c t)$ e 25 W nas bandas laterais. Cada banda tem amplitude $B/2$: $P_{BL} = 2\cdot\frac{(B/2)^2}{2} = \frac{B^2}{4} = 25$, logo $B = 10$ V. Com $\mu = 2/5$: $A = B/\mu = 25$ V.

**Verificação:** a FFT do sinal reconstruído dá 12 em 1 MHz e 3 em 0,5 e 1,5 MHz; a potência das bandas com $B = 10$ simulada dá 25,0 W.
