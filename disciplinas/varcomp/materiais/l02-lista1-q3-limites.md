---
id: varcomp-lista1-q3-limites
titulo: Lista 1, Q3 — limites complexos: (z³ − 8i)/(z + 2i) em −2i dá −12; (1 + z)^{1/4} − 1 sobre z dá 1/4; diferença de raízes cúbicas dá 2/3
assunto: varcomp-02-funcoes-analiticas-cauchy-riemann
tipo: lista
questao: 3
resolucao: sim
fonte: Lista nº 1 de Variável Complexa (Instituto de Computação, UFAL; arquivo Lista_1.pdf), questão 3
autoria: Enunciado: lista da disciplina (Instituto de Computação, UFAL; autor não identificado no arquivo), parafraseado pela equipe TutorON; resolução da equipe TutorON, conferida com SymPy
licenca: Não declarada (lista da disciplina); PDFs e imagens fora do repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
fontes_catalogo: ufal-varcomp-lista1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Lista nº 1 de Variável Complexa (IC/UFAL), questão 3. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (a lista não tem gabarito oficial; a resolução é da equipe TutorON, conferida com SymPy em `tests_acervo/test_disciplina_varcomp.py`).

Os três limites são da forma $0/0$. Duas saídas: fatorar, ou reconhecer a **definição de derivada** $\lim_{z\to z_0}\frac{f(z) - f(z_0)}{z - z_0} = f'(z_0)$ (nos ramos principais das raízes, perto de $z = 1$).

**(a)** $\lim_{z \to -2i}\frac{z^3 - 8i}{z + 2i}$. Como $(-2i)^3 = 8i$, é a derivada de $z^3$ em $-2i$: $3z^2 = 3(-2i)^2 = -12$. (Fatorando: $z^3 - 8i = (z + 2i)(z^2 - 2iz - 4)$, e $(-2i)^2 - 2i(-2i) - 4 = -4 - 4 - 4 = -12$.)

**(b)** $\lim_{z \to 0}\frac{(1+z)^{1/4} - 1}{z}$ é a derivada de $(1+z)^{1/4}$ em 0: $\frac14(1+z)^{-3/4}\big|_{0} = \frac14$.

**(c)** $\lim_{z \to 0}\frac{(1+z)^{1/3} - (1-z)^{1/3}}{z} = \frac13 + \frac13 = \frac23$ (some e subtrai 1 no numerador e use dois limites como o de (b)).

Erro comum em (a): substituir direto e concluir que o limite não existe; $0/0$ pede fatoração ou derivada.

**Verificação:** `sympy.limit` dá $-12$, $1/4$ e $2/3$.
