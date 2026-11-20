# Configurar o Supabase (banco + login com e-mail)

Leva uns 15 minutos. Quem tem a conta do projeto faz uma vez; depois é só colar as chaves no `.env`
(no PC) e nas variáveis da hospedagem.

## 1. Projeto
1. Crie a conta em https://supabase.com e um projeto novo (plano Free, região **South America (São Paulo)**).
2. Em **SQL Editor → New query**, cole todo o `docs/supabase/schema.sql` e clique em **Run**.
3. Em **Project Settings → API**, copie:
   - Project URL → `SUPABASE_URL`
   - **Publishable key** (`sb_publishable_...`) → `SUPABASE_ANON_KEY`
   - **Secret key** (`sb_secret_...`) → `SUPABASE_SERVICE_KEY` (**nunca** compartilhe nem coloque no git)

## 2. Login com e-mail
**Authentication → Providers → Email**: deixe ligado e com "Confirm email" ligado.
O Supabase grátis manda poucos e-mails por hora; para uma turma grande, configure um SMTP próprio
(Authentication → Emails → SMTP) ou use um provedor de e-mail transacional.

## 3. Login com Google
Cancelado em 19/11/2026: o login é só com e-mail e senha.

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
- `/entrar` mostra o formulário de e-mail (entrar / criar conta).
- Depois de entrar, a barra lateral mostra seu nome.
- Quem está em `TUTORON_ADMINS` vê "Contas e limites" (`/admin`) e pode mudar o limite de cada conta.
