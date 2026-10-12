# Loads variables from .env into the current PowerShell session.
# Usage (dot-source, from the project root):
#   . .\scripts\load-env.ps1

Get-Content (Join-Path $PSScriptRoot "..\.env") | ForEach-Object {
    if ($_ -match '^([A-Z_]+)=(.*)$') {
        [System.Environment]::SetEnvironmentVariable($matches[1], $matches[2])
    }
}

Write-Host "Variaveis de .env carregadas na sessao atual."
