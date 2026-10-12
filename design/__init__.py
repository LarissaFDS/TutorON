"""Design system do TutorON: tokens, base e componentes em CSS puro.

Não há bundler no projeto. Este módulo junta os arquivos na ordem certa
para quem precisa deles:

- ``backend/main.py`` serve ``/design.css`` para o site (modo Tutor e Validação).
- ``legado/poc-gemini/run_demo.py`` embute o CSS no relatório HTML da PoC antiga.

Para mudar cor, tipo, espaço ou raio, edite ``design/tokens/``. Regras e
motivos estão em ``docs/DESIGN.md``.
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
