# Variáveis Complexas — curadoria do acervo

Situação: **MVP** desde 20/11/2026: liberada no atendimento normal depois que a suíte completa, a bateria de relevância e as 6 perguntas com a IA real (Gemini e modelo local) passaram, sem nota de IA na busca e com bloco na busca para todo tópico coberto pelas provas. O acervo continua com as pendências da seção 7: resoluções da equipe `pendente_professor`, notas de IA fora da busca e transcrição não autorizada para publicação. A disciplina usa o mesmo fluxo e a mesma IA das outras.

| Item | Estado em 20/11/2026 |
|---|---|
| Cadastro, acervo (20 blocos) e índice híbrido (`bge-m3`) | **Feitos**; 13 blocos na busca, as 7 notas da equipe (IA) ficam fora até a revisão humana |
| Contas das resoluções | **Conferidas com SymPy e NumPy** (`tests_acervo/test_disciplina_varcomp.py`) |
| Gabarito oficial das provas | **Não existe**: as 13 resoluções estão como `pendente_professor` |
| Autorização para versionar e publicar as provas | **Não dada**: PDFs e foto fora do repositório; enunciados parafraseados com os dados |
| Revisão humana interna | **Pendente** em todos os blocos |
| Aprovação do professor | **Não declarada**; nenhum bloco tem `revisao_professor: sim` |
| Ementa oficial | **Conferida** no PPC de 2014 (seção 1) |
| Validação das respostas da IA | Seção 6 |

- Catálogo legível por máquina: [`fontes.json`](fontes.json)
- Blocos: [`materiais/`](materiais/). `p*` são resoluções da Prova 1 (versões A, B e C); `n*` são notas da equipe escritas com IA (candidatas)
- Gerados a partir dos blocos (não editar à mão): [`acervo/itens.json`](acervo/itens.json) e [`acervo/indice.json`](acervo/indice.json)
- Regras de rigor do tutor: [`rigor.md`](rigor.md)

## 1. Disciplina, professor e ementa

O cabeçalho das três provas diz: Universidade Federal de Alagoas, Instituto de Computação, Professor(a) **Xu Yang**, curso "Variáveis Complexas", **Prova 1**. Os PDFs foram gerados com pdfLaTeX em 21/03/2021; a foto de WhatsApp que repete a versão C é de 03/04/2021. O semestre não aparece nas provas.

O PPC de Engenharia de Computação de 2014 (`ufal-ppc-ecomp-2014`, p. 20 e 37 do PDF) lista **ECOM024 Variáveis Complexas**, 4º semestre, 60 h (40 teóricas e 20 práticas). Ementa, literal: "Números Complexos. Funções analíticas complexas. Representação conforme. Integração complexa. Método dos Resíduos. Funções harmônicas. Expansão em série de potências. A função Gamma. A fórmula de Stirling." Bibliografia básica: Ávila (*Variáveis complexas e aplicações*), Soares (*Cálculo em uma variável complexa*) e Hönig. As provas não dizem o código; a atribuição a ECOM024 vem do nome e da instituição.

### Tópicos, evidência e blocos

**Confirmado** = aparece nas provas; **fundamental** = está na ementa, sem material da turma; **complementar** = está na ementa, mas é periférico para a tutoria.

| Assunto | Classificação | Evidência | Blocos na busca | Notas IA (fora da busca) |
|---|---|---|---|---|
| `varcomp-01-numeros-complexos` | Confirmado | Q1 das três versões; ementa | p01–p04 | — |
| `varcomp-02-funcoes-analiticas-cauchy-riemann` | Fundamental | Ementa ("funções analíticas") | nenhum | n01 |
| `varcomp-03-funcoes-elementares` | Fundamental | Implícito na ementa (sen, cos, exp aparecem na Q2) | nenhum | n02 |
| `varcomp-04-integrais-de-contorno` | Confirmado | Q3 das três versões; ementa ("integração complexa") | p08–p10 | — |
| `varcomp-05-cauchy-goursat-primitivas` | Confirmado | Q4 das três versões | p11–p13 | — |
| `varcomp-06-formula-integral-cauchy` | Confirmado | Q2 das três versões | p05–p07 | — |
| `varcomp-07-series-taylor-laurent` | Fundamental | Ementa ("expansão em série de potências") | nenhum | n03 |
| `varcomp-08-residuos-singularidades` | Fundamental | Ementa ("método dos resíduos") | nenhum | n04 |
| `varcomp-09-representacao-conforme` | Fundamental | Ementa | nenhum | n05 |
| `varcomp-10-funcoes-harmonicas` | Fundamental | Ementa | nenhum | n06 |
| `varcomp-11-gamma-stirling` | Complementar | Ementa | nenhum | n07 |

