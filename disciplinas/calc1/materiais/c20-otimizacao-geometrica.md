---
id: calc1-otimizacao-geometrica
titulo: Otimização geométrica: cilindro de volume máximo inscrito num cone, calha de chapa de 60 cm (ângulo θ, anotação π/4 corrigida), cone máximo numa esfera, arame dividido em círculo e quadrado
assunto: calc1-10-otimizacao
tipo: prova
questao: vários
semestre: 2015–2016
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 4ª prova (foto), Q4b (calha); Avaliação Final (03.12.2015), Q9; Quarto Simulado (04.05.2016), Q3b; 4ª lista de Cálculo 1, Engenharia Ambiental 2016.2, Q5
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-im-calc1-provas-pdf,ufal-calc1-listas-simulados
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL (professor não impresso nas provas), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: corrigida (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

**Roteiro:** variável e domínio; função objetivo com **uma** variável (use a restrição); números críticos; compare com as extremidades (ou use o teste da 2ª derivada) para garantir que é máximo ou mínimo absoluto.

- **Cilindro inscrito num cone** de altura H e raio R. Semelhança: $h = H\left(1 - \tfrac{r}{R}\right)$, $V(r) = \pi H\left(r^2 - \tfrac{r^3}{R}\right)$, $0 \le r \le R$. $V'(r) = \pi H\left(2r - \tfrac{3r^2}{R}\right) = 0$ dá $r = \tfrac{2R}{3}$, $h = \tfrac{H}{3}$, $V = \tfrac{4\pi R^2H}{27}$. Nas pontas $V = 0$: é o máximo.
- **Calha:** fundo de 20 cm e lados de 20 cm inclinados de θ. Seção trapezoidal: $A(\theta) = 400\operatorname{sen}\theta(1 + \cos\theta)$, $0 \le \theta \le \tfrac{\pi}{2}$. $A' = 400(\cos\theta + \cos2\theta) = 0$ dá $2\cos^2\theta + \cos\theta - 1 = 0$, $\cos\theta = \tfrac12$, $\theta = \tfrac{\pi}{3}$, $A = 300\sqrt3$ cm².
- **Divergência.** Na foto da prova há a anotação manuscrita "π/4" ao lado da questão. **Correções da equipe:** $A(\tfrac{\pi}{4}) = 200\sqrt2 + 200 \approx 482{,}8 < A(\tfrac{\pi}{3}) \approx 519{,}6$; o ângulo ótimo é $\tfrac{\pi}{3}$ (60°).
- **Cone de volume máximo dentro de esfera de raio R:** $r^2 = h(2R - h)$, $V = \tfrac{\pi}{3}h^2(2R - h)$, $h = \tfrac{4R}{3}$, $V = \tfrac{32\pi R^3}{81}$.
- **Arame de comprimento l** (x para o círculo): $A(x) = \tfrac{x^2}{4\pi} + \left(\tfrac{l-x}{4}\right)^2$; mínimo em $x = \tfrac{\pi l}{\pi + 4}$; máximo na extremidade $x = l$ (só círculo).

**Verificação:** $V(2R/3) = 4\pi R^2H/27$ com $R = 3$, $H = 9$: $V(2) = 12\pi$; $A(\pi/3) = 400\cdot\tfrac{\sqrt3}{2}\cdot\tfrac32$.
