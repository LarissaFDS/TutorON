# Relatório do MVP do TutorON — 12/10/2026

Este relatório cobre o que foi implementado nesta rodada, como foi testado e o que a avaliação dos modelos mostrou. As respostas completas estão em [`06-avaliacao/resultados-mvp.json`](../06-avaliacao/resultados-mvp.json) e as perguntas com as soluções de referência em [`06-avaliacao/perguntas-mvp.json`](../06-avaliacao/perguntas-mvp.json).

## 1. O que foi feito

**Trabalho do Cleverson (`feat/RAG`).** A branch trazia a RAG no Supabase (pgvector, embeddings `bge-m3` locais), a atribuição de fonte por trecho e um laço de fallback entre modelos Gemini. O Supabase tem o **livro-texto de PAA** indexado (142 páginas). Isso foi mesclado e aproveitado: a busca agora consulta o acervo curado local (provas, listas, resoluções) **e** o livro, com o mesmo embedding da pergunta. A ingestão (`backend/ingest.py`) passou a aceitar qualquer PDF ou pasta, sem duplicar documentos já enviados.

**Site único** (`backend/`), com dois modos:

- *Tirar dúvida*: resposta em streaming, fontes consultadas e botões "ajudou / não ajudou / tem erro de conta".
- *Avaliar respostas (validação)*: A/B cego ao vivo. A mesma pergunta é respondida pelo TutorON (RAG + prompt) e pelo **mesmo modelo** sem material e sem instruções; a ordem é sorteada. A avaliação completa vai para `dados/validacao/avaliacoes.jsonl`, com qual lado era o TutorON.

**Corrida de modelos.** O primeiro Gemini da lista começa na hora. Se não começar a responder em 6 s, ou se der erro, o próximo começa também; o primeiro que responder vence e os demais são cancelados. Modelos que falharam ficam em pausa por alguns segundos (429: 60 s; 404: 10 min). Sem Gemini em 20 s, entra o TutorON local.

**Modelo local trocado.** O `tutoron-paa` passou de `qwen2.5:7b` para `qwen3:8b` com raciocínio, porque o antigo errava contas graves (ver seção 3). O antigo continua instalado como `tutoron-paa-qwen25`.

**Formatação corrigida.** O site antigo mostrava o Markdown cru. Agora as respostas passam por marked + KaTeX + DOMPurify, todos servidos localmente (sem CDN). Funciona com `$…$`, `$$…$$`, `\(…\)`, `\[…\]` e com `$ x $` com espaços; código não vira fórmula e "R$ 5" não vira fórmula.

**Hospedagem no Windows.** `1-Iniciar-Servidor.bat` sobe Ollama, site e um túnel Cloudflare (endereço `https://….trycloudflare.com`, sem abrir portas no roteador), reinicia o que cair e impede a suspensão do PC enquanto a janela estiver aberta.

**Treino em um clique.** `3-Treinar.bat`: dados do acervo curado → QLoRA do Qwen3-8B na RTX 4060 → mescla → Ollama (`tutoron-paa-ft`) → relatório comparando com o atual. Resultado na seção 4.

**Limpeza.** A raiz tinha 22 scripts `.bat/.sh`; agora tem 3 atalhos e o README. A PoC antiga foi para `legado/`, os relatórios da validação pré-MVP para `docs/validacao-pre-mvp/`, e o servidor de validação antigo (porta 8765) foi removido, porque a validação agora acontece no site principal.

## 2. Testes executados

| Teste | Resultado |
|---|---|
| Testes automatizados (backend + acervo) | 43 passaram |
| Corrida de modelos com falhas simuladas (503, lento, queda no meio, nenhum disponível) | 8 cenários passaram |
| Fallback real: todos os Gemini com 503 | o TutorON local respondeu |
| Corrida real: dois modelos com 503 em menos de 1 s | o terceiro respondeu em 13 s; o mais lento foi cancelado |
| Pergunta pelo **endereço público** (streaming pela Cloudflare) | resposta completa e correta |
| Validação pelo endereço público: gerar, dar notas e enviar | registro completo em `dados/validacao/avaliacoes.jsonl` |
| `/resultados` pelo endereço público | 404 (bloqueado); na própria máquina abre normalmente |
| Renderização de fórmulas, tabelas e código, no desktop e no celular | correta |
| Limite por pessoa (perguntas e envios) | 429 após o limite |

