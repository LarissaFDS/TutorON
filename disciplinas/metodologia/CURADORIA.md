# Metodologia da Pesquisa e do Trabalho Científico — curadoria do acervo

Situação: **em validação**. Usa o mesmo fluxo e a mesma IA das outras disciplinas; só acrescenta acervo, `rigor.md` e testes. Nenhum modelo, provedor ou prompt próprio.

| Item | Estado em 21/11/2026 |
|---|---|
| Cadastro, acervo (22 blocos) e índice híbrido (`bge-m3`) | **Feitos**; 16 blocos na busca, 6 notas da equipe com IA fora dela |
| Exemplos LaTeX | **Compilados** com pdflatex e bibtex no TeX Live 2026 (`tests_acervo/test_disciplina_metodologia.py`) |
| Gabarito do professor | **Não existe** no material recebido |
| Professor da turma | **Não identificado** |
| Revisão humana interna | **Pendente** em todos os blocos |
| Aprovação do professor | **Não declarada**; nenhum bloco tem `revisao_professor: sim` |
| Ementa oficial | **Conferida** no PPC de 2014 |

- Catálogo legível por máquina: [`fontes.json`](fontes.json)
- Blocos: [`materiais/`](materiais/)
- Gerados a partir dos blocos (não editar à mão): [`acervo/itens.json`](acervo/itens.json) e [`acervo/indice.json`](acervo/indice.json)
- Regras de rigor do tutor: [`rigor.md`](rigor.md)
- Imagem TeX dos testes: [`tests_acervo/latex_metodologia/Dockerfile`](../../tests_acervo/latex_metodologia/Dockerfile)

## 1. Disciplina, ementa e material

O PPC de Engenharia de Computação de 2014 (`ufal-ppc-ecomp-2014`, grade na p. 20 e ementa nas p. 33 e 34 do PDF) lista **ECOM018 Metodologia da Pesquisa e do Trabalho Científico**, 3º semestre, 30 h (20 teóricas e 10 práticas). A ementa, resumida: ciência e conhecimento científico; ciência e tecnologia; pesquisa científica, teorias e validação; metodologia; tipos, métodos e técnicas de pesquisa; problema e hipóteses; estudos exploratórios e referencial teórico; expressão oral e escrita; projeto e relatório de pesquisa; ferramentas auxiliares; redação científica e apresentação de trabalhos. A bibliografia (Marconi e Lakatos, Ruiz, Eco, Latour, Appolinário, Diógenes, Volpato, Costa) não foi recebida e não está no acervo.

Material da turma (originais fora do repositório):

| Fonte | Autoria | Licença | Uso |
|---|---|---|---|
| `alves-arruda-2004-artigo` | Alves e Arruda, BU/UFSC, 2004 (NBR 6022:2003) | Não declarada | Só paráfrase; o PDF traz e-mails das autoras, não versionados |
| `lopez-silva-2013-latex` | Lopez e Silva, UFRJ, 2013, v. 1.2a | CC BY-SA 3.0 | Exemplos adaptados; os blocos herdam a licença |
| `wilkins-1995-latex` | Wilkins, Trinity College Dublin, 1995 | Copyright, sem licença aberta | Só paráfrase |

O JabRef-2.10.jar da turma não foi incluído nem baixado; a ferramenta é citada como `jabref`.

### Tópicos, evidência e blocos

