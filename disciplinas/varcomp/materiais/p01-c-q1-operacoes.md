---
id: varcomp-p1c-q1-operacoes
titulo: Prova 1 versão C, Q1 a, c, d — produto (2 − 3i)(4 + 2i), quociente (i³⁰ − i¹⁹)/(2i − 1), produto pelo conjugado (3 + 2i)·conj(7 + i)
assunto: varcomp-01-numeros-complexos
tipo: prova
questao: 1
resolucao: sim
fonte: Prova 1 de Variáveis Complexas, versão C (arquivo prova16.pdf, PDF gerado em março de 2021), questão 1
autoria: Enunciado: Prof. Xu Yang (Variáveis Complexas, Instituto de Computação, UFAL), parafraseado pela equipe TutorON; resolução da equipe TutorON
licenca: Não declarada (prova do professor); PDFs e imagens fora do repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
fontes_catalogo: ufal-varcomp-prova1-2021
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Prova 1 de Variáveis Complexas (Prof. Xu Yang, IC/UFAL), versão C, questão 1. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (a prova não tem gabarito; a resolução é da equipe TutorON, conferida com SymPy e numericamente em `tests_acervo/test_disciplina_varcomp.py`).

Pede-se o valor (forma algébrica a + bi) de três expressões.

a) Produto $(2 - 3i)(4 + 2i)$: distributiva com $i^2 = -1$: $8 + 4i - 12i - 6i^2 = 8 + 6 - 8i = 14 - 8i$.

c) Quociente $\frac{i^{30} - i^{19}}{2i - 1}$ (i elevado a 30 menos i elevado a 19, sobre 2i menos 1). Potências de i pelo resto da divisão do expoente por 4: $30 = 4\cdot7 + 2$, então $i^{30} = i^2 = -1$; $19 = 4\cdot4 + 3$, então $i^{19} = i^3 = -i$. Numerador: $-1 + i$. Multiplicar pelo conjugado do denominador, $-1 - 2i$:
$$\frac{(-1 + i)(-1 - 2i)}{(-1 + 2i)(-1 - 2i)} = \frac{1 + 2i - i + 2}{1 + 4} = \frac{3 + i}{5} = \frac35 + \frac15 i.$$

d) Produto pelo conjugado: $(3 + 2i)\,\overline{(7 + i)} = (3 + 2i)(7 - i) = 21 - 3i + 14i + 2 = 23 + 11i$. Erro comum: esquecer a barra do conjugado e multiplicar por $7 + i$, o que daria $19 + 17i$.

A questão 1(b) desta versão (raízes cúbicas) está no bloco "Prova 1 versão C, Q1 b".

**Verificação:** em (c), $(2i - 1)\cdot\frac{3 + i}{5} = \frac{6i + 2i^2 - 3 - i}{5} = \frac{-5 + 5i}{5} = -1 + i$, que é o numerador. Em (a), os módulos batem: $|2 - 3i|\,|4 + 2i| = \sqrt{13}\sqrt{20} = \sqrt{260} = |14 - 8i|$.
