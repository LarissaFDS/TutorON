---
id: pcom-lista3-eficiencia-espectral
titulo: Eficiência espectral η = Rb/BT em bit/s/Hz; QPSK com pulsos de Nyquist: 2 bit/s/Hz, 2/(1 + α) com cosseno levantado; 16-QAM 4 bit/s/Hz; 4-ASK em largura 2W
assunto: pcom-06-modulacao-digital
tipo: lista
resolucao: sim
fonte: Anotações "Modulação Digital" (23 set. 2026), p. 5–8 (questões 8 e 9, enunciados não transcritos)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Princípios de Comunicação 2026.2; docente Jobson de Araújo Nascimento, conforme os cabeçalhos das simulações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de listas e de provas parafraseados; fotos de slide, capturas de tela e figuras coladas não foram copiadas
fontes_catalogo: ufal-pcom-anotacoes-otavio-2026-2, mit-ocw-6-02
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: pendente_professor
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: pendente de confirmação do professor.

**Eficiência espectral:** $\eta = R_b/B_T$, em bit/s/Hz (bits por segundo transmitidos em cada hertz de banda).

Com pulsos de Nyquist ideais, um sinal em banda passante de $R_s$ símbolos por segundo ocupa $B_T = R_s$ (de $f_c - R_s/2$ a $f_c + R_s/2$). Como $R_b = R_s\log_2 M$:
$$\eta = \log_2 M\ \text{(ideal)},\qquad \eta = \frac{\log_2 M}{1 + \alpha}\ \text{(cosseno levantado com fator de rolagem } \alpha).$$

- **QPSK:** 2 bits por símbolo, $\eta = 2$ bit/s/Hz no ideal; com $\alpha = 0{,}25$, $2/1{,}25 = 1{,}6$ bit/s/Hz. BPSK: 1 bit/s/Hz.
- **16-QAM:** 4 bit/s/Hz no ideal: é mais eficiente que QPSK (questão 9), porque cada símbolo leva mais bits na mesma banda, ao custo de símbolos mais próximos (mais sensível a ruído).

**Questão 8 (4-ASK):** com a banda de largura $2W$ (de $-W$ a $W$ em torno da portadora, como no AM), as anotações usam $V_m = 2W$ bauds e $V_T = 2W\cdot 2 = 4W$ bit/s. O $V_m = 2W$ vem de $B_T = R_s$ acima; a anotação registra que o aluno não entendeu essa parte.

Pendente: os enunciados das questões 8 e 9 não estão nas anotações, e a convenção de banda (com ou sem rolagem) precisa ser confirmada com o professor. As fórmulas de $\eta$ são complemento da equipe.

**Verificação:** $\log_2 4 = 2$, $\log_2 16 = 4$ e $2/(1 + 0{,}25) = 1{,}6$ conferidos; para 4-ASK, $R_b/B_T = 4W/2W = 2$ bit/s/Hz, igual a $\log_2 4$.
