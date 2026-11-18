r"""Gera um HTML interativo e autossuficiente para a apresentação sem internet.

    .venv\Scripts\python scripts\demo_apresentacao_offline.py

Reutiliza registros reais, bibliotecas e identidade visual do projeto. Não altera
o HTML de demonstração anterior. PyAV é necessário apenas para gerar o arquivo.
"""
from __future__ import annotations

import json
import re

from demo_offline import DEMO, RAIZ, WEB, data_uri, katex_css, script, webm_e_capa
from design import stylesheet


def main() -> None:
    pasta = RAIZ / "demo-offline"
    dados = json.loads((DEMO / "demo.json").read_text(encoding="utf-8"))
    foto = dados["ciclo"]["foto"]
    arquivos = {foto: data_uri((DEMO / foto).read_bytes(), ".jpg")}
    for v in dados["animacoes"]:
        mp4 = DEMO / v["arquivo"]
        webm, capa = webm_e_capa(mp4)
        arquivos[mp4.name] = data_uri(mp4.read_bytes(), ".mp4")
        arquivos[mp4.with_suffix(".webm").name] = data_uri(webm, ".webm")
        arquivos[mp4.with_suffix(".png").name] = data_uri(capa, ".png")

    html = (pasta / "apresentacao.html").read_text(encoding="utf-8")
    css = "\n".join((stylesheet(), katex_css(), (WEB / "app.css").read_text(encoding="utf-8")))
    html = html.replace("<!-- ESTILOS -->", "<style>\n" + css + "\n</style>")
    js = ["window.TUTORON_DEMO = " + json.dumps(dados, ensure_ascii=False) + ";\n"
          "window.TUTORON_DEMO_ARQUIVOS = " + json.dumps(arquivos) + ";"]
    js += [(WEB / p).read_text(encoding="utf-8") for p in
           ("vendor/marked.min.js", "vendor/purify.min.js", "vendor/katex/katex.min.js", "render.js")]
    js.append((pasta / "apresentacao.js").read_text(encoding="utf-8"))
    html = html.replace("<!-- SCRIPTS -->", "\n".join(script(s) for s in js))
    assert not re.search(r'(?:src|href)=["\'](?:https?:|/)', html), "Dependência externa no HTML"
    assert "url(fonts/" not in html, "Fonte não embutida"
    saida = pasta / "TutorON-apresentacao-offline.html"
    saida.write_text(html, encoding="utf-8")
    print(f"{saida}: {saida.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
