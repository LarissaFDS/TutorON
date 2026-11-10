# Cálculo 3 — curadoria do acervo

Situação: **em validação** desde 02/11/2026. A disciplina está cadastrada, com acervo e índice próprios, e usa o mesmo fluxo e a mesma IA das outras. Enquanto a validação não acontecer, o servidor recusa perguntas de Cálculo 3 no atendimento normal (403, a mesma barreira de OAC). Para testes autorizados, use `TUTORON_LIBERAR_EM_VALIDACAO=calc3` (veja [`docs/DISCIPLINAS.md`](../../docs/DISCIPLINAS.md)).

| Item | Estado em 02/11/2026 |
|---|---|
| Cadastro, acervo (21 blocos) e índice híbrido (`bge-m3`) | **Feitos**; 16 blocos no índice, as 5 notas da equipe ficam fora até a revisão |
| Contas das resoluções | **Conferidas com SymPy** e numericamente (`tests_acervo/test_disciplina_calc3.py`) |
| Gabarito oficial das provas | **Não existe no material**: as 7 resoluções de prova estão como `pendente_professor` |
| Revisão humana interna | **Pendente** em todos os blocos; as 5 notas da equipe são `candidato` |
| Autorização para publicar transcrições das provas | **Não dada**: os blocos trazem enunciados parafraseados e os dados |
| Aprovação do professor | **Não declarada**; nenhum bloco tem `revisao_professor: sim` |
| Ementa oficial | **Não conferida literalmente** (seção 1) |
| Validação das respostas da IA | **Parcial**: 5 perguntas com o Gemini, todas corretas na matemática (seção 6); modelo local não testado |

- Catálogo legível por máquina (fonte da verdade): [`fontes.json`](fontes.json)
- Blocos (um arquivo por bloco): [`materiais/`](materiais/). `t*` são provas e exercícios resolvidos da turma; `r*` são resumos de aula; `s*` são anotações dos alunos no Notion; `n*` são notas da equipe (candidatas)
- Gerados a partir dos blocos (não editar à mão): [`acervo/itens.json`](acervo/itens.json) e [`acervo/indice.json`](acervo/indice.json)
- Regras de rigor do tutor em Cálculo 3: [`rigor.md`](rigor.md)

## 1. Disciplina e ementa

O cabeçalho das provas identifica a disciplina: **ECOM017 Cálculo 3**, Instituto de Computação da UFAL, **Prof. Tiago Alves de Almeida**, semestre **2024.1** (AB1 em 23/08/2024, AB2 em 22/11/2024, reavaliação em 26/11/2024). A página "Disciplinas" do IC lista literalmente "ECOM017 Cálculo 3 60h" no 3º período (`ufal-calc3-ppc`).

O texto da ementa no Projeto Pedagógico (versões 2011 e 2014) **não foi conferido literalmente**: o que temos veio de um resumo automático do PDF. Segundo esse resumo, a ementa trataria de curvas parametrizadas, comprimento de arco, curvatura e torção, triedro de Frenet; funções de várias variáveis, limite, continuidade, derivadas parciais, matriz jacobiana; derivadas direcionais, gradiente, regra da cadeia, funções implícitas e inversa; máximos e mínimos, multiplicadores de Lagrange e fórmula de Taylor. **Integrais múltiplas e cálculo vetorial (Green, Stokes, Gauss) não apareceriam** e provavelmente ficam em Cálculo 4, o que também não foi conferido. Até a conferência literal, nada da ementa é tratado como confirmado.

O livro-texto de fato é o Stewart: as listas da turma são páginas escaneadas dele (`ufal-calc3-listas-stewart`). As notas citam "Stewart, Clegg e Watson, *Cálculo*, vol. 2, 9ª ed., seção X.Y" (`stewart-calculo-vol2`) como referência externa. Nenhum arquivo do livro nem do manual de soluções foi baixado, versionado ou ingerido, e nenhuma solução do manual foi usada.

### Tópicos, evidência e blocos

Classificação: **confirmado** = aparece em prova, lista ou resumo da turma; **fundamental, não confirmado** = central no Stewart e citado no resumo da ementa, sem material da turma; **complementar** = pré-requisito ou provável Cálculo 4.

