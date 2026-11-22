---
id: calc1-diferenciabilidade
titulo: Diferenciabilidade: |x − 5| + |x + 8|, função com |f(x)| ≤ x², função por partes com eˣ e |x − 1|·log₃x
assunto: calc1-04-derivada-definicao-tangente
tipo: prova
questao: vários
semestre: 2014–2015
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 2ª Avaliação (10.05.2014), Q1a e Q1b; 2ª Avaliação (04.10.2014), Q1a; Avaliação Final (03.12.2015), Q3b; resolução manuscrita da 2ª Avaliação (10.05.2014)
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-im-calc1-provas-pdf,ufal-calc1-resolucoes-manuscritas
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

Diferenciável em a: os limites laterais do quociente $\tfrac{f(a+h)-f(a)}{h}$ existem e são iguais. Diferenciável implica contínua (a recíproca é falsa).

- $f(x) = |x-5| + |x+8|$: em $x = 5$, derivada lateral direita $1 + 1 = 2$ e esquerda $-1 + 1 = 0$: não é diferenciável. Em $x = -8$: direita $0$, esquerda $-2$. f é diferenciável em $(-\infty,-8)\cup(-8,5)\cup(5,\infty)$ (a resolução manuscrita chega ao mesmo conjunto).
- $|f(x)| \le x^2$ dá $f(0) = 0$ e $\left|\tfrac{f(h)}{h}\right| \le |h| \to 0$: pelo confronto, $f'(0) = 0$.
- $f(x) = 1$ se $e^x \le 1$ (isto é, $x \le 0$) e $e^x$ se $x > 0$: contínua em 0, mas derivada à esquerda 0 e à direita $e^0 = 1$: não é diferenciável em 0.
- $f(x) = |x-1|\log_3 x$ em $x = 1$: $\dfrac{f(1+h)}{h} = \dfrac{|h|}{h}\log_3(1+h) \to 0$ pelos dois lados, então $f'(1) = 0$ (o fator $\log_3 x$ zera e "salva" o bico do módulo).

Erro comum: derivar cada pedaço e comparar só os valores da função, sem comparar as derivadas laterais.

**Verificação:** numericamente, $\tfrac{f(5+h)-f(5)}{h}$ com $h = \pm10^{-6}$ dá 2 e 0; para $|x-1|\log_3 x$, dá $\pm 9\cdot10^{-7}$, perto de 0.
