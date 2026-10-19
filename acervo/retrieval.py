import math
import os
import re
from collections import Counter

from .common import ROOT, progress, read_json, write_json
from .curate import searchable
from . import models

# Acervo de PAA; as outras disciplinas passam os próprios caminhos (acervo/disciplinas.py).
ITENS = '02-acervo/itens.json'
INDICE = '04-rag/indice.json'
STOP = set('a o e de da do das dos um uma que em no na os as para por com se ao ou qual como quais explique mostre prova professor algoritmo problema'.split())


def tokens(text):
    return ([t for t in re.findall(r'[a-z0-9]+', searchable(text)) if len(t) > 1 and t not in STOP]
            + estruturais(text))


def estruturais(text):
    """Tokens de notação booleana que as palavras soltas perdem (números e letras de um caractere):
    a lista de mintermos, maxtermos ou irrelevâncias ("Σm(0,1,3,5,7)" → "m:0,1,3,5,7"), as variáveis
    de uma função ("S(A,B,C)" → "vars:a,b,c") e os termos com negação ("A'B'" → "termo:a'b'").
    Lidos no texto original: variáveis booleanas vêm em maiúsculas, o que separa "S(A,B)" de
    "d(a,c)", e a lista exige o prefixo m/M/d, o que separa mintermos de decimais como "1,40".
    Só pontuam quando pergunta e trecho os compartilham; texto sem essa notação não muda."""
    texto = text.replace('’', "'").replace('′', "'")
    achados = []
    for produto, letra, lista in re.findall(r'(?<![A-Za-z])([Σ∑Π∏]?)\s*([mMd])\s*\(\s*(\d+(?:\s*,\s*\d+)+)\s*\)', texto):
        if letra == 'd':
            tipo = 'irrelevantes'
        elif letra == 'M' or produto in ('Π', '∏'):
            tipo = 'maxtermos'
        else:
            tipo = 'mintermos'
        achados.append(f'{tipo}:' + re.sub(r'\s+', '', lista))
    achados += ['vars:' + re.sub(r'\s+', '', v).lower() for v in
                re.findall(r'(?<![A-Za-z])[A-Z]\s*\(\s*([A-Z](?:\s*,\s*[A-Z])+)\s*\)', texto)]
    achados += ['termo:' + t.lower() for t in re.findall(r"(?<![A-Za-z0-9'])((?:[A-Z]'?){1,4})(?![A-Za-z0-9'])", texto)
                if "'" in t]
    return achados


def usar_nao_revisados():
    # Mesma variável de backend/config.py (o .env já foi carregado no ambiente pelo backend).
    return os.environ.get('ACERVO_USAR_NAO_REVISADOS', '0').strip().lower() in ('1', 'true', 'sim')


def embed_document(text, model):
    # Mantém uma questão por chunk, mas representa todo o texto por janelas
    # menores. OCR ruidoso pode ultrapassar limites do tokenizer antes de 8k caracteres.
    windows = [text[i:i+1000] for i in range(0, len(text), 1000)] or [' ']
    vectors = [models.embeddings([window], model, keep_alive='2m')[0] for window in windows]
    average = [sum(vector[i] * len(window) for vector, window in zip(vectors, windows)) / sum(map(len, windows))
               for i in range(len(vectors[0]))]
    norm = math.sqrt(sum(v*v for v in average)) or 1
    return [v / norm for v in average]


def build(root=ROOT, embed=False, itens=ITENS, indice=INDICE):
    items = read_json(root / itens, [])
    chunks = [r for r in items if r['confiabilidade'] in ('media', 'alta') and r['qualidade_ocr'] != 'ilegivel'
              and r['assunto'] != 'assunto_incerto' and r['segmentacao'] != 'pendente']
    model, error, vectors = os.environ.get('TUTORON_EMBED_MODEL', 'bge-m3'), None, []
    previous = read_json(root / indice, {})
    reusable = {}
    if previous.get('embedding_model') == model and previous.get('embedding_janelas_caracteres') == 1000:
        reusable = {i['sha256']: v for i, v in zip(previous.get('chunks', []), previous.get('vectors', []))}
    if embed and chunks:
        try:
            created = False
            # Nesta versão do runtime, lotes maiores podem somar os tokens contra
            # o limite de contexto. Uma questão por chamada preserva o texto inteiro.
            for item in chunks:
                if item['sha256'] in reusable:
                    vectors.append(reusable[item['sha256']])
                else:
                    vectors.append(embed_document(item['texto'], model))
                    created = True
        except Exception as exc:
            error, vectors = type(exc).__name__, []
        if vectors and created:
            try:
                models.post(models.ollama_url() + '/api/embed', {'model': model, 'input': '', 'keep_alive': 0})
            except Exception:
                pass  # Falha de descarregamento não invalida embeddings já calculados.
    index = {'versao': 1, 'modo': 'hibrido' if vectors else 'lexical',
             'embedding_model': model if vectors else None, 'erro_embeddings': error,
             'embedding_janelas_caracteres': 1000, 'chunks': chunks, 'vectors': vectors}
    write_json(root / indice, index)
    if indice == INDICE:
        progress('5. Busca', f'{len(chunks)} blocos indexados; modo {index["modo"]}. Somente confiança média/alta. Não verificados, baixa confiança, ilegíveis e segmentação incerta excluídos.', root)
    return index


