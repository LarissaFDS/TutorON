---
id: metodologia-latex-documento-minimo
titulo: Primeiro documento em LaTeX — preâmbulo, documentclass, pacotes para português (babel, inputenc), seções, negrito, itálico e caracteres especiais
assunto: metodologia-06-latex-basico
tipo: exemplo
resolucao: sim
fonte: Lopez e Silva, Introdução ao uso do LaTeX (UFRJ, 2013), cap. 1 e 2; Wilkins, Getting Started with LaTeX (1995), seções 1 e 2
fontes_catalogo: lopez-silva-2013-latex,wilkins-1995-latex
autoria: Exemplo da equipe TutorON (com apoio de IA) a partir dos guias de Lopez e Silva e de Wilkins; compilado nos testes
licenca: CC BY-SA 3.0 (adapta Lopez e Silva, 2013)
publicacao_transcricao: não; exemplo próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exemplo da equipe TutorON a partir dos guias de Lopez e Silva (2013) e Wilkins (1995). Compila sem erro com pdflatex (conferido em `tests_acervo/test_disciplina_metodologia.py`).

Um arquivo .tex tem duas partes: o **preâmbulo** (tudo antes de \begin{document}: classe e pacotes) e o **corpo** (o texto).

```latex
\documentclass[12pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[brazilian]{babel}
\title{Uso do \LaTeX{} na escrita científica}
\author{Nome do Aluno}
\date{\today}
\begin{document}
\maketitle
\begin{abstract}
Este texto mostra a estrutura mínima de um documento.
\end{abstract}
\section{Introdução}\label{sec:intro}
Texto com \textbf{negrito}, \textit{itálico} e ``aspas''.
\subsection{Objetivo}
Veja a Seção~\ref{sec:intro}.
\section*{Seção sem número}
Os caracteres \# \$ \% \& \_ \{ \} precisam de barra.
\end{document}
```

**O que cada linha faz.**
- `\documentclass[12pt,a4paper]{article}`: classe do documento (article, report, book; para trabalhos ABNT, abntex2).
- `fontenc` e `inputenc`: acentos digitados direto, em UTF-8.
- `babel` com `brazilian`: hifenização em português e títulos automáticos ("Resumo", "Sumário", "Figura"). O guia usa a opção `brazil`; o babel atual (TeX Live 2026) avisa que esse nome está obsoleto, então use `brazilian`.
- `\section`, `\subsection`: seções numeradas; com asterisco, sem número.
- `\label` e `\ref`: referência cruzada; o número aparece só na segunda compilação.
- Aspas: dois acentos graves para abrir e dois apóstrofos para fechar.
- Caracteres reservados: `# $ % & _ { } ~ ^ \` têm função especial; para imprimir, use a barra antes (`\%`, `\_`); a própria barra é `\textbackslash`.

**Verificação:** compile duas vezes com `pdflatex arquivo.tex`. No PDF, o resumo tem o título "Resumo" e a referência mostra "Seção 1", não "Seção ??".
