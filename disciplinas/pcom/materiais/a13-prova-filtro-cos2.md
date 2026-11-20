---
id: pcom-prova-filtro-cos2-8000t
titulo: Prova: m(t)cos(2000t) multiplicado por 2cos²(8000t); espectros em A e B (rad/s), filtro passa-baixas com corte entre 3000 e 13000 rad/s e demodulação por 2cos(2000t)
assunto: pcom-05-filtros-esquemas
tipo: prova
resolucao: sim
fonte: Anotações "fórmulas fundamentais para a prova 1" (7 set. 2026), p. 5–6 (questão 1 de prova, enunciado parafraseado)
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

**Enunciado (parafraseado):** $m(t)\cos(2000t)$ (ponto A) é multiplicado por $2\cos^2(8000t)$ (ponto B) e filtrado; um bloco a definir recupera $m(t)$. $M(\omega)$ é um triângulo de altura 1 em $|\omega| \le 1000$ rad/s.

**Em A:** $\frac{1}{2}[M(\omega - 2000) + M(\omega + 2000)]$: triângulos de altura 1/2 entre 1000 e 3000 rad/s (e simétricos).

**Em B:** $2\cos^2(8000t) = 1 + \cos(16000t)$, então
$$m\cos 2000t + \frac{m}{2}\cos 18000t + \frac{m}{2}\cos 14000t,$$ com espectro $\frac{1}{2}M(\omega \mp 2000)$ (1000 a 3000), $\frac{1}{4}M(\omega \mp 14000)$ (13000 a 15000) e $\frac{1}{4}M(\omega \mp 18000)$ (17000 a 19000 rad/s): alturas 1/2, 1/4 e 1/4.

**Filtro:** passa-baixas que deixe o primeiro par e corte os outros: corte entre 3000 e 13000 rad/s. As anotações dizem "6000 rad/s", que é a largura de $-3000$ a $+3000$, ou seja, corte em 3000 rad/s (cerca de 477 Hz).

**Bloco final:** multiplicar por $2\cos(2000t)$, que dá $m(t)[1 + \cos 4000t]$, e filtrar com corte entre 1000 e 3000 rad/s.

Correção: os rótulos do eixo no esboço de B (15, 16, 17) não batem com as faixas 13 a 15 e 17 a 19 mil rad/s, e o "6000 rad/s" precisava dizer que é bilateral.

**Verificação:** o espectro de B simulado (FFT, $m$ triangular) mostra picos 1/2, 1/4 e 1/4 nas faixas acima; a saída final recupera $m(t)$ com erro menor que 2%.