| Assunto | Classificação | Evidência | Stewart vol. 2 | Blocos |
|---|---|---|---|---|
| `calc3-01-curvas-parametricas` | Confirmado | AB1 Q1 e Q2; Resumo 1; lista 10.1; lista de conteúdos da AB1 | 10.1, 10.2 | t01, t02, r01, s01 |
| `calc3-02-coordenadas-polares` | Confirmado | AB1 Q3; lista de conteúdos da AB1 | 10.3, 10.4 | t03, n05 |
| `calc3-03-vetores-retas-planos` | Complementar (pré-requisito) | Quadro da 12.5 em "Fórmulas Úteis"; anotações "Vetor unitário e planos" | 12.1–12.6 | n04 |
| `calc3-04-funcoes-vetoriais` | Confirmado | Resumo 4; lista 13.1 ("Cálculo Vetorial") | 13.1, 13.2 | r03 |
| `calc3-05-comprimento-de-arco` | Confirmado | Resumos 2 e 5; lista de conteúdos da AB1 | 10.2, 13.3 | r02, r03 |
| `calc3-06-curvatura-movimento` | Confirmado (só anotações dos alunos) | Anotações "Curvatura e movimento"; resumo da ementa | 13.3, 13.4 | s02, n01 |
| `calc3-07-funcoes-varias-variaveis` | Confirmado (só anotações dos alunos) | Anotações "Funções de várias variáveis" | 14.1 | s03 |
| `calc3-08-limites-derivadas-parciais` | Confirmado | AB2 e reavaliação inteiras; exercícios resolvidos | 14.2, 14.3 | t04–t09, s04, n03 |
| `calc3-09-derivada-direcional-gradiente` | Fundamental, não confirmado | Página do Notion com o título, **vazia**; resumo da ementa | 14.6 | n02 |
| `calc3-10-plano-tangente-regra-da-cadeia` | Fundamental, não confirmado | Resumo da ementa | 14.4, 14.5 | nenhum |
| `calc3-11-maximos-minimos-lagrange` | Fundamental, não confirmado | Resumo da ementa | 14.7, 14.8 | nenhum |
| `calc3-12-integrais-multiplas` | Complementar (provável Cálculo 4) | Fora do resumo da ementa | 15 | nenhum |
| `calc3-13-campos-integrais-de-linha-green` | Complementar (provável Cálculo 4) | Fora do resumo da ementa; a "Lista Cálculo Vetorial" é de funções vetoriais | 16.1–16.4 | nenhum |
| `calc3-14-stokes-gauss` | Complementar (provável Cálculo 4) | Fora do resumo da ementa | 16.5–16.9 | nenhum |

Lacunas: plano tangente, regra da cadeia, funções implícitas, máximos e mínimos e Lagrange não têm bloco. A busca devolve vazio nesses temas, e o tutor responde só com o rigor e o conhecimento do modelo, sem fingir que há material da turma.

## 2. Fronteira com os pré-requisitos

A disciplina escolhida define o acervo; não há filtro por palavra-chave. "Vetor" e "derivada" existem em OAC (vetor = array), em PAA (vetor de inversões) e em Cálculo 3, mas cada índice é separado. Os testes `test_vocabulario_comum_fica_na_disciplina_escolhida` (acervo) e `test_vocabulario_comum_so_recupera_a_disciplina_escolhida` (backend) cobrem isso.

| Tema | Tratamento em Cálculo 3 |
|---|---|
| Derivada e integral de uma variável (Cálculo 1 e 2) | Usado sem bloco próprio; o tutor explica quando o aluno trava, mas o acervo não tem material de Cálculo 1 |
| Vetores, produto escalar e vetorial, retas e planos (Geometria Analítica, Stewart cap. 12) | Pré-requisito: uma nota da equipe (n04) porque o produto vetorial é usado em curvatura e T N B |
| Integrais múltiplas, Green, Stokes, Gauss | Provável Cálculo 4: assuntos cadastrados para o tutor saber classificar, sem blocos; o `rigor.md` já tem as regras de Jacobiano e orientação |
| EDPs (equação do calor, Laplace) | Só como verificação de derivadas parciais, como nas provas; não se resolve EDP |

