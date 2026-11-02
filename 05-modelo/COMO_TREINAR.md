# Treinar o TutorON socrático

Dê duplo clique em **`3-Treinar.bat`** para treinar PAA e Sistemas Digitais. O fluxo prepara os dados, treina um adapter QLoRA sobre `Qwen/Qwen3-8B`, mescla, converte para GGUF Q4_K_M, instala como **`tutoron-socratico-ft`** e compara com o modelo configurado no servidor. O modelo em uso só muda depois que você revisar o relatório e ativá-lo.

## O que o modelo aprende

O dataset anterior de soluções completas não é usado neste fluxo. A fonte agora é [`socratico/casos.json`](socratico/casos.json): 24 famílias autorais, com sete formas de ajuda por família. São **112 exemplos de treino, 28 de validação e 28 de teste**, equilibrados entre PAA e SD. Cada exemplo orienta sem completar o exercício e devolve a vez ao aluno. Há pistas, conceitos, exemplos, desenhos, perguntas, conferência de erro e insistência depois de uma ajuda anterior.

Famílias inteiras ficam num único split. O teste não entra na loss nem na escolha de checkpoints. Conversas e avaliações dos alunos não são importadas automaticamente. Os dados são sintéticos, escritos com auxílio de IA e com revisão docente pendente; esta versão é um ponto de partida, sem ganho pedagógico comprovado.

## Um clique, cinco etapas

| Etapa | Resultado |
|---|---|
| Dados e checagem | `05-modelo/socratico/preparado/`: JSONL, manifesto com hashes e contagens. O tokenizer real verifica todos os exemplos. Se algum exceder o contexto, o fluxo para sem cortar a resposta. |
| Treino | QLoRA rank 8, contexto máximo 2048, 60 passos, batch 1 e acumulação 4. Prompt mascarado com -100: a loss conta apenas a ajuda do tutor. |
| Mescla e conversão | Pesos mesclados por arquivo e conversão pelo llama.cpp. Requer pelo menos 35 GB livres, além dos pesos já baixados. |
| Instalação | Modelo `tutoron-socratico-ft` no Ollama, com instruções socráticas também para uso direto. |
| Avaliação | 32 casos reservados pelo fluxo real de busca e atendimento, para modelo atual e candidato. JSON e Markdown com primeira versão bruta, ajuda publicada, bloqueios, reservas, fontes e tempos. |

Cada execução guarda configuração, cópia dos dados, manifesto, adapter e métricas em `.tools/treino-socratico/<execução>/`. A avaliação fica em `05-modelo/socratico/preparado/avaliacao-socratica-*.md`. A resposta de reserva não conta como sucesso do modelo. O revisor automático usa o mesmo modelo e pode errar; leia também as respostas brutas.

Na primeira execução, o atalho instala o ambiente de treino e baixa os pesos se necessário. O tempo depende do hardware e das cotas; o teste de um passo não estima sozinho a duração do treino completo. O servidor bloqueia novas inferências locais durante treino e mescla para não recarregar o Ollama na mesma GPU; Gemini continua disponível. A reserva é liberada pelo sistema operacional mesmo se o processo cair. Feche aplicações que ocupem muita VRAM.

## Ativar depois de avaliar

Edite o `.env` e reinicie o servidor:

```ini
TUTORON_MODELO_LOCAL=tutoron-socratico-ft
```

Para voltar, use o nome anterior (nesta máquina, `tutoron-paa`). Loss menor não prova que o tutor orienta melhor. Não há troca automática nem publicação de pesos em serviços externos.

## Comandos opcionais

```bat
3-Treinar.bat --so-dados          :: exporta sem CUDA, sem baixar pesos nem ligar o Ollama
3-Treinar.bat --verificar         :: exporta e confere tokens, sem carregar pesos
3-Treinar.bat --teste-gpu         :: um passo real, sem mesclar nem instalar o adapter de teste
3-Treinar.bat --passos 30         :: altera a duração do treino
3-Treinar.bat --pular-avaliacao   :: instala o candidato sem rodar a bateria; revisão continua necessária
.venv\Scripts\python eval\socratico.py --modelos tutoron-paa tutoron-socratico-ft
```

A política do servidor já é socrática antes do fine-tuning. O treino adapta os pesos para reforçar esse comportamento; a barreira de publicação continua necessária. O uso direto no Ollama não passa pela barreira do site.

Detalhes técnicos do método: [quantização e LoRA no PEFT](https://huggingface.co/docs/peft/developer_guides/quantization) e [mascaramento de labels no Transformers](https://huggingface.co/docs/transformers/main_classes/data_collator). A implementação mantém embeddings em BF16 para caber na GPU de 8 GB e usa checkpointing de gradientes.
