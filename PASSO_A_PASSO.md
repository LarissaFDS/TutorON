# TutorON — o que fazer para abrir, testar, atualizar e treinar

Este é o guia principal para usar a entrega no seu computador. A branch criada é **`codex/paa-acervo-validacao`**. Não foi feito commit nem push, e as alterações que já existiam foram preservadas.

Pasta do projeto: `C:\Users\crowp\dev\TutorON`.

## 1. Testar agora, sem instalar novamente

1. Abra a pasta do projeto no Explorador de Arquivos.
2. Dê dois cliques em **`iniciar_validacao.bat`**.
3. Aguarde abrir `http://127.0.0.1:8765` no navegador. Se o script iniciar uma janela de servidor, mantenha-a aberta. Se o TutorON já estiver rodando, o script reutiliza essa instância.
4. Escolha uma dúvida na lista e clique em **Comparar respostas**.
5. Leia as respostas A e B. A posição de cada condição é sorteada a cada comparação.
6. Em cada resposta, toque numa nota de 1 a 5 para **clareza**, **confiança** e **utilidade para a prova**. A nota escolhida fica marcada em amarelo.
7. Escolha A, B ou empate e clique em **Enviar avaliação**. Comentário, curso e período são opcionais. Não informe nome, matrícula ou contato. Se faltar alguma nota, a tela diz qual.
8. A tela deve confirmar **Avaliação enviada** e já deixa a próxima dúvida da lista selecionada. O registro fica em `07-validacao-alunos\respostas.csv`.

As 12 questões prontas usam **respostas reais pré-geradas**: não precisam de internet nem de modelo carregado na hora da demonstração. Os textos podem conter erros; o objetivo da comparação é justamente identificá-los. Não use a nota do checklist como garantia de resposta correta.

Para encerrar o app, pressione **Ctrl+C** na janela do servidor. Se o navegador não abrir sozinho, cole o endereço acima. Se aparecer “porta em uso”, pode já existir uma instância funcionando: tente abrir o endereço antes de iniciar outra.

## 2. Ver se o código está funcionando

1. Dê dois cliques em **`testar_acervo.bat`**.
2. Aguarde a mensagem `passed`. O número pode aumentar conforme novos testes forem acrescentados.
3. Se aparecer `FAILED` ou um erro vermelho, copie a mensagem antes de fechar a janela.

Esse script testa a preservação de originais, extração, segmentação, erros conhecidos, filtragem da busca, fallback de modelo e gravação dos votos. Os votos de teste são gravados em uma pasta temporária, separados dos alunos.

O backend anterior também foi testado durante a entrega. Os resultados e limitações da rodada estão em **`RELATORIO_QUINTA.md`**; o histórico técnico está em `PROGRESSO.md`.

## 3. Fazer uma pergunta nova à IA local

1. Dê dois cliques em **`preparar_modelos.bat`**. Neste computador os modelos já foram baixados; o script inicia/verifica o Ollama e reutiliza os pesos. Em outra máquina, o primeiro download ocupa vários GB e exige internet.
2. Abra **`iniciar_validacao.bat`**.
3. Expanda **Ou escreva uma dúvida para responder agora**.
4. Digite uma pergunta e clique em **Comparar respostas**.
5. Aguarde: serão geradas duas respostas, uma genérica e uma com busca no acervo. Isso demora mais do que escolher uma pergunta pronta.

Exemplos para testar:

- “Quantos asteriscos ASTERISCO(n) imprime? Mostre a recorrência e confira n=3.”
- “Como provar a corretude do Algoritmo X usando indução?”
- “Qual será a sala da próxima prova?” — o acervo não permite inventar essa informação.

O gerador padrão é **qwen2.5:7b**, com contexto de 8.192 tokens. O modelo `tutoron-paa` também foi criado no Ollama com as instruções do tutor. O nome do modelo e o prompt, sozinhos, não fazem busca nos documentos: use o app ou o módulo `acervo` para ter RAG.

## 4. Colocar mais provas, listas e fotos na base

1. Coloque os arquivos em **`materiais\Disponiveis`**. Pode criar subpastas por disciplina ou semestre, mas esta implementação classifica o acervo de PAA.
2. Dê dois cliques em **`atualizar_acervo.bat`**.
3. O script faz inventário, preserva cópias em `00-originais`, extrai texto/OCR, separa blocos, aplica as regras de triagem e reconstrói a busca lexical.
4. Confira os números e pendências em `RELATORIO_QUINTA.md`.
5. Para complementar com visão e reconstruir a busca híbrida, execute **`extrair_com_visao.bat`** depois de preparar os modelos.

O processamento reaproveita saídas compatíveis já feitas. Se você mudar um documento, a nova versão ganha outro hash; a cópia anterior permanece preservada. **Não edite `00-originais`**.

