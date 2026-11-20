# Limpa arquivos gerados que não vão para o Git (caches, pytest, temporários).
# Uso: powershell -File scripts/limpar.ps1            -> só mostra o que seria apagado
#      powershell -File scripts/limpar.ps1 -Apagar    -> apaga
# Nunca toca em dados/ (dados de alunos), .env, .tools/ (modelos) nem nos ambientes .venv*.
param([switch]$Apagar)
$raiz = Split-Path $PSScriptRoot -Parent
$alvos = @()
$alvos += Get-ChildItem $raiz -Recurse -Directory -Force -Include __pycache__, .pytest_cache -ErrorAction SilentlyContinue |
  Where-Object { $_.FullName -notmatch '[\\/](\.venv[^\\/]*|\.tools|dados)[\\/]' }
$alvos += Get-ChildItem (Join-Path $raiz 'tmp') -Force -ErrorAction SilentlyContinue
$alvos += Get-Item (Join-Path $raiz '.uv-cache') -ErrorAction SilentlyContinue
foreach ($a in $alvos) {
  if ($Apagar) { Remove-Item $a.FullName -Recurse -Force -Confirm:$false; "apagado: $($a.FullName)" }
  else { "seria apagado: $($a.FullName)" }
}
if (-not $Apagar) { "`nNada foi apagado. Rode de novo com -Apagar para apagar." }
