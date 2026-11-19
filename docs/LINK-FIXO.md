# Link fixo do TutorON (o servidor é este PC)

O TutorON roda neste computador. Enquanto o `1-Iniciar-Servidor.bat` estiver aberto, a IA e o site ficam na internet por um túnel seguro. Nenhuma porta do roteador precisa ser aberta e os dados continuam no PC.

Hoje, sem configuração, o túnel é o **rápido** da Cloudflare: o endereço é `https://palavras-aleatorias.trycloudflare.com` e **muda a cada reinício**. Para ter **um link único que nunca muda**, escolha uma das opções abaixo e coloque as variáveis no `.env`.

| | Opção A: Tailscale Funnel | Opção B: domínio próprio + Cloudflare |
|---|---|---|
| Custo | grátis | domínio: cerca de R$ 40/ano (`.com.br` no registro.br) |
| Endereço | `https://tutoron.<sua-rede>.ts.net` | `https://tutoron.com.br` (o que você registrar) |
| Tempo de configuração | 10 min | 30 min + propagação do DNS |
| Pré-visualização no WhatsApp | sim | sim |
| Recomendado para | começar já | a versão pública definitiva |

## Opção A: Tailscale Funnel (grátis, endereço fixo)

1. Instale o Tailscale para Windows: <https://tailscale.com/download/windows> e entre com uma conta (Google/GitHub).
2. No painel <https://login.tailscale.com/admin/machines>, renomeie este PC para `tutoron` (o endereço vira `tutoron.<rede>.ts.net`).
3. No painel, em **DNS**, ative **MagicDNS** e **HTTPS Certificates**.
4. Em **Access controls**, permita o Funnel (o painel oferece um botão "Enable Funnel" na primeira vez que você rodar o comando abaixo).
5. Teste uma vez no PowerShell: `tailscale funnel --bg 8000` e depois `tailscale funnel --https=443 off`.
6. No `.env`:

   ```
   TUTORON_TUNEL=tailscale
   TUTORON_URL_PUBLICA=https://tutoron.<sua-rede>.ts.net
   ```

7. Abra o `1-Iniciar-Servidor.bat`. A janela mostra o link fixo e o copia para a área de transferência.

## Opção B: domínio próprio com túnel nomeado da Cloudflare

1. Registre um domínio (ex.: `tutoron.com.br` no registro.br) e adicione-o a uma conta grátis da Cloudflare (troque os servidores DNS no registro.br pelos que a Cloudflare indicar).
2. No painel da Cloudflare: **Zero Trust → Networks → Tunnels → Create a tunnel** (tipo *Cloudflared*), nome `tutoron`.
3. Copie o **token** que aparece no comando de instalação (o texto longo depois de `--token`). Não precisa instalar o serviço: o TutorON já baixa o `cloudflared`.
4. Em **Public Hostname**, adicione `tutoron.com.br` (ou `www`) apontando para `http://127.0.0.1:8000`.
5. No `.env`:

   ```
   TUTORON_TUNEL=cloudflare
   TUTORON_TUNEL_TOKEN=<token do passo 3>
   TUTORON_URL_PUBLICA=https://tutoron.com.br
   ```

6. Abra o `1-Iniciar-Servidor.bat`.

## Deixar o servidor sempre no ar

- `6-Iniciar-com-o-Windows.bat`: liga o TutorON sozinho ao entrar no Windows (rode de novo para desligar).
- A janela do servidor já impede o PC de suspender, religa o site se ele travar (3 falhas seguidas de `/health`), religa o modelo local se ele cair e reabre o túnel.
- Em **Configurações → Sistema → Energia**, deixe "Quando conectado, suspender após: Nunca".
- No BIOS/UEFI, a opção "Restore on AC power loss: Power On" faz o PC voltar sozinho depois de uma queda de luz; com o passo acima, o TutorON volta junto.

## Pré-visualização do link

Ao mandar o link no WhatsApp, Telegram, Discord ou Instagram, aparece o card com logo, título e descrição (`og:title`, `og:description`, `og:image` em `backend/web/index.html`). A imagem é `backend/web/marca/previa.png`, gerada por `python scripts/gerar_marca.py`. Com `TUTORON_URL_PUBLICA` preenchida, os endereços do card usam o link fixo; sem ela, usam o endereço pelo qual a página foi aberta. O WhatsApp guarda o card em cache por alguns dias: depois de trocar a imagem, teste com um link novo (ex.: `.../?v=2`).
