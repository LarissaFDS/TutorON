# Curadoria — Probabilidade e Estatística (`prob`)

Atualizado em 18/11/2026. Acervo: 25 blocos em `materiais/`, 19 na busca (as anotações do aluno, parafraseadas e conferidas) e 6 notas da equipe escritas com auxílio de IA, como `candidato`, **fora da busca** até a revisão humana.

## 1. Ementa (PPC) e escopo

O PPC de Engenharia de Computação da UFAL (2014, `ufal-ppc-ecomp-2014`, p. 35) define **ECOM020 Probabilidade e Estatística**, 60 h (40 teóricas e 20 práticas). A ementa cobre análise exploratória, probabilidade, distribuições discretas e contínuas de variáveis aleatórias, valor esperado e variância, inferência estatística (estimação de parâmetros e testes de hipóteses), tópicos especiais e uso de ferramentas computacionais. A bibliografia básica é Magalhães e Lima (*Noções de Probabilidade e Estatística*), Bussab e Morettin (*Estatística Básica*) e Magalhães (*Probabilidade e Variáveis Aleatórias*). A complementar inclui Verzani (*Using R for Introductory Statistics*) e Dalgaard (*Introductory Statistics with R*).

O uso de R nas anotações (`dbinom`, `pnorm`, `pexp`…) bate com o item "ferramentas computacionais" e com a bibliografia de R. Os cabeçalhos das anotações dizem só "Probabilidade e Estatística"; **a instituição e o professor não aparecem**. A ligação com ECOM020/UFAL é uma suposição, porque as outras disciplinas são de lá.

## 2. Inventário das anotações (`ufal-prob-anotacoes-2025-2`)

Autor: Otávio Joshua Costa Brandão Menezes, aluno e membro da equipe. São anotações de estudo, **não material do professor nem gabarito**. Os PDFs ficam fora do repositório, e nenhuma imagem foi versionada. Há capturas de slides e de um resumo em R coladas nas páginas, e o conteúdo delas foi descrito em texto. **A autorização para publicar a transcrição não foi confirmada**: os blocos parafraseiam e estão marcados `publicacao_transcricao: não autorizada até agora`.

| Arquivo (data AAMMDD) | Págs. | Conteúdo | Blocos |
|---|---|---|---|
| `Probabilidade _250907_210206.pdf` (07/09/2025) | 6 manuscritas | probabilidade clássica, adição, condicional, produto, independência, contagem, Bayes (máquinas e teste diagnóstico), dominó e baralho | `prob-anot-conceitos-probabilidade`, `prob-anot-contagem`, `prob-anot-bayes-maquinas`, `prob-anot-bayes-teste-diagnostico` |
| `Variáveis Aleatórias_251008_230428.pdf` (08/10/2025) | 7 manuscritas | VA discreta e contínua, fp, fdp, FDA, esperança, variância, lista das distribuições; tabela da comissão colada | `prob-anot-va-discreta`, `prob-anot-va-continua`, `prob-anot-esperanca-variancia` |
| `Principais Distribuições Discretas_251011_130200.pdf` (11/10/2025) | 4 manuscritas | uniforme discreta, Bernoulli, binomial (R), geométrica, hipergeométrica (só citada), Poisson | `prob-anot-uniforme-discreta-bernoulli`, `prob-anot-binomial`, `prob-anot-geometrica`, `prob-anot-poisson` |
| `Distribuições Normais e Uniformes_251011_135256.pdf` (11/10/2025) | 3 manuscritas | normal, cinco tipos de problema em R (captura colada), uniforme contínua | `prob-anot-normal-padronizacao`, `prob-anot-uniforme-continua` |
| `Distribuição Exponencial e Combinação Linear _251011_140915.pdf` (11/10/2025) | 6 digitadas | exponencial, falta de memória, Poisson x exponencial, combinação linear de normais, elevador ("questão 4 da prova"), "questão 3", aproximação normal | `prob-anot-exponencial`, `prob-anot-exponencial-exemplos`, `prob-anot-poisson-exponencial`, `prob-anot-combinacao-linear-normais`, `prob-anot-elevador`, `prob-anot-aproximacao-normal` |

