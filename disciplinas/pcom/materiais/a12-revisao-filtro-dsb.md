---
id: pcom-revisao-filtro-dsb-18000pi
titulo: Largura de banda do filtro para recuperar m(t) num esquema DSB: 2 m(t)cos(18000πt), mensagem de 2 kHz, filtro passa-baixas com corte entre W e 2fc − W
assunto: pcom-05-filtros-esquemas
tipo: resolucao
resolucao: sim
fonte: Anotações "Revisão prova 1" (30 ago. 2026), p. 1–2 (questão 1)
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

**Esquema:** $s(t) = 2m(t)\cos(18000\pi t)$ ($f_c = 9$ kHz), com $S(\omega) = M(\omega - 18000\pi) + M(\omega + 18000\pi)$.

**Largura da mensagem:** o espectro modulado vai até $22000\pi$ rad/s. A borda é $18000\pi + 2\pi B = 22000\pi$, logo $2\pi B = 4000\pi$ e $B = 2000$ Hz: a mensagem ocupa até 2 kHz ($4000\pi$ rad/s). Um filtro que deixa passar o sinal modulado inteiro precisa ir até 11 kHz ($22000\pi$ rad/s); contando de $-11$ a $+11$ kHz, as anotações escrevem 22 kHz.

**Demodulação:** multiplica-se por $\cos(18000\pi t)$:
$$2m(t)\cos^2(18000\pi t) = m(t) + m(t)\cos(36000\pi t).$$ A segunda parcela ocupa de 16 a 20 kHz. O **filtro passa-baixas** deve deixar passar $m(t)$ (até $W = 2$ kHz) e rejeitar a cópia em $2f_c$ (a partir de $2f_c - W = 16$ kHz):
$$W \le f_{corte} \le 2f_c - W.$$ As anotações escolhem o corte em 2 kHz ($4000\pi$ rad/s; $\pm 2$ kHz, ou 4 kHz contando as frequências negativas). No espectro: passa o triângulo centrado em 0; são rejeitados os triângulos em $\pm 18$ kHz.

**Verificação:** com $m(t) = \cos(2\pi\,2000t)$, o produto simulado e filtrado (Butterworth, corte 5 kHz) devolve $m(t)$ com erro menor que 1%.
