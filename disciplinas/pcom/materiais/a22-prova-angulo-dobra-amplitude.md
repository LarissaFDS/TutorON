---
id: pcom-prova-angulo-dobra-amplitude
titulo: Prova: sinal modulado em ângulo com fm = 3 kHz e Δf = 12 kHz, β = 4 e 30 kHz; amplitude da mensagem dobrada e fm = 2 kHz dá 52 kHz em FM e 36 kHz em PM
assunto: pcom-04-modulacao-angular
tipo: prova
resolucao: sim
fonte: Anotações "Revisão Final prova 1" (9 set. 2026), p. 6–8 (questão 3 de prova, enunciado parafraseado); Anotações "Revisão prova 1" (30 ago. 2026), p. 3–4
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

**Enunciado (parafraseado):** $x_c(t) = A\cos[\omega_c t + B\sin(\omega_m t)]$, mensagem senoidal de 3 kHz e desvio máximo de 12 kHz. (a) Largura de faixa. (b) A amplitude da mensagem dobra e a frequência cai para 2 kHz: novo desvio e nova largura.

**(a)** $\beta = \Delta f/f_m = 12/3 = 4$ e $B_T = 2(4 + 1)\cdot 3 = 30$ kHz.

**(b) depende de ser FM ou PM:**
- **FM:** $\Delta f = k_fA_m/2\pi$ não depende de $f_m$. Dobrando $A_m$: $\Delta f = 24$ kHz, $\beta = 24/2 = 12$, $B_T = 2(24 + 2) = 52$ kHz.
- **PM:** $\beta = k_pA_m$ dobra: $\beta = 8$, $\Delta f = \beta f_m = 16$ kHz, $B_T = 2(8 + 1)\cdot 2 = 36$ kHz.

As anotações fazem a conta de PM (dobram o $B$ da fase): 16 kHz e 36 kHz. O enunciado diz só "modulado em ângulo"; confirme com o professor qual resposta é esperada.

**Questão parecida (Revisão prova 1):** $f_m = 3$ kHz e $\Delta f = 15$ kHz: $\beta = 5$, $B_T = 2(5 + 1)\cdot 3 = 36$ kHz. Para a "amplitude do sinal modulante" as anotações chegam a $5/(2\pi)$, misturando Hz e rad/s: a amplitude da fase é $\beta = 5$ rad; a amplitude de $m(t)$ só sai com $k_f$, que não foi dado.

**Verificação:** frequência instantânea simulada para os dois casos de (b): desvios de 24 kHz (FM) e 16 kHz (PM); Carson recalculado: 52 e 36 kHz.
