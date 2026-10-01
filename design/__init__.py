"""Design system do TutorON: tokens, base e componentes em CSS puro.

Não há bundler no projeto. Este módulo junta os arquivos na ordem certa
para quem precisa deles:

- ``acervo/app.py`` serve ``/design.css`` e ``/text.js`` para a página de
  validação (funciona offline).
- ``run_demo.py`` embute o CSS no relatório HTML, que é um arquivo avulso.

Para mudar cor, tipo, espaço ou raio, edite ``design/tokens/``. Regras e
motivos estão em ``DESIGN.md`` na raiz.
"""
from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent

# Ordem importa: tokens primeiro, depois base, depois componentes.
LAYERS = (
    'tokens/colors.css',
    'tokens/typography.css',
    'tokens/spacing.css',
    'tokens/shape.css',
    'base.css',
    'components.css',
)


def stylesheet(*extra: str) -> str:
    """CSS completo do design system, com camadas extras opcionais (ex.: 'report.css')."""
    parts = []
    for name in LAYERS + extra:
        parts.append(f'/* ---- design/{name} ---- */\n' + (HERE / name).read_text(encoding='utf-8'))
    return '\n'.join(parts)


def script(name: str = 'text.js') -> str:
    return (HERE / name).read_text(encoding='utf-8')
