# Curadoria — Álgebra Linear

Situação: **MVP** desde 23/11/2026 (fila do 2º período de Engenharia de Computação).
Revisão humana e do professor pendentes em todos os blocos.

## Origem e ementa
Pasta de Álgebra Linear (ECOM011) do material do 2º período de Engenharia de Computação da UFAL. A disciplina
também está no 3º período da matriz de Ciência da Computação.

A pasta tem:
- lista 1 (espaços vetoriais) e uma lista de ponto extra;
- lista 2 (base, dimensão, posto, mudança de base), quatro códigos-base em Python e dois áudios;
- um relatório de alunos com as respostas da parte em Python;
- aulas (determinantes, um exemplo de sistema linear) e imagens de multiplicação de matrizes;
- o Anton (Álgebra Linear com Aplicações) e o manual de soluções em inglês.

**Ementa não conferida.** A ementa oficial de ECOM011 não está no repositório e não foi inventada. Os
assuntos saíram das listas.

## O que entrou
5 blocos (`materiais/a01`–`a05`), todos na busca, em quatro assuntos: espaços vetoriais e subespaços; base,
dimensão e posto; mudança de base; álgebra linear em Python. Enunciados parafraseados; resoluções da equipe
conferidas com SymPy e NumPy em `tests_acervo/test_disciplina_alglin.py`.

**Código da lista 2:** os `.py` foram lidos e rodados. Na questão 1, o produto por escalar usava $|\beta|$ em vez
de $\beta$ (quebra a distributividade com escalares complexos); na questão 2, a função de combinação linear
ficou sem implementar (responde "não é combinação linear" até no caso 1, que é). Rodando a questão 1, 21
verificações deram `False`, parte delas só por comparar números com igualdade exata (`np.array_equal`). O bloco `a05` explica os erros sem copiar o código; o teste usa código próprio.

## O que ficou de fora
- Anton e manual de soluções: protegidos; só catálogo.
- `audio1.wav` e `audio2.wav`: não versionados nem transcritos.
- O relatório de alunos (tem nomes de pessoas) e as partes preenchidas por alunos nos `.py`.
- Lista 2, questão 6: as matrizes ficaram ilegíveis na extração do PDF.
- Questão 3 do código (ajuste de curva de força magnética): a função de ajuste está marcada no próprio código
  como hipotética.
- Aulas de determinantes e lista de ponto extra: imagens sem texto extraível; não conferidas.

## Fronteiras
Geometria Analítica (`ga`): vetores no plano e no espaço, retas, planos e cônicas.
