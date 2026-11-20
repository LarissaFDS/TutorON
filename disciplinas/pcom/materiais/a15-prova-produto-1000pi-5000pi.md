---
id: pcom-prova-x-cos1000pi-cos5000pi
titulo: Prova: x(t) = 2cos(1000πt) vezes cos(5000πt) dá impulsos de 1/2 em ±2 kHz e ±3 kHz; filtro H e mistura com 4cos(5000πt) para recuperar x(t)
assunto: pcom-05-filtros-esquemas
tipo: prova
resolucao: sim
fonte: Anotações "Revisão Final prova 1" (9 set. 2026), p. 2–4 (questão 2 de prova, enunciado parafraseado)
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

**Enunciado (parafraseado):** $x(t) = 2\cos(1000\pi t)$ é multiplicado por $\cos(5000\pi t)$ e passa por um filtro $H(\omega)$. Pede-se o espectro antes do filtro, a largura de $H$ e os blocos depois do filtro para ter $y(t) = x(t)$.

**Antes do filtro:** $s(t) = 2\cos(1000\pi t)\cos(5000\pi t) = \cos(2\pi\,3000t) + \cos(2\pi\,2000t)$, e
$$S(f) = \frac{1}{2}[\delta(f - 3000) + \delta(f + 3000)] + \frac{1}{2}[\delta(f - 2000) + \delta(f + 2000)],$$ quatro impulsos de peso 1/2 em $\pm 2$ e $\pm 3$ kHz.

**Filtro:** não é preciso passar as duas bandas (6 kHz bilateral): basta uma. As anotações ficam com a de 2 kHz, com passa-baixas de corte entre 2 e 3 kHz ("4 kHz de largura", de $-2$ a $+2$ kHz). Sobra $\cos(4000\pi t)$.

**Depois do filtro:** um filtro sozinho não muda a frequência; é preciso misturar de novo: $4\cos(4000\pi t)\cos(5000\pi t) = 2\cos(1000\pi t) + 2\cos(9000\pi t)$, e um passa-baixas com corte entre 500 Hz e 4,5 kHz deixa $2\cos(1000\pi t) = x(t)$ (as anotações usam $2000\pi$ rad/s, isto é, $\pm 500$ Hz).

**Verificação:** FFT do produto: quatro picos de 0,5 em $\pm 2$ e $\pm 3$ kHz; a cadeia simulada (filtro, mistura, filtro) devolve $x(t)$ com erro menor que 1%.
