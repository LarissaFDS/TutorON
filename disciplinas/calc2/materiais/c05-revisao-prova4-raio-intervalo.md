---
id: calc2-revisao-prova4-raio-intervalo
titulo: Revisão da prova 4 (Profa. Xu Yang) — raio e intervalo de convergência de séries de potências, com o teste das extremidades
assunto: calc2-04-series-de-potencias-taylor
tipo: exercicio_resolvido
resolucao: sim
fonte: Revisão de Prova 4 de Cálculo 2 (Profa. Xu Yang, UFAL), imagem do material do 2º período de Engenharia de Computação | enunciados parafraseados
curso: Engenharia de Computação (UFAL), ECOM010 Cálculo 2, 2º período; semestre não identificado
fontes_catalogo: ufal-xu-yang-calc2-listas
autoria: Enunciados da revisão da Profa. Xu Yang; resoluções da equipe TutorON com apoio de IA, conferidas com SymPy
licenca: Não declarada (revisão da disciplina; imagem não versionada)
publicacao_transcricao: não autorizada; enunciados parafraseados
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Cálculo 2, revisão da prova 4 (raio e intervalo de convergência). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Método:** aplique o teste da razão em $|a_n(x-a)^n|$ e ache o raio $R$ (converge para $|x - a| < R$). O teste da razão **não decide nas extremidades**: teste $x = a \pm R$ separadamente, com outro teste.

- $\sum n^n x^n$: a raiz dá $n|x| \to \infty$ para todo $x \ne 0$: $R = 0$, só converge em $x = 0$.
- $\sum\tfrac{(-1)^n x^n}{n+1}$: $R = 1$. Em $x = 1$, série alternada harmônica (converge); em $x = -1$, vira $\sum\tfrac{1}{n+1}$ (diverge). Intervalo $(-1, 1]$.
- $\sum\tfrac{x^n}{n\,3^n}$: $R = 3$. Em $x = 3$, harmônica (diverge); em $x = -3$, alternada (converge). Intervalo $[-3, 3)$.
- $\sum\tfrac{(x-2)^n}{n^2+1}$: centro 2, $R = 1$. Nas duas extremidades $|a_n| = \tfrac{1}{n^2+1}$, que converge. Intervalo $[1, 3]$.
- $\sum\tfrac{x^n}{1\cdot3\cdot5\cdots(2n-1)}$: a razão dá $\tfrac{|x|}{2n+1} \to 0$: $R = \infty$, converge para todo $x$.

Erros comuns: esquecer o centro (em $(x-2)^n$ o intervalo é em torno de 2); dar só o raio quando a questão pede o intervalo.

**Verificação:** os limites da razão e as séries das extremidades foram conferidos com SymPy em `test_revisao_raio_intervalo`.
