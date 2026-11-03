# TutorON — script único chamado pelos atalhos da raiz:
#   1-Iniciar-Servidor.bat  -> -Acao Servidor   (IA ligada + site público)
#   2-Validacao.bat         -> -Acao Validacao  (abre o modo validação e os resultados)
#   3-Treinar.bat           -> -Acao Treinar    (fine-tuning QLoRA na GPU)
#   4-Reiniciar.bat         -> -Acao Reiniciar  (religa modelos e site sem mudar o endereço público)
# Outras ações: Testar, Acervo (refaz OCR/curadoria/índice), Parar.
param([ValidateSet('Servidor','Validacao','Treinar','Reiniciar','Testar','Acervo','Parar')][string]$Acao = 'Servidor',
      [Parameter(ValueFromRemainingArguments = $true)][string[]]$Extra = @())
# 'Continue': no PowerShell 5.1, avisos que programas escrevem no stderr virariam erro fatal com 'Stop'.
# Falhas de programas são checadas pelo código de saída (Falhou); cmdlets usam -ErrorAction Stop.
$ErrorActionPreference = 'Continue'
$Raiz = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $Raiz
$env:PYTHONUTF8 = '1'
$Tools = Join-Path $Raiz '.tools'
$Dados = Join-Path $Raiz 'dados'
$Logs = Join-Path $Dados 'logs'
$Python = Join-Path $Raiz '.venv\Scripts\python.exe'
$Ollama = Join-Path $Tools 'ollama\ollama.exe'
$Cloudflared = Join-Path $Tools 'cloudflared.exe'
$Porta = 8000
$Local = "http://127.0.0.1:$Porta"
New-Item -ItemType Directory -Force $Tools, $Dados, $Logs | Out-Null

function Titulo($texto) { Write-Host ''; Write-Host "== $texto" -ForegroundColor Cyan }
function Ok($texto) { Write-Host "   OK  $texto" -ForegroundColor Green }
function Aviso($texto) { Write-Host "   !!  $texto" -ForegroundColor Yellow }
function Falhou { if ($LASTEXITCODE -ne 0) { throw "Comando falhou (codigo $LASTEXITCODE). Veja a mensagem acima." } }

function Ler-Env([string]$nome) {
    $arquivo = Join-Path $Raiz '.env'
    if (!(Test-Path $arquivo)) { return '' }
    foreach ($linha in Get-Content $arquivo) {
        if ($linha -match "^\s*$nome\s*=\s*(.*)$") { return $matches[1].Trim().Trim('"') }
    }
    return ''
}

# ---------------------------------------------------------------- instalação
function Preparar-Python {
    Titulo 'Python'
    if (!(Test-Path $Python)) {
        $py = Get-Command py -ErrorAction SilentlyContinue
        if ($py) { & py -3 -m venv .venv } else { & python -m venv .venv }
        Falhou
    }
    & $Python -c "import fastapi, uvicorn, httpx, dotenv, PIL, manim" 2>$null
    if ($LASTEXITCODE -ne 0) {
        & $Python -m pip install --disable-pip-version-check -q -r requirements.txt
        Falhou
    }
    Ok 'ambiente .venv pronto'
}

function Preparar-Env {
    Titulo 'Chaves (.env)'
    $arquivo = Join-Path $Raiz '.env'
    if (!(Test-Path $arquivo)) {
        Copy-Item (Join-Path $Raiz '.env.example') $arquivo
        Aviso ".env criado a partir do .env.example. Preencha GEMINI_API_KEY em $arquivo"
    }
    if (Ler-Env 'GEMINI_API_KEY') { Ok 'GEMINI_API_KEY configurada' } else { Aviso 'Sem GEMINI_API_KEY: só o modelo local vai responder.' }
    if ((Ler-Env 'SUPABASE_URL') -and (Ler-Env 'SUPABASE_KEY')) { Ok 'Supabase configurado (livro-texto na RAG)' } else { Aviso 'Sem Supabase: a RAG usa só o acervo local.' }
}