Durante a noite de testes, o Gemini estava **muito instável**: 503 ("high demand") frequentes nos modelos 3.8, 3.7 e flash-latest. Na avaliação abaixo, 5 de 8 respostas do TutorON+Gemini vieram do `gemini-3.1-flash-lite`, o mais leve da lista, porque os outros estavam fora. A corrida de modelos foi exatamente o que manteve o site respondendo.

## 3. Avaliação dos modelos

Oito perguntas **novas**, criadas para esta avaliação (não estão no banco pré-definido), ligadas aos temas do acervo e com resposta conferida: programação dinâmica, método da iteração, contagem de laços, exponenciação rápida, seleção de intervalos, AGM com pesos transformados, primalidade e pseudo-polinomialidade, e uma armadilha clássica: $T(n)=2T(n/2)+n/\log n$, em que o Teorema Mestre **não** se aplica (a resposta é $\Theta(n\log\log n)$).

Todas as respostas foram geradas ao vivo pelos modelos e corrigidas uma a uma contra a referência. Nota: 2 = correta, 1 = parcial, 0 = errada.

| Pergunta | TutorON + Gemini | Genérico Gemini | TutorON local (qwen3 8B) | TutorON antigo (qwen2.5 7B) | Genérico local (qwen3 8B) |
|---|:-:|:-:|:-:|:-:|:-:|
| N1 Triângulo (PD) — 11 | 2 | 2 | 2 | **0** (12) | 2 |
| N2 Iteração — $n^2+n+1$ | 2 | 2 | 2 | **0** ($n^2-n+3$) | 2 |
| N3 Laços triplos — $n(n+1)(n+2)/6$ | 2 | 2 | 2 | 2 | 2 |
| N4 $a^{13}$ — 5 multiplicações | 1 (7) | 2 | 2 | **0** (13) | 2 |
| N5 Intervalos — 4 | 2 | 2 | 2 | **0** (11) | 2 |
| N6 AGM ×2 e ao quadrado | 2 | 2 | 2 | **0** | 2 |
| N7 Primalidade não é polinomial | 2 | 2 | 2 | 1 | 2 |
| N8 Mestre não se aplica — $\Theta(n\log\log n)$ | 2 | 2 | **0** ($n^2/\log n$) | **0** | 2 |
| **Total (de 16)** | **15** | **16** | **14** | **3** | **16** |
| Tempo médio | 19 s | 23 s | 57 s | 33 s | 112 s |

O que isso mostra:

1. **O modelo local antigo errava muito, e de forma grave**: 3 de 16. Errou somas simples (12 em vez de 11), escreveu uma fórmula fechada errada e "verificou" com valores errados ($T(2)=5$, o certo é 7), disse que o guloso escolhe os 11 intervalos. É o problema que vocês tinham observado. A troca para o `qwen3:8b` com raciocínio levou o TutorON local a **14 de 16**.
2. **O erro que sobrou no local é do tipo perigoso**: na N8 ele chegou ao resultado certo ($n\log\log n$) e depois o "corrigiu" para $n^2/\log n$ com Akra-Bazzi mal aplicado. Raciocinar mais não elimina esse tipo de erro.
3. **Neste conjunto, RAG + prompt não aumentou o acerto matemático.** O genérico acertou tudo, tanto no Gemini quanto no local. As perguntas são de conhecimento padrão de PAA, em que os modelos fortes já sabem a resposta. O valor do TutorON aparece em outro lugar: cita o material da disciplina, segue a notação das provas e responde mais rápido no local (57 s contra 112 s, com respostas mais curtas). Na N4, seguir o algoritmo do material (caso base $a^0$) fez o Flash-Lite contar 7 multiplicações em vez de 5; seguir o material também pode atrapalhar. **A validação A/B com alunos é o que vai dizer se o TutorON ajuda mais**; esta tabela não substitui isso.
4. **Oito perguntas são pouco.** Isto é um teste de fumaça, não um benchmark. A diferença de 1 ponto entre colunas não é significativa.

