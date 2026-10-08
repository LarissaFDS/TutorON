"""Comparação cega em localhost; identidade das condições fica apenas no servidor."""
import csv
import json
import secrets
import threading
from collections import defaultdict
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from .common import ROOT, digest, read_json, write_json
from . import models
from .retrieval import search, context

FIELDS = ['sessao', 'data', 'questao', 'origem', 'preferida', 'condicao_preferida',
          'condicao_a', 'condicao_b', 'clareza_a', 'confianca_a', 'utilidade_a',
          'clareza_b', 'confianca_b', 'utilidade_b', 'curso', 'periodo', 'comentario', 'par_sha256']


def csv_safe(value):
    value = str(value).strip()
    return "'" + value if value.startswith(('=', '+', '-', '@', '\t', '\r')) else value


class Study:
    def __init__(self, root=ROOT):
        self.root = root
        self.folder = root / '07-validacao-alunos'
        self.folder.mkdir(parents=True, exist_ok=True)
        self.lock = threading.Lock()
        self.sessions = read_json(self.folder / 'sessoes.json', {})
        self.pairs = read_json(self.folder / 'pares.json', [])

    def start(self, qid=None, question=None, live=False):
        if live:
            question = str(question or '').strip()
            if not 5 <= len(question) <= 4000:
                raise ValueError('Digite uma pergunta entre 5 e 4000 caracteres.')
            # Mesma base/modelo para as duas condições; somente contexto e prompt diferem.
            pair = {'id': 'livre-' + digest(question)[:12], 'pergunta': question,
                    'origem': 'ao_vivo_ollama',
                    'generico': models.generate(question, provider='ollama', structured=False),
                    'tutoron': models.generate(question, context(search(question, self.root), max_chars=5000), provider='ollama')}
        else:
            self.pairs = read_json(self.folder / 'pares.json', [])
            pair = next((p for p in self.pairs if p['id'] == qid), None)
            if not pair:
                raise ValueError('Questão offline não disponível.')
        order = ['generico', 'tutoron']
        secrets.SystemRandom().shuffle(order)
        token = secrets.token_urlsafe(24)
        with self.lock:
            pair_hash = digest(json.dumps(pair, ensure_ascii=False, sort_keys=True))
            write_json(self.folder / 'pares-sessoes' / (pair_hash + '.json'), pair)
            self.sessions[token] = {'questao': pair['id'], 'origem': pair['origem'], 'ordem': order,
                                    'par_sha256': pair_hash,
                                    'votado': False, 'data': datetime.now(timezone.utc).isoformat()}
            write_json(self.folder / 'sessoes.json', self.sessions)
        return {'sessao': token, 'pergunta': pair['pergunta'],
                'A': pair[order[0]]['texto'], 'B': pair[order[1]]['texto']}

    def vote(self, data):
        with self.lock:
            token = data.get('sessao')
            session = self.sessions.get(token)
            if not session:
                raise ValueError('Sessão inválida; gere uma comparação.')
            path = self.folder / 'respostas.csv'
            existing = []
            fields = FIELDS
            has_header = path.exists() and path.stat().st_size > 0
            if path.exists():
                with path.open(encoding='utf-8-sig', newline='') as f:
                    reader = csv.DictReader(f)
                    existing = list(reader)
                    old_fields = reader.fieldnames or []
                if has_header and 'par_sha256' not in old_fields:
                    # Preservar votos legados sem atribuir-lhes respostas não conhecidas.
                    backup = path.with_name('respostas-v1.csv')
                    if not backup.exists(): backup.write_bytes(path.read_bytes())
                    fields = list(dict.fromkeys(old_fields + FIELDS))
                    temporary = path.with_suffix('.tmp')
                    with temporary.open('w', newline='', encoding='utf-8-sig') as f:
                        writer = csv.DictWriter(f, fieldnames=fields)
                        writer.writeheader()
                        writer.writerows(existing)
                    temporary.replace(path)
                elif old_fields:
                    fields = old_fields
            if session['votado'] or any(r['sessao'] == token for r in existing):
                raise ValueError('Esta comparação já recebeu uma avaliação.')
            preference = data.get('preferida')
            if preference not in ('A', 'B', 'empate'):
                raise ValueError('Escolha A, B ou empate.')
            scores = {}
            for side in ('a', 'b'):
                for criterion in ('clareza', 'confianca', 'utilidade'):
                    key = criterion + '_' + side
                    value = data.get(key)
                    if type(value) is not int or value not in range(1, 6):
                        raise ValueError('Dê notas inteiras de 1 a 5 para ambas as respostas.')
                    scores[key] = value
            free = {}
            for key, limit in [('curso', 100), ('periodo', 30), ('comentario', 1500)]:
                value = data.get(key, '')
                if not isinstance(value, str) or len(value) > limit:
                    raise ValueError(f'Campo {key} inválido.')
                free[key] = csv_safe(value)
            record = {'sessao': token, 'data': datetime.now(timezone.utc).isoformat(),
                      'questao': session['questao'], 'origem': session['origem'], 'preferida': preference,
                      'condicao_preferida': 'empate' if preference == 'empate' else session['ordem'][0 if preference == 'A' else 1],
                      'condicao_a': session['ordem'][0], 'condicao_b': session['ordem'][1],
                      'par_sha256': session.get('par_sha256', ''), **scores, **free}
            with path.open('a', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                if not has_header:
                    writer.writeheader()
                writer.writerow(record)
                f.flush()
            session['votado'] = True
            write_json(self.folder / 'sessoes.json', self.sessions)
        return {'salvo': True}


def summarize(root=ROOT):
    path = root / '07-validacao-alunos/respostas.csv'
    rows = []
    if path.exists():
        with path.open(encoding='utf-8-sig', newline='') as f:
            rows = list(csv.DictReader(f))
    groups = defaultdict(list)
    for row in rows:
        groups[(row['questao'], row['origem'], row.get('par_sha256', ''))].append(row)
    summary = []
    for (qid, origin, pair_hash), votes in groups.items():
        entry = {'questao': qid, 'origem': origin, 'par_sha256': pair_hash,
                 'rastreabilidade': 'par_preservado' if pair_hash else 'legado_sem_hash', 'votos': len(votes)}
        for condition in ('generico', 'tutoron', 'empate'):
            entry['preferencia_' + condition] = 100 * sum(r['condicao_preferida'] == condition for r in votes) / len(votes)
        for condition in ('generico', 'tutoron'):
            for criterion in ('clareza', 'confianca', 'utilidade'):
                values = [int(r[criterion + '_' + side]) for r in votes for side in ('a', 'b') if r['condicao_' + side] == condition]
                entry[criterion + '_' + condition] = sum(values) / len(values)
        summary.append(entry)
    write_json(root / '07-validacao-alunos/resumo.json', {'total': len(rows), 'por_questao': summary})
    return {'total': len(rows), 'por_questao': summary}


WEB = Path(__file__).resolve().parent / 'web'


def pages():
    """Arquivos estáticos da página de validação. Lista fechada: nada fora dela é servido."""
    from design import script, stylesheet  # design system do TutorON (pasta design/ na raiz)
    return {
        '/': ((WEB / 'validacao.html').read_bytes(), 'text/html; charset=utf-8'),
        '/design.css': (stylesheet().encode('utf-8'), 'text/css; charset=utf-8'),
        '/text.js': (script('text.js').encode('utf-8'), 'text/javascript; charset=utf-8'),
    }


def serve(root=ROOT, port=8765):
    study = Study(root)
    static = pages()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass  # Não registrar IP, perguntas ou dados dos participantes.

        def send(self, status, body, content_type='application/json; charset=utf-8'):
            encoded = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(encoded)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.end_headers()
            self.wfile.write(encoded)

        def do_GET(self):
            path = urlparse(self.path).path
            if path in static:
                body, content_type = static[path]
                self.send(200, body, content_type)
            elif path == '/api/questoes':
                study.pairs = read_json(study.folder / 'pares.json', [])
                self.send(200, {'questoes': [{'id': p['id'], 'pergunta': p['pergunta']} for p in study.pairs],
                                'historico': any('historica' in p['origem'] for p in study.pairs)})
            else:
                self.send(404, {'erro': 'Não encontrado.'})

        def do_POST(self):
            origin = self.headers.get('Origin')
            allowed = [f'http://127.0.0.1:{port}', f'http://localhost:{port}']
            if origin not in allowed or self.headers.get('Host') not in [f'127.0.0.1:{port}', f'localhost:{port}']:
                self.send(403, {'erro': 'Origem não autorizada.'})
                return
            try:
                size = int(self.headers.get('Content-Length', '0'))
                if not 0 < size <= 20000:
                    raise ValueError('Requisição vazia ou grande demais.')
                data = json.loads(self.rfile.read(size))
                if not isinstance(data, dict):
                    raise ValueError('JSON inválido.')
                if self.path == '/api/comparar':
                    result = study.start(data.get('questao'), data.get('pergunta'), data.get('ao_vivo') is True)
                elif self.path == '/api/votar':
                    result = study.vote(data)
                else:
                    self.send(404, {'erro': 'Não encontrado.'})
                    return
                self.send(200, result)
            except (ValueError, TypeError, KeyError) as exc:
                self.send(400, {'erro': str(exc)})
            except Exception:
                self.send(503, {'erro': 'Modelo local indisponível. Use as questões offline ou execute preparar_modelos.sh no Linux / preparar_modelos.bat no Windows.'})

    print(f'TutorON em http://127.0.0.1:{port} — Ctrl+C para encerrar.', flush=True)
    ThreadingHTTPServer(('127.0.0.1', port), Handler).serve_forever()
