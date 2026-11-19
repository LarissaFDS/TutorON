"""Gera a marca do TutorON: logo (SVG), favicon, ícones PNG e a imagem de pré-visualização do link.

O símbolo: um balão de conversa (tutoria = diálogo) com o botão "liga" dentro (ON) e um ponto
verde de "online" no canto (o tutor está presente, a qualquer hora).

Uso: python scripts/gerar_marca.py   (grava em backend/web/marca/)
"""
from __future__ import annotations

import math
from pathlib import Path

import cairo

DESTINO = Path(__file__).resolve().parents[1] / "backend/web/marca"
AZUL_1, AZUL_2 = (0x4D / 255, 0x6B / 255, 0xFE / 255), (0x7B / 255, 0x4D / 255, 0xFF / 255)
VERDE = (0x22 / 255, 0xC5 / 255, 0x5E / 255)
TINTA = (0x0F / 255, 0x17 / 255, 0x2A / 255)

# Geometria em uma grade 64x64 (a mesma do SVG).
BALAO = (6, 7, 52, 42, 14)            # x, y, largura, altura, raio
CENTRO, RAIO, TRACO = (32, 28.5), 10.5, 4.6
PONTO, PONTO_R = (52, 11), 6.2

SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="TutorON">
  <defs>
    <linearGradient id="tg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#4D6BFE"/><stop offset="1" stop-color="#7B4DFF"/>
    </linearGradient>
  </defs>
  <path fill="url(#tg)" d="M20 7h24a14 14 0 0 1 14 14v14a14 14 0 0 1-14 14H27L11 58L10.1 44.9A14 14 0 0 1 6 35V21A14 14 0 0 1 20 7z"/>
  <path d="M25.2 21.3a10.5 10.5 0 1 0 13.6 0" fill="none" stroke="#fff" stroke-width="4.6" stroke-linecap="round"/>
  <path d="M32 16.5v11" stroke="#fff" stroke-width="4.6" stroke-linecap="round"/>
  <circle cx="52" cy="11" r="6.2" fill="#22C55E" stroke="#fff" stroke-width="2.6"/>
</svg>
"""


def balao(ctx: cairo.Context) -> None:
    x, y, w, h, r = BALAO
    ctx.new_path()
    ctx.arc(x + w - r, y + r, r, -math.pi / 2, 0)
    ctx.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    ctx.line_to(27, y + h)
    ctx.line_to(11, 58)
    ctx.arc(x + r, y + h - r, r, 0.75 * math.pi, math.pi)
    ctx.arc(x + r, y + r, r, math.pi, 3 * math.pi / 2)
    ctx.close_path()


def simbolo(ctx: cairo.Context, tamanho: float, ox: float = 0, oy: float = 0, fundo=None) -> None:
    ctx.save()
    ctx.translate(ox, oy)
    ctx.scale(tamanho / 64, tamanho / 64)
    g = cairo.LinearGradient(0, 0, 64, 64)
    g.add_color_stop_rgb(0, *AZUL_1)
    g.add_color_stop_rgb(1, *AZUL_2)
    balao(ctx)
    ctx.set_source(g)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(TRACO)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    cx, cy = CENTRO
    ctx.new_path()
    ctx.arc(cx, cy, RAIO, -math.pi / 2 + 0.70, -math.pi / 2 - 0.70 + 2 * math.pi)
    ctx.stroke()
    ctx.move_to(cx, 16.5)
    ctx.line_to(cx, 27.5)
    ctx.stroke()
    ctx.arc(*PONTO, PONTO_R, 0, 2 * math.pi)
    ctx.set_source_rgb(*VERDE)
    ctx.fill_preserve()
    ctx.set_source_rgb(*(fundo or (1, 1, 1)))
    ctx.set_line_width(2.6)
    ctx.stroke()
    ctx.restore()


def icone(lado: int, nome: str, margem: float = 0.0, fundo=None) -> None:
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, lado, lado)
    ctx = cairo.Context(s)
    if fundo:
        ctx.set_source_rgb(*fundo)
        ctx.paint()
    m = lado * margem
    simbolo(ctx, lado - 2 * m, m, m, fundo)
    s.write_to_png(str(DESTINO / nome))


def texto(ctx, x, y, conteudo, tamanho, cor, peso=cairo.FONT_WEIGHT_BOLD):
    ctx.select_font_face("Segoe UI", cairo.FONT_SLANT_NORMAL, peso)
    ctx.set_font_size(tamanho)
    ctx.set_source_rgb(*cor)
    ctx.move_to(x, y)
    ctx.show_text(conteudo)
    return ctx.text_extents(conteudo).x_advance


def previa() -> None:
    """1200x630: o que aparece quando o link é enviado no WhatsApp, Telegram, Discord etc."""
    w, h = 1200, 630
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(s)
    fundo = cairo.LinearGradient(0, 0, w, h)
    fundo.add_color_stop_rgb(0, 0.97, 0.98, 1)
    fundo.add_color_stop_rgb(1, 0.92, 0.93, 1)
    ctx.set_source(fundo)
    ctx.paint()
    # Bolhas decorativas discretas
    for (bx, by, br, a) in ((1080, 90, 160, 0.10), (1150, 560, 220, 0.08), (90, 600, 140, 0.06)):
        ctx.arc(bx, by, br, 0, 2 * math.pi)
        ctx.set_source_rgba(*AZUL_1, a)
        ctx.fill()
    simbolo(ctx, 210, 90, 120, (0.96, 0.97, 1))
    x = 340
    avanço = texto(ctx, x, 250, "Tutor", 112, TINTA)
    texto(ctx, x + avanço, 250, "ON", 112, AZUL_1)
    texto(ctx, x, 320, "Seu tutor de faculdade, online 24h", 40, (0.25, 0.30, 0.40), cairo.FONT_WEIGHT_NORMAL)
    linhas = ["Pistas e perguntas-guia, sem entregar a resposta.",
              "Engenharia e Ciência da Computação"]
    for i, l in enumerate(linhas):
        texto(ctx, 96, 450 + i * 52, l, 34, (0.30, 0.34, 0.45), cairo.FONT_WEIGHT_NORMAL)
    # Selo "online"
    ctx.arc(110, 560 - 12 + 2, 9, 0, 2 * math.pi)
    ctx.set_source_rgb(*VERDE)
    ctx.fill()
    texto(ctx, 130, 562, "online agora", 28, (0.13, 0.55, 0.30))
    s.write_to_png(str(DESTINO / "previa.png"))


def main() -> None:
    DESTINO.mkdir(parents=True, exist_ok=True)
    (DESTINO / "logo.svg").write_text(SVG, encoding="utf-8")
    icone(32, "favicon-32.png")
    icone(180, "apple-touch-icon.png", 0.10, (1, 1, 1))
    icone(192, "icone-192.png", 0.08, (1, 1, 1))
    icone(512, "icone-512.png", 0.08, (1, 1, 1))
    previa()
    print("Marca gravada em", DESTINO)


if __name__ == "__main__":
    main()
