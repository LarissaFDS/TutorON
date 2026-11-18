---
id: calc3-reav-2024-q1q2-limite-parciais
titulo: Reavaliação 2024.1, Q1 e Q2 — limite de x³y/(x⁶+2y²) que não existe (caminho y = x³); derivadas parciais pela definição
assunto: calc3-08-limites-derivadas-parciais
tipo: prova
questao: 1 e 2
semestre: 2024.1
resolucao: sim
fonte: foto da reavaliação (página do Notion "Cálculo 3", seção Provas antigas) | reavaliação de 26/11/2024
autoria: Enunciado: Prof. Tiago Alves de Almeida (ECOM017 Cálculo 3, IC/UFAL, reavaliação 2024.1), parafraseado pela equipe TutorON; resolução da equipe TutorON
licenca: Não declarada (material de turma); a foto não está no repositório (mostra o nome de um aluno)
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
fontes_catalogo: ufal-calc3-provas-2024-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Reavaliação de Cálculo 3 (2024.1), Questões 1 e 2. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (sem gabarito no material; resolução da equipe TutorON, conferida com SymPy).

Questão 1. $\lim_{(x,y)\to(0,0)} \dfrac{x^3 y}{x^6 + 2y^2}$.
- Retas $y = mx$: $f = \dfrac{m x^4}{x^6 + 2m^2x^2} = \dfrac{m x^2}{x^4 + 2m^2} \to 0$.
- Curva $y = x^3$ (escolhida para igualar os graus de $x^6$ e $y^2$): $f = \dfrac{x^6}{x^6 + 2x^6} = \dfrac13$.
- Dois caminhos com valores diferentes (0 e 1/3): o limite **não existe**. Todas as retas darem 0 não basta.

Questão 2. Derivadas pela definição (quociente de Newton).
a) $f(x,y) = \dfrac{x}{x+y^2}$, derivada em x: $\dfrac{f(x+h,y) - f(x,y)}{h} = \dfrac{1}{h}\left[\dfrac{x+h}{x+h+y^2} - \dfrac{x}{x+y^2}\right] = \dfrac{y^2}{(x+h+y^2)(x+y^2)}$, então $f_x = \dfrac{y^2}{(x+y^2)^2}$ (onde $x + y^2 \neq 0$).
b) $g(x,y) = xy^2 - x^3y$, derivada em y: $\dfrac{g(x,y+h) - g(x,y)}{h} = \dfrac{x(2yh + h^2) - x^3 h}{h} = 2xy + xh - x^3 \to 2xy - x^3$.

**Verificação:** pelas regras, $\partial_x[x/(x+y^2)] = [(x+y^2) - x]/(x+y^2)^2 = y^2/(x+y^2)^2$ e $\partial_y(xy^2 - x^3y) = 2xy - x^3$.
