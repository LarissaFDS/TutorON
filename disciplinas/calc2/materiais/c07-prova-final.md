---
id: calc2-prova-final
titulo: Prova final de Cálculo 2 — f definida por equação integral, integral da inversa, fórmula de Wallis, integral imprópria de x^a/(1 + x^b) e uma série para π
assunto: calc2-05-integral-impropria-aplicacoes
tipo: prova
resolucao: sim
fonte: Foto da prova final de Cálculo 2 (UFAL) do material do 2º período de Engenharia de Computação; sem nome de aluno nem de professor preenchidos | enunciados parafraseados
curso: Engenharia de Computação (UFAL), ECOM010 Cálculo 2, 2º período; semestre e professor não identificados
fontes_catalogo: ufal-calc2-prova-final
autoria: Enunciados da prova final; resoluções da equipe TutorON com apoio de IA, conferidas com SymPy
licenca: Não declarada (prova da disciplina; foto não versionada)
publicacao_transcricao: não autorizada; enunciados parafraseados
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Cálculo 2, prova final (parafraseada). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor. Prova é atividade avaliativa: o tutor guia, não entrega.

1. $\int_1^x f(t)\,dt = (x-1)e^{2x} + \int_1^x e^{-t}f(t)\,dt$ para todo $x$. Ache $f$.
Derive os dois lados (Teorema Fundamental): $f(x) = (2x-1)e^{2x} + e^{-x}f(x)$, logo $f(x) = \dfrac{(2x-1)e^{3x}}{e^x - 1}$.

2. $f$ contínua e crescente, $f(0) = 0$, $f(1) = 1$, $\int_0^1 f = \tfrac13$. Quanto vale $\int_0^1 f^{-1}(y)\,dy$?
As duas áreas completam o quadrado $[0,1]^2$: $\int_0^1 f + \int_0^1 f^{-1} = 1$, então a resposta é $\tfrac23$ (com $f(x) = x^2$: $\int_0^1\sqrt y\,dy = \tfrac23$).

3. Wallis: pela fórmula de redução, $I_n = \tfrac{n-1}{n}I_{n-2}$ com $I_n = \int_0^{\pi/2}\text{sen}^n x\,dx$ e $I_0 = \tfrac{\pi}{2}$, o que dá $I_{2n} = \tfrac{1\cdot3\cdots(2n-1)}{2\cdot4\cdots 2n}\cdot\tfrac{\pi}{2}$. Como $0 \le \text{sen}\,x \le 1$, as potências maiores são menores: $I_{2n+2} \le I_{2n+1} \le I_{2n}$.

4. Se $a > -1$ e $b > a + 1$, $\int_0^\infty\tfrac{x^a}{1+x^b}dx$ converge: perto de 0 o integrando se comporta como $x^a$ (integrável se $a > -1$); no infinito, como $x^{a-b}$ (integrável se $b - a > 1$).

5. Completando o quadrado, $\int_0^{1/2}\tfrac{dx}{x^2-x+1} = \tfrac{\pi}{3\sqrt3}$. Como $x^3 + 1 = (x+1)(x^2-x+1)$, o integrando é $\tfrac{x+1}{x^3+1} = (x+1)\sum(-1)^n x^{3n}$; integrando termo a termo em $[0, \tfrac12]$ sai $\pi = \tfrac{3\sqrt3}{4}\sum\tfrac{(-1)^n}{8^n}\left(\tfrac{2}{3n+1} + \tfrac{1}{3n+2}\right)$.

**Verificação:** a equação integral, as integrais e a série de π (60 termos) foram conferidas com SymPy em `test_prova_final`.
