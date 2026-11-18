---
id: calc3-ab1-2024-q1-projetil
titulo: AB1 2024.1, Q1 — projétil em curva paramétrica: ângulo de lançamento, altura máxima, pouso, tangente vertical
assunto: calc3-01-curvas-parametricas
tipo: prova
questao: 1
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
AB1 de Cálculo 3 (2024.1), Questão 1. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (a prova não tem gabarito no material; a resolução é da equipe TutorON, conferida com SymPy em `tests_acervo/test_disciplina_calc3.py`).

Dados: um projétil sai do solo com trajetória $x(t) = \tfrac14 t^3 + 2t$, $y(t) = bt - t^2$, $b > 0$, $t$ em segundos e distâncias em centímetros. A velocidade escalar inicial é $2\sqrt{101}$ cm/s.

a) Ângulo de lançamento e valor de b. Vetor velocidade: $\langle x'(t), y'(t) \rangle = \langle \tfrac34 t^2 + 2,\ b - 2t \rangle$; em $t = 0$, $\langle 2, b \rangle$. Velocidade escalar inicial: $\sqrt{4 + b^2} = 2\sqrt{101}$ → $4 + b^2 = 404$ → $b = 20$ (b > 0). Inclinação da tangente em t = 0: $dy/dx = y'(0)/x'(0) = 20/2 = 10$, então o ângulo é $\theta = \arctan 10 \approx 84{,}29°$.

b) Altura máxima (tangente horizontal, $dy/dt = 0$ com $dx/dt \neq 0$): $y'(t) = 20 - 2t = 0$ → $t = 10$ s; $y(10) = 200 - 100 = 100$ cm.

c) Pouso: $y(t) = t(20 - t) = 0$ → $t = 20$ s (t = 0 é o lançamento). Distância da origem: $x(20) = \tfrac14 \cdot 8000 + 40 = 2040$ cm (o ponto de pouso é (2040, 0)).

d) Tangente vertical exige $dx/dt = 0$ com $dy/dt \neq 0$. Mas $x'(t) = \tfrac34 t^2 + 2 \geq 2 > 0$ para todo t: **não há** ponto com tangente vertical.

**Verificação:** $y(10) = 100$ é máximo porque $y''(t) = -2 < 0$; em t = 20, $y = 0$ e $x' > 0$, coerente com o projétil indo para a direita.