| Assunto | Evidência | Blocos na busca | Notas da equipe com IA (fora da busca) |
|---|---|---|---|
| `metodologia-01-ciencia-conhecimento` | Ementa | — | `metodologia-nota-ciencia-conhecimento` |
| `metodologia-02-tipos-metodos-pesquisa` | Ementa | — | `metodologia-nota-tipos-pesquisa` |
| `metodologia-03-problema-hipotese-projeto` | Ementa | — | `metodologia-nota-problema-hipotese-projeto`, `metodologia-nota-revisao-bibliografica` |
| `metodologia-04-estrutura-artigo-monografia` | Modelo de artigo; apostila (abnTeX2) | `metodologia-artigo-estrutura`, `metodologia-artigo-secoes-textuais`, `metodologia-resumo-palavras-chave`, `metodologia-monografia-abntex2` | — |
| `metodologia-05-normas-abnt-citacoes-referencias` | Modelo de artigo | `metodologia-abnt-citacoes`, `metodologia-abnt-referencias`, `metodologia-abnt-ilustracoes-tabelas-secoes` | — |
| `metodologia-06-latex-basico` | Apostila; Wilkins | `metodologia-latex-documento-minimo`, `metodologia-latex-compilacao-erros`, `metodologia-latex-listas-citacao-longa` | — |
| `metodologia-07-latex-figuras-tabelas-matematica` | Apostila; Wilkins | `metodologia-latex-figura-legenda`, `metodologia-latex-tabela`, `metodologia-latex-matematica` | — |
| `metodologia-08-referencias-bibtex-jabref` | Apostila | `metodologia-bibtex-arquivo-bib`, `metodologia-bibtex-abntex2cite` | `metodologia-nota-jabref` |
| `metodologia-09-apresentacao-trabalhos` | Ementa; apostila (beamer) | `metodologia-apresentacao-beamer` | — |
| `metodologia-10-etica-plagio` | Ementa (redação científica), interpretação | — | `metodologia-nota-etica-plagio` |

Todo tópico com material da turma tem bloco na busca. Os tópicos 01, 02, 03 e 10 só têm notas `nota_da_equipe_ia` com `curadoria: candidato`: entram na busca só depois de revisão humana.

## 2. Fronteiras

- **Inglês Instrumental** (`ingles`): leitura de artigos em inglês fica lá; aqui ficam escrita, normas e LaTeX. O isolamento é testado nos dois sentidos.
- As normas ABNT (`abnt-normas`) são protegidas: os blocos citam número e edição, explicam com palavras próprias e conferem em guias de bibliotecas.

## 3. Status das resoluções e correções

- **validada**: o exemplo compila e o texto confere com a fonte.
- **corrigida**, com justificativa no próprio bloco:
  - `metodologia-latex-figura-legenda`: a apostila põe `\label` antes de `\caption`; o número sai errado (contraprova no teste).
  - `metodologia-bibtex-arquivo-bib`: `@Online` só existe no biblatex; com BibTeX vira `@misc` (contraprova no teste).
  - `metodologia-abnt-referencias`: a NBR 6023:2018 tirou os sinais < > do endereço (conferido em `ufscar-manual-nbr6023-2018`).
  - `metodologia-abnt-ilustracoes-tabelas-secoes`: identificação das ilustrações na parte superior (conferido em `ufv-normalizacao-2024`).
- **pendente_professor**: `metodologia-artigo-estrutura` (6022:2003 → 2018, conferido em `ufc-guia-artigo-2018`), `metodologia-resumo-palavras-chave`, `metodologia-abnt-citacoes` (10520:2002 → 2023, conferido em `ufc-guia-citacao-2025` e `unifor-nbr10520-2023`) e `metodologia-bibtex-abntex2cite` (o abntex2cite ainda imprime o sobrenome em maiúsculas). Falta o professor dizer qual edição a turma adota.
- A opção `brazil` do babel, usada na apostila, está obsoleta: todos os exemplos usam `brazilian`.

Outras fontes de conferência: `wikibooks-latex`, `abntex2-ctan`, `wilson-2014-best-practices` (artigo real usado nos exemplos de referência).

## 4. Como rodar os testes de compilação

Sem pdflatex local, os testes usam a imagem Docker:

```
docker build -t tutoron-latex-metodologia tests_acervo/latex_metodologia
python -m pytest tests_acervo/test_disciplina_metodologia.py -q
```

Sem pdflatex e sem a imagem, os testes de compilação são pulados (os outros rodam).
