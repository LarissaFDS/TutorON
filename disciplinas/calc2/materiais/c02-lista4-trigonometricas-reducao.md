---
id: calc2-lista4-trigonometricas-reducao
titulo: Lista 4 (Profa. Xu Yang) — fórmula de redução de ∫cosⁿx, integrais trigonométricas (sen³x cos²x, sen⁷x cos⁵x, tan⁴x, √(1 + cos 2x)) e ortogonalidade de seno e cosseno
assunto: calc2-02-integrais-trigonometricas
tipo: exercicio_resolvido
resolucao: sim
fonte: Lista 4 de Cálculo 2 (Profa. Xu Yang, UFAL), imagem do material do 2º período de Engenharia de Computação | enunciados parafraseados
curso: Engenharia de Computação (UFAL), ECOM010 Cálculo 2, 2º período; semestre não identificado
fontes_catalogo: ufal-xu-yang-calc2-listas
autoria: Enunciados da lista da Profa. Xu Yang; resoluções da equipe TutorON com apoio de IA, conferidas com SymPy
licenca: Não declarada (lista da disciplina; imagem não versionada)
publicacao_transcricao: não autorizada; enunciados parafraseados
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Cálculo 2, Lista 4 (integrais trigonométricas). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Fórmula de redução:** $\int\cos^n x\,dx = \tfrac1n\cos^{n-1}x\,\text{sen}\,x + \tfrac{n-1}{n}\int\cos^{n-2}x\,dx$. Prova: partes com $u = \cos^{n-1}x$, $dv = \cos x\,dx$, e troque $\text{sen}^2x = 1 - \cos^2x$. Com $n = 2$: $\int\cos^2x\,dx = \tfrac{x}{2} + \tfrac{\text{sen}\,2x}{4} + C$.

**Potências de seno e cosseno:** se uma das potências é ímpar, separe um fator e troque o resto pela identidade $\text{sen}^2 + \cos^2 = 1$.
- $\int\text{sen}^3x\cos^2x\,dx$ ($w = \cos x$): $\tfrac{\cos^5x}{5} - \tfrac{\cos^3x}{3} + C$.
- $\int_0^{\pi/2}\text{sen}^7x\cos^5x\,dx = \tfrac{1}{120}$.
- $\int_0^{\pi/4}\tan^4x\,dx$: use $\tan^2 = \sec^2 - 1$ duas vezes: $\tfrac{\pi}{4} - \tfrac23$.
- $\int_0^{\pi/6}\sqrt{1+\cos 2x}\,dx$: $1 + \cos 2x = 2\cos^2x$, e $\cos x > 0$ no intervalo: $\sqrt2\,\text{sen}(\pi/6) = \tfrac{\sqrt2}{2}$.

**Ortogonalidade** ($m$, $n$ inteiros positivos): transforme produto em soma, por exemplo $\text{sen}\,mx\cos nx = \tfrac12[\text{sen}(m+n)x + \text{sen}(m-n)x]$. Em $[-\pi, \pi]$, $\int\text{sen}\,mx\cos nx\,dx = 0$ sempre; $\int\text{sen}\,mx\,\text{sen}\,nx\,dx$ e $\int\cos mx\cos nx\,dx$ valem 0 se $m \ne n$ e $\pi$ se $m = n$ (é a base da série de Fourier).

Erro comum: tirar a raiz de $\cos^2 x$ sem o módulo; aqui pode porque $\cos x > 0$ entre 0 e $\pi/6$.

**Verificação:** as definidas e a ortogonalidade (vários pares m, n) foram calculadas com SymPy em `test_lista4_trigonometricas`.
