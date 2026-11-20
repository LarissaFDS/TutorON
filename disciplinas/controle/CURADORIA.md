# Curadoria — Sistemas de Controle (`controle`)

Atualizado em 19/11/2026. O acervo tem 24 blocos em `materiais/`. Destes, 22 estão na busca: são as anotações do aluno, parafraseadas e com cada resultado refeito por código (SymPy, NumPy e SciPy, `tests_acervo/test_disciplina_controle.py`). Os outros 2 são notas da equipe escritas com IA (`nota_da_equipe_ia`); ficam como `candidato`, **fora da busca**, até passarem por revisão humana.

## 1. Ementa (PPC) e escopo

O PPC de Engenharia de Computação da UFAL (2014, `ufal-ppc-ecomp-2014`) define **ECOM037 Sistemas de Controle 1** no 6º semestre: 60 h, sendo 40 teóricas e 20 práticas (grade na p. 21). A ementa (p. 44) é: introdução; modelagem por diagrama de blocos; malha aberta e malha fechada; estabilidade pela função de transferência; critério de Routh-Hurwitz; lugar geométrico das raízes; projeto de compensadores pelo lugar das raízes; resposta em frequência; diagramas de Bode e de Nyquist; projeto pela resposta em frequência; margens de fase e de ganho; estruturas de compensação; controladores P, PI, PD e PID.
- Bibliografia: Ogata (`ogata-engenharia-controle-moderno`), Dorf e Bishop (`dorf-bishop-sistemas-controle-modernos`), Nise (`nise-control-systems-engineering`). Só catálogo: protegidos.

O PDF é o mesmo já usado nas outras disciplinas (SHA-256 `31a3c6e7…`). Espaço de estados e controle digital são de ECOM058 Sistemas de Controle 2 e ficam fora.

O professor não aparece nos cabeçalhos; uma anotação cita só um primeiro nome, o que não basta para identificá-lo. Nenhum material do professor foi recebido e ninguém da disciplina revisou o acervo.

## 2. Mapeamento de tópicos

| Tópico | Assunto | Evidência nas anotações | Na busca |
|---|---|---|---|
| 1 Laplace e função de transferência | `controle-01-laplace-ft` | Sim | sim |
| 2 Modelagem (mecânica e elétrica) | `controle-02-modelagem` | Sim | sim |
| 3 Diagrama de blocos, malha aberta e fechada | `controle-03-diagramas-blocos` | Sim | sim |
| 4 Estabilidade e Routh-Hurwitz | `controle-04-estabilidade-routh` | Sim | sim |
| 5 Resposta temporal (1ª e 2ª ordem) | `controle-05-resposta-temporal` | Sim | sim |
| 6 Erro em regime permanente | `controle-06-erro-regime` | Sim | sim |
| 7 Lugar das raízes | `controle-07-lugar-raizes` | Sim | sim |
| 8 Resposta em frequência (Bode, Nyquist, margens) | `controle-08-resposta-frequencia` | a confirmar (nenhuma) | não (nota IA candidata) |
| 9 Projeto de controladores e compensadores | `controle-09-projeto-controladores` | a confirmar (nenhuma) | não (nota IA candidata) |

## 3. Inventário das anotações (`ufal-controle-anotacoes-otavio-2026-2`)

O autor é Otávio Joshua Costa Brandão Menezes, aluno da turma de 2026.2 e membro da equipe. São anotações de estudo: **não são material do professor nem gabarito**.

**Autorização:** o registro da equipe é de que o autor autoriza publicar suas anotações (ver `fontes.json` > `autorizacao_transcricao`). Mesmo assim, os enunciados de livros e de provas foram **parafraseados**, as figuras foram descritas em texto, e os PDFs e imagens ficam fora do repositório.

| Arquivo (data AAMMDD) | Páginas | Blocos |
|---|---|---|
| `Revisão de Laplace e Sistemas mecânicos_260819` | 16 | `controle-anot-laplace-tvf`, `controle-anot-fracoes-parciais`, `controle-anot-massa-mola-amortecedor`, `controle-anot-suspensao`, `controle-anot-circuito-rc` |
| `Sistemas mecânicos_260819` | 6 (só a 1ª com conteúdo) | `controle-anot-massa-mola-amortecedor` |
| `Estabilidade de SLIT continuo_260909` | 10 | `controle-anot-bibo-polos`, `controle-anot-routh`, `controle-anot-routh-ganho` |
| `Diagrama de Blocos_261001` | 7 | `controle-anot-diagrama-blocos`, `controle-anot-diagrama-circuito` |
| `Análise de Resposta Temporal_261001` | 15 | `controle-anot-primeira-ordem`, `controle-anot-segunda-ordem`, `controle-anot-especificacoes-k`, `controle-anot-polo-zero-adicional` |
| `Revisão prova 1_261002` | 13 | `controle-anot-revisao-sensor`, `controle-anot-revisao-primeira-ordem`, `controle-anot-revisao-segunda-ordem` |
| `Resposta em Regime permanente_261020` | 9 | `controle-anot-erro-regime-tipo`, `controle-anot-erro-regime-exemplo`, `controle-anot-erro-perturbacao` |
| `Método Lugar das raízes_261111` | 10 (a última em branco) | `controle-anot-lugar-raizes-intro`, `controle-anot-lugar-raizes-regras` |

### Erros encontrados e status de cada resolução

Cada resultado foi refeito por código: transformadas e frações parciais com SymPy, raízes com NumPy, respostas com `scipy.signal.step` e `lsim`.

