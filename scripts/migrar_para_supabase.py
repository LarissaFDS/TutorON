"""Copia os dados locais (dados/*.jsonl) para o Supabase. Não apaga nem muda nada em dados/.

Uso (com SUPABASE_URL e SUPABASE_SERVICE_KEY no .env e o schema de docs/supabase/schema.sql já criado):

    python scripts/migrar_para_supabase.py            # mostra o que seria enviado (simulação)
    python scripts/migrar_para_supabase.py --enviar   # envia

Linhas de teste ficam de fora (curso "teste-carga", perguntas do scripts/teste_carga.py e uso marcado
como dev). Perguntas, votos e planos usam o id de cada linha (upsert) e não duplicam; o histórico de
uso (uso_tokens) não tem id próprio, então rode com --enviar uma vez só.
Antes de enviar, confere o tamanho contra o limite do plano grátis (docs/BANCO-E-LIMITES.md).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from backend.banco import TABELAS_DE_ARQUIVO, Banco  # noqa: E402
from backend.config import load_settings  # noqa: E402

TETO_MB = 350  # 70% dos 500 MB do plano grátis


def eh_teste(registro: dict) -> bool:
    texto = json.dumps(registro, ensure_ascii=False).lower()
    return "teste-carga" in texto or "teste_carga" in texto


def ler(caminho: Path) -> list[dict]:
    if not caminho.exists():
        return []
    linhas = []
    for texto in caminho.read_text(encoding="utf-8").splitlines():
        try:
            linhas.append(json.loads(texto))
        except ValueError:
            continue
    return linhas


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--enviar", action="store_true")
    args = ap.parse_args()
    s = load_settings()
    pasta = s.data_dir
    lotes: dict[str, list[dict]] = {}
    for arquivo, tabela in TABELAS_DE_ARQUIVO.items():
        regs = [r for r in ler(pasta / arquivo) if not eh_teste(r)]
        lotes[tabela] = [{"id": str(r.get("id") or r.get("sessao") or f"{tabela}-{i}"),
                          "criado_em": r.get("data"), "dados": r} for i, r in enumerate(regs)]
    uso = [u for u in ler(pasta / "uso.jsonl") if not u.get("dev")]
    lotes["uso_tokens"] = [{k: u.get(k) for k in ("data", "quem", "tokens", "dev", "tipo", "plano")} for u in uso]
    planos = json.loads((pasta / "planos.json").read_text(encoding="utf-8")) if (pasta / "planos.json").exists() else {}
    lotes["planos"] = [{"quem": q} | {k: p.get(k) for k in ("plano", "desde", "cartao", "simulado")}
                       for q, p in planos.items()]

    total = sum(len(json.dumps(v, ensure_ascii=False).encode()) for v in lotes.values())
    for tabela, linhas in lotes.items():
        print(f"{tabela:12} {len(linhas):6} linhas")
    print(f"tamanho aproximado: {total / 1e6:.2f} MB (teto de trabalho: {TETO_MB} MB)")
    if total / 1e6 > TETO_MB:
        sys.exit("Passa do teto do plano grátis. Resuma ou envie só o necessário.")
    if not args.enviar:
        print("\nSimulação: nada foi enviado. Rode com --enviar.")
        return
    if not (s.supabase_url and s.supabase_service_key):
        sys.exit("Faltam SUPABASE_URL e SUPABASE_SERVICE_KEY no .env.")
    banco = Banco(s.supabase_url, s.supabase_service_key)
    chaves = {"uso_tokens": None, "planos": "quem"}
    for tabela, linhas in lotes.items():
        for i in range(0, len(linhas), 200):
            banco.inserir_agora(tabela, linhas[i:i + 200], upsert=chaves.get(tabela, "id"))
        print(f"enviado: {tabela}")
    print("Pronto. Os arquivos em dados/ continuam iguais.")


if __name__ == "__main__":
    main()
