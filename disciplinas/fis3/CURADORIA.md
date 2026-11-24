# Curadoria — Física 3

Situação: **MVP** desde 24/11/2026 (fila do 4º período de Engenharia de Computação).
Revisão humana e do professor pendentes em todos os blocos.

## Origem e ementa
Pasta `Fisica 3` do material do 4º período de Engenharia de Computação da UFAL (ECOM022 Física 3). A prova 1
(19/08/2025) é do Prof. Alexandre de Morais Carvalho (Instituto de Física, UFAL).

**Ementa não conferida.** A ementa oficial de ECOM022 não está no repositório e não foi inventada. Os dois
assuntos cadastrados saíram da prova 1 (Lei de Gauss e potencial elétrico).

## Critério para criar a disciplina
A pasta só tem a prova 1, com **duas** questões impressas (o quadro de notas tem quatro linhas, mas a folha só traz
as questões 1 e 2), e uma resolução manuscrita. A regra da fila pedia conferir se dá para responder pelo menos
quatro perguntas reais com o bloco certo. Dá: o teste `test_quatro_perguntas_reais_acham_o_bloco_certo` confere
quatro perguntas (campo dentro e fora do cilindro; potencial no eixo da coroa e a ideia de somar anéis). O
acervo é pequeno: os outros assuntos de Física 3 (capacitores, corrente, campo magnético, indução) não têm
material, e a busca devolve vazio neles.

## O que entrou
2 blocos, na busca, com status `pendente_professor` (não há gabarito oficial):
- `fis3-prova1-q1-gauss-cilindro`: campo de um cilindro maciço com ρ uniforme, dentro e fora;
- `fis3-prova1-q2-potencial-coroa`: potencial no eixo de uma coroa circular, V ≈ 103 V.

Fonte: `ufal-fis3-prova1-2025`. Resoluções da equipe conferidas com SymPy em `tests_acervo/test_disciplina_fis3.py`.
A resolução manuscrita que veio com a prova (`ufal-fis3-resolucao-prova1`, autoria não identificada) chega aos
mesmos resultados; ficou só como referência.

## O que ficou de fora
- `eletromagnetismo.html` e `guia_magnetismo.html`: páginas soltas que parecem geradas por IA; só evidência de
  tópicos (magnetismo), nunca bloco.
- Halliday (*Eletromagnetismo*, `halliday-eletromagnetismo`): livro protegido; só catálogo, por seção.

## Fronteiras
Física 1 (`fis1`): mecânica. Física 2 (`fis2`): fluidos, ondas e termodinâmica. Cálculo 4 (`calc4`): integrais de
superfície e teorema da divergência como matemática.
