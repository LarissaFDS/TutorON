# Curadoria: Eletrônica (`eletronica`)

Atualizado em 20/11/2026. O acervo tem 22 blocos em `materiais/`, e 19 deles estão na busca. Esses 19 são as anotações do aluno, parafraseadas, com cada resultado refeito por código em `tests_acervo/test_disciplina_eletronica.py`: SymPy para análise nodal, malhas do TBJ e conferência da hipótese de estado, e NumPy para médias e RMS numéricos e para a varredura do ceifador. Os outros 3 blocos são notas da equipe escritas com IA (`nota_da_equipe_ia`). Ficam como `candidato`, **fora da busca**, até passarem por revisão humana.

## 1. Ementa (PPC) e escopo

O PPC de Engenharia de Computação da UFAL (2014, `ufal-ppc-ecomp-2014`) define **ECOM035 Eletrônica** com 60 h: 40 teóricas e 20 práticas.

A ementa (p. 43) cobre:
- diodos e diodo Zener;
- circuitos com diodos;
- transistores: tipos, princípios, características e polarização;
- amplificadores e chaveamento;
- modelos de pequenos sinais;
- tiristores e optoeletrônicos;
- amplificador operacional;
- fontes de alimentação.

A bibliografia é Sedra e Smith (`sedra-smith-microeletronica`), Boylestad e Nashelsky (`boylestad-dispositivos-eletronicos`) e Cathey. Os três livros são protegidos e entram só no catálogo. O PDF do PPC é o mesmo já usado nas outras disciplinas (SHA-256 `31a3c6e7…`).

O cabeçalho de "Simulação de retificadores" indica como docente o Prof. João Raphael Souza Martins. Nenhum material do professor foi recebido, e ninguém da disciplina revisou o acervo.

## 2. Mapeamento de tópicos

| Tópico | Assunto | Evidência nas anotações | Na busca |
|---|---|---|---|
| 1 Diodo: modelos e estado | `eletronica-01-diodo-modelos` | Sim | sim |
| 2 Circuitos com diodo (portas, onda quadrada) | `eletronica-02-circuitos-diodo` | Sim | sim |
| 3 Retificadores (meia onda, ponte) | `eletronica-03-retificadores` | Sim; filtro capacitivo sem evidência | sim; filtro só em nota IA candidata |
| 4 Ceifadores e grampeadores | `eletronica-04-ceifadores-grampeadores` | Sim | sim |
| 5 Diodo Zener | `eletronica-05-zener` | a confirmar (nenhuma) | não (nota IA candidata) |
| 6 TBJ: regiões, β, Darlington | `eletronica-06-tbj-regioes` | Sim | sim |
| 7 Polarização do TBJ | `eletronica-07-tbj-polarizacao` | Sim | sim |
| 8 Pequenos sinais (modelo re, emissor comum) | `eletronica-08-pequenos-sinais` | Sim | sim |
| 9 MOSFET | `eletronica-09-mosfet` | a confirmar (nenhuma) | não (nota IA candidata) |

Estes temas da ementa não têm material nem nota: amplificador operacional, tiristores, optoeletrônicos e fontes de alimentação. O `rigor.md` manda a IA dizer que esses temas não são cobertos pelas anotações da turma.

## 3. Inventário (9 PDFs, 47 páginas, `ufal-eletronica-anotacoes-otavio-2026-2`)

Os PDFs são anotações manuscritas digitalizadas, sem texto extraível, e foram lidos página por página. Ficam fora do repositório, assim como as fotos de quadro, de slides e as figuras de livro coladas neles. Os enunciados vindos do livro foram parafraseados.

| PDF | Conteúdo | Blocos |
|---|---|---|
| Simulação de retificadores | Meia onda e ponte no Falstad (220 V RMS, 10 Ω) | `eletronica-anot-meia-onda`, `eletronica-anot-onda-completa-ponte` |
| Diodos | Modelos, polarização, pico e RMS | `eletronica-anot-diodo-modelos` |
| Exercícios | Porta AND com diodos, onda quadrada, pontes, ceifador | `eletronica-anot-porta-and-diodos`, `eletronica-anot-diodo-serie-quadrada`, `eletronica-anot-ponte-100v-piv`, `eletronica-anot-ponte-resistores`, `eletronica-anot-ponte-resistores-quadro`, `eletronica-anot-ceifador-paralelo` |
| Revisão prova 1 | Retificadores, PIV, RMS | `eletronica-anot-meia-onda` (correção) |
| Aplicações de diodos | Grampeadores e projeto | `eletronica-anot-grampeadores`, `eletronica-anot-projeto-grampeador` |
| Transistores: polarização fixa | Ponto Q, saturação, projeto de RB e RC | `eletronica-anot-polarizacao-fixa`, `eletronica-anot-projeto-rb-rc` |
| Exercício parte 2 | Emissor, tensões de nó, realimentação (marcado pelas próprias anotações como errado) | `eletronica-anot-emissor-tensoes-nos`, `eletronica-anot-realimentacao-coletor` |
| Circuitos de Polarização de Transistores | Emissor, divisor, Darlington | `eletronica-anot-polarizacao-emissor`, `eletronica-anot-divisor-tensao`, `eletronica-anot-darlington` |
| Transistor TBJ | Curva com VA, modelo re | `eletronica-anot-modelo-re` |

