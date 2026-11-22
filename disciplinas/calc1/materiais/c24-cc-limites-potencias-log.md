---
id: calc1-cc-limites-potencias-log
titulo: Limites com potência e logaritmo: (eˣ + x)^(1/x), (cos x)^(1/x), √x ln x, x ln(eˣ − 1), ln x/(x − √x)
assunto: calc1-09-lhospital
tipo: prova
questao: 4ª prova 2006, Q2; 4ª prova 2007, Q1
semestre: 2006–2007
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 4ª prova (19.08.2006), Q2; 4ª prova (07.07.2007), Q1
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

**Potência com variável no expoente** ($1^\infty$, $0^0$, $\infty^0$): escreva $L=\lim f^g$, tome $\ln L=\lim g\ln f$, resolva esse limite (em geral vira $\tfrac00$) e só no fim faça $L=e^{\ln L}$. Esquecer de voltar da exponencial é o erro mais comum.

- $\lim_{x\to0^+}(e^x+x)^{1/x}$: $\ln L=\lim\dfrac{\ln(e^x+x)}{x}$ (0/0); L'Hospital dá $\dfrac{e^x+1}{e^x+x}\to2$, logo $L=e^2$.
- $\lim_{x\to0}(\cos x)^{1/x}$: $\ln L=\lim\dfrac{\ln\cos x}{x}$; L'Hospital dá $-\operatorname{tg}x\to0$, logo $L=e^0=1$.

**Produto $0\cdot\infty$:** passe um fator para o denominador. Ex.: o limite de raiz de x vezes ln x quando x tende a zero pela direita:
- $\lim_{x\to0^+}\sqrt x\,\ln x=\lim\dfrac{\ln x}{x^{-1/2}}$ ($\infty/\infty$) $=\lim\dfrac{1/x}{-\tfrac12x^{-3/2}}=\lim(-2\sqrt x)=0$.
- $\lim_{x\to0^+}x\ln(e^x-1)$: perto de 0, $e^x-1\approx x$, e o limite se comporta como $x\ln x\to0$. Por L'Hospital: $\dfrac{\ln(e^x-1)}{1/x}$ dá $\dfrac{-x^2e^x}{e^x-1}\to0$.

**Quociente 0/0:** $\lim_{x\to1}\dfrac{\ln x}{x-\sqrt x}$: L'Hospital dá $\dfrac{1/x}{1-\tfrac{1}{2\sqrt x}}\to\dfrac{1}{1/2}=2$.

Antes de aplicar L'Hospital, confirme a forma indeterminada substituindo o ponto; se não for $\tfrac00$ nem $\tfrac\infty\infty$, a regra não vale.

**Verificação:** os cinco limites foram recalculados com sympy.limit (e², 1, 0, 0 e 2).
