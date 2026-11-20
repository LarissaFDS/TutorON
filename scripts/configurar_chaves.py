"""Grava as chaves do Supabase, Groq e worker no .env sem mostrá-las na tela.

Uso:  python scripts/configurar_chaves.py      (ou 8-Configurar-Chaves.bat)

As chaves secretas são digitadas/coladas sem eco (não aparecem). Enter vazio mantém o valor atual.
Nada é impresso nem enviado para lugar nenhum: só o .env deste PC é alterado (ele não vai para o git).
No fim, testa a conexão com o Supabase e com o Groq e diz só "ok" ou o erro.
"""
from __future__ import annotations

import getpass
import secrets
import sys
from pathlib import Path

import httpx

ENV = Path(__file__).resolve().parents[1] / ".env"

CAMPOS = [  # (variável, pergunta, secreta?)
    ("SUPABASE_URL", "URL do projeto Supabase (https://xxxx.supabase.co)", False),
    ("SUPABASE_ANON_KEY", "Publishable key do Supabase (sb_publishable_...)", True),
    ("SUPABASE_SERVICE_KEY", "Secret key do Supabase (sb_secret_...)", True),
    ("GROQ_API_KEY", "Chave do Groq (gsk_...)", True),
    ("TUTORON_ADMINS", "E-mails de administrador, separados por vírgula", False),
    ("TUTORON_SERVIDOR_URL", "Endereço do site hospedado (vazio se ainda não tem)", False),
]


def ler_env() -> list[str]:
    return ENV.read_text(encoding="utf-8").splitlines() if ENV.exists() else []


def valor_atual(linhas: list[str], nome: str) -> str:
    for l in linhas:
        if l.strip().startswith(nome + "="):
            return l.split("=", 1)[1].strip()
    return ""


def gravar(linhas: list[str], nome: str, valor: str) -> list[str]:
    for i, l in enumerate(linhas):
        if l.strip().startswith(nome + "="):
            linhas[i] = f"{nome}={valor}"
            return linhas
    return linhas + [f"{nome}={valor}"]


def testar(v: dict[str, str]) -> None:
    if v.get("SUPABASE_URL") and v.get("SUPABASE_SERVICE_KEY"):
        try:
            k = v["SUPABASE_SERVICE_KEY"]
            r = httpx.get(v["SUPABASE_URL"].rstrip("/") + "/rest/v1/perfis", params={"select": "id", "limit": "1"},
                          headers={"apikey": k} | ({"Authorization": "Bearer " + k} if k.startswith("eyJ") else {}), timeout=10)
            print("Supabase:", "ok" if r.status_code == 200 else
                  ("conectou, mas falta rodar docs/supabase/schema.sql" if r.status_code == 404 else f"erro HTTP {r.status_code}"))
        except httpx.HTTPError as exc:
            print("Supabase: sem conexão (" + type(exc).__name__ + ")")
    if v.get("GROQ_API_KEY"):
        try:
            r = httpx.get("https://api.groq.com/openai/v1/models",
                          headers={"Authorization": "Bearer " + v["GROQ_API_KEY"]}, timeout=10)
            print("Groq:", "ok" if r.status_code == 200 else f"erro HTTP {r.status_code} (chave errada?)")
        except httpx.HTTPError as exc:
            print("Groq: sem conexão (" + type(exc).__name__ + ")")


def main() -> None:
    linhas = ler_env()
    valores = {}
    print("Cole cada valor e aperte Enter. Chaves secretas não aparecem enquanto você cola.")
    print("Enter vazio mantém o que já está no .env.\n")
    for nome, pergunta, secreta in CAMPOS:
        atual = valor_atual(linhas, nome)
        marca = " [já configurado]" if atual else ""
        novo = (getpass.getpass if secreta else input)(f"{pergunta}{marca}: ").strip()
        if novo:
            linhas = gravar(linhas, nome, novo)
        valores[nome] = novo or atual
    if not valor_atual(linhas, "TUTORON_WORKER_TOKEN"):
        linhas = gravar(linhas, "TUTORON_WORKER_TOKEN", secrets.token_urlsafe(32))
        print("\nTUTORON_WORKER_TOKEN gerado. Copie do .env para o Render quando for hospedar.")
    if not valor_atual(linhas, "TUTORON_EXIGIR_LOGIN"):
        linhas = gravar(linhas, "TUTORON_EXIGIR_LOGIN", "1")
    ENV.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print("\n.env salvo. Testando...\n")
    testar(valores)
    print("\nReinicie o servidor (4-Reiniciar.bat) para valer.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nCancelado. Nada foi salvo.")