O exercício "Exercício parte 2" foi refeito do zero.

## 4. Erros encontrados e status

| Bloco | Status | O que diverge das anotações |
|---|---|---|
| `eletronica-anot-diodo-modelos` | corrigida | A polarização era justificada pelo sentido da corrente. A tensão de 220 V é RMS, não pico; o pico é 311 V. |
| `eletronica-anot-porta-and-diodos` | validada | |
| `eletronica-anot-diodo-serie-quadrada` | validada | |
| `eletronica-anot-meia-onda` | corrigida | A revisão usava $I_{rms} = I_{med}/2$. O certo é $I_{max}/2$, que dá 15,5 A em vez de 4,9 A. |
| `eletronica-anot-onda-completa-ponte` | validada | |
| `eletronica-anot-ponte-100v-piv` | validada | |
| `eletronica-anot-ponte-resistores` | validada | Conferida por análise nodal nos dois semiciclos. |
| `eletronica-anot-ponte-resistores-quadro` | pendente_professor | A topologia no quadro está ilegível. A leitura adotada é o divisor por três (56,67 V de pico, 36,04 V de média). |
| `eletronica-anot-ceifador-paralelo` | corrigida | Faltava o joelho: abaixo de $v_i = 1{,}4$ V a saída é $v_i/2$. A corrente é 9,3 mA. |
| `eletronica-anot-grampeadores` | validada | A página "Grampeadores" tinha o slide do ceifador colado (só imagem, não usada). |
| `eletronica-anot-projeto-grampeador` | validada | |
| `eletronica-anot-polarizacao-fixa` | validada | Inclui a conferência de saturação com β = 120. A queda de VCE ao dobrar β é −76 % (as anotações traziam −75 %). |
| `eletronica-anot-polarizacao-emissor` | validada | IC sobe 81 % ao dobrar β. |
| `eletronica-anot-emissor-tensoes-nos` | corrigida | VB e VC foram tomadas como quedas nos resistores, e VCE saiu com o sinal trocado. O certo é VE = 2,046 V, VB = 2,746 V, VC = 15,99 V, VCE = +13,94 V e VBC = −13,24 V. |
| `eletronica-anot-divisor-tensao` | validada | |
| `eletronica-anot-realimentacao-coletor` | corrigida | A corrente IE passa por RC e por RE. O exemplo estava incompleto e foi terminado: VCE = 3,65 V, ou 3,72 V com a aproximação IE ≈ IC. |
| `eletronica-anot-darlington` | validada | |
| `eletronica-anot-projeto-rb-rc` | validada | RB = 361,6 kΩ; a anotação tinha 361,4 kΩ. |
| `eletronica-anot-modelo-re` | corrigida | $r_e \approx V_A/I_{CQ}$ é na verdade $r_o$, e $A_v$ divide por $r_e$, não por $r_o$. Resultado: Av = −280, ou −264 com ro = 50 kΩ. |

Notas da equipe (IA), todas `candidato`, `pendente_professor` e fora da busca:
- `eletronica-nota-ia-zener`, apoiada em `lec-vol3-semiconductors`;
- `eletronica-nota-ia-filtro-capacitivo`, apoiada em `lec-vol3-semiconductors`;
- `eletronica-nota-ia-mosfet`, apoiada em `mit-ocw-6-012`.

## 5. Fontes e licenças

| Fonte | Uso | Licença |
|---|---|---|
| `ufal-eletronica-anotacoes-otavio-2026-2` | acervo | Não declarada. A transcrição parafraseada foi autorizada pelo autor em 18/11/2026; a aprovação do professor não foi declarada. |
| `ufal-ppc-ecomp-2014` | referência | Documento institucional público |
| `lec-vol3-semiconductors` | citada | CC BY 4.0 |
| `mit-ocw-6-012` | citada | CC BY-NC-SA 4.0 |
| `mit-ocw-6-002` | referência | CC BY-NC-SA 4.0 |
| `falstad-circuitjs` | referência | Código sob GPL-2.0+; a página do simulador não declara licença |
| `ngspice` | referência | Não declarada na página. O ngspice não foi instalado nem usado. |
| `boylestad-dispositivos-eletronicos` | referência | Protegido |
| `sedra-smith-microeletronica` | referência | Protegido |

## 6. Fronteiras

- Kirchhoff, Thévenin e divisores são de Circuitos Elétricos (`circ`). Aqui são usados sem ser reensinados.
- Portas lógicas e Karnaugh são de Sistemas Digitais (`sd`).
- A porta AND com diodos fica em Eletrônica porque o assunto é o estado dos diodos.
- Os testes conferem o isolamento nos dois sentidos.

## 7. Pendências reais

- Falta a revisão humana e a do professor em todos os blocos. Nenhum bloco está marcado como revisado.
- A topologia do exercício 31 precisa ser confirmada.
- Zener, filtro capacitivo e MOSFET só têm notas IA fora da busca.
- Amp-op, tiristores, optoeletrônicos e fontes não têm material.
- Nenhuma conta foi conferida em SPICE, só em SymPy e NumPy.
