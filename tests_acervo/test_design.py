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
        html = re.sub(r'<meta [^>]*>', '', html)  # og:image/og:url são absolutos por exigência dos apps
        assert not re.search(r'(src|href)="https?://', html), 'O site precisa funcionar sem CDN.'
        for asset in re.findall(r'(?:src|href)="/static/([^"]*)"', html):
            from urllib.parse import urlsplit
            assert (WEB / urlsplit(asset).path).is_file(), asset


def test_site_keeps_api_contract():
    js = (WEB / 'app.js').read_text(encoding='utf-8')
    for fragment in ["'/api/perguntar'", "'/api/comparar'", "'/api/avaliar'", "'/api/feedback'", 'preferida', 'sessao',
                     'erro_matematico']:
        assert fragment in js
    for criterion in ['clareza', 'confianca', 'utilidade']:
        assert f"'{criterion}'" in js


def test_tutor_history_markup_is_local_and_accessible():
    """Conversas na barra lateral: lista com botão acessível, só na memória da página."""
    html = (WEB / 'index.html').read_text(encoding='utf-8')
    js = (WEB / 'app.js').read_text(encoding='utf-8')
    assert 'id="historico-botao"' in html and 'aria-controls="historico"' in html and 'aria-expanded="false"' in html
    assert re.search(r'<ol[^>]*id="historico"[^>]*hidden', html), 'Lista começa fechada (sem conversas).'
    assert "'Conversas ('" in js and "'Mostrar conversas ('" in js
    # Conversas só em memória: recarregar a página zera. Nada novo vem da internet.
    assert 'localStorage' not in js
    assert not re.search(r'https?://', js), 'app.js não pode buscar nada fora do TutorON.'


def test_chat_css_define_its_own_tokens():
    css = (WEB / 'chat.css').read_text(encoding='utf-8')
    defined = set(re.findall(r'(--[a-z0-9-]+)\s*:', css))
    used = set(re.findall(r'var\((--[a-z0-9-]+)', css))
    assert used - defined == set()
