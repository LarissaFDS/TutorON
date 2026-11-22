---
id: calc1-primitivas-condicoes
titulo: Primitivas com condições: f'' = 6(x − 1) com tangente y = 3x − 5 em (2, 1); f' = 1 − 8/x³ com f(2) = 5; f'' = 2 − 4x por (−1, 3) e (0, 2); constante de integração
assunto: calc1-11-primitivas-integral
tipo: prova
questao: vários
semestre: 2015–2016
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | Avaliação Final (03.12.2015), Q6b; 4ª prova (foto), Q5a; prova (foto), Q4b
fontes_catalogo: ufal-im-calc1-provas-pdf,ufal-im-calc1-provas-fotos
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

**Primitiva:** F é primitiva de f se $F' = f$; a primitiva geral é $F(x) + C$ (num intervalo). Cada integração gera **uma constante**; cada condição dada fixa uma. Tabela básica: $\int x^n\,dx = \tfrac{x^{n+1}}{n+1} + C$ ($n \ne -1$), $\int \tfrac1x\,dx = \ln|x| + C$, $\int\cos x\,dx = \operatorname{sen}x + C$.

- $f''(x) = 6(x - 1)$, gráfico tangente a $y = 3x - 5$ em (2, 1): $f'(x) = 3(x-1)^2 + C_1$ e $f'(2) = 3$ dá $C_1 = 0$; $f(x) = (x-1)^3 + C_2$ e $f(2) = 1$ dá $C_2 = 0$. Resposta: $f(x) = (x - 1)^3$.
- $f'(x) = 1 - \dfrac{8}{x^3}$, $f(2) = 5$: $f(x) = x + \dfrac{4}{x^2} + C$, $2 + 1 + C = 5$, $C = 2$. Assíntotas: vertical $x = 0$ e oblíqua $y = x + 2$ (pois $\tfrac{4}{x^2} \to 0$); sem horizontal.
- $f''(x) = 2 - 4x$, gráfico por (−1, 3) e (0, 2): $f(x) = x^2 - \tfrac23x^3 + C_1x + C_2$; $C_2 = 2$ e $1 + \tfrac23 - C_1 + 2 = 3$ dá $C_1 = \tfrac23$. Com $g(x) = \tfrac{3x^2 - 2x^3}{3}$: $f - g = \tfrac23x + 2 = 0$ em $x = -3$, então os gráficos se cortam em $(-3, 27)$.

Erro comum: usar uma só constante para duas integrações, ou usar a condição de f na equação de f'.

**Verificação:** derive a primitiva obtida: $\tfrac{d}{dx}(x-1)^3 = 3(x-1)^2$ e $\tfrac{d^2}{dx^2} = 6(x-1)$; $f(-3) = g(-3) = 27$.
