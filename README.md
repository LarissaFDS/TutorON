# TutorON

Monitoria de **Projeto e Análise de Algoritmos (PAA)** da UFAL com IA. O aluno pergunta, o TutorON busca no material da disciplina (provas, listas, resoluções e o livro-texto) e responde passo a passo, com as fórmulas formatadas.

O site tem dois modos:

- **Tirar dúvida** — modo normal: pergunta e resposta, com as fontes consultadas e um botão para marcar "tem erro de conta".
- **Avaliar respostas (validação)** — teste cego A/B: a mesma pergunta é respondida pelo TutorON (RAG + instruções) e por um modelo genérico (o mesmo modelo, sem material e sem instruções). O aluno dá notas sem saber qual é qual. Tudo chega como JSON nesta máquina, com a identificação de cada lado.

## Como usar (Windows)

Três atalhos na raiz. Nada mais é necessário no dia a dia.

| Atalho | O que faz |
|---|---|
| **`1-Iniciar-Servidor.bat`** | Liga tudo: modelo local na GPU, site e endereço público `https://….trycloudflare.com` para qualquer pessoa acessar. Instala o que faltar na primeira vez. Deixe a janela aberta. |
| **`2-Validacao.bat`** | Abre o modo validação e o painel de resultados, e copia o link da validação para enviar aos alunos. |
| **`3-Treinar.bat`** | Treina o modelo local na GPU (QLoRA), importa no Ollama como `tutoron-paa-ft` e gera um relatório comparando com o atual. Não troca o modelo sozinho. |

Antes da primeira vez, crie o arquivo `.env` (copie de [`.env.example`](.env.example)) e preencha `GEMINI_API_KEY` e, para incluir o livro-texto na busca, `SUPABASE_URL` e `SUPABASE_KEY`. O `.env` não vai para o Git.

### O que fica nesta máquina

- `dados/perguntas.jsonl` — perguntas do modo Tutor, resposta, modelo usado e fontes.
- `dados/feedback.jsonl` — "ajudou / não ajudou / tem erro de conta".
- `dados/validacao/avaliacoes.jsonl` — cada avaliação A/B completa: pergunta, as duas respostas, notas, preferência e **qual lado era o TutorON**.
- `http://127.0.0.1:8000/resultados` — resumo das avaliações. Só abre nesta máquina; pelo endereço público responde 404.

Nenhum IP, nome ou matrícula é gravado.

## Como a resposta é escolhida

1. A pergunta vira um embedding `bge-m3` (local, na CPU) e busca em duas fontes: o acervo curado de PAA ([`04-rag/`](04-rag/)) e o livro-texto no Supabase.
2. O prompt do tutor ([`backend/prompts.py`](backend/prompts.py)) exige contas passo a passo, verificação no final, citação das fontes e Markdown com LaTeX.
3. **Corrida entre modelos** ([`backend/llm.py`](backend/llm.py)): o primeiro Gemini da lista começa na hora; se não começar a responder em 6 s, ou der erro (503, 429…), o próximo começa também. O primeiro que responder vence e os outros são cancelados. Um modelo que falhou fica alguns segundos em pausa, então as perguntas seguintes nem tentam ele.
4. Se nenhum Gemini responder em 20 s, entra o **TutorON local** (`tutoron-paa`, Qwen3 8B com raciocínio, na GPU desta máquina).

A ordem dos modelos, os tempos e o modelo local ficam no `.env` (veja os comentários em `.env.example`).

## Estrutura

```
1-Iniciar-Servidor.bat  2-Validacao.bat  3-Treinar.bat   atalhos
backend/          servidor (FastAPI), cascata de modelos, RAG, registro dos dados, site (backend/web)
scripts/          tutoron.ps1 (motor dos atalhos), treinar.py, avaliar_modelos.py
acervo/           pipeline de OCR, curadoria e índice do material de PAA
00-…06-           dados do pipeline: originais, extração, acervo, triagem, índice RAG, modelo, avaliação
design/           design system (tokens e componentes CSS) — regras em docs/DESIGN.md
frontend/         cliente de terminal (CLI) que usa a mesma API
docs/             documentação, schema do Supabase, relatórios da validação pré-MVP
legado/           prova de conceito antiga com Gemini (preservada)
```

## Comandos úteis

```bat
:: testes (backend + acervo)
powershell -ExecutionPolicy Bypass -File scripts\tutoron.ps1 -Acao Testar

:: desligar servidor e túnel que ficaram abertos
powershell -ExecutionPolicy Bypass -File scripts\tutoron.ps1 -Acao Parar

:: enviar mais PDFs de PAA para o Supabase (livro-texto na RAG); repetir não duplica
.venv\Scripts\python -m backend.ingest "C:\caminho\para\pdfs"

:: refazer OCR, curadoria e índice do acervo depois de adicionar material em materiais\
powershell -ExecutionPolicy Bypass -File scripts\tutoron.ps1 -Acao Acervo

:: comparar os modelos nas perguntas de 06-avaliacao\perguntas-mvp.json
.venv\Scripts\python scripts\avaliar_modelos.py
```

## Treinamento

Veja [`05-modelo/COMO_TREINAR.md`](05-modelo/COMO_TREINAR.md). Resumo: o `3-Treinar.bat` usa as soluções curadas do acervo, treina um adapter LoRA sobre o Qwen3-8B na RTX 4060, mescla, importa no Ollama e avalia. Para usar o modelo treinado, coloque `TUTORON_MODELO_LOCAL=tutoron-paa-ft` no `.env` e reinicie o servidor.

## Documentação

- [Relatório do MVP](docs/RELATORIO_MVP.md): o que foi implementado, testes e avaliação dos modelos.
- [Design system](docs/DESIGN.md) · [Schema do Supabase](docs/schema.sql)
- [Validação pré-MVP](docs/validacao-pre-mvp/) (OCR, curadoria, comparação local, relatórios anteriores)
- Issues: [#3 backend](docs/issue-3-backend-ai-service.md) · [#5 CLI](docs/issue-5-frontend-cli.md)
