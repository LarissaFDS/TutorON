---
id: calc3-resumo-curvas-parametricas
titulo: Resumo de aula — curvas parametrizadas: dy/dx, parametrizações usuais (reta, circunferência, cicloide), área sob a curva
assunto: calc3-01-curvas-parametricas
tipo: material_estudo
resolucao: nao
fonte: "Resumo 1" (página do Notion "Cálculo 3"; manuscrito escaneado)
autoria: Resumo manuscrito anexado ao Notion da turma com o rótulo "Resumo do professor" (autoria não confirmada); paráfrase da equipe TutorON
licenca: Não declarada (material de turma); o arquivo não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco resume com texto próprio
fontes_catalogo: ufal-calc3-notion-resumos
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Resumo de aula sobre curvas parametrizadas, parafraseado (o Notion o rotula como "Resumo do professor"; a autoria não foi confirmada). Status da resolução: validada (fórmulas e exemplo conferidos com SymPy).

Curva parametrizada: $x = x(t)$, $y = y(t)$, com t num intervalo; a curva tem um sentido de percurso (o de t crescente). A mesma curva pode ter várias parametrizações.

Parametrizações usuais citadas:
- Reta por $P_0$ com direção $\mathbf{v}$: $(x, y) = P_0 + t\,\mathbf{v}$.
- Circunferência de centro (h, k) e raio a: $x = h + a\cos t$, $y = k + a\operatorname{sen} t$, $0 \le t \le 2\pi$ (anti-horário).
- Gráfico $y = f(x)$: $x = t$, $y = f(t)$.
- Cicloide (ponto de um círculo de raio r que rola sobre o eixo x): $x = r(\theta - \operatorname{sen}\theta)$, $y = r(1 - \cos\theta)$.

Tangente: $\dfrac{dy}{dx} = \dfrac{y'(t)}{x'(t)}$ quando $x'(t) \neq 0$ (derivada de y em relação a x, que é a razão das derivadas em relação a t). Tangente horizontal quando $y' = 0$ e $x' \neq 0$; vertical quando $x' = 0$ e $y' \neq 0$. Segunda derivada: $\dfrac{d^2y}{dx^2} = \dfrac{d(dy/dx)/dt}{dx/dt}$.

Área sob a curva (curva percorrida uma vez, $y \ge 0$): $A = \int_\alpha^\beta y(t)\,x'(t)\,dt$; se o percurso for da direita para a esquerda, troque os limites ou o sinal.

**Verificação:** para o arco da cicloide de raio r, $A = \int_0^{2\pi} r(1-\cos\theta)\, r(1-\cos\theta)\,d\theta = 3\pi r^2$ (três vezes a área do círculo).
