#!/usr/bin/env bash
# Pacotes oficiais Ubuntu 24.04, extraídos localmente sem sudo.
set -euo pipefail
cd "$(dirname "$0")"
if [ -x .tools/tesseract/usr/bin/tesseract ] || command -v tesseract >/dev/null 2>&1; then
    echo 'Tesseract já disponível. Confirme idiomas com tesseract --list-langs.'
    exit 0
fi
command -v apt-get >/dev/null 2>&1 || { echo 'Sem apt-get: use Tesseract do sistema ou o fallback RapidOCR.'; exit 1; }
mkdir -p .tools/tesseract-packages .tools/tesseract
cd .tools/tesseract-packages
apt-get download tesseract-ocr tesseract-ocr-por tesseract-ocr-eng tesseract-ocr-osd libtesseract5 liblept5 libarchive13t64
for package in *.deb; do dpkg-deb -x "$package" ../tesseract; done
echo 'OCR portátil pronto; os scripts e o módulo acervo configuram seu caminho.'