function Iniciar-Ollama {
    Titulo 'Ollama (modelo local na GPU)'
    if (!(Test-Path $Ollama)) {
        Write-Host '   Baixando Ollama portátil oficial (sem administrador)...'
        $zip = Join-Path $Tools 'ollama-windows-amd64.zip'
        if (!(Test-Path $zip)) {
            Invoke-WebRequest -ErrorAction Stop 'https://github.com/ollama/ollama/releases/download/v0.34.4/ollama-windows-amd64.zip' -OutFile $zip
        }
        if ((Get-FileHash $zip -Algorithm SHA256).Hash -ne '535193F38F3344E5B08F5D1C171C31CE11AA17F0124FF69AE26D8EC7FE06FA62') {
            throw 'Hash inesperado no download do Ollama. Nada foi executado.'
        }
        Expand-Archive -ErrorAction Stop $zip -DestinationPath (Join-Path $Tools 'ollama') -Force
    }
    $env:OLLAMA_MODELS = Join-Path $Tools 'models'
    $env:OLLAMA_HOST = '127.0.0.1:11434'
    $env:OLLAMA_KEEP_ALIVE = '60m'
    # 2 respostas ao mesmo tempo com cache em 8 bits: quase o dobro de vazão e ainda cabe nos 8 GB.
    # Com 3, o modelo transborda para a CPU e fica mais lento (medido na RTX 4060).
    $env:OLLAMA_NUM_PARALLEL = '2'
    $env:OLLAMA_FLASH_ATTENTION = '1'
    $env:OLLAMA_KV_CACHE_TYPE = 'q8_0'
    try { $null = Invoke-RestMethod -ErrorAction Stop 'http://127.0.0.1:11434/api/tags' -TimeoutSec 3; Ok 'já estava rodando' }
    catch {
        Start-Process -FilePath $Ollama -ArgumentList 'serve' -WindowStyle Hidden `
            -RedirectStandardOutput (Join-Path $Logs 'ollama.log') -RedirectStandardError (Join-Path $Logs 'ollama-erros.log')
        for ($i = 0; $i -lt 40; $i++) {
            Start-Sleep -Milliseconds 500
            try { $null = Invoke-RestMethod -ErrorAction Stop 'http://127.0.0.1:11434/api/tags' -TimeoutSec 2; break } catch { }
        }
        Ok 'iniciado'
    }
    $instalados = (Invoke-RestMethod -ErrorAction Stop 'http://127.0.0.1:11434/api/tags').models.name
    $base = if (Ler-Env 'TUTORON_MODELO_GENERICO_LOCAL') { Ler-Env 'TUTORON_MODELO_GENERICO_LOCAL' } else { 'qwen3:8b' }
    foreach ($modelo in @($base, 'bge-m3')) {
        $nome = if ($modelo -match ':') { $modelo } else { "${modelo}:latest" }
        if ($instalados -notcontains $nome) {
            Write-Host "   Baixando $modelo (só na primeira vez)..."
            & $Ollama pull $modelo; Falhou
        }
    }
    $tutor = if (Ler-Env 'TUTORON_MODELO_LOCAL') { Ler-Env 'TUTORON_MODELO_LOCAL' } else { 'tutoron-paa' }
    $nomeTutor = if ($tutor -match ':') { $tutor } else { "${tutor}:latest" }
    if ($instalados -notcontains $nomeTutor -and $tutor -eq 'tutoron-paa') {
        & $Ollama create tutoron-paa -f 05-modelo\Modelfile; Falhou
    }
    Ok "modelos: $tutor (tutor) e $base (genérico), embeddings bge-m3"
}

function Baixar-Cloudflared {
    if (!(Test-Path $Cloudflared)) {
        Write-Host '   Baixando cloudflared oficial (túnel público, sem administrador)...'
        Invoke-WebRequest -ErrorAction Stop 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe' -OutFile $Cloudflared
        $assinatura = Get-AuthenticodeSignature $Cloudflared
        if ($assinatura.Status -ne 'Valid' -or $assinatura.SignerCertificate.Subject -notmatch 'Cloudflare, Inc\.') {
            Remove-Item $Cloudflared -Force
            throw 'cloudflared baixado sem assinatura válida da Cloudflare. Nada foi executado.'
        }
    }
}

# ---------------------------------------------------------------- processos
$ArquivoPids = Join-Path $Dados 'processos.json'
function Salvar-Pids($pids) { $pids | ConvertTo-Json | Set-Content $ArquivoPids -Encoding utf8 }
function Parar-Tudo {
    if (Test-Path $ArquivoPids) {
        $pids = Get-Content $ArquivoPids -Raw | ConvertFrom-Json
        foreach ($p in @($pids.servidor, $pids.tunel)) {
            if ($p) { Stop-Process -Id $p -Force -ErrorAction SilentlyContinue }
        }
        Remove-Item $ArquivoPids -Force
    }
    Get-NetTCPConnection -LocalPort $Porta -State Listen -ErrorAction SilentlyContinue |
        ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
    # Túneis esquecidos de execuções anteriores (ex.: janela fechada à força).
    Get-Process cloudflared -ErrorAction SilentlyContinue |
        Where-Object { $_.Path -and $_.Path.StartsWith($Tools, [StringComparison]::OrdinalIgnoreCase) } |
        Stop-Process -Force -ErrorAction SilentlyContinue
    Remove-Item (Join-Path $Dados 'url-publica.txt') -ErrorAction SilentlyContinue
}

function Iniciar-Servidor {
    $p = Start-Process -FilePath $Python -ArgumentList '-m','uvicorn','backend.main:app','--host','127.0.0.1','--port',"$Porta",'--no-access-log' `
        -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $Logs 'servidor.log') -RedirectStandardError (Join-Path $Logs 'servidor-erros.log')
    for ($i = 0; $i -lt 60; $i++) {
        Start-Sleep -Milliseconds 500
        try { $null = Invoke-RestMethod -ErrorAction Stop "$Local/health" -TimeoutSec 2; return $p } catch { }
        if ($p.HasExited) { break }
    }
    throw "O servidor não iniciou. Veja $Logs\servidor-erros.log"
}

