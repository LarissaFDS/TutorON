# TutorON — validação antes do MVP

O estágio atual é validar OCR, curadoria e RAG local antes de construir e publicar o MVP. A hipótese é que dados acadêmicos melhores ajudem o mesmo modelo a responder melhor. Resultados negativos também devem ser registrados.

## Abrir a validação

No Ubuntu, use `bash instalar_atalho.sh` uma vez para criar o atalho **TutorON — Validação** no menu de aplicativos e na área de trabalho. O duplo clique em `.sh` pode abrir o editor em vez de executar. Se os serviços já estiverem ativos, abra http://127.0.0.1:8765 diretamente.

Linux/Ubuntu:

```bash
./preparar_modelos.sh
./iniciar_validacao.sh
```

Windows: execute `preparar_modelos.bat` e depois `iniciar_validacao.bat`.

A página fica em http://127.0.0.1:8765. Os pares offline abrem imediatamente; perguntas ao vivo usam o Ollama local e podem levar minutos nesta CPU. As notas A/B são sorteadas e os votos ficam somente no notebook.

## Acervo e OCR

São 57 arquivos de entrada, incluindo 16 PDFs e 30 fotos WebP, extraídos em 161 páginas/blocos. [Auditoria por arquivo](03-triagem/AUDITORIA.md) e [manifesto detalhado](03-triagem/auditoria.json) registram hashes, páginas, correções e exclusões. Há 53 blocos com versões corrigidas por agente; a recuperação automática usa somente confiança média/alta, atualmente esses 53 blocos; isso não representa aprovação do professor.

A extração usa texto nativo e Tesseract português/inglês, com RapidOCR como alternativa. PNG, JPEG, WebP, BMP, GIF e TIFF são aceitos; TIFF/GIF multipágina preservam os frames. PDF digitalizado passa pelo OCR. Handwriting, fórmulas e diagramas continuam sujeitos a falhas; candidatos de visão nunca substituem automaticamente a fonte. Não há promessa de ler qualquer imagem com fidelidade.

```bash
./instalar_ocr.sh              # Ubuntu 24.04 amd64: Tesseract portátil
./atualizar_acervo.sh           # inventário, extração, organização e busca
./extrair_com_visao.sh          # candidatos visuais: lento na CPU
./testar_acervo.sh
```

Os originais são preservados por hash. [Correções](03-triagem/correcoes.json) vinculam texto derivado ao hash exato do bloco original. Uma fonte alterada invalida sua correção. Os arquivos de setembro permanecem históricos e o índice só usa o inventário atual.

## Comparação dos modelos

```bash
./avaliar_modelos.sh
./resumo_validacao.sh
```

Quatro condições: genérico `qwen2.5:3b`; base com instruções TutorON sem contexto; `tutoron-paa` com contexto manual; `tutoron-paa` com RAG automático. Os pesos são [idênticos](05-modelo/pesos-validacao.json), com seed 42, temperatura 0,2, contexto de 4096 tokens e mesma orientação de até 220 palavras. O controle distingue o efeito das instruções do efeito dos dados.

[Comparação atual](06-avaliacao/COMPARACAO_ATUAL.md), [respostas e fontes](06-avaliacao/resultados.json), [relatório de execução](RELATORIO_VALIDACAO.md). Cobertura lexical de checklist não equivale à acurácia; revisão técnica e votos humanos são evidências separadas. Não se deve concluir superioridade antes de analisar os erros.

## Treinamento e hardware

Este Ubuntu tem Ryzen 7 3700U, aproximadamente 10 GiB de RAM e nenhuma GPU NVIDIA detectada. Inferência quantizada de 3B funciona na CPU; o perfil QLoRA preparado requer outra máquina com GPU CUDA. [Hardware medido](05-modelo/ambiente.json).

```bash
./preparar_treino.sh           # dados de agente, famílias separadas, dry-run
./treinar_lora.sh --steps 30   # executar na máquina com GPU, não neste notebook
```

No Windows, use os equivalentes `.bat`; WSL2 também pode usar os scripts Linux. [Guia completo](05-modelo/COMO_TREINAR.md). O dataset é pequeno e rotulado como revisão por agente; famílias do benchmark são excluídas do treino. Não houve ajuste de pesos nesta rodada. Criar o modelo Ollama e fornecer contexto por RAG não é fine-tuning.

## Estrutura

- `materiais/`: arquivos-fonte e transcrições anteriores.
- `00-originais/`, `01-extraido/`: snapshots e OCR; imagens de conferência são locais.
- `02-acervo/`, `03-triagem/`: blocos, alertas e correções derivadas.
- `04-rag/`: recuperação lexical + embeddings BGE-M3.
- `05-modelo/`: modelos, hardware e preparo do treinamento.
- `06-avaliacao/`, `07-validacao-alunos/`: respostas e avaliação A/B.
- `acervo/`: pipeline de validação local.
- `backend/`: API FastAPI, Ollama local por padrão; Gemini opcional explícito.

No Ubuntu, `./scripts/instalar_servicos.sh` instala serviços da sua sessão de usuário; `systemctl --user start tutoron-ollama tutoron-validacao` inicia ambos após encerrar instâncias manuais. Eles reiniciam em falhas e no login; logout e suspensão podem encerrar/interromper a disponibilidade.

A API pode ser aberta com `.venv/bin/python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000` após instalar `backend/requirements.txt`. A interface A/B de validação é a de 8765. Não existe implantação pública nesta fase. Para manter o servidor local disponível, mantenha o notebook ligado e sem suspensão.

A [PoC histórica com Gemini](docs/POC_HISTORICA.md) foi preservada. Seus resultados e o hardware Windows antigo não são a avaliação Linux atual.

Aprovações em `03-triagem/revisoes.json` exigem `sha256` (texto atual) e `sha256_fonte` (arquivo original), além de revisor, confiabilidade e justificativa. Mudanças no arquivo invalidam o parecer mesmo com OCR idêntico. Votos preservam o hash e snapshot de cada par; resumos não misturam versões.
