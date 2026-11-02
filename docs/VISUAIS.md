# Aprender com desenhos — Manim

Abra **`/visuais`** pelo link **Aprender com desenhos** no TutorON. Escolha um tema, reproduza a animação e use **Pausar na pergunta**. A pergunta também aparece fora do vídeo, para continuar legível com os controles do player. Depois escreva uma tentativa e clique em **Continuar com o tutor**. O formulário recebe a dúvida e a tentativa para conferência; o aluno ainda precisa clicar em **Pedir ajuda**.

## Sete exemplos para apresentar

| Exemplo | O que mostra | O que deixa para o aluno |
|---|---|---|
| Robô / programação dinâmica | Custos do terreno, obstáculos e predecessores, separados da tabela de estados | Valores de DP, tratamento do bloqueio e rota |
| Fluxo residual | Fluxo/capacidade de uma rede viável e uma aresta destacada | Residual numérico, caminho aumentante e fluxo máximo |
| Karnaugh | Ordem Gray e um grupo parcial que atravessa as bordas | Outros grupos e expressão simplificada |
| Circuito / tabela-verdade | Portas, fios e combinações de entrada | Sinais intermediários e todas as saídas |
| BFS | Grafo não ponderado e primeira fronteira | Fila, marcação e restante da busca |
| Certificado em NP | Um vértice marcado e suas arestas incidentes | Verificar arestas restantes e construir um certificado completo |
| Redução | Direção A → B, transformação polinomial e condição de equivalência | Definir uma transformação específica e sua prova |

São exemplos didáticos controlados, não respostas geradas para o enunciado do aluno. A geração usa Manim de verdade, em processo separado; os vídeos e imagens de prévia ficam em `dados/animacoes`. A primeira preparação nesta máquina levou de 4 a 10 segundos por exemplo após os ajustes; os vídeos têm aproximadamente 7–12 segundos. O limite por render continua sendo 90 segundos. O cache muda quando o roteiro ou o código do desenho muda. Pedidos simultâneos pelo mesmo exemplo compartilham o render.

## Preparar antes da apresentação

Com o ambiente do servidor instalado pelo atalho normal:

```powershell
.venv\Scripts\python scripts\preparar_visuais.py
```

O comando renderiza os sete exemplos sem chamar modelos, cria as prévias e exporta quadros intermediários/finais e metadados em `tmp/qa-visuais`. Depois abra `http://127.0.0.1:8000/visuais`. Não depende da cota de Gemini para os exemplos do catálogo. MP4 é o formato desta primeira versão; a galeria exige um navegador que o reproduza. A demo offline anterior permanece separada.

## Animação da dúvida do aluno

O botão **Ver em animação (beta)** continua no final da ajuda do tutor. A IA preenche um roteiro JSON, nunca Python. O esquema e a revisão são aplicados antes do render. Além das quatro cenas anteriores do PR #29, há `grade_dp`, `fluxo`, `karnaugh`, `circuito` e `reducao`.

A personalização ainda é experimental: os dois ensaios locais iniciais (robô e Karnaugh) falharam ao validar/revisar o roteiro. Quando há correspondência de tema, o atendimento agora oferece um exemplo relacionado do catálogo, identificado com **“Este vídeo usa outro exercício…”**. Não adapta os números do aluno nem o apresenta como se fosse sua questão. Nos dois ensaios posteriores, esse caminho entregou os vídeos em cerca de 12 segundos. Sem correspondência, mantém a falha explícita e o link para explorar os exemplos.

## Barreiras e limites

- Karnaugh valida retângulos de potência de dois com adjacência cíclica, rejeita zero obrigatório no grupo e deixa outros uns sem agrupar.
- Fluxo valida capacidades e conservação nos nós internos; destaca somente uma saída disponível da fonte.
- Circuito valida dependências e entradas das portas. Os sinais calculados são desenhados como `?`, sem campo para saídas prontas.
- Grade não recebe caminho ou tabela resolvida; mostra apenas as dependências e os custos de entrada.
- Layout dos grafos pode ser explicitado para evitar cruzamentos desnecessários.
- A revisão por IA de roteiros personalizados também pode falhar. A verificação técnica dos exemplos controlados não substitui avaliação docente de sua utilidade pedagógica.

O modelo textual atual continua podendo dar pistas erradas. O teste de interface confirmou a transferência da tentativa para o tutor, mas uma resposta sobre a grade confundiu dependências de células. A galeria ajuda a estruturar o raciocínio; não é evidência de que os pesos ou o revisor estejam validados.

## Verificação desta entrega

372 testes automatizados passaram; um teste opcional de treino foi ignorado no ambiente do servidor. Os sete vídeos foram renderizados, decodificados integralmente e seus quadros finais foram conferidos. A interface foi verificada em janela normal e em 390 px, sem rolagem horizontal da página; a seleção de tema pode rolar dentro da própria lista. Foram verificados vídeo, pausa, preenchimento do formulário e envio manual ao tutor, além dos dois ensaios reais com caminho alternativo. Evidências em `eval/results/visuais-20261102/`.
