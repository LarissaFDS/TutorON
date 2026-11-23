---
id: cg-aliasing-e-antialiasing-efeito-escada-supersampling-subpixels-mascara-ponderada-amostragem-por-area
titulo: Aliasing e antialiasing: efeito escada, superamostragem (supersampling) com subpixels, largura finita, pós-filtragem com máscara ponderada, amostragem por área (filtro caixa e cone)
assunto: cg-01-fundamentos-e-rasterizacao
tipo: material_estudo
questao: aula de Aliasing e Antialiasing e reavaliação da AB1 de 2014.2
resolucao: sim
fonte: Aulas de Computação Gráfica do Prof. Marcelo Costa Oliveira (IC-UFAL), 2012 a 2017
curso: Ciência da Computação (UFAL), COMP381 Computação Gráfica; aulas de 2012 a 2017 e provas de 2014 e 2021.2 (Prof. Marcelo Costa Oliveira)
fontes_catalogo: ufal-marcelo-aulas-cg
autoria: Slides do Prof. Marcelo Costa Oliveira (IC-UFAL); explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Gráfica (IC-UFAL), aula de Aliasing e Antialiasing e reavaliação da AB1 de 2014.2 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Aliasing:** distorção causada por amostrar uma primitiva contínua numa grade discreta de pixels. O sintoma clássico é o **efeito escada** (serrilhado) nas bordas de retas inclinadas.

**Antialiasing** suaviza a transição com tons intermediários:
- **superamostragem (supersampling):** divide cada pixel em $N$ subpixels, conta quantos são cobertos pela primitiva e dá ao pixel a intensidade proporcional. Com $3 \times 3 = 9$ subpixels e reta de largura zero, um pixel pode ter no máximo 3 subpixels marcados, isto é, 3 níveis de intensidade; com largura finita, até 9 níveis;
- **pós-filtragem com máscara ponderada:** os subpixels do centro pesam mais do que os da borda (por exemplo, máscara $3 \times 3$ com pesos 1, 2, 1 / 2, 4, 2 / 1, 2, 1, soma 16);
- **amostragem por área (pré-filtragem):** a intensidade é a área do pixel coberta pela primitiva; com **filtro caixa** todos os pontos do pixel pesam igual, com **filtro cone** o peso cai com a distância ao centro.

A cor final de um pixel parcialmente coberto é a média ponderada: com 3 de 9 subpixels vermelhos e 6 azuis, $\text{cor} = (3\,\text{vermelho} + 6\,\text{azul})/9$.

**Custo:** mais subpixels dão mais níveis e menos serrilhado, mas multiplicam a memória e o processamento.

**Verificação:** `test_supersampling` conta os subpixels cobertos numa grade $3 \times 3$ e confere que a máscara ponderada soma 16 e dá intensidade entre 0 e 1.
