-- TutorON: banco de contas, cota e coleta (Supabase / Postgres).
-- Rode uma vez no Supabase: SQL Editor -> New query -> cole tudo -> Run.
-- Limites do plano grátis e regra de tamanho: docs/BANCO-E-LIMITES.md.
--
-- Segurança: todas as tabelas têm RLS ligado e NENHUMA política pública. Só o servidor, com a
-- chave de serviço (SUPABASE_SERVICE_KEY), lê e grava. O navegador usa a chave pública só para login.

-- ------------------------------------------------------------------ contas
create table if not exists public.perfis (
    id            uuid primary key references auth.users (id) on delete cascade,
    email         text,
    nome          text,
    limite_tokens integer check (limite_tokens is null or limite_tokens >= 0), -- null = limite do plano
    criado_em     timestamptz not null default now()
);

-- ------------------------------------------------------------------ cota e planos (backend/cota.py)
create table if not exists public.cota_diaria (
    quem   text    not null,          -- "u:<uuid>" (conta), "c_..." (convidado) ou "ip:..."
    dia    date    not null,
    usados integer not null default 0,
    primary key (quem, dia)
);

create table if not exists public.planos (
    quem     text primary key,
    plano    text not null,
    desde    text,
    cartao   text,                     -- só os 4 últimos dígitos digitados (pagamento SIMULADO)
    simulado boolean not null default true
);

create table if not exists public.uso_tokens (
    id     bigint generated always as identity primary key,
    data   timestamptz not null default now(),
    quem   text not null,
    tokens integer not null,
    dev    boolean not null default false,
    tipo   text,
    plano  text
);
create index if not exists uso_tokens_quem_data on public.uso_tokens (quem, data desc);

-- Resumo por usuário para o painel /admin (Cota.relatorio).
create or replace view public.uso_por_usuario as
select quem,
       sum(tokens)::bigint                                          as tokens,
       count(*) filter (where tipo in ('pergunta', 'comparacao'))   as perguntas,
       count(*) filter (where tipo = 'foto')                        as fotos,
       count(*) filter (where tipo = 'animacao')                    as animacoes,
       min(data)                                                    as primeiro,
       max(data)                                                    as ultimo,
       bool_or(dev)                                                 as dev
from public.uso_tokens
group by quem;

-- ------------------------------------------------------------------ coleta (backend/dados.py)
-- Mesmo formato para todas: o registro completo fica em `dados` (jsonb), como nos arquivos .jsonl.
do $$
declare t text;
begin
  foreach t in array array['perguntas', 'feedback', 'fotos', 'animacoes', 'comparacoes', 'avaliacoes'] loop
    execute format('create table if not exists public.%I (
        id        text primary key,
        criado_em timestamptz not null default now(),
        usuario   text,
        dados     jsonb not null
    )', t);
    execute format('create index if not exists %I on public.%I (usuario, criado_em desc)', t || '_usuario', t);
  end loop;
end $$;

-- ------------------------------------------------------------------ segurança
do $$
declare t text;
begin
  foreach t in array array['perfis', 'cota_diaria', 'planos', 'uso_tokens', 'perguntas', 'feedback',
                           'fotos', 'animacoes', 'comparacoes', 'avaliacoes'] loop
    execute format('alter table public.%I enable row level security', t);
  end loop;
end $$;
alter view public.uso_por_usuario set (security_invoker = true);

-- ------------------------------------------------------------------ manutenção (docs/BANCO-E-LIMITES.md)
-- Tamanho atual do banco (o plano grátis tem 500 MB; teto de trabalho 350 MB):
--   select pg_size_pretty(pg_database_size(current_database()));
-- Limpeza: texto completo das respostas fica 30 dias; depois, só os metadados.
--   update public.perguntas set dados = dados - 'resposta' - 'prompt' - 'contexto'
--   where criado_em < now() - interval '30 days' and dados ? 'resposta';

-- ------------------------------------------------------------------ permissões do servidor
-- Projetos novos do Supabase não liberam tabelas criadas por SQL para a API. Só o servidor
-- (service_role, chave secreta) recebe acesso; anon e authenticated continuam sem nada (RLS sem políticas).
grant usage on schema public to service_role;
grant select, insert, update, delete on all tables in schema public to service_role;
grant usage, select on all sequences in schema public to service_role;

-- ------------------------------------------------------------------ conversas salvas (24/11/2026)
-- Histórico do chat por conta, compactado: até 40 trocas, pergunta até 800 e resposta até 2.500 caracteres.
create table if not exists public.conversas (
    id            text primary key,          -- "<8 primeiros do usuário>-<id da conversa no navegador>"
    usuario       text not null,
    titulo        text not null default '',
    atualizado_em timestamptz not null default now(),
    dados         jsonb not null              -- {"n": 3, "trocas": [{"p": ..., "r": ..., "a": ...}]}
);
create index if not exists conversas_usuario on public.conversas (usuario, atualizado_em desc);
alter table public.conversas enable row level security;
grant select, insert, update, delete on public.conversas to service_role;
