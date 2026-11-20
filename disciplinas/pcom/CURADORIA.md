# Curadoria — Princípios de Comunicação (`pcom`)

Atualizado em 20/11/2026. O acervo tem 33 blocos em `materiais/`. Destes, 28 estão na busca: são as anotações do aluno, parafraseadas e com cada resultado refeito por código (NumPy, SciPy e SymPy, `tests_acervo/test_disciplina_pcom.py`). Os outros 5 são notas da equipe escritas com IA (`nota_da_equipe_ia`); ficam como `candidato`, **fora da busca**, até passarem por revisão humana.

## 1. Ementa (PPC) e escopo

O PPC de Engenharia de Computação da UFAL (2014, `ufal-ppc-ecomp-2014`) define **ECOM034 Princípios de Comunicação** no 6º semestre: 60 h, sendo 40 teóricas e 20 práticas (grade na p. 21). A ementa (p. 43) é: sinais analógicos e digitais; introdução a processos estocásticos; ruídos em sistemas; transmissão de sinais em sistemas lineares; modulação e demodulação em banda base; codificação de linha; modulação e demodulação em banda passante; análise de enlaces; introdução à teoria da informação.
- Bibliografia: Lathi (`lathi-modern-digital-analog-communication`), Haykin (`haykin-intro-sistemas-comunicacao`), Proakis e Salehi (`proakis-salehi-communication-systems-engineering`). Só catálogo: protegidos. Os complementares do PPC (Young; Brennand e Souza Filho) não foram catalogados.

O PDF é o mesmo já usado nas outras disciplinas (SHA-256 `31a3c6e7…`).

Os cabeçalhos das simulações trazem "Docente: Jobson de Araújo Nascimento". A instituição não aparece escrita nas anotações. Nenhum material do professor foi recebido e ninguém da disciplina revisou o acervo.

## 2. Mapeamento de tópicos

| Tópico | Assunto | Evidência nas anotações | Na busca |
|---|---|---|---|
| 1 Sinais, espectro e Fourier | `pcom-01-sinais-espectro` | Sim | sim |
| 2 AM e DSB (índice, potência, banda, demodulação) | `pcom-02-am-dsb` | Sim | sim |
| 3 SSB e VSB | `pcom-03-ssb-vsb` | a confirmar (só figura colada) | não (nota IA candidata) |
| 4 Modulação em ângulo (PM, FM, Carson, Bessel) | `pcom-04-modulacao-angular` | Sim | sim |
| 5 Esquemas com filtros e moduladores | `pcom-05-filtros-esquemas` | Sim | sim |
| 6 Modulação digital (ASK, PSK, FSK, QAM, taxas) | `pcom-06-modulacao-digital` | Sim | sim |
| 7 Amostragem e PCM | `pcom-07-amostragem-pcm` | a confirmar (nenhuma) | não (nota IA candidata) |
| 8 Exposição a campos (Lista 4) | `pcom-08-exposicao-campos` | Sim (atribuição a confirmar) | sim |
| 9 Processos estocásticos e ruído | `pcom-09-ruido-processos` | não (só ementa) | não (nota IA candidata) |
| 10 Banda base e codificação de linha | `pcom-10-banda-base-codificacao-linha` | não (só ementa) | não (nota IA candidata) |
| 11 Enlaces e teoria da informação | `pcom-11-enlaces-teoria-informacao` | não (só ementa) | não (nota IA candidata) |

## 3. Inventário das anotações (`ufal-pcom-anotacoes-otavio-2026-2`)

O autor é Otávio Joshua Costa Brandão Menezes, aluno da turma de 2026.2 e membro da equipe. São anotações de estudo: **não são material do professor nem gabarito**.

**Autorização:** o registro da equipe é de que o autor autoriza publicar suas anotações (ver `fontes.json` > `autorizacao_transcricao`). Mesmo assim, os enunciados de listas e de provas foram **parafraseados**, as figuras foram descritas em texto, e os PDFs e imagens ficam fora do repositório.