## 3. Inventário do Notion da turma (workspace "Faculdade")

| Material | Conteúdo | Uso |
|---|---|---|
| Fotos de AB1, AB2 e reavaliação 2024.1 | Provas sem gabarito; AB2 e reavaliação com nome de aluno coberto | Enunciados parafraseados (t01–t07); **fotos não versionadas** |
| `Exercicios_Limites_Derivadas.pdf` (11 p., manuscrito) | Limites e parciais de várias variáveis (não é Cálculo 1) | t08, t09 |
| Resumos 1, 2, 4 e 5 (manuscritos, rotulados "Resumo do professor") | Paramétricas, comprimento de arco, funções vetoriais | r01–r03; **o Resumo 3 não está na página** |
| Listas 01, 02, Cálculo Vetorial e Fórmulas Úteis | Páginas escaneadas do Stewart (inglês) | Só mapeamento de seções; **protegidas, não transcritas** |
| `image.png` | Lista de conteúdos da AB1 | Evidência de tópicos |
| Páginas de anotações | Parametrização, curvatura, T N B, funções de várias variáveis, limites | s01–s04 |
| Páginas "Coordenada polar" e "Derivadas direcionais e vetor gradiente" | **Vazias** | — |
| Página "Funções vetoriais" e imagens das subpáginas | Quase só imagens (fotos de quadro e de WhatsApp) | **Não lidas**; podem conter conteúdo não inventariado |

Os originais foram baixados para leitura numa pasta temporária fora do repositório.

## 4. Resoluções: status e correções

Cada bloco da turma tem `status_resolucao` e diz o status no texto. A IA é instruída (`rigor.md`) a não apresentar resoluções corrigidas ou pendentes como gabarito oficial.

| Bloco | Status | O que mudou em relação ao material |
|---|---|---|
| `calc3-ab1-2024-q1-projetil` | pendente_professor | Resolução da equipe: b = 20, ângulo arctan 10 ≈ 84,29°, altura máxima 100 cm em t = 10 s, pouso em t = 20 s e x = 2040 cm, sem tangente vertical |
| `calc3-ab1-2024-q2-colisao` | pendente_professor | Elipse horária e circunferência anti-horária; colisão só em t = 3π/2, no ponto (−3, 0) |
| `calc3-ab1-2024-q3-cardioide` | pendente_professor | Inclinação −1 em π/3; tangentes horizontais em (0, 2) e (±√3/4, −1/4); θ = 3π/2 é cúspide, não tangente horizontal |
| `calc3-ab2-2024-q1q2-limite-parciais` | pendente_professor | Limite 0 por confronto; parciais 1/y e −x/y² |
| `calc3-ab2-2024-q3q4-edp` | pendente_professor | B = A²; δ = ±λ |
| `calc3-reav-2024-q1q2-limite-parciais` | pendente_professor | Limite não existe (0 nas retas, 1/3 em y = x³); parciais y²/(x+y²)² e 2xy − x³ |
| `calc3-reav-2024-q3q4-edp` | pendente_professor | T_xx + T_yy = T³ conferido; B = A² |
| `calc3-lista-limites-varias-variaveis` | corrigida | Ex. 6: o original escreveu 1/(1+m), o certo é 1/(1+\|m\|); a conclusão (não existe) se mantém |
| `calc3-lista-derivadas-parciais` | validada | Numeração "3" repetida no original (aqui 3a e 3b) |
| `calc3-resumo-curvas-parametricas`, `calc3-resumo-comprimento-de-arco`, `calc3-resumo-funcoes-vetoriais` | validada | Item "5" repetido no Resumo 4 |
| `calc3-notion-parametrizacao` | corrigida | t isolado com sinal trocado; "velocidade = x′ em t = 0" e "m = 0 → altura máxima" com o alcance corrigido |
| `calc3-notion-curvatura-tnb` | corrigida | κ dividia por um vetor; faltava o módulo na curvatura plana; "T = ‖T′‖N" deveria ser T′ |
| `calc3-notion-funcoes-varias-variaveis`, `calc3-notion-limite-criterio-caminhos` | validada | — |

