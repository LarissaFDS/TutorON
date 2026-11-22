---
id: calc1-cc-esboco-x3-sobre-x2-menos-1
titulo: Esboço completo de f(x) = x³/(x² − 1): domínio, assíntotas vertical e oblíqua, crescimento, extremos, concavidade e inflexão
assunto: calc1-08-esboco-graficos
tipo: prova
questao: 4ª prova 2006, Q5; 4ª prova 2007, Q4
semestre: 2006–2007
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 4ª prova (19.08.2006), Q5; 4ª prova (07.07.2007), Q4
curso: Ciência da Computação (UFAL), banco de questões da turma (provas do IM-UFAL aplicadas a vários cursos)
fontes_catalogo: ufal-cc-calc1-banco-provas
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL, parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova); PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

Como esboçar o gráfico de x³/(x² − 1), que caiu nas duas provas: siga os passos para $f(x)=\dfrac{x^3}{x^2-1}$.

1. **Domínio:** $x\ne\pm1$. f é ímpar ($f(-x)=-f(x)$): o gráfico é simétrico em relação à origem. Único corte nos eixos: $(0,0)$.
2. **Assíntotas:** verticais $x=1$ e $x=-1$ ($f\to+\infty$ quando $x\to1^+$ e $-\infty$ quando $x\to1^-$). Não há horizontal. Dividindo, $f(x)=x+\dfrac{x}{x^2-1}$, então a **oblíqua** é $y=x$.
3. **Crescimento:** $f'(x)=\dfrac{x^2(x^2-3)}{(x^2-1)^2}$. Cresce em $(-\infty,-\sqrt3)$ e $(\sqrt3,\infty)$; decresce em $(-\sqrt3,-1)$, $(-1,1)$ e $(1,\sqrt3)$.
4. **Extremos:** máximo local em $x=-\sqrt3$, $f=-\tfrac{3\sqrt3}{2}$; mínimo local em $x=\sqrt3$, $f=\tfrac{3\sqrt3}2$. Em $x=0$, $f'=0$ mas o sinal não muda: não é extremo.
5. **Concavidade:** $f''(x)=\dfrac{2x(x^2+3)}{(x^2-1)^3}$. Para cima em $(-1,0)$ e $(1,\infty)$; para baixo em $(-\infty,-1)$ e $(0,1)$. Inflexão só em $(0,0)$ ($x=\pm1$ não estão no domínio).

Erros comuns: chamar $x=\pm1$ de inflexão, e dizer que $x=0$ é máximo ou mínimo só porque $f'(0)=0$.

**Verificação:** derivadas, sinais, limites laterais e a divisão para a oblíqua foram recalculados com SymPy.
