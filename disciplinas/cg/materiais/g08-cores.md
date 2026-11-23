---
id: cg-cores-e-sistemas-de-cores-rgb-cmy-hsv-aditivo-subtrativo-matiz-saturacao-valor-quantizacao
titulo: Cores e sistemas de cores: RGB (aditivo), CMY e CMYK (subtrativo, impressão), HSV (matiz, saturação, valor) e conversão; quantização de níveis de cinza (ENADE 2008)
assunto: cg-03-modelagem-iluminacao-e-textura
tipo: prova
questao: aula de Cores e Sistemas de Cores, questão de RGB e HSV da AB2 de 2014.1 e ENADE 2008 na AB1 de 2021.2
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
Computação Gráfica (IC-UFAL), aula de Cores e Sistemas de Cores, questão de RGB e HSV da AB2 de 2014.1 e ENADE 2008 na AB1 de 2021.2 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**RGB:** modelo **aditivo** dos monitores; cada cor é uma mistura de vermelho, verde e azul em $[0,1]$. $(1,1,1)$ é branco e $(0,0,0)$ é preto.

**CMY:** modelo **subtrativo** das tintas e impressoras (ciano, magenta, amarelo): $C = 1 - R$, $M = 1 - G$, $Y = 1 - B$. O **CMYK** acrescenta o preto (K) para economizar tinta e dar preto de verdade.

**HSV:** mais próximo de como se descreve uma cor:
- **H (matiz):** a cor pura, um ângulo de 0° a 360° (0° vermelho, 120° verde, 240° azul);
- **S (saturação):** pureza; $S = 0$ é cinza, sem cor;
- **V (valor, brilho):** $V = \max(R,G,B)$; $V = 0$ é preto.

**Comparação:** RGB é natural para o hardware, mas ruim para ajustar "mais claro" ou "menos saturado"; HSV separa cor, pureza e brilho, por isso é usado em seletores de cor. Os dois descrevem o mesmo conjunto de cores do dispositivo.

**ENADE 2008:** duas imagens de $246 \times 300$ pixels, uma com 256 e outra com 4 níveis de cinza. Como a resolução (número de pixels) é a mesma, o atributo alterado é a **quantização** (número de níveis de intensidade), alternativa (b). Amostragem espacial seria mudar o número de pixels. 256 níveis usam 8 bits por pixel; 4 níveis, 2 bits.

**Verificação:** `test_cores` confere com `colorsys` a conversão de vermelho, verde e azul puros para HSV, $\text{CMY} = 1 - \text{RGB}$ e os 8 e 2 bits da questão do ENADE.
