---
id: compevol-ag-versus-subida-de-encosta-otimos-locais-memeticos-ilhas-estado-fixo
titulo: AG × subida de encosta (escalada de montanha) e o problema dos ótimos locais; populações de estado fixo, incrementais e modelo de ilhas; algoritmos meméticos e híbridos
assunto: compevol-03-outras-metaheuristicas
tipo: exercicio_resolvido
questao: Apostila de Lucas, cap. 5 e seção 6.4
resolucao: sim
fonte: Apostilas e textos da pasta da turma (Lucas, UFRGS 2002; Lacerda e Carvalho; Dianati, Song e Treiber)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: lucas-apostila-ag
autoria: Exercício clássico dos textos da pasta da turma; resolução da equipe TutorON
licenca: Textos sem licença aberta declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Apostila de Lucas, cap. 5 e seção 6.4 (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Subida de encosta** (*hill climbing*): parte de uma solução e passa para um vizinho melhor até nenhum vizinho melhorar. É rápida, mas **para no primeiro ótimo local**; o resultado depende do ponto de partida. Remédio simples: reinícios aleatórios.

**AG:** mantém uma **população** espalhada e recombina partes de soluções diferentes, o que permite saltar entre regiões; é mais lento por avaliação, mas mais robusto em funções multimodais (como $x\,\text{sen}(10\pi x) + 1$). A mutação e a diversidade evitam a **convergência prematura**.

**Variações de população:**
- **geracional:** toda a população é trocada a cada geração;
- **estado fixo** (*steady-state*): a cada passo, só um ou dois filhos substituem os piores; converge mais rápido, com mais risco de perder diversidade;
- **modelo de ilhas:** várias subpopulações evoluem separadas e trocam indivíduos (**migração**) de tempos em tempos; mantém diversidade e paraleliza bem.

**Híbridos e meméticos:** o **algoritmo memético** aplica uma **busca local** (como subida de encosta) a cada filho: o AG encontra boas regiões, a busca local refina dentro delas. Outros híbridos usam heurísticas do problema na inicialização ou nos operadores.

**Outras meta-heurísticas da família:** programação genética (indivíduos são programas em árvore), programação evolutiva, evolução diferencial; e, fora da evolução, têmpera simulada, busca tabu, colônia de formigas e enxame de partículas.

**Verificação:** `test_subida_de_encosta_e_ag` roda subida de encosta em $x\,\text{sen}(10\pi x) + 1$ a partir de 20 pontos com semente fixa e mostra que a maioria para em ótimos locais, enquanto o AG e o memético chegam perto do máximo global $2{,}85$.
