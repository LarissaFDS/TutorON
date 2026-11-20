---
id: pcom-anot-am-convencional-indice
titulo: AM convencional: s(t) = Ac[1 + μ m(t)]cos(2πfc t); índice de modulação μ = B/A = (Emax − Emin)/(Emax + Emin); submodulação, 100% e sobremodulação
assunto: pcom-02-am-dsb
tipo: material_estudo
resolucao: sim
fonte: Anotações "Modulação AM" (25 ago. 2026), p. 2–3; Anotações "fórmulas fundamentais para a prova 1" (7 set. 2026), p. 1 e 3
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

O AM convencional transmite a portadora junto com as bandas laterais:
$$s(t) = A_c[1 + \mu\,m_n(t)]\cos(2\pi f_c t),$$ com $m_n(t)$ a mensagem normalizada (valor máximo 1). Com tom, $s(t) = [A + B\cos(2\pi f_m t)]\cos(2\pi f_c t)$ e o **índice de modulação** é $\mu = B/A$ (amplitude da mensagem sobre o nível da envoltória; $A$ = amplitude da portadora, $B$ = amplitude da mensagem).

Expandindo: $s(t) = A\cos(2\pi f_c t) + \frac{A\mu}{2}\cos[2\pi(f_c + f_m)t] + \frac{A\mu}{2}\cos[2\pi(f_c - f_m)t]$.

| Componente | Frequência | Amplitude | Impulso em $S(f)$ |
|---|---|---|---|
| portadora | $f_c$ | $A$ | $A/2$ |
| banda lateral inferior | $f_c - f_m$ | $A\mu/2$ | $A\mu/4$ |
| banda lateral superior | $f_c + f_m$ | $A\mu/2$ | $A\mu/4$ |

**Pela envoltória:** $\mu = \frac{E_{max} - E_{min}}{E_{max} + E_{min}}$. $0 < \mu < 1$: modulação normal (submodulação); $\mu = 1$: 100%; $\mu > 1$: **sobremodulação**, a envoltória inverte e o detector de envoltória distorce.

Correção: as anotações destacam "$B = A_c\mu/2$". O certo é $B = A_c\mu$; $A_c\mu/2$ é a amplitude de **cada** banda lateral.

**Verificação:** com $A = 2$ e $B = 1$, $E_{max} = 3$, $E_{min} = 1$ e as duas fórmulas dão $\mu = 0{,}5$; a FFT mostra 1 em $f_c$ e 0,25 em $f_c \pm f_m$.
