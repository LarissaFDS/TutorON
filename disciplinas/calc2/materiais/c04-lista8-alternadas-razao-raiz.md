---
id: calc2-lista8-alternadas-razao-raiz
titulo: Lista 8 (Profa. Xu Yang) — teste da série alternada, teste da razão e teste da raiz
assunto: calc2-03-series-convergencia
tipo: exercicio_resolvido
resolucao: sim
fonte: Lista 8 de Cálculo 2 (Profa. Xu Yang, UFAL), PDF do material do 2º período de Engenharia de Computação | enunciados parafraseados
curso: Engenharia de Computação (UFAL), ECOM010 Cálculo 2, 2º período; semestre não identificado
fontes_catalogo: ufal-xu-yang-calc2-listas
autoria: Enunciados da lista da Profa. Xu Yang; resoluções da equipe TutorON com apoio de IA, conferidas com SymPy
licenca: Não declarada (lista da disciplina; PDF não versionado)
publicacao_transcricao: não autorizada; enunciados parafraseados
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Cálculo 2, Lista 8 (séries alternadas, razão e raiz). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Série alternada** $\sum(-1)^{n}b_n$, $b_n > 0$: converge se $b_n$ é decrescente (a partir de algum $n$) e $b_n \to 0$.
- $\sum\tfrac{(-1)^{n-1}}{\sqrt n}$ e $\sum\tfrac{(-1)^n}{\ln(n+4)}$: convergem (condicionalmente).
- $\sum\tfrac{(-1)^n\ln n}{n}$: $\tfrac{\ln x}{x}$ decresce para $x > e$ (derivada $\tfrac{1-\ln x}{x^2}$) e vai a 0: converge.
- $\sum\tfrac{\text{sen}(n\pi/2)}{n!}$: os termos valem $1, 0, -1, 0, \dots$ divididos por $n!$; converge absolutamente ($|a_n| \le 1/n!$).
- $\sum(-1)^n\text{sen}(\pi/n)$: $\text{sen}(\pi/n)$ decresce para 0: converge.

**Razão:** $L = \lim|a_{n+1}/a_n|$. **Raiz:** $L = \lim\sqrt[n]{|a_n|}$. $L < 1$ converge absolutamente, $L > 1$ diverge, $L = 1$ não decide.
- $\sum\tfrac{n}{(\ln n)^n}$ (raiz): $\tfrac{\sqrt[n]{n}}{\ln n} \to 0$: converge.
- $\sum\left(\tfrac{n^2+1}{2n^2+1}\right)^n$ (raiz): $L = \tfrac12$: converge.
- $\sum\tfrac{2^{n^2}}{n!}$ (razão): $\tfrac{2^{2n+1}}{n+1} \to \infty$: diverge.
- $\sum\tfrac{2\cdot4\cdot6\cdots(2n)}{n!}$: o numerador é $2^n n!$, o termo é $2^n$: diverge.

Erro comum: usar razão ou raiz numa série $p$ (dá $L = 1$ e não conclui nada).

**Verificação:** limites da razão e da raiz e a monotonia conferidos com SymPy em `test_lista8_alternadas_razao_raiz`.
