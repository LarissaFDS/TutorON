---
id: calc1-regra-cadeia-tangente-horizontal
titulo: Regra da cadeia e tangente horizontal: y = 5^(sen²(2x + 3)), y = sen²(4x)/8 − sen²(3x)/6, ln|sec x + tg x| − x (resolução manuscrita corrigida)
assunto: calc1-05-regras-derivacao
tipo: prova
questao: vários
semestre: 2013–2014
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 2ª Avaliação (10.05.2014), Q2a; 2ª Avaliação (04.10.2014), Q3a; material de apoio "abscissas dos pontos da curva"; resolução manuscrita da 2ª Avaliação (10.05.2014)
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-calc1-dicas-apoio,ufal-calc1-resolucoes-manuscritas
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL (professor não impresso nas provas), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: corrigida (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

Tangente horizontal: $y' = 0$. Derive de fora para dentro, multiplicando por cada derivada interna (regra da cadeia).

**$y = 5^{\operatorname{sen}^2(2x+3)}$.** $y' = 5^{\operatorname{sen}^2(2x+3)}\ln5\cdot2\operatorname{sen}(2x+3)\cos(2x+3)\cdot2 = 2\ln5\,\operatorname{sen}(4x+6)\,5^{\operatorname{sen}^2(2x+3)}$. A exponencial nunca zera, então $\operatorname{sen}(4x+6) = 0$: $x = \dfrac{n\pi - 6}{4}$, n inteiro.

**Divergência.** A resolução manuscrita conclui que em todos esses pontos $y = 5$. Mas $2x + 3 = \tfrac{n\pi}{2}$ e $\operatorname{sen}^2(\tfrac{n\pi}{2})$ vale 1 para n ímpar e **0 para n par**.

**Correções da equipe.** Os pontos são $\left(\tfrac{n\pi-6}{4}, 5\right)$ com n ímpar (máximos) e $\left(\tfrac{n\pi-6}{4}, 1\right)$ com n par (mínimos).

**$y = \tfrac{\operatorname{sen}^2(4x)}{8} - \tfrac{\operatorname{sen}^2(3x)}{6} + \operatorname{sen}^{99}(99)$.** O último termo é constante. $y' = \operatorname{sen}4x\cos4x - \operatorname{sen}3x\cos3x = \tfrac12(\operatorname{sen}8x - \operatorname{sen}6x) = \cos7x\,\operatorname{sen}x$. Zeros: $x = k\pi$ ou $x = \tfrac{\pi}{14} + \tfrac{k\pi}{7}$.

**$f(x) = \ln|\sec x + \operatorname{tg} x| - x$, $-\pi \le x \le \pi$.** $f'(x) = \sec x - 1 = 0 \iff \cos x = 1 \iff x = 0$ (fora de $\pm\tfrac{\pi}{2}$, onde f não está definida).

**Verificação:** $n = 1$: $x = \tfrac{\pi-6}{4}$, $2x+3 = \tfrac{\pi}{2}$, $y = 5$; $n = 2$: $2x + 3 = \pi$, $y = 5^0 = 1$.
