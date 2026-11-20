---
id: pcom-lista3-taxas-qam
titulo: Lista 3: 50 kbauds e 200 kbit/s dão 16-QAM; 10 Mbit/s com compressão 20:1 em 32-QAM dá 100 kbauds; 2-ASK e 2-PSK pelos ciclos por símbolo; 64-QAM a 120 Mbit/s dá 20 Mbauds
assunto: pcom-06-modulacao-digital
tipo: lista
resolucao: sim
fonte: Anotações "Modulação Digital" (23 set. 2026), p. 4–7 (questões 6, 7, 10, 11 e 14, enunciados parafraseados)
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

Todas usam $V_T = V_m\cdot k$, com $M = 2^k$.

- **Q6:** $V_m = 50$ kbauds e $V_T = 200$ kbit/s: $k = 200/50 = 4$ bits por símbolo, $M = 2^4 = 16$: **16-QAM**.
- **Q7:** fonte de 10 Mbit/s comprimida 20:1: $V_T = 10/20 = 0{,}5$ Mbit/s. Em 32-QAM, $k = \log_2 32 = 5$: $V_m = 500/5 = 100$ kbauds.
- **Q10:** 2-ASK (um bit por símbolo, "0" ou "1"), portadora de 2,4 kHz e 2 ciclos por símbolo: $V_m = 2{,}4/2 = 1{,}2$ kbaud e $V_T = 1{,}2$ kbit/s.
- **Q11:** 2-PSK (a inversão de fase marca a inversão do bit, fases 0° e 180°), portadora de 3 kHz e 1 ciclo por símbolo: $V_m = 3$ kbauds $= 3$ kbit/s.
- **Q14:** 64-QAM varia amplitude e fase; $\log_2 64 = 6$ bits por símbolo; com $V_T = 120$ Mbit/s, $V_m = 120/6 = 20$ Mbauds.

As dúvidas anotadas ("por que 2 ciclos?") vêm do gráfico do enunciado: o número de ciclos por símbolo se conta no desenho, entre duas mudanças de símbolo.

**Verificação:** as cinco contas foram refeitas com `math.log2` e divisões exatas (`fractions`).
