---
id: metodologia-latex-tabela
titulo: Como fazer uma tabela numerada no LaTeX (table, tabular, caption em cima e fonte embaixo)
assunto: metodologia-07-latex-figuras-tabelas-matematica
tipo: exemplo
resolucao: sim
fonte: Lopez e Silva, Introdução ao uso do LaTeX (UFRJ, 2013), seções 2.18 e 2.19 (tabelas); Wilkins, Getting Started with LaTeX (1995), seção 4.4
fontes_catalogo: lopez-silva-2013-latex,wilkins-1995-latex
autoria: Exemplo da equipe TutorON (com apoio de IA) a partir dos guias; compilado nos testes
licenca: CC BY-SA 3.0 (adapta Lopez e Silva, 2013)
publicacao_transcricao: não; exemplo próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exemplo da equipe TutorON a partir de Lopez e Silva (2013) e Wilkins (1995). Compila sem erro com pdflatex (conferido em `tests_acervo/test_disciplina_metodologia.py`).

```latex
\documentclass[12pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[brazilian]{babel}
\begin{document}
A Tabela~\ref{tab:tempo} resume os testes.
\begin{table}[htbp]
  \centering
  \caption{Tempo médio de formatação das referências}
  \label{tab:tempo}
  \begin{tabular}{lrr}
    \hline
    Modo      & Referências & Tempo (min) \\
    \hline
    À mão     & 10 & 25 \\
    Com BibTeX & 10 & 6 \\
    \hline
  \end{tabular}
  \par\small Fonte: dados fictícios do exemplo.
\end{table}
\end{document}
```

- `table` é o ambiente flutuante (numeração, legenda, lista de tabelas com `\listoftables`); `tabular` é a grade.
- `{lrr}`: uma letra por coluna: `l` à esquerda, `c` centralizada, `r` à direita; `|` entre letras desenha linha vertical. `p{4cm}` faz coluna com quebra de linha.
- `&` separa colunas e `\\` termina a linha; o número de `&` por linha é o número de colunas menos um.
- `\hline` desenha linha horizontal. Sem linhas verticais nas bordas, a tabela fica no estilo do IBGE (bloco de ilustrações e tabelas).
- `\caption` antes de `tabular` põe o título em cima, como pede a norma; a fonte vem embaixo.

**Verificação:** conte os `&` de cada linha (dois, para três colunas) e compile duas vezes: o texto deve dizer "Tabela 1", não "Tabela ??".
