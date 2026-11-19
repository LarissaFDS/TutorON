# Curadoria — Circuitos Elétricos (`circ`)

Atualizado em 19/11/2026. O acervo tem 26 blocos em `materiais/`. Destes, 23 estão na busca: são as anotações do aluno, parafraseadas e com cada resolução refeita por código. Os outros 3 são notas da equipe escritas com IA (`nota_da_equipe_ia`). Elas ficam como `candidato`, **fora da busca**, até passarem por revisão humana.

## 1. Ementa (PPC) e escopo

O PPC de Engenharia de Computação da UFAL (2014, `ufal-ppc-ecomp-2014`, p. 39) define **ECOM028 Circuitos Elétricos**: 60 h, sendo 40 teóricas e 20 práticas. A ementa transcrita é: elementos de circuitos lineares; lei de Ohm; leis de Kirchhoff; métodos de análise; teoremas; circuitos de primeira ordem; excitação senoidal; fasores; análise em regime permanente CA; potência em regime permanente CA; síntese de circuitos.
- Bibliografia básica: Nilsson e Riedel (`nilsson-riedel-circuitos`), Hayt e Burian.
- Bibliografia complementar: O’Malley e Kienitz.

Não foi possível baixar de novo o PDF do PPC em 19/11/2026: houve tempo esgotado e erro 502. A ementa acima foi lida na cópia baixada em 18/11/2026 para Probabilidade, que tem o mesmo SHA-256.

O que a turma estudou não coincide inteiro com a ementa:
- **Segunda ordem** (RLC) está nas anotações e nas listas AB2, mas **não** aparece na ementa de 2014.
- **Amp-op** não aparece nem na ementa nem nas anotações. Mesmo assim é tema clássico do curso (Nilsson, capítulo 5), por isso entrou como assunto, sem material aprovado.
- **Primeira ordem e fasores** estão na ementa, mas não têm resolução nas anotações. Primeira ordem aparece só como condições iniciais dentro dos problemas de segunda ordem.

Os cabeçalhos das listas AB1 e AB2 citam o **Prof. Jobson de Araújo Nascimento**. Nenhum material do professor foi recebido e ele não revisou o acervo.

## 2. Inventário das anotações (`ufal-circ-anotacoes-otavio-2026-1`)

O autor é Otávio Joshua Costa Brandão Menezes, aluno da turma de 2026.1 e membro da equipe. São anotações de estudo: **não são material do professor nem gabarito**.

**Autorização:** o autor autorizou publicar a transcrição, segundo informação da responsável pela curadoria em 18/11/2026; o registro está em `fontes.json` > `autorizacao_transcricao`. Mesmo assim:
- os enunciados de livros e de provas foram **parafraseados**;
- as fotos de quadro e as figuras coladas foram descritas em texto, não copiadas;
- os PDFs e as imagens ficam fora do repositório.

| Arquivo (data AAMMDD) | Conteúdo | Blocos |
|---|---|---|
| `Introdução à Circuitos Elétricos_260305_151403.pdf` | carga, corrente, tensão, Ohm, série e paralelo | `circ-anot-grandezas-ohm` |
| `Potência e Leis de Kirchoff_260312_152549.pdf` | potência, convenção passiva, LKC, LKT, nodal, malhas | `circ-anot-potencia-convencao-passiva`, `circ-anot-nodal-lista2-q1`, `circ-anot-nodal-duas-fontes`, `circ-anot-malhas-fonte-dependente` |
| `Máxima Transferência de Potência_260428_162126.pdf` | lista 4: condição $R_L = R_{Th}$, alto-falantes, $v_\phi$, Y-Δ | `circ-anot-maxima-transferencia`, `circ-anot-maxima-transferencia-vphi`, `circ-anot-maxima-transferencia-y-delta` |
| `Teorema de Thévenin e Norton_260428_171421.pdf` | exercícios 1, 2, 5, 6, 7, 9, 11 e 12 | `circ-anot-thevenin-norton-basicos`, `circ-anot-thevenin-ex2`, `circ-anot-thevenin-ex12`, `circ-anot-thevenin-fonte-dependente`, `circ-anot-thevenin-dependentes-ex6-ex11` |
| `Questões circuitos_260501_111748.pdf` | superposição com três fontes; segunda tentativa da AB1 Q3; repetição da prova antiga | `circ-anot-superposicao-tres-fontes` (e parte de `circ-anot-superposicao-superno-ab1-q3`) |
| `Lista para AB1_260501_213420.pdf` | lista do professor, questões 1 a 5 | `circ-anot-nodal-ab1-q1-q2`, `circ-anot-superposicao-superno-ab1-q3`, `circ-anot-transformacao-fontes-ab1-q4`, parte de `circ-anot-maxima-transferencia` |
| `Questões para a prova 2_260517_161546.pdf` | Thévenin com $6i_0$ (questão de prova antiga) | `circ-anot-thevenin-prova-antiga` |
| `Lista para AB 2_260616_174145.pdf` | RLC crítico e superamortecido | `circ-anot-rlc-ab2-q1`, `circ-anot-rlc-ab2-q2` |
| `Circuitos de Segunda Ordem_260618_093824.pdf` | teoria de segunda ordem e lista de revisão | `circ-anot-segunda-ordem-conceitos`, `circ-anot-rlc-revisao-q1`, `circ-anot-rlc-revisao-q2` |

