---
id: metodologia-bibtex-abntex2cite
titulo: Citações e referências no padrão ABNT com BibTeX — pacote abntex2cite, comandos cite e citeonline, estilo autor-data alf
assunto: metodologia-08-referencias-bibtex-jabref
tipo: exemplo
resolucao: sim
fonte: Lopez e Silva, Introdução ao uso do LaTeX (UFRJ, 2013), seções 2.22.2 e 2.24 (abnTeX2); documentação do abntex2cite (CTAN)
fontes_catalogo: lopez-silva-2013-latex,abntex2-ctan
autoria: Exemplo da equipe TutorON (com apoio de IA); compilado com pdflatex e bibtex nos testes, saída conferida
licenca: CC BY-SA 3.0 (adapta Lopez e Silva, 2013)
publicacao_transcricao: não; exemplo próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Exemplo da equipe TutorON a partir de Lopez e Silva (2013) e da documentação do abnTeX2. Compila sem erro com pdflatex e bibtex, usando o mesmo `refs.bib` do bloco do arquivo .bib (conferido em `tests_acervo/test_disciplina_metodologia.py`).

```latex
\documentclass[12pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[brazilian]{babel}
\usepackage[alf]{abntex2cite}
\begin{document}
Segundo \citeonline{lopez2013}, o BibTeX gera a lista.
O BibTeX lê um arquivo .bib \cite[p.~68]{lopez2013}.
Boas práticas de software \cite{wilson2014}.
\bibliography{refs}
\end{document}
```

Saída conferida no PDF (TeX Live 2026, abntex2cite):
- `\citeonline{lopez2013}` → *Lopez e Silva (2013)*: autor fora dos parênteses, como parte da frase;
- `\cite[p.~68]{lopez2013}` → *(LOPEZ; SILVA, 2013, p. 68)*: autor dentro dos parênteses, com página;
- a lista sai com o título "Referências", em ordem alfabética e no formato da NBR 6023.

Pontos de atenção:
- `[alf]` escolhe o sistema autor-data; `[num]` escolhe o numérico. Não é preciso `\bibliographystyle`: o pacote já usa o estilo `abntex2-alf`.
- O ciclo é o mesmo: pdflatex, bibtex, pdflatex, pdflatex.
- Em trabalhos completos, use a classe `abntex2` (bloco da monografia), que já carrega as regras de formatação.

**Maiúsculas dentro dos parênteses.** O abntex2cite segue a NBR 10520 de 2002 e imprime o sobrenome em MAIÚSCULAS dentro dos parênteses. Pela edição de 2023, segundo os guias de bibliotecas (bloco de citações), a forma seria *(Lopez; Silva, 2013, p. 68)*. Status da resolução: pendente de confirmação do professor sobre qual forma a turma deve entregar.

**Verificação:** compile e procure no PDF as duas formas da citação; se aparecer "(??)" ou a chave em negrito, faltou rodar o bibtex ou a chave está escrita diferente no .bib.
