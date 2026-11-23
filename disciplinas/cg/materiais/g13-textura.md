---
id: cg-mapeamento-de-textura-espaco-de-textura-coordenadas-s-t-mapeamento-inverso-texels-bump-mapping-procedural
titulo: Mapeamento de textura: espaço de textura (s,t) e texels, processo em três passos (parametrização, mapeamento inverso e média dos texels), textura por tabela e procedural, bump mapping (POSCOMP 2018), environment mapping
assunto: cg-03-modelagem-iluminacao-e-textura
tipo: prova
questao: aula de Mapeamento de Textura, AB2 de 2014.1 (questão 9) e reavaliação da AB2 de 2021.2 (questões 3 e 4)
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
status_resolucao: validada
revisao_humana: pendente
---
Computação Gráfica (IC-UFAL), aula de Mapeamento de Textura, AB2 de 2014.1 (questão 9) e reavaliação da AB2 de 2021.2 (questões 3 e 4) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Por quê:** modelos de iluminação não descrevem bem padrões e rugosidade (madeira, tijolo); a textura acrescenta detalhe sem aumentar a geometria.

**Espaço de textura:** imagem com coordenadas $(s, t) \in [0,1]^2$; cada elemento é um **texel**. A superfície é parametrizada, $(x,y,z) = F(s,t)$, e cada vértice recebe coordenadas de textura.

**Processo (três passos):**
1. **projeção do pixel na superfície:** os cantos do pixel são levados aos pontos correspondentes do objeto;
2. **mapeamento inverso:** esses pontos são levados ao espaço de textura pela parametrização, formando um quadrilátero de texels;
3. **média (filtragem):** a cor do pixel é a média dos texels cobertos, ponderada pela área. Sem filtragem aparece aliasing.

**Tipos:**
- **por tabela (imagem):** os valores vêm de uma matriz de texels;
- **procedural:** os valores vêm de uma função (ruído, xadrez, veios), sem guardar imagem e sem limite de resolução;
- **sólida (3D):** função de $(x,y,z)$, como se o objeto fosse esculpido no material;
- **bump mapping:** perturba a **normal** da superfície por uma função, mudando a iluminação sem mudar a geometria; resposta (C) da questão do POSCOMP 2018;
- **environment mapping:** reflete uma imagem do ambiente na superfície.

**Interpolação bilinear** de uma textura em $(s, t)$ com os 4 texels vizinhos suaviza a ampliação.

**Verificação:** `test_textura` faz o mapeamento de $(s,t)$ para texels com interpolação bilinear e confere o valor no centro de uma textura $2 \times 2$.
