---
id: prob-anot-va-continua
titulo: Variável aleatória contínua: densidade de probabilidade, área sob a curva, distribuição acumulada e suas propriedades
assunto: prob-03-variaveis-aleatorias
tipo: material_estudo
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Variáveis Aleatórias_251008_230428.pdf" (2025.2), págs. 4–5
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
Anotações de aluno (2025.2), parafraseadas. Status da resolução: corrigida (faltava o intervalo onde a densidade vale; "sempre crescente" virou "não decrescente"). Conferido com SymPy.

**Densidade de probabilidade (fdp)** de uma VA contínua X: uma função $f(x)$ com
1. $f(x) \ge 0$;
2. $P(a \le X \le b) = \int_a^b f(x)\,dx$ (a probabilidade é a área sob a curva entre a e b);
3. $\int_{-\infty}^{+\infty} f(x)\,dx = 1$.
Numa contínua, $P(X = a) = 0$, então $\le$ e $<$ dão o mesmo resultado.

**Exemplo:** $f(x) = x/4$ para $1 \le x \le 3$ e 0 fora. $P(1 \le X \le 3) = \int_1^3 \frac{x}{4}\,dx = \frac{9 - 1}{8} = 1$.
- **Correção:** as anotações não dizem o intervalo. Sem ele, $x/4$ não é densidade (a integral em toda a reta não é 1). Com $[1, 3]$, a conta das anotações é exatamente a condição 3.

**Função de distribuição acumulada:** $F(a) = P(X \le a) = \int_{-\infty}^{a} f(x)\,dx$, e $f(x) = F'(x)$ onde a derivada existe. No exemplo, $F(x) = (x^2 - 1)/8$ para $1 \le x \le 3$.

**Propriedades da FDA** (valem para discretas e contínuas): $0 \le F(x) \le 1$; $F(-\infty) = 0$; $F(+\infty) = 1$; F é **não decrescente**; $P(a < X \le b) = F(b) - F(a)$.
- **Correção:** as anotações dizem "sempre crescente". F pode ficar constante (numa discreta, entre dois valores; no exemplo, antes de 1 e depois de 3).

**Verificação:** $F(3) - F(1) = 1 - 0 = 1$; $P(X \le 2) = F(2) = 3/8 = \int_1^2 x/4\,dx$.
