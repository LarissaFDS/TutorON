---
id: pcom-prova-filtro-17khz
titulo: Prova: m(t) vezes 4cos(16000πt) e filtro de largura 17 kHz; valor de B depende da convenção de largura de banda (bilateral dá 500 Hz, unilateral dá 9 kHz)
assunto: pcom-05-filtros-esquemas
tipo: prova
resolucao: sim
fonte: Anotações "Revisão Final prova 1" (9 set. 2026), p. 1–2 (questão 1 de prova, enunciado parafraseado)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Princípios de Comunicação 2026.2; docente Jobson de Araújo Nascimento, conforme os cabeçalhos das simulações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de listas e de provas parafraseados; fotos de slide, capturas de tela e figuras coladas não foram copiadas
fontes_catalogo: ufal-pcom-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: pendente_professor
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: pendente de confirmação do professor.

**Enunciado (parafraseado):** $m(t)$, com $M(\omega)$ triangular de altura 2 em $|\omega| \le 2\pi B$, é multiplicada por $4\cos(16000\pi t)$ ($f_c = 8$ kHz) e passa por um filtro de largura de banda 17 kHz. Pede-se $B$, o espectro em A e os blocos que recuperam $m(t)$.

**Espectro em A:** $4m(t)\cos(16000\pi t) \leftrightarrow 2[M(\omega - 16000\pi) + M(\omega + 16000\pi)]$: triângulos de altura **4** centrados em $\pm 16000\pi$ rad/s, de $16000\pi - 2\pi B$ a $16000\pi + 2\pi B$.

**Valor de $B$: depende da convenção.**
- Anotações (largura contada de $-f$ a $+f$): $(2\pi B + 16000\pi) - (-2\pi B - 16000\pi) = 34000\pi$, logo $B = 500$ Hz.
- Largura de banda como frequência de corte (só frequências positivas, a convenção usual): $8\ \text{kHz} + B = 17$ kHz, logo $B = 9$ kHz.
Nas listas da turma a largura do filtro aparece sempre bilateral ("$\pm 11$ kHz = 22 kHz"); confirme com o professor qual vale na prova.

**Recuperação:** multiplicar por $\frac{1}{2}\cos(16000\pi t)$: $2m(t)\cos^2 = m(t) + m(t)\cos(32000\pi t)$, e passa-baixas que deixe só $m(t)$ (largura 1000 Hz bilateral na convenção das anotações, corte em 500 Hz).

Correção: o esboço das anotações marca o pico do espectro em A como 2; com o fator $4\cdot\frac{1}{2} = 2$ multiplicando $M$ de altura 2, o pico é 4.

**Verificação:** as duas equações foram resolvidas (500 Hz e 9 kHz); a FFT do sinal simulado com $B = 500$ Hz mostra o pico 4 e a faixa de 7,5 a 8,5 kHz.
