# TutorON: por que cobrar e limitar por tokens

Escrito em 15/11/2026 para quem vai fazer o estudo de precificação. Os números de custo estão em
[hospedagem-e-precos.md](hospedagem-e-precos.md). Aqui está o **porquê** do modelo escolhido.

## 1. O problema

O TutorON responde dúvidas com IA. Cada resposta tem custo variável, que depende do tamanho:
- **Gemini (API do Google):** cobra por token de entrada e de saída, e o plano grátis da API tem cota diária.
  Com muitos alunos ao mesmo tempo, essa cota acaba.
- **Modelo local (no PC do projeto):** não paga API, mas ocupa a GPU. Uma pergunta longa segura a fila para todos.

O servidor é o PC do projeto, então ele também precisa de proteção contra uso excessivo de um aluno só.

## 2. O que é token

Token é o pedaço de texto que o modelo lê e escreve, cerca de 4 caracteres ou ¾ de palavra em português.
É a unidade em que **o fornecedor nos cobra**. Uma dúvida típica gasta cerca de 6.000 tokens de entrada
(pergunta + instruções + trechos do material da disciplina + conversa anterior) e 800 de saída.

## 3. Alternativas consideradas

| Modelo de limite | Vantagem | Por que não foi escolhido |
|---|---|---|
| Nº de perguntas por dia | Fácil de entender | "Oi" e "resolva esta prova de 3 páginas com foto" contariam igual. O custo real varia mais de 10x entre perguntas. |
| Tempo de uso | Simples | Não tem relação com o custo; o aluno pensando com a aba aberta "gastaria". |
| Ilimitado com fila | Melhor experiência | Sem teto de custo: um aluno ou um robô esgota a cota do Gemini de todos. |
| **Tokens por janela de tempo** (escolhido) | Acompanha o custo real, é justo entre perguntas curtas e longas e é o padrão do mercado | É menos intuitivo. Por isso o aluno vê só uma **porcentagem** e o horário de renovação, não o número de tokens. |

## 4. Como funciona a escolha

- **Cota de 40.000 tokens a cada 5 horas por aluno** no plano grátis (≈15 a 25 dúvidas).
  A janela começa no primeiro uso. Quando acaba, o site informa o horário em que a cota volta.
  É o mesmo desenho do ChatGPT e do Claude no plano gratuito, que os alunos já conhecem.
- **Por que janela de 5 h e não diária:** o estudo acontece em sessões (antes da aula, véspera de prova).
  Com 5 horas, o aluno que esgota de manhã volta a estudar à tarde, e o pico de uso fica espalhado.
- **Aluno = navegador.** O "modo convidado" funciona sem login, por um identificador anônimo no cookie,
  e sem cookie vale o IP. Não é guardado nome, e-mail nem matrícula.
- **O que é contado:** pergunta, contexto, histórico da conversa e resposta (estimativa: caracteres ÷ 4).
  Foto = 1.500 tokens fixos e animação = 3.000 fixos, porque o custo delas não depende do texto.
- **Conta de desenvolvedor sem limite** para a equipe testar sem consumir cota.
- **Registro de uso por aluno** em `dados/uso.jsonl` no PC do servidor, com o painel `/uso`.
  É daí que vêm os dados reais para o estudo de preço.

## 5. Por que isso serve de base para a cobrança

1. **Custo e preço na mesma unidade:** o fornecedor cobra por token, então a margem de cada plano é uma conta direta.
2. **Planos viram multiplicadores da cota:** Estudante = 10x o grátis, Intensivo = 40x.
   Dá para ajustar o preço sem mudar o sistema.
3. **Pacotes avulsos** ("+100 mil tokens") são possíveis com o mesmo mecanismo.
4. **Instituições** podem comprar um volume de tokens para a turma.

## 6. Limitações conhecidas (para o estudo levar em conta)

- **A contagem atual é estimada e só do texto visível.** O custo real inclui as instruções internas e o material da disciplina,
  de 5 a 10x mais. O próximo passo técnico é registrar a contagem exata que o Gemini e o Ollama devolvem.
  **Antes de fixar preços, medir algumas semanas de uso real com a contagem exata.**
- Respostas do modelo local custam quase zero de API, mas hoje contam igual. Pode-se descontar ou não; é decisão de negócio.
- Limpar os cookies dá uma cota nova. Para um plano pago é preciso login (ex.: conta Google).
- A cobrança (Pix/cartão) ainda não existe. A página `/planos` só mostra os preços propostos.

## 7. O que pedimos ao estudo

1. Validar ou ajustar a cota grátis (40 mil / 5 h) e os preços (R$ 14,90 e R$ 29,90/mês) com os dados de `/uso`.
2. Definir se o plano principal é a assinatura do aluno ou a licença institucional (por aluno/mês).
3. Avaliar os custos de meio de pagamento, os impostos e a meta de margem.
