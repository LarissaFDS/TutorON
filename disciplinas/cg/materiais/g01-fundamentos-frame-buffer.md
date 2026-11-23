---
id: cg-fundamentos-areas-raster-pixel-frame-buffer-tabela-de-cores-lut-resolucao
titulo: Fundamentos: síntese, processamento e análise de imagens; raster, pixel e linha de varredura; memória do frame buffer, tabela de cores (LUT) e resolução gráfica
assunto: cg-01-fundamentos-e-rasterizacao
tipo: exercicio_resolvido
questao: aulas 1 e 2 e exercícios da aula de Fundamentos da CG
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
status_resolucao: corrigida
revisao_humana: pendente
---
Computação Gráfica (IC-UFAL), aulas 1 e 2 e exercícios da aula de Fundamentos da CG (parafraseado). Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Computação Gráfica** estuda a geração, a manipulação e a interpretação de modelos e imagens por computador. Subáreas:
- **síntese de imagens:** cria a imagem a partir de modelos geométricos (jogos, cinema, CAD);
- **processamento de imagens:** melhora uma imagem pronta (ruído, contraste);
- **análise de imagens:** extrai informação da imagem (OCR, reconhecimento).

**Raster:** matriz retangular de pontos; **pixel:** um ponto do raster; **linha de varredura (scan line):** uma linha de pixels. **Resolução gráfica:** $ndh \times ndv$ posições endereçáveis (horizontal × vertical) num retângulo de largura × altura em mm.

**Contas:**
- memória do frame buffer $= ndh \cdot ndv \cdot$ bits por pixel;
- uma **tabela de cores (LUT)** indexada por $d$ bits tem $2^d$ posições;
- para $c$ cores são precisos $\lceil \log_2 c \rceil$ bits.

**Exercício:** frame buffer de $20 \times 20$ pontos com 8 bits por pixel.
- a) memória: $20 \cdot 20 \cdot 8 = 3200$ bits $= 400$ bytes;
- b) a LUT indexada pelos 8 bits tem $2^8 = 256$ posições;
- c) 64 cores exigem $\log_2 64 = 6$ bits.

**Tamanho do pixel:** tela de $512 \times 512$ mm com $256 \times 256$ posições: cada pixel mede $512/256 = 2$ mm por lado; uma figura de 13 pixels ocupa $13 \cdot 2 \cdot 2 = 52$ mm² (não m²: a unidade vem dos milímetros da tela).

**Janela → coordenadas normalizadas:** num mundo de $400 \times 500$ m, o ponto $(x, y)$ vai para $(x/400,\ y/500)$; por exemplo $(100, 300) \mapsto (0{,}25;\ 0{,}6)$.

**Verificação:** `test_frame_buffer_e_lut` confere 3200 bits, 400 bytes, 256 posições, 6 bits, 52 mm² e a normalização dos pontos.
