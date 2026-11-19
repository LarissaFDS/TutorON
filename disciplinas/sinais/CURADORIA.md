# Curadoria — Sinais e Sistemas (`sinais`)

Atualizado em 19/11/2026. O acervo tem 29 blocos em `materiais/`. Destes, 28 estão na busca: são as anotações do aluno, parafraseadas e com cada resultado refeito por código (SymPy e SciPy, `tests_acervo/test_disciplina_sinais.py`). O outro é uma nota da equipe escrita com IA (`nota_da_equipe_ia`), que fica como `candidato`, **fora da busca**, até passar por revisão humana.

## 1. Ementa (PPC) e escopo

O PPC de Engenharia de Computação da UFAL (2014, `ufal-ppc-ecomp-2014`) define **ECOM030 Sinais e Sistemas** no 5º semestre: 90 h, sendo 60 teóricas e 30 práticas (grade na p. 20). A ementa (p. 40) é: sinais e sistemas em tempo contínuo; sistemas lineares e invariantes no tempo contínuo; função de transferência de tempo contínuo; convolução; aplicações da transformada de Laplace; domínio da frequência; diagramas de Bode; noções de projeto de filtros; série e transformada de Fourier.
- Bibliografia básica: Haykin e Van Veen (`haykin-veen-sinais-sistemas`), Lathi (`lathi-sinais-sistemas-lineares`), Oppenheim, Willsky e Nawab (`oppenheim-willsky-signals-systems`).
- Bibliografia complementar: Abrantes; Hsu.

O PDF foi baixado em 19/11/2026 (SHA-256 `31a3c6e7…`, o mesmo da cópia usada para Probabilidade e Circuitos).

O que a turma estudou e a ementa:
- **Tempo discreto** (amostragem, convolução discreta, transformada Z) **não está** na ementa de ECOM030; é de ECOM063 Processamento Digital de Sinais. Também não aparece nas anotações. Ficou como assunto `sinais-11-tempo-discreto` "a confirmar", só com nota IA candidata.
- **Diagramas de Bode e projeto de filtros** estão na ementa, mas **não** nas anotações. A resposta em frequência $G(j\omega)$ aparece em `sinais-anot-tf-pares-senoidal`. Não foi criado assunto próprio; é pendência.
- **Números complexos** e **EDO** não estão escritos na ementa, mas são pré-requisitos estudados pela turma.

O professor e a instituição não aparecem nos cabeçalhos das anotações. Nenhum material do professor foi recebido e ninguém da disciplina revisou o acervo.

## 2. Mapeamento de tópicos

| Tópico | Assunto | Evidência nas anotações | Na busca |
|---|---|---|---|
| 1 Números complexos | `sinais-01-complexos` | Sim | sim |
| 2 Operações no tempo | `sinais-02-operacoes-tempo` | Sim | sim |
| 3 Sinais elementares | `sinais-03-sinais-elementares` | Sim | sim |
| 4 Propriedades de sistemas | `sinais-04-propriedades-sistemas` | Sim | sim |
| 5 Convolução | `sinais-05-convolucao` | Sim | sim |
| 6 EDO | `sinais-06-edo` | Sim | sim |
| 7 Série de Fourier | `sinais-07-serie-fourier` | Sim | sim |
| 8 Transformada de Fourier | `sinais-08-transformada-fourier` | Sim | sim |
| 9 Laplace | `sinais-09-laplace` | Sim | sim |
| 10 Função de transferência | `sinais-10-funcao-transferencia` | Sim | sim |
| 11 Tempo discreto | `sinais-11-tempo-discreto` | a confirmar (nenhuma) | não (nota IA candidata) |

## 3. Inventário das anotações (`ufal-sinais-anotacoes-otavio-2026-1`)

O autor é Otávio Joshua Costa Brandão Menezes, aluno da turma de 2026.1 e membro da equipe. São anotações de estudo: **não são material do professor nem gabarito**.

**Autorização:** o autor autorizou publicar a transcrição, segundo informação da responsável pela curadoria em 18/11/2026; o registro está em `fontes.json` > `autorizacao_transcricao`. Mesmo assim, os enunciados de livros e de provas foram **parafraseados**, as fotos de quadro, slides e figuras foram descritas em texto, e os PDFs e imagens ficam fora do repositório.

