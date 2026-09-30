# TutorON local — guia de execução

A PoC existente continua em `materiais/`, `questoes.json`, `prompts.py` e `run_demo.py`. Não foi movida para `tutoron-poc-rag/`, pois os caminhos atuais já são usados pela equipe. O backend existente continua independente. O novo módulo `acervo` não exige Supabase nem credenciais.

## Uso no Windows

| Arquivo | O que executa |
|---|---|
| `iniciar_validacao.bat` | Abre a comparação A/B em `http://127.0.0.1:8765`. Usa respostas reais pré-geradas. |
| `atualizar_acervo.bat` | Inventário, cópia, extração direta, organização, regras de triagem, busca lexical e avaliação de recuperação. |
| `preparar_modelos.bat` | Prepara o Ollama portátil e baixa modelos; cria `tutoron-paa`. Precisa de internet para o download inicial. |
| `extrair_com_visao.bat` | Processa páginas/imagens com visão local e atualiza busca híbrida. Pode demorar. |
| `avaliar_modelos.bat` | Faz triagem com IA, embeddings e gera respostas nas três condições; atualiza os pares offline. |
| `resumo_validacao.bat` | Mostra preferências e médias por questão/condição. |
| `testar_acervo.bat` | Executa os testes isolados, sem gerar votos na base real. |

Os atalhos chamam `scripts/tutoron.ps1`. Não precisam de terminal elevado. Dependências ficam em `.venv-acervo`, modelos em `.tools/models`, binários em `.tools/ollama`. Se Python não existir, instale Python 3.12+ ou uv. A preparação verifica erros e interrompe a sequência quando um comando falha.

O servidor de validação atende somente neste computador. Mantenha a janela do servidor aberta durante a sessão. Para encerrar, use Ctrl+C. Se a porta já estiver ocupada pelo TutorON, abra o endereço existente. Perguntas livres exigem Ollama em execução; questões pré-geradas funcionam sem internet e sem modelo carregado.

## Comandos equivalentes

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/tutoron.ps1 -Acao Preparar
.venv-acervo\Scripts\python.exe -m acervo inventario
.venv-acervo\Scripts\python.exe -m acervo extrair
.venv-acervo\Scripts\python.exe -m acervo extrair --visao
.venv-acervo\Scripts\python.exe -m acervo organizar
.venv-acervo\Scripts\python.exe -m acervo triar --ia
.venv-acervo\Scripts\python.exe -m acervo indexar --embeddings
.venv-acervo\Scripts\python.exe -m acervo buscar --pergunta "Quantos asteriscos ASTERISCO imprime?"
.venv-acervo\Scripts\python.exe -m acervo avaliar --gerar
.venv-acervo\Scripts\python.exe -m acervo offline
.venv-acervo\Scripts\python.exe -m acervo servir
.venv-acervo\Scripts\python.exe -m acervo resumo
```

Para uma amostra curta: `python -m acervo avaliar --gerar --questoes Q1,Q2`. Essa execução gera um relatório da amostra selecionada. Para recuperar todos os resultados, execute sem o filtro; o cache reaproveita chamadas idênticas. `--reprocessar` força nova extração, preservando cópias originais. `--pasta caminho` em `inventario`/`pipeline` permite uma pasta adicional; informe-a novamente nas próximas execuções ou coloque os arquivos em `materiais/Disponiveis`.

## Onde conferir os resultados

- `00-originais/manifesto.json`: snapshot inicial; `.env`, Git, caches e ambientes virtuais foram excluídos. Cópias novas de documentos ficam em `00-originais/ingestao/<sha256>/`, marcadas somente leitura. Arquivos alterados ganham outro hash, sem sobrescrever versões anteriores.
- `03-triagem/inventario.csv`: documentos didáticos e referências, tipo, páginas, texto extraível e assunto provável. Referências de planejamento e apresentação não entram no RAG.
- `01-extraido/<id>.md` e `.json`: extração com fonte/página/método/qualidade. Figuras raster recortadas e páginas inteiras em `figuras`; desenhos vetoriais ficam preservados na página para revisão.
- `02-acervo/indice.csv` e `itens.json`: manifesto **atual** dos blocos. Arquivos de versões anteriores são preservados no disco e não entram na busca por simples presença na pasta.
- `03-triagem/relatorio.md`: suspeitas e contagens. `pacote-revisao` contém transcrição e parecer separados. `pareceres.json` lista a rodada atual.
- `04-rag/indice.json`: chunks e embeddings. Baixa confiança, ilegíveis, assunto incerto e segmentação pendente são excluídos. Na falta de embeddings a busca degrada explicitamente para lexical.
- `06-avaliacao/questoes.json`: 12 questões, sete assuntos, perguntas de aluno, ausência de informação e material errado. `relatorio.md` e `resultados.json` registram geração real; `recuperacao.json` registra apenas busca.
- `07-validacao-alunos/pares.json`: respostas offline e sua procedência. Pares históricos do HTML são rotulados como contexto manual; não se confundem com execução da busca automática.
- `07-validacao-alunos/respostas.csv`: votos e notas, criado no primeiro voto. `sessoes.json` guarda a ordem A/B no servidor; o navegador recebe apenas textos e token aleatório. O CSV não registra nome, login, IP ou matrícula. Comentários devem evitar identificação pessoal.
- `RELATORIO_QUINTA.md`: números e pendências para o professor. `PROGRESSO.md`: etapas executadas.

## Revisão humana

Uma nota alegada no cabeçalho de uma transcrição não comprova aprovação do professor. Por isso, nenhum item vira `alta` automaticamente. Registre aprovações em `03-triagem/revisoes.json`:

```json
{
  "id-do-item": {
    "sha256": "hash exato de itens.json",
    "revisor": "identificação do revisor",
    "confiabilidade": "alta",
    "justificativa": "Fonte e resolução conferidas na página original."
  }
}
```

Execute novamente a triagem e a indexação. Uma mudança de texto invalida a aprovação antiga pelo hash. Rebaixamentos são consultados também durante a busca, mesmo se o índice ainda não foi reconstruído. Não corrija a transcrição original; produza uma nova fonte revisada separadamente.

## Modelos e privacidade

O padrão é Ollama local. O modelo usado aparece em cada resultado. Defina `TUTORON_MODEL`, `TUTORON_EMBED_MODEL` e `OLLAMA_URL` apenas se desejar substituir os padrões. O OCR impresso usa Tesseract `por` quando disponível e RapidOCR local como fallback. `--visao` produz interpretações adicionais marcadas como incertas; elas não substituem a transcrição usada pelo RAG. Veja as falhas observadas e a comparação dos modelos em `05-modelo/escolha.md`.

Gemini é opcional: forneça `GEMINI_API_KEY` no ambiente e execute `--provedor auto`. Nesse modo os trechos selecionados serão enviados ao Gemini; erros, bloqueios, limite de uso, resposta vazia ou timeout fazem fallback para Ollama. Não carregamos automaticamente o `.env` do backend. Nesta entrega, o fallback externo foi verificado por testes simulados, sem chamadas reais ao Gemini.

## Limitações

OCR e segmentação são candidatos à revisão, especialmente manuscritos e fórmulas. Os testes numéricos cobrem ASTERISCO e o incremento do custo de árvores, não todos os algoritmos. Código extraído nunca é executado. Pareceres de IA não certificam correção. Citações e estilo podem dar pistas da condição mesmo com os rótulos A/B ocultos. As notas medem preferência percebida; não demonstram ganho de aprendizagem. O dataset de fine-tuning fica vazio até haver pares explicitamente aprovados.
