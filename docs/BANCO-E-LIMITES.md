# Banco de dados e limites do plano grátis (Supabase)

Medição feita em 19/11/2026. **Confira os limites atuais em https://supabase.com/pricing antes de mudar algo
grande** — eles podem ter mudado.

## Limites do plano grátis que usamos

| Recurso | Limite grátis | Observação |
|---|---|---|
| Banco Postgres | 500 MB | inclui índices e tabelas do Auth |
| Storage (arquivos) | 1 GB | vídeos de animação, fotos |
| Tráfego de saída | 5 GB/mês | |
| Usuários do Auth | 50.000 ativos/mês | Google e e-mail |
| Inatividade | projeto **pausa após 7 dias sem uso** | qualquer acesso ao banco evita a pausa |

## O que temos hoje (dados/)

| Arquivo | Tamanho | Linhas | Vai para |
|---|---|---|---|
| perguntas.jsonl | 227 KB | 60 | tabela `perguntas` (~3,8 KB por linha) |
| animacoes.jsonl | 26 KB | 14 | tabela `animacoes` |
| uso.jsonl | 3 KB | 25 | tabela `uso_tokens` |
| fotos.jsonl / feedback.jsonl | < 4 KB | 5 | tabelas `fotos` / `feedback` |
| cota.json / planos.json | < 1 KB | — | tabelas `usuarios` / `planos` |
| animacoes/*.mp4 | 5,3 MB | 36 vídeos (~150 KB cada) | **não** vão para o banco (ver abaixo) |
| testes, auditorias, logs | ~4 MB | — | ficam só no PC (não são dados de alunos) |

**Conclusão:** tudo que é dado de aluno cabe com folga (< 0,1% do limite). Migrar tudo.

## Projeção

- Uma pergunta com resposta ≈ 4–5 KB (com índice). **500 MB ≈ 100 mil perguntas.**
- Uma linha de uso ≈ 150 B (duas por pergunta). Irrelevante.
- Com 100 alunos × 20 perguntas/dia = 2.000/dia ≈ 10 MB/dia → **~50 dias para encher**.
  Por isso: o texto completo das respostas fica 30 dias; depois o job de limpeza guarda só os metadados
  (disciplina, modelo, tokens, voto). Exporte para o PC antes (`scripts/exportar_banco.py`).
- Vídeos: 1 GB ≈ 7 mil animações. Guardamos o vídeo no Storage por 7 dias (o roteiro JSON fica no banco e
  o vídeo pode ser gerado de novo).
- O acervo/RAG (`pipeline/04-rag/indice.json`) **não** vai para o banco: é estático e vai junto com o deploy.

## Regra para quem mexer no código (pessoas e agentes)

Antes de criar uma tabela ou coluna nova, ou passar a gravar algo novo:
1. Estime bytes por linha × linhas por dia × dias guardados.
2. Some com o uso atual (painel do Supabase → Database → tamanho; ou `select pg_database_size(current_database());`).
3. Se passar de **350 MB** (70% do limite), não grave: resuma, guarde menos tempo ou deixe no PC.
4. Nunca grave binários (imagens, vídeo, áudio) no Postgres — use o Storage com prazo de expiração.
5. Atualize a tabela "O que temos hoje" deste arquivo.