| Arquivo (data AAMMDD) | Páginas | Blocos |
|---|---|---|
| `Revisão números complexos_260308` | 3 | `sinais-anot-numeros-complexos` |
| `Escalonamento e Deslocamento de tempo_260313` | 5 | `sinais-anot-escalonamento-deslocamento` |
| `Sistemas de Tempo Contínuo_260320` | 4 | `sinais-anot-sistemas-blocos` |
| `Modelos de Sinais_260404` | 7 | `sinais-anot-exponenciais`, `sinais-anot-degrau-rampa-impulso` |
| `Propriedades de Sistemas_260408` | 14 | `sinais-anot-memoria-causalidade`, `sinais-anot-bibo-invariancia`, `sinais-anot-linearidade`, `sinais-anot-integral-janela` |
| `Lista Sinais e Sistemas_260427` | 10 | `sinais-anot-lista-transformacoes`, `sinais-anot-lista-impulso` |
| `Descrição matemática de sistemas de tempo contínuo_260429` | 14 | `sinais-anot-convolucao-definicao`, `sinais-anot-convolucao-pulsos`, `sinais-anot-convolucao-exponencial` |
| `Modelos por equações diferenciais_260501` | 13 | `sinais-anot-modelos-edo`, `sinais-anot-edo-solucao` |
| `Represen em Série de Fourier…_260513` e `Rep em Série de Fourier…_260603` | 11 + 11 | `sinais-anot-serie-fourier-formulas`, `sinais-anot-serie-fourier-quadrada`, `sinais-anot-serie-fourier-exponencial` |
| `Transformada de Fourier_260528` | 13 | `sinais-anot-tf-pulso`, `sinais-anot-tf-pares-senoidal` |
| `Transformada de Laplace_260610` | 7 | `sinais-anot-laplace` |
| `Representação por função de transferência_260619` | 14 | `sinais-anot-funcao-transferencia`, `sinais-anot-fracoes-parciais-reais`, `sinais-anot-fracoes-parciais-complexos` |
| `Revisão Prova 2_260630` | 14 | `sinais-anot-revisao-bibo`, `sinais-anot-revisao-realimentacao`, `sinais-anot-questoes-prova` |

### Erros encontrados e status de cada resolução

Cada resultado foi refeito por código: integrais e transformadas com SymPy, convolução e coeficientes de Fourier por integração numérica (numpy, `scipy.integrate`), respostas com `dsolve`, `scipy.signal.freqresp`, `lsim` e `step`.

| Bloco | Status | O que estava nas anotações | Correção |
|---|---|---|---|
| `sinais-anot-numeros-complexos` | corrigida | ângulo $\tan^{-1}(b/a)$ também para $a<0$; recíproco com $e^{-jz}$; conjugado "$re^{-j\theta} = re^{j\theta}$" | somar $\pm\pi$ quando $a<0$; $\frac1re^{-j\theta}$; $z^* = re^{-j\theta}$ |
| `sinais-anot-exponenciais` | corrigida | "reduzida 36,8%" a cada $\tau$ | cai **para** 36,8% (redução de 63,2%) |
| `sinais-anot-degrau-rampa-impulso` | corrigida | $u(at - t_0) = u(t - t_0/a)$ para todo $a \ne 0$ | só para $a>0$; com $a<0$, $u(t_0/a - t)$ |
| `sinais-anot-memoria-causalidade` | corrigida | forma com $v_C(0)$ "para $t \le 0$" | vale para $t \ge 0$ |
| `sinais-anot-bibo-invariancia` | corrigida | indutor chamado de "marginalmente estável" porque algumas entradas dão saída limitada | não é BIBO estável; "marginal" é classificação por polos |
| `sinais-anot-edo-solucao` | corrigida | segunda versão do diagrama com $-b_0/a_3\,u$ | sinal positivo |
| `sinais-anot-fracoes-parciais-complexos` | corrigida | rótulos "devido à entrada" e "devido aos polos" trocados | termo 1 vem da entrada; $e^{-2t}$ dos polos |
| `sinais-anot-revisao-bibo` | corrigida | regra "partes reais negativas (>0)" | todos os polos com parte real **negativa** |
| `sinais-anot-revisao-realimentacao` | corrigida | $\theta = \tan^{-1}(1/(-10))$ sem $+\pi$; $\mathcal L\{e^{-at}\cos\omega t\} = \frac{s-a}{(s-a)^2+\omega^2}$ | $\theta = 174{,}29^\circ$; $\frac{s+a}{(s+a)^2+\omega^2}$ |
| `sinais-anot-questoes-prova` | corrigida | Q3 para em "acha M e resolve" | equipe completou: $M = 1/17$, $y(0) = 1/17$, $\dot y(0) = -4/17$ |
| `sinais-anot-convolucao-definicao` | validada | rótulo "$y(t)$" para a resposta ao impulso | esclarecido no texto; resultado confere |
| demais blocos `sinais-anot-*` | validada | — | resultado das anotações confere com o código |

