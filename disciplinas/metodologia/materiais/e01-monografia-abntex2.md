---
id: metodologia-monografia-abntex2
titulo: Estrutura de monografia e TCC com a classe abntex2 — capa, folha de rosto, resumo, sumário, capítulos, referências e apêndices (NBR 14724)
assunto: metodologia-04-estrutura-artigo-monografia
tipo: exemplo
resolucao: sim
fonte: Lopez e Silva, Introdução ao uso do LaTeX (UFRJ, 2013), seção 2.24 (textos em português e abnTeX2); modelos do abnTeX2 (CTAN)
fontes_catalogo: lopez-silva-2013-latex,abntex2-ctan
autoria: Exemplo da equipe TutorON (com apoio de IA); compilado com pdflatex e bibtex nos testes
licenca: CC BY-SA 3.0 (adapta Lopez e Silva, 2013)
publicacao_transcricao: não; exemplo próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exemplo da equipe TutorON a partir de Lopez e Silva (2013) e dos modelos do abnTeX2. Compila sem erro com pdflatex e bibtex, com o `refs.bib` do bloco do arquivo .bib (conferido em `tests_acervo/test_disciplina_metodologia.py`).

Como montar um TCC ou uma monografia no padrão ABNT usando LaTeX: use a classe `abntex2`. Um trabalho acadêmico (TCC, monografia, relatório) segue a **NBR 14724**: elementos **pré-textuais** (capa, folha de rosto, resumo, *abstract*, listas, sumário), **textuais** (introdução, desenvolvimento, conclusão) e **pós-textuais** (referências, apêndices, anexos). A classe `abntex2` monta a maior parte sozinha.

```latex
\documentclass[12pt,a4paper,oneside,brazilian]{abntex2}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[alf]{abntex2cite}
\titulo{Gerenciamento de referências com BibTeX}
\autor{Nome do Aluno}
\local{Maceió}
\data{2026}
\instituicao{Universidade Federal de Alagoas}
\tipotrabalho{Monografia}
\preambulo{Trabalho da disciplina de Metodologia da Pesquisa.}
\begin{document}
\pretextual
\imprimircapa
\imprimirfolhaderosto

\begin{resumo}
Texto do resumo.\par
\textbf{Palavras-chave}: LaTeX. BibTeX.
\end{resumo}
\tableofcontents*
\textual
\chapter{Introdução}
Texto com citação \cite{lopez2013}.
\chapter{Conclusão}
Texto.
\postextual
\bibliography{refs}
\begin{apendicesenv}
\chapter{Questionário aplicado}
\end{apendicesenv}
\end{document}
```

- `\pretextual`, `\textual` e `\postextual` mudam a paginação e o estilo de cada parte.
- `\imprimircapa` e `\imprimirfolhaderosto` usam os dados de `\titulo`, `\autor`, `\local`… Deixe uma **linha em branco** depois de `\imprimirfolhaderosto`, como no modelo oficial: na versão testada, sem ela, o comando engole o `\begin{resumo}` seguinte e a compilação para com "Argument of \begin has an extra }".
- `apendicesenv` nomeia os capítulos como "APÊNDICE A – …"; `anexosenv` faz o mesmo com ANEXO.

**Verificação:** compile (pdflatex, bibtex, pdflatex, pdflatex) e confira que o sumário lista os capítulos e o APÊNDICE A, e que a capa mostra a instituição, o título e o local.
