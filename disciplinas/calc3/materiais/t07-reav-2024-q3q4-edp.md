---
id: calc3-reav-2024-q3q4-edp
titulo: Reavaliação 2024.1, Q3 e Q4 — T = (x²+y²)^(−1/2) com T_xx + T_yy = T³; sen(Ax)e^(−Bt) na equação do calor
assunto: calc3-08-limites-derivadas-parciais
tipo: prova
questao: 3 e 4
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
Reavaliação de Cálculo 3 (2024.1), Questões 3 e 4. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (sem gabarito no material; resolução da equipe TutorON, conferida com SymPy).

Questão 3. Mostrar que $T(x,y) = (x^2+y^2)^{-1/2}$ (um sobre a distância à origem) satisfaz $T_{xx} + T_{yy} = T^3$, fora da origem.
- $T_x = -x(x^2+y^2)^{-3/2}$.
- $T_{xx} = -(x^2+y^2)^{-3/2} + 3x^2(x^2+y^2)^{-5/2} = \dfrac{2x^2 - y^2}{(x^2+y^2)^{5/2}}$.
- Por simetria, $T_{yy} = \dfrac{2y^2 - x^2}{(x^2+y^2)^{5/2}}$.
- Soma: $\dfrac{x^2 + y^2}{(x^2+y^2)^{5/2}} = (x^2+y^2)^{-3/2} = T^3$. ✔

Questão 4. Para que constantes $u(x,t) = \operatorname{sen}(Ax)\,e^{-Bt}$ satisfaz $u_t = u_{xx}$?
- $u_t = -B\operatorname{sen}(Ax)e^{-Bt}$; $u_{xx} = -A^2\operatorname{sen}(Ax)e^{-Bt}$.
- Igualdade para todo (x, t) ⇔ $B = A^2$ (se A = 0, u ≡ 0 e qualquer B serve; caso trivial).

**Verificação:** no ponto (1, 0), $T = 1$, $T_{xx} = 2$, $T_{yy} = -1$, soma 1 = $T^3$; com A = 1, B = 1, $u = \operatorname{sen}x\,e^{-t}$ dá $u_t = -u = u_{xx}$.
