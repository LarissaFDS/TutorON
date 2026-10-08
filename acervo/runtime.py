"""Configuração portátil; variáveis explícitas prevalecem sobre o perfil local."""
import os

from .common import ROOT, read_json, write_json


def settings():
    saved = read_json(ROOT / '.tools/runtime.json', {})
    return {
        'base_model': os.environ.get('TUTORON_BASE_MODEL', saved.get('base_model', 'qwen2.5:3b')),
        'tutor_model': os.environ.get('TUTORON_MODEL', saved.get('tutor_model', 'tutoron-paa')),
        'num_ctx': int(os.environ.get('TUTORON_NUM_CTX', saved.get('num_ctx', 4096))),
        'seed': int(os.environ.get('TUTORON_SEED', saved.get('seed', 42))),
        'timeout': int(os.environ.get('TUTORON_TIMEOUT', saved.get('timeout', 900))),
    }


def prepare():
    from .models import SYSTEM
    profile = settings()
    write_json(ROOT / '.tools/runtime.json', profile)
    (ROOT / '.tools/Modelfile.local').write_text(
        f'FROM {profile["base_model"]}\nPARAMETER num_ctx {profile["num_ctx"]}\n'
        f'PARAMETER temperature 0.2\nSYSTEM """{SYSTEM}"""\n', encoding='utf-8')
    print('Perfil local:', profile, flush=True)


if __name__ == '__main__':
    prepare()
