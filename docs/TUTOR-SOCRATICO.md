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

### Onde está a garantia

- **Prompt** ([backend/prompts.py](../backend/prompts.py), `sistema_socratico`): o mesmo prompt de fontes, citações, rigor e segurança, com o objetivo trocado e a regra "nunca entregue a resposta final" acima de tudo.
- **Código** ([backend/seguranca.py](../backend/seguranca.py)): `entrega_resposta` reconhece frases de quem fecha o exercício ("a resposta final é", "gabarito:", "portanto, T(n) = Θ(…)"). Se aparecerem, a ajuda é **refeita uma vez** com um reforço. `garantir_sua_vez` acrescenta a seção "Sua vez" se a IA esqueceu. O registro (`dados/perguntas.jsonl`) marca `entregou_resposta`, `sua_vez_acrescentada`, a `ajuda` e a `rodada`.
- **Limite conhecido:** uma resolução completa escrita sem nenhuma daquelas frases passa pelo filtro. Por isso o teste com alunos deve acompanhar o campo `ajustes` do registro.

A **Validação A/B** continua com o prompt anterior (`SISTEMA_TUTOR`), para não invalidar as avaliações já coletadas. O treino e a avaliação de modelos também.

## 2. Do papel para o prompt sem a IA entender errado

Botão **Enviar foto do papel** no modo Tutor ([backend/foto.py](../backend/foto.py)):

1. **Visão computacional antes da IA (Pillow):** corrige a rotação da câmera (EXIF), corta a mesa e a borda vazia, aumenta o contraste e gera **recortes ampliados e sobrepostos** (3 faixas para folha em pé; grade 2×2 ou 3 faixas para folha deitada). A IA recebe a foto inteira, para o contexto e a ordem, e os recortes, para a letra pequena e manuscrita. Vai tudo num único pedido, então gasta 1 da cota.
2. **A IA só transcreve** (JSON): enunciado, tentativa do aluno (só o que ele escreveu à mão; resolução impressa vai para o enunciado), subtópicos (a, b, c…), assuntos, o que há em cada região da folha, os trechos duvidosos e a confiança.
3. **O aluno confere:** vê a foto ao lado da leitura, os trechos duvidosos em destaque, edita o texto e desmarca subtópicos errados. Só a versão confirmada vai para o tutor.

A foto **não é guardada**. Só a leitura vai para `dados/fotos.jsonl`, sem identificação, para medir a qualidade.

Com a cota do Gemini esgotada, a leitura falha com uma mensagem amigável ("digite o enunciado"). Para ter um fallback local, instale um modelo de visão no Ollama e defina `TUTORON_MODELO_VISAO_LOCAL` (ex.: `qwen2.5vl:7b`). Isso não foi testado nesta máquina, porque a GPU de 8 GB já roda o `tutoron-paa`.

## 3. Animações com Manim (protótipo)

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

**Custo:** 1 chamada de IA, mais 5 a 15 s de render na CPU (480p, 24 fps, ~10 s de vídeo). Os renders rodam um de cada vez, em processo separado, com limite de 90 s. Os vídeos ficam em `dados/animacoes/`.

**Próximos passos possíveis:** mais modelos de cena (circuito com portas lógicas, linha do tempo de flip-flop, pilha de chamadas), narração por texto passo a passo sincronizada e, para o ensino superior, modelos de cena por área.