Todos os tópicos confirmados pelas provas têm bloco na busca (critério 4 da liberação). Os fundamentais sem material ficam só em notas de IA fora da busca, até revisão humana. Perguntas sobre eles recebem a resposta pelo rigor e pelo conhecimento do modelo, sem fingir material da turma.

## 2. Fronteiras

A disciplina escolhida define o acervo; os índices são separados.

| Tema | Tratamento |
|---|---|
| Integrais de linha de campos vetoriais (Cálculo 3/4) | Fora; aqui só integrais complexas $\int f(z)\,dz$ |
| Números complexos em Sinais e Sistemas (Laplace, polos) e fasores em Circuitos | Fora; a aritmética complexa é a mesma, mas o acervo de cada disciplina é o seu |
| Resíduos para transformadas inversas | Só a teoria dos resíduos, em nota candidata |

O teste `test_isolamento_com_calculo3_sinais_e_circuitos` confere os dois sentidos com a busca léxica, e os índices não têm blocos em comum.

## 3. Inventário das provas e transcrição

Arquivos recebidos (nenhum está no repositório; o teste `test_provas_e_imagens_fora_do_repositorio` confere):

| Arquivo | Versão | Q1 | Q2 (curva $|z| = 3$, anti-horária) | Q3 | Q4 (segmento de 0 a) |
|---|---|---|---|---|---|
| `prova variaveis.pdf` | A | $(1+i)(1-2i)$; $|-i-2|^{1/2}$; $\frac{i^{10}-i^9}{2i+1}$; $(3+2i)\overline{(3-i)}$ | $\frac{\sin\pi z^2+\cos\pi z^2}{(z+1)(z-2)}$ e $\frac{e^z}{(z-2)^4}$ | $\frac1z$ e $\frac1{z^2}$ em $\gamma(t) = 2\cos t - i\sin t$ (**horária**) | $1-2i$ |
| `prova10.pdf` | B | $(2+i)(2-5i)$; $|-2i+5|^{1/2}$; $\frac{i^{12}-i^{15}}{2i+3}$; $(4+i)\overline{(3-2i)}$ | $\frac{\operatorname{sen}\pi z^2+\cos\pi z^2}{(z+0{,}5)(z-1{,}5)}$ e $\frac{e^{2z}}{(z-1{,}5)^4}$ | $\frac1{z-1}$ e $\frac1{(z-1)^2}$ em $|z| = 3$ | $3-4i$ |
| `prova16.pdf` | C | $(2-3i)(4+2i)$; $|-i+1|^{1/3}$; $\frac{i^{30}-i^{19}}{2i-1}$; $(3+2i)\overline{(7+i)}$ | $\frac{\sin\pi z^2+\cos\pi z^2}{(z-1)(z-2)}$ e $\frac{e^{2z}}{(z+1)^4}$ | $\frac1z$ e $\frac1{z^2}$ em $\gamma(t) = \cos t + 2i\sin t$ | $2+i$ |
| `WhatsApp Image 2021-04-03 at 18.58.46.jpeg` | C | duplicata da versão C, conferida com o PDF | | | |

Transcrição: o texto extraído dos PDFs perde sinais de menos, barras de conjugado e frações. Cada enunciado foi lido na imagem renderizada da página (110 dpi) e conferido símbolo a símbolo com o texto extraído (expoentes, números e letras). Pesos das questões: 2, 4, 2 e 2 pontos.

