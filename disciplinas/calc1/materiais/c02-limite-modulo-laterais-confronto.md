---
id: calc1-limite-modulo-confronto
titulo: Limites laterais com módulo (|x − 5|/(x − 5)) e Teorema do Confronto (|f(x) − 3| ≤ 2|x − 1|)
assunto: calc1-01-funcoes-inequacoes-modulo
tipo: prova
questao: 1a, 1b
semestre: 2015.2
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | Avaliação Final (03.12.2015), Q1a e Q1b; Exercícios resolvidos (aula de 17.02.2017), Q5
fontes_catalogo: ufal-im-calc1-provas-pdf,ufal-calc1-aula-distancia-2017
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

**Módulo pede limites laterais.** $|x - 5| = x - 5$ se $x \ge 5$ e $|x - 5| = -(x - 5)$ se $x < 5$.
- $x \to 5^+$: $\dfrac{|x - 5|}{x - 5} = 1$, limite 1.
- $x \to 5^-$: $\dfrac{|x - 5|}{x - 5} = -1$, limite −1.
- Laterais diferentes: $\lim_{x\to5} \dfrac{|x-5|}{x-5}$ **não existe**.

**Confronto.** Se $|f(x) - 3| \le 2|x - 1|$ para todo x, então $3 - 2|x - 1| \le f(x) \le 3 + 2|x - 1|$. As duas pontas tendem a 3 quando $x \to 1$, logo $\lim_{x\to1} f(x) = 3$ (Teorema do Confronto, ou do sanduíche).

**Confronto com função limitada (aula de 2017).** $\lim_{x\to-\pi^+} 3^{\operatorname{tg}(x/2)}\operatorname{sen} x$: quando $x \to -\pi^+$, $x/2 \to -\tfrac{\pi}{2}^+$, $\operatorname{tg}(x/2) \to -\infty$ e $3^{\operatorname{tg}(x/2)} \to 0^+$. Como $-1 \le \operatorname{sen} x \le 1$, o produto fica entre $\pm 3^{\operatorname{tg}(x/2)}$: o limite é 0. A resolução da aula foi conferida e está certa.

Erro comum: "cancelar" $|x - 5|$ com $x - 5$ sem separar os lados.

**Verificação:** numericamente, $x = 5{,}001$ dá 1 e $x = 4{,}999$ dá −1; $3^{\operatorname{tg}(-1{,}57)} \approx 0$.
