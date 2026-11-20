---
id: controle-anot-primeira-ordem
titulo: Resposta ao degrau de sistema de primeira ordem K/(τs + 1): constante de tempo τ, 63,2% em τ, tempo de acomodação 4τ (2%) ou 3τ (5%), tempo de subida 2,2τ (10–90%)
assunto: controle-05-resposta-temporal
tipo: resolucao
resolucao: sim
fonte: Anotações "Análise de Resposta Temporal" (1º out. 2026), p. 1–3 e 6
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

**Modelo:** $G(s) = \frac{b_0}{s + a_0} = \frac{C}{\tau s + 1}$, com ganho estático $C = G(0) = b_0/a_0$ e constante de tempo $\tau = 1/a_0$ (polo em $-1/\tau$).

**Degrau unitário:** $y(t) = C(1 - e^{-t/\tau})$, $t \ge 0$. Resposta = transitório ($-Ce^{-t/\tau}$) + regime ($C$). $y(\tau) = 0{,}632C$; inclinação inicial $\dot y(0) = C/\tau \ne 0$.

**Especificações:**
- tempo de acomodação, critério de 2%: $t_s = -\tau\ln 0{,}02 = 3{,}91\tau \approx 4\tau$; critério de 5%: $t_s = -\tau\ln 0{,}05 \approx 3\tau$;
- tempo de subida de 10% a 90%: $t_r = \tau\ln 9 = 2{,}197\tau \approx 2{,}2\tau$;
- não há sobressinal.

**Exemplo (lista):** $G = \frac{8}{s + 5}$: $y = \frac85(1 - e^{-5t})$, $\tau = 0{,}2$ s, $y(\tau) = 1{,}6\cdot0{,}632 = 1{,}01$.

**Verificação:** `scipy.signal.step` de $8/(s+5)$ dá $y(0{,}2) = 1{,}011$ e entra na faixa de 2% em $t = 0{,}78$ s ($\approx 4\tau$).
