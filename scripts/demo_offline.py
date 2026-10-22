"""Gera a demonstração do tutor socrático num ÚNICO arquivo HTML, para abrir sem servidor e sem internet
(ex.: num computador Linux no lugar da apresentação, com duplo clique).

    .venv\\Scripts\\python scripts\\demo_offline.py            # -> demo-offline/TutorON-demo.html

Embute tudo: CSS do design system, KaTeX (com as fontes), marked, DOMPurify, o renderizador do site,
os dados de backend/web/demo/demo.json, a foto e os vídeos. Os vídeos vão em MP4 (H.264) e também em
WebM (VP9), porque Firefox no Linux sem codecs proprietários não toca H.264; o quadro final de cada
vídeo vira a imagem de capa, para aparecer algo mesmo se nenhum formato tocar.
"""
from __future__ import annotations

import base64
import io
import json
import re
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from design import stylesheet  # noqa: E402

WEB = RAIZ / "backend" / "web"
DEMO = WEB / "demo"
SAIDA = RAIZ / "demo-offline" / "TutorON-demo.html"
TIPOS = {".jpg": "image/jpeg", ".png": "image/png", ".mp4": "video/mp4", ".webm": "video/webm", ".woff2": "font/woff2"}


def data_uri(dados: bytes, sufixo: str) -> str:
    return f"data:{TIPOS[sufixo]};base64," + base64.b64encode(dados).decode()


def katex_css() -> str:
    """CSS do KaTeX com as fontes embutidas (só woff2: todos os navegadores atuais leem)."""
    css = (WEB / "vendor/katex/katex.min.css").read_text(encoding="utf-8")
    fontes = WEB / "vendor/katex/fonts"

    def trocar(m: re.Match) -> str:
        nome = re.search(r"url\(fonts/([^)]+?\.woff2)\)", m.group(0)).group(1)
        return f'src:url({data_uri((fontes / nome).read_bytes(), ".woff2")}) format("woff2")'
    return re.sub(r"src:url\(fonts/[^;}]+", trocar, css)


def webm_e_capa(mp4: Path) -> tuple[bytes, bytes]:
    import av

    with av.open(str(mp4)) as entrada:
        quadros = [q.to_image() for q in entrada.decode(video=0)]
        fps = entrada.streams.video[0].average_rate
    with tempfile.TemporaryDirectory() as tmp:
        destino = Path(tmp) / "v.webm"
        with av.open(str(destino), "w") as saida:
            s = saida.add_stream("libvpx-vp9", rate=fps)
            s.width, s.height = quadros[0].size
            s.pix_fmt = "yuv420p"
            s.options = {"crf": "36", "b:v": "0", "deadline": "good", "cpu-used": "4"}
            for img in quadros:
                for pacote in s.encode(av.VideoFrame.from_image(img)):
                    saida.mux(pacote)
            for pacote in s.encode():
                saida.mux(pacote)
        webm = destino.read_bytes()
    capa = io.BytesIO()
    quadros[-1].save(capa, "PNG", optimize=True)
    return webm, capa.getvalue()


def script(texto: str) -> str:
    return "<script>\n" + texto.replace("</script", "<\\/script") + "\n</script>"


def main() -> None:
    demo = json.loads((DEMO / "demo.json").read_text(encoding="utf-8"))
    arquivos = {demo["ciclo"]["foto"]: data_uri((DEMO / demo["ciclo"]["foto"]).read_bytes(), ".jpg")}
    for v in demo["animacoes"]:
        mp4 = DEMO / v["arquivo"]
        webm, capa = webm_e_capa(mp4)
        arquivos[v["arquivo"]] = data_uri(mp4.read_bytes(), ".mp4")
        arquivos[mp4.with_suffix(".webm").name] = data_uri(webm, ".webm")
        arquivos[mp4.with_suffix(".png").name] = data_uri(capa, ".png")
        print(f"  {v['arquivo']}: mp4 {mp4.stat().st_size // 1024} KB, webm {len(webm) // 1024} KB")

    html = (WEB / "demo.html").read_text(encoding="utf-8")
    estilos = "<style>\n" + stylesheet() + "\n" + katex_css() + "\n" + (WEB / "app.css").read_text(encoding="utf-8") + "\n</style>"
    html = re.sub(r'<link rel="stylesheet" href="[^"]+">\n?', "", html).replace("</head>", estilos + "\n</head>")
    dados = ("window.TUTORON_DEMO = " + json.dumps(demo, ensure_ascii=False) + ";\n"
             "window.TUTORON_DEMO_ARQUIVOS = " + json.dumps(arquivos) + ";")
    scripts = [dados] + [(WEB / p).read_text(encoding="utf-8") for p in
                         ("vendor/marked.min.js", "vendor/purify.min.js", "vendor/katex/katex.min.js", "render.js", "demo.js")]
    html = re.sub(r'<script src="[^"]+"></script>\n?', "", html)
    html = html.replace("</body>", "\n".join(script(s) for s in scripts) + "\n</body>")
    # Sem servidor não há o site principal: o link vira texto.
    html = html.replace('<p class="caption"><a href="/">Ir para o TutorON</a></p>',
                        '<p class="caption">Versão offline da demonstração (arquivo único, sem servidor).</p>')
    assert 'src="/' not in html and 'href="/' not in html, "sobrou referência a arquivo do servidor"
    SAIDA.parent.mkdir(exist_ok=True)
    SAIDA.write_text(html, encoding="utf-8")
    print(f"{SAIDA.relative_to(RAIZ)}: {SAIDA.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
