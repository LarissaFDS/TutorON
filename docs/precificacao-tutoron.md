# Custo de inferência do TutorON: Gemini (API) e modelo local

Versão de 17/11/2026. Este documento estima o custo de uma resposta do TutorON nas duas fontes de inferência que o servidor usa hoje. A primeira é a API do Gemini (Google). A segunda é o modelo local servido pelo Ollama no PC do projeto. O objetivo é dar ao estudo de precificação um custo unitário defensável e mostrar a partir de que volume cada fonte compensa. Os valores marcados como premissa devem ser substituídos por medições quando estiverem disponíveis (seção 7).

## 1. Base de medição

Os tempos de resposta vêm do registro do próprio servidor (`dados/perguntas.jsonl`), com 50 respostas gravadas entre outubro e novembro de 2026. Dessas, 22 foram geradas pelo Gemini e 26 pelo modelo local. As outras 2 são recusas fixas, sem chamada de modelo, e foram descartadas.

| Fonte | Respostas | Tempo médio até a resposta completa | Tamanho médio da resposta |
|---|---|---|---|
| Gemini (cascata de modelos Flash) | 22 | 19,3 s | 1.333 caracteres |
| Local (`tutoron-paa` / `qwen3:8b`, raciocínio ligado) | 26 | 46,9 s | 1.394 caracteres |

A amostra é pequena e veio de testes internos, não de uso em sala. Serve para a ordem de grandeza, não para fixar preço.

O tamanho de uma requisição típica do modo Tutor foi estimado a partir da montagem do prompt. São cerca de 6.000 tokens de entrada: instruções de sistema, trechos recuperados do acervo da disciplina, histórico da conversa e a pergunta. A saída tem cerca de 800 tokens. No modelo local, o raciocínio interno (thinking) acrescenta por volta de 1.500 tokens gerados que o aluno não vê. A estimativa vem da diferença de tempo de geração com o raciocínio ligado e desligado.

## 2. Custo da resposta pelo Gemini

O Gemini é cobrado por token, com preços separados para entrada e saída. Usamos como referência a tabela pública dos modelos Flash: US$ 0,30 por milhão de tokens de entrada e US$ 2,50 por milhão de tokens de saída. O câmbio considerado é de R$ 5,70, com IOF de 3,5% sobre a fatura em cartão internacional. Os preços mudam com frequência e devem ser conferidos na página oficial antes do uso.

Custo de uma resposta:

    entrada  6.000 × 0,30 / 10^6 = US$ 0,00180
    saída      800 × 2,50 / 10^6 = US$ 0,00200
    total                         = US$ 0,00380  →  R$ 0,0217  →  R$ 0,0224 com IOF

A leitura de uma foto do caderno custa cerca de R$ 0,007. São aproximadamente 800 tokens de entrada (imagem e instrução) e 400 de saída (transcrição).

O custo do Gemini é inteiramente variável: não há custo fixo, e o gasto do mês é proporcional ao número de respostas. O nível gratuito da API tem custo zero, mas limita as requisições por minuto e por dia. Pelos termos do Google, os dados enviados nesse nível podem ser usados para melhorar os produtos deles. Como as perguntas são de alunos, isso pesa a favor do nível pago assim que houver uso real.

## 3. Custo da resposta pelo modelo local

O servidor é um PC com processador Intel Core i5-12400F, 16 GB de RAM e placa NVIDIA GeForce RTX 4060 de 8 GB. Pelo `nvidia-smi`, o limite de potência da placa é de 115 W, mas o driver não expõe a leitura instantânea de consumo nessa placa. Por isso as potências abaixo são premissas.

| Estado | Potência da máquina (premissa) |
|---|---|
| Ligado, sem requisição | 60 W |
| Gerando resposta (GPU no limite, CPU e restante) | 190 W |

A tarifa considerada é de R$ 0,95/kWh, valor residencial com tributos. Ela varia entre cerca de R$ 0,75 e R$ 1,10 conforme a distribuidora e a bandeira tarifária.

Energia de uma resposta, usando o tempo médio medido:

    190 W × 46,9 s = 8.911 J = 0,00248 kWh  →  R$ 0,0024
    parcela acima do consumo ocioso: 130 W × 46,9 s  →  R$ 0,0016

O servidor atende até duas gerações em paralelo (`TUTORON_LOCAL_PARALELO=2`). Em paralelo, a potência não dobra e o custo de energia por resposta cai. A conta acima considera uma geração por vez e, portanto, tende a superestimar o custo.

Diferente do Gemini, o modelo local tem um custo fixo relevante, que existe mesmo sem perguntas:

| Item | Cálculo | R$/mês |
|---|---|---|
| Energia com o PC ligado 24 h em espera | 60 W × 720 h = 43,2 kWh × 0,95 | 41 |
| Depreciação do equipamento | R$ 4.500 ÷ 36 meses (premissa de preço e vida útil) | 125 |
| Total fixo | | 166 |

A depreciação responde por três quartos do custo fixo. Se o PC é de uso pessoal e seria mantido de qualquer forma, é razoável atribuir ao TutorON só uma fração dela. Com 50%, o fixo cai para R$ 103/mês.

