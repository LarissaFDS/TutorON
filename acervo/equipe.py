"""Material elaborado pela equipe TutorON (materiais/Equipe/*.md).

Não é material do professor nem resolução de aluno: cada arquivo declara `autoria` e
`revisado: false` até uma revisão humana. Entra no acervo com confiabilidade média,
como as correções derivadas (c01, c02, c09…), e pode ser rebaixado pela triagem por
regras ou promovido por revisão humana em 03-triagem/revisoes.json.
Enquanto `revisado: false`, a busca de produção ignora o bloco (ACERVO_USAR_NAO_REVISADOS);
como revisar: docs/curadoria-equipe.md.

Atualizar o acervo sem rodar o pipeline inteiro:
    python -m acervo equipe                 # itens.json
    python -m acervo indexar --embeddings   # índice (precisa do bge-m3)
"""
import re

from .common import ROOT, caminho_guardado, digest, read_json, write_csv, write_json

PASTA = 'materiais/Equipe'
TIPO = 'material_equipe'
MOTIVO = 'Material elaborado pela equipe TutorON (não é do professor); revisão humana pendente.'


def ler(caminho):
    bruto = caminho.read_text(encoding='utf-8')
    partes = bruto.split('---', 2)
    if len(partes) != 3 or partes[0].strip():
        raise ValueError(f'{caminho.name}: falta o cabeçalho entre ---')
    meta = dict(re.findall(r'^(\w+):\s*(.+?)\s*$', partes[1], re.M))
    for campo in ('id', 'titulo', 'assunto', 'autoria', 'revisado'):
        if campo not in meta:
            raise ValueError(f'{caminho.name}: falta {campo} no cabeçalho')
    if 'professor' in meta['autoria'].lower() and 'não' not in meta['autoria'].lower():
        raise ValueError(f'{caminho.name}: material da equipe não pode ser atribuído ao professor')
    return meta, partes[2].strip(), digest(bruto)


def registros(root=ROOT):
    itens = []
    for caminho in sorted((root / PASTA).glob('*.md')):
        meta, texto, sha_fonte = ler(caminho)
        revisado = meta['revisado'].lower() in ('true', 'sim', 'yes')
        itens.append({
            'id': meta['id'], 'bloco': meta['assunto'][:2].upper(), 'assunto': meta['assunto'], 'tipo': TIPO,
            'fonte_original': f'{PASTA}/{caminho.name}', 'semestre': 'nao_informado', 'tem_resposta': 's',
            'confiabilidade': 'media', 'motivo_confiabilidade': MOTIVO, 'qualidade_ocr': 'boa',
            'arquivo': caminho_guardado(caminho, root), 'sha256': digest(texto), 'questao': '1',
            'segmentacao': 'manual', 'grupo': meta['id'], 'texto': texto, 'documento_id': 'equipe',
            'sha256_fonte': sha_fonte, 'origem': 'equipe', 'autoria': meta['autoria'], 'revisado': revisado,
            'titulo': meta['titulo'],
        })
    return itens


def mesclar(records, root=ROOT):
    """Substitui os itens da equipe pelos arquivos atuais (idempotente)."""
    return [r for r in records if r.get('origem') != 'equipe'] + registros(root)


def sincronizar(root=ROOT):
    from .curate import FIELDS

    records = mesclar(read_json(root / '02-acervo/itens.json', []), root)
    write_json(root / '02-acervo/itens.json', records)
    write_csv(root / '02-acervo/indice.csv', records, FIELDS)
    return records