### Erros encontrados e status de cada resolução

A equipe refez todas as resoluções com análise nodal modificada exata (SymPy, `tests_acervo/circ_mna.py`). Para cada uma, fechou também o balanço de potências. As de segunda ordem foram refeitas com `dsolve`.

| Bloco | Status | O que estava nas anotações | Correção |
|---|---|---|---|
| `circ-anot-grandezas-ohm` | corrigida | $V_i = IR_i$ chamado de corrente | é a tensão no resistor $i$ |
| `circ-anot-superposicao-superno-ab1-q3` | corrigida | segunda tentativa com $-\tfrac{32}{6} - 16 = -\tfrac{128}{6}$ V, potências sem fechar | $v_x = -\tfrac{80}{3}$ V; balanço fecha |
| `circ-anot-thevenin-ex2` | corrigida | $R_{Th} = 40$ Ω | $R_{Th} = 25$ Ω ($V_{Th} = -2$ V confere) |
| `circ-anot-segunda-ordem-conceitos` | corrigida | $e^{at}(A\cos bt + B\sin bt)$ chamado de solução particular | é a solução homogênea (natural) |
| `circ-anot-rlc-revisao-q1` | corrigida | resolução para antes da segunda constante | equipe completou: $i = -9{,}6te^{-20t}$ A |
| `circ-anot-nodal-lista2-q1` | validada | sinal trocado num passo intermediário; equação final certa | resultado mantido ($v_1 = 32$ V, $v_2 = 16$ V) |
| `circ-anot-thevenin-dependentes-ex6-ex11` | validada | $R_{Th}$ do exercício 6 não calculado; do 11 não feito | equipe calculou $R_{Th} = 10$ Ω no 6; no 11 só $V_{ab} = 3$ V entra |
| demais blocos `circ-anot-*` | validada | — | resultado das anotações confere com o código |

Também ficou um erro de vocabulário: as anotações chamam de "superposição" o ato de zerar as fontes. Ele foi esclarecido no texto de `circ-anot-superposicao-tres-fontes` e em `rigor.md`.

### O que não entrou

- Foto do quadro e primeira página riscada de "Questões circuitos".
- Enunciados colados na pág. 7, que não têm resolução.
- Exemplo de $I_x$ incompleto em "Potência".
- Lista 4, questão 1 ($60i_\alpha$), só parcial.
- Lista 6, questão 9, incompleta.
- Último problema de 1 H, 1 F e 3 A: topologia ambígua e sem fim.
- Circuito de 8 V e 40 V da prova antiga, sem enunciado.
- No exercício 11, uma $R_{Th}$ que a equipe tentou calcular com topologia incerta.

## 3. Notas da equipe (IA, fora da busca)

| Bloco | Assunto | Situação |
|---|---|---|
| `circ-nota-ia-amp-op` | amp-op ideal | candidato, revisão humana pendente |
| `circ-nota-ia-primeira-ordem` | RC e RL | candidato, revisão humana pendente |
| `circ-nota-ia-fasores` | fasores e impedância | candidato, revisão humana pendente |

## 4. Mapa de assuntos

| Assunto | Na busca | Origem |
|---|---|---|
| `circ-01-grandezas-potencia` | sim | anotações |
| `circ-02-kirchhoff-nodal-malhas` | sim | anotações |
| `circ-03-superposicao-transformacao` | sim | anotações |
| `circ-04-thevenin-norton` | sim | anotações |
| `circ-05-maxima-transferencia` | sim | anotações |
| `circ-06-amp-op` | não | só nota IA candidata |
| `circ-07-primeira-ordem` | parcial | condições iniciais dentro de `circ-08`; nota IA candidata |
| `circ-08-segunda-ordem` | sim | anotações |
| `circ-09-fasores` | não | só nota IA candidata |

## 5. Catálogo de fontes

`ufal-circ-anotacoes-otavio-2026-1` (acervo), `ufal-ppc-ecomp-2014` (ementa), `kuphaldt-lessons-electric-circuits` (Design Science License), `mit-ocw-6-002-2007` (CC BY-NC-SA 4.0), `libretexts-fiore-dc-analysis` (CC BY-NC-SA 4.0), `falstad-circuit-simulator` (ferramenta) e `nilsson-riedel-circuitos` (protegido, só referência). Nenhuma fonte aberta foi ingerida nesta versão. ngspice e All About Circuits responderam 403 e não entraram.

## 6. Pendências

- Revisão humana de todos os blocos (`revisao_humana: pendente`); confirmação do professor, que não foi pedida.
- Material da turma para amp-op, primeira ordem e fasores; revisão das três notas IA.
- Nova tentativa de baixar o PPC direto do site do IC.
