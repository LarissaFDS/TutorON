---
id: controle-anot-revisao-primeira-ordem
titulo: Revisão prova 1: termômetro de 1ª ordem (95% em 45 s, τ = 15 s, erro de 5° na rampa de 20°/min); malha fechada K/(τs+1) com yss = 0,96 e 0,60 em 1 s
assunto: controle-05-resposta-temporal
tipo: resolucao
resolucao: sim
fonte: Anotações "Revisão prova 1" (2 out. 2026), questão 2 e exercício 4.1
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Termômetro (paráfrase):** modelo de 1ª ordem $\frac{1}{\tau s + 1}$ (ganho 1: indica a temperatura exata em regime constante). Atinge 95% da leitura em 45 s.
- (a) 95% é o critério de 5%: $3\tau = 45 \Rightarrow \tau = 15$ s.
- (b) banho aquecendo em rampa de $20^\circ$/min $= \frac{1}{3}\,{}^\circ$/s, $R = \frac{1/3}{s^2}$. O sistema é estável (polo $-1/15$), então vale o TVF:
$$e_{ss} = \lim_{s\to0}s\Big[1 - \frac{1}{15s + 1}\Big]\frac{1/3}{s^2} = \frac{15}{3} = 5^\circ.$$ Depois de 2 min ($8\tau$) o transitório já acabou: o termômetro marca $5^\circ$ a menos.

**Exercício 4.1 (paráfrase):** malha fechada com $G = \frac{K}{\tau s + 1}$ e $H = 1$; a saída ao degrau vai a $0{,}96$ e vale $0{,}60$ em $t = 1$ s. $G_{mf} = \frac{K}{\tau s + 1 + K}$, ganho $\frac{K}{1 + K} = 0{,}96 \Rightarrow K = 24$; constante de tempo de malha fechada $\frac{\tau}{1 + K}$; $0{,}60 \approx 0{,}632\cdot0{,}96$, logo $\tau_{mf} \approx 1$ s e $\tau = 25$ s.

**Verificação:** a simulação do termômetro com a rampa dá erro de quase $5^\circ$ em 120 s; com $K = 24$, $\tau = 25$: $y(\infty) = 0{,}96$ e $y(1) \approx 0{,}61$.
