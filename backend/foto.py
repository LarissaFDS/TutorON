"""Foto do papel -> texto que o aluno confere antes de perguntar.

Do papel para o prompt sem a IA entender errado (reunião de 21/10/2026):

1. Visão computacional antes da IA (Pillow): corrige a rotação da câmera (EXIF), corta a borda
   vazia em volta do papel, aumenta o contraste e gera recortes ampliados e sobrepostos da foto,
   de cima para baixo. A IA recebe a foto inteira (contexto e ordem) e os recortes (letra pequena e
   manuscrita) num único pedido, então nenhum canto da folha fica de fora e a cota gasta é 1.
2. A IA só transcreve: enunciado, tentativa do aluno, subtópicos (a, b, c…), assuntos, o que há em
   cada região da folha e o que ficou ilegível ou ambíguo, com a confiança da leitura.
3. O aluno vê essa leitura, corrige o que estiver errado e confirma. Só a versão confirmada vai
   para o tutor. A foto não é guardada no servidor.
"""
from __future__ import annotations

import base64
import binascii
import io
import re

from PIL import Image, ImageFilter, ImageOps

MAX_BYTES = 8 * 1024 * 1024
LADO_INTEIRA = 1600
LADO_RECORTE = 1400
SOBREPOSICAO = 0.18

CAMPOS_TEXTO = ("enunciado", "tentativa")
TIPOS = ("enunciado", "tentativa", "enunciado_e_tentativa", "anotacoes", "outro")


class FotoInvalida(ValueError):
    pass


def decodificar(data_url: str) -> bytes:
    m = re.match(r"^data:image/(png|jpe?g|webp|gif|bmp);base64,(.+)$", data_url.strip(), re.S | re.I)
    if not m:
        raise FotoInvalida("Envie uma imagem JPG, PNG ou WEBP.")
    try:
        dados = base64.b64decode(m.group(2), validate=False)
    except (binascii.Error, ValueError):
        raise FotoInvalida("Imagem corrompida.") from None
    if len(dados) > MAX_BYTES:
        raise FotoInvalida("Imagem grande demais (máximo 8 MB).")
    return dados


def _abrir(dados: bytes) -> Image.Image:
    try:
        img = Image.open(io.BytesIO(dados))
        img.load()
    except Exception:  # Pillow lança vários tipos para arquivo que não é imagem
        raise FotoInvalida("Não consegui abrir a imagem.") from None
    if img.width * img.height > 40_000_000:
        raise FotoInvalida("Imagem com resolução grande demais.")
    img = ImageOps.exif_transpose(img)  # foto de celular "deitada"
    return img.convert("RGB")


def _cortar_borda(img: Image.Image) -> Image.Image:
    """Corta a margem sem conteúdo (mesa, borda branca) para o papel ocupar a imagem toda."""
    cinza = ImageOps.autocontrast(img.convert("L"), cutoff=2)
    # Tinta = pixel bem mais escuro que o papel. Um leve blur une letras e ignora ruído.
    tinta = cinza.filter(ImageFilter.MinFilter(5)).point(lambda p: 255 if p < 110 else 0)
    caixa = tinta.getbbox()
    if not caixa:
        return img
    x0, y0, x1, y1 = caixa
    if (x1 - x0) * (y1 - y0) < 0.15 * img.width * img.height:
        return img  # pouco conteúdo detectado: não arrisca cortar demais
    m = int(0.03 * max(img.size))
    return img.crop((max(0, x0 - m), max(0, y0 - m), min(img.width, x1 + m), min(img.height, y1 + m)))


def _realcar(img: Image.Image) -> Image.Image:
    img = ImageOps.autocontrast(img, cutoff=1)
    return img.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=3))


def _reduzir(img: Image.Image, lado: int) -> Image.Image:
    if max(img.size) <= lado:
        return img
    escala = lado / max(img.size)
    return img.resize((round(img.width * escala), round(img.height * escala)), Image.LANCZOS)


