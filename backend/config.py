"""Configuração do servidor TutorON, lida do .env da raiz do repositório.

Variáveis já definidas no ambiente prevalecem sobre o .env. Nenhum valor
secreto é registrado em log ou devolvido pela API.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(ENV_PATH, override=False)

DEFAULT_GEMINI_MODELS = (
    "gemini-3.8-flash,gemini-3.7-flash,gemini-3.6-flash,"
    "gemini-3.5-flash,gemini-flash-latest,gemini-3.1-flash-lite"
)


def _env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def _list(name: str, default: str) -> list[str]:
    return [item.strip() for item in _env(name, default).split(",") if item.strip()]


def _float(name: str, default: float) -> float:
    try:
        return float(_env(name, str(default)))
    except ValueError:
        return default


def _int(name: str, default: int) -> int:
    try:
        return int(_env(name, str(default)))
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str = field(repr=False, default="")
    gemini_models: tuple[str, ...] = ()
    # Tempo máximo até o primeiro trecho da resposta. Um modelo que não
    # começa a responder nesse prazo é considerado indisponível.
    gemini_first_chunk_s: float = 40.0
    gemini_idle_s: float = 30.0
    # Corrida escalonada: intervalo para iniciar o próximo modelo se o atual
    # ainda não começou a responder, e espera máxima antes de acionar o local.
    stagger_s: float = 6.0
    local_wait_s: float = 20.0

    ollama_url: str = "http://127.0.0.1:11434"
    local_model: str = "tutoron-paa"
    local_generic_model: str = "qwen3:8b"
    local_thinking: bool = True
    local_thinking_validacao: bool = False
    local_first_chunk_s: float = 150.0
    local_num_ctx: int = 8192
    local_parallel: int = 2
    embed_model: str = "bge-m3"

    supabase_url: str = ""
    supabase_key: str = field(repr=False, default="")
    supabase_min_similarity: float = 0.5

    rate_limit_per_10min: int = 300
    data_dir: Path = ROOT_DIR / "dados"

    @property
    def supabase_enabled(self) -> bool:
        return bool(self.supabase_url and self.supabase_key)

    @property
    def gemini_enabled(self) -> bool:
        return bool(self.gemini_api_key and self.gemini_models)


def load_settings() -> Settings:
    data_dir = _env("TUTORON_DADOS")
    return Settings(
        gemini_api_key=_env("GEMINI_API_KEY") or _env("GOOGLE_API_KEY"),
        gemini_models=tuple(_list("GEMINI_MODELS", DEFAULT_GEMINI_MODELS)),
        gemini_first_chunk_s=_float("GEMINI_TIMEOUT_PRIMEIRO_TRECHO", 40.0),
        gemini_idle_s=_float("GEMINI_TIMEOUT_ENTRE_TRECHOS", 30.0),
        stagger_s=_float("TUTORON_ESCALONAMENTO_S", 6.0),
        local_wait_s=_float("TUTORON_ESPERA_LOCAL_S", 20.0),
        ollama_url=_env("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/"),
        local_model=_env("TUTORON_MODELO_LOCAL", "tutoron-paa"),
        local_generic_model=_env("TUTORON_MODELO_GENERICO_LOCAL", "qwen3:8b"),
        local_thinking=_env("TUTORON_RACIOCINIO_LOCAL", "1") not in ("0", "false", "nao", "não"),
        local_thinking_validacao=_env("TUTORON_RACIOCINIO_LOCAL_VALIDACAO", "0") not in ("0", "false", "nao", "não"),
        local_first_chunk_s=_float("TUTORON_TIMEOUT_LOCAL", 150.0),
        local_num_ctx=_int("TUTORON_NUM_CTX", 8192),
        local_parallel=max(1, _int("TUTORON_LOCAL_PARALELO", 2)),
        embed_model=_env("TUTORON_EMBED_MODEL", "bge-m3"),
        supabase_url=_env("SUPABASE_URL").rstrip("/"),
        supabase_key=_env("SUPABASE_KEY"),
        supabase_min_similarity=_float("SUPABASE_SIMILARIDADE_MINIMA", 0.5),
        rate_limit_per_10min=_int("TUTORON_LIMITE_PERGUNTAS_10MIN", 300),
        data_dir=Path(data_dir) if data_dir else ROOT_DIR / "dados",
    )
