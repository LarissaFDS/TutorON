---
id: metodologia-latex-figura-legenda
titulo: Como inserir uma figura com legenda (caption), rótulo (label) e referência cruzada no LaTeX, com legenda em cima no padrão ABNT
assunto: metodologia-07-latex-figuras-tabelas-matematica
tipo: exemplo
resolucao: sim
fonte: Lopez e Silva, Introdução ao uso do LaTeX (UFRJ, 2013), seções 2.20 e 2.21 (figuras numeradas)
fontes_catalogo: lopez-silva-2013-latex,wikibooks-latex
autoria: Exemplo e correção da equipe TutorON (com apoio de IA) a partir do guia de Lopez e Silva; compilado nos testes
licenca: CC BY-SA 3.0 (adapta Lopez e Silva, 2013)
publicacao_transcricao: não; exemplo próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Exemplo da equipe TutorON a partir de Lopez e Silva (2013). Compila sem erro com pdflatex, com uma imagem `grafico.png` na mesma pasta do .tex (conferido em `tests_acervo/test_disciplina_metodologia.py`).

```latex
\documentclass[12pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[brazilian]{babel}
\usepackage{graphicx}
\begin{document}
\section{Resultados}
A Figura~\ref{fig:grafico} mostra o tempo de compilação.
\begin{figure}[htbp]
  \centering
  \caption{Tempo de compilação por número de páginas}
  \label{fig:grafico}
  \includegraphics[width=0.6\textwidth]{grafico}
  \par\small Fonte: elaborado pelo autor (2026).
\end{figure}
\end{document}
```

- `figure` é um ambiente **flutuante**: o LaTeX escolhe onde pôr a figura. `[htbp]` aceita aqui (h), no topo (t), no pé (b) ou numa página só de figuras (p). Com o pacote `float`, `[H]` força a posição exata.
- `\includegraphics` (pacote `graphicx`) aceita .png, .jpg e .pdf com pdflatex; a extensão pode ser omitida. `width=0.6\textwidth` é 60% da largura do texto.
- `\caption` gera "Figura 1: …" e a entrada da lista de figuras (`\listoffigures`). Antes da imagem, a legenda fica em cima, como pede a ABNT; a fonte vem embaixo.
- `\ref{fig:grafico}` imprime o número; compile duas vezes.

**Correção do guia.** No exemplo do guia, o `\label` vem **antes** do `\caption`. O número da figura só existe depois do `\caption`, então um `\label` posto antes guarda o número da **seção** e o `\ref` imprime o número da seção, não o da figura. O guia também usa o ambiente `center`, que acrescenta espaço vertical; dentro de `figure`, prefira `\centering`. Status da resolução: corrigida (o teste mostra o `\ref` errado com a ordem do guia).

**Verificação:** depois de duas compilações, o `.aux` deve ter `\newlabel{fig:grafico}{{1}…}` e o PDF deve mostrar "Figura 1" em cima da imagem.
