# Custo de tokens por pergunta (análise de 19/11/2026)

O professor apontou que o modelo local "gasta mais porque faz um monte de coisa". Ele tem razão.
O modelo local **continua sendo o principal** — o objetivo aqui é ele gastar menos.

## Como era (antes desta mudança)

Uma pergunta no modo Tutor fazia, no pior caso, **4 chamadas** à IA:

| Etapa | Entrada (tokens) | Saída (tokens) |
|---|---|---|
| 1. Gerar a ajuda (prompt de sistema ~1.300 + acervo até 9.000 caracteres ~2.300 + pergunta) | ~3.800 | **até 8.192 de raciocínio** + ~500 de ajuda |
| 2. Revisor confere se entregou a resposta (reenvia contexto + ajuda) | ~4.500 | até 256 |
| 3. Se reprovada: gera de novo com a anterior anexada | ~5.000 | até 8.192 + ~500 |
| 4. Revisa de novo | ~5.000 | até 256 |

Típico: **~10 mil tokens**; pior caso: **~35 mil**. O que mais pesava era o raciocínio (`think`) do Qwen3,
ligado por padrão, e a segunda chamada de revisão sempre.

## O que mudou

1. **Raciocínio desligado por padrão** (`TUTORON_RACIOCINIO_LOCAL=0`) e, quando ligado, limitado
   a 2.048 tokens de saída (`TUTORON_RACIOCINIO_MAX`).
2. **Acervo menor**: 3 trechos e 5.000 caracteres (`ACERVO_K`, `ORCAMENTO_CARACTERES` em `backend/rag.py`).
3. **Revisão só quando precisa**: o filtro de código (`seguranca.entrega_resposta`) roda sempre; o revisor
   por IA só roda se o texto tiver sinais de solução (números finais, "a resposta é", fórmulas resolvidas).
4. **Histórico curto**: só as 2 últimas ajudas entram no prompt.
5. **Groq como reserva**: quando o PC está desligado ou ocupado, responde o Groq (`gpt-oss-120b` com
   `reasoning_effort: low`), antes do Gemini.

Ainda pendente: a cota continua **estimando** tokens (caracteres ÷ 4). O próximo passo é usar o número
que o modelo devolve (`eval_count` no Ollama, `usage` no Groq/Gemini).

Meta: **~3–4 mil tokens por pergunta típica** (limite grátis de 40 mil ≈ 10–13 dúvidas reais; ajuste
`tokens_dia` em `backend/cota.py` depois de medir com usuários).

## Como medir

O painel `/admin` mostra tokens por conta. Compare a média antes/depois na tabela `uso_tokens`.

## Limites do Groq (plano grátis, nov/2026 — confira em console.groq.com/settings/limits)

| Modelo | Pedidos/min | Pedidos/dia | Tokens/min | Tokens/dia |
|---|---|---|---|---|
| openai/gpt-oss-120b | 30 | 1.000 | 8.000 | 200.000 |
| openai/gpt-oss-20b | 30 | 1.000 | 8.000 | 200.000 |
| qwen/qwen3.8-27b (fotos) | 30 | 1.000 | 8.000 | 200.000 |

O gargalo é **8 mil tokens por minuto**: com ~3,5 mil por pergunta, só ~2 perguntas por minuto por modelo.
Numa aula com a turma toda, o modelo local e o Gemini precisam segurar o resto. O disjuntor de
`backend/llm.py` pausa o modelo pelo tempo do `retry-after` e passa para o próximo.