### Dúvidas de enunciado

- **Q1(b), as três versões:** "Ache todos os valores de $|w|^{1/n}$" com barras de módulo. O módulo é real positivo; "todos os valores" faz sentido para a raiz complexa $w^{1/n}$. Os blocos resolvem as duas leituras e deixam a escolha ao professor.
- **Q3, versão A:** $\gamma(t) = 2\cos t - i\sin t$ percorre a elipse no sentido horário, então $\oint dz/z = -2\pi i$. Não parece erro de digitação (as versões B e C são anti-horárias), mas é o ponto em que um aluno erra o sinal; está registrado no bloco.
- **Q2, versão B:** a primeira integral dá exatamente zero, porque $g(-0{,}5) = g(1{,}5) = \sqrt2$. É resultado legítimo, não um erro de enunciado; o bloco explica que o zero vem do cancelamento dos resíduos, não de Cauchy-Goursat.

## 4. Resoluções: status e verificação

Todas as 13 resoluções são da equipe TutorON, com `status_resolucao: pendente_professor` (não há gabarito). Nenhuma foi marcada `corrigida`, porque não há resolução original para corrigir. A verificação em `tests_acervo/test_disciplina_varcomp.py`:

- **Q1:** aritmética exata com SymPy; raízes elevadas de volta à potência; as raízes cúbicas comparadas com `numpy.roots`; argumento principal no quadrante certo ($-\pi + \arctan(1/2)$ para $-2-i$).
- **Q2:** soma dos resíduos (`sympy.residue`) dentro de $|z| = 3$ e integral numérica sobre a parametrização, com a derivada exata de $\gamma$ (regra do trapézio periódica). O teste também confere que esquecer o $3!$ muda o resultado.
- **Q3:** integral numérica sobre cada curva, com a orientação do enunciado, e o sentido de giro calculado de $\gamma'(0)$.
- **Q4:** primitiva, integral da parametrização com SymPy, integral numérica no segmento e por outro caminho (independência do caminho).
- **Notas IA:** cada valor (Cauchy-Riemann de $z^2$, $i^i$, série de Laurent, resíduo em $i$, $\int dx/(1+x^2) = \pi$, Möbius, $\Gamma(1/2)$, Stirling para n = 10) é refeito com SymPy, mas a revisão humana continua pendente.

Erros típicos cobertos pelos blocos: raiz cúbica com um só valor, argumento no quadrante errado, singularidade fora da curva, fator $n!$ esquecido, orientação ignorada e $\oint dz/z^2 \neq 0$.

## 5. Fontes

Matriz de critérios igual à das outras disciplinas (`fontes.json`, notas de 1 a 5).

| id | Fonte | Licença | Prioridade | Uso |
|---|---|---|---|---|
| `ufal-varcomp-prova1-2021` | Prova 1 (A, B e C), Prof. Xu Yang | não declarada; transcrição não autorizada | alta | acervo (paráfrase) |
| `ufal-ppc-ecomp-2014` | PPC de Engenharia de Computação, ECOM024 | documento público | alta | referência (ementa) |
| `beck-first-course-complex-analysis` | Beck, Marchesi, Pixton e Sabalka, *A First Course in Complex Analysis* | CC BY 4.0 | alta | citada nas notas |
| `mit-ocw-1804-2018` | MIT OCW 18.04 (Orloff, 2018) | CC BY-NC-SA 4.0 | alta | citada nas notas |
| `sympy` | SymPy | BSD | média | verificação |
| `avila-variaveis-complexas` | Ávila, *Variáveis complexas e aplicações* | protegida | referência | só catálogo |
| `churchill-variaveis-complexas` | Churchill, *Variáveis complexas e suas aplicações* | protegida | referência | só catálogo |

Não foi encontrada apostila aberta em português com licença declarada: a página da UNICAMP tentada respondeu 403 e a da UFMG não tem material da disciplina na página inicial. O sumário online de Beck veio vazio, então os capítulos não foram conferidos seção a seção; os tópicos do MIT foram conferidos pelos títulos das notas de aula, sem abrir os PDFs. Nenhum texto dessas fontes foi copiado para o acervo.

