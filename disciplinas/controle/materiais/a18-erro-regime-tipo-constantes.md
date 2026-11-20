---
id: controle-anot-erro-regime-tipo
titulo: Erro em regime permanente com realimentação unitária: ess = lim s·R/(1+G); tipo do sistema (polos na origem de G em malha aberta); Kp, Kv, Ka; degrau, rampa e parábola
assunto: controle-06-erro-regime
tipo: resolucao
resolucao: sim
fonte: Anotações "Resposta em Regime permanente" (20 out. 2026), p. 1–6
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Erro de rastreamento:** $e(t) = r(t) - y(t)$, $E = [1 - G_{mf}]R$. Se $G_{mf}$ é **BIBO estável**, vale o TVF: $e_{ss} = \lim_{s\to0}s[1 - G_{mf}(s)]R(s)$. Verifique a estabilidade antes.

**Realimentação unitária negativa** ($G_{mf} = \frac{G}{1 + G}$, $G$ de malha aberta): $e_{ss} = \lim_{s\to0}\frac{sR(s)}{1 + G(s)}$.

**Tipo do sistema:** número $n_I$ de polos de $G$ (malha **aberta**) na origem, $G = \frac{B(s)}{s^{n_I}(\dots)}$.

| Entrada | $R(s)$ | Constante | $e_{ss}$ |
|---|---|---|---|
| degrau $1$ | $1/s$ | $K_p = \lim G$ | $\frac{1}{1 + K_p}$ |
| rampa $t$ | $1/s^2$ | $K_v = \lim sG$ | $\frac{1}{K_v}$ |
| parábola $t^2/2$ | $1/s^3$ | $K_a = \lim s^2G$ | $\frac{1}{K_a}$ |

- Tipo 0: erro finito ao degrau, infinito à rampa.
- **Tipo 1: erro nulo ao degrau**, $1/K_v$ à rampa, infinito à parábola.
- Tipo 2: nulo ao degrau e à rampa, $1/K_a$ à parábola. Tipo $\ge 3$: nulo também à parábola.

**Correções:** as anotações chamam $r = t^2$ de "parábola unitária" com $R = 1/s^3$; $1/s^3$ é de $t^2/2$ (de $t^2$ seria $2/s^3$). E escrevem "$n_I > 3$" onde é $n_I \ge 3$.

**Verificação:** com $G = \frac{1}{s(s + 1)}$ (tipo 1): $K_v = 1$; a simulação da malha fechada com rampa dá $e(t) \to 1$ e com degrau $e \to 0$.