def cosine(a, b):
    if len(a) != len(b):
        raise ValueError('Dimensões de embeddings divergentes')
    return sum(x*y for x,y in zip(a,b)) / (math.sqrt(sum(x*x for x in a)) * math.sqrt(sum(y*y for y in b)) or 1)


HUB_VIZINHOS = 10
_hub_cache = {}
# Destaque mínimo do bloco sobre a mediana da similaridade da pergunta com o próprio acervo.
# Pergunta sem relação fica "igualmente parecida" com tudo (destaque baixo); pergunta do assunto
# fica bem mais perto de poucos blocos. Calibrado em eval/relevancia.py com perguntas reais de PAA e SD.
DESTAQUE_COM_PALAVRA = 0.06   # bloco que também compartilha palavras com a pergunta
DESTAQUE_SO_SEMANTICO = 0.12  # bloco sem nenhuma palavra em comum: exige destaque bem maior
# BM25 alto (termos raros do assunto, como "gray" ou "karnaugh") basta sozinho, como as frases exatas.
# Palavras genéricas que casam por acaso ("sistema", "caminhos") ficaram abaixo de 3,5 na calibração.
LEXICO_FORTE = 6.0


def hub_scores(vectors, cache_key=None):
    """Quanto cada bloco é "hub": média do cosseno com seus HUB_VIZINHOS vizinhos mais próximos no
    acervo, menos a média geral. Hubs ficam perto de quase tudo e entram em perguntas sem relação
    (ex.: PAA_L3 p. 4). Subtrair isso da similaridade é a correção CSLS (Conneau et al., 2018)."""
    if cache_key is not None and cache_key in _hub_cache:
        return _hub_cache[cache_key]
    k = min(HUB_VIZINHOS, len(vectors) - 1)
    if k < 1:
        return [0.0] * len(vectors)
    vizinhanca = []
    for i, v in enumerate(vectors):
        sims = sorted((cosine(v, w) for j, w in enumerate(vectors) if j != i), reverse=True)[:k]
        vizinhanca.append(sum(sims) / k)
    media = sum(vizinhanca) / len(vizinhanca)
    # Só penaliza: bloco isolado (abaixo da média) não ganha bônus por ser isolado.
    hubs = [max(0.0, r - media) for r in vizinhanca]
    if cache_key is not None:
        _hub_cache.clear()
        _hub_cache[cache_key] = hubs
    return hubs


