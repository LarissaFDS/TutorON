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
   a 1.024 tokens (`TUTORON_RACIOCINIO_MAX`).
2. **Acervo menor**: 3 trechos e 5.000 caracteres (`ACERVO_K`, `ORCAMENTO_CARACTERES` em `backend/rag.py`).
3. **Revisão só quando precisa**: o filtro de código (`seguranca.entrega_resposta`) roda sempre; o revisor
   por IA só roda se o texto tiver sinais de solução (números finais, "a resposta é", fórmulas resolvidas).
4. **Histórico curto**: só as 2 últimas ajudas entram no prompt.
5. **Contagem real**: a cota usa os tokens que o modelo/API devolve (`prompt_eval_count`/`eval_count` no
   Ollama, `usage` no Groq/Gemini), não mais caracteres ÷ 4.

Meta: **~3–4 mil tokens por pergunta típica** (limite grátis de 40 mil ≈ 10–13 dúvidas reais; ajuste
`tokens_dia` em `backend/cota.py` depois de medir com usuários).

## Como medir

`/uso` (admin) mostra tokens por pergunta e por modelo. Compare a média antes/depois na tabela `uso_tokens`.
