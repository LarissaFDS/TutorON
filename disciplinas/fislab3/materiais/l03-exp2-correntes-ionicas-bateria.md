---
id: fislab3-exp2-correntes-e-bateria
titulo: Experimento 2 de Física Experimental 3, questões 1, 2 e 4 — sentido da corrente entre as ponteiras, eletrostática com correntes iônicas e bateria isolada no ar
assunto: fislab3-01-campo-e-potencial
tipo: roteiro
questao: 1, 2, 4
resolucao: sim
fonte: Roteiro "Campo a partir do potencial", Física Experimental 3, Experimento 2 (Instituto de Física, UFAL, Laboratório de Ensino), questões 1, 2 e 4 | parafraseado
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
Roteiro do Experimento 2 de Física Experimental 3 (Laboratório de Ensino do IF-UFAL), questões 1, 2 e 4, parafraseadas. Status da resolução: pendente de confirmação do professor. A explicação é da equipe TutorON e não é gabarito do professor. Relatório é atividade avaliativa: o tutor guia, não escreve a resposta.

**Q1. Corrente nos dois sentidos.** O multímetro mede a diferença $V_{móvel} - V_{fixa}$. Ao levar a ponteira móvel de um eletrodo ao outro, ela passa por pontos de potencial menor e depois maior que o da fixa, então a leitura troca de sinal (e a pequena corrente pelo medidor troca de sentido) ao cruzar a equipotencial da ponteira fixa. Se a fixa ficar no eletrodo negativo (V = 0), a leitura só cresce, de zero até a tensão da fonte, à medida que a móvel se aproxima do eletrodo positivo.

**Q2. Eletrostática com corrente?** Há corrente iônica na solução, então não é eletrostática estrita. Mas, em regime estacionário, $\vec J = \sigma\vec E$ e a conservação de carga dão $\nabla\cdot\vec E = 0$ num meio homogêneo: o potencial obedece à mesma equação de Laplace do caso eletrostático, com as mesmas condições nos eletrodos. Por isso o mapa de equipotenciais é o mesmo; a corrente é o que deixa o voltímetro medir.

**Q4. Bateria ligada só ao ar.** Os polos têm diferença de potencial, mas o ar é isolante (condutividade muito baixa), então quase não há corrente nem caminho fechado: a fonte não fornece energia, está isolada. Na cuba, a solução de sulfato de cobre fecha o circuito.

**Perguntas para guiar.** Onde a leitura do multímetro passa por zero? O que a equação de Laplace exige nas bordas, nos dois casos?

**Verificação:** `test_meio_condutor_tem_o_mesmo_potencial_da_eletrostatica` confere com SymPy que o potencial de duas linhas de carga satisfaz Laplace fora dos eletrodos e que a leitura muda de sinal ao cruzar a equipotencial da ponteira fixa.
