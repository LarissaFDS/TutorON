---
id: calc1-tvm-rolle
titulo: O que diz o Teorema do Valor Médio (TVM) e o Teorema de Rolle, hipóteses e usos: (x + 8)/(2x − 4) em (0, 4), raízes de x⁴/4 + 8x + arctg 10, f'' < 0 dá f(x) ≤ 2x + 1, tg c > c, ponto fixo, f' ≤ 5
assunto: calc1-07-extremos-tvm
tipo: prova
questao: vários
semestre: 2013–2016
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 3ª Avaliação (01.11.2014), Q5a e Q5b; 4ª prova (foto), Q3b e Q5a; 4ª Avaliação (16.03.2013), Q3b; Avaliação Final (03.12.2015), Q2b
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-im-calc1-provas-pdf
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL (professor não impresso nas provas), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: pendente de confirmação do professor (resolução da equipe TutorON, conferida com SymPy; depende da leitura do enunciado).

O que diz o Teorema do Valor Médio? **TVM:** f contínua em $[a,b]$ e derivável em $(a,b)$ ⇒ existe c com $f'(c) = \dfrac{f(b)-f(a)}{b-a}$. Rolle é o caso $f(a) = f(b)$. **Confira as duas hipóteses antes de usar.**

- $f(x) = \dfrac{x+8}{2x-4}$ em $[0, 4]$: $\tfrac{f(4)-f(0)}{4} = \tfrac{3-(-2)}{4} = \tfrac54$, mas $f'(x) = -\dfrac{20}{(2x-4)^2} < 0$. Não há c, e isso não contradiz o TVM: f não é contínua em $x = 2$.
- $f(x) = \tfrac{x^4}{4} + 8x + \operatorname{arctg}10$ tem no máximo duas raízes: se tivesse três, Rolle daria duas raízes de $f'(x) = x^3 + 8$, que só zera em $x = -2$.
- $f'' < 0$, $f'(0) = 2$, $f(0) = 1$: $g(x) = f(x) - (2x + 1)$ tem $g(0) = 0$, $g'(0) = 0$ e $g'$ decrescente, então g cresce até 0 e decresce depois: $g \le 0$, isto é, $f(x) \le 2x + 1$ (gráfico côncavo abaixo da tangente).
- $\operatorname{tg}c > c$ em $(0, \tfrac{\pi}{2})$: TVM em $[0, c]$ dá $\operatorname{tg}c = c\sec^2\xi > c$.
- Ponto fixo: se $f'(x) \ne 1$ sempre e $f(a) = a$, $f(b) = b$ com $a \ne b$, o TVM daria $f'(\xi) = 1$. Absurdo: no máximo um ponto fixo.

**Pendência.** "Existe f derivável com $f' \le 5$, $f(2) = -1$, $f(4) = 10$, restrita a $(2, 4)$?" Se f for contínua em $[2,4]$, não: o TVM exigiria $f'(c) = \tfrac{11}{2} > 5$. Como o enunciado fala no intervalo **aberto**, a resposta depende de f ser contínua nas pontas; confirmar com o professor.

**Verificação:** $f(0) = -2$, $f(4) = 3$; $x^3 + 8$ tem uma raiz real; $\operatorname{tg}1 \approx 1{,}557 > 1$.
