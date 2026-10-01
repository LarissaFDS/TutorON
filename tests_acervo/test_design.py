"""Guarda do design system: tokens definidos, página offline e renderizador seguro."""
import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

from acervo.app import WEB, pages
from design import HERE as DESIGN, stylesheet

ROOT = Path(__file__).resolve().parents[1]


def test_every_css_variable_used_is_defined():
    css = stylesheet('report.css')
    page = (WEB / 'validacao.html').read_text(encoding='utf-8')
    report = (ROOT / 'run_demo.py').read_text(encoding='utf-8')
    defined = set(re.findall(r'(--[a-z0-9-]+)\s*:', css))
    used = set(re.findall(r'var\((--[a-z0-9-]+)', css + page + report))
    assert used - defined == set(), 'Tokens usados sem definição em design/tokens/'


def test_type_scale_has_five_sizes():
    typography = (DESIGN / 'tokens/typography.css').read_text(encoding='utf-8')
    assert len(re.findall(r'--text-[a-z]+\s*:', typography)) == 5


def test_validation_page_is_offline_and_serves_closed_asset_list():
    static = pages()
    assert set(static) == {'/', '/design.css', '/text.js'}
    html = static['/'][0].decode('utf-8')
    assert not re.search(r'(src|href)="https?://', html), 'A validação com alunos precisa funcionar sem internet.'
    for asset in re.findall(r'(?:src|href)="(/[^"]*)"', html):
        assert asset in static


def test_validation_page_keeps_api_contract():
    html = (WEB / 'validacao.html').read_text(encoding='utf-8')
    for fragment in ["'/api/questoes'", "'/api/comparar'", "'/api/votar'", 'ao_vivo', 'preferida', 'sessao']:
        assert fragment in html
    for criterion in ['clareza', 'confianca', 'utilidade']:
        assert f"'{criterion}'" in html


@pytest.mark.skipif(shutil.which('node') is None, reason='Node.js não instalado')
def test_answer_renderer_escapes_html_and_renders_markdown():
    script = (DESIGN / 'text.js').read_text(encoding='utf-8')
    probe = script + '\nconsole.log(JSON.stringify(TutorONText.toHtml(process.argv[1])));'
    source = '### Caso base\n**negrito** <img src=x onerror=alert(1)> e \\( T(n) \\le 2^{n} \\)\n\n1. um\n   - dois'
    out = subprocess.run(['node', '-e', probe, source], capture_output=True, text=True, check=True).stdout
    html = json.loads(out)
    assert '<img' not in html and '&lt;img' in html
    assert '<h4>Caso base</h4>' in html  # ### vira h4: a resposta não compete com os títulos da página
    assert '<strong>negrito</strong>' in html
    assert '≤' in html and '<sup>n</sup>' in html
    assert '<ol><li>um<ul><li>dois</li></ul></li></ol>' in html
