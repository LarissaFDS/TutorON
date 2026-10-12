"""Envia PDFs de PAA para o Supabase (tabelas documents/chunks de docs/schema.sql).

Cada página vira um trecho com embedding bge-m3 (1024 dimensões, gerado no Ollama
local). Documentos com o mesmo nome já enviados são pulados, então dá para rodar
de novo numa pasta inteira sem duplicar nada.

Uso (na raiz do repositório, com o Ollama ligado):
    .venv\\Scripts\\python -m backend.ingest "C:\\caminho\\livro.pdf" "C:\\pasta\\com\\pdfs"
    .venv\\Scripts\\python -m backend.ingest --listar
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import httpx
from pypdf import PdfReader

from .config import load_settings

LOTE = 8  # páginas por chamada de embedding


def _cliente(settings):
    if not settings.supabase_enabled:
        raise SystemExit("Preencha SUPABASE_URL e SUPABASE_KEY no .env.")
    headers = {"apikey": settings.supabase_key, "Authorization": f"Bearer {settings.supabase_key}",
               "Content-Type": "application/json", "Prefer": "return=representation"}
    return httpx.Client(base_url=settings.supabase_url + "/rest/v1", headers=headers, timeout=60)


def documentos(api: httpx.Client) -> dict[str, int]:
    resposta = api.get("/documents", params={"select": "id,name"})
    resposta.raise_for_status()
    return {d["name"]: d["id"] for d in resposta.json()}


def embeddings(settings, textos: list[str]) -> list[list[float]]:
    resposta = httpx.post(settings.ollama_url + "/api/embed", timeout=300,
                          json={"model": settings.embed_model, "input": textos, "keep_alive": "10m"})
    resposta.raise_for_status()
    vetores = resposta.json()["embeddings"]
    if len(vetores) != len(textos) or any(len(v) != 1024 for v in vetores):
        raise RuntimeError("Embeddings incompletos ou com dimensão diferente de 1024 (bge-m3).")
    return vetores


def enviar_pdf(settings, api: httpx.Client, caminho: Path, existentes: dict[str, int]) -> None:
    if caminho.name in existentes:
        print(f"= {caminho.name}: já está no Supabase (id {existentes[caminho.name]}), pulando.")
        return
    paginas = []
    for numero, pagina in enumerate(PdfReader(str(caminho)).pages, start=1):
        texto = (pagina.extract_text() or "").strip()
        if len(texto) >= 40:  # páginas vazias ou só com número não ajudam a busca
            paginas.append((numero, texto))
    if not paginas:
        print(f"! {caminho.name}: nenhuma página com texto (PDF escaneado? rode o OCR do acervo antes).")
        return
    documento = api.post("/documents", json={"name": caminho.name})
    documento.raise_for_status()
    doc_id = documento.json()[0]["id"]
    for inicio in range(0, len(paginas), LOTE):
        lote = paginas[inicio:inicio + LOTE]
        vetores = embeddings(settings, [t for _, t in lote])
        linhas = [{"document_id": doc_id, "content": t, "page_number": n, "embedding": v}
                  for (n, t), v in zip(lote, vetores)]
        api.post("/chunks", json=linhas, headers={"Prefer": "return=minimal"}).raise_for_status()
        print(f"  {caminho.name}: {min(inicio + LOTE, len(paginas))}/{len(paginas)} páginas", flush=True)
    existentes[caminho.name] = doc_id
    print(f"+ {caminho.name}: {len(paginas)} páginas enviadas (id {doc_id}).")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("caminhos", nargs="*", help="PDFs ou pastas com PDFs")
    parser.add_argument("--listar", action="store_true", help="mostra os documentos já enviados")
    args = parser.parse_args()
    settings = load_settings()
    with _cliente(settings) as api:
        existentes = documentos(api)
        if args.listar or not args.caminhos:
            for nome, ident in sorted(existentes.items(), key=lambda x: x[1]):
                print(f"{ident:>4}  {nome}")
            return
        arquivos: list[Path] = []
        for c in map(Path, args.caminhos):
            arquivos += sorted(c.rglob("*.pdf")) if c.is_dir() else [c]
        for arquivo in arquivos:
            try:
                enviar_pdf(settings, api, arquivo, existentes)
            except (httpx.HTTPError, RuntimeError) as exc:
                print(f"! {arquivo.name}: falhou ({exc}). Os demais continuam.", file=sys.stderr)


if __name__ == "__main__":
    main()
