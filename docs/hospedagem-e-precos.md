# TutorON — hospedagem gratuita e estudo de preço por token (15/11/2026)

Material de partida para o estudo de cobrança. Os preços de API abaixo são de referência e
**precisam ser conferidos** na página de preços do Google antes de qualquer decisão.

## 1. Onde hospedar

Decisão de 15/11/2026: **o servidor é o PC do projeto** (`1-Iniciar-Servidor.bat`), e todos os dados
ficam salvos nele, em `dados/`. Nuvem (Oracle, Hugging Face) fica para depois.

Para ter um link fixo sem mudar isso: use um túnel nomeado da Cloudflare (o túnel é grátis e o domínio custa
cerca de R$ 40/ano) e preencha `TUTORON_TUNEL_TOKEN` e `TUTORON_URL_PUBLICA` no `.env`. Sem isso, o link
`*.trycloudflare.com` continua mudando a cada reinício.

O limite real de usuários é a cota do Gemini, por isso a cota por usuário abaixo continua valendo.

## 2. O que foi implementado (protótipo)

- **Convidado sem login**: cada navegador recebe um cookie anônimo `tutoron_id`; a cota vale por ele.
- **Cota por janela**: `TUTORON_COTA_TOKENS` (padrão 40.000) a cada `TUTORON_COTA_JANELA_H` (padrão 5 h).
  Esgotou → resposta 429 "Ela renova às HH:MM. Veja os planos em /planos." O topo do site mostra
  o saldo ("Plano grátis · 62% restante · renova às 19:04").
- **Conta de desenvolvedor sem limite**: defina `TUTORON_DEV_CHAVE=<senha longa>` no `.env` e abra
  uma vez `https://<seu-link>/dev?chave=<senha>`. O navegador guarda o cookie por 180 dias. Quem
  acessa da própria máquina do servidor também não tem limite. Para a equipe toda, compartilhem a chave.
- **Página /planos** com os planos e preços abaixo; botão "Assinar (em breve)" desativado.
- `TUTORON_COTA_TOKENS=0` desliga a cota.
- Código: `backend/cota.py`; testes: `backend/tests/test_cota.py`.

Limitações conhecidas do protótipo:
- Tokens são **estimados** (caracteres ÷ 4) só do que o aluno vê (pergunta, contexto, histórico, resposta);
  foto = 1.500 e animação = 3.000 fixos. O custo real inclui o prompt de sistema e o material da RAG
  (5 a 10x mais). Próximo passo: usar a contagem exata que o Gemini (`usageMetadata`) e o Ollama
  (`prompt_eval_count`/`eval_count`) já devolvem.
- Limpar cookies ou abrir aba anônima gera uma cota nova. Com login (Google) isso acaba.
- Estado em `dados/cota.json`: ok para um servidor só.

## 3. Custo por pergunta (estimativa)

Uma dúvida típica no modo Tutor: ~6.000 tokens de entrada (prompt + trechos da RAG + histórico) e
~800 de saída. Com um Gemini Flash na faixa de US$ 0,30 / 1M de entrada e US$ 2,50 / 1M de saída:

| Item | Conta | US$ | R$ (US$ 1 ≈ R$ 5,70) |
|---|---|---|---|
| Entrada | 6.000 × 0,30 / 1M | 0,0018 | 0,010 |
| Saída | 800 × 2,50 / 1M | 0,0020 | 0,011 |
| **Por pergunta** | | **~0,004** | **~R$ 0,02** |
| Foto lida | ~1 imagem + transcrição | ~0,002 | ~R$ 0,01 |

Modelo local (Ollama): custo por token ~zero, mas paga-se o servidor/GPU e é mais lento.

## 4. Proposta de planos (para o estudo validar)

| Plano | Preço | Cota | Custo de API estimado do usuário pesado | Margem bruta |
|---|---|---|---|---|
| Grátis | R$ 0 | 40 mil tokens / 5 h (≈15–25 dúvidas) | ~R$ 2/mês se usar todo dia | negativa (custo de aquisição) |
| Estudante | R$ 14,90/mês | 10x o grátis | ~R$ 6/mês (300 dúvidas) | ~45% depois de taxas de pagamento (~5%) e imposto (Simples ~6%) |
| Intensivo (provas) | R$ 29,90/mês | ~40x o grátis | ~R$ 15/mês (750 dúvidas) | ~40% |
| Instituição | R$ 3 a 6 por aluno/mês | combinada | uso médio bem menor que o pesado | maior margem, venda B2B |

Pontos para o analista estudar:
1. Medir o consumo real (tokens exatos por pergunta, por disciplina, por modo) antes de fixar preços.
2. Quanto do tráfego o modelo local consegue absorver (cada pergunta nele é ~custo zero de API).
3. Pacotes avulsos ("+100 dúvidas por R$ 4,90") além da assinatura.
4. Preço anual com desconto e meia-entrada para semestre.
5. Meio de pagamento (Pix recorrente / Mercado Pago / Stripe) e emissão de nota.
