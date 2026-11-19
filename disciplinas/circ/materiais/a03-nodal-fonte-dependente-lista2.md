---
id: circ-anot-nodal-lista2-q1
titulo: Análise nodal (LKC) com fonte de corrente dependente 3i₁: tensões de nó, correntes e balanço de potência (lista 2, questão 1)
assunto: circ-02-kirchhoff-nodal-malhas
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Potência e Leis de Kirchoff" (12 mar. 2026), págs. 3–4
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Circuitos Elétricos 2026.1, Prof. Jobson de Araújo Nascimento, IC/UFAL); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-circ-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Circuito (descrito):** referência (terra) embaixo. Fonte de 50 V (+ em cima) ligada pelo resistor de 6 Ω ao nó 1; $i_1$ é a corrente no 6 Ω, da fonte para o nó 1. Do nó 1: 8 Ω ao terra e 2 Ω ao nó 2. Do nó 2: 4 Ω ao terra e fonte independente de 5 A injetando corrente no nó 2. Fonte de corrente **dependente** $3i_1$ entre os nós, com a seta do nó 2 para o nó 1 (injeta $3i_1$ no nó 1 e retira do nó 2).

**Montagem (correntes que saem do nó positivas):** $i_1 = (50 - v_1)/6$.
- Nó 1: $\dfrac{v_1-50}{6} + \dfrac{v_1}{8} + \dfrac{v_1-v_2}{2} - 3i_1 = 0 \Rightarrow 31v_1 - 12v_2 = 800$.
- Nó 2: $\dfrac{v_2-v_1}{2} + \dfrac{v_2}{4} - 5 + 3i_1 = 0$.

**Resultado:** $v_1 = 32$ V, $v_2 = 16$ V, $i_1 = 3$ A, fonte dependente $3i_1 = 9$ A.

Potências (convenção passiva): fonte de 50 V fornece 150 W; fonte de 5 A fornece $16\cdot5 = 80$ W; fonte dependente fornece $(32-16)\cdot 9 = 144$ W. Resistores: 6 Ω 54 W, 8 Ω 128 W, 2 Ω 128 W, 4 Ω 64 W (total 374 W).

Nas anotações, a corrente do 6 Ω foi escrita saindo do nó ($i_1' = -i_1$); a equação final está certa.

**Verificação:** 150 + 80 + 144 = 374 W fornecidos = 374 W absorvidos; LKC no nó 2: 8 A chegam pelo 2 Ω e 5 A pela fonte; saem 4 A pelo 4 Ω e 9 A pela dependente. Conferido com análise nodal modificada no SymPy.
