---
id: prob-anot-conceitos-probabilidade
titulo: Probabilidade clássica, regra da adição, probabilidade condicional, regra do produto; eventos independentes x mutuamente exclusivos
assunto: prob-01-probabilidade-basica
tipo: material_estudo
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Probabilidade _250907_210206.pdf" (2025.2), págs. 1–2
autoria: Otávio Joshua Costa Brandão Menezes (aluno, equipe TutorON), anotações de estudo; paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações pessoais do aluno); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia as anotações e não reproduz imagens
fontes_catalogo: ufal-prob-anotacoes-2025-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Anotações de aluno (2025.2), parafraseadas. Status da resolução: corrigida (as anotações listam duas fórmulas sem dizer quando valem; a condição foi acrescentada). Conferido com `fractions`.

**Probabilidade clássica** (resultados igualmente prováveis): $P(A) = \dfrac{\text{casos favoráveis}}{\text{casos possíveis}}$.

**Regra da adição** (A ou B ou ambos): $P(A \cup B) = P(A) + P(B) - P(A \cap B)$. Para três eventos: $P(A\cup B\cup C) = P(A)+P(B)+P(C) - P(A\cap B) - P(A\cap C) - P(B\cap C) + P(A\cap B\cap C)$.

**Probabilidade condicional** (A dado B, com $P(B) > 0$): $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$. O enunciado informa um evento que já ocorreu, e o espaço amostral passa a ser B. Não troque $P(A\mid B)$ por $P(B\mid A)$.

**Regra do produto:** $P(A\cap B) = P(A\mid B)\,P(B) = P(B\mid A)\,P(A)$; para três eventos, $P(A\cap B\cap C) = P(A)\,P(B\mid A)\,P(C\mid A\cap B)$.

**Diferença entre eventos independentes e mutuamente exclusivos (disjuntos):**
- Mutuamente exclusivos: não ocorrem juntos, $P(A\cap B) = 0$; então $P(A\cup B) = P(A) + P(B)$.
- Independentes: um não muda a probabilidade do outro, $P(A\mid B) = P(A)$; então $P(A\cap B) = P(A)\,P(B)$ (para vários independentes, o produto de todas).
- **Correção:** as anotações escrevem $P(A\cap B) = P(A)P(B)$ e $P(A\cup B) = P(A)+P(B)$ lado a lado, sem condição. A primeira só vale para independentes; a segunda só para disjuntos. Dois eventos disjuntos com probabilidade positiva **nunca** são independentes, porque $P(A\cap B) = 0 \neq P(A)P(B)$.

Exemplo com um dado: A = "par" = {2,4,6} e B = {1,2}. $P(A\cap B) = 1/6 = (1/2)(1/3)$: independentes, mas não disjuntos.

**Verificação:** com A = {2,4,6} e C = {1,3}, $P(A\cup C) = 5/6 = 1/2 + 1/3$ (disjuntos) e $P(A\cap C) = 0 \ne 1/6$ (não independentes).
