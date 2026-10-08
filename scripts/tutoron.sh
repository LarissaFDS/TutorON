#!/usr/bin/env bash
# Equivalente Linux de scripts/tutoron.ps1: mesmas ações, mesmas pastas e saídas.
# Uso: scripts/tutoron.sh [Preparar|Pipeline|Visao|Modelos|Avaliar|Validar|Resumo|Testar|Dataset]
set -euo pipefail

acao="${1:-Validar}"
case "$acao" in
    Preparar|Pipeline|Visao|Modelos|Avaliar|Validar|Resumo|Testar|Dataset) ;;
    *) echo "Ação desconhecida: $acao" >&2
       echo "Use: Preparar, Pipeline, Visao, Modelos, Avaliar, Validar, Resumo, Testar ou Dataset." >&2
       exit 2 ;;
esac

raiz="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$raiz"
export PYTHONUTF8=1
export UV_CACHE_DIR="$raiz/.uv-cache"
if [ -x "$raiz/.tools/tesseract/usr/bin/tesseract" ]; then
    export PATH="$raiz/.tools/tesseract/usr/bin:$PATH"
    export LD_LIBRARY_PATH="$raiz/.tools/tesseract/usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH:-}"
    export TESSDATA_PREFIX="$raiz/.tools/tesseract/usr/share/tesseract-ocr/5/tessdata"
fi
python_tutor="$raiz/.venv-acervo/bin/python"

falha() { echo "ERRO: $*" >&2; exit 1; }

setup_python() {
    if [ ! -x "$python_tutor" ]; then
        if command -v uv >/dev/null 2>&1; then
            uv venv .venv-acervo --python 3.12
        elif command -v python3 >/dev/null 2>&1; then
            python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' \
                || falha 'Python 3.10+ necessário (recomendado 3.12). Instale-o ou instale o uv.'
            python3 -m venv .venv-acervo \
                || falha 'Não foi possível criar .venv-acervo. No Ubuntu/Debian: sudo apt install python3-venv'
        else
            falha 'Instale Python 3.12+ (ex.: sudo apt install python3 python3-venv) ou uv e execute novamente.'
        fi
    fi
    if ! "$python_tutor" -c "import importlib.util,sys; sys.exit(0 if all(importlib.util.find_spec(m) for m in ('pymupdf','PIL','pytesseract','pytest','rapidocr_onnxruntime')) else 1)" \
            || [ "$acao" = Preparar ]; then
        if command -v uv >/dev/null 2>&1; then
            uv pip install --python "$python_tutor" -r requirements-acervo.txt
        else
            "$python_tutor" -m pip install -r requirements-acervo.txt
        fi
    fi
}

