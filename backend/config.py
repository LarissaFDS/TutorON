"""Always load this repository's .env, without overriding deployment variables."""

import os
from pathlib import Path

from dotenv import load_dotenv

from .errors import ConfigurationError

ROOT_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(ENV_PATH, override=False)


def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ConfigurationError(f"Missing {name}; fill {ENV_PATH} and restart the backend")
    return value


def generation_models() -> list[str]:
    primary = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()
    fallback = os.getenv("GEMINI_FALLBACK_MODEL", "gemini-3.6-flash").strip()
    if not primary:
        raise ConfigurationError("GEMINI_MODEL must not be blank")
    return list(dict.fromkeys(model for model in (primary, fallback) if model))
