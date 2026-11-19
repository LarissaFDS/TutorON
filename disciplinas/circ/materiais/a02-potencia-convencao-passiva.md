---
id: circ-anot-potencia-convencao-passiva
titulo: Potência fornecida e absorvida: convenção passiva de sinais e balanço de potência (soma das potências igual a zero)
assunto: circ-01-grandezas-potencia
tipo: material_estudo
resolucao: nao
fonte: Anotações manuscritas "Potência e Leis de Kirchoff" (12 mar. 2026), pág. 1
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

**Convenção passiva:** se a corrente $i$ **entra** pelo terminal + da tensão $v$ do elemento, a potência absorvida é
$$p = v\,i .$$
Se a corrente entra pelo terminal −, $p = -v\,i$. Resultado positivo: o elemento **absorve** (recebe) potência; negativo: **fornece**. Resistores sempre absorvem ($p = R i^2 \ge 0$). Fontes podem absorver (bateria sendo carregada) ou fornecer.

Corrente ou tensão negativa no resultado só quer dizer que o sentido real é o oposto ao escolhido; mantenha os sentidos de referência até o fim e só então interprete o sinal. Antes de calcular a potência, confira para qual terminal a corrente de referência aponta.

**Conservação de energia (balanço):** a soma das potências absorvidas por todos os elementos é zero:
$$\sum_k p_k = 0 \quad\Longleftrightarrow\quad \sum P_{fornecidas} = \sum P_{absorvidas}.$$
Um balanço que não fecha indica erro de sinal ou de conta.

Exemplos: fonte de 120 V cuja corrente de 8 A **sai** pelo terminal +: $p = -120 \cdot 8 = -960$ W, fornece 960 W. Fonte de corrente com 1,8 A saindo pelo terminal de maior potencial (35 V contra 0 V): fornece $35 \cdot 1{,}8 = 63$ W.

**Verificação:** no circuito de 120 V e 20 V das listas (bloco de análise nodal), as fontes fornecem 960 + 100 = 1060 W e os resistores absorvem 640 + 180 + 125 + 45 + 70 = 1060 W.
