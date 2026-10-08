# TutorON local — execução e procedência

Operação: [PASSO_A_PASSO.md](../PASSO_A_PASSO.md). Evidências e limitações: [RELATORIO_VALIDACAO.md](../RELATORIO_VALIDACAO.md).

## Linux e Windows

Atalhos `.sh` e `.bat` executam ações equivalentes via `scripts/tutoron.sh` e `scripts/tutoron.ps1`. Linux foi executado; os wrappers Windows foram revisados, mas não executados em Windows nesta rodada. Pastas: `.venv-acervo`, `.tools/ollama`, `.tools/models`.

Linux exige Python 3.10+ com venv (recomendado 3.12) ou uv, curl e zstd. Ollama portátil v0.34.4 é baixado da release oficial e verificado por SHA-256. `instalar_ocr.sh` prepara Tesseract português/inglês portátil no Ubuntu 24.04 amd64. Em Windows, instale Tesseract com esses idiomas; sem ele há fallback RapidOCR, registrado na extração.

| Atalho (use .sh ou .bat) | Ação |
|---|---|
| preparar_modelos | Ollama, base/visão/embeddings e alias TutorON |
| iniciar_validacao | Interface A/B em http://127.0.0.1:8765 |
| atualizar_acervo | Inventário, snapshots, extração, regras e busca lexical |
| extrair_com_visao | Candidatos de visão incertos e índice híbrido |
| avaliar_modelos | Regras/revisões, embeddings, quatro condições e pares offline |
| testar_acervo | Testes isolados, sem votos reais |
| resumo_validacao | Resumo dos votos humanos existentes |
| preparar_treino | Dados de agente, manifesto e dry-run |
| treinar_lora | Receita CUDA para outra máquina |

Caminhos do inventário têm representação Windows estável como chave; o acesso aos arquivos normaliza separadores. Assim os IDs se mantêm entre sistemas. Saídas textuais usam LF.

## Comandos Python

Linux: `.venv-acervo/bin/python`; Windows: `.venv-acervo/Scripts/python.exe`.

```bash
python -m acervo inventario
python -m acervo extrair --reprocessar
python -m acervo organizar
python -m acervo triar
python -m acervo indexar --embeddings
python -m acervo.audit
python -m acervo buscar --pergunta 'Quantos asteriscos ASTERISCO imprime?'
python -m acervo avaliar --gerar
python -m acervo.benchmark_report
python -m acervo offline
python -m acervo servir
python -m acervo resumo
```

Prepare modelos antes de embeddings/geração. `--questoes Q1,Q2` limita a amostra e substitui o agregado: execute sem filtro depois para restaurá-lo via cache. `--reprocessar` refaz OCR preservando snapshots. `--pasta caminho` inclui uma pasta extra no inventário/pipeline; informe-a novamente ou use `materiais/Disponiveis`.

## Arquivos e confiança

- `00-originais/ingestao/<sha256>/`: snapshots imutáveis locais, fora do Git.
- `03-triagem/inventario.csv`: fontes atuais e referências.
- `01-extraido/<id>.json/.md`: fonte, página, método, qualidade e texto bruto. `figuras/` contém páginas/recortes locais.
- `02-acervo/itens.json`: manifesto atual; arquivos históricos na pasta não entram na busca por simples presença.
- `03-triagem/correcoes.json` e `correcoes/`: versões por agente vinculadas ao SHA-256 original.
- `03-triagem/auditoria.json` e `AUDITORIA.md`: conferência por arquivo/página/bloco. Integridade não certifica qualidade pedagógica.
- `03-triagem/verificacoes-curadoria.json`: propriedades verificadas em casos finitos por código independente.
- `03-triagem/revisoes.json`: pareceres humanos explícitos; hashes antigos não aprovam textos novos.
- `04-rag/indice.json`: recuperação lexical + BGE-M3, exigindo confiança média/alta e filtrando ilegibilidade/assunto/cortes pendentes.
- `05-modelo/treino/`: 26 exemplos de agente para treino e seis para validação, benchmark reservado.
- `06-avaliacao/`: questões, quatro condições, respostas reais, hashes, latências e revisão técnica.
- `07-validacao-alunos/pares.json`: pares reais atuais; votos/sessões são locais e ignorados pelo Git.

OCR foi testado em PNG, JPEG, WebP, BMP, GIF e TIFF, inclusive TIFF com múltiplos frames. Manuscritos, fórmulas e diagramas ainda exigem conferência. Visão é interpretação incerta separada e não substitui automaticamente a transcrição. Código extraído nunca é executado.

## Perfil e privacidade

`.tools/runtime.json` guarda o perfil. Variáveis explícitas o substituem: `TUTORON_BASE_MODEL`, `TUTORON_MODEL`, `TUTORON_NUM_CTX`, `TUTORON_SEED`, `TUTORON_TIMEOUT`. Padrão: Qwen2.5 3B, 4096 tokens, seed 42 e timeout 900 s. `TUTORON_EMBED_MODEL` e `OLLAMA_URL` configuram embeddings/endereço. Ao trocar a base preservando aliases separados, defina ambos os nomes antes de preparar modelos.

Ollama escuta 127.0.0.1:11434 e validação 127.0.0.1:8765. Pares offline dispensam inferência; perguntas livres exigem Ollama. Mantenha notebook e servidor ativos.

Backend usa Ollama por padrão. Gemini exige `TUTORON_AI_PROVIDER=gemini` e credencial. No acervo, `--provedor auto` com `GEMINI_API_KEY` pode enviar trechos ao Gemini e faz fallback local. Nenhuma geração externa foi feita nesta rodada; Gemini foi testado com mocks.

A/B oculta condições, mas estilo/citações podem sugeri-las. O CSV não registra nome, matrícula ou IP; comentários devem evitar identificação. Preferência não demonstra ganho de aprendizagem. Somente avaliações humanas reais alimentam os votos.

Aprovações em `03-triagem/revisoes.json` exigem `sha256` (texto atual) e `sha256_fonte` (arquivo original), além de revisor, confiabilidade e justificativa. Mudanças no arquivo invalidam o parecer mesmo com OCR idêntico. Votos preservam o hash e snapshot de cada par; resumos não misturam versões.
