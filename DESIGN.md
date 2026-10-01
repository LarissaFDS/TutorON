# DESIGN.md — como o TutorON se parece, e por quê

Este arquivo é para quem for criar ou mudar uma tela do TutorON, inclusive agentes de IA. Leia antes de escrever CSS ou texto de interface. Se uma regra daqui atrapalhar uma necessidade real, mude a regra aqui primeiro e explique o motivo; não abra exceção em silêncio dentro de uma tela.

## Para quem é e o que a interface precisa fazer

O TutorON é monitoria de **Projeto e Análise de Algoritmos (PAA) da UFAL**. Quem usa:

- **Alunos** lendo respostas longas, com recorrências, provas por indução e pseudocódigo, e julgando se elas ajudam a estudar para a prova.
- **A equipe e o professor** lendo relatórios de avaliação para decidir se a RAG melhora as respostas.

A tarefa principal é **ler com atenção e avaliar**. Não é vender um produto. Por isso a interface recua e o texto da resposta vem para frente.

## A ideia visual

O vocabulário vem da própria disciplina: **quadro-verde da sala, folha de prova quadriculada, marca-texto do aluno e caneta vermelha da correção.**

- **Um único gesto forte**: a faixa do topo (`.masthead`) em verde de quadro com a quadrícula da folha. Ela aparece uma vez por tela, no topo. Nada mais na página compete com ela.
- **Marca-texto significa "o que você escolheu"**: a nota marcada, a dúvida selecionada. Não use o amarelo para decorar, destacar título ou chamar atenção.
- **Vermelho é só erro.** Verde-sucesso é só confirmação.

### O que evitamos de propósito

Estes padrões são o que faz uma tela parecer gerada automaticamente. Não traga de volta:

- Gradientes azul/roxo, glassmorphism, sombras suaves em tudo.
- Todo bloco dentro de um card arredondado igual. Cards aqui só para **coisas comparáveis lado a lado** (as respostas A e B) e para o enunciado.
- Rótulo em caixa alta e espaçado acima de cada título ("LABORATÓRIO DE RESPOSTAS").
- Pílulas de metadado com "A · B · C".
- Hero centralizado com botão único e grade de três cards.
- Ícones e emojis decorativos. Hoje não usamos ícones; se um dia forem necessários, um conjunto só, mesmo peso e tamanho.
- Frases genéricas ("Transforme sua jornada de aprendizado"). Escreva o que a tela faz para um aluno de PAA.
- Destacar uma palavra do título com outra cor ou itálico. O logotipo "Tutor**ON**" é a única exceção, porque é marca.

## Onde está cada coisa

```
design/
├── tokens/
│   ├── colors.css       cores por papel, claro e escuro
│   ├── typography.css   famílias, 5 tamanhos, pesos
│   ├── spacing.css      passos de 4 px, largura de página e de leitura
│   └── shape.css        raio, bordas, foco (sem sombras)
├── base.css             reset, foco, .prose (texto de resposta), código, matemática
├── components.css       componentes compartilhados (lista abaixo)
├── report.css           só para o relatório da PoC (run_demo.py)
├── text.js              renderizador local de Markdown + TeX leve das respostas
└── __init__.py          stylesheet() e script(): junta as camadas na ordem certa
```

Não há bundler. `acervo/app.py` serve `/design.css` e `/text.js` para a página de validação; `run_demo.py` embute o CSS no relatório, que é um arquivo HTML avulso. Para criar uma tela nova, sirva ou embuta `design.stylesheet()` do mesmo jeito; não copie valores para dentro da página.

## Paleta

Os nomes são de papel, não de cor. Use sempre a variável, nunca o hex.

| Token | Claro | Uso |
|---|---|---|
| `--color-canvas` | `#f3f5f2` | Fundo da página (folha) |
| `--color-surface` | `#fbfcfa` | Blocos que precisam se separar do fundo |
| `--color-surface-sunken` | `#eaeee8` | Código, pseudocódigo, hover de linha |
| `--color-ink` | `#1a2420` | Texto principal |
| `--color-ink-muted` | `#56625c` | Texto de apoio, legendas |
| `--color-hairline` / `-strong` | `#d5dbd4` / `#a9b5ad` | Fios divisórios / bordas de controle |
| `--color-board` | `#1f3b32` | Quadro-verde: faixa do topo e botão principal |
| `--color-chalk` / `-muted` | `#eef2ec` / `#b8c6be` | Texto sobre o quadro |
| `--color-highlight` / `-soft` | `#f2da5e` / `#fbf3c6` | Marca-texto: escolha da pessoa |
| `--color-focus` | `#2f6f5a` | Anel de foco, links |
| `--color-danger` / `-soft` | `#a8322a` / `#f7e4e1` | Erro |
| `--color-success` / `-soft` | `#276b45` / `#e1efe5` | Confirmação |
| `--color-warning` / `-soft` | `#7d5a09` / `#f8eed0` | Aviso (ex.: modo de demonstração) |

O modo escuro redefine os mesmos tokens em `@media (prefers-color-scheme: dark)`. Nenhum componente deve testar o tema por conta própria.

Nada de `#fff` ou `#000` puros: a folha e a tinta são levemente esverdeadas, coerentes com o quadro.

## Tipografia

Três vozes, cada uma com um papel:

