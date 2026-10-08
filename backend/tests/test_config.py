import importlib
from unittest.mock import Mock

import pytest

from backend import config
from backend.errors import ConfigurationError


def test_root_env_is_loaded_from_another_working_directory(monkeypatch, tmp_path):
    # Use a temporary root so this test never reads or modifies real credentials.
    root = tmp_path / "repo"
    (root / "backend").mkdir(parents=True)
    (root / ".env").write_text("GEMINI_API_KEY=fixture-key\nSUPABASE_KEY=file-key\n")
    other = tmp_path / "elsewhere"
    other.mkdir()
    (other / ".env").write_text("GEMINI_API_KEY=wrong-file\n")
    monkeypatch.chdir(other)
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setenv("SUPABASE_KEY", "deployment-key")
    # Execute the real config module with a temporary __file__ anchor.
    namespace = {"__file__": str(root / "backend" / "config.py"), "__package__": "backend"}
    exec(compile(config.ROOT_DIR.joinpath("backend/config.py").read_text(), "config.py", "exec"), namespace)
    assert namespace["ENV_PATH"] == root / ".env"
    assert namespace["required_env"]("GEMINI_API_KEY") == "fixture-key"
    assert namespace["required_env"]("SUPABASE_KEY") == "deployment-key"


def test_missing_and_blank_settings_fail_clearly(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", " ")
    with pytest.raises(ConfigurationError, match="GEMINI_API_KEY"):
        config.required_env("GEMINI_API_KEY")
    monkeypatch.setenv("GEMINI_MODEL", " ")
    with pytest.raises(ConfigurationError, match="GEMINI_MODEL"):
        config.generation_models()


def test_importing_rag_does_not_create_clients(monkeypatch):
    from backend import rag
    google = Mock(side_effect=AssertionError("client created on import"))
    database = Mock(side_effect=AssertionError("client created on import"))
    with monkeypatch.context() as patch:
        patch.setattr("google.genai.Client", google)
        patch.setattr("supabase.create_client", database)
        importlib.reload(rag)
        google.assert_not_called()
        database.assert_not_called()
    # Restore the imported factory binding as well as the source module.
    importlib.reload(rag)
