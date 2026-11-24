# Curadoria — Cálculo 4

Situação: **MVP** desde 24/11/2026 (fila do 4º período de Engenharia de Computação).
Revisão humana e do professor pendentes em todos os blocos.

## Origem e ementa
Pasta `C4` do material do 4º período de Engenharia de Computação da UFAL (ECOM023 Cálculo 4). A prova 2 é do
Prof. Gleydson Santos da Silva (IC-UFAL).

**Ementa não conferida.** A ementa oficial de ECOM023 não está no repositório e não foi inventada. Os assuntos
saíram da prova 2 (cálculo vetorial: campos conservativos, integrais de linha e de superfície, Stokes e
divergência) e da aula de função impulso (transformada de Laplace). Isso confirma o que o `CURADORIA.md` de
Cálculo 3 supunha: integrais de linha, Green, Stokes e Gauss ficam em Cálculo 4.

## O que entrou
5 blocos, todos na busca:
- `calc4-p2-q1-campo-conservativo`, `calc4-p2-q2-area-esfera-superficie`, `calc4-p2-q3-stokes-plano` e
  `calc4-p2-q4-divergencia-caixa`: as quatro questões da prova 2 (`ufal-calc4-p2-gleydson`), parafraseadas, com
  status `pendente_professor` (a prova não tem gabarito);
- `calc4-impulso-delta-dirac-laplace`: anotações da aula de função impulso (`ufal-calc4-anotacoes-impulso`), com a
  EDO $y'' + 4y = \delta(t-\pi) - \delta(t-2\pi)$ resolvida pela equipe, status `validada`.

Resoluções da equipe conferidas com SymPy em `tests_acervo/test_disciplina_calc4.py`.

## O que ficou de fora
- `Resumo - Função Impulso (Delta de Dirac).pdf` (`ufal-calc4-resumo-impulso`): material de apresentação de
  autoria incerta; só referência.
- `impulse_function.html`: página solta, parece gerada por IA; só evidência do tópico.
- Stewart (`stewart-calculo-vol2`) e Boyce & DiPrima (`boyce-diprima-edo`): livros protegidos; só catálogo.
- `P3C3`, `Prova 3 - C3` e `C3.docx` estão na mesma pasta, mas são de Cálculo 3: a lista P3C3 entrou como
  complemento de `calc3`; a correção manuscrita é de aluno (só evidência); `C3.docx` é uma lista de frequência com
  notas e matrículas de alunos: fora, sem citação.

## Fronteiras
Cálculo 3 (`calc3`): curvas, derivadas parciais, gradiente, máximos e mínimos e integrais múltiplas. Sinais e
Sistemas (`sinais`): convolução, Fourier e função de transferência; a transformada de Laplace aparece nas duas, e
aqui fica o uso em EDO com impulso.