| Bloco | Status | O que estava nas anotações | Correção |
|---|---|---|---|
| `controle-anot-fracoes-parciais` | corrigida | Ex. 3 termina em $e^{-t} + t^2e^{-3t}$ | $e^{-t} + t^2e^{-t}$ |
| `controle-anot-circuito-rc` | corrigida | todos os termos de $V_i$ com sinal negativo (daria $G(0) = -1$) | sinais positivos, $G(0) = 1$ |
| `controle-anot-diagrama-blocos` | corrigida | "$1 \pm$ ganho de malha", sinal deixado em aberto | negativa: $1 + GH$; positiva: $1 - GH$ |
| `controle-anot-routh` | corrigida | Ex. 1 escrito com $2s^2$, mas a tabela usa coeficiente $1$ | tabela mantida para $s^2$; coluna do $2s^2$ também dada (2 raízes instáveis nos dois casos) |
| `controle-anot-segunda-ordem` | corrigida | polos sem $\omega_n$; $\omega_d = \omega_n\sqrt{\zeta^2 - 1}$; "$(\pi - \theta)/\sqrt{1 - \zeta^2} \approx 2$ para $0{,}4 \le \zeta \le 0{,}8$" | $-\zeta\omega_n \pm j\omega_n\sqrt{1 - \zeta^2}$; a razão vai de 2,16 a 4,16 |
| `controle-anot-revisao-segunda-ordem` | corrigida | 4.5 com $M_p = e^{-\zeta\pi\sqrt{1 - \zeta^2}}$: 25,65% e $y_{max} = 0{,}691$ | $M_p = 16{,}3\%$, $y_{max} = 0{,}646$ |
| `controle-anot-erro-regime-tipo` | corrigida | parábola unitária $t^2$ com $R = 1/s^3$; "$n_I > 3$" | $t^2/2$; $n_I \ge 3$ |
| `controle-anot-lugar-raizes-regras` | corrigida | raiz descartada escrita "0,26" sem sinal; partida 145° | $-0{,}27$; $144{,}7^\circ$ |
| demais blocos `controle-anot-*` | validada | — | resultado das anotações confere com o código |

Complementos da equipe, conferidos por código e marcados no texto: função de transferência do massa-mola-amortecedor $1/(ms^2 + bs + K)$ (em `controle-anot-massa-mola-amortecedor`); lugar das raízes de $K/(s(s + 2))$ (em `controle-anot-lugar-raizes-intro`); sinal da realimentação positiva.

Nenhuma resolução ficou `pendente_professor`: as que não puderam ser conferidas foram deixadas de fora.

### O que não entrou

- Revisão prova 1, exercício 4.2: depende de um gráfico que não está legível.
- Revisão prova 1, exercício 4.11: só foto do enunciado, sem resolução.
- Sistemas mecânicos, p. 2–6, e Lugar das raízes, p. 10: em branco.
- Fotos de quadro e de livro coladas (descritas e parafraseadas, não copiadas).

## 4. Notas da equipe (IA, fora da busca)

| Bloco | Assunto | Situação |
|---|---|---|
| `controle-nota-ia-resposta-frequencia` | Bode, Nyquist, margens | candidato, revisão humana pendente |
| `controle-nota-ia-projeto-controladores` | P, PI, PD, PID, avanço e atraso | candidato, revisão humana pendente |

## 5. Fronteiras com outras disciplinas

- **Sinais e Sistemas** (`sinais`): Laplace, função de transferência e BIBO aparecem nas duas. Aqui o foco é malha fechada, especificações e projeto; propriedades de sinais, convolução e Fourier são de Sinais. Isolamento testado nas duas direções.
- **Circuitos Elétricos** (`circ`): circuitos aparecem só como planta a modelar; resolver o circuito é de Circuitos. Isolamento testado nas duas direções.
- **Sistemas de Controle 2** (ECOM058): espaço de estados e controle digital, sem acervo.

## 6. Catálogo de fontes

| Fonte | Licença | Prioridade | Uso |
|---|---|---|---|
| `ufal-controle-anotacoes-otavio-2026-2` | não declarada; autorização do autor | alta | acervo |
| `ufal-ppc-ecomp-2014` | documento institucional | referência | ementa |
| `mit-ocw-16-06` | CC BY-NC-SA 4.0 | média | citada nas notas IA |
| `astrom-murray-feedback-systems` | CC BY-NC-SA 4.0 (wiki) | média | citada nas notas IA |
| `libretexts-iqbal-intro-control` | CC BY-NC-SA 4.0 | média | citada nas notas IA |
| `mit-ocw-6-302` | CC BY-NC-SA 4.0 | referência | catálogo |
| `mit-ocw-2-04a` | CC BY-NC-SA 4.0 | referência | catálogo |
| `python-control` | BSD-3-Clause | referência | ferramenta |
| `octave-control` | GPL-3.0-or-later e BSD-3-Clause | referência | ferramenta |
| `umich-ctms` | não verificada (HTTP 403) | referência | catálogo |
| `ogata-engenharia-controle-moderno` | protegida | referência | bibliografia do PPC |
| `dorf-bishop-sistemas-controle-modernos` | protegida | referência | bibliografia do PPC |
| `nise-control-systems-engineering` | protegida | referência | bibliografia do PPC |

Nenhuma fonte aberta foi ingerida nesta versão. Nenhuma das fontes abertas conferidas trata explicitamente de Routh-Hurwitz ou de erro em regime.

## 7. Pendências

- Revisão humana de todos os blocos (`revisao_humana: pendente`); confirmação do professor, que não foi pedida.
- Material da turma para resposta em frequência e projeto de controladores (na ementa); revisão das notas IA.
- Identificar o professor e a turma para a atribuição.
