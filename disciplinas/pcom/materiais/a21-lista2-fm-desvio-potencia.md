---
id: pcom-lista2-fm-desvio-potencia
titulo: Lista 2: s(t) = 100cos[2πfc t + 15 sen(2π·5000t)], Δf = 75 kHz, β = 15, largura 2Δf = 150 kHz ou Carson 160 kHz, potência 5 kW; x(t) = 100cos[2000πt + sen(100πt)], Δf = 50 Hz
assunto: pcom-04-modulacao-angular
tipo: lista
resolucao: sim
fonte: Anotações "Lista 2s" (19 ago. 2026), p. 2–3 (questões 3 e 4)
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

**Questão 3:** $s(t) = 100\cos[2\pi f_c t + 15\sin(2\pi f_m t)]$, $f_c = 100$ MHz, $f_m = 5$ kHz.
- Desvio: $|\dot\phi|_{max} = 15\cdot 2\pi\cdot 5000 = 150000\pi$ rad/s, ou seja $\Delta f = 75$ kHz; $\beta = 75/5 = 15$.
- Largura: as anotações usam $2\Delta f = 150$ kHz ($300000\pi$ rad/s), a aproximação de banda larga. Pela regra de Carson, $2(\Delta f + f_m) = 2(75 + 5) = 160$ kHz.
- Potência: a amplitude do FM é constante, então $P = \frac{100^2}{2} = 5$ kW (em 1 Ω). Cuidado: o 15 está dentro da fase e não entra na potência.

**Questão 4:** $x(t) = 100\cos[2000\pi t + \sin(100\pi t)]$: $\Delta\omega = |100\pi\cos(100\pi t)|_{max} = 100\pi$ rad/s, logo $\Delta f = 50$ Hz; $f_m = 50$ Hz, $\beta = 1$ e Carson $2(50 + 50) = 200$ Hz.

Correção: na questão 4 a anotação escreve "$\Delta f = 100\pi$". Esse valor é $\Delta\omega$, em rad/s; em Hz, $\Delta f = 50$ Hz.

**Verificação:** frequência instantânea calculada numericamente: máximos de 75 kHz e 50 Hz acima da portadora; a média de $s^2$ dá 5000 W; as raias de Bessel de $\beta = 15$ fora de $\pm 160$ kHz somam menos de 2% da potência.
