---
id: pcom-lista1-produto-cossenos
titulo: Lista 1: espectro de m(t) = cos(3000t)cos(5000t) e de m(t)cos(12000t), em rad/s; propriedade m(t)cos(ωc t) ↔ ½[M(ω + ωc) + M(ω − ωc)]
assunto: pcom-05-filtros-esquemas
tipo: lista
resolucao: sim
fonte: Anotações "Lista 1 pcom" (26 ago. 2026), p. 1
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

**Enunciado (parafraseado):** dado $m(t) = \cos(3000t)\cos(5000t)$ ($\omega$ em rad/s), esboçar o espectro de $m(t)$ e o de $m(t)\cos(12000t)$.

Pares usados: $\cos(\omega_0 t) \leftrightarrow \pi[\delta(\omega - \omega_0) + \delta(\omega + \omega_0)]$ e $m(t)\cos(\omega_c t) \leftrightarrow \frac{1}{2}[M(\omega + \omega_c) + M(\omega - \omega_c)]$.

**Mensagem:** $m(t) = \frac{1}{2}[\cos(2000t) + \cos(8000t)]$, então
$$M(\omega) = \frac{\pi}{2}[\delta(\omega \mp 2000) + \delta(\omega \mp 8000)]$$ (impulsos de área $\pi/2$ em $\pm 2000$ e $\pm 8000$ rad/s, isto é, cerca de 318 Hz e 1273 Hz).

**Modulado:** $m(t)\cos(12000t) = \frac{1}{4}[\cos 4000t + \cos 10000t + \cos 14000t + \cos 20000t]$, com impulsos de área $\pi/4$ em $\pm 4000$, $\pm 10000$, $\pm 14000$ e $\pm 20000$ rad/s. A banda inferior (4000 e 10000) é o espectro da mensagem espelhado abaixo de 12000; a superior (14000 e 20000), deslocado para cima.

Correção (complemento): a anotação só monta os pares e não resolve; a resolução é da equipe.

**Verificação:** a FFT do sinal amostrado mostra linhas de amplitude 1/4 exatamente em 4000, 10000, 14000 e 20000 rad/s, e a expansão foi conferida ponto a ponto.