function Iniciar-Tunel {
    $log = Join-Path $Logs 'tunel.log'
    Remove-Item $log -ErrorAction SilentlyContinue
    $token = Ler-Env 'TUTORON_TUNEL_TOKEN'
    if ($token) {
        # Túnel nomeado (endereço fixo configurado no painel da Cloudflare).
        $p = Start-Process -FilePath $Cloudflared -ArgumentList 'tunnel','--no-autoupdate','run','--token',$token `
            -WindowStyle Hidden -PassThru -RedirectStandardError $log -RedirectStandardOutput (Join-Path $Logs 'tunel-saida.log')
        $url = Ler-Env 'TUTORON_URL_PUBLICA'
    } else {
        # Túnel rápido: endereço aleatório *.trycloudflare.com, muda a cada reinício.
        $p = Start-Process -FilePath $Cloudflared -ArgumentList 'tunnel','--no-autoupdate','--url',$Local `
            -WindowStyle Hidden -PassThru -RedirectStandardError $log -RedirectStandardOutput (Join-Path $Logs 'tunel-saida.log')
        $url = $null
        for ($i = 0; $i -lt 60 -and !$url; $i++) {
            Start-Sleep -Milliseconds 500
            if (Test-Path $log) {
                $m = Select-String -Path $log -Pattern 'https://[a-z0-9-]+\.trycloudflare\.com' | Select-Object -First 1
                if ($m) { $url = $m.Matches[0].Value }
            }
        }
    }
    if ($url) { Set-Content (Join-Path $Dados 'url-publica.txt') $url -Encoding utf8 }
    return @{ processo = $p; url = $url }
}

