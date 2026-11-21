---
id: metodologia-latex-matematica
titulo: Fórmulas matemáticas no LaTeX — modo matemático em linha e em destaque, equation numerada, align, frações, raízes, somatórios e integrais
assunto: metodologia-07-latex-figuras-tabelas-matematica
tipo: exemplo
resolucao: sim
fonte: Wilkins, Getting Started with LaTeX (1995), cap. 3 (fórmulas matemáticas); Lopez e Silva (2013), seções 2.12 a 2.15
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
\usepackage{amsmath}
\begin{document}
Em linha: a área do círculo é $A = \pi r^2$.
\begin{equation}\label{eq:media}
  \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
\end{equation}
A média~\eqref{eq:media} vale para qualquer $n \geq 1$.
\begin{align}
  (a+b)^2 &= a^2 + 2ab + b^2 \\
  \binom{n}{k} &= \frac{n!}{k!\,(n-k)!}
\end{align}
Sem número: \[ \sqrt{x^2 + y^2} \leq |x| + |y| \]
\end{document}
```

Como fica, em palavras e no site:
- em linha, a área do círculo, $A = \pi r^2$ ("A igual a pi r ao quadrado");
- a média, $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$ ("x barra é a soma dos x i, de i igual a 1 até n, dividida por n");
- $\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$ ("n escolhe k é n fatorial sobre k fatorial vezes n menos k fatorial").

O bloco ensina a **escrever** fórmulas; resolver a conta é assunto da disciplina de origem.

Regras:
- `$…$` para fórmula no meio da frase; `\[…\]` para fórmula em destaque sem número; `equation` para fórmula numerada.
- `^` é expoente e `_` é índice; com mais de um caractere, use chaves: `x^{10}`, `x_{ij}`.
- `\frac{a}{b}`, `\sqrt{x}`, `\sum`, `\int`, letras gregas (`\alpha`, `\pi`) e funções (`\sin`, `\log`) só no modo matemático.
- `align` (pacote `amsmath`) alinha várias linhas pelo `&`; cada linha ganha número.
- `\eqref` imprime o número entre parênteses: "(1)".

**Verificação:** compile duas vezes: o texto deve dizer "A média (1)", e as duas linhas do align devem sair numeradas (2) e (3).