def search(question, root=ROOT, k=4, semantic=True, vector=None, min_similarity=None, hub_penalty=False,
           itens=ITENS, indice=INDICE):
    """Busca híbrida (BM25 + bge-m3, fundidos por RRF).

    min_similarity: com embeddings, só entram blocos com similaridade (já descontada a de hub, se
    hub_penalty) maior ou igual a ela E que se destaquem da mediana da pergunta no acervo
    (DESTAQUE_*); palavra em comum sozinha não basta. Pode devolver lista vazia.
    Sem embeddings (busca só léxica), o filtro antigo continua valendo. None mantém o comportamento antigo."""
    index_path = root / indice
    # mtime antes de ler: se o índice for refeito no meio, a próxima consulta vê outro mtime.
    mtime = index_path.stat().st_mtime_ns if index_path.exists() else 0
    index = read_json(index_path, {'chunks': [], 'vectors': []})
    # Revalidar confiança em cada consulta: uma revisão baixa invalida índice antigo.
    live = {r['id']: r for r in read_json(root / itens, [])}
    incluir_nao_revisados = usar_nao_revisados()
    chunks = index['chunks']
    query = tokens(question)
    words = [tokens(c['texto']) for c in chunks]
    avg = sum(map(len, words)) / max(1, len(words))
    scores = []
    for word_list, item in zip(words, chunks):
        freq = Counter(word_list)
        score = 0
        for token in set(query):
            df = sum(token in doc for doc in words)
            idf = math.log(1 + (len(words) - df + 0.5) / (df + 0.5))
            score += idf * freq[token] * 2.5 / (freq[token] + 1.5 * (0.25 + 0.75 * len(word_list) / (avg or 1)))
        for exact in ['asterisco', 'algoritmo x', 'composto']:
            if exact in searchable(question) and exact in searchable(item['texto']):
                score += 5
        # Mesma lista de mintermos ou mesmo termo booleano: indica a mesma questão, como as frases acima.
        score += 5 * len({t for t in query if ':' in t} & set(word_list))
        scores.append(score)
    semantic_scores = []
    mode = 'lexical'
    if semantic and index.get('vectors') and query:
        try:
            if vector is None:
                vector = models.embeddings([question], index['embedding_model'])[0]
            semantic_scores = [cosine(vector, v) for v in index['vectors']]
            mode = 'hibrido'
        except Exception:
            mode = 'lexical_fallback'
    raw_scores = list(semantic_scores)
    if semantic_scores and hub_penalty:
        chave = (str(index_path), mtime, len(index['vectors']))
        semantic_scores = [s - h for s, h in zip(semantic_scores, hub_scores(index['vectors'], chave))]
    base = sorted(raw_scores)[len(raw_scores) // 2] if raw_scores else 0
    result = []
    lexical_order = sorted(range(len(chunks)), key=lambda i: scores[i], reverse=True)
    ranks = {i: rank for rank, i in enumerate(lexical_order, 1)}
    semantic_ranks = {i: rank for rank, i in enumerate(sorted(range(len(chunks)), key=lambda i: semantic_scores[i], reverse=True), 1)} if semantic_scores else {}
    for i, item in enumerate(chunks):
        current = live.get(item['id'])
        if current and current.get('revisado') is False and not incluir_nao_revisados:
            continue  # material da equipe ainda sem revisão humana (acervo/equipe.py)
        if not current or current['sha256'] != item['sha256'] or current['confiabilidade'] not in ('media', 'alta'):
            continue
        exato = any(e in searchable(question) and e in searchable(item['texto']) for e in ['asterisco', 'algoritmo x', 'composto'])
        if semantic_scores and min_similarity is not None:
            exige = DESTAQUE_COM_PALAVRA if scores[i] > 0 else DESTAQUE_SO_SEMANTICO
            if not exato and scores[i] < LEXICO_FORTE and (semantic_scores[i] < min_similarity or raw_scores[i] - base < exige):
                continue  # sem evidência de assunto: melhor nada do que preencher os k lugares
        elif scores[i] <= 0 and (not semantic_scores or semantic_scores[i] < 0.55):
            continue
        score = 1 / (60 + ranks[i]) if scores[i] else 0
        if semantic_scores:
            score += 1 / (60 + semantic_ranks[i])
        score *= {'alta': 1.25, 'media': 1.1}.get(current['confiabilidade'], 1)
        # score_lexico e similaridade(_ajustada) informam o diagnóstico (eval/); a ordem usa só score.
        result.append({**current, 'score': score, 'busca': mode, 'score_lexico': round(scores[i], 3),
                       'similaridade': round(raw_scores[i], 3) if raw_scores else None,
                       'similaridade_ajustada': round(semantic_scores[i], 3) if semantic_scores else None})
    unique, seen = [], set()
    for item in sorted(result, key=lambda r: r['score'], reverse=True):
        signature = searchable(item['texto'])
        if signature not in seen:
            seen.add(signature)
            unique.append(item)
    return unique[:k]


def context(items, max_chars=18000):
    blocks, used = [], 0
    for item in items:
        block = f'[{item["id"]}] Fonte: {item["fonte_original"]}; confiabilidade: {item["confiabilidade"]}; OCR: {item["qualidade_ocr"]}\n{item["texto"]}'
        if used + len(block) > max_chars:
            continue  # Não corta código/fórmula no meio silenciosamente.
        blocks.append(block)
        used += len(block)
    return '\n\n'.join(blocks)
