# Preparar e treinar TutorON — Linux e Windows

## Estado desta máquina

Ubuntu 24.04, Ryzen 7 3700U, aproximadamente 10 GiB de RAM, sem GPU NVIDIA detectada. Ollama executa inferência quantizada na CPU. Nenhum peso foi treinado nesta rodada. O perfil QLoRA fornecido exige GPU CUDA; use outra máquina, Linux nativo, Windows com CUDA ou WSL2 com suporte à GPU. Um notebook somente com CPU não é um ambiente prático para o perfil 3B proposto.

Os arquivos do treino são pequenos e podem ser copiados com o repositório. Modelos e ambientes em `.tools/` e `.venv-treino/` não vão ao GitHub.

## Dados preparados

```bash
./preparar_treino.sh
```

No Windows, execute `preparar_treino.bat`. O dry-run verifica hashes, presença de dados e separação de famílias. Os arquivos `treino/treino.jsonl`, `treino/validacao.jsonl` e `treino/manifesto.json` registram fonte, hash, modelo base, revisão exata e famílias reservadas.

São dados **silver**, corrigidos por agente; não estão aprovados por professor. O conjunto é pequeno, adequado a verificar a engenharia do treino, sem sustentar uma promessa de melhoria pedagógica. As questões e conceitos reservados do benchmark não entram no treino. A RAG pode consultar o material no protocolo aberto; isso é diferente de vazar questões para fine-tuning.

O exportador antigo de alta confiança (`dataset-finetuning.jsonl`) continua exigindo aprovações verificáveis e pode estar vazio. Não renomeie revisão por agente como revisão humana.

## Executar na máquina com GPU

Instale Python 3.12, driver NVIDIA/CUDA compatível e copie o repositório. Comece com GPU de pelo menos 12–16 GB como margem prática; o consumo real depende do contexto e do backend e precisa ser medido. O perfil usa Qwen2.5 3B em NF4, LoRA rank 8, contexto 1024, batch 1 e acumulação 4.

Linux:

```bash
./treinar_lora.sh --steps 30
```

Windows:

```bat
treinar_lora.bat --steps 30
```

A instalação usa `treino/requirements.txt` com versões fixadas. A base Hugging Face também tem revisão fixada em `treino/manifesto.json`. O treino não envia dados a um serviço de geração: baixa os pesos e treina na máquina em que você executa o script. Resultados, versões efetivas e adapter ficam em `.tools/treino/`. O script interrompe quando não há CUDA, os hashes mudam, um split fica vazio ou há sobreposição de famílias.

A instalação GPU e o treinamento real **não foram executados nem validados neste notebook**. O preparo dos dados, a sintaxe e o dry-run foram verificados. Consulte os requisitos da [quantização bitsandbytes](https://huggingface.co/docs/transformers/quantization/bitsandbytes), [PEFT/QLoRA](https://huggingface.co/docs/peft/main/en/developer_guides/quantization) e [SFTTrainer](https://huggingface.co/docs/trl/sft_trainer).

Os wrappers instalam primeiro PyTorch 2.14.1 pelo índice oficial CUDA 12.6, com wheels Python 3.12 verificadas para Linux amd64 e Windows amd64. Isso evita selecionar silenciosamente uma distribuição CPU. Verificam `torch.cuda.is_available()` antes de instalar os demais pacotes. Para outra GPU/driver, escolha o índice no [seletor oficial do PyTorch](https://pytorch.org/get-started/locally/) e defina `TUTORON_TORCH_INDEX_URL` (por exemplo, o índice cu130 quando apropriado). A existência dos wheels e a resolução de dependências não equivalem a um treino executado.

## Avaliar e importar

Guarde a base sem treinamento. Compare base e modelo ajustado no mesmo conjunto reservado, com as mesmas opções, medindo correção matemática, citações e abstenção. Loss menor não prova que o tutor melhorou.

Não importe um adapter sobre outra base. Para uma rota portátil, mescle o adapter com a base Hugging Face de mesma revisão em uma máquina com memória suficiente, salve pesos/tokenizer e converta/quantize para GGUF usando llama.cpp. Importe o GGUF com `FROM ./tutoron-paa-lora.gguf` em um Modelfile e execute `ollama create tutoron-paa-lora -f Modelfile`. Verifique a [documentação atual de importação](https://docs.ollama.com/import); não se presume suporte a ADAPTER para toda arquitetura.

O contexto acadêmico continua sendo recuperado pelo RAG após fine-tuning. Os pesos não são um banco atualizado de PDFs. Antes da implantação pública, conclua a validação cega, corrija os erros observados e registre desempenho/latência com o hardware escolhido.