# Impede o Windows de suspender enquanto o servidor estiver aberto.
Add-Type -Namespace TutorON -Name Energia -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint SetThreadExecutionState(uint esFlags);' -ErrorAction SilentlyContinue
function Manter-Acordado { [void][TutorON.Energia]::SetThreadExecutionState([uint32]'0x80000001') }

function Mostrar-Enderecos($url) {
    Write-Host ''
    Write-Host '  ===================================================================' -ForegroundColor Cyan
    Write-Host '   TutorON NO AR' -ForegroundColor Cyan
    Write-Host "   Nesta máquina:     $Local"
    if ($url) { Write-Host "   Para os alunos:    $url" -ForegroundColor Green }
    else { Write-Host '   Endereço público:  indisponível (veja dados\logs\tunel.log)' -ForegroundColor Yellow }
    Write-Host "   Modo validação:    $(if ($url) { $url } else { $Local })/?modo=validacao"
    Write-Host "   Resultados:        $Local/resultados   (só nesta máquina)"
    Write-Host '   Dados recebidos:   pasta dados\'
    Write-Host '  ===================================================================' -ForegroundColor Cyan
    Write-Host '   Deixe esta janela aberta. Fechar a janela ou Ctrl+C desliga o site.' -ForegroundColor Yellow
}

$PedidoReinicio = Join-Path $Dados 'reiniciar.pedido'

function Parar-Ollama {
    Get-Process ollama, 'ollama app', llama-server -ErrorAction SilentlyContinue |
        Where-Object { $_.Path -and $_.Path.StartsWith($Tools, [StringComparison]::OrdinalIgnoreCase) } |
        Stop-Process -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 2
}

function Parar-Servidor {
    Get-NetTCPConnection -LocalPort $Porta -State Listen -ErrorAction SilentlyContinue |
        ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
}

