# Hospedagem do TutorON (site na nuvem + modelo local no PC)

Decisão de 19/11/2026: o site sai do PC e vai para a nuvem, com banco Supabase e contas.
O **modelo local continua sendo o principal**: o PC da equipe empresta a GPU enquanto estiver ligado.

```
 aluno ──► site hospedado (Render, Docker) ──► Supabase (contas, cota, coleta)
                 │
                 ├─ 1º modelo local do TutorON ◄── túnel ◄── PC da equipe (7-Ligar-IA-Local.bat)
                 ├─ 2º Groq (gpt-oss-120b / 20b)        ← quando o PC está desligado ou demora
                 └─ 3º Gemini                            ← reserva final
```

- **PC ligado:** o PC abre um túnel e avisa o site a cada minuto (`scripts/worker_pc.py`). O site usa o
  modelo local primeiro (plano grátis). O aviso a cada minuto também impede o Render de "dormir".
- **PC desligado:** em até 2,5 min o site para de tentar o PC e responde direto pelo Groq/Gemini,
  sem o aluno esperar o prazo do modelo local.
- A conexão com o PC tem senha (`TUTORON_WORKER_TOKEN`) e só libera as rotas de geração do Ollama.

## Onde hospedar: Render (plano Free)

| | Render Free | Observação |
|---|---|---|
| Custo | R$ 0 | sem cartão |
| Memória | 512 MB | suficiente para o site; animações Manim longas podem faltar memória |
| Dorme | após 15 min sem acesso | o worker do PC mantém acordado; sem o PC, o 1º acesso leva ~1 min |
| Disco | temporário | por isso os dados vão para o Supabase; vídeos de animação somem ao reiniciar |
| Endereço | `https://tutoron-xxxx.onrender.com` | sem domínio próprio; fixo |

Alternativa se faltar memória: Hugging Face Spaces (Docker, 16 GB grátis), mas o código do Space fica
público — e o acervo tem provas e listas dos professores. Por isso o padrão é o Render, que publica a
partir do repositório privado.

## Passo a passo

1. **Supabase**: siga `docs/supabase/CONFIGURAR.md` (banco, login Google e e-mail).
2. **Groq**: crie a chave em https://console.groq.com/keys.
3. **Render**: https://render.com → entre com o GitHub de quem é dono do repositório
   (`LarissaFDS/TutorON`, ou dê acesso a quem for publicar) → **New → Blueprint** → escolha o repositório.
   O `render.yaml` cria o serviço. Preencha as chaves pedidas:
   `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_KEY`, `GROQ_API_KEY`, `GEMINI_API_KEY`,
   `TUTORON_ADMINS` (seus e-mails) e `TUTORON_URL_PUBLICA` (o endereço `.onrender.com`).
   `TUTORON_WORKER_TOKEN` é gerado sozinho: copie o valor em **Environment**.
4. **Supabase → Authentication → URL Configuration**: Site URL = endereço do Render; Redirect URL =
   endereço do Render + `/entrar`.
5. **PC**: no `.env` do PC, coloque `TUTORON_SERVIDOR_URL=<endereço do Render>` e o mesmo
   `TUTORON_WORKER_TOKEN`. Abra `1-Iniciar-Servidor.bat` (liga o Ollama) e depois `7-Ligar-IA-Local.bat`.
   A janela mostra `servidor: ok` a cada minuto.
6. **Conferir**: `https://<endereço>/api/status` mostra `"pc_conectado": true` e o Groq habilitado.
   Entre em `/entrar` com o Google e faça uma pergunta; em `/admin` aparece sua conta e o uso.

Cada `git push` na branch configurada no Render publica de novo (o CI do GitHub roda os testes antes).

## O que ainda roda só no PC
- Treino do modelo (`3-Treinar.bat`) e o pipeline do acervo.
- Os painéis antigos `/resultados` e `/uso` (só abrem na própria máquina); no site hospedado use `/admin`.
