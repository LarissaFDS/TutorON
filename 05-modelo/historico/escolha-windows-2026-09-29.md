# Escolha dos modelos — execução local em 29/09/2026

Hardware medido: 17.014.046.720 bytes de RAM física (aproximadamente 16 GiB); NVIDIA GeForce RTX 4060, 8.188 MiB de VRAM conforme `nvidia-smi`. O campo AdapterRAM do Windows reportou aproximadamente 4 GB; usamos a medição do driver para a decisão.

Ollama portátil oficial 0.34.4 instalado em `.tools/ollama`, com hash SHA-256 do download verificado. Escuta somente em `127.0.0.1:11434`. Modelos em `.tools/models`; nenhum serviço de sistema foi instalado.

## Texto

Padrão: `qwen2.5:7b`, 8.192 tokens de contexto. Mantém a continuidade com a PoC da equipe; o catálogo oficial informa pesos de aproximadamente 4,7 GB e janela máxima de 32K. Não usamos a janela máxima nesta GPU. O alias `tutoron-paa` foi criado com o Modelfile desta pasta. As avaliações usam o modelo base com prompts explícitos idênticos entre execuções, para que a condição genérica não herde o prompt do tutor.

Comparamos rapidamente `qwen2.5:7b` e `gemma3:4b` na mesma pergunta de PAA. Os textos integrais e tempos estão em `comparacao.json`. Ambos responderam em aproximadamente 10 segundos, mas **ambos erraram**: Qwen confundiu NP com número de chamadas e não calculou corretamente a quantidade de asteriscos; Gemma ignorou a segunda chamada recursiva e calculou 6 em vez de 11. Essa pequena prova não demonstra superioridade de nenhum dos dois. Mantemos Qwen como baseline operacional, não como modelo pedagogicamente aprovado.

## OCR e visão

Qwen2.5-VL 3B foi baixado e testado em fotos e PDFs. Uma foto manuscrita retornou transcrição, mas várias páginas renderizadas falharam com `prediction aborted, token repeat limit reached` nesta combinação de runtime/modelo. Gemma3 4B conseguiu responder a uma página, porém a conferência visual revelou que reescreveu um algoritmo C++ em vez de transcrevê-lo fielmente.

Por isso, interpretações de visão são **candidatos incertos separados**, nunca substituição automática de fonte. A transcrição principal usa texto direto e OCR dos recortes na ordem da página. Tesseract `por` é usado se estiver instalado; neste computador o fallback executado foi RapidOCR ONNX local. Seu modelo padrão privilegia caracteres latinos/inglês e não garante todos os acentos portugueses; código, índices e fórmulas permanecem parciais. Não foi possível certificar transcrição fiel de todos os manuscritos.

## Embeddings

`bge-m3`, aproximadamente 1,2 GB, multilíngue. Combina embeddings densos com busca lexical implementada no projeto. O modelo é descarregado após cada lote para liberar VRAM ao gerador. Falhas de embeddings deixam o modo lexical explicitamente registrado.

## Referências verificadas

- [Ollama no Windows e distribuição portátil](https://docs.ollama.com/windows)
- [Qwen2.5](https://registry.ollama.com/library/qwen2.5)
- [BGE-M3](https://ollama.com/library/bge-m3)
- [API de embeddings](https://docs.ollama.com/api/embed)
- [RapidOCR](https://github.com/RapidAI/RapidOCR)

Não houve fine-tuning, download de modelos de origem desconhecida ou chamada real ao Gemini. A revisão do professor permanece necessária para as respostas e para os critérios de avaliação.
