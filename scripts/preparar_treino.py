"""Exporta dados de agente separados por família; não inicia treinamento."""
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from acervo.common import ROOT, digest, read_json, write_json
from acervo.models import SYSTEM

RESERVED = {'c01', 'c02', 'c05', 'c06', 'c08', 'c09', 'a177bf5bc3c7-q1-1', 'a177bf5bc3c7-q2-2',
            '1a81ca283132-q4-4', '70d6475b28bf-q1-1', '97254bb4a1b8-q1-1', 'd455baef2cdf-q1-1',
            '97254bb4a1b8-q2-2', '97254bb4a1b8-q10-10'}


def prepare(root=ROOT):
    folder = root / '05-modelo/treino'
    folder.mkdir(parents=True, exist_ok=True)
    samples, held = [], []
    for item in read_json(root / '02-acervo/itens.json', []):
        if item.get('curadoria', {}).get('status') != 'corrigido_por_agente':
            continue
        # Todas as questões de NP estão reservadas: evitamos treinar conceitos
        # de Q3/Q4/Q11 mesmo em uma formulação diferente.
        if item['id'] in RESERVED or item['id'].startswith('f38bb8142136'):
            held.append(item['id'])
            continue
        text = item['texto']
        family = item['id']  # Cada problema curado tem uma família, sem variantes duplicadas.
        samples.append({'family': family, 'fonte_id': item['id'], 'sha256': item['sha256'],
                        'sha256_fonte': item['sha256_fonte'],
                        'qualidade': 'silver: correção por agente; revisão humana pendente',
                        'prompt': [{'role': 'system', 'content': SYSTEM},
                                   {'role': 'user', 'content': text.split('\n', 1)[0]}],
                        'completion': [{'role': 'assistant', 'content': text}]})
    # Determinístico por família, nunca por fragmentos de uma mesma solução.
    samples.sort(key=lambda s: digest(s['family']))
    n_eval = max(2, len(samples) // 5)
    groups = {'validacao': samples[:n_eval], 'treino': samples[n_eval:]}
    for name, rows in groups.items():
        (folder / f'{name}.jsonl').write_text(''.join(json.dumps(s, ensure_ascii=False) + '\n' for s in rows), encoding='utf-8')
    gpu = None
    if shutil.which('nvidia-smi'):
        result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader'], capture_output=True, text=True)
        if result.returncode == 0: gpu = result.stdout.strip()
    manifest = {'modelo': 'Qwen/Qwen2.5-3B-Instruct', 'revision': 'aa8e72537993ba99e69dfaafa59ed015b17504d1',
                'seed': 42, 'sistema': platform.platform(), 'gpu_nvidia': gpu,
                'treino_local_executado': False, 'gpu_externa_recomendada': not bool(gpu),
                'treino': len(groups['treino']), 'validacao': len(groups['validacao']),
                'familias_reservadas_benchmark': held,
                'dados': {name: digest((folder / f'{name}.jsonl').read_bytes()) for name in groups},
                'limite': 'Dataset pequeno de agente, adequado a teste técnico; não comprova ganho pedagógico.'}
    write_json(folder / 'manifesto.json', manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return manifest


if __name__ == '__main__':
    prepare()