| Arquivo (data) | Páginas | Blocos |
|---|---|---|
| conceitos iniciais (22 ago. 2026) | 3 | `pcom-anot-portadora-fase-instantanea`, `pcom-anot-fourier-cosseno-espectro`, `pcom-anot-pm-fm-diferenca` |
| Modulação AM (25 ago. 2026) | 3 | `pcom-anot-dsb-sc`, `pcom-anot-demodulacao-coerente`, `pcom-anot-am-convencional-indice` |
| Lista 1 pcom (26 ago. 2026) | 2 | `pcom-lista1-produto-cossenos` |
| Lista 2s (19 ago. 2026) | 3 | `pcom-lista2-fm-kf-bessel`, `pcom-lista2-fm-desvio-potencia`, `pcom-anot-desvio-beta-carson` |
| Simulação - Modulação FM e PM (27 ago. 2026) | 6 | `pcom-anot-pm-fm-diferenca` |
| Revisão prova 1 (30 ago. 2026) | 4 | `pcom-revisao-filtro-dsb-18000pi`, `pcom-revisao-am-envoltoria`, `pcom-anot-identidades-produto-cossenos`, `pcom-prova-angulo-dobra-amplitude` |
| Simulação Modulação AM (30 ago. 2026) | 14 | `pcom-anot-am-simulacao-k-m`, `pcom-anot-am-potencia-eficiencia`, `pcom-anot-largura-banda-am-dsb`, `pcom-anot-demodulacao-coerente` |
| fórmulas fundamentais para a prova 1 (7 set. 2026) | 7 | `pcom-anot-identidades-produto-cossenos`, `pcom-anot-fourier-cosseno-espectro`, `pcom-anot-am-convencional-indice`, `pcom-anot-am-potencia-eficiencia`, `pcom-anot-largura-banda-am-dsb`, `pcom-anot-desvio-beta-carson`, `pcom-prova-filtro-cos2-8000t`, `pcom-prova-am-potencia-88w` |
| Revisão Final prova 1 (9 set. 2026) | 8 | `pcom-prova-filtro-17khz`, `pcom-prova-x-cos1000pi-cos5000pi`, `pcom-revisao-am-espectro-impulsos`, `pcom-prova-angulo-dobra-amplitude`, `pcom-anot-identidades-produto-cossenos` |
| Modulação Digital (23 set. 2026) | 8 | `pcom-anot-digital-conceitos-baud`, `pcom-lista3-taxas-qam`, `pcom-lista3-eficiencia-espectral` |
| Simulação - Modulação Digital (30 set. 2026) | 8 | `pcom-sim-digital-ask-psk-fsk-qam` |
| Lista 4 (22 out. 2026) | 2 | `pcom-lista4-exposicao-60hz`, `pcom-lista4-distancia-separacao` |

A Lista 4 (exposição a campos eletromagnéticos) foi atribuída a esta disciplina pela sequência das listas (as Listas 1 a 3 são de Comunicação) e pela data; não há confirmação escrita.

### Erros encontrados e status de cada resolução

Cada resultado foi refeito por código: espectros por FFT, potências pela média de $s^2(t)$, desvios por derivação numérica da fase, raias de FM com `scipy.special.jv`, filtros com Butterworth e com filtro ideal por FFT, identidades com SymPy, taxas e limites com `fractions`.

| Bloco | Status | O que estava nas anotações | Correção |
|---|---|---|---|
| `pcom-anot-fourier-cosseno-espectro` | corrigida | par em rad/s escrito como $X(f)$ | $X(\omega)$; pesos do exemplo completados |
| `pcom-anot-identidades-produto-cossenos` | corrigida | $\cos a\cos b = \frac12[\cos(a+b) - \cos(a-b)]$ | sinal **mais** |
| `pcom-anot-dsb-sc` | corrigida | linha da portadora desenhada no espectro DSB-SC | portadora suprimida, sem linha em $f_c$ |
| `pcom-anot-demodulacao-coerente` | corrigida | troca de $f_c$ (3000 para 1500 Hz) entre partes da simulação sem aviso; "filtro de 600 Hz" | troca indicada; 600 Hz é bilateral (corte em 300 Hz) |
| `pcom-anot-am-convencional-indice` | corrigida | $B = A_c\mu/2$ | $B = A_c\mu$; $A_c\mu/2$ é cada banda lateral |
| `pcom-prova-am-potencia-88w` | corrigida | rótulos "amplitude da mensagem/portadora" trocados | rótulos corrigidos; 88 W confere |
| `pcom-revisao-am-envoltoria` | corrigida | identidade com sinal trocado | sinal mais; 19 W confere |
| `pcom-prova-filtro-cos2-8000t` | corrigida | rótulos do eixo (15, 16, 17) e "6000 rad/s" sem dizer bilateral | faixas 13–15 e 17–19 mil rad/s; corte em 3000 rad/s |
| `pcom-lista1-produto-cossenos` | corrigida | exercício só montado | resolução completa da equipe (complemento) |
| `pcom-anot-largura-banda-am-dsb` | corrigida | "largura de banda do sinal modulado" como $f_c - f_d$; "filtro $2f_c$" | $B_T = 2W$; $2f_c$ é largura bilateral |
| `pcom-anot-pm-fm-diferenca` | corrigida | FM com $\phi = \beta m(t)$; código com $m$ seno e fase $\beta\sin$ | $\phi = k_f\int m$; com tom, $\beta\sin$ vem de $m = \cos$ |
| `pcom-anot-desvio-beta-carson` | corrigida | "$\Delta\omega = 12$ kHz" | $\Delta\omega$ em rad/s; em Hz é $\Delta f$ |
| `pcom-lista2-fm-kf-bessel` | corrigida | $t$ omitido no termo da portadora; $J_3$, $J_4$ arredondados (0,02 e 0,001 V) | $2\pi 10^3 t$; 0,026 e 0,0016 V |
| `pcom-lista2-fm-desvio-potencia` | corrigida | "$\Delta f = 100\pi$" | $\Delta\omega = 100\pi$ rad/s, $\Delta f = 50$ Hz; Carson dado ao lado de $2\Delta f$ |
| `pcom-prova-filtro-17khz` | pendente_professor | pico de A desenhado como 2; $B$ depende da convenção | pico 4; 500 Hz (bilateral) ou 9 kHz (corte) |
| `pcom-prova-angulo-dobra-amplitude` | pendente_professor | conta de PM num enunciado "em ângulo"; amplitude $5/(2\pi)$ | FM 52 kHz, PM 36 kHz; amplitude de $m$ exige $k_f$ |
| `pcom-lista3-eficiencia-espectral` | pendente_professor | enunciados não transcritos; $V_m = 2W$ sem justificativa | $\eta = \log_2 M$ (ideal), $2/(1+\alpha)$ para QPSK |
| `pcom-lista4-exposicao-60hz` | pendente_professor | 4,16 kV/m; "colocar conformidade" estando acima do limite | 4,17 kV/m; acima do limite é não conforme; soma ICNIRP dada |
| `pcom-lista4-distancia-separacao` | pendente_professor | fator 23 de origem desconhecida | fator 6 da IEC 60601-1-2 dado ao lado (0,6 m) |
| demais blocos `pcom-*` | validada | — | resultado das anotações confere com o código |

