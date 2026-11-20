---
id: pcom-anot-pm-fm-diferenca
titulo: Diferença entre PM e FM: na PM a fase é kp m(t); na FM a frequência instantânea é ωc + kf m(t) e a fase é kf ∫m; simulação de PM e FM
assunto: pcom-04-modulacao-angular
tipo: material_estudo
resolucao: sim
fonte: Anotações "Simulação - Modulação FM e PM" (27 ago. 2026), p. 1–5; Anotações "Lista 2s" (19 ago. 2026), p. 1; Anotações "conceitos iniciais" (22 ago. 2026), p. 1
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

**Modulação em ângulo:** $x(t) = A\cos(\omega_c t + \phi(t))$; a amplitude é constante e a informação vai no ângulo.
- **PM (fase):** $\phi(t) = k_p\,m(t)$ ($k_p$ em rad/V). A fase segue a mensagem; a frequência instantânea é $\omega_c + k_p\dot m(t)$.
- **FM (frequência):** a **frequência instantânea** segue a mensagem, $\omega_i = \omega_c + k_f\,m(t)$ ($k_f$ em rad/s/V), então $\phi(t) = k_f\int m(\tau)\,d\tau$.

Logo FM de $m(t)$ é o mesmo que PM da integral de $m(t)$, e PM de $m$ é FM da derivada. Com tom $m(t) = A_m\cos\omega_m t$: FM dá $\phi = \beta\sin(\omega_m t)$ com $\beta = \frac{k_fA_m}{\omega_m} = \frac{\Delta\omega}{\omega_m}$; PM dá $\phi = k_pA_m\cos(\omega_m t)$, com $\beta = k_pA_m$.

**Simulação (MATLAB):** PM com $k_p = \pi$ (180°), $\pi/2$ e $3\pi/2$ rad, portadoras de 5, 10 e 9 Hz e mensagens de 1, 3 e 2 Hz; FM com $\beta = 15$, 0,5 e 20, portadoras de 1000, 750 e 1200 Hz e mensagens de 60, 250 e 300 Hz. Quanto maior $\beta$, mais "sanfonado" o sinal.

Correção: as anotações escrevem, para FM, $\phi(t) = \frac{\Delta\omega}{\omega_m}m(t) = \beta\,m(t)$. Isso só vale com tom e com o seno: a fase é $\beta\sin(\omega_m t)$ quando $m = \cos(\omega_m t)$. No código, $m(t)$ é um seno, mas a fase usa $\beta\sin$; então o gráfico é FM de um cosseno (ou PM do seno desenhado).

**Verificação:** derivando numericamente a fase de $\beta\sin(2\pi f_m t)$, o desvio máximo da frequência instantânea é $\beta f_m$ (900 Hz para $\beta = 15$, $f_m = 60$ Hz).
