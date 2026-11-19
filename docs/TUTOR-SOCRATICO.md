# Modo Tutor socrático, foto do papel e animações (21/10/2026)

O que mudou depois da reunião com o professor, e por quê.

## 1. Filosofia: o aluno resolve no papel, o TutorON dá ideias

O modo **Tirar dúvida** não entrega resposta. O aluno escolhe **como** quer ser ajudado:

| Tipo de ajuda | O que o tutor faz |
|---|---|
| O tutor escolhe | decide a forma que mais destrava agora |
| Uma pista | a menor dica que destrava o próximo passo |
| Perguntas-guia | 2 a 4 perguntas em sequência, sem respondê-las |
| Explicar o conceito | a teoria por trás, sem aplicar ao exercício |
| Exemplo parecido | resolve um exemplo **diferente** (outros números) |
| Conferir meu raciocínio | diz o que está certo e aponta **onde** está o primeiro erro, sem corrigir |
| Desenho/esquema | descreve um desenho para o aluno fazer no papel |

Toda ajuda termina com **"### Sua vez"**: uma tarefa curta para o aluno fazer no papel.

**Ciclo "Ainda não consegui".** Depois de cada ajuda, o aluno diz se conseguiu. Se não conseguiu (e, se quiser, escreve onde travou), o tutor recebe as ajudas anteriores daquele exercício e explica de **outro jeito**: outra abordagem, outra analogia ou um exemplo novo e mais simples, com um passo menor que o anterior. Nunca dá a resposta, e o ciclo se repete enquanto o aluno precisar. Quando o aluno deixa o tutor escolher, a forma muda a cada rodada (pista → perguntas → exemplo → desenho → conceito → mais exemplos).

### Política e revisão antes de publicar (atualização de 02/11/2026)

O prompt socrático tem regras de rigor próprias para orientar em PAA e SD, sem herdar as ordens do prompt antigo para mostrar todas as contas ou a tabela completa. Questões curtas, exemplos copiáveis e soluções distribuídas pelo histórico também são proibidos.

O atendimento acumula o texto no servidor e só o publica depois da revisão. `seguranca.entrega_resposta` faz uma checagem de frases; o revisor em `backend/tutoria.py` lê também a tarefa, o contexto e o histórico para identificar soluções sem essas frases. Se reprovar, há uma reformulação; se ela reprovar novamente ou a revisão falhar, o aluno recebe uma tarefa curta de reserva. Nenhuma versão reprovada é publicada pelo código. Isso não garante ausência de falhas semânticas: o revisor também é IA e pode aprovar algo indevido.

A mesma revisão vale para o lado TutorON da validação A/B e para os roteiros Manim antes do render. O genérico continua como controle sem instruções. Registros novos recebem `versao_politica: socratico-v2`; não agregue suas notas às avaliações antigas sem separar as versões. Os prompts legados continuam disponíveis para reproduzir experimentos históricos.

O registro guarda `revisoes_pedagogicas`, `resposta_bloqueada`, `resposta_original`, `ajustes`, `ajuda` e `rodada`. `ajuda_de_reserva` deve ser contada como falha do candidato ao avaliar sua qualidade.

Treinamento em um clique: [COMO_TREINAR.md](../05-modelo/COMO_TREINAR.md). A bateria nova é `eval/socratico.py`: salva versões brutas e publicadas e não chama Gemini no modo local.

### Demonstração: `/demo`

A página **`/demo`** (link "Veja exemplos de como funciona" no modo Tutor) mostra respostas **reais** do tutor socrático com o Gemini, gravadas em 21 e 22/10/2026 e sem edição:

- 9 exemplos: todos os tipos de ajuda, PAA e SD, o aluno pedindo "só a resposta" e uma tentativa de burlar as regras;
- o ciclo foto → conferência → "Ainda não consegui" em 3 rodadas, cada uma de uma forma diferente;
- as 3 animações Manim.

A página **não chama nenhuma IA**: funciona sem cota do Gemini e sem o modelo local, então serve para apresentar ao professor enquanto o modelo local ainda não foi treinado para o modo socrático. Os dados ficam em `backend/web/demo/demo.json`. O `backend/tests/test_demo.py` garante que a página carrega, que todos os tipos de ajuda estão lá e que nenhuma resposta da vitrine passa no filtro de "entregou a resposta".

**Plano B para apresentação, sem servidor:** [`demo-offline/TutorON-demo.html`](../demo-offline/TutorON-demo.html) é a mesma demonstração num único arquivo de 2,7 MB, com CSS, fórmulas, foto e vídeos embutidos. Abre com duplo clique em qualquer navegador (Windows ou Linux), sem internet. Os vídeos vão em WebM e MP4, porque o Firefox em alguns Linux não toca MP4; se nenhum tocar, aparece o quadro final como imagem. Depois de mudar a demo, gere de novo com `python scripts/demo_offline.py`; o `test_demo.py` falha se o arquivo ficar desatualizado.

