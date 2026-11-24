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
    # Groq (API compatível com OpenAI, plano grátis): reserva do modelo local, antes do Gemini.
    groq_api_key: str = field(repr=False, default="")
    groq_models: tuple[str, ...] = ("openai/gpt-oss-120b", "openai/gpt-oss-20b")
    groq_vision_model: str = "qwen/qwen3.8-27b"
    # Mais reservas grátis no mesmo formato da OpenAI (24/11/2026): entram depois do Groq, antes do Gemini.
    cerebras_api_key: str = field(repr=False, default="")
    cerebras_models: tuple[str, ...] = ("gpt-oss-120b",)
    openrouter_api_key: str = field(repr=False, default="")
    openrouter_models: tuple[str, ...] = ("openai/gpt-oss-120b:free",)
    # Worker: com a chave definida, o servidor hospedado usa o modelo local do PC só enquanto o PC
    # se registra (scripts/worker_pc.py). Sem ela, usa OLLAMA_URL direto (servidor no próprio PC).
    worker_token: str = field(repr=False, default="")
    gemini_idle_s: float = 30.0
    # Corrida escalonada: intervalo para iniciar o próximo modelo se o atual
    # ainda não começou a responder, e espera máxima antes de acionar o local.
    stagger_s: float = 6.0
    local_wait_s: float = 20.0

    ollama_url: str = "http://127.0.0.1:11434"
    local_model: str = "tutoron-paa"
    local_generic_model: str = "qwen3:8b"
    local_thinking: bool = False  # raciocínio custa até 8x mais tokens: docs/CUSTO-POR-PERGUNTA.md
    local_thinking_validacao: bool = False
    local_first_chunk_s: float = 150.0
    local_num_ctx: int = 8192
    local_thinking_max: int = 2048  # teto de saída (raciocínio + ajuda) quando o raciocínio está ligado
    local_parallel: int = 2
    # Modelo de visão no Ollama para ler fotos quando nenhum Gemini responder (ex.: qwen2.5vl:7b).
    # Vazio = só Gemini lê fotos.
    local_vision_model: str = ""
    embed_model: str = "bge-m3"
    # Material da equipe com `revisado: false` fica fora da busca em produção. Liga só para medir
    # (eval/matriz.py gerar --incluir-nao-revisados). A busca lê a mesma variável a cada consulta.
    acervo_usar_nao_revisados: bool = False

    supabase_url: str = ""
    supabase_key: str = field(repr=False, default="")
    supabase_min_similarity: float = 0.5
    # Banco e contas (docs/supabase/schema.sql). A chave de serviço fica só no servidor; a pública
    # (anon/publishable) vai para o navegador para o login com Google/e-mail.
    supabase_service_key: str = field(repr=False, default="")
    supabase_anon_key: str = ""
    exigir_login: bool = False
    admins: tuple[str, ...] = ()  # e-mails com acesso de administrador
    # Piso absoluto do acervo local (cosseno bge-m3, já descontado o "hub"). Quem separa pergunta
    # fora do tema é o destaque sobre a mediana (acervo/retrieval.py); o piso de 0,45 só descarta o
    # que é distante de tudo. Com 0,5, perguntas legítimas de SD (Moore/Mealy, 0,50) e de PAA (PD)
    # ficavam sem material: veja `python eval/relevancia.py`. Valor negativo desliga o corte E a penalidade de hub
    # (a busca volta a ser exatamente a de antes). A penalidade de hub só vale com o corte ligado.
    acervo_min_similarity: float = 0.45
    acervo_hub_penalty: bool = True
    # Disciplinas "em validação" no cadastro ficam fora do atendimento normal. Liberação explícita,
    # só para testes e validações autorizadas: ids separados por vírgula ou "todas". Vazio = nenhuma.
    disciplinas_em_validacao_liberadas: tuple[str, ...] = ()

    rate_limit_per_10min: int = 300
    data_dir: Path = ROOT_DIR / "dados"
    # Cota de tokens por usuário (0 = desligada). Ver backend/cota.py.
    cota_tokens: int = 0
    # Convidado sem conta (com o Supabase ligado): limite bem menor, para incentivar a criar conta.
    cota_convidado: int = 6000
    cota_janela_h: float = 24.0
    dev_chave: str = ""
    gratis_local_primeiro: bool = True
    url_publica: str = ""

    @property
    def supabase_enabled(self) -> bool:
        return bool(self.supabase_url and self.supabase_key)

    @property
    def groq_enabled(self) -> bool:
        return bool(self.groq_api_key and self.groq_models)

    @property
    def cerebras_enabled(self) -> bool:
        return bool(self.cerebras_api_key and self.cerebras_models)

    @property
    def openrouter_enabled(self) -> bool:
        return bool(self.openrouter_api_key and self.openrouter_models)

    @property
    def gemini_enabled(self) -> bool:
        return bool(self.gemini_api_key and self.gemini_models)