## 4. Treino

O `3-Treinar.bat` foi executado de ponta a ponta nesta máquina, pelo mesmo caminho que você vai usar: dados → QLoRA do Qwen3-8B → mescla → GGUF Q4_K_M → Ollama (`tutoron-paa-ft`) → avaliação. Treino de 30 passos em 7,8 min na RTX 4060; mescla, conversão e quantização em ~8 min; avaliação em ~15 min.

Problemas encontrados no caminho, já corrigidos no pipeline:

- O TRL 1.15 exige Triton, que não existe no Windows. O treino passou a usar o `Trainer` do `transformers` com mascaramento manual do prompt.
- O `prepare_model_for_kbit_training` convertia as embeddings para float32 e lotava os 8 GB. Removido; o modelo carregado ocupa 5,8 GB.
- O Ollama do Windows não importa safetensors (precisa do runtime MLX, que só existe no Mac). A importação passou a converter para GGUF com o conversor oficial do llama.cpp e quantizar com o `llama-quantize` que vem com o Ollama.
- **A primeira versão treinada ficou quebrada**: parou de raciocinar e entrava em loop repetindo a mesma frase. Duas causas: o template do Qwen3 coloca um bloco de raciocínio vazio antes da resposta, e o modelo aprendeu a gerá-lo; e 60 passos sobre 26 exemplos (~9 épocas) sobreajustaram. Agora o bloco vazio fica fora da perda e o padrão é 30 passos com taxa de aprendizado menor. A versão nova raciocina normalmente e não entra em loop.

Resultado (relatório completo em [`05-modelo/treino/avaliacao-20261012-0154.md`](../05-modelo/treino/avaliacao-20261012-0154.md)):

| Modelo | Nota média do juiz (0–2) | Casos julgados |
|---|---:|---:|
| `tutoron-paa` (atual) | 1,43 | 7 de 9 |
| `tutoron-paa-ft` (treinado) | 1,62 | 8 de 9 |

A diferença é pequena e está dentro do ruído: são 9 perguntas, dois casos ficaram sem juiz (cota do Gemini esgotada) e os dois modelos erram em pontos diferentes (o treinado escreveu `dp[i][3]` no lugar de `dp[i][j]` numa recorrência; o atual confundiu cobertura de vértices com o teorema de König). **O modelo em uso continua sendo o `tutoron-paa`.** O treino serve hoje para provar que o processo funciona de ponta a ponta nesta máquina; ganho real depende de mais dados revisados (ver seção 6).

## 5. Como usar agora

1. Dois cliques em `1-Iniciar-Servidor.bat`. A janela mostra o endereço público; deixe-a aberta.
2. Mande aos alunos o endereço com `?modo=validacao` no fim (o `2-Validacao.bat` copia esse link).
3. Acompanhe em `http://127.0.0.1:8000/resultados` e nos arquivos de `dados/`.

## 6. Limites e próximos passos

- **O endereço público muda** a cada vez que o servidor é reiniciado (túnel rápido da Cloudflare, sem conta). Para um endereço fixo, é preciso uma conta Cloudflare com domínio; o `.env.example` explica onde colocar o token.
- O PC precisa ficar ligado e conectado. Enquanto a janela do servidor estiver aberta, a suspensão automática fica bloqueada.
- **Cota do Gemini:** no fim dos testes desta noite a chave começou a receber 429 (cota esgotada) em vários modelos. Com alunos usando, isso vai acontecer mais cedo; o site continua respondendo pelo modelo local, só que mais devagar. Se o uso crescer, vale ativar o faturamento na chave ou usar mais de uma chave.
- A instabilidade do serviço do Gemini também limita quantas pessoas podem usar ao mesmo tempo. Quando o Gemini cai, cada resposta local leva cerca de 1 minuto e a GPU atende uma pessoa por vez.
- Não enviei novos PDFs ao Supabase, porque isso altera o banco compartilhado do time. O comando está no README (`python -m backend.ingest <pasta>`).
- Para reduzir os erros de matemática de verdade, o que mais ajuda é **ter mais soluções corretas revisadas** para treinar e usar as avaliações com "erro de matemática" marcadas pelos alunos para achar onde o modelo erra.
