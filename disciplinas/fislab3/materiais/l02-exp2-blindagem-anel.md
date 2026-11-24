---
id: fislab3-exp2-blindagem-anel
titulo: Experimento 2 de Física Experimental 3, questão 3 — o anel de latão na cuba é uma blindagem eletrostática perfeita?
assunto: fislab3-01-campo-e-potencial
tipo: roteiro
questao: 3
resolucao: sim
fonte: Roteiro "Campo a partir do potencial", Física Experimental 3, Experimento 2 (Instituto de Física, UFAL, Laboratório de Ensino), questão 3 | parafraseado
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
Roteiro do Experimento 2 de Física Experimental 3 (Laboratório de Ensino do IF-UFAL), questão 3, parafraseada. Status da resolução: pendente de confirmação do professor. A explicação é da equipe TutorON e não é gabarito do professor. Relatório é atividade avaliativa: o tutor guia, não escreve a resposta.

**Pergunta.** Ao colocar um anel de latão entre os eletrodos na cuba, observa-se o potencial fora, perto e dentro do anel. O anel é uma blindagem eletrostática perfeita?

**Ideia física.** Um condutor em equilíbrio tem o mesmo potencial em todos os pontos. Se o anel envolve uma região sem cargas, o potencial lá dentro obedece à equação de Laplace com o mesmo valor em toda a borda; a única solução é V constante, logo $\vec E = -\nabla V = 0$ dentro. Na medida, a ponteira móvel mostra quase a mesma tensão em todo o interior do anel: as equipotenciais de fora contornam o anel e não entram. É o efeito gaiola de Faraday, em duas dimensões.

**Por que não é perfeita na prática.** O anel não fecha a região em três dimensões (a solução passa por cima e por baixo), o latão e a solução não são condutores ideais e há corrente iônica atravessando a cuba; por isso aparece uma pequena variação de potencial no interior. Para o relatório, compare a variação medida dentro do anel com a variação na mesma distância fora dele.

**Perguntas para guiar.** Qual é o potencial do anel comparado com os pontos vizinhos? As linhas de campo que você traçou terminam no anel em ângulo reto? O que mudaria com um cilindro metálico fechado?

**Verificação:** `test_anel_condutor_blinda_o_interior` confere com SymPy que, para um anel condutor num campo uniforme (2D), o potencial é constante na borda e no interior e o campo dentro é zero.