Complementos da equipe, conferidos por código e marcados no texto: $y(t) = x(2t)$ é variante (contraexemplo com pulso), em `sinais-anot-bibo-invariancia`; convolução de dois pulsos retangulares (triângulo), em `sinais-anot-convolucao-pulsos`.

Nenhuma resolução ficou `pendente_professor`: as que não puderam ser conferidas foram deixadas de fora.

### O que não entrou

- Lista, questões 5 e 6: dependem de figuras que não podem ser copiadas.
- Convolução, item c (pulso de largura 2 com resposta ao degrau $1 - e^{-t}$): incompleto.
- Função de transferência, "para fazer" com fonte dependente $4v_L$: sem resolução.
- Fotos de quadro (parte da convolução pulso–rampa, refeita pela equipe a partir das contas), slides e enunciados de prova colados (parafraseados).
- Série de Fourier parte 2, p. 11: em branco.

## 4. Notas da equipe (IA, fora da busca)

| Bloco | Assunto | Situação |
|---|---|---|
| `sinais-nota-ia-tempo-discreto` | tempo discreto, amostragem, transformada Z | candidato, revisão humana pendente |

## 5. Fronteiras com outras disciplinas

- **Circuitos Elétricos** (`circ`): o circuito é só exemplo de sistema aqui (RL, RLC, função de transferência de um circuito); montar e resolver o circuito é de Circuitos. Isolamento testado nas duas direções.
- **Cálculo 3** (`calc3`): integrais e EDO como ferramenta; isolamento testado nas duas direções.
- **Sistemas de Controle** e **Princípios de Comunicação**: sem acervo no TutorON. Realimentação, posicionamento de polos e malha fechada aparecem aqui só como nas questões de revisão; modulação, Bode e filtros não têm material.
- **Processamento Digital de Sinais** (ECOM063): tempo discreto e transformada Z.

## 6. Catálogo de fontes

| Fonte | Licença | Prioridade | Uso |
|---|---|---|---|
| `ufal-sinais-anotacoes-otavio-2026-1` | não declarada; autorização do autor | alta | acervo |
| `ufal-ppc-ecomp-2014` | documento institucional | referência | ementa |
| `mit-ocw-6-003-2011` | CC BY-NC-SA 4.0 | alta | referência (candidata à ingestão) |
| `libretexts-baraniuk-signals-systems` | CC BY 4.0 | alta | referência (cobre tempo discreto) |
| `ulaby-yagle-signals-systems` | não determinada | média | referência |
| `scipy-signal` | BSD-3-Clause | média | ferramenta de verificação |
| `sympy` | BSD-3-Clause | média | ferramenta de verificação |
| `gnu-octave` | GPL-3.0 | referência | ferramenta |
| `lathi-sinais-sistemas-lineares` | protegida | referência | bibliografia do PPC |
| `oppenheim-willsky-signals-systems` | protegida | referência | bibliografia do PPC |
| `haykin-veen-sinais-sistemas` | protegida | referência | bibliografia do PPC |

Nenhuma fonte aberta foi ingerida nesta versão. A busca por apostilas brasileiras com licença aberta não encontrou nenhuma (planos de ensino de outras instituições não têm licença de reuso).

## 7. Pendências

- Revisão humana de todos os blocos (`revisao_humana: pendente`); confirmação do professor, que não foi pedida.
- Material da turma para Bode e filtros (na ementa) e decisão sobre tempo discreto; revisão da nota IA.
- Identificar o professor e a turma para a atribuição.