Notas da equipe, `candidato` (fora da busca até a revisão humana): `calc3-nota-curvatura-exemplo` (κ(0) = 2 para (t, t², t³)), `calc3-nota-gradiente-derivada-direcional` (D_u f = 16/5, taxa máxima √17), `calc3-nota-limite-xy-sobre-x2-y2` (não existe: m/(1+m²)), `calc3-nota-plano-tres-pontos` (6x + 3y + 2z = 6), `calc3-nota-polares-tangente-area` (cardioide: área 3π/2, comprimento 8). Todas estão conferidas com SymPy. Para promover uma nota, troque `curadoria: candidato` por `aprovado` depois da revisão e rode `python -m acervo.disciplinas calc3 --embeddings`.

## 5. Critérios e matriz de curadoria

Mesma escala de SD e OAC: notas de 1 a 5 em autoridade, cobertura, profundidade, didática, aderência (à turma e à notação do Stewart), acessibilidade, reutilização (licença) e utilidade para tutoria. Em Cálculo 3, a tutoria precisa de **resoluções passo a passo conferíveis**; por isso as provas e as listas resolvidas da turma ficam acima de livros abertos com licença restritiva.

| Fonte | Notação | Aut. | Cob. | Prof. | Did. | Ader. | Acess. | Reut. | Tut. | Prioridade | Uso |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `ufal-calc3-provas-2024-1` Provas 2024.1 | Stewart | 5 | 2 | 4 | 3 | 5 | 3 | 2 | 5 | alta | acervo (parafraseadas) |
| `ufal-calc3-notion-resolucoes` Limites e parciais resolvidos | Stewart | 3 | 3 | 4 | 4 | 5 | 3 | 2 | 4 | alta | acervo |
| `ufal-calc3-notion-resumos` Resumos 1, 2, 4, 5 | Stewart | 4 | 3 | 3 | 4 | 5 | 3 | 2 | 4 | alta | acervo |
| `ufal-calc3-notion-anotacoes` Anotações dos alunos | Stewart (com erros) | 2 | 3 | 2 | 3 | 4 | 4 | 3 | 3 | média | acervo (corrigidas) |
| `ufal-calc3-topicos-ab1` Conteúdos da AB1 | — | 3 | 2 | 1 | 1 | 5 | 4 | 2 | 2 | média | citada |
| `ufal-calc3-ppc` Projeto Pedagógico | — | 4 | 3 | 1 | 1 | 3 | 4 | 3 | 1 | média | citada |
| `openstax-calculus-vol3` OpenStax Calculus Vol. 3 | ≈ Stewart | 5 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | média | citada (não ingerida) |
| `mit-ocw-1802sc` MIT 18.02SC | dw/ds\|_u | 5 | 4 | 4 | 5 | 3 | 5 | 3 | 4 | média | citada (não ingerida) |
| `mit-ocw-1802-2007` MIT 18.02 (2007) | idem | 5 | 4 | 4 | 4 | 3 | 5 | 3 | 3 | referência | catálogo |
| `libretexts-calculus-openstax` LibreTexts | ≈ Stewart | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 3 | referência | catálogo |
| `pauls-online-notes-calc3` Paul's Notes | ≈ Stewart | 4 | 4 | 3 | 5 | 4 | 5 | 1 | 4 | referência | catálogo (licença proíbe reutilizar) |
| `ufal-calc3-listas-stewart` Listas (páginas do Stewart) | Stewart | 5 | 2 | 3 | 4 | 5 | 3 | 1 | 3 | referência | só mapeamento |
| `stewart-calculo-vol2` Stewart, Clegg e Watson | referência | 5 | 5 | 5 | 5 | 5 | 2 | 1 | 5 | referência | só citação por seção |
| `geogebra-3d` GeoGebra | (x, y, z) | — | — | — | — | — | — | — | — | referência | ferramenta |
| `calcplot3d` CalcPlot3D | <a, b, c> | — | — | — | — | — | — | — | — | referência | ferramenta |
| `apex-calculus` APEX Calculus | não conferida | — | — | — | — | — | — | — | — | referência | candidato (licença não conferida) |
| `active-calculus-multivariable` Active Calculus Multivariable | não conferida | — | — | — | — | — | — | — | — | referência | candidato (licença não conferida) |

