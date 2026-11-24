---
id: alglin-lista1-subespacos-funcoes-planos
titulo: Lista 1 — subespaço de funções contínuas com integral nula, espaço de matrizes com AC = 0 e equação do plano gerado por dois vetores
assunto: alglin-01-espacos-vetoriais-subespacos
tipo: exercicio_resolvido
resolucao: sim
fonte: Lista 1 de Álgebra Linear (Espaços Vetoriais, UFAL), PDF do material do 2º período de Engenharia de Computação | enunciados parafraseados
curso: Engenharia de Computação (UFAL), ECOM011 Álgebra Linear, 2º período (também no 3º período de Ciência da Computação); semestre não identificado
fontes_catalogo: ufal-alglin-listas
autoria: Enunciados da lista da disciplina; resoluções da equipe TutorON com apoio de IA, conferidas com SymPy e NumPy
licenca: Não declarada (lista da disciplina; PDF não versionado)
publicacao_transcricao: não autorizada; enunciados parafraseados
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Álgebra Linear, Lista 1 (subespaços). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Roteiro para provar que $W \subset V$ é subespaço:** (i) o vetor nulo está em $W$; (ii) $u, v \in W \Rightarrow u + v \in W$; (iii) $u \in W \Rightarrow \alpha u \in W$.

**2. Matrizes $A$ com $AC = 0$** ($C$ fixa, $2\times2$): $0\,C = 0$; $(A + B)C = AC + BC = 0$; $(\alpha A)C = \alpha(AC) = 0$. Os outros axiomas vêm de $M_{2\times2}$.

**4. Funções contínuas em $[a, b]$ com $\int_a^b f = 0$:** a função nula tem integral 0; a integral é linear, $\int(f + g) = \int f + \int g = 0$ e $\int \alpha f = \alpha\int f = 0$. Logo é subespaço de $C[a, b]$. Exemplo: em $[0, 1]$, $f(x) = x - \tfrac12$ e $g(x) = x^2 - \tfrac13$ estão nele, e $f + g$ também.

**5. Plano gerado.** $F = [u, v]$ é $\{a x + b y + c z = 0\}$ com $(a, b, c) = u \times v$.
- $F_1 = [(0, 1, -2), (1, 1, 1)]$: $3x - 2y - z = 0$.
- $F_2 = [(-1, 0, 3), (2, -1, 0)]$: $3x + 6y + z = 0$.
Confira substituindo os geradores na equação (deve dar 0).

Erro comum: provar só o fechamento da soma e esquecer o vetor nulo.

**Verificação:** linearidade da integral, normais e geradores conferidos com SymPy em `test_lista1_subespacos_planos`.