function Servidor {
    # Uma janela por vez: duas janelas vigiando o mesmo servidor ficariam reiniciando uma à outra.
    $trava = New-Object System.Threading.Mutex($false, 'Local\TutorON-Servidor')
    if (!$trava.WaitOne(0)) {
        $url = Join-Path $Dados 'url-publica.txt'
        Aviso 'O TutorON já está rodando em outra janela.'
        if (Test-Path $url) { Mostrar-Enderecos ((Get-Content $url -Raw).Trim()) }
        Start-Process "$Local/"
        return
    }
    Preparar-Python
    Preparar-Env
    Iniciar-Ollama
    Titulo 'Site e túnel público'
    Baixar-Cloudflared
    Parar-Tudo
    Remove-Item $PedidoReinicio -ErrorAction SilentlyContinue
    $servidor = Iniciar-Servidor
    Ok "servidor em $Local"
    $tunel = Iniciar-Tunel
    Salvar-Pids @{ servidor = $servidor.Id; tunel = $tunel.processo.Id }
    Mostrar-Enderecos $tunel.url
    Start-Process "$Local/"
    $falhas = 0
    $ultimaVerificacao = [DateTime]::MinValue
    try {
        while ($true) {
            Manter-Acordado
            Start-Sleep -Seconds 3
            try {
                # Pedido do 4-Reiniciar.bat: religa Ollama e site; o túnel (e o endereço público) continua.
                if (Test-Path $PedidoReinicio) {
                    Aviso "$(Get-Date -Format HH:mm:ss) reinício pedido: religando modelos e site..."
                    Parar-Servidor
                    Parar-Ollama
                    Iniciar-Ollama
                    $servidor = Iniciar-Servidor
                    Salvar-Pids @{ servidor = $servidor.Id; tunel = $tunel.processo.Id }
                    Remove-Item $PedidoReinicio -ErrorAction SilentlyContinue
                    Ok "$(Get-Date -Format HH:mm:ss) reiniciado; o endereço público continua o mesmo"
                    $falhas = 0
                }
                if (((Get-Date) - $ultimaVerificacao).TotalSeconds -lt 15) { continue }
                $ultimaVerificacao = Get-Date
                $vivo = $true
                try { $null = Invoke-RestMethod -ErrorAction Stop "$Local/health" -TimeoutSec 10 } catch { $vivo = $false }
                if ($vivo) { $falhas = 0 } else { $falhas++ }
                # Três falhas seguidas (~45 s) antes de religar: um soluço não derruba respostas em andamento.
                if ($servidor.HasExited -or $falhas -ge 3) {
                    Aviso "$(Get-Date -Format HH:mm:ss) site sem resposta; religando..."
                    Parar-Servidor
                    $servidor = Iniciar-Servidor
                    Salvar-Pids @{ servidor = $servidor.Id; tunel = $tunel.processo.Id }
                    $falhas = 0
                    Ok 'site religado'
                }
                if ($tunel.processo.HasExited) {
                    Aviso "$(Get-Date -Format HH:mm:ss) túnel caiu; reabrindo (o endereço público pode mudar)..."
                    $tunel = Iniciar-Tunel
                    Salvar-Pids @{ servidor = $servidor.Id; tunel = $tunel.processo.Id }
                    Mostrar-Enderecos $tunel.url
                }
                try { $null = Invoke-RestMethod -ErrorAction Stop 'http://127.0.0.1:11434/api/tags' -TimeoutSec 10 }
                catch { Aviso "$(Get-Date -Format HH:mm:ss) modelo local parou; religando..."; Parar-Ollama; Iniciar-Ollama }
            } catch {
                # Nunca sair do laço por causa de um erro ao religar: tenta de novo na próxima volta.
                Aviso "$(Get-Date -Format HH:mm:ss) erro ao recuperar: $($_.Exception.Message). Tentando de novo..."
                Start-Sleep -Seconds 5
            }
        }
    } finally {
        Write-Host 'Desligando o TutorON...'
        Parar-Tudo
        $trava.ReleaseMutex()
    }
}

function Reiniciar {
    $trava = New-Object System.Threading.Mutex($false, 'Local\TutorON-Servidor')
    if ($trava.WaitOne(0)) {
        # Nenhuma janela de servidor aberta: só abrir uma.
        $trava.ReleaseMutex()
        Write-Host 'O servidor não estava ligado. Abrindo o 1-Iniciar-Servidor...'
        Start-Process -FilePath (Join-Path $Raiz '1-Iniciar-Servidor.bat')
        return
    }
    Titulo 'Reiniciando modelos e site (o endereço público continua o mesmo)'
    Set-Content $PedidoReinicio (Get-Date -Format o) -Encoding utf8
    for ($i = 0; $i -lt 300 -and (Test-Path $PedidoReinicio); $i++) { Start-Sleep -Seconds 1 }
    if (Test-Path $PedidoReinicio) { throw 'A janela do servidor não respondeu ao pedido. Feche-a e abra o 1-Iniciar-Servidor.bat.' }
    $ok = $false
    for ($i = 0; $i -lt 60 -and !$ok; $i++) {
        try { $null = Invoke-RestMethod -ErrorAction Stop "$Local/health" -TimeoutSec 5; $ok = $true } catch { Start-Sleep -Seconds 1 }
    }
    if (!$ok) { throw 'O site não voltou. Veja a janela do servidor.' }
    $url = Join-Path $Dados 'url-publica.txt'
    Ok 'TutorON reiniciado e respondendo.'
    if (Test-Path $url) { Write-Host "   Endereço público: $((Get-Content $url -Raw).Trim())" -ForegroundColor Green }
}

