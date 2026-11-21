---
id: logica-unificacao-mgu
titulo: Unificação: substituição, unificador mais geral (u.m.g.), conjunto de discórdia e teste de ocorrência
assunto: logica-12-forma-clausal-unificacao-resolucao
tipo: material_estudo
resolucao: sim
fonte: Slides de Resolução (Baldoino Fonseca, UFAL), unificação
fontes_catalogo: ufal-baldoino-slides-primeira-ordem
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: corrigida (resolução da equipe TutorON, não é gabarito do professor; conferida com Python; o original tem erro apontado abaixo).

**Substituição** $\{x_1/t_1,\dots,x_n/t_n\}$: troca, ao mesmo tempo, cada variável $x_i$ pelo termo $t_i$. Um **unificador** de um conjunto de expressões as torna idênticas; o **unificador mais geral** (u.m.g.) é aquele do qual todo outro se obtém compondo mais uma substituição.

**Algoritmo:** compare as expressões símbolo a símbolo; no primeiro ponto em que diferem, o **conjunto de discórdia** traz os subtermos que começam ali. Se ele tem uma variável $x$ e um termo $t$ em que $x$ **não ocorre** (teste de ocorrência), aplique $x/t$ e continue; se não (duas constantes ou funções diferentes, ou $x$ dentro de $t$), pare: não unifica.

**Exemplos dos slides:**
- $\{p(a,f(x)),\;p(y,z)\}$: u.m.g. $\{y/a,\;z/f(x)\}$. $\{y/a,\;x/b,\;z/f(b)\}$ também unifica, mas é menos geral.
- $\{p(a,x),\;p(b,y)\}$: não unifica ($a\ne b$, duas constantes).
- $\{p(a,x,f(g(y))),\;p(z,h(z,w),f(w)),\;p(a,h(a,g(b)),f(g(v)))\}$: passos $z/a$, $x/h(a,w)$, $w/g(b)$, $y/b$, $v/b$; u.m.g. $\{z/a,\;x/h(a,g(b)),\;w/g(b),\;y/b,\;v/b\}$, e as três ficam $p(a,h(a,g(b)),f(g(b)))$.
- $\{q(f(a),g(x)),\;q(y,y)\}$: após $y/f(a)$, a discórdia $\{g(x),f(a)\}$ não tem variável: não unifica.

**Correção:** nos passos 3 e 5 do terceiro exemplo, o slide escreve "$x/h(a,g(b)$" sem fechar o parêntese; o certo é $x/h(a,g(b))$.

**Renomear antes de resolver:** $p(x)$ e $\neg p(f(x))$ parecem não unificar ($x$ ocorre em $f(x)$), mas são cláusulas diferentes: renomeando a segunda para $\neg p(f(y))$, o u.m.g. $\{x/f(y)\}$ dá $\square$.

**Verificação:** todos os u.m.g. e as falhas foram recalculados pelo algoritmo de Robinson com teste de ocorrência implementado nos testes.
