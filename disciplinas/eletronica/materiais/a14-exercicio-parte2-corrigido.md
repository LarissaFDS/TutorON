---
id: eletronica-anot-emissor-tensoes-nos
titulo: Tensões de nó VB, VC, VE e VBC do TBJ com resistor de emissor (20 V, 430 kΩ, 2 kΩ, 1 kΩ, β = 50), refeitas: VCE positivo e tensões de nó medidas em relação ao terra
assunto: eletronica-07-tbj-polarizacao
tipo: resolucao
resolucao: sim
fonte: Anotações "Exercício parte 2" (22 out. 2026), p. 1–2; a própria anotação marca "corrigir essa aqui, tem cálculos errados"
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Eletrônica 2026.2, IC/UFAL; docente indicado no cabeçalho: Prof. João Raphael Souza Martins); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de slides parafraseados; fotos de quadro, de slides e figuras de livro não foram copiadas
fontes_catalogo: ufal-eletronica-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Circuito:** o mesmo da polarização estável no emissor: $V_{CC} = 20$ V, $R_B = 430$ kΩ, $R_C = 2$ kΩ, $R_E = 1$ kΩ, $\beta = 50$.

**Refeito do zero:** $I_B = \frac{19{,}3}{430\mathrm{k} + 51\cdot1\mathrm{k}} = 40{,}12\ \mu$A; $I_C = 2{,}006$ mA; $I_E = 2{,}046$ mA.
- $V_E = I_E R_E = 2{,}046$ V;
- $V_B = V_E + 0{,}7 = 2{,}746$ V (ou $20 - 430\mathrm{k}\,I_B$);
- $V_C = 20 - R_C I_C = 15{,}99$ V;
- $V_{CE} = V_C - V_E = 13{,}94$ V;
- $V_{BC} = V_B - V_C = -13{,}24$ V.

**Correção (os erros das anotações):**
- $V_{CE} = 20 - 6{,}058$ foi escrito como $-13{,}942$ V; o certo é $+13{,}94$ V;
- $V_B = 430\mathrm{k}\cdot I_B = 17{,}25$ V e $V_C = 2\mathrm{k}\cdot I_C = 4{,}01$ V são as **quedas** nos resistores, não as tensões de nó. Tensão de nó = $V_{CC}$ menos a queda;
- $V_E = 17{,}95$ V veio do sinal trocado; o certo é 2,046 V;
- $V_{BC} = +13{,}24$ V indicaria a junção base-coletor direta (saturação); o certo, $-13{,}24$ V, é reverso, como exige a região ativa.

**Verificação:** a LKT $20 - 2\cdot2{,}006 - 13{,}94 - 1\cdot2{,}046 = 0$; $V_{BE} = V_B - V_E = 0{,}7$ V; a junção BC reversa confirma a região ativa.