O último arquivo é um resumo digitado com título riscado ("Distribuição normal e uniforme") e cita questões de uma prova. O enunciado da prova não está no material.

### Erros encontrados e status de cada resolução

| Bloco | Status | O que estava nas anotações | Correção |
|---|---|---|---|
| `prob-anot-conceitos-probabilidade` | corrigida | $P(A\cap B)=P(A)P(B)$ e $P(A\cup B)=P(A)+P(B)$ lado a lado, sem condição | a primeira só para independentes, a segunda só para disjuntos; disjuntos com probabilidade positiva nunca são independentes |
| `prob-anot-contagem` | corrigida | arranjo escrito com o símbolo $\binom{n}{p}$ | $A_{n,p} = n!/(n-p)!$ |
| `prob-anot-va-continua` | corrigida | $f(x)=x/4$ sem intervalo; FDA "sempre crescente" | intervalo $[1,3]$; FDA não decrescente |
| `prob-anot-esperanca-variancia` | corrigida | $\sigma^2(X-Y) = \sigma^2(X) - \sigma^2(Y)$ | as variâncias somam |
| `prob-anot-binomial` | corrigida | $P(X\le 3)$ = `dbinom(1)+…+dbinom(4)` | de 0 a 3 |
| `prob-anot-combinacao-linear-normais` | corrigida | $\operatorname{Var}(nX) = n\sigma^2$; $N(75, 16{,}81^2)$ somado como variância | $n^2\sigma^2$ para $nX$ ($n\sigma^2$ é a soma de n cópias); 16,81 e 106,09 são variâncias |
| `prob-anot-elevador` | pendente_professor | 4 pessoas no título e 8 no código; capacidade "605 + round(xx/10)" | montagem correta registrada; valores dependem do enunciado da prova |
| `prob-anot-bayes-maquinas`, `prob-anot-bayes-teste-diagnostico` | validada | item b "análogo"; valor final de $P(D\mid +)$ não calculado | completados: 10/29 ≈ 0,3448 e ≈ 0,1610 |
| demais blocos | validada | — | valores conferidos |

Todas as contas foram conferidas em `tests_acervo/test_disciplina_prob.py`: exatas com `fractions`/SymPy, distribuições com `scipy.stats` e probabilidades com simulações de Monte Carlo de semente fixa. Os erros acima também são testados como erros: por exemplo, a simulação mostra que $\operatorname{Var}(X-Y)$ é a soma, e o teste confere que nenhum bloco afirma a forma errada. A tabela da normal citada é a de área acumulada (Φ). O bloco da normal explica também a tabela de área entre 0 e z.

## 3. Mapeamento dos tópicos

| Assunto | Evidência nas anotações | Situação no acervo |
|---|---|---|
| `prob-01-probabilidade-basica` | sim | na busca |
| `prob-02-bayes` | sim | na busca |
| `prob-03-variaveis-aleatorias` | sim | na busca |
| `prob-04-esperanca-variancia` | sim | na busca |
| `prob-05-distribuicoes-discretas` | sim (uniforme, Bernoulli, binomial, geométrica, Poisson; hipergeométrica só citada) | na busca; `prob-nota-hipergeometrica` candidata |
| `prob-06-uniforme-normal` | sim | na busca |
| `prob-07-exponencial` | sim | na busca |
| `prob-08-combinacao-linear` | sim | na busca (o elevador fica pendente) |
| `prob-09-aproximacao-normal-tcl` | parcial (aproximação normal; o TCL não é enunciado) | aproximação na busca; `prob-nota-tcl` candidata |
| `prob-10-estatistica-descritiva` | não (fundamental na ementa: "análise exploratória") | só `prob-nota-estatistica-descritiva`, candidata |
| `prob-11-estimacao` | não (fundamental: "estimação de parâmetros") | só `prob-nota-intervalo-confianca`, candidata |
| `prob-12-testes-hipoteses` | não (fundamental: "teste de hipóteses") | só `prob-nota-teste-hipoteses`, candidata |
| `prob-13-conjuntas-regressao` | não (complementar; covariância aparece no rigor) | só `prob-nota-covariancia-regressao`, candidata |

