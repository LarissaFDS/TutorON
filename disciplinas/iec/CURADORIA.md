# Curadoria — Introdução à Engenharia de Computação (`iec`, ECOM006)

Situação: **MVP** desde 20/11/2026, sem aviso, por decisão da equipe, aceitando as falhas da IA registradas em `docs/DISCIPLINAS.md`.

## Disciplina e ementa

- ECOM006, 1º semestre, 60 h (40 teóricas e 20 práticas), Engenharia de Computação da UFAL.
- **Ementa conferida** no PPC de 2014 (`ufal-ppc-ecomp-2014`, p. 19 e 25 do PDF): histórico da engenharia; atribuições do engenheiro de computação; componentes básicos de um sistema de computação; linguagens de programação (conceituação e classificação); noções de software básico (sistema operacional, compilador, interpretador, montador, ligador e carregador); representação interna dos dados e sistemas de numeração; noções de sistemas embarcados e automação. Bibliografia básica: Fedeli, Polloni e Peres; Cocian; Forbellone e Eberspacher; Tanenbaum.
- Professor: não identificado (as provas não trazem nome).
- As provas de 2016.1 cobram também **portas lógicas, Karnaugh, circuitos combinacionais e redes (TCP/IP, DNS, IPv4)**, que não estão na ementa de 2014. Esses tópicos entraram porque há material da turma.

## Fronteira com Sistemas Digitais e OAC

Numeração, Boole, Karnaugh e combinacionais se sobrepõem a Sistemas Digitais (`sd`), e os níveis de máquina a OAC (`oac`). Decidimos **criar a disciplina** em vez de só complementar SD porque metade das provas (software básico, SO, redes, IEEE 754 aplicado a variáveis de programa) não cabe em SD, e o aluno do 1º período escolhe a disciplina que está cursando. Ângulo introdutório de cada tópico:

| Tópico | Aqui (IEC) | Aprofundado em |
|---|---|---|
| Numeração | conversões com método, IP em binário/hex | SD (aritmética, overflow) |
| Representação | complemento de 2 e IEEE 754 de variáveis `int`/`float` | SD e OAC |
| Portas e Boole | tabelas-verdade, fatoração, ler um circuito | SD |
| Karnaugh | 3 e 4 variáveis, sem projeto | SD (irrelevâncias, projeto) |
| Combinacionais | somadores e comparador de igualdade | SD (MUX, decodificadores, RTL) |
| Níveis de máquina | os seis níveis de Tanenbaum | OAC |

O rigor diz isso ao tutor, e `tests_acervo/test_disciplina_iec.py` testa o isolamento nos dois sentidos com SD, OAC, Programação 1 e Discreta.

## Fotos de provas e dados pessoais

- 6 fotos (Reavaliação AB1, 5 questões; Reavaliação AB2, 10 questões) foram lidas e parafraseadas; **nenhuma imagem está no repositório**. O campo "Nome" das provas está em branco; nenhuma pessoa aparece.
- O circuito da AB1, Q4, foi descrito em texto porta a porta a partir da foto ampliada; a leitura das ligações é da equipe.

## Fontes (`fontes.json`)

| id | Uso | Licença |
|---|---|---|
| `ufal-ppc-ecomp-2014` | citada (ementa) | Documento institucional público |
| `ufal-iec-reav-ab1-2016` | acervo | Não declarada (prova da disciplina) |
| `ufal-iec-reav-ab2-2016` | acervo | Não declarada (prova da disciplina) |
| `pearson-tanenbaum-slides` | acervo (só paráfrase) | Protegido (© 2014 Pearson) |
| `usp-baranauskas-boole` | acervo | Não declarada |
| `unicamp-deaecto-combinacionais` | acervo | Não declarada |
| `pucrs-vargas-circuitos-digitais` | referencia | Não declarada |
| `tanenbaum-livro` | referencia | Protegido; não incluído |
| `rfc-791` | citada | RFC, distribuição ilimitada |
| `rfc-1035` | citada | RFC, distribuição ilimitada |
| `maziero-so` | citada | CC BY-NC-SA (versão 3.0 ou 4.0 a confirmar) |
| `wikilivros-eletronica-digital` | referencia | CC BY-SA 4.0 |
| `confea-atribuicoes` | indisponivel | documento não obtido |
| `sbc-referenciais` | indisponivel | documento não obtido |

Nenhum material desta pasta tem licença aberta declarada: todos os blocos são paráfrases com exemplos próprios, sem figuras. **Confirmar com a equipe** se os slides da Pearson, de Baranauskas e de Deaecto podem continuar como base de paráfrase. O livro de Tanenbaum não foi buscado, transcrito nem ingerido.

Matriz de critérios (como nas disciplinas anteriores): alta = material da turma ou ementa; média = fonte aberta que confere conceitos; referência = consulta.

## Blocos (16, todos `material_da_disciplina`, todos na busca)

Nenhum bloco é `nota_da_equipe_ia`. Todos têm `revisao_humana: pendente` e nenhum tem revisão do professor. Todas as resoluções são `validada`: contas, expressões e circuitos recalculados por força bruta em `tests_acervo/test_disciplina_iec.py`; as questões conceituais (redes, SO) conferidas com RFC 791 e Maziero.

| Bloco | Assunto | Origem |
|---|---|---|
| `iec-niveis-de-maquina` | iec-02 | slides Tanenbaum cap. 3, slide 2 |
| `iec-portas-logicas` | iec-07 | slides Tanenbaum cap. 3 |
| `iec-algebra-boole-fatoracao` | iec-07 | Baranauskas, slides 7–20 |
| `iec-formas-canonicas` | iec-07 | Baranauskas, slides 21–27 |
| `iec-circuito-para-tabela-verdade` | iec-07 | Reavaliação AB1, Q4 |
| `iec-karnaugh-3-variaveis` | iec-08 | Baranauskas, slides 62–70 |
| `iec-karnaugh-4-variaveis` | iec-08 | Baranauskas, slides 90 e 94 |
| `iec-somadores` | iec-09 | Deaecto, p. 40–47 |
| `iec-comparador-2-bits` | iec-09 | Reavaliação AB1, Q5 |
| `iec-conversao-bases-ip` | iec-05 | Reavaliação AB1, Q1; Apêndice A |
| `iec-sistemas-numeracao-negativos` | iec-05 | Apêndice A |
| `iec-complemento-de-2-e-float` | iec-06 | Reavaliação AB1, Q2 |
| `iec-fracoes-binarias-ieee754` | iec-06 | Reavaliação AB1, Q3 |
| `iec-redes-tcpip-www-dns` | iec-10 | Reavaliação AB2, Q1, Q2, Q3, Q7, Q8 |
| `iec-ipv4-classe-c-mascara-broadcast` | iec-10 | Reavaliação AB2, Q9 |
| `iec-software-basico-so-compilacao` | iec-04 | Reavaliação AB2, Q4, Q5, Q6, Q10 |

## Tópicos sem bloco

Sem material da turma e sem fonte aberta conferida, ficaram sem bloco (o tutor diz que a resposta não veio do material): `iec-01-historia-atribuicoes` (os documentos do Confea e da SBC não abriram), `iec-03-linguagens-programacao` e `iec-11-embarcados-automacao`. Pendente: obter o plano de curso do professor e fontes para esses tópicos.
