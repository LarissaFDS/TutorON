---
id: metodologia-bibtex-arquivo-bib
titulo: Como fazer referências bibliográficas no LaTeX com BibTeX — arquivo .bib, tipos de entrada (@book, @article, @misc), chave de citação e acentos
assunto: metodologia-08-referencias-bibtex-jabref
tipo: exemplo
resolucao: sim
fonte: Lopez e Silva, Introdução ao uso do LaTeX (UFRJ, 2013), seção 2.22 (referências bibliográficas e uso do BibTeX)
fontes_catalogo: lopez-silva-2013-latex,wikibooks-latex
autoria: Exemplo e correção da equipe TutorON (com apoio de IA) a partir do guia de Lopez e Silva; compilado com pdflatex e bibtex nos testes
licenca: CC BY-SA 3.0 (adapta Lopez e Silva, 2013)
publicacao_transcricao: não; exemplo próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Exemplo da equipe TutorON a partir de Lopez e Silva (2013). O par abaixo compila sem erro nem aviso com pdflatex e bibtex (conferido em `tests_acervo/test_disciplina_metodologia.py`).

Arquivo `refs.bib`:
```bibtex
@book{lopez2013,
  author    = {Lopez, Ivo Fernandez and Silva, Maria Darci Godinho da},
  title     = {Introdu{\c c}{\~a}o ao uso do {\LaTeX}},
  publisher = {Edi{\c c}{\~a}o do autor},
  address   = {Rio de Janeiro},
  year      = {2013}
}
@article{wilson2014,
  author  = {Wilson, Greg and others},
  title   = {Best practices for scientific computing},
  journal = {PLOS Biology},
  volume  = {12},
  number  = {1},
  pages   = {e1001745},
  year    = {2014}
}
@misc{wilkins1995,
  author       = {Wilkins, David R.},
  title        = {Getting started with {\LaTeX}},
  howpublished = {\url{https://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/}},
  year         = {1995}
}
```

Arquivo `artigo.tex`:
```latex
\documentclass{article}
\usepackage{url}
\begin{document}
Ver \cite{lopez2013}, \cite{wilson2014} e \cite{wilkins1995}.
\bibliographystyle{plain}
\bibliography{refs}
\end{document}
```

- Cada entrada tem **tipo** (`@book`, `@article`, `@misc`…), **chave** (`lopez2013`, usada no `\cite`) e campos. Autores são separados por `and`; `others` vira "et al.".
- Só entra na lista o que for citado (ou `\nocite{*}` para todos).
- Acentos no .bib no formato do TeX: `{\'a}`, `{\~a}`, `{\c c}`, `{\'\i}`, porque o BibTeX clássico ordena e põe em maiúsculas mal os caracteres UTF-8. Chaves extras protegem maiúsculas: `{\LaTeX}`.
- Compile: pdflatex, bibtex, pdflatex, pdflatex (bloco de compilação).

**Correção do guia.** O guia usa `@Online` para páginas da internet. Esse tipo é do **biblatex**; o BibTeX com os estilos padrão não o conhece e avisa "entry type for … isn't style-file defined". Com BibTeX, use `@misc` com `howpublished` (ou `url`, no estilo do abntex2cite). Status da resolução: corrigida.

**Verificação:** o `.blg` do bibtex deve terminar sem "Warning", e o PDF deve listar as três referências.