Os blocos validados são `pcom-anot-portadora-fase-instantanea`, `pcom-anot-am-potencia-eficiencia`, `pcom-anot-am-simulacao-k-m`, `pcom-revisao-am-espectro-impulsos`, `pcom-revisao-filtro-dsb-18000pi`, `pcom-prova-x-cos1000pi-cos5000pi`, `pcom-anot-digital-conceitos-baud`, `pcom-lista3-taxas-qam` e `pcom-sim-digital-ask-psk-fsk-qam`.

### O que não entrou

- Fotos de slide, capturas de tela e figuras coladas (descritas e parafraseadas, não copiadas), incluindo a figura de SSB.
- Gráficos dos enunciados que não estão nas anotações: os valores usados são os lidos pelo aluno, e isso está dito nos blocos.

## 4. Notas da equipe (IA, fora da busca)

| Bloco | Assunto | Situação |
|---|---|---|
| `pcom-nota-ia-ssb-vsb` | SSB e VSB | candidato, revisão humana pendente |
| `pcom-nota-ia-amostragem-pcm` | amostragem e PCM | candidato, revisão humana pendente |
| `pcom-nota-ia-ruido-processos` | processos estocásticos e ruído | candidato, revisão humana pendente |
| `pcom-nota-ia-codigos-linha` | banda base e codificação de linha | candidato, revisão humana pendente |
| `pcom-nota-ia-enlaces-informacao` | enlaces e teoria da informação | candidato, revisão humana pendente |

## 5. Fronteiras com outras disciplinas

- **Sinais e Sistemas** (`sinais`): Fourier aparece nas duas. Aqui o foco é o espectro de sinais modulados e o projeto de moduladores e filtros; propriedades gerais da transformada são de Sinais. Isolamento testado nas duas direções.
- **Física 2** (`fis2`): campos elétricos aparecem na Lista 4 só como limite de exposição; eletrostática e ondas são de Física 2. Isolamento testado nas duas direções.
- **Probabilidade** (`prob`): processos estocásticos e ruído usam probabilidade; aqui ainda não há material aprovado.

## 6. Catálogo de fontes

| Fonte | Licença | Prioridade | Uso |
|---|---|---|---|
| `ufal-pcom-anotacoes-otavio-2026-2` | não declarada; autorização do autor | alta | acervo |
| `ufal-ppc-ecomp-2014` | documento institucional | referência | ementa |
| `mit-ocw-6-02` | CC BY-NC-SA 4.0 (a confirmar) | média | citada nas notas IA e na eficiência espectral |
| `frost-intro-communication-systems` | não confirmada | referência | citada na nota IA de SSB |
| `kuphaldt-socratic-modulation` | CC BY 4.0 | referência | catálogo |
| `icnirp-1998-diretrizes` | protegida | média | limites da Lista 4 |
| `aneel-ren-398-2010` | ato normativo público | média | limites de 60 Hz da Lista 4 |
| `iec-60601-1-2` | protegida | referência | distância de separação da Lista 4 |
| `lathi-modern-digital-analog-communication` | protegida | referência | bibliografia do PPC |
| `haykin-intro-sistemas-comunicacao` | protegida | referência | bibliografia do PPC |
| `proakis-salehi-communication-systems-engineering` | protegida | referência | bibliografia do PPC |

Nenhuma fonte aberta foi ingerida nesta versão. A vigência atual da REN 398/2010 não foi confirmada.

## 7. Pendências

- Revisão humana de todos os blocos (`revisao_humana: pendente`); confirmação do professor, que não foi pedida, em especial dos cinco blocos `pendente_professor`.
- Confirmar que a Lista 4 é desta disciplina.
- Material da turma para SSB e VSB, amostragem e PCM, ruído, codificação de linha, enlaces e teoria da informação (na ementa); revisão das notas IA.
- Confirmar autoria e licença de `frost-intro-communication-systems` e a licença de `mit-ocw-6-02`.