O OCR impresso funciona localmente. Há texto direto, RapidOCR e suporte a Tesseract em português, caso esteja instalado. Visão local foi testada, mas apresentou muitas falhas e transcrições infiéis em manuscritos/fórmulas. Por isso, os candidatos de visão ficam **separados e incertos**, e não entram automaticamente no texto usado pela busca.

## 5. Revisar antes de usar o material como referência confiável

1. Abra **`03-triagem\relatorio.md`**: ele lista as suspeitas, inclusive os casos de NP na Lista 7 e de árvore geradora na Lista 4.
2. Abra o arquivo do item em **`03-triagem\pacote-revisao`**. Ele contém fonte, texto, parecer e um prompt para uma segunda revisão.
3. Confira a página original e os recortes em **`01-extraido\figuras`**. Não confie apenas no parecer da IA.
4. Se houver erro no texto extraído, crie uma **nova transcrição revisada** em `materiais\Curadoria`, com um exercício por `.md`, número da questão, assunto e uma linha de fonte com arquivo/página. Não sobrescreva o original. Execute `atualizar_acervo.bat` para incorporá-la.
5. Confira o ID e o SHA-256 desse item em **`02-acervo\itens.json`**.
6. Para registrar uma aprovação, edite **`03-triagem\revisoes.json`**, acrescentando um objeto como o abaixo, com os valores reais do item:

```json
{
  "ID_REAL_DO_ITEM": {
    "sha256": "HASH_REAL_DE_ITENS_JSON",
    "revisor": "quem conferiu",
    "confiabilidade": "alta",
    "justificativa": "Enunciado, fonte e resolução conferidos na página original e revisados pelo professor."
  }
}
```

Mantenha os registros já existentes; não substitua o arquivo todo pelo exemplo. Use `media`, `baixa` ou `nao_verificada` quando esse for o parecer adequado. Uma classificação `alta` exige revisão real. Se a fonte mudar, o hash antigo deixa de aprová-la.

7. Execute **`avaliar_modelos.bat`** para aplicar a revisão, reconstruir o índice híbrido e atualizar a avaliação. Esse processo pode levar vários minutos.

O `indice.csv` é uma saída de consulta. Não faça sua curadoria apenas nele: a próxima execução o gera novamente. Fotos com classificação duvidosa e cortes inseguros ficam pendentes, em vez de receberem uma classificação inventada.

## 6. Rodar uma nova avaliação da IA

1. Prepare os modelos com **`preparar_modelos.bat`**.
2. Execute **`avaliar_modelos.bat`**.
3. Aguarde a sequência completa: pareceres locais → índice híbrido → 12 questões × 3 condições → pares offline.
4. Abra **`06-avaliacao\relatorio.md`**.
5. Confira as respostas completas, fontes usadas, provedor e tempo em **`06-avaliacao\resultados.json`**.
6. Feche e reabra o servidor de validação para apresentar os novos pares.

As três condições são: **genérico**, **RAG manual** e **RAG automática**. A seleção manual inclui material errado em casos adversariais; a busca automática filtra baixa confiança. Portanto, nem todo “não encontrou a fonte esperada” significa falha: em alguns casos, a fonte foi excluída de propósito.

As expressões regulares medem cobertura de um checklist, não correção matemática. O checklist e as fontes esperadas precisam ser conferidos com o professor. Execuções idênticas reutilizam o cache; mudar pergunta, contexto, provedor ou modelo gera uma nova chamada. Não confunda reaproveitamento de cache com repetição experimental independente.

A geração local usa limite inicial de 1.800 tokens de saída. Se a resposta terminar por esse limite, tenta uma vez com 3.600 e registra a repetição. Se continuar incompleta, registra falha; não apresenta a resposta cortada como concluída.

Para rodar somente duas questões, abra PowerShell na pasta do projeto e use:

```powershell
.venv-acervo\Scripts\python.exe -m acervo avaliar --gerar --questoes Q1,Q2
```

Esse comando gera o relatório da amostra selecionada. Rode novamente sem `--questoes` para voltar ao conjunto completo.

## 7. Ver o que os alunos acharam

1. Execute **`resumo_validacao.bat`**.
2. Confira o total de votos, percentual de preferência e médias por questão.
3. O resumo também fica em **`07-validacao-alunos\resumo.json`**.

Os votos são associados à condição real no servidor, mesmo quando A/B trocam de posição. Pares da PoC histórica e pares da RAG automática têm origens diferentes e são agrupados separadamente. Não apague votos reais para “limpar testes”; os testes técnicos já usam outra pasta.

## 8. “Treinar a IA” agora: atualizar a base de conhecimento

Para o protótipo atual, a melhoria vem de **RAG e curadoria**:

1. Adicione materiais.
2. Execute extração/OCR.
3. Revise fontes e soluções.
4. Reconstrua a busca.
5. Rode a avaliação.
6. Compare os resultados com o professor.

