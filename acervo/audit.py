"""Auditoria por documento; legibilidade não certifica correção matemática."""
from collections import Counter
from .common import ROOT, caminho_local, digest, read_json, write_json


def audit(root=ROOT):
    inventory = read_json(root / '03-triagem/inventario.json', [])
    items = read_json(root / '02-acervo/itens.json', [])
    indexed = {i['id'] for i in read_json(root / '04-rag/indice.json', {}).get('chunks', [])}
    docs = []
    for source in inventory:
        original = caminho_local(source['arquivo'], root)
        snapshot = caminho_local(source['copia'], root)
        extracted = read_json(root / '01-extraido' / (source['id'] + '.json'), {})
        pages = extracted.get('paginas_extraidas', [])
        blocks = [i for i in items if i['documento_id'] == source['id']]
        integrity = original.exists() and snapshot.exists() and digest(original.read_bytes()) == digest(snapshot.read_bytes()) == source['sha256']
        figures = [p['imagem'] for p in pages if p.get('imagem')]
        figures += [f for p in pages for f in p.get('figuras', [])]
        docs.append({'id': source['id'], 'arquivo': source['arquivo'], 'sha256': source['sha256'],
                     'integridade': integrity, 'paginas_esperadas': source['paginas'], 'paginas_extraidas': len(pages),
                     'extraido_sha256_confere': extracted.get('sha256') == source['sha256'],
                     'metodos': dict(Counter(p['metodo'] for p in pages)), 'qualidades': dict(Counter(p['qualidade'] for p in pages)),
                     'figuras_ausentes': [f for f in figures if not caminho_local(f, root).exists()],
                     'blocos': [i['id'] for i in blocks],
                     'blocos_corrigidos': [i['id'] for i in blocks if i.get('curadoria', {}).get('status') == 'corrigido_por_agente'],
                     'blocos_rag': [i['id'] for i in blocks if i['id'] in indexed],
                     'revisao_pedagogica': 'correcao_parcial_por_agente' if any(i.get('curadoria') for i in blocks) else 'pendente'})
    block_audit = []
    for item in items:
        flags = []
        if '[ilegivel]' in item['texto']: flags.append('conteudo_visual_ilegivel')
        if '[incerto]' in item['texto']: flags.append('simbolos_incertos')
        if item['segmentacao'] == 'pendente': flags.append('segmentacao_pendente')
        if item['confiabilidade'] == 'baixa': flags.append('quarentena')
        if item['sha256'] != digest(item['texto']): flags.append('hash_texto_invalido')
        block_audit.append({'id': item['id'], 'arquivo': item['arquivo'], 'sha256': item['sha256'],
                            'caracteres': len(item['texto']), 'confiabilidade': item['confiabilidade'],
                            'alertas': flags, 'no_rag': item['id'] in indexed,
                            'curadoria': item.get('curadoria', {}).get('status', 'revisao_pedagogica_pendente')})
    result = {'documentos': docs, 'blocos': block_audit,
              'resumo': {'documentos': len(docs), 'paginas': sum(d['paginas_extraidas'] for d in docs),
                         'blocos': len(items), 'blocos_corrigidos': sum(len(d['blocos_corrigidos']) for d in docs),
                         'blocos_rag': len(indexed), 'integridade_ok': all(d['integridade'] for d in docs)}}
    write_json(root / '03-triagem/auditoria.json', result)
    lines = ['# Auditoria por arquivo', '', 'Cada entrada foi aberta, extraída e verificada por hash. '
             'Correções pedagógicas por agente não equivalem à aprovação do professor. '
             'Fotos, código e diagramas podem continuar parciais. Não há alegação de OCR universal.', '',
             '| Arquivo | Páginas | Integridade | Blocos corrigidos | Blocos no RAG |', '|---|---:|---|---:|---:|']
    lines += [f'| {d["arquivo"]} | {d["paginas_extraidas"]}/{d["paginas_esperadas"]} | {d["integridade"]} | {len(d["blocos_corrigidos"])} | {len(d["blocos_rag"])} |' for d in docs]
    lines += ['', 'Detalhes de todos os blocos, hashes, alertas e pendências: auditoria.json. '
              'Artefatos históricos fora do inventário atual não alimentam o índice.']
    (root / '03-triagem/AUDITORIA.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(result['resumo'])
    if not result['resumo']['integridade_ok'] or any(d['figuras_ausentes'] or not d['extraido_sha256_confere'] or d['paginas_extraidas'] != d['paginas_esperadas'] for d in docs):
        raise RuntimeError('Auditoria encontrou falha estrutural; veja auditoria.json')
    return result


if __name__ == '__main__':
    audit()
