---
id: calc3-nota-limite-xy-sobre-x2-y2
titulo: Nota — limite de xy/(x²+y²) em (0,0) não existe: retas y = mx dão m/(1+m²)
assunto: calc3-08-limites-derivadas-parciais
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: ufal-calc3-notion-anotacoes,ufal-calc3-provas-2024-1,openstax-calculus-vol3
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Exemplo clássico de limite em duas variáveis que não existe (Stewart, Clegg e Watson, *Cálculo*, vol. 2, 9ª ed., seção 14.2). Conferido com SymPy.

Calcular $\lim_{(x,y)\to(0,0)} \dfrac{xy}{x^2 + y^2}$ (o limite de xy/(x^2+y^2) na origem). A função não está definida em (0, 0).

1. Eixos: em y = 0, $f = 0$; em x = 0, $f = 0$. Os dois dão 0, mas isso **não prova** nada.
2. Retas $y = mx$ ($x \ne 0$): $f = \dfrac{m x^2}{x^2 + m^2x^2} = \dfrac{m}{1 + m^2}$, constante ao longo de cada reta. Com m = 1 vale 1/2; com m = 0 vale 0.
3. Dois caminhos, dois valores (0 e 1/2): o limite **não existe**.

Em coordenadas polares: $f = \cos\theta\operatorname{sen}\theta = \tfrac12\operatorname{sen}2\theta$, que depende só do ângulo θ e não de r: cada reta pela origem tem seu valor.

Comparação com a AB2 2024.1 (questão 1): $\dfrac{xy}{\sqrt{x^2+y^2}}$ tem limite 0, porque o denominador tem grau 1 e $|f| \le |x|$ (Teorema do Confronto). A diferença está no grau: numerador de grau 2 sobre denominador de grau 2 (este caso) pode depender da direção; grau 2 sobre grau 1 tende a zero.

**Verificação:** em $(10^{-6}, 10^{-6})$, $f = 10^{-12}/(2\cdot10^{-12}) = 0{,}5$; em $(10^{-6}, 0)$, $f = 0$: pontos igualmente próximos da origem, valores diferentes.
