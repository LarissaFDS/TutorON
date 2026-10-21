"""Registro das disciplinas do TutorON e acervo em Markdown das disciplinas novas.

Uma única IA atende todas as disciplinas. O que muda de uma para outra é só o
conhecimento: o acervo (itens.json + indice.json, no mesmo formato do de PAA), as
instruções de rigor da área e os exemplos de pergunta. Tudo isso fica cadastrado em
``disciplinas/disciplinas.json``; nenhum código é específico de uma disciplina.

PAA continua com o pipeline de OCR (``python -m acervo pipeline``) e seus caminhos de
sempre (02-acervo, 04-rag). Disciplinas novas usam material já curado em Markdown,
um arquivo por bloco, com cabeçalho de metadados entre ``---``:

    python -m acervo.disciplinas sd                 # gera itens.json e indice.json (busca léxica)
    python -m acervo.disciplinas sd --embeddings    # idem, com bge-m3 (busca híbrida)

Como cadastrar uma disciplina: docs/DISCIPLINAS.md.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from .common import ROOT, caminho_guardado, digest, read_json, write_json
from .curate import searchable

REGISTRO = ROOT / 'disciplinas' / 'disciplinas.json'
CAMPOS = ('id', 'titulo', 'assunto', 'tipo', 'fonte', 'autoria', 'licenca', 'curadoria')
# Situação da curadoria -> confiabilidade usada pela busca (só média/alta entram no índice).
CONFIABILIDADE = {'aprovado': 'media', 'candidato': 'nao_verificada', 'rejeitado': 'baixa'}
# O que o bloco é e quanto dele foi conferido: a curadoria não trata tudo como validado.
NATUREZA = ('material_da_disciplina', 'nota_da_equipe_ia')
VERIFICACAO = ('conferida_por_codigo', 'exemplos_conferidos', 'parcial', 'sem_resolucao', 'nao_verificada')
MOTIVO = {
    'aprovado': 'Aprovado na curadoria (fonte e transcrição conferidas); revisão do professor pendente.',
    'candidato': 'Candidato: aguarda conferência da fonte ou do conteúdo; fora da busca.',
    'rejeitado': 'Rejeitado na curadoria; fora da busca.',
}


@dataclass(frozen=True)
class Disciplina:
    id: str
    nome: str
    sigla: str
    itens: Path
    indice: Path
    rigor: str = field(repr=False)
    livro_supabase: bool = False
    materiais: Path | None = None
    assuntos: tuple[str, ...] = ()
    exemplos: tuple[str, ...] = ()
    situacao: str = ''

    @property
    def em_validacao(self) -> bool:
        """Situação "em validação" no cadastro: fora do atendimento normal (backend/main.py)."""
        return 'validacao' in re.sub(r'[^a-z]', '', searchable(self.situacao))

    def publico(self) -> dict:
        return {'id': self.id, 'nome': self.nome, 'sigla': self.sigla,
                'exemplos': list(self.exemplos), 'situacao': self.situacao, 'em_validacao': self.em_validacao}


@lru_cache(maxsize=None)
def _carregar(caminho: Path) -> tuple[str, dict[str, Disciplina]]:
    dados = json.loads(caminho.read_text(encoding='utf-8'))
    base = caminho.parent.parent  # disciplinas/disciplinas.json -> raiz do repositório
    disciplinas = {}
    for d in dados['disciplinas']:
        disciplinas[d['id']] = Disciplina(
            id=d['id'], nome=d['nome'], sigla=d['sigla'],
            itens=base / d['itens'], indice=base / d['indice'],
            rigor=(base / d['rigor']).read_text(encoding='utf-8').strip(),
            livro_supabase=bool(d.get('livro_supabase')),
            materiais=base / d['materiais'] if d.get('materiais') else None,
            assuntos=tuple(d.get('assuntos', ())), exemplos=tuple(d.get('exemplos', ())),
            situacao=d.get('situacao', ''))
    if dados['padrao'] not in disciplinas:
        raise ValueError(f'Disciplina padrão {dados["padrao"]!r} não está cadastrada')
    return dados['padrao'], disciplinas


def todas(registro: Path = REGISTRO) -> list[Disciplina]:
    return list(_carregar(Path(registro))[1].values())


def obter(ident: str | None = None, registro: Path = REGISTRO) -> Disciplina:
    """Disciplina pelo id; sem id, a padrão (PAA), para não mudar o comportamento do MVP."""
    padrao, disciplinas = _carregar(Path(registro))
    if ident is None or not str(ident).strip():
        return disciplinas[padrao]
    try:
        return disciplinas[str(ident).strip().lower()]
    except KeyError:
        raise KeyError(f'Disciplina desconhecida: {ident!r}') from None


# ---------------------------------------------------------------------------
# Acervo em Markdown
# ---------------------------------------------------------------------------

def ler(caminho: Path) -> tuple[dict, str, str]:
    bruto = caminho.read_text(encoding='utf-8')
    partes = bruto.split('---', 2)
    if len(partes) != 3 or partes[0].strip():
        raise ValueError(f'{caminho.name}: falta o cabeçalho entre ---')
    meta = dict(re.findall(r'^(\w+):\s*(.+?)\s*$', partes[1], re.M))
    faltando = [c for c in CAMPOS if c not in meta]
    if faltando:
        raise ValueError(f'{caminho.name}: falta {", ".join(faltando)} no cabeçalho')
    if meta['curadoria'] not in CONFIABILIDADE:
        raise ValueError(f'{caminho.name}: curadoria deve ser aprovado, candidato ou rejeitado')
    if meta.get('natureza', NATUREZA[0]) not in NATUREZA or meta.get('verificacao', 'nao_verificada') not in VERIFICACAO:
        raise ValueError(f'{caminho.name}: natureza ou verificacao fora dos valores de acervo/disciplinas.py')
    return meta, partes[2].strip(), digest(bruto)


def registros(disciplina: Disciplina, root: Path = ROOT) -> list[dict]:
    """Itens no mesmo esquema de 02-acervo/itens.json, para a busca de PAA servir sem mudança."""
    itens, vistos = [], set()
    for caminho in sorted(disciplina.materiais.glob('*.md')):
        if caminho.name.upper() == 'README.MD':
            continue
        meta, texto, sha_fonte = ler(caminho)
        if meta['id'] in vistos:
            raise ValueError(f'{caminho.name}: id {meta["id"]!r} repetido')
        if disciplina.assuntos and meta['assunto'] not in disciplina.assuntos:
            raise ValueError(f'{caminho.name}: assunto {meta["assunto"]!r} não cadastrado para {disciplina.id}')
        vistos.add(meta['id'])
        status = meta['curadoria']
        confiabilidade = CONFIABILIDADE[status]
        if status == 'aprovado' and meta.get('revisao_professor', '').lower() in ('sim', 'true'):
            confiabilidade = 'alta'
        itens.append({
            'id': meta['id'], 'disciplina': disciplina.id, 'bloco': disciplina.sigla,
            'assunto': meta['assunto'], 'tipo': meta['tipo'], 'titulo': meta['titulo'],
            'fonte_original': meta['fonte'], 'semestre': meta.get('semestre', 'nao_informado'),
            'tem_resposta': 's' if meta.get('resolucao', 'nao').lower() in ('sim', 'true') else 'n',
            'confiabilidade': confiabilidade, 'motivo_confiabilidade': MOTIVO[status],
            'qualidade_ocr': 'boa', 'arquivo': caminho_guardado(caminho, root), 'sha256': digest(texto),
            'questao': meta.get('questao', '1'), 'segmentacao': 'manual', 'grupo': meta['id'],
            'texto': texto, 'documento_id': meta['id'], 'sha256_fonte': sha_fonte,
            'status_curadoria': status, 'autoria': meta['autoria'], 'licenca': meta['licenca'],
            'natureza': meta.get('natureza', NATUREZA[0]), 'verificacao': meta.get('verificacao', 'nao_verificada'),
            # Revisão interna da curadoria. Não promove a confiabilidade: só revisao_professor faz isso.
            'revisao_humana': meta.get('revisao_humana', 'pendente'),
            'revisao_humana_em': meta.get('revisao_humana_em'), 'revisao_humana_por': meta.get('revisao_humana_por'),
            'fontes_catalogo': [f.strip() for f in meta.get('fontes_catalogo', '').split(',') if f.strip()],
        })
    return itens


def construir(disciplina: Disciplina, root: Path = ROOT, embed: bool = False) -> dict:
    from .retrieval import build

    if disciplina.materiais is None:
        raise ValueError(f'{disciplina.id} não tem pasta de materiais em Markdown (PAA usa o pipeline de OCR)')
    write_json(disciplina.itens, registros(disciplina, root))
    return build(root, embed=embed, itens=disciplina.itens, indice=disciplina.indice)


def main():
    parser = argparse.ArgumentParser(description='TutorON — acervo em Markdown de uma disciplina')
    parser.add_argument('disciplina')
    parser.add_argument('--embeddings', action='store_true')
    args = parser.parse_args()
    indice = construir(obter(args.disciplina), embed=args.embeddings)
    itens = read_json(obter(args.disciplina).itens, [])
    print(f'{len(itens)} blocos lidos; {len(indice["chunks"])} no índice ({indice["modo"]}).')


if __name__ == '__main__':
    main()
