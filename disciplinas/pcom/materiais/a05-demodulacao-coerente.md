---
id: pcom-anot-demodulacao-coerente
titulo: Demodulação coerente (síncrona): multiplicar pela portadora e filtrar passa-baixas; erro de fase cos φ; componentes em 0, banda básica e 2fc
assunto: pcom-02-am-dsb
tipo: material_estudo
resolucao: sim
fonte: Anotações "Modulação AM" (25 ago. 2026), p. 2; Anotações "Simulação Modulação AM" (30 ago. 2026), p. 10–14
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

**Demodulação coerente:** multiplica-se o sinal recebido por uma portadora local de mesma frequência e passa-se por um **filtro passa-baixas**. Com DSB-SC e erro de fase $\phi$:
$$m(t)\cos(\omega_c t)\cos(\omega_c t + \phi) = \frac{m(t)}{2}[\cos\phi + \cos(2\omega_c t + \phi)],$$ e o filtro deixa $\frac{1}{2}m(t)\cos\phi$. Com $\phi = 90^\circ$ a mensagem é perdida.

**Com portadora** (simulação, nível $K$ somado antes do modulador): $e(t) = [K + m(t)]\cos^2(\omega_c t) = \frac{K}{2} + \frac{m(t)}{2} + \frac{K}{2}\cos(2\omega_c t) + \frac{m(t)}{2}\cos(2\omega_c t)$: nível contínuo em 0 Hz, mensagem em banda básica, portadora em $2f_c$ e bandas laterais em $2f_c \pm f_m$. O passa-baixas deixa $\frac{K}{2} + \frac{m(t)}{2}$; para ter $m(t)$ exato tira-se o nível contínuo e compensa-se o ganho 1/2.

Simulação com $f_m = 300$ Hz e $f_c = 1500$ Hz: componentes em 0, $\pm 300$ Hz, 3000 Hz, 2700 Hz e 3300 Hz. O filtro corta em 300 Hz (a anotação fala em "largura de 600 Hz", contando de $-300$ a $+300$ Hz).

Correção: a 2ª parte da simulação usa $f_c = 3000$ Hz e a 3ª usa $f_c = 1500$ Hz ($2f_c = 3000$ Hz), mas o texto não avisa a troca.

**Verificação:** o produto foi simulado (NumPy) e filtrado com Butterworth de corte 1 kHz: sai $\frac{1}{2}\cos(2\pi\,300t)$ com erro menor que 1%; com $\phi = 90^\circ$ a saída fica abaixo de 1% de amplitude.
