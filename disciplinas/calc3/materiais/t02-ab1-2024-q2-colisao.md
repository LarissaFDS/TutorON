---
id: calc3-ab1-2024-q2-colisao
titulo: AB1 2024.1, Q2 — duas partículas (elipse e circunferência): equações cartesianas, sentido e ponto de colisão
assunto: calc3-01-curvas-parametricas
tipo: prova
questao: 2
semestre: 2024.1
resolucao: sim
fonte: Prova.jpg (página do Notion "Cálculo 3", seção Provas antigas) | AB1 de 23/08/2024
autoria: Enunciado: Prof. Tiago Alves de Almeida (ECOM017 Cálculo 3, IC/UFAL, AB1 2024.1), parafraseado pela equipe TutorON; resolução da equipe TutorON
licenca: Não declarada (material de turma); a foto não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
fontes_catalogo: ufal-calc3-provas-2024-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
AB1 de Cálculo 3 (2024.1), Questão 2. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (sem gabarito no material; resolução da equipe TutorON, conferida com SymPy).

Dados: partícula $P_1$: $x = 3\operatorname{sen} t$, $y = 2\cos t$; partícula $P_2$: $x = -3 + \cos t$, $y = 1 + \operatorname{sen} t$; $0 \le t \le 2\pi$. Colisão = mesmo ponto no **mesmo** instante t.

a) Equações cartesianas (eliminar o parâmetro com $\operatorname{sen}^2 t + \cos^2 t = 1$):
- $P_1$: $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$, elipse centrada na origem, semieixos 3 (em x) e 2 (em y). Em t = 0 está em (0, 2); em $t = \pi/2$, em (3, 0): percorre a elipse no sentido **horário**, uma volta.
- $P_2$: $(x + 3)^2 + (y - 1)^2 = 1$, circunferência de centro (−3, 1) e raio 1. Em t = 0 está em (−2, 1); em $t = \pi/2$, em (−3, 2): sentido **anti-horário**, uma volta.
Descrição da figura: a circunferência fica à esquerda, tocando a região da elipse perto de (−3, 0).

b) Colisão: resolver $3\operatorname{sen} t = -3 + \cos t$ e $2\cos t = 1 + \operatorname{sen} t$ juntos. Em $t = 3\pi/2$: $P_1 = (-3, 0)$ e $P_2 = (-3 + 0,\ 1 - 1) = (-3, 0)$. É a única solução em $[0, 2\pi]$ (conferido numericamente). As curvas podem se cruzar em outro ponto sem colisão, se as partículas passam por ele em instantes diferentes: por isso a condição é sobre o mesmo t.

Resposta: colidem uma vez, no ponto (−3, 0), em $t = 3\pi/2$.

**Verificação:** (−3, 0) satisfaz $9/9 + 0 = 1$ (elipse) e $0 + (−1)^2 = 1$ (circunferência).
