# Curadoria — Física Experimental 3

Situação: **MVP** desde 24/11/2026 (fila do 4º período de Engenharia de Computação).
Revisão humana e do professor pendentes em todos os blocos.

## Origem e ementa
Pasta `Lab de Fisica 3` do material do 4º período de Engenharia de Computação da UFAL (ECOM026 Física
Experimental 3). O único material de aula é o roteiro do Experimento 2, "Campo a partir do potencial"
(Laboratório de Ensino do Instituto de Física, UFAL).

**Ementa não conferida.** A ementa oficial de ECOM026 não está no repositório e não foi inventada. O assunto
cadastrado saiu do roteiro (campo e potencial, equipotenciais).

## Critério para criar a disciplina
A regra da fila pedia material de aula para pelo menos quatro perguntas reais. O roteiro traz quatro questões
impressas (sentido da corrente entre as ponteiras, eletrostática com correntes iônicas, blindagem pelo anel e
bateria isolada no ar), além do procedimento. O teste `test_perguntas_reais_acham_o_bloco_certo` confere cinco
perguntas. O acervo é pequeno: os outros experimentos não têm roteiro na pasta.

## O que entrou
3 blocos, na busca, com status `pendente_professor` (não há gabarito oficial):
- `fislab3-exp2-equipotenciais-cuba`: objetivo, montagem, procedimento e por que as linhas de campo são
  perpendiculares às equipotenciais;
- `fislab3-exp2-blindagem-anel`: questão 3 (anel de latão como blindagem);
- `fislab3-exp2-correntes-e-bateria`: questões 1, 2 e 4.

A equação (2) do roteiro escreve E = ∇V sem o sinal de menos; os blocos usam E = −∇V e dizem isso.

## O que ficou de fora
- Relatórios 1 a 6 (`Relatório N - ...pdf`) e `fisica.ggb`: trabalhos de alunos; nem lidos além da identificação,
  nem versionados, nem citados.
- `Exemplo de relatório.pdf`: não é modelo do professor; é um relatório de alunos de outra instituição e de outro
  curso (química). Fora.
- `Figure_1.png`, `Figure_1_2.png`, `Figure_2.png`: figuras soltas, fora.
- Halliday (*Eletromagnetismo*): livro protegido citado no roteiro; só catálogo.

## Fronteiras
Física 3 (`fis3`): a teoria (Lei de Gauss, potencial de distribuições). Aqui fica a parte experimental.
