---
id: cg-sombreamento-flat-gouraud-phong-interpolacao-de-intensidades-e-de-normais-bandas-de-mach
titulo: Sombreamento de polígonos: flat (constante), Gouraud (interpolação de intensidades nos vértices) e Phong (interpolação de normais); vantagens de cada um, bandas de Mach e brilhos especulares; ENADE na AB2 de 2021.2
assunto: cg-03-modelagem-iluminacao-e-textura
tipo: prova
questao: AB2 de 2021.2 (questão 3) e reavaliação (questão 1), aula de Iluminação
resolucao: sim
fonte: Exercícios e provas de Computação Gráfica do Prof. Marcelo Costa Oliveira (IC-UFAL)
curso: Ciência da Computação (UFAL), COMP381 Computação Gráfica; aulas de 2012 a 2017 e provas de 2014 e 2021.2 (Prof. Marcelo Costa Oliveira)
fontes_catalogo: ufal-marcelo-aulas-cg,ufal-cg-provas-exercicios
autoria: Questões do Prof. Marcelo Costa Oliveira (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Computação Gráfica (IC-UFAL), AB2 de 2021.2 (questão 3) e reavaliação (questão 1), aula de Iluminação (parafraseado). Status da resolução: pendente do professor. A resolução é da equipe TutorON e não é gabarito do professor.

**Flat (constante):** uma intensidade por polígono, calculada com a normal da face. Rápido, mas o objeto fica **facetado**; é exato só com luz e observador no infinito e o polígono sendo a superfície real.

**Gouraud:** calcula a intensidade **nos vértices** (com normais médias das faces vizinhas) e **interpola as intensidades** ao longo das arestas e das linhas de varredura. Vantagem sobre o flat: tira o facetado. Limites: **bandas de Mach** atenuadas mas presentes e brilhos especulares perdidos ou borrados quando o reflexo cai no meio do polígono.

**Phong:** **interpola as normais** e calcula a iluminação em cada pixel. Vantagem sobre Gouraud: reflexos especulares corretos e menos bandas de Mach. Custo maior (iluminação por pixel).

**Questão da AB2 de 2021.2** (afirmações sobre os modelos):
- I. flat dá aparência facetada: **verdadeira**;
- II. Phong é pouco eficiente para reflexões especulares: **falsa**, é justamente o ponto forte dele;
- III. flat não serve para imagens realistas porque destaca o facetado: **verdadeira**;
- IV. Gouraud exige luz no infinito: **falsa** na leitura usual, porque Gouraud calcula a iluminação nos vértices com qualquer fonte; a hipótese de luz no infinito é a do flat exato.

Com essa leitura a resposta é **I e III**, alternativa (B). Como a questão vem de exame externo, confira o gabarito oficial.

**Verificação:** `test_gouraud_phong` interpola intensidades e normais num segmento com reflexo no meio e confere que Gouraud perde o pico especular que Phong encontra.