function Validacao {
    $rodando = $true
    try { $null = Invoke-RestMethod -ErrorAction Stop "$Local/health" -TimeoutSec 3 } catch { $rodando = $false }
    if (!$rodando) {
        Write-Host 'O servidor não está ligado. Abrindo 1-Iniciar-Servidor em outra janela...'
        Start-Process -FilePath (Join-Path $Raiz '1-Iniciar-Servidor.bat')
        for ($i = 0; $i -lt 600 -and !$rodando; $i++) {
            Start-Sleep -Seconds 1
            try { $null = Invoke-RestMethod -ErrorAction Stop "$Local/health" -TimeoutSec 2; $rodando = $true } catch { }
        }
        if (!$rodando) { throw 'O servidor não respondeu. Veja a janela do servidor.' }
    }
    $url = Join-Path $Dados 'url-publica.txt'
    $publico = if (Test-Path $url) { (Get-Content $url -Raw).Trim() } else { $Local }
    Write-Host ''
    Write-Host "  Link da validação para os alunos:  $publico/?modo=validacao" -ForegroundColor Green
    Write-Host "  Resultados (só nesta máquina):     $Local/resultados"
    Write-Host '  Avaliações completas (JSON):       dados\validacao\avaliacoes.jsonl'
    try { Set-Clipboard "$publico/?modo=validacao"; Write-Host '  (link copiado para a área de transferência)' } catch { }
    Start-Process "$Local/?modo=validacao"
    Start-Process "$Local/resultados"
}

function Treinar {
    Titulo 'Treinamento do TutorON (QLoRA na GPU)'
    Iniciar-Ollama
    $Treino = Join-Path $Raiz '.venv-treino\Scripts\python.exe'
    if (!(Test-Path $Treino)) {
        Write-Host '   Criando ambiente de treino (.venv-treino) — só na primeira vez, baixa ~3 GB...'
        if (Get-Command py -ErrorAction SilentlyContinue) { & py -3 -m venv .venv-treino } else { & python -m venv .venv-treino }
        Falhou
    }
    & $Treino -c "import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>$null
    if ($LASTEXITCODE -ne 0) {
        $indice = if ($env:TUTORON_TORCH_INDEX_URL) { $env:TUTORON_TORCH_INDEX_URL } else { 'https://download.pytorch.org/whl/cu128' }
        & $Treino -m pip install --disable-pip-version-check torch --index-url $indice; Falhou
        & $Treino -c "import torch; assert torch.cuda.is_available(), 'PyTorch sem CUDA: confira o driver NVIDIA.'"; Falhou
    }
    & $Treino -c "import transformers, peft, datasets, bitsandbytes, safetensors" 2>$null
    if ($LASTEXITCODE -ne 0) { & $Treino -m pip install --disable-pip-version-check -r 05-modelo\treino\requirements.txt; Falhou }
    & $Treino scripts\treinar.py @Extra; Falhou
}

switch ($Acao) {
    'Servidor'  { Servidor }
    'Validacao' { Validacao }
    'Treinar'   { Treinar }
    'Reiniciar' { Reiniciar }
    'Parar'     {
        # Fecha também a janela do 1-Iniciar-Servidor (senão ela religa o servidor).
        Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
            Where-Object { $_.ProcessId -ne $PID -and $_.CommandLine -match 'tutoron\.ps1' -and $_.CommandLine -match 'Servidor' } |
            ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
        Parar-Tudo; Parar-Ollama; Ok 'servidor, túnel e modelo local desligados'
    }
    'Testar'    {
        Preparar-Python
        & $Python -m pytest backend\tests tests_acervo -q -p no:cacheprovider; Falhou
    }
    'Acervo'    {
        Preparar-Python
        & $Python -m pip install --disable-pip-version-check -q -r requirements-acervo.txt; Falhou
        Iniciar-Ollama
        & $Python -m acervo pipeline --embeddings; Falhou
    }
}