Licenças conferidas: OpenStax e MIT OCW são CC BY-NC-SA 4.0, e o OpenStax ainda declara que o conteúdo não pode ser usado para treinar modelos de linguagem. Por isso nenhum dos dois foi ingerido; ficam como leitura indicada. Paul's Notes proíbe incorporar o conteúdo. GeoGebra exige atribuição e uso não comercial. CalcPlot3D não mostra licença. APEX e Active Calculus não tiveram autoria nem licença confirmadas.

## 6. Validação

O que foi testado e o que falta está no relatório do PR e em `docs/DISCIPLINAS.md` (seção "Cálculo 3"). Resumo:

- **Busca**: as perguntas de exemplo em LaTeX e em texto simples foram testadas com a busca híbrida real (`bge-m3`, corte 0,45, penalidade de hub). Notação matemática exigiu uma mudança pequena e genérica no tokenizador (seção 7).
- **Contas**: todas as resoluções e notas estão conferidas com SymPy em `tests_acervo/test_disciplina_calc3.py`.
- **Fórmulas**: os blocos usam `$…$` e `$$…$$`, os delimitadores que o `frontend/render.js` já entrega ao KaTeX; `\operatorname{sen}` é usado para o seno em português.
- **Respostas com o modelo real** (02/11/2026), pelo mesmo caminho do site (`rag.recuperar` → `prompts.sistema_tutor` → `LLM.complete`), só com os modelos Gemini da corrida; os primeiros da lista deram 429 e a corrida passou para os seguintes:

| Pergunta | Modelo | Fontes | Resultado |
|---|---|---|---|
| Curvatura de (t, t², t³) em t = 0 | gemini-3.6-flash | anotações de curvatura | Correta: κ(0) = 2, produto vetorial ⟨0, 0, 2⟩, verificação pela parábola |
| Derivada direcional de x²y em (1, 2) na direção (3, 4) | gemini-3.1-flash-lite | nenhuma | Correta: normalizou, ∇f = ⟨4, 1⟩, 16/5; disse que não havia trecho do material |
| Limite de xy/(x² + y²) | gemini-3.1-flash-lite | AB2 Q1, anotações, listas | Correta: não existe (0 e 1/2), e distinguiu da AB2 Q1 |
| Plano por (1,0,0), (0,2,0), (0,0,3) | gemini-3.1-flash-lite | nenhuma | Correta: n = ⟨6, 3, 2⟩, 6x + 3y + 2z = 6, conferiu os três pontos |
| Tangente horizontal da cardioide | gemini-3.1-flash-lite | AB1 Q3 | Correta: (0, 2) e (±√3/4, −1/4), cúspide em 3π/2. **Não avisou** que a resolução da prova está pendente de confirmação do professor |

  Pendência: o aviso de "pendente de confirmação" chega ao prompt, mas o modelo nem sempre o repete. Rever o `rigor.md` ou a instrução comum antes de sair de "em validação".
- **Manim**: não há modelos de animação para Cálculo 3 (curvas, superfícies, gradiente). Lacuna registrada; nenhum modelo novo foi criado.

## 7. Notação matemática na busca

O tokenizador (`acervo/retrieval.tokens`) só guarda palavras com duas letras ou mais. `x²y` já virava `x2y`, mas `x^2y` em LaTeX virava `x` e `2y`, e `\langle`, `\mathbf`, `\frac` viravam palavras que casavam blocos de outro assunto. Duas regras genéricas resolvem isso: `x^2` e `x^{2}` viram `x2`, como `x²`, e comandos de diagramação do LaTeX são ignorados (`\lim`, `\nabla` e `\kappa` continuam contando). A bateria `eval/relevancia.py` de PAA e SD deu o mesmo resultado antes e depois (52/52, saída idêntica), e o ranking léxico de PAA (`tests_acervo/ranking-paa-lexico.json`) não mudou.

Limitação conhecida: `∇f`, `∂f/∂x` e `r'(t)` continuam sem token próprio. A busca depende das palavras ("gradiente", "derivada parcial") que os blocos e as perguntas costumam trazer.
