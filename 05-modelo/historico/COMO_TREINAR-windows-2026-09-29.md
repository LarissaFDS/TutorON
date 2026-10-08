# Fine-tuning futuro — não executado nesta entrega

Primeiro valide a recuperação e a curadoria com o professor. Fine-tuning não substitui o acervo atualizado nem garante respostas corretas.

## Preparar dados aprovados

1. Confirme cada fonte na página original. Em `03-triagem/revisoes.json`, registre o ID, SHA-256 atual, revisor, justificativa e confiabilidade `alta`.
2. Em `05-modelo/pares-aprovados.json`, registre objetos com `fonte_id`, `sha256`, `revisor`, `pergunta` e `resposta_ideal`. A resposta ideal deve ser revisada; não copie automaticamente uma resolução de aluno.
3. Execute `.venv-acervo\Scripts\python.exe -m acervo triar` e `.venv-acervo\Scripts\python.exe -m acervo relatorio`. O arquivo `dataset-finetuning.jsonl` recebe somente pares aprovados cujo hash ainda coincide com a fonte de alta confiança. Um dataset vazio é intencional enquanto não houver aprovação.
4. Separe treino/validação/teste por famílias de exercícios e semestres, evitando variantes da mesma questão nos dois lados. Preserve um conjunto de teste que nunca entre no treino.

## Treinar depois

Use um ambiente separado (preferencialmente Linux/WSL2), com Transformers, PEFT e TRL ou Unsloth. Faça SFT com LoRA/QLoRA, modelo base e template de conversa explicitamente fixados. Registre sementes, versões, dataset, métricas e licenças. Não execute pseudocódigo gerado sem revisão.

Esta máquina tem aproximadamente 16 GB de RAM e RTX 4060 com 8 GB de VRAM. A inferência quantizada cabe; treinar um 7B depende de contexto, batch, quantização e offload, e pode exceder a memória. Comece com um modelo menor ou use uma GPU com mais memória. Não há promessa de que QLoRA de 7B caiba aqui com a configuração desejada.

Avalie antes/depois no conjunto separado: correção, citações, abstenção, reprodução de erros de aluno e aderência aos critérios. Use avaliação humana, não apenas regex.

## Importar no Ollama

A compatibilidade de adapters varia por arquitetura e versão. Confira a [documentação oficial de importação](https://docs.ollama.com/import) antes de treinar. Para um adapter suportado, use um Modelfile com o mesmo modelo base e `ADAPTER ./caminho-do-adapter`, depois `ollama create tutoron-paa-lora -f Modelfile`. Para outros casos, mescle o adapter com o modelo base usando ferramentas compatíveis, converta para GGUF, valide a conversão e importe com `FROM ./modelo.gguf`.

Não reutilize um adapter sobre um modelo base diferente. Mantenha o modelo original disponível para comparação e reversão.
