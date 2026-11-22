---
id: metodologia-latex-listas-citacao-longa
titulo: Listas (itemize, enumerate, description) e citação longa recuada no LaTeX (ambiente quote)
assunto: metodologia-06-latex-basico
tipo: exemplo
resolucao: sim
fonte: Wilkins, Getting Started with LaTeX (1995), seções 4.2 (listas) e 4.3 (citações em destaque); Lopez e Silva (2013), seção 2.17
fontes_catalogo: wilkins-1995-latex,lopez-silva-2013-latex
autoria: Exemplo da equipe TutorON (com apoio de IA) a partir dos guias de Wilkins e de Lopez e Silva; compilado nos testes
licenca: CC BY-SA 3.0 (adapta Lopez e Silva, 2013)
publicacao_transcricao: não; exemplo próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exemplo da equipe TutorON a partir de Wilkins (1995) e Lopez e Silva (2013). Compila sem erro com pdflatex (conferido em `tests_acervo/test_disciplina_metodologia.py`).

```latex
\documentclass[12pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[brazilian]{babel}
\begin{document}
Elementos de um artigo:
\begin{itemize}
  \item pré-textuais;
  \item textuais;
  \item pós-textuais.
\end{itemize}
Etapas da compilação:
\begin{enumerate}
  \item rodar o pdflatex;
  \item rodar o bibtex;
  \item rodar o pdflatex mais duas vezes.
\end{enumerate}
\begin{description}
  \item[Apêndice] texto do próprio autor.
  \item[Anexo] texto de outro autor.
\end{description}
Citação longa, recuada e em fonte menor:
\begin{quote}\small
Texto citado com mais de três linhas, sem aspas, em
espaço simples, seguido do autor, do ano e da página
(Lopez; Silva, 2013, p. 66).
\end{quote}
\end{document}
```

- `itemize` usa marcadores; `enumerate` numera sozinho; `description` usa o termo entre colchetes. As listas podem ser aninhadas (até quatro níveis).
- `quote` recua as duas margens; `\small` reduz a fonte, como pede a ABNT para citação longa. A classe abntex2 tem o ambiente `citacao`, que já aplica o recuo de 4 cm.

**Verificação:** compile e confira no PDF: três marcadores, itens numerados 1, 2 e 3, os termos Apêndice e Anexo em negrito, e o parágrafo citado recuado.
