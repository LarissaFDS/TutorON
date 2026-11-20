"""Banco de dados (Supabase/Postgres) pela API REST, sem dependências novas.

- Sem `SUPABASE_URL` e `SUPABASE_SERVICE_KEY` no .env, nada muda: tudo continua em `dados/` (arquivos).
- Com eles, as gravações vão também para o banco. Inserções são em segundo plano (fila + thread),
  para não travar a resposta ao aluno; leituras são síncronas e curtas (timeout de 5 s).
- Tabelas: docs/supabase/schema.sql. Limites do plano grátis: docs/BANCO-E-LIMITES.md.

A chave de serviço (service_role) ignora o RLS: ela só existe no servidor, nunca vai para o navegador.
"""
from __future__ import annotations

import logging
import queue
import threading
from typing import Any

import httpx

logger = logging.getLogger("tutoron.banco")

# arquivo em dados/ -> tabela no banco (registro genérico: id, criado_em, usuario, dados jsonb)
TABELAS_DE_ARQUIVO = {
    "perguntas.jsonl": "perguntas",
    "feedback.jsonl": "feedback",
    "fotos.jsonl": "fotos",
    "animacoes.jsonl": "animacoes",
    "validacao/comparacoes.jsonl": "comparacoes",
    "validacao/avaliacoes.jsonl": "avaliacoes",
}


class Banco:
    def __init__(self, url: str, chave_servico: str, client: httpx.Client | None = None):
        self.url = url.rstrip("/")
        self.rest = self.url + "/rest/v1"
        # Chaves novas (sb_secret_...) vão só no cabeçalho apikey; as antigas (JWT eyJ...) também no Bearer.
        self.headers = {"apikey": chave_servico, "Content-Type": "application/json"}
        if chave_servico.startswith("eyJ"):
            self.headers["Authorization"] = "Bearer " + chave_servico
        self.client = client or httpx.Client(timeout=5)
        self._fila: queue.Queue = queue.Queue(maxsize=5000)
        self._thread = threading.Thread(target=self._trabalhar, name="banco", daemon=True)
        self._thread.start()

    # ------------------------------------------------------------------ escrita em segundo plano
    def inserir(self, tabela: str, linha: dict | list[dict], upsert: str | None = None) -> None:
        """Enfileira; não bloqueia. `upsert` = colunas da chave para mesclar (on_conflict)."""
        try:
            self._fila.put_nowait((tabela, linha, upsert))
        except queue.Full:
            logger.error("Fila do banco cheia; descartando gravação em %s", tabela)

    def inserir_agora(self, tabela: str, linha: dict | list[dict], upsert: str | None = None) -> None:
        params = {"on_conflict": upsert} if upsert else None
        prefer = "resolution=merge-duplicates,return=minimal" if upsert else "return=minimal"
        r = self.client.post(f"{self.rest}/{tabela}", json=linha, params=params,
                             headers=self.headers | {"Prefer": prefer})
        if r.status_code >= 300:
            raise RuntimeError(f"{tabela}: HTTP {r.status_code} {r.text[:300]}")

    def _trabalhar(self) -> None:
        while True:
            tabela, linha, upsert = self._fila.get()
            try:
                self.inserir_agora(tabela, linha, upsert)
            except Exception as exc:  # noqa: BLE001 - nunca derrubar a thread
                logger.warning("Falha ao gravar no banco: %s", exc)
            finally:
                self._fila.task_done()

    def esperar(self, timeout: float = 10) -> None:
        """Para testes e para o desligamento: espera a fila esvaziar."""
        fim = threading.Event()
        threading.Thread(target=lambda: (self._fila.join(), fim.set()), daemon=True).start()
        fim.wait(timeout)

    # ------------------------------------------------------------------ leitura e atualização
    def selecionar(self, tabela: str, params: dict[str, str] | None = None) -> list[dict]:
        r = self.client.get(f"{self.rest}/{tabela}", params=params or {}, headers=self.headers)
        r.raise_for_status()
        return r.json()

    def atualizar(self, tabela: str, filtro: dict[str, str], dados: dict[str, Any]) -> None:
        r = self.client.patch(f"{self.rest}/{tabela}", params=filtro, json=dados,
                              headers=self.headers | {"Prefer": "return=minimal"})
        r.raise_for_status()

    def apagar(self, tabela: str, filtro: dict[str, str]) -> None:
        r = self.client.delete(f"{self.rest}/{tabela}", params=filtro, headers=self.headers)
        r.raise_for_status()

    # ------------------------------------------------------------------ autenticação
    def usuario_do_token(self, token: str, chave_publica: str) -> dict | None:
        """Confere o token de sessão no próprio Supabase Auth. None se inválido ou expirado."""
        try:
            r = self.client.get(self.url + "/auth/v1/user",
                                headers={"apikey": chave_publica, "Authorization": "Bearer " + token})
        except httpx.HTTPError:
            return None
        return r.json() if r.status_code == 200 else None


def criar(settings) -> Banco | None:
    if settings.supabase_url and settings.supabase_service_key:
        return Banco(settings.supabase_url, settings.supabase_service_key)
    return None
