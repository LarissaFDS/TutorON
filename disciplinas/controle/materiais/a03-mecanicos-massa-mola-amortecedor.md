---
id: controle-anot-massa-mola-amortecedor
titulo: Sistemas mecânicos: mola f = Kx, amortecedor f = bẋ, massa f = mẍ; função de transferência X(s)/F(s) = 1/(ms² + bs + K) do massa-mola-amortecedor; rotacional e satélite 1/(Js²)
assunto: controle-02-modelagem
tipo: resolucao
resolucao: sim
fonte: Anotações "Sistemas mecânicos" (19 ago. 2026) e "Revisão de Laplace e Sistemas mecânicos", p. 7–8 e 10
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

**Elementos translacionais:** mola linear $f = Kx$ ($K$ constante elástica); amortecedor ideal (atrito viscoso) $f = b\dot x$; massa $f = m\ddot x$ (2ª lei de Newton). **Rotacionais:** mola $T = K\theta$; atrito $T = b\omega = b\dot\theta$; inércia $T = J\ddot\theta$.

**Massa-mola-amortecedor (montagem da equipe a partir desses elementos):** massa $m$ presa a uma parede por mola $K$ e amortecedor $b$, força $f(t)$ aplicada. Somando as forças na massa:
$$m\ddot x + b\dot x + Kx = f(t).$$ Com condições iniciais nulas, a função de transferência de malha aberta (não há realimentação) é
$$G(s) = \frac{X(s)}{F(s)} = \frac{1}{ms^2 + bs + K}$$ (X de s sobre F de s é um sobre m s ao quadrado mais b s mais K). Na forma padrão de segunda ordem: $\omega_n = \sqrt{K/m}$, $\zeta = \frac{b}{2\sqrt{Km}}$, ganho estático $G(0) = 1/K$.

**Satélite rígido sem atrito:** torque $T$, ângulo de atitude $\theta$: $T = J\ddot\theta$, logo $G(s) = \frac{\Theta(s)}{T(s)} = \frac{1}{Js^2}$ (dois polos na origem: não é BIBO estável).

**Verificação:** força constante $F_0$ dá $x(\infty) = F_0/K$ (a mola equilibra); com $m = 1$, $b = 2$, $K = 5$ os polos são $-1 \pm 2j$ e $\zeta = 0{,}447$, conferidos por `roots`.
