# Treinar o TutorON

Um clique: **`3-Treinar.bat`**. Na primeira vez ele cria `.venv-treino`, instala PyTorch com CUDA (~3 GB) e baixa os pesos do Qwen3-8B do Hugging Face (~16 GB, em `.tools/hf`). Depois disso, cada treino leva poucos minutos.

## O que acontece

| Etapa | O quê | Onde fica |
|---|---|---|
| 1. Dados | Soluções corrigidas do acervo viram pares pergunta → resposta, no mesmo formato de prompt do servidor. Questões do benchmark ficam de fora. | `05-modelo/treino/treino.jsonl`, `validacao.jsonl`, `manifesto.json` |
| 2. Treino | QLoRA: modelo em 4 bits na GPU, adapter LoRA rank 16 em todas as projeções. Descarrega o Ollama da GPU antes. | `.tools/treino/adapter`, `.tools/treino/resultado-treino.json` |
| 3. Mescla | Aplica o adapter nos pesos originais, um arquivo por vez (cabe em 16 GB de RAM). | temporário, apagado no fim |
| 4. Ollama | Converte para GGUF (conversor do llama.cpp), quantiza em Q4_K_M e importa como `tutoron-paa-ft` (mesmo tamanho do atual). | `.tools/models` |
| 5. Avaliação | Perguntas de validação + sondas de matemática, respondidas pelo modelo atual e pelo novo; um juiz (Gemini) compara com a solução de referência. | `05-modelo/treino/avaliacao-AAAAMMDD-HHMM.md` |

O modelo em uso **não é trocado sozinho**. Leia o relatório; se o novo for melhor, coloque no `.env`:

```
TUTORON_MODELO_LOCAL=tutoron-paa-ft
```

e reinicie o `1-Iniciar-Servidor.bat`. Para voltar, apague a linha.

## Opções

```bat
3-Treinar.bat --passos 60           :: mais passos (padrão 30; com poucos dados, mais passos sobreajustam)
3-Treinar.bat --so-dados            :: só exporta os dados, sem treinar
3-Treinar.bat --pular-avaliacao     :: não gera o relatório
3-Treinar.bat --base Qwen/Qwen3-4B  :: base menor (precisa trocar também o modelo servido)
```

O servidor pode ficar ligado durante o treino: o Gemini continua respondendo, e o modelo local volta para a GPU sozinho na próxima vez que for usado.

## Limites (importante)

- **O dataset é pequeno** (26 exemplos de treino, 6 de validação) e foi corrigido por agente, não por professor. Ele prova que o processo funciona; não sustenta, sozinho, uma melhora pedagógica.
- **Loss menor não significa tutor melhor.** Compare pelo relatório de avaliação e pela validação A/B com alunos.
- O treino não ensina o conteúdo do livro: a RAG continua buscando o material em cada pergunta.
- Para reduzir os erros de matemática, o que mais ajuda é ter **mais soluções corretas e revisadas**: cada resolução nova aprovada em `03-triagem/revisoes.json` e curada no acervo entra no próximo treino. As avaliações com "erro de matemática" marcadas pelos alunos (`dados/validacao/avaliacoes.jsonl`) mostram onde o modelo erra.

## Hardware desta máquina

RTX 4060 (8 GB), i5-12400F, 16 GB de RAM. Inferência do Qwen3 8B Q4_K_M: ~45 tokens/s. Treino QLoRA do 8B com contexto de 1536 tokens cabe na VRAM com checkpointing.
