---
id: calc2-revisao-prova4-representacao-taylor
titulo: Revisão da prova 4 (Profa. Xu Yang) — representar funções por séries de potências (geométrica, derivar, integrar, frações parciais) e séries de Taylor e Maclaurin
assunto: calc2-04-series-de-potencias-taylor
tipo: exercicio_resolvido
resolucao: sim
fonte: Revisão de Prova 4 de Cálculo 2 (Profa. Xu Yang, UFAL), imagem do material do 2º período de Engenharia de Computação | enunciados parafraseados
curso: Engenharia de Computação (UFAL), ECOM010 Cálculo 2, 2º período; semestre não identificado
fontes_catalogo: ufal-xu-yang-calc2-listas
autoria: Enunciados da revisão da Profa. Xu Yang; resoluções da equipe TutorON com apoio de IA, conferidas com SymPy
licenca: Não declarada (revisão da disciplina; imagem não versionada)
publicacao_transcricao: não autorizada; enunciados parafraseados
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Cálculo 2, revisão da prova 4 (séries de potências e Taylor). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Ponto de partida:** $\tfrac{1}{1-u} = \sum u^n$ para $|u| < 1$. Escreva a função nessa forma.
- $\tfrac{3}{1-x^2} = \sum 3x^{2n}$, $|x| < 1$.
- $\tfrac{1}{x+10} = \tfrac{1}{10}\cdot\tfrac{1}{1+x/10} = \sum\tfrac{(-1)^n x^n}{10^{n+1}}$, $|x| < 10$.
- $\tfrac{x^2}{a^2-x^2} = \sum\tfrac{x^{2n+2}}{a^{2n+2}}$, $|x| < |a|$.
- $\tfrac{x+2}{2x^2-x-1} = \tfrac{1}{x-1} - \tfrac{1}{2x+1} = -\sum x^n - \sum(-2x)^n$; vale onde as duas valem: $|x| < \tfrac12$.

**Integrar ou derivar a geométrica** (o raio não muda): $\ln(5-x) = \ln 5 - \sum_{n\ge1}\tfrac{x^n}{n\,5^n}$, $R = 5$. $\tfrac{x^2}{(1-2x)^2} = \sum_{n\ge0}(n+1)2^n x^{n+2}$, $R = \tfrac12$.

**Taylor em $a$:** $\sum\tfrac{f^{(n)}(a)}{n!}(x-a)^n$ (Maclaurin é $a = 0$).
- $\text{sen}\,2x = \sum\tfrac{(-1)^n(2x)^{2n+1}}{(2n+1)!}$; $xe^x = \sum\tfrac{x^{n+1}}{n!}$.
- $x^3$ em $a = -1$: $-1 + 3(x+1) - 3(x+1)^2 + (x+1)^3$ (polinômio: a série termina).
- $\tfrac1x$ em $a = -3$: $-\sum\tfrac{(x+3)^n}{3^{n+1}}$, $|x+3| < 3$.
- $\text{sen}^2x = \tfrac12(1-\cos 2x) = x^2 - \tfrac{x^4}{3} + \tfrac{2x^6}{45} - \dots$
- $x^2\arctan(x^3) = \sum\tfrac{(-1)^n x^{6n+5}}{2n+1}$, $|x| \le 1$.

**Verificação:** cada série foi comparada com a expansão do SymPy (`series`) em `test_revisao_representacao_taylor`.