| Família | Token | Para quê |
|---|---|---|
| Serifa de leitura (Charter, Sitka, Cambria…) | `--font-reading` | Respostas e enunciados: o que se lê com atenção |
| Sans do sistema (Segoe UI, system-ui…) | `--font-ui` | Interface: rótulos, botões, títulos de etapa |
| Mono (Cascadia Mono, Consolas…) | `--font-code` | Pseudocódigo e código, como nas provas |

Todas são fontes locais, sem Google Fonts. **A validação com alunos precisa funcionar sem internet.**

Escala com **cinco tamanhos**. Não crie um sexto:

| Token | Tamanho | Uso |
|---|---|---|
| `--text-caption` | 13 px | Dicas, metadados, rodapé |
| `--text-ui` | 15 px | Corpo da interface, botões, títulos dentro de respostas |
| `--text-reading` | 17 px | Respostas e enunciados |
| `--text-title` | 22 px | Título de etapa ou seção |
| `--text-display` | 28–38 px | Título da página, um por tela |

Pesos: 400, 600 e 700. Títulos grandes levam `--tracking-display` (espaçamento negativo). Os títulos dentro de uma resposta (`### …`) são rebaixados para o tamanho da interface: a resposta não pode competir com a estrutura da página.

## Espaço, forma e profundidade

- Espaçamento só em `--space-1` a `--space-8` (4, 8, 12, 16, 24, 32, 48, 64 px). Espaço grande separa etapas; pequeno agrupa o que é do mesmo assunto.
- Parágrafos lidos não passam de `--measure` (68 caracteres).
- Um raio para tudo: `--radius` (6 px). Pílula (`--radius-pill`) só em `.tag`.
- **Sem sombras.** Profundidade vem de superfície mais fio. O único anel é o de foco, que é informação.
- Pseudocódigo tem régua à esquerda (`--rule-accent`), como o código numa folha de prova.

## Componentes

Cada um existe por um motivo de uso. Antes de criar outro, veja se um destes resolve.

| Classe | Por que existe |
|---|---|
| `.masthead` | Identidade e contexto da tela, uma vez, no topo |
| `.step` | Fluxo com ordem real (escolher → ler → avaliar). Não numere o que não é sequência |
| `.button` / `.button--secondary` | Uma ação principal por etapa. O rótulo diz o que acontece: "Enviar avaliação" leva a "Avaliação enviada" |
| `.choice-list` / `.choice` | Escolher entre itens com texto longo. Substituiu um `<select>` que cortava o enunciado |
| `.scale` / `.pick` | Nota de 1 a 5 com um toque (alvo de 44 px). Substituiu seis menus "Nota ▾" |
| `.field` / `.input` | Campos com rótulo visível e dica embaixo, nunca só placeholder |
| `.question` | Enunciado do aluno, com pseudocódigo |
| `.answer` | Respostas comparadas. **No teste cego, A e B têm tratamento idêntico** |
| `.notice` | Aviso que muda a leitura da tela (ex.: dados de demonstração) |
| `.status` | Mensagem viva (`aria-live`): `data-tone="busy"`, `"error"` |
| `.confirmation` | Estado de sucesso com o próximo passo |
| `.table` | Dados comparáveis. Números à direita, com `tabular-nums` |
| `.prose` | Texto de resposta renderizado |

## Texto de interface

- Escreva do ponto de vista do aluno de PAA, em português claro, frases curtas, caixa normal.
- Botão diz o verbo e o objeto: "Comparar respostas", "Enviar avaliação", "Comparar outra dúvida".
- Erro diz o que aconteceu e como resolver, sem pedir desculpas. Ex.: "Falta a nota de clareza da Resposta B."
- Estado vazio convida à ação. Ex.: "Ainda não há respostas prontas. Rode atualizar_acervo.bat…"
- Nunca peça nem incentive nome, matrícula ou contato.
- Não revele no texto qual resposta usa o material da disciplina. O estudo é cego.

## Estados que toda tela precisa ter

Carregando, vazio, erro, sucesso e desabilitado durante envio. Se a ação pode demorar (gerar resposta no modelo local leva minutos), diga isso antes, no botão e no status.

## Qualidade mínima

- Funciona em 390 px de largura sem rolagem horizontal da página. Código pode rolar dentro do próprio bloco.
- Foco visível em tudo que é interativo; rótulos ligados aos campos; grupos de rádio em `fieldset` com `legend`.
- Respeita `prefers-reduced-motion` e `prefers-color-scheme`.
- Cor nunca é o único sinal: ✓/✗ no checklist, texto no status.

## Respostas da IA na tela

As respostas chegam em Markdown com LaTeX. `design/text.js` converte localmente títulos, listas, negrito, código e matemática simples (`\le` → ≤, `2^{n}` → 2ⁿ, `\frac{a}{b}` → a/b). Todo o texto é escapado antes; o renderizador não gera links nem atributos arbitrários. Se falhar, a resposta aparece como texto puro, nunca em branco.

O relatório da PoC, que é interno e aberto com internet, continua usando marked + KaTeX.

## Antes e depois

Capturas do redesign de 30/09/2026 em [`docs/redesign/`](docs/redesign/): escolha da dúvida, respostas, celular, relatório e modo escuro.

## Como verificar

`python -m pytest tests_acervo` roda `tests_acervo/test_design.py`, que confere:

- que toda variável CSS usada existe nos tokens;
- que a escala tem cinco tamanhos;
- que a página de validação não carrega nada da internet e só referencia arquivos servidos;
- que o contrato com a API (`/api/questoes`, `/api/comparar`, `/api/votar`) continua igual;
- que o renderizador escapa HTML (precisa de Node.js; sem ele, o teste é pulado).
