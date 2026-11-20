---
id: pcom-anot-am-simulacao-k-m
titulo: Simulação AM: s(t) = [M + K m(t)]cos(ωc t), A = M e μ = K/M; casos μ = 1/2, μ = 2 (sobremodulação) e μ = 1; máximos e mínimos da envoltória
assunto: pcom-02-am-dsb
tipo: resolucao
resolucao: sim
fonte: Anotações "Simulação Modulação AM" (30 ago. 2026), p. 1–6
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

Modelo da simulação (diagrama em blocos): a mensagem $m(t)$, de amplitude 1, é multiplicada por $K$, somada a uma constante $M$ e multiplicada pela portadora:
$$s(t) = [M + K\,m(t)]\cos(\omega_c t) = M\left[1 + \frac{K}{M}m(t)\right]\cos(\omega_c t),$$ logo $A = M$ (amplitude da portadora), $B = K$ e $\mu = K/M$.

| $K$, $M$ | $\mu$ | Envoltória $M + K\cos\omega_m t$ | Situação |
|---|---|---|---|
| 1, 2 | 1/2 (50%) | de 1 a 3 | submodulação |
| 2, 1 | 2 (200%) | de $-1$ a 3 | sobremodulação: a "amplitude" fica negativa, a envoltória inverte |
| 1, 1 | 1 (100%) | de 0 a 2 | limite entre as duas |

Com $\mu = 2$, o detector de envoltória entrega $|1 + 2\cos\omega_m t|$, que não é a mensagem: só a demodulação coerente recupera $m(t)$.

**Verificação:** a envoltória simulada (transformada de Hilbert) tem máximo 3 e mínimo 1 no 1º caso, e $\mu$ pela fórmula $\frac{E_{max} - E_{min}}{E_{max} + E_{min}}$ dá 0,5; no 3º caso dá 1,0.