Fronteiras: densidades conjuntas com integrais duplas pertencem a Cálculo 3, e a distribuição de Maxwell, a Física 2. O `rigor.md` manda dizer isso, e os índices separados garantem o isolamento (testado nos dois sentidos).

## 4. Fontes (`fontes.json`)

Novas (complemento de CC): `ufal-cc-prob-provas-heitor-2013` (acervo) e `ufal-ppc-cc-2011` (citada).

Matriz de critérios igual à das disciplinas anteriores (notas de 1 a 5 em autoridade, cobertura, profundidade, didática, aderência, acessibilidade, reutilização e tutoria).

| id | Prioridade | Uso | Licença conferida |
|---|---|---|---|
| `ufal-prob-anotacoes-2025-2` | alta | acervo | não declarada; publicação não autorizada |
| `openstax-introductory-statistics-2e` | alta | citada | **CC BY-NC-SA 4.0** (API da OpenStax; não é CC BY) |
| `openintro-statistics` | alta | citada | CC BY-SA 3.0 (openintro.org/license) |
| `grinstead-snell` | média | citada | GNU FDL (página de rosto do PDF) |
| `mit-ocw-18-05` | média | citada | CC BY-NC-SA 4.0 (página do curso) |
| `ufal-ppc-ecomp-2014` | referência | referência | documento institucional |
| `verzani-simpler` | referência | referência | "All rights reserved" (só acesso livre) |
| `bussab-morettin` | referência | referência | obra protegida, não acessada |
| `magalhaes-lima-nocoes` | referência | referência | obra protegida, não acessada |
| `scipy-stats` | referência | referência | BSD-3 (ferramenta dos testes) |

Nenhum texto das fontes abertas foi copiado. As notas da equipe citam as seções como leitura. Não foi encontrada apostila em português com licença aberta verificável. Os livros da bibliografia do PPC entram só como referência externa.

## 5. Notas da equipe (fora da busca)

`prob-nota-hipergeometrica`, `prob-nota-estatistica-descritiva`, `prob-nota-tcl`, `prob-nota-intervalo-confianca`, `prob-nota-teste-hipoteses`, `prob-nota-covariancia-regressao`. Foram escritas com auxílio de IA e conferidas por código (inclusive uma correção: o valor exato do exemplo do TCL é 0,1184, não 0,1086 como no primeiro rascunho). Ficam `curadoria: candidato`, `revisao_humana: pendente`. Para entrarem na busca, uma pessoa da equipe precisa revisá-las e mudar a curadoria para `aprovado`.

## 6. Respostas da IA real (18/11/2026)

`python eval/bateria_tutor.py --so prob-…`, resultado em `eval/results/bateria-prob-2026-11-18.json`. Os modelos principais do Gemini responderam HTTP 503 e as 6 respostas vieram do modelo de reserva configurado, `gemini-3.1-flash-lite`. Conferidas contra o gabarito de cada entrada:

| Pergunta | Resultado |
|---|---|
| `prob-indep` | correta: $P(A\cap B)=0$ × produto; disjuntos com probabilidade positiva não são independentes |
| `prob-poisson` | método correto (complemento, fp da Poisson com λ = 3); socrática, sem o número final (gabarito ≈ 0,5768) |
| `prob-memoria` | correta: $P(X>s+t\mid X>s)=P(X>t)$ |
| `prob-2x-y` | correta: normal, coeficientes ao quadrado, variâncias somam. Na primeira rodada caiu na recusa de `copia_instrucoes` porque repetiu a fórmula escrita em LaTeX no `rigor.md`; a regra foi reescrita por extenso e a resposta passou sem ajustes |
| `prob-padronizar` | correta: $z=(x-\mu)/\sigma$, Φ acumulada, tabela 0..z + 0,5, conferir variância × desvio |
| `prob-fora` | correta: diz que é de Física 2 e não cita fontes |

Nenhuma resposta teve rótulo inexistente. Falta repetir com o modelo principal quando ele estiver disponível.

## Complemento de Ciência da Computação (22/11/2026)

A ementa de CCOM022 no PPC de Ciência da Computação (matriz 2011, `ufal-ppc-cc-2011`) traz análise exploratória, probabilidade, distribuições, esperança e variância, inferência e ferramentas: os mesmos tópicos de `prob`. Não há disciplina separada.