O custo por resposta passa a depender do volume:

    custo por resposta = 166 / N + 0,0024        (N = respostas no mês)

## 4. Comparação direta

| Critério | Gemini (API paga) | Modelo local |
|---|---|---|
| Custo variável por resposta | R$ 0,0224 | R$ 0,0024 |
| Custo fixo mensal | zero | R$ 166 (R$ 103 com 50% de depreciação) |
| Tempo médio até a resposta | 19,3 s | 46,9 s |
| Capacidade | limitada pela cota contratada; escala sem mudar o servidor | ~150 respostas/h no teto teórico, ~75/h sustentável |
| Disponibilidade | depende da internet e da cota do Google | depende do PC ligado |
| Dados dos alunos | saem para o Google | ficam no PC |
| Qualidade observada | maior; erra menos contas | menor sem raciocínio; com raciocínio fica mais próxima, mas mais lenta |

Custo total do mês para cada volume, sem os custos de pagamento e impostos:

| Respostas/mês | Só Gemini | Só local | Local por resposta | Gemini por resposta |
|---|---|---|---|---|
| 1.000 | R$ 22 | R$ 168 | R$ 0,168 | R$ 0,022 |
| 5.000 | R$ 112 | R$ 178 | R$ 0,036 | R$ 0,022 |
| 10.000 | R$ 224 | R$ 190 | R$ 0,019 | R$ 0,022 |
| 20.000 | R$ 448 | R$ 214 | R$ 0,011 | R$ 0,022 |
| 40.000 | R$ 896 | acima da capacidade | — | R$ 0,022 |

O ponto de equilíbrio é o volume em que os dois custos totais se igualam:

    166 + 0,0024 N = 0,0224 N   →   N ≈ 8.300 respostas/mês
    com depreciação a 50%:  103 / 0,020  →  N ≈ 5.150 respostas/mês

Abaixo desse volume, o Gemini é mais barato, porque o custo fixo do PC não se dilui. Acima dele, o modelo local é mais barato até o limite de capacidade. Considerando 12 h de operação por dia a 75 respostas/h, o limite é de cerca de 27.000 respostas/mês. Acima disso, o excedente volta para o Gemini ou exige outra GPU. Com 40.000 respostas/mês em operação híbrida (27.000 locais e 13.000 no Gemini), o custo seria de cerca de R$ 522, contra R$ 896 só com o Gemini.

## 5. Custo marginal e uso no plano gratuito

O custo fixo do PC existe enquanto ele estiver ligado, com ou sem o TutorON. Para uma resposta a mais, o custo relevante é o marginal, de R$ 0,0016 no local contra R$ 0,0224 no Gemini, cerca de catorze vezes menor. Isso justifica direcionar o plano gratuito para o modelo local, onde a latência maior é aceitável, e reservar o Gemini para os planos pagos e para a contingência, quando a fila local estiver cheia.

Um usuário gratuito que esgote a cota todos os dias (cerca de 20 respostas/dia, 600/mês) custa cerca de R$ 1,00/mês no local, em custo marginal, contra R$ 13,40/mês no Gemini.

## 6. Reflexo nos planos propostos

Para o plano Estudante (R$ 14,90/mês), considerou-se uma taxa de meio de pagamento de cerca de 5% e Simples Nacional de cerca de 6%. A receita líquida fica em cerca de R$ 13,26. O cenário é de 300 respostas/mês por assinante:

| Fonte das respostas | Custo de inferência | Margem bruta |
|---|---|---|
| Só Gemini | R$ 6,72 | R$ 6,54 (49%) |
| Só local (custo marginal) | R$ 0,48 | R$ 12,78 (96%) |
| Só local (com rateio do fixo a 8.300 respostas/mês) | R$ 6,72 | R$ 6,54 (49%) |

No volume de equilíbrio, as duas fontes dão o mesmo custo por resposta, R$ 0,0224. Isso permite tratar a cota em tokens como uma unidade só, sem diferenciar a fonte na cobrança. A diferença aparece na margem conforme o volume cresce.

## 7. Limitações e medições pendentes

1. As potências de 60 W e 190 W são premissas. Uma tomada medidora nos três estados (ocioso, uma geração e duas gerações em paralelo) substitui a seção 3 por valores medidos.
2. A tarifa deve ser a da conta de luz do local do servidor, com bandeira e tributos.
3. Os tokens de entrada e de saída foram estimados. As duas fontes devolvem a contagem exata: o Gemini em `usageMetadata` e o Ollama em `prompt_eval_count`, `eval_count` e `eval_duration`. O servidor ainda não grava esses campos, e a cota atual do TutorON também usa uma estimativa (caracteres ÷ 4).
4. Os preços do Gemini e o câmbio variam. A seção 2 deve ser recalculada a cada revisão de preço.
5. A amostra de 48 respostas vem de testes internos. A conta deve ser refeita após um mês de uso real, com o volume do painel de uso (`/uso`) e com tempos medidos sob carga.
