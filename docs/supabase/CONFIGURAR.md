# Configurar o Supabase (banco + login com Google e e-mail)

Leva uns 15 minutos. Quem tem a conta do projeto faz uma vez; depois é só colar as chaves no `.env`
(no PC) e nas variáveis da hospedagem.

## 1. Projeto
1. Crie a conta em https://supabase.com e um projeto novo (plano Free, região **South America (São Paulo)**).
2. Em **SQL Editor → New query**, cole todo o `docs/supabase/schema.sql` e clique em **Run**.
3. Em **Project Settings → API**, copie:
   - Project URL → `SUPABASE_URL`
   - chave `anon` / publishable → `SUPABASE_ANON_KEY`
   - chave `service_role` / secret → `SUPABASE_SERVICE_KEY` (**nunca** compartilhe nem coloque no git)

## 2. Login com e-mail
**Authentication → Providers → Email**: deixe ligado e com "Confirm email" ligado.
O Supabase grátis manda poucos e-mails por hora; para uma turma grande, configure um SMTP próprio
(Authentication → Emails → SMTP) ou use o login com Google.

## 3. Login com Google
1. No Google Cloud Console (https://console.cloud.google.com): crie um projeto →
   **APIs e serviços → Tela de permissão OAuth** (tipo Externo, nome "TutorON") →
   **Credenciais → Criar credenciais → ID do cliente OAuth → Aplicativo da Web**.
2. Em "URIs de redirecionamento autorizados", coloque o endereço que o Supabase mostra em
   **Authentication → Providers → Google** (algo como `https://<projeto>.supabase.co/auth/v1/callback`).
3. Copie o Client ID e o Client Secret para **Authentication → Providers → Google** no Supabase e ative.

## 4. Endereços permitidos
**Authentication → URL Configuration**:
- Site URL: o endereço da hospedagem (ex.: `https://tutoron.onrender.com`).
- Redirect URLs: o mesmo endereço com `/entrar`, e `http://localhost:8000/entrar` para testar no PC.

## 5. Dados que já existem
Com as chaves no `.env`:
```
python scripts/migrar_para_supabase.py            # simula e mostra o tamanho
python scripts/migrar_para_supabase.py --enviar   # envia (uma vez)
```
Nada em `dados/` é apagado. Linhas de teste ficam de fora.

## 6. Conferir
- `/entrar` mostra "Continuar com o Google" e o formulário de e-mail.
- Depois de entrar, a barra lateral mostra seu nome.
- Quem está em `TUTORON_ADMINS` vê "Contas e limites" (`/admin`) e pode mudar o limite de cada conta.
