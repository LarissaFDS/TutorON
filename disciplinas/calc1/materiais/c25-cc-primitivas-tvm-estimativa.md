---
id: calc1-cc-primitivas-tvm-estimativa
titulo: Achar f a partir de f'' ou f''' com condições (ponto de máximo inconsistente no enunciado) e estimar f(4) pelo TVM
assunto: calc1-11-primitivas-integral
tipo: prova
questao: 4ª prova 2006, Q3 e Q4; 4ª prova 2007, Q5
semestre: 2006–2007
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 4ª prova (19.08.2006), Q3 e Q4; 4ª prova (07.07.2007), Q5
curso: Ciência da Computação (UFAL), banco de questões da turma (provas do IM-UFAL aplicadas a vários cursos)
fontes_catalogo: ufal-cc-calc1-banco-provas
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL, parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova); PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: corrigida (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

**Uma constante por integração.** Use cada condição na etapa certa.
- $f''(x)=x+\operatorname{sen}x$, $f'(\pi/2)=\pi^2/4$, $f(0)=\pi^2/16$: $f'(x)=\tfrac{x^2}2-\cos x+C$ e $C=\pi^2/8$; $f(x)=\tfrac{x^3}6-\operatorname{sen}x+\tfrac{\pi^2}{8}x+\tfrac{\pi^2}{16}$, então $f(\pi)=\tfrac{7\pi^3}{24}+\tfrac{\pi^2}{16}$.
- $f'(x)=x^3$ com tangente $y=-x$: o ponto de tangência tem $f'(a)=-1$, logo $a=-1$ e $f(-1)=1$ (está na reta). $f(x)=\tfrac{x^4}4+\tfrac34$.
- $f'(x)=\dfrac{1+x}{\sqrt x}=x^{-1/2}+x^{1/2}$, $f(1)=0$: $f(x)=2\sqrt x+\tfrac23x^{3/2}-\tfrac83$.

**$y'''=2-6x$, com $(0,2)$ ponto de máximo local e $(1,31/12)$ ponto de inflexão.** As condições são $y(0)=2$, $y'(0)=0$ e $y''(1)=0$. Dá $y''=-3x^2+2x+1$ e $y=-\tfrac{x^4}4+\tfrac{x^3}3+\tfrac{x^2}2+2$, e $y(1)=31/12$ confere.

**Divergência:** $y''(0)=1>0$, então $(0,2)$ é **mínimo** local, não máximo. **Correções da equipe:** com as outras condições, nenhuma função tem máximo em (0, 2); o tutor deve mostrar a conta de $y''(0)$ e dizer que o enunciado tem um erro.

**Estimativa pelo TVM:** f contínua em [1, 4], derivável em (1, 4), $f(1)=2$ e $2\le f'(x)\le3$. Pelo TVM, $f(4)-f(1)=3f'(c)$, logo $8\le f(4)\le11$.

**Verificação:** as primitivas e as constantes foram recalculadas com SymPy (integrate e solve), que também confirmou $y''(0)=1$.
