---
id: calc1-limites-algebricos
titulo: Limites com forma indeterminada 0/0 por fatoração e racionalização: raiz cúbica, diferença de frações, ⁵√x e ∛x
assunto: calc1-02-limites-continuidade
tipo: prova
questao: vários
semestre: 2014–2017
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 1ª Avaliação (05.04.2014), Q1a e Q2a; 1ª Avaliação (30.08.2014), Q5b; Exercícios resolvidos (aula de 17.02.2017), Q6 e Q7
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-calc1-aula-distancia-2017
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

Roteiro: substitua primeiro. Se der $\tfrac{0}{0}$ (forma indeterminada), fatore, racionalize ou troque a variável para cancelar o fator que zera; L'Hospital costuma não ser permitido nessas provas.

- $\lim_{x\to0}\dfrac{\sqrt[3]{ax+1}-1}{x}$: com $u = \sqrt[3]{ax+1}$, $x = \tfrac{u^3-1}{a}$ e $\dfrac{u-1}{(u^3-1)/a} = \dfrac{a}{u^2+u+1} \to \dfrac{a}{3}$.
- $\lim_{x\to10}\left(\dfrac{1}{x-10}-\dfrac{20}{x^2-100}\right)$ (forma $\infty - \infty$): denominador comum, $\dfrac{x+10-20}{(x-10)(x+10)} = \dfrac{1}{x+10} \to \dfrac{1}{20}$.
- $\lim_{x\to1}\dfrac{\sqrt[5]{x}-1}{\sqrt[3]{x}-1}$: com $x = t^{15}$, $\dfrac{t^3-1}{t^5-1} \to \dfrac{3}{5}$.
- $\lim_{x\to1}\dfrac{\sqrt[3]{x}-1}{\sqrt{x}-1} = \lim \dfrac{\sqrt x + 1}{\sqrt[3]{x^2}+\sqrt[3]{x}+1} = \dfrac{2}{3}$ (diferença de cubos e de quadrados; resolução da aula conferida).
- Maior inteiro: $\lim_{x\to2^+}\left(\dfrac{[\![x]\!]}{[\![-x]\!]}+\dfrac{[\![-x]\!]}{[\![x]\!]}\right)$. Para $2 < x < 3$, $[\![x]\!] = 2$ e $[\![-x]\!] = -3$: resultado $-\tfrac{2}{3}-\tfrac{3}{2} = -\tfrac{13}{6}$ (resolução da aula conferida).

Erro comum: com maior inteiro ou módulo, esquecer que só vale o limite **lateral** pedido.

**Verificação:** $x = 10{,}001$ dá $\approx 0{,}04999$; $x = 1{,}0001$ no quociente de raízes dá $\approx 0{,}6000$.