## 6. Blocos e verificação com a IA real

| id | Arquivo | Na busca |
|---|---|---|
| `varcomp-p1c-q1-operacoes` | p01 | sim |
| `varcomp-p1c-q1b-raizes-cubicas` | p02 | sim |
| `varcomp-p1a-q1-operacoes-raizes` | p03 | sim |
| `varcomp-p1b-q1-operacoes-raizes` | p04 | sim |
| `varcomp-p1c-q2-formula-cauchy` | p05 | sim |
| `varcomp-p1a-q2-formula-cauchy` | p06 | sim |
| `varcomp-p1b-q2-formula-cauchy` | p07 | sim |
| `varcomp-p1c-q3-1-sobre-z-elipse` | p08 | sim |
| `varcomp-p1a-q3-orientacao-horaria` | p09 | sim |
| `varcomp-p1b-q3-1-sobre-z-menos-1` | p10 | sim |
| `varcomp-p1c-q4-z2-segmento` | p11 | sim |
| `varcomp-p1a-q4-z2-segmento` | p12 | sim |
| `varcomp-p1b-q4-z2-segmento` | p13 | sim |
| `varcomp-nota-ia-cauchy-riemann` | n01 | não (candidata) |
| `varcomp-nota-ia-funcoes-elementares` | n02 | não (candidata) |
| `varcomp-nota-ia-taylor-laurent` | n03 | não (candidata) |
| `varcomp-nota-ia-residuos` | n04 | não (candidata) |
| `varcomp-nota-ia-conformes` | n05 | não (candidata) |
| `varcomp-nota-ia-harmonicas` | n06 | não (candidata) |
| `varcomp-nota-ia-gamma-stirling` | n07 | não (candidata) |

Busca (`eval/relevancia.py`, com o `bge-m3` real): as 5 perguntas de exemplo, 8 variantes em LaTeX e em texto simples e 5 perguntas de outras áreas passam. Limitação: "O que são as equações de Cauchy-Riemann?" traz blocos da fórmula integral de Cauchy (similaridade 0,46–0,52), pela palavra "Cauchy"; não há bloco de Cauchy-Riemann na busca. Com a nota n01 aprovada, ela passa a ser o primeiro resultado (`test_cauchy_riemann_so_teria_bloco_com_a_nota_aprovada`).

IA real: as 6 perguntas de `eval/bateria_tutor.py` rodaram em 20/11/2026 pelo fluxo completo, com o Gemini (`eval/results/bateria-varcomp-2026-11-20.json`) e só com o modelo local `tutoron-paa` (`…-local.json`), e as respostas foram lidas uma a uma. Raízes cúbicas de $1-i$, fórmula de Cauchy com $(z+1)^4$, $\oint 1/z$ vs $\oint 1/z^2$ e $\int z^2$ no segmento: corretas e socráticas nos dois (no segmento, o modelo local sugeriu a primitiva $z^3/3$ e o ajuste `entregou_resposta` atuou; o valor final não foi dado). Cauchy-Riemann: equações corretas nos dois; o Gemini disse que elas "garantem" a preservação de ângulos, impreciso (conformidade exige também $f' 
e 0$). Pergunta de fora (mapa de Karnaugh): o Gemini apontou Sistemas Digitais; o modelo local respondeu o conteúdo de Karnaugh sem dizer que é de outra disciplina, o mesmo comportamento já visto em Circuitos, Sinais, Controle e Eletrônica (a busca devolve vazio; não há trecho do acervo na resposta).

## 7. Pendências

- Autorização do professor (ou da equipe) para publicar a transcrição literal e versionar os PDFs.
- Confirmação das 13 resoluções e das leituras da Q1(b) pelo professor.
- Revisão humana das 7 notas de IA; só depois elas entram na busca.
- Material da turma (listas, slides, provas 2 e finais) para funções analíticas, séries, resíduos, conformes, harmônicas e Gamma.
- Conferir o sumário de Beck et al. seção a seção antes de usá-lo como base de notas.
