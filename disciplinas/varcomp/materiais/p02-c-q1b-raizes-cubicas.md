---
id: varcomp-p1c-q1b-raizes-cubicas
titulo: Prova 1 versão C, Q1 b — todas as raízes cúbicas de 1 − i (e a leitura com módulo |1 − i| elevado a 1/3); forma polar, argumento principal −π/4
assunto: varcomp-01-numeros-complexos
tipo: prova
questao: 1b
resolucao: sim
fonte: Prova 1 de Variáveis Complexas, versão C (arquivo prova16.pdf, PDF gerado em março de 2021), questão 1b
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
Prova 1 de Variáveis Complexas (Prof. Xu Yang, IC/UFAL), versão C, questão 1b. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (a prova não tem gabarito; a resolução é da equipe TutorON, conferida com SymPy e numericamente em `tests_acervo/test_disciplina_varcomp.py`).

Pede-se "todos os valores" de $|-i + 1|^{1/3}$. **Dúvida de enunciado:** com as barras de módulo, $|1 - i| = \sqrt2$ é um número real positivo; "todos os valores" faz mais sentido para a raiz complexa $(1 - i)^{1/3}$ (raiz cúbica de 1 menos i). As duas leituras estão resolvidas; a escolha é do professor.

**Leitura 1: raízes cúbicas de 1 − i.** Forma polar: $|1 - i| = \sqrt2$; o ponto (1, −1) está no 4º quadrante, então o argumento principal é $\operatorname{Arg}(1 - i) = -\pi/4$ (convenção $(-\pi, \pi]$). Então $1 - i = \sqrt2\, e^{-i\pi/4}$. As três raízes cúbicas:
$$w_k = 2^{1/6}\, e^{i(-\pi/4 + 2k\pi)/3}, \quad k = 0, 1, 2.$$
- $k = 0$: ângulo $-\pi/12$: $w_0 \approx 1{,}0842 - 0{,}2905i$;
- $k = 1$: ângulo $7\pi/12$: $w_1 \approx -0{,}2905 + 1{,}0842i$;
- $k = 2$: ângulo $5\pi/4$ (argumento principal $-3\pi/4$): $w_2 = 2^{1/6}(-\tfrac{\sqrt2}{2} - \tfrac{\sqrt2}{2}i) \approx -0{,}7937 - 0{,}7937i$.
O módulo é $2^{1/6} \approx 1{,}1225$ (raiz sexta de 2). As três raízes formam um triângulo equilátero no círculo de raio $2^{1/6}$, separadas de $2\pi/3$.

**Leitura 2: o módulo elevado a 1/3.** $|1 - i|^{1/3} = (\sqrt2)^{1/3} = 2^{1/6}$ (valor real). Se a potência for lida como complexa, os três valores são $2^{1/6} e^{2k\pi i/3}$, $k = 0, 1, 2$: $2^{1/6}$ e $2^{1/6}(-\tfrac12 \pm \tfrac{\sqrt3}{2} i)$.

Erros comuns: dar só uma raiz; usar $\arctan(-1) = -\pi/4$ sem conferir o quadrante (aqui está certo, mas em $-1 + i$ o ângulo é $3\pi/4$); somar $2k\pi$ depois de dividir por 3.

**Verificação:** $w_k^3 = (2^{1/6})^3 e^{i(-\pi/4 + 2k\pi)} = \sqrt2\, e^{-i\pi/4} = 1 - i$ para os três k; a soma das três raízes é zero, como deve ser para as raízes de $w^3 - (1 - i) = 0$.
