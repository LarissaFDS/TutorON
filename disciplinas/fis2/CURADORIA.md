# Física 2 — curadoria do acervo

Situação: **em validação** desde 02/11/2026. A disciplina está cadastrada com acervo e índice próprios e passa pelo mesmo fluxo da IA que PAA, SD e OAC: mesmo modelo, mesmo backend e mesmo prompt de sistema, com as regras de [`rigor.md`](rigor.md) anexadas. Enquanto a validação não acontecer, o servidor recusa perguntas de Física 2 no atendimento normal (403). Para testes autorizados, use `TUTORON_LIBERAR_EM_VALIDACAO=fis2` (veja [`docs/DISCIPLINAS.md`](../../docs/DISCIPLINAS.md)).

| Item | Estado em 02/11/2026 |
|---|---|
| Cadastro, acervo (34 blocos, 30 na busca) e índice híbrido (`bge-m3`) | **Feitos** |
| Contas das resoluções e exemplos | **Conferidas por código** (`tests_acervo/test_disciplina_fis2.py`, SymPy e Python) |
| Revisão humana interna | **Pendente** (`revisao_humana: pendente` em todos os blocos) |
| Autorização para publicar transcrições das listas | **Não dada**: os blocos trazem enunciados parafraseados e os dados |
| Aprovação do professor | **Não declarada**; nenhum bloco tem `revisao_professor: sim` |
| Ementa ou plano de ensino | **Não localizado** (seção 1) |
| Validação das respostas da IA com um modelo | **Não feita** nesta entrega (seção 6) |

- Catálogo legível por máquina: [`fontes.json`](fontes.json)
- Blocos (um arquivo por bloco): [`materiais/`](materiais/). `s*` = anotações da turma no Notion, reescritas e corrigidas; `t*` = exercícios das listas da turma; `n*` = notas da equipe (candidatas, fora da busca)
- Gerados (não editar à mão): [`acervo/itens.json`](acervo/itens.json) e [`acervo/indice.json`](acervo/indice.json)

## 1. Ementa e professor

A lista de oscilações (`ufal-fis2-lista-oscilacoes`) tem o cabeçalho "Universidade Federal de Alagoas, Instituto de Física, Disciplina: Física II, Docente: Prof. Dr. Marconi Silva Santos Júnior". É a única evidência de instituição e docente. O projeto pedagógico com a ementa oficial de Física 2 **não foi encontrado** na busca pública; os tópicos abaixo seguem os capítulos 12–20 do livro usado pela turma (`halliday-fundamentos-vol2`) e a organização do Notion. A curadoria **não está validada pelo professor**.

## 2. Tópicos, evidência e blocos

| Assunto | Halliday, vol. 2 | Evidência da turma | Blocos |
|---|---|---|---|
| `fis2-01-equilibrio-elasticidade` | cap. 12 | Notion + lista com resolução | `fis2-notion-equilibrio`, `fis2-lista-equilibrio-q1`, `fis2-lista-equilibrio-q2`, `fis2-lista-equilibrio-q3`, `fis2-lista-equilibrio-q4`, `fis2-lista-equilibrio-q5`, `fis2-notion-q9-lista1`, `fis2-nota-escolher-metodo` |
| `fis2-02-gravitacao` | cap. 13 | Notion + lista | `fis2-notion-gravitacao-forca`, `fis2-notion-gravitacao-energia-kepler`, `fis2-lista-gravitacao-q1-q5` |
| `fis2-03-fluidos` | cap. 14 | Notion + lista | `fis2-notion-fluidos-hidrostatica`, `fis2-notion-fluidos-pascal-arquimedes`, `fis2-notion-fluidos-escoamento`, `fis2-lista-fluidos-q1`, `fis2-lista-fluidos-q2-q3`, `fis2-lista-fluidos-q4`, `fis2-lista-fluidos-q5`, `fis2-lista-fluidos-q6-q11` |
| `fis2-04-oscilacoes` | cap. 15 | Notion + lista do professor | `fis2-notion-mhs`, `fis2-notion-pendulos`, `fis2-lista-oscilacoes-q1-q4` |
| `fis2-05-ondas-i` | cap. 16 | Notion + notas de aula | `fis2-notion-ondas-progressivas`, `fis2-notion-ondas-estacionarias` |
| `fis2-06-ondas-ii-som` | cap. 17 | Notion + notas de aula | `fis2-notion-som-intensidade-tubos`, `fis2-notion-batimentos-doppler` |
| `fis2-07-temperatura-calor-primeira-lei` | cap. 18 | Notion | `fis2-notion-temperatura-calor`, `fis2-notion-primeira-lei`, `fis2-notion-transferencia-calor`, `fis2-nota-processos-termodinamicos` |
| `fis2-08-teoria-cinetica` | cap. 19 | Notion | `fis2-notion-gas-ideal-cinetica`, `fis2-notion-calores-especificos-adiabatica` |
| `fis2-09-entropia-segunda-lei` | cap. 20 | Notion | `fis2-notion-entropia`, `fis2-notion-maquinas-carnot` |

Não há listas anexadas para os capítulos 16–20; esses tópicos têm só as anotações.

**Pré-requisitos**: Física 1 (leis de Newton, energia, rotação e momento de inércia) e Cálculo 1 (derivada, integral simples, ln). **Fronteira com Cálculo 3**: aqui só aparecem integrais simples (força de uma barra, trabalho p dV, força numa parede); fluxo, divergente e integrais múltiplas ficam em Cálculo 3. "Fluxo" em Física 2 é vazão ($R_V = Av$), e a busca de cada disciplina usa só o seu acervo.

