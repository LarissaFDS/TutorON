---
id: metodologia-latex-compilacao-erros
titulo: Como compilar LaTeX com BibTeX (pdflatex, bibtex, pdflatex duas vezes) e como ler as mensagens de erro mais comuns
assunto: metodologia-06-latex-basico
tipo: material_estudo
resolucao: sim
fonte: Lopez e Silva, Introdução ao uso do LaTeX (UFRJ, 2013), seções 1.6, 1.15, 2.22.2 e cap. 4 (mensagens de erro)
fontes_catalogo: lopez-silva-2013-latex
autoria: Paráfrase da equipe TutorON (com apoio de IA) do guia de Lopez e Silva; cada erro foi reproduzido nos testes
licenca: CC BY-SA 3.0 (adapta Lopez e Silva, 2013)
publicacao_transcricao: não; só paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Paráfrase da equipe TutorON do guia de Lopez e Silva (2013). Cada mensagem abaixo foi reproduzida com pdflatex em `tests_acervo/test_disciplina_metodologia.py`.

**Ciclo de compilação com referências** (arquivo `artigo.tex` e `refs.bib`):
```bash
pdflatex artigo
bibtex artigo
pdflatex artigo
pdflatex artigo
```
A 1ª passada anota as citações no `.aux`; o `bibtex` lê o `.aux` e o `.bib` e escreve o `.bbl`; a 2ª passada põe a lista no texto; a 3ª acerta os números de citações e referências cruzadas. Sem citações, basta rodar pdflatex duas vezes. Editores como TeXworks e Texmaker fazem isso por botões.

**Arquivos auxiliares:** `.aux` (rótulos e citações), `.log` (o relatório completo da compilação), `.toc` (sumário), `.bbl` e `.blg` (saída e relatório do BibTeX). Pode apagá-los: eles são recriados.

**Como ler um erro.** A mensagem é em inglês e vem com o número da linha, como `l.12`. O erro pode estar numa linha **anterior**. Corrija o **primeiro** erro e compile de novo: um erro costuma provocar outros.

| Mensagem | Causa provável |
|---|---|
| Undefined control sequence | comando digitado errado ou de pacote não carregado |
| `Missing $ inserted` | `_` ou `^` (ou símbolo matemático) fora do modo matemático, ou `$` não fechado |
| \begin{itemize} … ended by \end{document} | ambiente aberto e não fechado |
| Runaway argument? / Paragraph ended before … was complete | chave `{` sem a `}` |
| Extra alignment tab has been changed to \cr | mais `&` que colunas numa tabela, ou faltou `\\` |
| Reference … undefined / Citation … undefined | falta compilar de novo (ou rodar o bibtex), ou o rótulo está escrito diferente |
| Overfull \hbox | linha passa da margem; é aviso, não erro |

**Verificação:** abra o `.log`, procure a primeira linha que começa com `!` e a linha `l.` logo abaixo dela; é ali que está o erro.
