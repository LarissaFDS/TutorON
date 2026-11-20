---
id: controle-anot-circuito-rc
titulo: Modelagem de circuito por LKC: rede R1, R2, C1, C2 com saída em aberto; G(s) = (C1C2R1R2s² + C2(R1+R2)s + 1)/(C1C2R1R2s² + (C1R1 + C2R1 + C2R2)s + 1)
assunto: controle-02-modelagem
tipo: resolucao
resolucao: sim
fonte: Anotações "Revisão de Laplace e Sistemas mecânicos" (19 ago. 2026), p. 5–6
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Circuito (descrito em texto):** fonte $V_i$; $R_1$ de $V_i$ ao nó 1 (tensão $V_1$); $R_2$ do nó 1 à saída $V_o$ (em aberto); $C_1$ do nó 1 ao terra; $C_2$ ligado direto de $V_i$ à saída.

**LKC:** nó 1: $\frac{V_1 - V_i}{R_1} + C_1\dot V_1 + \frac{V_1 - V_o}{R_2} = 0$; saída: $C_2(\dot V_i - \dot V_o) + \frac{V_1 - V_o}{R_2} = 0$, daí $V_1 = V_o + C_2R_2(\dot V_o - \dot V_i)$. Substituindo:
$$C_1C_2R_2\ddot V_o + \Big(\tfrac{C_2R_2}{R_1} + C_1 + C_2\Big)\dot V_o + \tfrac{1}{R_1}V_o = C_1C_2R_2\ddot V_i + \Big(\tfrac{C_2R_2}{R_1} + C_2\Big)\dot V_i + \tfrac{1}{R_1}V_i.$$

**Correção:** as anotações põem sinal **negativo** em todos os termos de $V_i$ do lado direito. Com eles, $G(0)$ seria $-1$; mas em corrente contínua os capacitores ficam abertos, não passa corrente e $V_o = V_i$, logo $G(0) = 1$.

**Função de transferência (CI nulas, multiplicando por $R_1$):**
$$G(s) = \frac{V_o}{V_i} = \frac{C_1C_2R_1R_2s^2 + C_2(R_1 + R_2)s + 1}{C_1C_2R_1R_2s^2 + (C_1R_1 + C_2R_1 + C_2R_2)s + 1}.$$

**Verificação:** `sympy.solve` das duas LKC dá este $G$; $G(0) = 1$ e $G(\infty) = 1$ ($C_2$ vira curto em alta frequência).
