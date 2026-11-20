# Modelos — validação Linux de 07/10/2026

Ollama 0.34.4 foi instalado localmente a partir da release oficial, verificando SHA-256. O comando também está em `~/.local/bin/ollama`. Pacotes e modelos do projeto ficam em `.tools/`; o serviço escuta em 127.0.0.1:11434.

O notebook atual tem Ryzen 7 3700U e aproximadamente 10 GiB de RAM, sem GPU NVIDIA detectada. Inferência é CPU. A informação antiga sobre RTX 4060 corresponde à máquina Windows anterior, preservada em `historico/`.

A rodada principal usa `qwen2.5:3b` e `tutoron-paa`, com pesos idênticos, contexto 4096 e temperatura 0,2. A base é o cenário genérico; TutorON adiciona instruções e RAG. O controle usa as instruções sem contexto. O nome do modelo não implica treinamento: não houve fine-tuning.

Tesseract 5.3.4 português/inglês foi instalado por pacotes Ubuntu em `.tools/tesseract/`, sem sudo. RapidOCR permanece como fallback. Qwen2.5-VL 3B está disponível para candidatos de visão, mas a tentativa de manuscrito atingiu o limite de saída e foi rejeitada. Fórmulas, manuscritos e diagramas continuam sujeitos a falhas; correções legíveis por agente são derivadas e vinculadas à fonte.

Embeddings BGE-M3 e busca lexical compõem o índice híbrido de 53 blocos corrigidos com confiança média. Correções e conteúdo original possuem hashes diferentes; os vetores são reaproveitados somente quando o hash do texto coincide. Conteúdo não verificado, baixa confiança e cortes pendentes são excluídos; duplicatas textuais não ocupam todo o top-k.

Qwen2.5 7B e tutoron-paa-7b também foram preparados. O seguimento de oito respostas levou em média 225,9 segundos por resposta nesta CPU; algumas provas e recorrências melhoraram, mas a amostra não demonstra superioridade. O perfil padrão continua 3B: a recuperação automática levou em média 109,9 segundos na rodada principal, contra 40,8 segundos do genérico. Não houve treinamento de pesos em nenhum dos dois tamanhos.

Veja `../06-avaliacao/COMPARACAO_ATUAL.md` e `../RELATORIO_VALIDACAO.md` para resultados e erros. Cobertura de regex não certifica matemática. O modelo pequeno mostrou erros mesmo com dados corretos; isso limita qualquer conclusão de superioridade. A validação é anterior ao MVP e nenhuma implantação pública foi feita.

Fontes técnicas: [Linux Ollama](https://github.com/ollama/ollama/blob/main/docs/linux.mdx), [importação de modelos](https://docs.ollama.com/import), [PEFT](https://huggingface.co/docs/peft/main/en/developer_guides/quantization).
