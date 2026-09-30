param([ValidateSet('Preparar','Pipeline','Visao','Modelos','Avaliar','Validar','Resumo','Testar','Dataset')][string]$Acao = 'Validar')
$ErrorActionPreference = 'Stop'
$raizTutor = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $raizTutor
$env:PYTHONUTF8 = '1'
$env:UV_CACHE_DIR = Join-Path $raizTutor '.uv-cache'
$pythonTutor = Join-Path $raizTutor '.venv-acervo\Scripts\python.exe'

function Check-Native { if ($LASTEXITCODE -ne 0) { throw "Comando falhou (codigo $LASTEXITCODE). Consulte a mensagem acima." } }
function Setup-Python {
    if (!(Test-Path -LiteralPath $pythonTutor)) {
        if (Get-Command uv -ErrorAction SilentlyContinue) {
            & uv venv .venv-acervo --python 3.12
            Check-Native
        } elseif (Get-Command py -ErrorAction SilentlyContinue) {
            & py -3 -m venv .venv-acervo
            Check-Native
        } elseif (Get-Command python -ErrorAction SilentlyContinue) {
            & python -m venv .venv-acervo
            Check-Native
        } else { throw 'Instale Python 3.12+ (python.org) ou uv e execute novamente.' }
    }
    & $pythonTutor -c "import importlib.util,sys; sys.exit(0 if all(importlib.util.find_spec(m) for m in ('pymupdf','PIL','pytesseract','pytest','rapidocr_onnxruntime')) else 1)"
    if ($LASTEXITCODE -ne 0 -or $Acao -eq 'Preparar') {
        if (Get-Command uv -ErrorAction SilentlyContinue) { & uv pip install --python $pythonTutor -r requirements-acervo.txt }
        else { & $pythonTutor -m pip install -r requirements-acervo.txt }
        Check-Native
    }
}

function Setup-Ollama {
    $ollamaTutor = Join-Path $raizTutor '.tools\ollama\ollama.exe'
    if (!(Test-Path -LiteralPath $ollamaTutor)) {
        Write-Host 'Baixando Ollama portatil oficial (1,46 GB), sem administrador...'
        New-Item -ItemType Directory -Force .tools\ollama | Out-Null
        $zipTutor = Join-Path $raizTutor '.tools\ollama-windows-amd64.zip'
        if (!(Test-Path -LiteralPath $zipTutor)) {
            Invoke-WebRequest 'https://github.com/ollama/ollama/releases/download/v0.34.4/ollama-windows-amd64.zip' -OutFile $zipTutor
        }
        if ((Get-FileHash -LiteralPath $zipTutor -Algorithm SHA256).Hash -ne '535193f38f3344e5b08f5d1c171c31ce11aa17f0124ff69ae26d8ec7fe06fa62') { throw 'Hash inesperado no download do Ollama. Nenhum binario executado.' }
        Expand-Archive -LiteralPath $zipTutor -DestinationPath .tools\ollama
    }
    $env:OLLAMA_MODELS = Join-Path $raizTutor '.tools\models'
    $env:OLLAMA_HOST = '127.0.0.1:11434'
    $env:OLLAMA_NUM_PARALLEL = '1'
    try { $null = Invoke-RestMethod 'http://127.0.0.1:11434/api/tags' -TimeoutSec 3 }
    catch {
        Start-Process -FilePath $ollamaTutor -ArgumentList 'serve' -WindowStyle Hidden -RedirectStandardOutput (Join-Path $raizTutor '.tools\ollama-server.log') -RedirectStandardError (Join-Path $raizTutor '.tools\ollama-server-error.log')
        $pronto = $false
        for ($tentativaTutor=0; $tentativaTutor -lt 30; $tentativaTutor++) {
            Start-Sleep -Seconds 1
            try { $null = Invoke-RestMethod 'http://127.0.0.1:11434/api/tags' -TimeoutSec 2; $pronto = $true; break } catch { }
        }
        if (!$pronto) { throw 'Ollama nao iniciou. Veja .tools\ollama-server-error.log.' }
    }
    if ($Acao -eq 'Modelos') {
        foreach ($modeloTutor in @('qwen2.5:7b','qwen2.5vl:3b','bge-m3')) {
            & $ollamaTutor pull $modeloTutor
            Check-Native
        }
        & $ollamaTutor create tutoron-paa -f 05-modelo\Modelfile
        Check-Native
    }
}

Setup-Python
switch ($Acao) {
    'Preparar' { Write-Host 'Dependencias prontas.' }
    'Modelos' { Setup-Ollama }
    'Pipeline' { & $pythonTutor -m acervo pipeline; Check-Native }
    'Visao' { Setup-Ollama; & $pythonTutor -m acervo pipeline --visao --embeddings; Check-Native }
    'Avaliar' { Setup-Ollama; & $pythonTutor -m acervo triar --ia; Check-Native; & $pythonTutor -m acervo indexar --embeddings; Check-Native; & $pythonTutor -m acervo avaliar --gerar; Check-Native; & $pythonTutor -m acervo offline; Check-Native }
    'Validar' {
        if (!(Test-Path '07-validacao-alunos\pares.json')) { & $pythonTutor -m acervo pipeline; Check-Native }
        $instanciaTutor = $false
        try { $estadoTutor = Invoke-RestMethod 'http://127.0.0.1:8765/api/questoes' -TimeoutSec 2; $instanciaTutor = $null -ne $estadoTutor.questoes } catch { }
        Start-Process 'http://127.0.0.1:8765'
        if ($instanciaTutor) { Write-Host 'TutorON ja estava em execucao. Aberto no navegador.' }
        else { & $pythonTutor -m acervo servir; Check-Native }
    }
    'Resumo' { & $pythonTutor -m acervo resumo; Check-Native }
    'Dataset' { & $pythonTutor -m acervo triar; Check-Native; & $pythonTutor -m acervo relatorio; Check-Native; Write-Host 'Dataset atualizado em 05-modelo\dataset-finetuning.jsonl. Somente pares aprovados sao exportados.' }
    'Testar' { $testeTempTutor = Join-Path $raizTutor ('tmp\pytest-' + [guid]::NewGuid().ToString('N')); & $pythonTutor -m pytest tests_acervo -q --basetemp $testeTempTutor -o cache_dir=tmp/pytest-cache; Check-Native }
}
