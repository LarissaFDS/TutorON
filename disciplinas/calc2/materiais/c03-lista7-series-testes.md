---
id: calc2-lista7-series-soma-integral-comparacao
titulo: Lista 7 (Profa. Xu Yang) — séries telescópicas e geométricas com soma, teste da divergência, teste da integral e teste da comparação
assunto: calc2-03-series-convergencia
tipo: exercicio_resolvido
resolucao: sim
fonte: Lista 7 de Cálculo 2 (Profa. Xu Yang, UFAL), PDF do material do 2º período de Engenharia de Computação | enunciados parafraseados
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
Cálculo 2, Lista 7 (convergência de séries). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Antes de tudo, o teste da divergência:** se $a_n \not\to 0$, a série diverge. Ex.: no item (a), o termo é um quociente de dois polinômios de grau 1 em $n$ (coeficientes líderes 1 e 2) e tende a $\tfrac12$, então a série diverge. O contrário não vale: $a_n \to 0$ não garante convergência.

**Somas que dá para calcular:**
- Telescópica: $\sum_{n\ge1}(e^{1/n} - e^{1/(n+1)})$; a soma parcial é $e - e^{1/(N+1)} \to e - 1$.
- Frações parciais: $\tfrac{2}{n^2+4n+3} = \tfrac{1}{n+1} - \tfrac{1}{n+3}$; sobram $\tfrac12 + \tfrac13$, soma $\tfrac56$.
- Geométrica: $\sum_{k\ge1}(\cos 1)^k$, razão $r = \cos 1 \approx 0{,}54$, $|r| < 1$: soma $\tfrac{\cos 1}{1 - \cos 1}$. (Na lista o índice aparece como $n$ e o expoente como $k$: leia tudo com a mesma letra.)

**Teste da integral** ($f$ positiva, contínua e decrescente): $\sum\tfrac{1}{(2n+1)^3}$ e $\sum n e^{-n}$ convergem; $\sum\tfrac{1}{n\ln n}$ diverge ($\int\tfrac{dx}{x\ln x} = \ln(\ln x) \to \infty$); $\sum\tfrac{1}{n^2+4n+5}$ converge.

**Comparação:** $\tfrac{1}{n^2+n+1} < \tfrac{1}{n^2}$ (converge); $\tfrac{1}{n!} \le \tfrac{1}{2^{n-1}}$ (converge); $\text{sen}(1/n)$ se compara no limite com $1/n$ (razão $\to 1$; diverge); $\tfrac{2+(-1)^n}{n\sqrt n} \le \tfrac{3}{n^{3/2}}$ (converge, série $p$ com $p = 3/2$).

Erro comum: concluir convergência só porque o termo vai a zero ($\sum 1/n$ diverge).

**Verificação:** somas, integrais e limites conferidos com SymPy em `test_lista7_series`.
