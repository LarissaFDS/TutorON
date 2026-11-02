"""Mesma aplicação, modelo local forçado e dados isolados; nunca altera o .env."""
import dataclasses
import os
from pathlib import Path

from backend.config import ROOT_DIR, load_settings
from backend.main import create_app


def criar():
    pensar = os.environ.get('AUDITORIA_RACIOCINIO', '1') == '1'
    pasta = Path(os.environ.get('AUDITORIA_DADOS', str(ROOT_DIR / 'dados/auditoria-local')))
    config = dataclasses.replace(load_settings(), gemini_api_key='', gemini_models=(),
                                 data_dir=pasta, local_thinking=pensar)
    return create_app(settings=config, warm_up=False)


def criar_rapido():
    config = dataclasses.replace(load_settings(), gemini_api_key='', gemini_models=(),
                                 data_dir=ROOT_DIR / 'dados/auditoria-rapido', local_thinking=False)
    return create_app(settings=config, warm_up=False)