## 3. Inventário do Notion e dos anexos

Notion da turma (`ufal-fis2-notion`). Página principal: PDF do Halliday (não usado), 3 embeds do Miro (`ufal-fis2-miro`, não legíveis) e nove subpáginas por capítulo. Subpáginas internas: "Lista Equilíbrio" (só um link para `respondeai-equilibrio`), "Questão 9 Lista 1" (resolução do ChatGPT colada; bloco `fis2-notion-q9-lista1`, pendente), "Oscilações (Socorro)" (21 imagens, sem texto; não usada).

Anexos baixados só para leitura, fora do repositório, com sha256 no catálogo: `ufal-fis2-lista-equilibrio`, `ufal-fis2-lista-gravitacao`, `ufal-fis2-lista-fluidos`, `ufal-fis2-lista-oscilacoes`, `ufal-fis2-notas-ondas`, `ufal-fis2-notas-som`. As listas são enunciados impressos com resolução manuscrita de aluno. As notas de aula são manuscritas e sem autoria; serviram só para conferir fórmulas. Nenhuma imagem ou foto foi versionada; as fórmulas que estavam em imagem foram transcritas pela equipe e descritas em texto.

## 4. Erros encontrados nas anotações e como foram tratados

Cada bloco `s*` termina com "Correções da equipe".

| Página | Anotação | Correção |
|---|---|---|
| Fluidos | 1,01×10⁵ Pa = 750 torr | 760 torr |
| Fluidos | "Fe = Fg" como definição de empuxo | Empuxo = peso do fluido deslocado; Fe = Fg só flutuando em equilíbrio |
| Fluidos | "laminar" | Explicado: no Halliday, laminar = estacionário; em outros textos, laminar é o oposto de turbulento |
| Fluidos | "irrotacional (sem torque)" | Elemento do fluido não gira sobre o próprio centro de massa |
| Fluidos | Bernoulli e vazão só em imagem | Transcritos em LaTeX; o resumo da lista tem um termo ρv² a mais |
| Fluidos | "monométrica" | manométrica |
| Gravitação | Fr = GMm/(r+l) | GMm/(d(d+L)) |
| Gravitação | distância entre focos = dobro da excentricidade | 2ea |
| Gravitação | E = −K na elipse | Só na órbita circular; na elipse E = −GMm/(2a) |
| Oscilações | a = ω²x_m cos(…) | sinal negativo |
| Oscilações | f = v/d | removida (é de ondas: f = v/λ) |
| Oscilações | pêndulo simples com 2π√(I/mgL) | 2π√(L/g) |
| Oscilações | barra com I = mL²/12 e g = 8π²L/(3T²) | eixo na extremidade: I = mL²/3 |
| Temperatura | 1 mol = 6,02×10⁻³ | 6,02×10²³ |
| Teoria cinética | kT por grau de liberdade; E_int = nRT | ½kT; E_int = (f/2)nRT |
| Entropia | constante se o processo for irreversível | reversível |
| Ondas II | construtiva quando "f" é múltiplo de 2π | φ (fase) |

## 5. Resoluções das listas: status

| Bloco | Status | Motivo |
|---|---|---|
| `fis2-lista-equilibrio-q1`, `fis2-lista-equilibrio-q2`, `fis2-lista-equilibrio-q3`, `fis2-lista-equilibrio-q4`, `fis2-lista-equilibrio-q5` | validada | contas refeitas por código |
| `fis2-lista-fluidos-q1` | corrigida | o aluno escreve 0,074% em vez de 7,4% |
| `fis2-lista-fluidos-q2-q3`, `fis2-lista-fluidos-q6-q11` | validada | Q10 fora (depende da figura) |
| `fis2-lista-fluidos-q4` | corrigida | sinal escrito errado na pressão dos pés |
| `fis2-lista-fluidos-q5` | pendente_professor | geometria só na figura; bloco `candidato`, fora da busca |
| `fis2-lista-gravitacao-q1-q5` | corrigida | G arredondado (18,92 m → 19 m); Q2–Q4 dependem de figura |
| `fis2-lista-oscilacoes-q1-q4` | validada | resolução da equipe; a lista não tem gabarito |
| `fis2-notion-q9-lista1` | pendente_professor | resolução do ChatGPT com geometria inconsistente; `candidato` |

Nenhuma resolução é gabarito do professor; os blocos dizem isso no texto.

## 6. Notas da equipe e validação

`fis2-nota-escolher-metodo` e `fis2-nota-processos-termodinamicos` são `nota_da_equipe_ia` com `curadoria: candidato`: ficam fora da busca até revisão humana. Os blocos `s*` reescrevem material da turma (mesmo critério de OAC) e entram na busca com `revisao_humana: pendente`.

Respostas do tutor com um modelo (Gemini ou local) **não foram avaliadas** nesta entrega. A busca foi conferida por testes e por `eval/relevancia.py`.

## 7. Fontes externas

Nenhuma fonte externa foi ingerida. `openstax-university-physics-v1` e `openstax-university-physics-v2` são CC BY-NC-SA 4.0, mas o prefácio proíbe uso em IA generativa sem permissão: só referência. `mit-ocw-8-03sc`, `mit-ocw-8-01sc` e `mit-ocw-5-60` (CC BY-NC-SA 4.0) são leitura indicada; o 5.60 usa ΔU = q + w. `phet-simulacoes` e `hyperphysics` têm termos não verificados. `halliday-fundamentos-vol2` é protegido: não foi versionado, fragmentado nem ingerido.
