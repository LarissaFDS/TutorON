---
id: fislab3-exp2-equipotenciais-cuba
titulo: Experimento 2 de Física Experimental 3 — mapear linhas equipotenciais numa cuba eletrolítica e traçar as linhas de campo perpendiculares a elas
assunto: fislab3-01-campo-e-potencial
tipo: roteiro
resolucao: sim
fonte: Roteiro "Campo a partir do potencial", Física Experimental 3, Experimento 2 (Instituto de Física, UFAL, Laboratório de Ensino) | parafraseado
curso: Engenharia de Computação (UFAL), ECOM026 Física Experimental 3, 4º período
fontes_catalogo: ufal-fislab3-roteiro-exp2
autoria: Roteiro: Laboratório de Ensino do IF-UFAL; explicação da equipe TutorON
licenca: Não declarada (roteiro da disciplina); PDF não versionado
publicacao_transcricao: não autorizada; roteiro parafraseado
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Roteiro do Experimento 2 de Física Experimental 3 (Laboratório de Ensino do IF-UFAL), parafraseado. Status da resolução: pendente de confirmação do professor. A explicação é da equipe TutorON e não é gabarito do professor. Relatório é atividade avaliativa: o tutor guia, não escreve o relatório.

**Objetivo.** Ver como é o campo eletrostático entre dois eletrodos a partir de linhas equipotenciais medidas numa solução condutora (sulfato de cobre) numa cuba com papel milimetrado por baixo.

**Montagem.** Uma fonte de baixa tensão (cerca de 6 V) liga dois eletrodos (cilindros de cobre; depois, placas retangulares). Um multímetro fica entre uma ponteira fixa e uma ponteira móvel, ambas na solução.

**Procedimento, em resumo.** Com a ponteira fixa parada, mova a móvel até o multímetro mostrar a mesma tensão: cada posição assim é um ponto da mesma equipotencial. Marque pelo menos oito pontos por linha e pelo menos seis linhas (três perto de cada eletrodo). Depois trace linhas de campo cortando as equipotenciais em ângulo reto. Repita com um anel de latão entre os eletrodos e com placas paralelas.

**A física por trás.** O campo é menos o gradiente do potencial:
$$\vec E = -\nabla V = -\left(\frac{\partial V}{\partial x}\hat i + \frac{\partial V}{\partial y}\hat j + \frac{\partial V}{\partial z}\hat k\right).$$
Ao longo de uma equipotencial V não muda, então E não tem componente nessa direção: as linhas de campo são perpendiculares às equipotenciais e apontam do potencial maior para o menor. O roteiro escreve a relação sem o sinal de menos; o sinal só muda o sentido, não a direção das linhas.

**O que esperar.** Entre dois cilindros, as equipotenciais lembram as de duas linhas de carga opostas (curvas fechadas em volta de cada eletrodo). Entre placas paralelas, ficam quase retas e igualmente espaçadas no meio: campo quase uniforme.

**Verificação:** `test_campo_perpendicular_as_equipotenciais` confere com SymPy que −∇V é perpendicular à tangente da equipotencial para duas linhas de carga e que entre placas o campo é uniforme.
