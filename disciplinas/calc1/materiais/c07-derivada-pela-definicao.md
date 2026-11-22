---
id: calc1-derivada-pela-definicao
titulo: Como derivar pela definição (limite do quociente de Newton) e achar a reta tangente: f(x) = √(2x + 1), √(2x² + 4x), 1/√(x + 2) e (2x + 1)/(3x − 2)
assunto: calc1-04-derivada-definicao-tangente
tipo: prova
questao: vários
semestre: 2012–2014
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 1ª Avaliação (05.04.2014), Q3b; Reavaliação AB1 (11.07.2014), Q5b; 1ª prova (15.12.2012), Q5a; 1ª prova Adventistas (14.12.2012), Q5a
fontes_catalogo: ufal-im-calc1-provas-fotos
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

Como derivar uma função pela definição, por exemplo $\sqrt{2x+1}$: monte o limite do quociente e simplifique antes de fazer h tender a 0.

**Definição:** $f'(a) = \lim_{h\to0}\dfrac{f(a+h)-f(a)}{h}$ (forma 0/0). Tangente: $y = f(a) + f'(a)(x - a)$.

**Raiz: racionalize.** Para $f(x) = \sqrt{2x+1}$ (domínio $x \ge -\tfrac12$):
$$\frac{\sqrt{2x+2h+1}-\sqrt{2x+1}}{h}\cdot\frac{\sqrt{2x+2h+1}+\sqrt{2x+1}}{\sqrt{2x+2h+1}+\sqrt{2x+1}} = \frac{2}{\sqrt{2x+2h+1}+\sqrt{2x+1}} \to \frac{1}{\sqrt{2x+1}}.$$
Na prova de 2014, o ponto é $x = a$ com $a = \lim_{x\to3}\dfrac{x^3-27}{x^2-9} = \dfrac{9}{2}$: $f(\tfrac92) = \sqrt{10}$, $f'(\tfrac92) = \tfrac{1}{\sqrt{10}}$, tangente $y = \sqrt{10} + \tfrac{1}{\sqrt{10}}\left(x - \tfrac92\right)$.

- $f(x) = \sqrt{2x^2+4x}$ em $x = 2$: $f(2) = 4$; racionalizando, o quociente vira $\dfrac{4h+2h^2+8h}{h\,(\sqrt{\cdots}+4)} \to \dfrac{12}{8} = \dfrac32$. Tangente $y = 4 + \tfrac32(x - 2)$.
- $f(x) = \dfrac{1}{\sqrt{x+2}}$ em $x = 2$: $f(2) = \tfrac12$, $f'(2) = -\tfrac{1}{16}$, tangente $y = \tfrac12 - \tfrac{1}{16}(x-2)$.
- $f(x) = \dfrac{2x+1}{3x-2}$: $\dfrac{f(1+h)-f(1)}{h} = \dfrac{-7}{3h+1} \to -7$.

Erro comum: pular a racionalização e "substituir h = 0" em 0/0.

**Verificação:** a regra da cadeia dá $\tfrac{d}{dx}\sqrt{2x+1} = \tfrac{1}{\sqrt{2x+1}}$; numericamente, $\tfrac{f(4{,}501)-f(4{,}5)}{0{,}001} \approx 0{,}3162$.
