---
id: eletronica-anot-divisor-tensao
titulo: Ponto Q de TBJ com polarização por divisor de tensão (22 V, 39 kΩ e 3,9 kΩ, RC 10 kΩ, RE 1,5 kΩ): equivalente de Thévenin na base, IB, IC e VCE para β = 50 e 100
assunto: eletronica-07-tbj-polarizacao
tipo: resolucao
resolucao: sim
fonte: Anotações "Circuitos de Polarização de Transistores" (23 out. 2026), item c, e "Exercício parte 2" (22 out. 2026), p. 2–5 (exercício de livro, parafraseado)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Eletrônica 2026.2, IC/UFAL; docente indicado no cabeçalho: Prof. João Raphael Souza Martins); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de slides parafraseados; fotos de quadro, de slides e figuras de livro não foram copiadas
fontes_catalogo: ufal-eletronica-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Como calcular o ponto Q com divisor de tensão:**
1. Em CC, capacitores abertos (acoplamento e desvio do emissor).
2. Thévenin na base (a topologia mais usada em amplificadores): $R_{Th} = R_1 \parallel R_2$ e $V_{Th} = V_{CC}\frac{R_2}{R_1 + R_2}$.
3. Malha da base: $I_B = \frac{V_{Th} - V_{BE}}{R_{Th} + (\beta + 1)R_E}$; $I_C = \beta I_B$.
4. Malha do coletor: $V_{CE} = V_{CC} - R_C I_C - R_E I_E$.

**Exemplo:** $V_{CC} = 22$ V, $R_1 = 39$ kΩ, $R_2 = 3{,}9$ kΩ, $R_C = 10$ kΩ, $R_E = 1{,}5$ kΩ.
$R_{Th} = 3{,}545$ kΩ; $V_{Th} = 22\cdot3{,}9/42{,}9 = 2{,}0$ V.

| $\beta$ | $I_B$ | $I_C$ | $V_{CE}$ |
|---|---|---|---|
| 50 | 16,24 μA | 0,812 mA | 12,64 V |
| 100 | 8,385 μA | 0,838 mA | 12,35 V |

Ao dobrar $\beta$, $I_C$ muda só +3,25% e $V_{CE}$ −2,3%: o divisor quase não depende de $\beta$. Com $\beta R_E \ge 10R_2$ vale a aproximação $V_B \approx V_{Th}$, $I_E \approx (V_{Th} - 0{,}7)/R_E = 0{,}867$ mA.

**Verificação:** para $\beta = 100$, $V_E = 1{,}270$ V, $V_C = 13{,}62$ V; $V_C - V_E = 12{,}35$ V confere; $V_{CE} > 0{,}2$ V e a junção BC reversa confirmam a região ativa.
