---
id: calc1-funcoes-hiperbolicas
titulo: Funções hiperbólicas, derivada do seno hiperbólico e do cosseno hiperbólico: (cosh x − senh x)ⁿ = cosh nx − senh nx, sec θ = cosh x, f'' = senh x, tangente a senh[x + cosh(x − 1)], retângulo sobre 5 tgh x
assunto: calc1-05-regras-derivacao
tipo: prova
questao: vários
semestre: 2014–2016
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 2ª prova Verão 2015, Q3b, Q4a; 4ª prova (foto), Q3b; 3ª Avaliação (01.11.2014), Q3a; Avaliação Final (03.12.2015), Q7a; 4ª lista de Cálculo 1, Engenharia Ambiental 2016.2, Q7
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-im-calc1-provas-pdf,ufal-calc1-listas-simulados
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL (professor não impresso nas provas), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

A derivada do seno hiperbólico é o cosseno hiperbólico, e a do cosseno hiperbólico é o seno hiperbólico (sem sinal de menos).

Definições: $\operatorname{senh}x = \dfrac{e^x - e^{-x}}{2}$, $\cosh x = \dfrac{e^x + e^{-x}}{2}$, $\cosh^2x - \operatorname{senh}^2x = 1$, $(\operatorname{senh}x)' = \cosh x$, $(\cosh x)' = \operatorname{senh}x$.

- **Identidade.** $\cosh x - \operatorname{senh}x = e^{-x}$, então $(\cosh x - \operatorname{senh}x)^n = e^{-nx} = \cosh(nx) - \operatorname{senh}(nx)$.
- **$x = \ln(\sec\theta + \operatorname{tg}\theta)$.** $e^x = \sec\theta + \operatorname{tg}\theta$ e $e^{-x} = \sec\theta - \operatorname{tg}\theta$ (pois $\sec^2 - \operatorname{tg}^2 = 1$); somando e dividindo por 2, $\cosh x = \sec\theta$.
- **$f''(x) = \operatorname{senh}x$, $f'(0) = 2$, $f(0) = 3$.** $f'(x) = \cosh x + 1$, $f(x) = \operatorname{senh}x + x + 3$. Gráficos de f e f'' se cortam onde $x + 3 = 0$: a reta paralela ao eixo y é $x = -3$.
- **$f(x) = \operatorname{senh}[x + \cosh(x-1)]$ em $x = 1$.** $f(1) = \operatorname{senh}2$; $f'(x) = \cosh[x+\cosh(x-1)]\,(1 + \operatorname{senh}(x-1))$, $f'(1) = \cosh2$. Tangente $y = \operatorname{senh}2 + \cosh2\,(x - 1)$; corta o eixo y em $\operatorname{senh}2 - \cosh2 = -e^{-2}$ e o eixo x em $1 - \operatorname{tgh}2 = \dfrac{2}{e^4+1}$. Área do triângulo com a origem: $\dfrac{e^{-2}}{e^4+1}$.
- **Retângulo sobre $y = 5\operatorname{tgh}x$ com abscissa $\ln2$.** $\operatorname{tgh}(\ln2) = \dfrac{2 - 1/2}{2 + 1/2} = \dfrac35$, vértice $(\ln2, 3)$; vértices simétricos $(\pm\ln2, \pm3)$; área $12\ln2$.

**Verificação:** $f(-3) = \operatorname{senh}(-3) = f''(-3)$; numericamente, área $\approx 0{,}0025$.