api_ollama() { curl -fsS --max-time "${1:-3}" http://127.0.0.1:11434/api/tags >/dev/null 2>&1; }

setup_ollama() {
    command -v curl >/dev/null 2>&1 || falha 'Instale o curl (sudo apt install curl).'
    export OLLAMA_MODELS="$raiz/.tools/models"
    export OLLAMA_HOST='127.0.0.1:11434'
    export OLLAMA_NUM_PARALLEL='1'
    local ollama_tutor
    if command -v ollama >/dev/null 2>&1; then
        ollama_tutor="$(command -v ollama)"  # instalação do sistema
    else
        ollama_tutor="$(find "$raiz/.tools/ollama" -type f -name ollama -perm -u+x 2>/dev/null | head -n 1 || true)"
        if [ -z "$ollama_tutor" ]; then
            # Mesma versão do Windows; hashes publicados pelo GitHub na release v0.34.4.
            local arquivo hash
            case "$(uname -m)" in
                x86_64|amd64) arquivo='ollama-linux-amd64.tar.zst'
                              hash='c238986e61d40c0cc5f4a9b9e40b9eea104350b77efa34741fc134e105cb9533' ;;
                aarch64|arm64) arquivo='ollama-linux-arm64.tar.zst'
                               hash='96f50a1192133028cf4e010d8c333f8af14b1505db6be7b2034c11487e7fd7e6' ;;
                *) falha "Arquitetura $(uname -m) sem pacote do Ollama; instale-o pelo site oficial." ;;
            esac
            command -v zstd >/dev/null 2>&1 || falha 'Instale o zstd para descompactar o Ollama (sudo apt install zstd).'
            echo 'Baixando Ollama portátil oficial (~1,4 GB), sem administrador...'
            mkdir -p .tools/ollama
            if [ ! -f ".tools/$arquivo" ]; then
                curl -fL --retry 3 -o ".tools/$arquivo.part" \
                    "https://github.com/ollama/ollama/releases/download/v0.34.4/$arquivo"
                mv ".tools/$arquivo.part" ".tools/$arquivo"
            fi
            echo "$hash  .tools/$arquivo" | sha256sum -c --quiet - \
                || falha 'Hash inesperado no download do Ollama. Nenhum binário executado.'
            tar --zstd -xf ".tools/$arquivo" -C .tools/ollama
            ollama_tutor="$(find "$raiz/.tools/ollama" -type f -name ollama -perm -u+x | head -n 1)"
            [ -n "$ollama_tutor" ] || falha 'Executável do Ollama não encontrado no pacote extraído.'
        fi
    fi
    if ! api_ollama 3; then
        mkdir -p .tools
        nohup "$ollama_tutor" serve >.tools/ollama-server.log 2>.tools/ollama-server-error.log &
        local pronto=0
        for _ in $(seq 30); do
            sleep 1
            if api_ollama 2; then pronto=1; break; fi
        done
        [ "$pronto" = 1 ] || falha 'Ollama não iniciou. Veja .tools/ollama-server-error.log.'
    fi
    if [ "$acao" = Modelos ]; then
        for modelo in "${TUTORON_BASE_MODEL:-qwen2.5:3b}" qwen2.5vl:3b bge-m3; do
            "$ollama_tutor" pull "$modelo"
        done
        "$python_tutor" -m acervo.runtime
        "$ollama_tutor" create "${TUTORON_MODEL:-tutoron-paa}" -f .tools/Modelfile.local
    fi
}

abrir_navegador() {
    if command -v xdg-open >/dev/null 2>&1 && { [ -n "${DISPLAY:-}" ] || [ -n "${WAYLAND_DISPLAY:-}" ]; }; then
        xdg-open "$1" >/dev/null 2>&1 &
    else
        echo "Abra no navegador: $1"
    fi
}

setup_python
case "$acao" in
    Preparar) echo 'Dependências prontas.' ;;
    Modelos) setup_ollama ;;
    Pipeline) "$python_tutor" -m acervo pipeline ;;
    Visao) setup_ollama; "$python_tutor" -m acervo pipeline --visao --embeddings ;;
    Avaliar)
        setup_ollama
        if [ "${TUTORON_TRIAGE_AI:-0}" = 1 ]; then
            "$python_tutor" -m acervo triar --ia
        else
            "$python_tutor" -m acervo triar
        fi
        "$python_tutor" -m acervo indexar --embeddings
        "$python_tutor" -m acervo avaliar --gerar
        "$python_tutor" -m acervo.benchmark_report
        "$python_tutor" -m acervo offline ;;
    Validar)
        setup_ollama
        [ -f 07-validacao-alunos/pares.json ] || "$python_tutor" -m acervo pipeline
        if curl -fsS --max-time 2 http://127.0.0.1:8765/api/questoes 2>/dev/null | grep -q '"questoes"'; then
            abrir_navegador 'http://127.0.0.1:8765'
            echo 'TutorON já estava em execução. Aberto no navegador.'
        else
            # O servidor ocupa o terminal; o navegador abre logo depois que ele sobe.
            (for _ in $(seq 20); do
                sleep 0.5
                if curl -fsS --max-time 1 http://127.0.0.1:8765/api/questoes >/dev/null 2>&1; then
                    abrir_navegador 'http://127.0.0.1:8765'; break
                fi
             done) &
            "$python_tutor" -m acervo servir
        fi ;;
    Resumo) "$python_tutor" -m acervo resumo ;;
    Dataset)
        "$python_tutor" -m acervo triar
        "$python_tutor" -m acervo relatorio
        echo 'Dataset atualizado em 05-modelo/dataset-finetuning.jsonl. Somente pares aprovados são exportados.' ;;
    Testar)
        mkdir -p tmp  # o pytest não cria a pasta-mãe do --basetemp
        "$python_tutor" -m pytest tests_acervo -q \
            --basetemp "$raiz/tmp/pytest-$(date +%s)-$$" -o cache_dir=tmp/pytest-cache ;;
esac
