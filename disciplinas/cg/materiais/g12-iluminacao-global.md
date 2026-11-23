---
id: cg-iluminacao-global-ray-tracing-recursivo-arvore-de-raios-refletido-refratado-sombra-radiosidade-fator-de-forma
titulo: Iluminação global: ray tracing recursivo e árvore de raios (raios de sombra, refletidos e refratados), radiosidade, patches e fator de forma, pipeline da radiosidade
assunto: cg-03-modelagem-iluminacao-e-textura
tipo: prova
questao: aula de Modelos de Iluminação Global, AB2 de 2014.1 (questões 4, 5 e 8) e reavaliação da AB2 de 2021.2 (questão 2)
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
Computação Gráfica (IC-UFAL), aula de Modelos de Iluminação Global, AB2 de 2014.1 (questões 4, 5 e 8) e reavaliação da AB2 de 2021.2 (questão 2) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Por que global:** modelos locais só tratam fonte → superfície → olho; não mostram reflexos entre objetos, transparência nem sombras.

**Ray tracing recursivo:** para cada pixel lança-se um raio do olho; no ponto de interseção mais próximo lançam-se:
- **raio de sombra** até cada fonte: se bater num objeto opaco, o ponto está em sombra para essa fonte;
- **raio refletido**, na direção $\vec R = \vec D - 2(\vec D\cdot\vec N)\vec N$, se a superfície reflete;
- **raio refratado**, pela lei de Snell $\eta_1 \sin\theta_1 = \eta_2 \sin\theta_2$, se é transparente.

Os raios formam a **árvore de raios** do pixel; a cor é somada das folhas para a raiz, com os coeficientes de reflexão e transmissão. A recursão para numa profundidade máxima ou quando a contribuição fica pequena. Bom para reflexos especulares; depende do observador.

**Radiosidade:** trata as trocas **difusas** de energia. A cena é dividida em $n$ **patches** e resolve-se
$$B_i = E_i + \rho_i \sum_j F_{ij} B_j$$
($B$ radiosidade, $E$ emissão, $\rho$ refletância).

**Fator de forma $F_{ij}$:** fração da energia que sai do patch $i$ e chega ao patch $j$. É puramente **geométrico**: depende da distância, da orientação relativa e da visibilidade, não do observador. Vale a reciprocidade $A_i F_{ij} = A_j F_{ji}$ e, num ambiente fechado, $\sum_j F_{ij} = 1$. Custo: $n^2$ fatores.

**Pipeline:** geometria da cena → fatores de forma → propriedades de reflexão → solução das radiosidades → parâmetros de visualização → imagem. Como a solução não depende do observador, pode-se mudar a câmera sem recalcular.

**Verificação:** `test_radiosidade_e_reflexao` resolve um sistema de radiosidade com 2 patches, confere a reciprocidade e a fórmula do raio refletido.
