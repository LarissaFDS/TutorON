"""Regressões de OCR real, proveniência e comparação com modelos distintos."""
import shutil

import pytest

from acervo import models
from acervo.common import ROOT, init, digest, write_json, read_json
from acervo.curate import apply_corrections, organize
from acervo.extract import configure_ocr, image_text, inventory, extract


@pytest.mark.parametrize('suffix', ['png', 'jpg', 'webp', 'bmp', 'tiff', 'gif'])
def test_real_printed_ocr_in_supported_formats(tmp_path, suffix):
    from PIL import Image, ImageDraw, ImageFont
    configure_ocr()
    if not shutil.which('tesseract'):
        pytest.skip('Integração requer Tesseract português; RapidOCR é testado separadamente.')
    font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    if not __import__('pathlib').Path(font_path).exists():
        pytest.skip('Fonte da imagem de referência indisponível neste sistema.')
    image = Image.new('RGB', (1400, 400), 'white')
    font = ImageFont.truetype(font_path, 45)
    ImageDraw.Draw(image).multiline_text((50, 50), 'Algoritmo de busca binaria\nComplexidade logaritmica\nCertificado verificavel', font=font, fill='black', spacing=20)
    path = tmp_path / ('prova.' + suffix)
    image.save(path)
    with Image.open(path) as source:
        text, method, quality = image_text(source)
    assert 'binaria' in text.lower() and 'certificado' in text.lower()
    assert method == 'tesseract-por' and quality == 'parcial'


def test_multiframe_tiff_preserves_all_pages(tmp_path, monkeypatch):
    from PIL import Image
    init(tmp_path)
    folder = tmp_path / 'materiais'
    folder.mkdir()
    first = Image.new('RGB', (200, 200), 'white')
    second = Image.new('RGB', (200, 200), 'black')
    first.save(folder / 'prova.tiff', save_all=True, append_images=[second])
    monkeypatch.setattr('acervo.extract.image_text', lambda im, *_: ('página clara' if im.getpixel((0,0))[0] else 'página escura', 'teste', 'parcial'))
    inv = inventory(tmp_path)
    docs = extract(tmp_path)
    assert inv[0]['paginas'] == 2
    assert [p['texto'] for p in docs[0]['paginas_extraidas']] == ['página clara', 'página escura']


def test_correction_invalidates_when_original_changes(tmp_path):
    init(tmp_path)
    path = tmp_path / '03-triagem/correcao.md'
    path.write_text('NP usa certificados verificáveis.', encoding='utf-8')
    write_json(tmp_path / '03-triagem/correcoes.json', {'q': {'sha256_original': digest('original'), 'sha256_fonte': digest('fonte.pdf'), 'arquivo': '03-triagem/correcao.md'}})
    item = {'id': 'q', 'texto': 'original', 'sha256': digest('original'), 'sha256_fonte': digest('fonte.pdf'), 'arquivo': '02-acervo/q.md', 'fonte_original': 'fonte.pdf'}
    apply_corrections([item], tmp_path)
    assert item['texto_original'] == 'original' and item['sha256_original'] == digest('original')
    changed = {**item, 'texto': 'nova fonte', 'sha256': digest('nova fonte')}
    apply_corrections([changed], tmp_path)
    assert changed['texto'] == 'nova fonte' and changed['curadoria']['status'] == 'fonte_alterada'
    changed_image = {**item, 'texto': 'original', 'sha256': digest('original'), 'sha256_fonte': digest('nova imagem')}
    apply_corrections([changed_image], tmp_path)
    assert changed_image['texto'] == 'original' and changed_image['curadoria']['status'] == 'fonte_alterada'


def test_absent_document_cannot_reenter_index_via_old_extraction(tmp_path):
    init(tmp_path)
    write_json(tmp_path / '03-triagem/inventario.json', [])
    write_json(tmp_path / '01-extraido/stale.json', {'id': 'stale', 'sha256': 'old'})
    assert organize(tmp_path) == []


def test_named_tutor_base_and_prompt_control_share_sampling(monkeypatch):
    captured = []
    def fake_post(url, payload, timeout):
        captured.append(payload)
        return {'response': 'Resposta completa.', 'done_reason': 'stop'}
    monkeypatch.setattr(models, 'post', fake_post)
    monkeypatch.setenv('TUTORON_BASE_MODEL', 'base:test')
    monkeypatch.setenv('TUTORON_MODEL', 'tutor:test')
    models.generate('Pergunta', provider='ollama', structured=False)
    models.generate('Pergunta', provider='ollama', model='base:test')
    models.generate('Pergunta', 'contexto', provider='ollama')
    assert [p['model'] for p in captured] == ['base:test', 'base:test', 'tutor:test']
    assert captured[0]['system'] == ''
    assert captured[1]['system'] == captured[2]['system'] == models.SYSTEM
    assert captured[0]['options'] == captured[1]['options'] == captured[2]['options']


def test_every_curated_source_hash_matches():
    manifest = read_json(ROOT / '03-triagem/correcoes.json', {})
    items = {i['id']: i for i in read_json(ROOT / '02-acervo/itens.json', [])}
    for identifier, correction in manifest.items():
        assert items[identifier]['sha256_original'] == correction['sha256_original']
        assert digest(items[identifier]['texto']) == items[identifier]['sha256']
