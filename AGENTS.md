# Regras para agentes e pessoas que mexem no TutorON

Leia antes de mudar código. Vale para Claude, Codex e qualquer pessoa da equipe.

## Produto
- Tutor socrático: o modo Tutor **nunca entrega a resposta final** (`docs/TUTOR-SOCRATICO.md`).
- Um só visual: toda página usa o layout novo do chat (`backend/web/chat.css`, barra lateral).
  Não crie páginas com o layout antigo (`masthead`, abas no topo).

## Modelos de IA
- Ordem (desde 24/11/2026): Groq → Cerebras/OpenRouter (se houver chave) → Gemini →
  **modelo local do TutorON (PC da equipe, via worker `scripts/worker_pc.py`)**. A nuvem vem primeiro porque
  responde ~8x mais rápido e acerta mais; o local garante resposta quando a nuvem falha ou fica sem cota.
  `TUTORON_GRATIS_LOCAL_PRIMEIRO=1` volta a pôr o local em primeiro. Hospedagem e worker: `docs/HOSPEDAGEM.md`.
  O modelo local **não deve ser removido**.
- Custo de tokens importa (o professor cobrou isso). Antes de aumentar prompt, contexto do acervo,
  histórico ou número de chamadas por pergunta, leia `docs/CUSTO-POR-PERGUNTA.md` e meça.
- Não rode treino. Só prepare (`3-Treinar.bat` pronto para um clique).

## Banco de dados (Supabase, plano grátis)
- **Sempre confira se os dados cabem no plano grátis** antes de gravar algo novo:
  regra e números em `docs/BANCO-E-LIMITES.md` (teto de trabalho: 350 MB de 500 MB).
- Nunca grave binários no Postgres; use o Storage com prazo de expiração.
- Dados reais de alunos (votos, perguntas) ficam misturados com linhas de teste nos arquivos
  antigos de `dados/`: filtre linhas de teste, nunca apague ou mova arquivos inteiros.
- Chaves (`SUPABASE_SERVICE_KEY`, `GROQ_API_KEY`, `GEMINI_API_KEY`) só no `.env`, nunca no git.

## Desenvolvimento
- Testes: `python -m pytest backend/tests -q` antes de cada commit; tudo verde.
- Lint/format: `ruff check . && ruff format .` (configurado em `pyproject.toml`).
- Commits e PRs sem marca de autoria de IA ("Co-Authored-By: Claude", "Generated with ...").
- Arquivos temporários vão para fora do repositório; nada de `tmp/`, rascunhos de PR ou logs no git.
