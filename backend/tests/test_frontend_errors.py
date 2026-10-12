import httpx
import pytest

from frontend import api_client


def test_cli_handles_temporary_ai_failure(monkeypatch):
    def post(url, **kwargs):
        assert kwargs["timeout"] == 120.0
        return httpx.Response(503, request=httpx.Request("POST", url))

    monkeypatch.setattr(api_client.httpx, "post", post)
    with pytest.raises(api_client.AIServiceError, match="temporariamente"):
        api_client.send_student_question("Explain recursion")
