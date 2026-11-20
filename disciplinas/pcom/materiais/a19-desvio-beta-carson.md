---
id: pcom-anot-desvio-beta-carson
titulo: Desvio de frequência Δf, índice de modulação β = Δf/fm e regra de Carson BT = 2(Δf + fm) = 2(β + 1)fm; banda estreita e banda larga
assunto: pcom-04-modulacao-angular
tipo: material_estudo
resolucao: sim
fonte: Anotações "fórmulas fundamentais para a prova 1" (7 set. 2026), p. 2 e 4; Anotações "Lista 2s" (19 ago. 2026), p. 2; Anotações "Revisão Final prova 1" (9 set. 2026), p. 8
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

**Desvio de frequência:** o maior afastamento da frequência instantânea em relação à portadora,
$$\Delta\omega = |\dot\phi(t)|_{max}\ \text{(rad/s)},\qquad \Delta f = \frac{\Delta\omega}{2\pi}\ \text{(Hz)}.$$ **Índice de modulação:** $\beta = \frac{\Delta\omega}{\omega_m} = \frac{\Delta f}{f_m}$ (adimensional; desvio sobre a frequência da mensagem).

**Regra de Carson** (cerca de 98% da potência):
$$B_T \approx 2(\Delta f + f_m) = 2(\beta + 1)f_m.$$ Banda estreita ($\beta \ll 1$): $B_T \approx 2f_m$, como no AM. Banda larga ($\beta \gg 1$): $B_T \approx 2\Delta f$.

**Exemplo:** FM com $\Delta f = 75$ kHz e $f_m = 15$ kHz: $\beta = 5$ e $B_T = 2(75 + 15) = 180$ kHz. Note que $\Delta f$ e $f_m$ entram somados: trocar um pelo outro não muda a soma, mas muda $\beta$ (seria 0,2 em vez de 5).

**Passos:** (1) escreva a fase $\phi(t)$; (2) derive e pegue o máximo: $\Delta\omega$ em rad/s; (3) divida por $2\pi$: $\Delta f$ em Hz; (4) $\beta = \Delta f/f_m$; (5) Carson em Hz.

Correção: as anotações escrevem "$\Delta\omega = 12$ kHz" e "$|\phi'|_{max} = 15$ kHz". $\Delta\omega$ é em rad/s; quando o valor está em Hz, é $\Delta f$ ($\Delta\omega = 2\pi\cdot 12\cdot 10^3 = 24000\pi$ rad/s).

**Verificação:** com $\beta = 5$, a soma de $J_n^2(5)$ para $|n| \le 6$ (as linhas dentro dos 180 kHz) dá 0,99 da potência (SciPy, `jv`).