**Modelo local:** o atendimento usa agora o prompt socrático e a revisão mesmo antes do fine-tuning. O fluxo de treinamento novo instala um candidato separado, `tutoron-socratico-ft`; o relatório desta entrega registra o que foi efetivamente testado, sem confundir mudança de prompt com adaptação dos pesos.

## 2. Do papel para o prompt sem a IA entender errado

Botão **Enviar foto do papel** no modo Tutor ([backend/foto.py](../backend/foto.py)):

1. **Visão computacional antes da IA (Pillow):** corrige a rotação da câmera (EXIF), corta a mesa e a borda vazia, aumenta o contraste e gera **recortes ampliados e sobrepostos** (3 faixas para folha em pé; grade 2×2 ou 3 faixas para folha deitada). A IA recebe a foto inteira, para o contexto e a ordem, e os recortes, para a letra pequena e manuscrita. Vai tudo num único pedido, então gasta 1 da cota.
2. **A IA só transcreve** (JSON): enunciado, tentativa do aluno (só o que ele escreveu à mão; resolução impressa vai para o enunciado), subtópicos (a, b, c…), assuntos, o que há em cada região da folha, os trechos duvidosos e a confiança.
3. **O aluno confere:** vê a foto ao lado da leitura, os trechos duvidosos em destaque, edita o texto e desmarca subtópicos errados. Só a versão confirmada vai para o tutor.

A foto **não é guardada**. Só a leitura vai para `dados/fotos.jsonl`, sem identificação, para medir a qualidade.

Com a cota do Gemini esgotada, a leitura falha com uma mensagem amigável ("digite o enunciado"). Para ter um fallback local, instale um modelo de visão no Ollama e defina `TUTORON_MODELO_VISAO_LOCAL` (ex.: `qwen2.5vl:7b`). Isso não foi testado nesta máquina, porque a GPU de 8 GB já roda o `tutoron-paa`.

## 3. Animações com Manim (protótipo)

**Fluxo atual:** **Aprender com desenhos** é uma aba separada com pergunta livre e exemplos recomendados opcionais. Em **Tirar dúvida**, a seleção inicial é **O tutor escolhe**; **Quer entender visualmente?** aparece após a ajuda textual e usa a pergunta e a explicação para gerar um desenho na própria conversa. Há um esquema aberto de blocos para conceitos, além das cenas de grade, fluxo, Karnaugh, circuito e redução. Propostas que falham pedem reformulação. Veja [VISUAIS.md](VISUAIS.md). As quatro cenas descritas abaixo são a base anterior, preservada.

**O que é o Manim:** a biblioteca Python de animações matemáticas criada pelo 3Blue1Brown. Usamos a versão da comunidade (Manim CE 0.19). Pela pip no Windows, ela já vem com PyAV (vídeo) e Pango (texto), então **não precisa de ffmpeg nem LaTeX**: só não usamos `MathTex`.

**O que existe na pesquisa:** o TheoremExplainAgent (Ku et al., ACL 2025) faz a IA escrever código Manim direto e chega a ~94% de vídeos que renderizam com o3-mini, mas com problemas de layout frequentes, vários minutos por vídeo e LaTeX instalado.

**O que fizemos, e por quê:** a IA **nunca escreve Python**. Ela escolhe um de 4 modelos de cena e preenche um roteiro JSON ([backend/animacao/roteiro.py](../backend/animacao/roteiro.py)), que é validado e desenhado por código nosso ([backend/animacao/cena.py](../backend/animacao/cena.py)):

| Modelo | Serve para |
|---|---|
| `arvore_recursao` | T(n) = aT(n/b) + f(n), custo por nível |
| `vetor` | ordenação, partição, busca binária, dois ponteiros |
| `grafo` | BFS, DFS, Dijkstra, árvore geradora, máquina de estados |
| `tabela` | programação dinâmica, tabela verdade, mapa de Karnaugh (com grupos, inclusive os que dão a volta) |

Motivos: (1) num servidor aberto na internet, executar código gerado pela IA permitiria que um texto malicioso na pergunta ou na foto virasse código rodando no PC do servidor; (2) roteiro validado não quebra por erro de sintaxe; (3) o modelo local de 8B consegue preencher JSON, mas não escrever cena Manim boa.

A animação também é uma **pista**: mostra a estrutura e os primeiros passos, deixa `?` nas últimas células e fecha com "Sua vez: …".

**Custo:** geração do roteiro e revisão pedagógica (com até uma reformulação), mais 5 a 15 s de render na CPU (480p, 24 fps, ~10 s de vídeo). Os renders rodam um de cada vez, em processo separado, com limite de 90 s. Os vídeos ficam em `dados/animacoes/`.

**Próximos passos possíveis:** mais modelos de cena (circuito com portas lógicas, linha do tempo de flip-flop, pilha de chamadas), narração por texto passo a passo sincronizada e, para o ensino superior, modelos de cena por área.
