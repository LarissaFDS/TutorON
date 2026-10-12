"""Guarda do design system: tokens definidos e site sem dependências externas."""
import re
from pathlib import Path

from design import HERE as DESIGN, stylesheet

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / 'backend/web'


def test_every_css_variable_used_is_defined():
    css = stylesheet('report.css')
    pages = ''.join((WEB / name).read_text(encoding='utf-8') for name in ('index.html', 'resultados.html', 'app.css'))
    report = (ROOT / 'legado/poc-gemini/run_demo.py').read_text(encoding='utf-8')
    defined = set(re.findall(r'(--[a-z0-9-]+)\s*:', css))
    used = set(re.findall(r'var\((--[a-z0-9-]+)', css + pages + report))
    assert used - defined == set(), 'Tokens usados sem definição em design/tokens/'


def test_type_scale_has_five_sizes():
    typography = (DESIGN / 'tokens/typography.css').read_text(encoding='utf-8')
    assert len(re.findall(r'--text-[a-z]+\s*:', typography)) == 5


def test_site_loads_only_local_assets():
    for page in ('index.html', 'resultados.html'):
        html = (WEB / page).read_text(encoding='utf-8')
        assert not re.search(r'(src|href)="https?://', html), 'O site precisa funcionar sem CDN.'
        for asset in re.findall(r'(?:src|href)="/static/([^"]*)"', html):
            assert (WEB / asset).is_file(), asset


def test_site_keeps_api_contract():
    js = (WEB / 'app.js').read_text(encoding='utf-8')
    for fragment in ["'/api/perguntar'", "'/api/comparar'", "'/api/avaliar'", "'/api/feedback'", 'preferida', 'sessao',
                     'erro_matematico']:
        assert fragment in js
    for criterion in ['clareza', 'confianca', 'utilidade']:
        assert f"'{criterion}'" in js