def load_settings() -> Settings:
    data_dir = _env("TUTORON_DADOS")
    return Settings(
        gemini_api_key=_env("GEMINI_API_KEY") or _env("GOOGLE_API_KEY"),
        gemini_models=tuple(_list("GEMINI_MODELS", DEFAULT_GEMINI_MODELS)),
        gemini_first_chunk_s=_float("GEMINI_TIMEOUT_PRIMEIRO_TRECHO", 40.0),
        groq_api_key=_env("GROQ_API_KEY"),
        groq_models=tuple(_list("GROQ_MODELS", "openai/gpt-oss-120b,openai/gpt-oss-20b")),
        groq_vision_model=_env("GROQ_MODELO_VISAO", "qwen/qwen3.8-27b"),
        cerebras_api_key=_env("CEREBRAS_API_KEY"),
        cerebras_models=tuple(_list("CEREBRAS_MODELS", "gpt-oss-120b")),
        openrouter_api_key=_env("OPENROUTER_API_KEY"),
        openrouter_models=tuple(_list("OPENROUTER_MODELS", "openai/gpt-oss-120b:free")),
        worker_token=_env("TUTORON_WORKER_TOKEN"),
        gemini_idle_s=_float("GEMINI_TIMEOUT_ENTRE_TRECHOS", 30.0),
        stagger_s=_float("TUTORON_ESCALONAMENTO_S", 6.0),
        local_wait_s=_float("TUTORON_ESPERA_LOCAL_S", 20.0),
        ollama_url=_env("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/"),
        local_model=_env("TUTORON_MODELO_LOCAL", "tutoron-paa"),
        local_generic_model=_env("TUTORON_MODELO_GENERICO_LOCAL", "qwen3:8b"),
        local_thinking=_env("TUTORON_RACIOCINIO_LOCAL", "0") not in ("0", "false", "nao", "não"),
        local_thinking_validacao=_env("TUTORON_RACIOCINIO_LOCAL_VALIDACAO", "0") not in ("0", "false", "nao", "não"),
        local_first_chunk_s=_float("TUTORON_TIMEOUT_LOCAL", 150.0),
        local_num_ctx=_int("TUTORON_NUM_CTX", 8192),
        local_thinking_max=_int("TUTORON_RACIOCINIO_MAX", 2048),
        local_parallel=max(1, _int("TUTORON_LOCAL_PARALELO", 2)),
        local_vision_model=_env("TUTORON_MODELO_VISAO_LOCAL"),
        embed_model=_env("TUTORON_EMBED_MODEL", "bge-m3"),
        acervo_usar_nao_revisados=_env("ACERVO_USAR_NAO_REVISADOS", "0").lower() in ("1", "true", "sim"),
        supabase_url=_env("SUPABASE_URL").rstrip("/"),
        supabase_key=_env("SUPABASE_KEY"),
        supabase_min_similarity=_float("SUPABASE_SIMILARIDADE_MINIMA", 0.5),
        supabase_service_key=_env("SUPABASE_SERVICE_KEY"),
        supabase_anon_key=_env("SUPABASE_ANON_KEY"),
        exigir_login=_env("TUTORON_EXIGIR_LOGIN", "0") not in ("0", "false", "nao", "não"),
        admins=tuple(e.lower() for e in _list("TUTORON_ADMINS", "")),
        acervo_min_similarity=_float("ACERVO_SIMILARIDADE_MINIMA", 0.45),
        disciplinas_em_validacao_liberadas=tuple(
            i.strip().lower() for i in _env("TUTORON_LIBERAR_EM_VALIDACAO").split(",") if i.strip()),
        acervo_hub_penalty=_env("ACERVO_PENALIDADE_HUB", "1") not in ("0", "false", "nao", "não"),
        rate_limit_per_10min=_int("TUTORON_LIMITE_PERGUNTAS_10MIN", 300),
        data_dir=Path(data_dir) if data_dir else ROOT_DIR / "dados",
        cota_tokens=_int("TUTORON_COTA_TOKENS", 40000),
        cota_convidado=_int("TUTORON_COTA_CONVIDADO", 6000),
        cota_janela_h=_float("TUTORON_COTA_JANELA_H", 24.0),
        dev_chave=_env("TUTORON_DEV_CHAVE"),
        gratis_local_primeiro=_env("TUTORON_GRATIS_LOCAL_PRIMEIRO", "1") not in ("0", "false", "nao", "não"),
        url_publica=_env("TUTORON_URL_PUBLICA").rstrip("/"),
    )