def _jpeg(img: Image.Image) -> bytes:
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=88, optimize=True)
    return buf.getvalue()


def recortes(img: Image.Image) -> list[Image.Image]:
    """Faixas horizontais sobrepostas (folha em pé) ou grade 2x2 (folha deitada)."""
    w, h = img.size
    if h >= w:
        n = 2 if h < 1.4 * w else 3
        alto = h / (n - (n - 1) * SOBREPOSICAO)
        passo = alto * (1 - SOBREPOSICAO)
        return [img.crop((0, round(i * passo), w, min(h, round(i * passo + alto)))) for i in range(n)]
    if w < 1.4 * h:
        mw, mh = w / 2, h / 2
        ox, oy = SOBREPOSICAO * mw, SOBREPOSICAO * mh
        return [img.crop((round(max(0, x - ox)), round(max(0, y - oy)), round(min(w, x + mw + ox)), round(min(h, y + mh + oy))))
                for y in (0, mh) for x in (0, mw)]
    n = 3
    largo = w / (n - (n - 1) * SOBREPOSICAO)
    passo = largo * (1 - SOBREPOSICAO)
    return [img.crop((round(i * passo), 0, min(w, round(i * passo + largo)), h)) for i in range(n)]


def preparar(dados: bytes) -> dict:
    """Imagem inteira + recortes ampliados, já em JPEG, e o que foi feito (para o registro)."""
    original = _abrir(dados)
    papel = _realcar(_cortar_borda(original))
    partes = [_jpeg(_reduzir(r, LADO_RECORTE)) for r in recortes(papel)]
    return {"inteira": _jpeg(_reduzir(papel, LADO_INTEIRA)), "recortes": partes,
            "info": {"original": list(original.size), "papel": list(papel.size), "recortes": len(partes)}}


def _lista(v, limite: int = 12) -> list[str]:
    if not isinstance(v, list):
        return []
    return [str(x).strip()[:400] for x in v if str(x).strip()][:limite]


def normalizar(dados: dict) -> dict:
    """Leitura da IA num formato fixo, mesmo que ela omita campos ou mande tipos errados."""
    leitura = {c: str(dados.get(c) or "").strip()[:6000] for c in CAMPOS_TEXTO}
    leitura["legivel"] = bool(dados.get("legivel", bool(leitura["enunciado"] or leitura["tentativa"])))
    leitura["tipo"] = dados.get("tipo") if dados.get("tipo") in TIPOS else "outro"
    leitura["subtopicos"] = _lista(dados.get("subtopicos"))
    leitura["assuntos"] = _lista(dados.get("assuntos"), 8)
    leitura["duvidas"] = _lista(dados.get("duvidas"))
    regioes = dados.get("regioes") if isinstance(dados.get("regioes"), list) else []
    leitura["regioes"] = [{"onde": str(r.get("onde", ""))[:30], "conteudo": str(r.get("conteudo", ""))[:300]}
                          for r in regioes if isinstance(r, dict)][:8]
    confianca = str(dados.get("confianca", "")).lower()
    leitura["confianca"] = confianca if confianca in ("alta", "media", "baixa") else "baixa"
    if leitura["duvidas"] and leitura["confianca"] == "alta":
        leitura["confianca"] = "media"  # dúvida listada não combina com confiança alta
    if not leitura["legivel"]:
        leitura["confianca"] = "baixa"
    return leitura


def texto_confirmado(enunciado: str, tentativa: str, subtopicos: list[str]) -> str:
    """O que vai para o tutor depois que o aluno conferiu a leitura."""
    partes = []
    if enunciado.strip():
        partes += ["Enunciado (lido da foto e conferido pelo aluno):", enunciado.strip()]
    if subtopicos:
        partes += ["Subtópicos:"] + [f"- {s}" for s in subtopicos]
    if tentativa.strip():
        partes += ["Tentativa do aluno no papel:", tentativa.strip()]
    return "\n".join(partes)[:8000]
