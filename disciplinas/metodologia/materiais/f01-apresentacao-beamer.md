---
id: metodologia-apresentacao-beamer
titulo: Como fazer slides de apresentação de trabalho no LaTeX com Beamer — frame, título, itens revelados aos poucos e roteiro da apresentação
assunto: metodologia-09-apresentacao-trabalhos
tipo: exemplo
resolucao: sim
fonte: Lopez e Silva, Introdução ao uso do LaTeX (UFRJ, 2013), seção 3.2 (elaboração de apresentações)
fontes_catalogo: lopez-silva-2013-latex
autoria: Exemplo da equipe TutorON (com apoio de IA) a partir do guia de Lopez e Silva; compilado nos testes
licenca: CC BY-SA 3.0 (adapta Lopez e Silva, 2013)
publicacao_transcricao: não; exemplo próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exemplo da equipe TutorON a partir de Lopez e Silva (2013). Compila sem erro com pdflatex (conferido em `tests_acervo/test_disciplina_metodologia.py`).

```latex
\documentclass{beamer}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[brazilian]{babel}
\usetheme{Madrid}
\title{Gerenciamento de referências}
\author{Nome do Aluno}
\date{2026}
\begin{document}
\begin{frame}
  \titlepage
\end{frame}
\begin{frame}{Roteiro}
  \tableofcontents
\end{frame}
\section{Problema}
\begin{frame}{Problema}
  \begin{itemize}
    \item<1-> Formatar referências à mão gera erros.
    \item<2-> O BibTeX automatiza o formato.
  \end{itemize}
\end{frame}
\end{document}
```

- Cada `frame` é um slide; o texto entre chaves depois de `\begin{frame}` é o título dele.
- `\item<2->` aparece só a partir da 2ª etapa do slide: o PDF ganha uma página por etapa.
- `\section` alimenta o roteiro (`\tableofcontents`) e a barra de navegação do tema.
- `\usetheme` troca o visual (Madrid, Warsaw, CambridgeUS…).

**Roteiro de apresentação (equipe TutorON):** um slide de título; o problema e o objetivo; o método; os resultados principais (uma figura ou tabela por slide); a conclusão; as referências. Regra prática: cerca de um slide por minuto de fala, e poucas palavras por slide, para o público ouvir em vez de ler.

**Verificação:** o PDF deve ter 4 páginas: título, roteiro e duas etapas do slide "Problema".
