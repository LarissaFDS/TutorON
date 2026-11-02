"""Auditoria reproduzível de um servidor real. Não muda modelos ou notas de alunos.

Salva requisições, texto bruto, publicado, modelos e tempos. A avaliação de
utilidade/correção é separada: uma aprovação do revisor não é um acerto.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import math
import statistics
import subprocess
import time
from datetime import datetime
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
CAMPOS = {'pergunta', 'disciplina', 'ajuda', 'contexto', 'foto', 'historico', 'travou'}


def gpu():
    r = subprocess.run(['nvidia-smi', '--query-gpu=memory.used,utilization.gpu', '--format=csv,noheader,nounits'],
                       capture_output=True, text=True, timeout=8)
    try:
        memoria, uso = map(int, r.stdout.strip().split(','))
        return {'memoria_mib': memoria, 'uso_pct': uso}
    except ValueError:
        return {}


def ler_registro(pasta, ident):
    arquivo = pasta / 'perguntas.jsonl'
    if not arquivo.exists():
        return {}
    for linha in reversed(arquivo.read_text(encoding='utf-8').splitlines()):
        try:
            r = json.loads(linha)
        except ValueError:
            continue
        if r.get('id') == ident:
            return r
    return {}


def resumo(registros):
    tempos = sorted(r['segundos_total'] for r in registros)
    p95 = tempos[math.ceil(.95 * len(tempos)) - 1] if tempos else None
    return {'casos': len(registros), 'prontas': sum(r['status'] == 'pronta' for r in registros),
            'erros': sum(r['status'] != 'pronta' for r in registros),
            'reservas': sum('ajuda_de_reserva' in r['registro'].get('ajustes', []) for r in registros),
            'fixas': sum(r['registro'].get('bloqueio') == 'questao_atomica' for r in registros),
            'recusas_instrucoes': sum(r['registro'].get('bloqueio') == 'pedido_de_instrucoes' for r in registros),
            'primeiras_versoes_reprovadas': sum(bool(r['registro'].get('resposta_bloqueada')) for r in registros),
            'texto_publicado_antes_de_revisao': sum(r['texto_antes_de_pronta'] for r in registros),
            'mediana_s': round(statistics.median(tempos), 2) if tempos else None,
            'p95_s': p95, 'max_s': max(tempos) if tempos else None}


def salvar(pasta, registros, meta, completa=False):
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / 'resultados.json').write_text(json.dumps({'completa': completa, 'meta': meta,
        'resumo_operacional': resumo(registros), 'avaliacao_pedagogica': 'ver parecer separado, não inferir das aprovações do revisor',
        'casos': registros}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    md = ['# Auditoria por HTTP', '', f"Servidor: {meta['url']}. Completa: {completa}.", '',
          'Aprovação pelo revisor não prova utilidade nem correção.', '',
          '| Caso | Disciplina | Status | Modelo | Tempo (s) | Reserva |', '|---|---|---|---|---:|---|']
    for r in registros:
        reg = r['registro']
        md.append(f"| {r['id']} | {r['corpo'].get('disciplina')} | {r['status']} | {reg.get('modelo', reg.get('bloqueio', '?'))} | {r['segundos_total']:.1f} | {'ajuda_de_reserva' in reg.get('ajustes', [])} |")
    for r in registros:
        reg = r['registro']
        md += ['', f"## {r['id']}", '', '**Pedido:** ' + r['corpo']['pergunta'], '',
               '**Tentativa:** ' + (r['corpo'].get('contexto') or '(não enviada)'), '',
               '**Critério do avaliador (não enviado ao modelo):** ' + r.get('criterio', ''), '',
               '**Primeira versão bruta:**', '', reg.get('resposta_bloqueada') or reg.get('resposta_original') or
               ('(sem inferência)' if reg.get('bloqueio') else reg.get('resposta', '(sem registro)')), '',
               '**Publicada:**', '', r['publicada'], '', '**Revisões:**', '',
               json.dumps(reg.get('revisoes_pedagogicas', []), ensure_ascii=False), '']
    (pasta / 'respostas.md').write_text('\n'.join(l.rstrip() for l in '\n'.join(md).splitlines()) + '\n', encoding='utf-8', newline='\n')


async def caso(client, c, logs, limite=600):
    corpo = {k: v for k, v in c.items() if k in CAMPOS}
    inicio = time.monotonic()
    r = await client.post('/api/perguntar', json=corpo)
    tempo_post = time.monotonic() - inicio
    t = r.json()
    parciais, estados, erros_poll = False, [], []
    if r.status_code == 200:
        ident = t['id']
        while t['status'] not in ('pronta', 'erro'):
            estado = (t['status'], t.get('mensagem', ''))
            if not estados or estados[-1]['mensagem'] != estado[1]:
                estados.append({'s': round(time.monotonic() - inicio, 2), 'status': estado[0], 'mensagem': estado[1]})
            parciais |= bool(t.get('texto'))
            if time.monotonic() - inicio > limite:
                t = {'status': 'timeout_auditoria', 'mensagem': 'limite de acompanhamento excedido'}
                break
            await asyncio.sleep(.5)
            try:
                resposta = await client.get(f'/api/tarefas/{ident}')
                resposta.raise_for_status()
                t = resposta.json()
            except httpx.HTTPError as exc:
                erros_poll.append(type(exc).__name__)
    reg = ler_registro(logs, t.get('id_resposta')) if t.get('id_resposta') else {}
    return {'id': c['id'], 'tema': c.get('tema'), 'criterio': c.get('criterio'), 'corpo': corpo,
            'status': t.get('status', f'HTTP_{r.status_code}'), 'http_post': r.status_code,
            'segundos_post': round(tempo_post, 3), 'segundos_total': round(time.monotonic() - inicio, 2),
            'texto_antes_de_pronta': parciais, 'estados': estados, 'erros_poll': erros_poll,
            'publicada': t.get('texto', ''), 'fontes': t.get('fontes', []), 'registro': reg, 'gpu_depois': gpu()}


async def executar(a):
    todos = json.loads((ROOT / 'eval/casos_auditoria.json').read_text(encoding='utf-8'))
    selecionados = [c for c in todos if not a.ids or c['id'] in a.ids]
    if a.ids and {c['id'] for c in selecionados} != set(a.ids):
        raise ValueError('IDs desconhecidos')
    selecionados = selecionados[a.pular:]
    if a.limite:
        selecionados = selecionados[:a.limite]
    fonte = ROOT / 'eval/casos_auditoria.json'
    meta = {'url': a.url, 'logs': str(a.logs), 'inicio': datetime.now().astimezone().isoformat(),
            'sha256_casos': hashlib.sha256(fonte.read_bytes()).hexdigest(), 'repeticoes': a.repeticoes,
            'concorrencia': a.concorrencia, 'gpu_inicial': gpu()}
    meta['politica_sha256'] = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                              for p in ('backend/prompts.py', 'backend/tutoria.py', 'backend/tarefas.py')}
    meta['git_revision'] = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    registros = []
    async with httpx.AsyncClient(base_url=a.url, timeout=30) as client:
        meta['status_servidor'] = (await client.get('/api/status')).json()
        if a.dialogos:
            dialogos = json.loads((ROOT / 'eval/dialogos_auditoria.json').read_text(encoding='utf-8'))
            for d in dialogos:
                historico = []
                for n, etapa in enumerate(d['rodadas'], 1):
                    c = {**d, **etapa, 'id': f"{d['id']}/{n}", 'historico': list(historico)}
                    r = await caso(client, c, a.logs)
                    registros.append(r)
                    if r['status'] == 'pronta':
                        historico.append({'ajuda': r['registro'].get('ajuda', c['ajuda']), 'texto': r['publicada']})
                    salvar(a.saida, registros, meta)
                    print(f"{r['id']}: {r['status']} {r['segundos_total']:.1f}s ajustes={r['registro'].get('ajustes', [])}", flush=True)
            salvar(a.saida, registros, meta, True)
            print(json.dumps(resumo(registros), ensure_ascii=False), flush=True)
            return
        trabalhos = [{**c, 'id': c['id'] + (f'/rep{n+1}' if a.repeticoes > 1 else '')}
                     for n in range(a.repeticoes) for c in selecionados]
        for i in range(0, len(trabalhos), a.concorrencia):
            lote = await asyncio.gather(*(caso(client, c, a.logs) for c in trabalhos[i:i+a.concorrencia]))
            registros += lote
            salvar(a.saida, registros, meta)
            for r in lote:
                print(f"{r['id']}: {r['status']} {r['segundos_total']:.1f}s modelo={r['registro'].get('modelo', r['registro'].get('bloqueio'))} ajustes={r['registro'].get('ajustes', [])}", flush=True)
    salvar(a.saida, registros, meta, True)
    print(json.dumps(resumo(registros), ensure_ascii=False), flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--url', required=True)
    p.add_argument('--logs', type=Path, required=True)
    p.add_argument('--saida', type=Path, required=True)
    p.add_argument('--ids', nargs='+')
    p.add_argument('--limite', type=int)
    p.add_argument('--pular', type=int, default=0)
    p.add_argument('--repeticoes', type=int, default=1)
    p.add_argument('--concorrencia', type=int, default=1)
    p.add_argument('--dialogos', action='store_true')
    a = p.parse_args()
    if min(a.repeticoes, a.concorrencia) < 1:
        p.error('repetições e concorrência precisam ser positivas')
    asyncio.run(executar(a))


if __name__ == '__main__':
    main()
