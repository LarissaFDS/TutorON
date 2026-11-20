---
id: pcom-anot-fourier-cosseno-espectro
titulo: Espectro do cosseno: A cos(2π f0 t) ↔ (A/2)[δ(f − f0) + δ(f + f0)], fator 1/2; propriedade da modulação x(t)cos(2πfc t); espectro simétrico
assunto: pcom-01-sinais-espectro
tipo: material_estudo
resolucao: sim
fonte: Anotações "conceitos iniciais" (22 ago. 2026), p. 2–3; Anotações "fórmulas fundamentais para a prova 1" (7 set. 2026), p. 2–3
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

A transformada de Fourier mostra quais frequências formam o sinal e com que intensidade. Pares usados na disciplina:

- Em Hz: $A\cos(2\pi f_0 t) \leftrightarrow \frac{A}{2}[\delta(f - f_0) + \delta(f + f_0)]$: o cosseno real dá **duas linhas**, em $+f_0$ e $-f_0$, cada uma com peso $A/2$ (A sobre 2).
- Em rad/s: $A\cos(\omega_0 t) \leftrightarrow A\pi[\delta(\omega - \omega_0) + \delta(\omega + \omega_0)]$.
- Seno: $A\sin(2\pi f_0 t) \leftrightarrow \frac{A}{2j}[\delta(f - f_0) - \delta(f + f_0)]$.
- **Modulação:** $x(t)\cos(2\pi f_c t) \leftrightarrow \frac{1}{2}[X(f - f_c) + X(f + f_c)]$: uma cópia do espectro em $+f_c$, outra em $-f_c$, cada uma multiplicada por 1/2.
- Sinal real: $X(-f) = X^*(f)$, então $|X(-f)| = |X(f)|$ (módulo simétrico).

**Exemplo:** $x(t) = 3\cos(2\pi\,1000t) + 2\cos(2\pi\,3000t)$ tem linhas em $\pm 1$ kHz com peso 1,5 e em $\pm 3$ kHz com peso 1.

Correção: a folha de fórmulas escreve o par em rad/s como "$X(f) = A\pi[\delta(\omega - \omega_0) + \dots]$"; com impulsos em $\omega$ a função é $X(\omega)$. Os pesos 1,5 e 1 do exemplo são complemento da equipe (a anotação só lista as frequências).

**Verificação:** a FFT de $x(t)$ amostrado em 1 s dá picos de 1,5 em 1 kHz e 1,0 em 3 kHz (espectro bilateral normalizado por $N$).
