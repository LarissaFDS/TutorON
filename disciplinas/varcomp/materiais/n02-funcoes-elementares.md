---
id: varcomp-nota-ia-funcoes-elementares
titulo: Nota — exponencial, logaritmo e potências complexas: log z multivalente, Log principal, ramo, i^i
assunto: varcomp-03-funcoes-elementares
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON escrita com IA (não é material do professor)
autoria: Equipe TutorON (rascunho gerado por IA); revisão humana pendente
licenca: Texto próprio da equipe
publicacao_transcricao: não se aplica
fontes_catalogo: beck-first-course-complex-analysis,mit-ocw-1804-2018
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Rascunho escrito por IA, aguardando revisão humana; fora da busca. Contas conferidas com SymPy em `tests_acervo/test_disciplina_varcomp.py`.

**Exponencial:** $e^{x + iy} = e^x(\cos y + i\sin y)$; é periódica de período $2\pi i$ e nunca é zero.

**Logaritmo:** os valores de $\log z$ ($z \neq 0$) são $\ln|z| + i(\operatorname{Arg} z + 2k\pi)$, k inteiro. O **logaritmo principal** usa $\operatorname{Arg} z \in (-\pi, \pi]$: $\operatorname{Log} z = \ln|z| + i\operatorname{Arg} z$. Ele é analítico fora do semieixo real negativo (o corte do ramo) e $(\operatorname{Log} z)' = 1/z$ ali.

Exemplo: $\operatorname{Log}(-1) = i\pi$; $\log(-1) = i(\pi + 2k\pi)$.

**Potências complexas:** $z^c = e^{c\log z}$, multivalente em geral. Exemplo: $i^i = e^{i\log i} = e^{i\cdot i(\pi/2 + 2k\pi)} = e^{-\pi/2 - 2k\pi}$, todos reais; o valor principal é $e^{-\pi/2} \approx 0{,}2079$. Se $c = 1/n$, há exatamente n valores: as raízes n-ésimas.

**Trigonométricas:** $\cos z = (e^{iz} + e^{-iz})/2$ e $\sin z = (e^{iz} - e^{-iz})/(2i)$; não são limitadas: $\cos(iy) = \cosh y$.

**Verificação:** $e^{\operatorname{Log}(-1)} = e^{i\pi} = -1$; $\cos^2 z + \sin^2 z = 1$ continua valendo (SymPy).
