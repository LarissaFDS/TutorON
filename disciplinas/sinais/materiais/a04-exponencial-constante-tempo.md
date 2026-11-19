---
id: sinais-anot-exponenciais
titulo: Exponencial real, complexa e senoide amortecida: constante de tempo τ = 1/σ, período 2π/ω₀ e envelope
assunto: sinais-03-sinais-elementares
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Modelos de Sinais" (4 abr. 2026)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sinais e Sistemas 2026.1; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-sinais-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Modelo geral:** $x(t) = Ce^{st}$ com $C = re^{j\phi}$ e $s = \sigma + j\omega_0$ complexos.

**Caso 1, exponencial real** ($s = \sigma$): $ae^{\sigma t}$ cresce se $\sigma > 0$, é constante se $\sigma = 0$. Para $x(t) = ae^{-\sigma t}u(t)$, $\sigma > 0$, a **constante de tempo** é $\tau = 1/\sigma$: $x(\tau) = a/e \approx 0{,}368a$, $x(2\tau) \approx 0{,}135a$, $x(3\tau) \approx 0{,}0498a$, $x(4\tau) \approx 0{,}0183a$, $x(5\tau) \approx 0{,}0067a$.

**Correção:** as anotações dizem que a exponencial "é reduzida 36,8%" a cada $\tau$. O certo: a cada intervalo $\tau$ o sinal **cai para** 36,8% do valor anterior (uma redução de 63,2%). Na prática, desprezível depois de 4τ a 5τ.

**Caso 2, exponencial complexa** ($\sigma = 0$): $x(t) = re^{j(\omega_0 t + \phi)} = r\cos(\omega_0 t + \phi) + jr\,\mathrm{sen}(\omega_0 t + \phi)$. É periódica: $e^{j\omega_0(t + T)} = e^{j\omega_0 t}$ exige $\omega_0 T = 2\pi m$, e o período fundamental é $T_0 = 2\pi/\omega_0$.

**Caso 3, geral:** $x(t) = re^{\sigma t}[\cos(\omega_0 t + \phi) + j\,\mathrm{sen}(\omega_0 t + \phi)]$. A parte real $re^{\sigma t}\cos(\omega_0 t + \phi)$ fica entre $\pm re^{\sigma t}$ (o **envelope**): senoide amortecida se $\sigma < 0$, crescente se $\sigma > 0$.

**Verificação:** $e^{-1} = 0{,}3679$, $1 - e^{-1} = 0{,}632$, $e^{-5} = 0{,}0067$; período de $e^{j4t}$: $2\pi/4 = \pi/2$, e $e^{j4(t + \pi/2)} = e^{j4t}$.
