"""Amostra impressa controlada; não certifica OCR de manuscritos ou diagramas."""
import base64
import json
import sys
import time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from acervo import models
from acervo.common import ROOT, digest, write_json


def main():
    lines = ['VALIDACAO OCR TUTORON', 'ASTERISCO(3) = 11', 'A(n) = 2*A(n-1) + n']
    img = Image.new('RGB', (900, 240), 'white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default(size=38)
    for i, line in enumerate(lines):
        draw.text((30, 25+i*65), line, font=font, fill='black')
    path = ROOT / '.tools/ocr-visao-impressa.png'
    img.save(path)
    result = {'modelo': 'qwen2.5vl:3b', 'entrada_sha256': digest(path.read_bytes()),
              'esperado': lines, 'limite': 'Uma imagem impressa sintética; não generaliza para fotos, manuscritos ou figuras.'}
    begin = time.monotonic()
    try:
        answer = models.local('Transcreva literalmente as três linhas da imagem. Retorne somente o texto, sem resolver ou explicar.',
            system='Você é um transcritor de OCR. Preserve números e símbolos; não invente conteúdo.',
            model=result['modelo'], images=[base64.b64encode(path.read_bytes()).decode('ascii')],
            num_predict=256, options={'temperature': 0, 'repeat_penalty': 1.15})
        normalized = ''.join(answer.lower().split())
        matches = [line for line in lines if ''.join(line.lower().split()) in normalized]
        result.update(status='ok', texto=answer, linhas_conferem=len(matches), linhas_total=len(lines))
    except Exception as exc:
        result.update(status='falhou', erro=type(exc).__name__ + ': ' + str(exc)[:180])
    result['segundos'] = time.monotonic()-begin
    write_json(ROOT / '06-avaliacao/visao-impressa.json', result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
