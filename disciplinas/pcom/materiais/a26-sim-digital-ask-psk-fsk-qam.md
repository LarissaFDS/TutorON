---
id: pcom-sim-digital-ask-psk-fsk-qam
titulo: Simulação de modulação digital: ASK binário, de 2 e de 3 bits (níveis de 1 a 8 V), PSK com fases 90°, 180° e 270°, FSK de 1 e 2 Hz e 8-QAM com constelação
assunto: pcom-06-modulacao-digital
tipo: resolucao
resolucao: sim
fonte: Anotações "Simulação - Modulação Digital" (30 set. 2026), p. 1–7
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

Portadora de 1 Hz, um símbolo por segundo (salvo no FSK).
- **ASK binário**, bit 0 com 1 V e bit 1 com 2 V, sequência 101001: amplitudes 2, 1, 2, 1, 1, 2 V; $T_b = 1$ s, um ciclo por bit, 6 s, 1 bit/s.
- **ASK de 2 bits**: 00 → 1 V, 01 → 2 V, 10 → 3 V, 11 → 4 V. Sequência 10 00 11 01 00 11: 3, 1, 4, 2, 1, 4 V. $T_s = 1$ s, $k = \log_2 4 = 2$, $T_b = 0{,}5$ s, 1 baud, 2 bit/s.
- **ASK de 3 bits**: 000 a 111 → 1 a 8 V. Sequência 100 011 010 011 000 111: 5, 4, 3, 4, 1, 8 V; 3 bit/s.
- **PSK** com $\sin(2\pi t + \varphi)$, bit 1 em 0°: com 90° o trecho começa em +1 (é um cosseno); com 180°, começa em 0 e desce; com 270°, começa em −1.
- **FSK**: bit 0 com 1 Hz e bit 1 com 2 Hz, $T_b = 2$ s (2 e 4 ciclos por bit); 0,5 bit/s; 01101 dura 10 s.
- **8-QAM**: amplitudes 1 e 2 V e fases 0°, 90°, 180°, 270°, com $s(t) = A\cos(2\pi t + \varphi)$. Mapa: 000 (1 V, 0°), 001 (2 V, 0°), 010 (1 V, 90°), 011 (2 V, 90°), 100 (1 V, 180°), 101 (2 V, 180°), 110 (1 V, 270°), 111 (2 V, 270°); $k = 3$, 1 baud, 3 bit/s.

Observação: $\cos(\omega t + 90^\circ) = -\sin(\omega t)$. A constelação desenhada põe 90° no semieixo "+seno"; é uma convenção de eixo, e convém dizê-la.

**Verificação:** as formas de onda foram geradas e o valor no início de cada símbolo (+1, 0, −1) e as amplitudes por trecho conferem com a lista.
