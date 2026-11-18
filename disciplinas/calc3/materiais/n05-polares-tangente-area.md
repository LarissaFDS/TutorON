---
id: calc3-nota-polares-tangente-area
titulo: Nota — coordenadas polares: conversão, tangente a r = f(θ), área e comprimento de arco em polares
assunto: calc3-02-coordenadas-polares
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: ufal-calc3-provas-2024-1,ufal-calc3-topicos-ab1,openstax-calculus-vol3
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Coordenadas polares (Stewart, Clegg e Watson, *Cálculo*, vol. 2, 9ª ed., seções 10.3 e 10.4). A página "Coordenada polar" do Notion da turma está vazia; os tópicos constam da lista de conteúdos da AB1. Conferida com SymPy.

Conversão: $x = r\cos\theta$, $y = r\operatorname{sen}\theta$; $r^2 = x^2 + y^2$, $\tan\theta = y/x$ (escolha o quadrante de θ pelo sinal de x e y). Um ponto tem infinitas representações: $(r, \theta)$, $(r, \theta + 2\pi)$, $(-r, \theta + \pi)$.

Tangente a $r = f(\theta)$: tratando θ como parâmetro,
$$\frac{dy}{dx} = \frac{f'(\theta)\operatorname{sen}\theta + f(\theta)\cos\theta}{f'(\theta)\cos\theta - f(\theta)\operatorname{sen}\theta}.$$
Horizontal: numerador zero e denominador não; vertical: o contrário. Na origem (r = 0), a tangente tem a direção θ. Exemplo da turma: a cardioide da AB1 2024.1, questão 3.

Área da região entre a curva e os raios θ = a e θ = b:
$$A = \int_a^b \tfrac12\,r^2\,d\theta$$
(meio r ao quadrado; vem da área do setor circular $\tfrac12 r^2\Delta\theta$). Área entre duas curvas: $\tfrac12\int_a^b (r_{ext}^2 - r_{int}^2)\,d\theta$; ache os ângulos de interseção e confira também a origem, que pode ser atingida em ângulos diferentes.

Comprimento de arco: $L = \int_a^b \sqrt{r^2 + (dr/d\theta)^2}\,d\theta$.

Exemplo: a cardioide $r = 1 + \operatorname{sen}\theta$ tem área $\tfrac12\int_0^{2\pi}(1 + \operatorname{sen}\theta)^2 d\theta = \tfrac{3\pi}{2}$ e comprimento 8.

**Verificação:** a circunferência r = a dá $A = \tfrac12 a^2 \cdot 2\pi = \pi a^2$ e $L = \int_0^{2\pi} a\,d\theta = 2\pi a$.
