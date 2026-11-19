---
id: circ-anot-superposicao-superno-ab1-q3
titulo: Lista AB1, questão 3: superposição com fonte dependente (a dependente nunca é desligada) e supernó com a fonte de tensão 4ix
assunto: circ-03-superposicao-transformacao
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Lista para AB1" (1 maio 2026), lista do Prof. Jobson de Araújo Nascimento, págs. 3–4; segunda tentativa em "Questões circuitos", págs. 8–11
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Circuitos Elétricos 2026.1, Prof. Jobson de Araújo Nascimento, IC/UFAL); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-circ-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Circuito (descrito):** nó de cima T e dois nós de baixo, E (esquerda) e D (direita), ligados por uma fonte de tensão **dependente** $4i_x$ com o + em D: $v_D - v_E = 4i_x$. Entre T e E: 2 Ω ($i_x$ de T para E) e fonte de 6 A (de E para T). Entre T e D: fonte de 4 A (de D para T) e 8 Ω com $v_x$ (+ em T).

**Supernó.** Tomando T como referência, a fonte $4i_x$ liga dois nós que não são a referência: E e D formam um **supernó**. Escreva uma LKC para a superfície que envolve os dois nós e use a equação da fonte como restrição:
- LKC no supernó: $\dfrac{v_E}{2} + \dfrac{v_D}{8} + 6 + 4 = 0$ (saindo: pelos resistores até T e pelas duas fontes, que levam corrente para T);
- restrição: $v_D - v_E = 4i_x$, com $i_x = -v_E/2$ (de T para E) $\Rightarrow v_D = -v_E$.

Daí $\tfrac{3}{8}v_E = -10$, $v_E = -\tfrac{80}{3}$ V, $v_D = \tfrac{80}{3}$ V e $v_x = 0 - v_D = -\tfrac{80}{3} \approx -26{,}67$ V.

**Superposição (como nas anotações):** liga-se uma fonte **independente** por vez e a dependente fica sempre no circuito. Só 4 A: $v_x' = -\tfrac{32}{3}$ V. Só 6 A: $v_x'' = -16$ V. Soma: $v_x = -\tfrac{32}{3} - 16 = -\tfrac{80}{3}$ V.

**Correções:** numa segunda tentativa ("Questões circuitos") a soma foi refeita com denominador errado ($-\tfrac{32}{6} - 16 = -\tfrac{128}{6}$), e as potências calculadas a partir daí não fecharam o balanço. O valor certo é $-\tfrac{80}{3}$ V.

**Verificação:** potências com $v_x = -\tfrac{80}{3}$: 2 Ω $\tfrac{3200}{9}$ W, 8 Ω $\tfrac{800}{9}$ W, 6 A fornece 160 W, dependente fornece $\tfrac{3520}{9}$ W e a de 4 A **absorve** $\tfrac{320}{3}$ W; soma zero. Conferido no SymPy.