Isso faz a IA consultar materiais melhores a cada pergunta. **Não altera os pesos do modelo.** É o caminho já implementado e executado nesta entrega.

## 9. Fine-tuning de verdade: preparar agora, treinar depois

Não foi feito fine-tuning. Também não existe um `.bat` que treina pesos automaticamente, porque as respostas ideais ainda precisam ser aprovadas. Executar treinamento sobre resoluções erradas ensinaria esses erros ao modelo.

### Preparar o dataset

1. Conclua a revisão do passo 5 e aprove somente itens realmente confiáveis.
2. Edite **`05-modelo\pares-aprovados.json`**, acrescentando pares pergunta → resposta ideal:

```json
[
  {
    "fonte_id": "ID_REAL_DO_ITEM",
    "sha256": "HASH_REAL_DE_ITENS_JSON",
    "revisor": "quem aprovou a resposta ideal",
    "pergunta": "Pergunta conferida com o professor",
    "resposta_ideal": "Resposta completa e revisada, com justificativa e fonte"
  }
]
```

3. Execute **`exportar_dataset.bat`**.
4. Abra **`05-modelo\dataset-finetuning.jsonl`**. Cada linha é um par aprovado cuja fonte ainda tem o mesmo hash e confiança alta.
5. Se o arquivo estiver vazio, ainda não há pares elegíveis. Não preencha com respostas automáticas só para aumentar o número de exemplos.

### Treinar e importar futuramente

1. Separe treino, validação e teste por família de questão/semestre, evitando versões quase iguais nos dois lados.
2. Escolha um modelo base e um ambiente separado, preferencialmente Linux/WSL2, com Transformers + PEFT/TRL ou Unsloth.
3. Configure SFT com LoRA/QLoRA e fixe versões, template, contexto e batch. A RTX 4060 tem 8 GB: inferência funciona, mas um treino 7B pode precisar de contexto/batch menores, offload ou uma GPU maior.
4. Treine somente no conjunto de treino e avalie no conjunto separado. Confira precisão, citações, abstenção e reprodução de erros; não use só perda de treinamento.
5. Verifique a compatibilidade do adapter com o Ollama. Quando suportado, crie um Modelfile com o mesmo modelo base e `ADAPTER`; em outros casos, mescle/converta o modelo para GGUF e importe.
6. Compare o modelo novo com o anterior nas mesmas condições antes de usá-lo com alunos.

Os detalhes e a documentação oficial de importação estão em **`05-modelo\COMO_TREINAR.md`**. Essa etapa futura ainda não foi executada nem validada no hardware local. Criar o alias `tutoron-paa` por Modelfile configura o tutor; não é fine-tuning.

## 10. Se algo não funcionar

| Sintoma | O que fazer |
|---|---|
| App não abre | Mantenha a janela do `.bat` aberta e visite `http://127.0.0.1:8765`. Confira se outro servidor já usa essa porta. |
| Perguntas prontas funcionam, pergunta nova falha | Execute `preparar_modelos.bat` e tente novamente. O modo offline não precisa do Ollama, mas a pergunta nova precisa. |
| Arquivo novo não aparece | Confira se está em `materiais\Disponiveis`, execute `atualizar_acervo.bat` e confira `inventario.csv`. |
| Busca aparece como `lexical` | Confira `04-rag\indice.json`, campo `erro_embeddings`. Execute `avaliar_modelos.bat` com Ollama disponível para reconstruir a busca híbrida. |
| Questão ficou fora da busca | Veja confiança, assunto e segmentação em `itens.json`. Itens baixos, ilegíveis ou incertos são filtrados. |
| OCR está errado | Confira a imagem original e crie uma transcrição revisada separada. Não “corrija” o arquivo original. |
| Arquivo do dataset está vazio | Confira fonte aprovada como alta, hash atual, revisor, pergunta e resposta ideal. |
| Notebook ficou lento | Aguarde a etapa terminar ou interrompa com Ctrl+C. O cache permite reaproveitar etapas concluídas; não inicie dois lotes ao mesmo tempo. |

Não é necessário configurar uma chave do Gemini para executar este roteiro. A opção Gemini/fallback existe para uso posterior explícito; os testes reais desta entrega foram locais.

## Ordem recomendada para a apresentação

1. **Hoje:** abra `iniciar_validacao.bat` e experimente duas ou três questões.
2. **Com a equipe:** confira `03-triagem\relatorio.md` e os exemplos problemáticos.
3. **Com o professor:** valide fontes, cortes e checklists antes de aprovar o dataset.
4. **Depois da revisão:** execute `avaliar_modelos.bat`, reapresente os pares e acompanhe `resumo_validacao.bat`.

Para detalhes técnicos adicionais: `docs\ACERVO_LOCAL.md`. Para mostrar o estado da entrega: `RELATORIO_QUINTA.md`.