Fontes usadas: `ufal-cc-prob-provas-heitor-2013` (provas de 2013 do Prof. Heitor S. Ramos Filho). Entraram 4 blocos, com `curso:` no cabeçalho:

| Bloco | Assunto | Status |
|---|---|---|
| `prob-cc-eventos-defeitos-custo` | prob-01-probabilidade-basica | corrigida |
| `prob-cc-limites-bayes-amostra` | prob-02-bayes | validada |
| `prob-cc-servidor-erlang-weibull` | prob-07-exponencial | validada |
| `prob-cc-overbooking-media-amostral` | prob-09-aproximacao-normal-tcl | validada |

A folha de respostas de 16/10/2013 tem três erros (o complementar de "todos ocorrem", a fórmula do custo e $P(C>2300)$), corrigidos em `prob-cc-eventos-defeitos-custo`.

Fora do acervo: a atividade AT1 (trabalho de alunos identificados pelo nome), o arquivo de dados de idades que a acompanha, o livro OpenIntro, as soluções do OpenIntro e os slides (já cobertos por `openintro-statistics`), e as outras provas (AB2, LE, reavaliações), que ficam como evidência dos tópicos. Estatística descritiva e inferência continuam sem bloco na busca.

## Complemento do 4º período de Engenharia de Computação (24/11/2026)

Material bruto do 4º período de EC (ECOM020, Prof. Petrucio A. Medeiros Barros), comparado com o catálogo e os blocos.

Fontes usadas: `ufal-prob-petrucio-listas-r` (listas de VA discretas e de distribuições contínuas, com dicas de R) e `ufal-prob-ec4-lista2-basica` (lista 2 de probabilidade básica com respostas). Entraram 6 blocos, com `curso:` no cabeçalho; os valores foram refeitos com `scipy.stats` e frações exatas em `tests_acervo/test_disciplina_prob.py`:

| Bloco | Assunto | Status |
|---|---|---|
| `prob-petrucio-binomial-r` | prob-05-distribuicoes-discretas | validada |
| `prob-petrucio-poisson-r` | prob-05-distribuicoes-discretas | validada |
| `prob-petrucio-normal-r` | prob-06-uniforme-normal | validada |
| `prob-petrucio-exponencial-r` | prob-07-exponencial | validada |
| `prob-petrucio-soma-media-normais-r` | prob-08-combinacao-linear | validada |
| `prob-ec4-lista2-basica` | prob-01-probabilidade-basica | corrigida |

Na lista 2, duas respostas do arquivo foram corrigidas (bilhetes: só a chance de perder; vacina chinesa: 28,57%, não 28,75%) e uma depende de convenção (cartas "maiores que 7").

Só referência (`ufal-prob-avaliacoes-petrucio-r`): AB1.1, AB2.1 e AB2.2 dependem da matrícula ou da base de dados de cada aluno, sem resposta única. Fora do acervo, sem citação: a lista 1 de questões e a lista 1 resolvida (mesmos assuntos de a01 a a04), os arquivos com nome de aluno (`AB2_*`, `02_PE_*`, a AB2.1 entregue), os trabalhos, os scripts `.R` (preparação de uma base de dados e estudo, sem procedimento que falte no acervo) e a pasta `Monitoria` (material de Sistemas Digitais, que não é desta disciplina; não foi usado para não sobrepor a PR #104). A pasta `C4` dentro de `ab2.1` é cópia do material de Cálculo 4 e foi tratada naquela disciplina.

## 7. Pendências

- Autorização do autor das anotações para publicar a transcrição. Até lá, ficam só paráfrases.
- Professor, instituição e enunciados das provas (questões 3 e 4) de 2025.2. A resolução do elevador continua pendente.
- Revisão humana das 6 notas da equipe. Sem ela, descritiva, estimação, testes de hipóteses e regressão, que são fundamentais na ementa, ficam sem bloco na busca.
- `revisao_humana` e `revisao_professor` de todos os blocos continuam pendentes.
- Repetir a bateria com o modelo principal do Gemini (nesta data, HTTP 503).
