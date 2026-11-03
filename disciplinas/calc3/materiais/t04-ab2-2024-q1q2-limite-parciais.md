---
id: calc3-ab2-2024-q1q2-limite-parciais
titulo: AB2 2024.1, Q1 e Q2 — limite de xy/√(x²+y²) na origem por caminhos e confronto; derivadas parciais de x/y pela definição
assunto: calc3-08-limites-derivadas-parciais
tipo: prova
questao: 1 e 2
semestre: 2024.1
resolucao: sim
fonte: foto da AB2 (página do Notion "Cálculo 3", seção Provas antigas) | AB2 de 22/11/2024
autoria: Enunciado: Prof. Tiago Alves de Almeida (ECOM017 Cálculo 3, IC/UFAL, AB2 2024.1), parafraseado pela equipe TutorON; resolução da equipe TutorON
licenca: Não declarada (material de turma); a foto não está no repositório (mostra o nome de um aluno)
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
fontes_catalogo: ufal-calc3-provas-2024-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
AB2 de Cálculo 3 (2024.1), Questões 1 e 2. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (sem gabarito no material; resolução da equipe TutorON, conferida com SymPy).

Questão 1. Calcular $\lim_{(x,y)\to(0,0)} \dfrac{xy}{\sqrt{x^2+y^2}}$ (o limite de xy sobre a raiz de x² + y² na origem). A prova sugere testar caminhos e depois o Teorema do Confronto.
- Caminhos: no eixo y ($x = 0$) a função vale 0; em $y = mx$, $f = \dfrac{m x^2}{|x|\sqrt{1+m^2}} \to 0$; em $y = \alpha x^2$, também $\to 0$. Todos dão 0, mas caminhos **não provam** que o limite existe; só indicam o candidato L = 0.
- Confronto: como $|y| \le \sqrt{x^2+y^2}$, vale $0 \le \left|\dfrac{xy}{\sqrt{x^2+y^2}}\right| \le |x|$, e $|x| \to 0$. Logo o limite existe e é 0.

Questão 2. Pela definição, derivadas parciais de $f(x,y) = x/y$ ($y \neq 0$).
- $f_x = \lim_{h\to0} \dfrac{(x+h)/y - x/y}{h} = \lim_{h\to0} \dfrac{h/y}{h} = \dfrac1y$.
- $f_y = \lim_{h\to0} \dfrac{x/(y+h) - x/y}{h} = \lim_{h\to0} \dfrac{-x h}{h\,y(y+h)} = \lim_{h\to0} \dfrac{-x}{y(y+h)} = -\dfrac{x}{y^2}$.

**Verificação:** pelas regras de derivação, $\partial(x/y)/\partial x = 1/y$ e $\partial(x/y)/\partial y = -x/y^2$; no limite, em coordenadas polares $|f| = r|\cos\theta\operatorname{sen}\theta| \le r \to 0$.
